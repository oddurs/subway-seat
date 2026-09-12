#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate every Subway Seat port into dist/, plus the site's tokens and the README tables.

    ./build.py                 # everything
    ./build.py --only vscode   # one or more ports (comma-separated); the manifest keeps the rest
    ./build.py --check         # build in memory and fail if anything on disk differs
    ./build.py --list          # show discovered ports

Each module in ports/ (see ports/_lib.py for the contract) returns its files for
every flavor. This script validates them, writes them to dist/<id>/ with a
generated README.md, checks that structured files parse, and records everything
in dist/manifest.json for the site and docs. Needs Python 3.12+; `uv run build.py`
also brings PyYAML so YAML output is checked.
"""

import argparse
import ast
import importlib
import io
import json
import pkgutil
import plistlib
import shutil
import sys
import tomllib
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

import palette as p
import ports
from ports._lib import CATEGORIES, LANGS, MARK_END, MARK_START, SITE, VERSION, Out

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE_THEME = ROOT / "site" / "src" / "theme"
README = ROOT / "README.md"
GLOBALS = ROOT / "site" / "src" / "app" / "globals.css"
REQUIRED_META = ("id", "name", "category", "homepage", "notes")
KNOWN_META = {*REQUIRED_META, "enable", "auto", "requires", "detect"}
# `dest` is a path; directions and prose belong in `how`.
NOT_A_PATH = ("→", "›", " e.g.", " or ", "`", "; ", "double-click", "packaged", "merged", "wherever", "anywhere")


# ── Discovery and validation ───────────────────────────────────────────────
def module_name(pid: str) -> str:
    return pid.replace("-", "_")


def validate_meta(mod) -> None:
    meta = getattr(mod, "META", None)
    where = mod.__name__
    if not isinstance(meta, dict):
        raise SystemExit(f"✗ {where}: missing META")
    if missing := [k for k in REQUIRED_META if not meta.get(k)]:
        raise SystemExit(f"✗ {where}: META is missing {', '.join(missing)}")
    if module_name(meta["id"]) != where.removeprefix("ports."):
        raise SystemExit(f"✗ {where}: META id {meta['id']!r} should match the file name")
    if meta["category"] not in CATEGORIES:
        raise SystemExit(f"✗ {where}: category {meta['category']!r} is not one of {CATEGORIES}")
    if unknown := set(meta) - KNOWN_META:
        raise SystemExit(f"✗ {where}: unknown META keys {sorted(unknown)} (see ports/_lib.py)")
    for key in ("enable", "auto"):
        block = meta.get(key)
        if block is None:
            continue
        if missing := [k for k in ("where", "code", "lang") if not block.get(k)]:
            raise SystemExit(f"✗ {where}: META {key} is missing {', '.join(missing)}")
        if block["lang"] not in LANGS:
            raise SystemExit(f"✗ {where}: {key}.lang {block['lang']!r} is not one of LANGS")
    if "detect" in meta and not (isinstance(meta["detect"], list) and all(isinstance(d, str) for d in meta["detect"])):
        raise SystemExit(f"✗ {where}: META detect should be a list of commands or paths")
    if "requires" in meta and not isinstance(meta["requires"], str):
        raise SystemExit(f"✗ {where}: META requires should be a string like 'Ghostty 1.3+'")


def sort_key(meta) -> tuple:
    return (CATEGORIES.index(meta["category"]), meta["name"].lower())


def discover() -> dict:
    mods = {}
    for info in pkgutil.iter_modules(ports.__path__):
        if info.name.startswith("_"):
            continue
        mod = importlib.import_module(f"ports.{info.name}")
        validate_meta(mod)
        if mod.META["id"] in mods:
            raise SystemExit(f"✗ duplicate port id {mod.META['id']!r}")
        mods[mod.META["id"]] = mod
    return dict(sorted(mods.items(), key=lambda kv: sort_key(kv[1].META)))


def load(pid: str):
    """Import one port by id, without importing the others."""
    try:
        mod = importlib.import_module(f"ports.{module_name(pid)}")
    except ModuleNotFoundError as e:
        if e.name != f"ports.{module_name(pid)}":
            raise
        raise SystemExit(f"unknown port: {pid} (expected ports/{module_name(pid)}.py)") from None
    validate_meta(mod)
    return mod


# ── Checks on generated content ────────────────────────────────────────────
def check(rel: str, content: str | bytes) -> None:
    """Parse structured files so a broken template fails the build."""
    if isinstance(content, bytes):
        return
    suffix = Path(rel).suffix.lower()
    try:
        if suffix in {".json", ".alfredappearance"}:
            json.loads(content)
        elif suffix == ".sublime-color-scheme":
            json.loads("\n".join(line for line in content.splitlines() if not line.lstrip().startswith("//")))
        elif suffix == ".toml":
            tomllib.loads(content)
        elif suffix in {".plist", ".tmtheme", ".itermcolors", ".xccolortheme", ".terminal"}:
            plistlib.loads(content.encode())
        elif suffix in {".xml", ".icls", ".svg"}:
            ET.fromstring(content)
        elif suffix in {".yml", ".yaml"}:
            if yaml is None:
                UNCHECKED_YAML.append(rel)
            else:
                yaml.safe_load(content)
        elif suffix == ".py":
            ast.parse(content)
    except Exception as e:
        raise SystemExit(f"✗ dist/{rel} does not parse: {e}") from e


WARNINGS: list[str] = []
UNCHECKED_YAML: list[str] = []  # YAML files written without PyYAML to parse them


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def vars_for(f) -> dict:
    return {"name": f.name, "slug": f.slug, "snake": f.snake, "id": f.id, "prefix": f.prefix}


# ── One port → files + manifest entry ─────────────────────────────────────
def render_port(mod) -> tuple[dict[str, str | bytes], dict]:
    meta = mod.META
    outs: list[Out] = mod.build(p.FLAVORS)
    files: dict[str, str | bytes] = {}
    listed = []
    flavor_ids = {f.id for f in p.FLAVORS}
    for out in outs:
        rel = Path(out.path)
        if rel.is_absolute() or ".." in rel.parts:
            raise SystemExit(f"✗ {meta['id']}: output path {out.path!r} must stay inside dist/{meta['id']}/")
        key = f"{meta['id']}/{rel.as_posix()}"
        if key in files:
            raise SystemExit(f"✗ {meta['id']}: two outputs write {out.path!r}")
        if out.flavor is not None and out.flavor not in flavor_ids:
            raise SystemExit(f"✗ {meta['id']}: unknown flavor {out.flavor!r} for {out.path!r}")
        if out.lang not in LANGS:
            raise SystemExit(f"✗ {meta['id']}: lang {out.lang!r} for {out.path!r} is not one of LANGS")
        if out.dest is not None and (
            ("/" not in out.dest and "\\" not in out.dest) or any(w in out.dest for w in NOT_A_PATH)
        ):
            raise SystemExit(f"✗ {meta['id']}: dest {out.dest!r} for {out.path!r} isn't a path; put directions in `how`")
        if out.append and isinstance(out.content, str) and MARK_START not in out.content:
            raise SystemExit(f"✗ {meta['id']}: appended file {out.path!r} should be wrapped in MARK_START/MARK_END")
        check(key, out.content)
        files[key] = out.content
        listed.append(
            {
                "path": key,
                "flavor": out.flavor,
                "dest": out.dest,
                "how": out.how,
                "lang": out.lang,
                "append": out.append,
                "binary": isinstance(out.content, bytes),
            }
        )
    enable = meta.get("enable")
    entry = {
        **{k: v for k, v in meta.items() if k != "enable"},
        "enable": {
            f.id: {k: v.format(**vars_for(f)) if k in ("code", "sh") else v for k, v in enable.items()}
            for f in p.FLAVORS
        }
        if enable
        else None,
        "files": listed,
    }
    readme = f"{meta['id']}/README.md"
    if readme not in files:
        files[readme] = port_readme(entry)
    return files, entry


def port_readme(entry: dict) -> str:
    """dist/<id>/README.md: what's here and how to switch it on, per flavor."""
    by_flavor = {f.id: f for f in p.FLAVORS}
    lines = [
        f"# Subway Seat {entry['name'].lower()}" if entry['id'] == 'wallpapers' else f"# Subway Seat for {entry['name']}",
        "",
        entry["notes"],
        "",
        f"[{entry['name']}]({entry['homepage']}) · [Previews and copy buttons]({SITE}/ports/{entry['id']}/)"
        + (f" · Needs {entry['requires']}" if entry.get("requires") else ""),
        "",
        "## Files",
        "",
        "| Flavor | File | Where it goes |",
        "|---|---|---|",
    ]
    for file in entry["files"]:
        flavor = by_flavor[file["flavor"]].name if file["flavor"] else "All three"
        name = file["path"].split("/", 1)[1]
        where = f"`{file['dest']}`" if file["dest"] else ""
        if file["append"]:
            where = f"add to the end of {where}"
        if file["how"]:
            where = f"{where}; {file['how']}" if where else file["how"]
        lines.append(f"| {flavor} | [`{name}`]({name.replace(' ', '%20')}) | {where.replace('|', '\\|')} |")
    if entry["enable"]:
        lines += ["", "## Turn it on", ""]
        codes = {e["code"] for e in entry["enable"].values()}
        for f in p.FLAVORS:
            enable = entry["enable"][f.id]
            if len(codes) > 1:
                lines.append(f"**{f.name}**, in {enable['where']}:")
            else:
                lines.append(f"In {enable['where']}:")
            lines += ["", f"```{enable['lang']}", enable["code"], "```", ""]
            if enable.get("sh"):
                lines += ["In bash or zsh:", "", "```sh", enable["sh"], "```", ""]
            if len(codes) == 1:
                break
    if auto := entry.get("auto"):
        lines += [
            "## Follow light and dark",
            "",
            f"In {auto['where']}:",
            "",
            f"```{auto['lang']}",
            auto["code"],
            "```",
            "",
        ]
    removals = []
    for file in entry["files"]:
        if file["append"] and file["dest"]:
            removals.append(f"- Delete the block between `{MARK_START}` and `{MARK_END}` in `{file['dest']}`.")
        elif file["dest"]:
            removals.append(f"- Delete `{file['dest']}`.")
    if removals:
        lines += ["## Uninstall", "", *dict.fromkeys(removals)]
        if entry["enable"]:
            lines.append("- Remove the line you added to turn it on.")
        lines.append("")
    lines += [
        f"Generated by `build.py` from `palette.py` (v{VERSION}). Edit the port in `ports/`, not these files.",
        "",
    ]
    return "\n".join(lines)


