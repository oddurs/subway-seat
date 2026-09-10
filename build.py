#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate every Subway Seat port into dist/, plus the site's tokens and the README table.

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
import re
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
from ports._lib import CATEGORIES, LANGS, SITE, Out

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE_THEME = ROOT / "site" / "src" / "theme"
README = ROOT / "README.md"
START, END = "<!-- ports:start -->", "<!-- ports:end -->"
REQUIRED_META = ("id", "name", "category", "homepage", "notes")


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
    if (enable := meta.get("enable")) and enable.get("lang") not in LANGS:
        raise SystemExit(f"✗ {where}: enable.lang {enable.get('lang')!r} is not one of LANGS")


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
        elif suffix in {".plist", ".tmtheme", ".itermcolors", ".xccolortheme"}:
            plistlib.loads(content.encode())
        elif suffix in {".xml", ".icls", ".svg"}:
            ET.fromstring(content)
        elif suffix in {".yml", ".yaml"} and yaml is not None:
            yaml.safe_load(content)
        elif suffix == ".py":
            ast.parse(content)
    except Exception as e:
        raise SystemExit(f"✗ dist/{rel} does not parse: {e}") from e


def vars_for(f) -> dict:
    return {"name": f.name, "slug": f.slug, "snake": f.snake, "id": f.id}


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
        check(key, out.content)
        files[key] = out.content
        listed.append({
            "path": key,
            "flavor": out.flavor,
            "dest": out.dest,
            "lang": out.lang,
            "append": out.append,
            "binary": isinstance(out.content, bytes),
        })
    enable = meta.get("enable")
    entry = {
        **{k: v for k, v in meta.items() if k != "enable"},
        "enable": {f.id: {**enable, "code": enable["code"].format(**vars_for(f))} for f in p.FLAVORS}
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
        f"# Subway Seat for {entry['name']}",
        "",
        entry["notes"],
        "",
        f"[{entry['name']}]({entry['homepage']}) · [All ports and previews]({SITE}/ports/{entry['id']}/)",
        "",
        "## Files",
        "",
        "| Flavor | File | Where it goes |",
        "|---|---|---|",
    ]
    for file in entry["files"]:
        flavor = by_flavor[file["flavor"]].name if file["flavor"] else "All three"
        name = file["path"].split("/", 1)[1]
        dest = (file["dest"] or "").replace("|", "\\|")
        if file["append"]:
            dest = f"append to {dest}"
        lines.append(f"| {flavor} | [`{name}`]({name.replace(' ', '%20')}) | {dest} |")
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
            if len(codes) == 1:
                break
    lines += ["", "Generated by `build.py` from `palette.py`. Edit the port in `ports/`, not these files.", ""]
    return "\n".join(lines)


# ── Site tokens and README table ───────────────────────────────────────────
def camel(key: str) -> str:
    head, *rest = key.split("_")
    return head + "".join(w.title() for w in rest)


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
        "accentRoles": {camel(k): v for k, v in p.ACCENT_ROLES.items()},
        "flavors": [
            {
                "id": f.id,
                "name": f.name,
                "slug": f.slug,
                "dark": f.dark,
                "blurb": f.blurb,
                "colors": {camel(r): f.colors[r] for r in p.ROLES},
                "ansi": [camel(r) for r in f.ansi_roles],
            }
            for f in p.FLAVORS
        ],
    }
    return {
        "tokens.stylex.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n\n'
        f"export const color = stylex.defineVars({{\n{walnut}\n}});\n",
        "flavors.ts": f'{header}\nimport * as stylex from "@stylexjs/stylex";\n'
        f'import {{ color }} from "./tokens.stylex";\n\n{themes}\n',
        "palette.json": json.dumps(data, indent=2) + "\n",
    }


def readme_with_table(entries: dict) -> str | None:
    text = README.read_text(encoding="utf-8")
    if START not in text:
        return None
    rows = []
    for category in CATEGORIES:
        ports_in = sorted((e for e in entries.values() if e["category"] == category), key=lambda e: e["name"].lower())
        if ports_in:
            links = ", ".join(f"[{e['name']}](dist/{e['id']})" for e in ports_in)
            rows.append(f"| **{category}** ({len(ports_in)}) | {links} |")
    table = "| | |\n|---|---|\n" + "\n".join(rows)
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{table}\n{END}{tail}"


def manifest(entries: dict) -> str:
    return (
        json.dumps(
            {
                "flavors": [{"id": f.id, "name": f.name, "slug": f.slug, "dark": f.dark} for f in p.FLAVORS],
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

    if yaml is None:
        print("  note: PyYAML isn't installed, so YAML output isn't parse-checked (use `uv run build.py`)")

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
    if not args.only:
        outputs.update({SITE_THEME / name: body for name, body in site_tokens().items()})
        if (readme := readme_with_table(entries)) is not None:
            outputs[README] = readme

    port_dirs = {DIST / pid for pid in mods}

    if args.check:
        problems = [f"changed  {path.relative_to(ROOT)}" for path, body in outputs.items() if not same(path, body)]
        for d in sorted(port_dirs):
            if d.exists():
                extra = {x for x in d.rglob("*") if x.is_file() and "__pycache__" not in x.parts} - set(outputs)
                problems += [f"extra    {x.relative_to(ROOT)}" for x in sorted(extra)]
        if not args.only:
            owned = {d.name for d in port_dirs} | {"manifest.json"}
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
        for stale in sorted(x for x in DIST.iterdir() if x.name not in {d.name for d in port_dirs} | {"manifest.json"}):
            if stale.is_dir():
                shutil.rmtree(stale)
                print(f"  removed stale dist/{stale.name}/")
            else:
                print(f"  note: dist/{stale.name} isn't generated by any port")
    print(f"{len(entries)} ports in dist/")


if __name__ == "__main__":
    main()