# ── Site tokens and README table ───────────────────────────────────────────
def camel(key: str) -> str:
    head, *rest = key.split("_")
    return head + "".join(w.title() for w in rest)


# The accents a light flavor paints its *art* in. A light flavor's accents are
# solved to carry small text on paper, so they come out dark and earthy — right
# for code, wrong for a supergraphic or a line diagram, which have no contrast
# floor to clear and just need to sing. Art in a light flavor therefore borrows
# its family's dark default, which is the same hue at the lightness the shape
# wants. Dark flavors already paint art in their own accents.
ART = ("red", "orange", "yellow", "green", "sage", "denim", "clay")


def page_ground(f) -> str:
    """The website's own canvas, a step beyond the theme's darkest ground.

    An editor fills the screen, so its `base` has to be comfortable to stare
    into. A web page is mostly margin, and the same value there reads heavier
    and more colored than it does behind code. So the site steps a little past
    `crust` on the dark flavors and a little past `base` on the light ones —
    a shade, not a different room: the page recedes, and the cards and mockups
    sitting on it are what carry the flavor."""
    if f.dark:
        return p.blend(f.crust, "#000000", 0.82)
    return p.blend("#FFFFFF", f.base, 0.3)


def art_colors(f) -> dict[str, str]:
    if f.dark:
        return {role: f.colors[role] for role in ART}
    # Part of the way toward the family's dark default, not all of it: enough to
    # lift the art off a pale ground, not so much that the page stops looking
    # like the flavor it is.
    vivid = p.FAMILY[f.family].default
    return {role: p.blend(vivid.colors[role], f.colors[role], 0.55) for role in ART}


def site_tokens() -> dict[str, str]:
    header = "// Generated by build.py from palette.py — edit the palette, not this file."
    walnut = "\n".join(f'  {camel(r)}: "{p.DEFAULT.colors[r]}",' for r in p.ROLES)
    themes = "\n\n".join(
        f"export const {f.id} = stylex.createTheme(color, {{\n"
        + "\n".join(f'  {camel(r)}: "{f.colors[r]}",' for r in p.ROLES)
        + "\n});"
        for f in p.FLAVORS
    )
    data = {
        "roles": [camel(r) for r in p.ROLES],
        "ground": [camel(r) for r in p.GROUND],
        "text": [camel(r) for r in p.TEXT],
        "accents": [camel(r) for r in p.ACCENTS],
        "roleNames": {camel(k): v for k, v in p.ROLE_NAMES.items()},
        "families": [
            {
                "id": fam.id,
                "name": fam.name,
                "blurb": fam.blurb,
                "lead": camel(fam.lead),
                "roleNames": {camel(k): v for k, v in fam.role_names.items()},
                "flavors": [f.id for f in fam.flavors],
                "default": fam.default.id,
                "light": fam.light.id,
            }
            for fam in p.FAMILIES
        ],
        "accentRoles": {camel(k): v for k, v in p.ACCENT_ROLES.items()},
        "roleUses": {camel(k): p.ROLE_USES[k] for k in p.ROLES},
        "flavors": [
            {
                "id": f.id,
                "family": f.family,
                "name": f.name,
                "slug": f.slug,
                "dark": f.dark,
                "blurb": f.blurb,
                "colors": {camel(r): f.colors[r] for r in p.ROLES},
                "art": {**{camel(r): v for r, v in art_colors(f).items()}, "page": page_ground(f)},
                "ansi": [camel(r) for r in f.ansi_roles],
            }
            for f in p.FLAVORS
        ],
    }
    art_default = "\n".join(f'  {camel(r)}: "{art_colors(p.DEFAULT)[r]}",' for r in ART)
    art_default += f'\n  page: "{page_ground(p.DEFAULT)}",'
    art_themes = "\n\n".join(
        f"export const {f.id} = stylex.createTheme(art, {{\n"
        + "\n".join(f'  {camel(r)}: "{art_colors(f)[r]}",' for r in ART)
        + f'\n  page: "{page_ground(f)}",'
        + "\n});"
        for f in p.FLAVORS
    )
    return {
        "art.stylex.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n\n'
        f"// Decorative colors: see build.py's ART note.\n"
        f"export const art = stylex.defineVars({{\n{art_default}\n}});\n",
        "art.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n'
        f'import {{ art }} from "./art.stylex";\n\n{art_themes}\n',
        "tokens.stylex.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n\n'
        f"export const color = stylex.defineVars({{\n{walnut}\n}});\n",
        "flavors.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n'
        f'import {{ color }} from "./tokens.stylex";\n\n{themes}\n',
        "palette.json": json.dumps(data, indent=2) + "\n",
    }


def globals_css() -> str:
    """The per-flavor rules in site/src/app/globals.css, one block per flavor.

    Hex is written lowercase here, and only here: it is the site's CSS
    convention (biome reformats anything else), while the palette itself and
    every generated theme stay uppercase.

    Hand-written CSS can't match a flavor id generically, so every rule that
    names one is generated here and a new family costs nothing."""
    ind = "  "
    first = p.FAMILIES[0].sign
    out = [f"{ind}:root {{", f"{ind}{ind}--ss-shadow: rgba(8, 5, 2, 0.55);",
           f"{ind}{ind}--ss-shadow-soft: rgba(8, 5, 2, 0.28);",
           *(f"{ind}{ind}--sign-{k}: {v.lower()};" for k, v in first.items()),
           *(f"{ind}{ind}--radius-{k}: {v};" for k, v in p.FAMILIES[0].shape.items()), f"{ind}}}"]
    for fam in p.FAMILIES[1:]:
        out += [f'{ind}html[data-family="{fam.id}"] {{',
                *(f"{ind}{ind}--sign-{k}: {v.lower()};" for k, v in fam.sign.items()),
                *(f"{ind}{ind}--radius-{k}: {v};" for k, v in fam.shape.items()), f"{ind}}}"]
    for f in p.FLAVORS:
        if not f.dark:
            shadow = p.blend(f.text, "#FFFFFF", 0.75)
            r, g, b = p.hex_to_rgb(shadow)
            out += [f'{ind}html[data-flavor="{f.id}"] {{',
                    f"{ind}{ind}--ss-shadow: rgba({r}, {g}, {b}, 0.2);",
                    f"{ind}{ind}--ss-shadow-soft: rgba({r}, {g}, {b}, 0.12);", f"{ind}}}"]
    out.append("")
    # The inverse of data-only: shown everywhere except its own flavor or family.
    # Lets a control render both of its states and let CSS pick, so it is correct
    # in the first painted frame rather than after React hydrates.
    unless = ",\n".join(
        f'{ind}html[data-flavor="{f.id}"] [data-unless="{f.id}"]' for f in p.FLAVORS
    ) + ",\n" + ",\n".join(
        f'{ind}html[data-family="{fam.id}"] [data-unless="{fam.id}"]' for fam in p.FAMILIES
    )
    out += [f"{unless} {{", f"{ind}{ind}display: none !important;", f"{ind}}}", ""]

    for attr, media in (("data-only", None), ("data-narrow-only", "@media (max-width: 720px)")):
        pad = ind + (ind if media else "")
        rules = ",\n".join(
            f'{pad}html:not([data-flavor="{f.id}"]) [{attr}="{f.id}"]' for f in p.FLAVORS
        )
        family_rules = ",\n".join(
            f'{pad}html:not([data-family="{fam.id}"]) [{attr}="{fam.id}"]' for fam in p.FAMILIES
        )
        block = f"{rules},\n{family_rules} {{\n{pad}{ind}display: none !important;\n{pad}}}"
        if media:
            out += [f"{ind}/* Wide tables show every flavor; phones show the one you're riding. */",
                    f"{ind}{media} {{", block, f"{ind}}}"]
        else:
            out += [f"{ind}/* Content written for one flavor or one family; the rest is hidden. */", block]
        out.append("")
    out.append(f"{ind}/* Shiki renders {p.DEFAULT.name} by default and carries the others as variables. */")
    for f in p.FLAVORS:
        if f.id == p.DEFAULT.id:
            continue
        out += [f'{ind}html[data-flavor="{f.id}"] .shiki-themes,',
                f'{ind}html[data-flavor="{f.id}"] .shiki-themes span {{',
                f"{ind}{ind}color: var(--shiki-{f.id}) !important;", f"{ind}}}",
                f'{ind}html[data-flavor="{f.id}"] .shiki-themes {{',
                f"{ind}{ind}background-color: var(--shiki-{f.id}-bg) !important;", f"{ind}}}"]
    return "\n".join(out)


def readme_tables(entries: dict) -> dict[str, str]:
    """The README's generated tables, by marker name (<!-- name:start --> … <!-- name:end -->)."""
    flavors = []
    for fam in p.FAMILIES:
        flavors += [f"**{fam.name}** — {fam.blurb}", "", "| | | |", "|---|---|---|"]
        flavors += [
            f"| **{f.name}** | `{f.id}` · {'dark' if f.dark else 'light'} | {f.blurb} |" for f in fam.flavors
        ]
        flavors.append("")
    flavors = flavors[:-1]
    accents = ["| Accent | Leads |", "|---|---|"] + [
        f"| {p.ROLE_NAMES[role]} | {leads} |" for role, leads in p.ACCENT_ROLES.items()
    ]
    ports_rows = ["| | |", "|---|---|"]
    for category in CATEGORIES:
        ports_in = sorted((e for e in entries.values() if e["category"] == category), key=lambda e: e["name"].lower())
        if ports_in:
            links = ", ".join(f"[{e['name']}](dist/{e['id']})" for e in ports_in)
            ports_rows.append(f"| **{category}** ({len(ports_in)}) | {links} |")
    return {"flavors": "\n".join(flavors), "accents": "\n".join(accents), "ports": "\n".join(ports_rows)}


def fill_markers(text: str, tables: dict[str, str], mark: str = "<!-- {} -->") -> str:
    """Replace what sits between each pair of markers; markers that aren't there are skipped.

    `mark` wraps the marker name, so the same mechanism works in Markdown
    (`<!-- x:start -->`) and in CSS (`/* x:start */`)."""
    for name, body in tables.items():
        start, end = mark.format(f"{name}:start"), mark.format(f"{name}:end")
        if start in text:
            head, rest = text.split(start, 1)
            _, tail = rest.split(end, 1)
            text = f"{head}{start}\n{body}\n{end}{tail}"
    return text


def readme_with_tables(entries: dict) -> str:
    return fill_markers(README.read_text(encoding="utf-8"), readme_tables(entries))


def esc(text: str) -> str:
    """One TSV field: backslash, tab and newline escaped for `printf '%b'`."""
    return text.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")


def install_table(entries: dict) -> str:
    """dist/install.tsv, what install.sh reads (no jq or Python needed). One record per line:

    version <x.y.z>
    family  <id>  <name>
    flavor  <id>  <name>  <slug>  <dark|light>  <family>
    color   <flavor>  <role>  <#hex>           # accents install.sh paints its own output with
    port    <id>  <name>  <category>  <requires>   # first record of each port, in site order
    detect  <id>  <command or path>
    file    <id>  <flavor|*>  <src under dist/>  <dest>  <link|append>
    how     <id>  <flavor|*>  <text>  <src under dist/>   # a step install.sh can only print
    enable  <id>  <flavor>  <config file>  <code>  <where>  <lang>  <sh>
    auto    <id>  <config file>  <code>  <where>  <lang>

    Fields are tab-separated and may be empty (an `enable` with no config file is printed as a
    step, not appended). Backslash, tab and newline are escaped for `printf '%b'`. `how` rows for
    files that only ship inside another artifact ("packaged in the extension") are left out.
    """
    rows = [
        "# Generated by build.py for install.sh. Tab-separated; fields escaped for printf %b.",
        f"version\t{VERSION}",
    ]
    for fam in p.FAMILIES:
        rows.append(f"family\t{fam.id}\t{esc(fam.name)}")
    for f in p.FLAVORS:
        rows.append(f"flavor\t{f.id}\t{f.name}\t{f.slug}\t{'dark' if f.dark else 'light'}\t{f.family}")
        rows += [
            f"color\t{f.id}\t{role}\t{f.colors[role]}"
            for role in ("yellow", "orange", "green", "red_hi", "denim", "sage")
        ]
    for e in sorted(entries.values(), key=sort_key):
        pid = e["id"]
        rows.append(f"port\t{pid}\t{esc(e['name'])}\t{esc(e['category'])}\t{esc(e.get('requires', ''))}")
        rows += [f"detect\t{pid}\t{esc(d)}" for d in e.get("detect", [])]
        for file in e["files"]:
            flavor = file["flavor"] or "*"
            if file["dest"]:
                mode = "append" if file["append"] else "link"
                rows.append(f"file\t{pid}\t{flavor}\t{esc(file['path'])}\t{esc(file['dest'])}\t{mode}")
            if file["how"] and not file["how"].lower().startswith(("packaged", "inside", "bundled", "included")):
                rows.append(f"how\t{pid}\t{flavor}\t{esc(file['how'])}\t{esc(file['path'])}")
        for fid, enable in (e["enable"] or {}).items():
            fields = (enable.get("file", ""), enable["code"], enable["where"], enable["lang"], enable.get("sh", ""))
            rows.append("\t".join(["enable", pid, fid, *map(esc, fields)]))
        if auto := e.get("auto"):
            fields = (auto.get("file", ""), auto["code"], auto["where"], auto["lang"])
            rows.append("\t".join(["auto", pid, *map(esc, fields)]))
    return "\n".join(rows) + "\n"


def manifest(entries: dict) -> str:
    return (
        json.dumps(
            {
                "version": VERSION,
                "flavors": [
                    {"id": f.id, "family": f.family, "name": f.name, "slug": f.slug, "dark": f.dark}
                    for f in p.FLAVORS
                ],
                "families": [
                    {"id": fam.id, "name": fam.name, "blurb": fam.blurb,
                     "flavors": [f.id for f in fam.flavors]}
                    for fam in p.FAMILIES
                ],
                "categories": CATEGORIES,
                "ports": sorted(entries.values(), key=sort_key),
            },
            indent=2,
        )
        + "\n"
    )


# ── Writing and checking ───────────────────────────────────────────────────
def as_bytes(content: str | bytes) -> bytes:
    return content if isinstance(content, bytes) else content.encode("utf-8")


def same(path: Path, content: str | bytes) -> bool:
    if not path.exists():
        return False
    disk, new = path.read_bytes(), as_bytes(content)
    if disk == new:
        return True
    # Zips: zlib builds compress identical input differently, so compare members.
    if zipfile.is_zipfile(io.BytesIO(new)) and zipfile.is_zipfile(io.BytesIO(disk)):
        with zipfile.ZipFile(io.BytesIO(new)) as a, zipfile.ZipFile(io.BytesIO(disk)) as b:
            return a.namelist() == b.namelist() and all(a.read(n) == b.read(n) for n in a.namelist())
    return False


def write(path: Path, content: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content, encoding="utf-8", newline="\n")
    if path.suffix in {".sh", ".fish"} or path.parent.name in {"bin", "scripts"}:
        path.chmod(0o755)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--only", help="comma-separated port ids")
    ap.add_argument("--list", action="store_true", help="show discovered ports")
    ap.add_argument("--check", action="store_true", help="fail if anything on disk differs from a fresh build")
    ap.add_argument("--no-manifest", action="store_true", help="write port files only (safe for parallel runs)")
    args = ap.parse_args()

    if args.only and not args.list:
        mods = {}
        for pid in args.only.split(","):
            mod = load(pid.strip())
            mods[mod.META["id"]] = mod
    else:
        mods = discover()

    if args.list:
        for pid, mod in mods.items():
            print(f"{mod.META['category']:<15} {pid:<22} {mod.META['name']}")
        print(f"{len(mods)} ports")
        return

    outputs: dict[Path, str | bytes] = {}
    entries = {}
    for pid, mod in mods.items():
        files, entries[pid] = render_port(mod)
        outputs.update({DIST / rel: body for rel, body in files.items()})
        if not args.check:
            print(f"  ✓ {pid:<22} {len(entries[pid]['files'])} files")

    manifest_path = DIST / "manifest.json"
    if args.only and manifest_path.exists():
        previous = {e["id"]: e for e in json.loads(manifest_path.read_text(encoding="utf-8"))["ports"]}
        entries = {**previous, **entries}
    if not args.no_manifest:
        outputs[manifest_path] = manifest(entries)
        outputs[DIST / "install.tsv"] = install_table(entries)
    if not args.only:
        outputs.update({SITE_THEME / name: body for name, body in site_tokens().items()})
        outputs[README] = readme_with_tables(entries)
        outputs[GLOBALS] = fill_markers(
            GLOBALS.read_text(encoding="utf-8"), {"flavors": globals_css()}, mark="  /* {} */"
        )

    port_dirs = {DIST / pid for pid in mods}
    for msg in WARNINGS:
        print(f"  ⚠ {msg}")
    if UNCHECKED_YAML:
        print(
            f"  ⚠ PyYAML isn't installed, so {len(UNCHECKED_YAML)} YAML files weren't parse-checked. "
            "Run `uv run build.py` (it brings PyYAML) or `pip install pyyaml`."
        )

    if args.check:
        problems = [f"changed  {path.relative_to(ROOT)}" for path, body in outputs.items() if not same(path, body)]
        for d in sorted(port_dirs):
            if d.exists():
                extra = {x for x in d.rglob("*") if x.is_file() and "__pycache__" not in x.parts} - set(outputs)
                problems += [f"extra    {x.relative_to(ROOT)}" for x in sorted(extra)]
        if not args.only:
            owned = {d.name for d in port_dirs} | {"manifest.json", "install.tsv"}
            problems += [f"extra    dist/{x.name}" for x in sorted(DIST.iterdir()) if x.name not in owned]
        if problems:
            print("\n".join(problems[:50]))
            sys.exit(f"✗ {len(problems)} file(s) differ from a fresh build. Run ./build.py and commit the result.")
        print(f"✓ dist/, the site tokens and README match a fresh build ({len(outputs)} files)")
        return

    for d in port_dirs:
        shutil.rmtree(d, ignore_errors=True)  # renamed outputs leave no stale files
    for path, body in outputs.items():
        write(path, body)
    if not args.only:
        for stale in sorted(
            x for x in DIST.iterdir() if x.name not in {d.name for d in port_dirs} | {"manifest.json", "install.tsv"}
        ):
            if stale.is_dir():
                shutil.rmtree(stale)
                print(f"  removed stale dist/{stale.name}/")
            else:
                print(f"  note: dist/{stale.name} isn't generated by any port")
    print(f"{len(entries)} ports in dist/")


if __name__ == "__main__":
    main()
