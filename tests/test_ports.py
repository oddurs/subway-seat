"""Every port: the META contract, the files it generates, and the build that writes them."""

import ast
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import pytest
from conftest import PORT_IDS

import build
import palette as p
from ports._lib import CATEGORIES, HEADER, LANGS, VERSION

ROOT = build.ROOT
FLAVOR_IDS = {f.id for f in p.FLAVORS}
KEBAB = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


# ── META ───────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("pid", PORT_IDS)
def test_meta_contract(pid, mods):
    mod = mods[pid]
    meta = mod.META
    for key in build.REQUIRED_META:
        assert isinstance(meta.get(key), str) and meta[key].strip(), f"META {key} is missing or empty"
    assert set(meta) <= build.KNOWN_META, f"unknown META keys {set(meta) - build.KNOWN_META}"
    assert KEBAB.fullmatch(meta["id"]), "id should be kebab-case"
    assert mod.__name__ == f"ports.{meta['id'].replace('-', '_')}", "the module name should be the id in snake_case"
    assert meta["category"] in CATEGORIES
    assert meta["homepage"].startswith("https://"), "homepage should be https"
    for key in ("enable", "auto"):
        if block := meta.get(key):
            assert {"where", "code", "lang"} <= set(block), f"{key} needs where, code and lang"
            allowed = {"where", "code", "lang", "file"} | ({"sh"} if key == "enable" else set())
            assert set(block) <= allowed, f"unknown {key} keys {set(block) - allowed}"
            assert block["lang"] in LANGS
            assert all(isinstance(v, str) and v.strip() for v in block.values())
    if "requires" in meta:
        assert isinstance(meta["requires"], str) and meta["requires"].strip(), "requires names a version or a prerequisite"
    if "detect" in meta:
        assert isinstance(meta["detect"], list) and meta["detect"], "detect is a non-empty list"
        assert all(isinstance(d, str) and d.strip() and "\t" not in d for d in meta["detect"])


def test_port_ids_unique(mods):
    names = [mod.META["name"] for mod in mods.values()]
    assert len(set(PORT_IDS)) == len(PORT_IDS)
    assert len(set(names)) == len(names), "two ports share a display name"


# Ports whose "turn it on" step is legitimately the same for every flavor.
SAME_ENABLE_FOR_ALL = {"termux", "terminal-agents", "herdr", "aichat", "obsidian", "lsd"}


@pytest.mark.parametrize("pid", PORT_IDS)
def test_enable_code_formats_for_every_flavor(pid, mods):
    enable = mods[pid].META.get("enable")
    if not enable:
        pytest.skip("no enable step")
    codes = set()
    for f in p.FLAVORS:
        for key in ("code", "sh", "file"):
            if key in enable:
                enable[key].format(**build.vars_for(f))  # a stray { or an unknown field fails here
        codes.add(enable["code"].format(**build.vars_for(f)))
    if pid not in SAME_ENABLE_FOR_ALL:
        assert len(codes) == len(p.FLAVORS), "every flavor should get its own enable line"


# ── Generated files ────────────────────────────────────────────────────────
# Ports where a shared file covers every flavor and a flavor-specific file is an extra.
PARTIAL_FLAVOR_FILES = {
    "obsidian": "one theme holds both modes; the Tunnel snippet deepens its dark mode",
    "opencode": "the Walnut and Tunnel themes pair with Enamel for light mode",
}


@pytest.mark.parametrize("pid", PORT_IDS)
def test_outputs_well_formed(pid, outs):
    port_outs = outs[pid]
    assert port_outs, "build() returned nothing"
    paths = [o.path for o in port_outs]
    assert len(set(paths)) == len(paths), "two outputs share a path"
    for o in port_outs:
        rel = Path(o.path)
        assert not rel.is_absolute() and ".." not in rel.parts, o.path
        assert o.content, f"{o.path} is empty"
        assert o.flavor is None or o.flavor in FLAVOR_IDS, o.path
        assert o.lang in LANGS, o.path
        assert o.dest is None or (isinstance(o.dest, str) and o.dest.strip()), o.path
        assert o.how is None or (isinstance(o.how, str) and o.how.strip()), o.path
        assert not (o.append and o.dest is None), f"{o.path} is appended but has no dest"
        if isinstance(o.content, str):
            assert "\r" not in o.content, f"{o.path} has a carriage return"
    flavored = {o.flavor for o in port_outs if o.flavor}
    if flavored and pid not in PARTIAL_FLAVOR_FILES:
        assert flavored == FLAVOR_IDS, f"files for {sorted(FLAVOR_IDS - flavored)} are missing"


def shell_parses(shell: str, content: str) -> subprocess.CompletedProcess:
    return subprocess.run([shell, "-n"], input=content, capture_output=True, text=True, check=False)


SHELLS = {".sh": "bash", ".bash": "bash", ".zsh": "zsh", ".fish": "fish"}


@pytest.mark.parametrize("pid", PORT_IDS)
def test_structured_outputs_parse(pid, rendered):
    """build.check() already ran in render_port; this adds shell syntax checks."""
    files, _ = rendered[0][pid]
    for path, body in files.items():
        if isinstance(body, bytes):
            continue
        build.check(path, body)
        rel = Path(path)
        shell = SHELLS.get(rel.suffix) or ("bash" if rel.parent.name in {"bin", "scripts"} else None)
        if shell and body.startswith("#!") and "fish" in body.split("\n", 1)[0]:
            shell = "fish"
        if not shell or not shutil.which(shell):
            continue
        result = shell_parses(shell, body)
        assert result.returncode == 0, f"{shell} -n dist/{path}: {result.stderr}"


# Strict JSON and plain text can't carry a comment; .svg files are image assets.
HEADER_EXEMPT = {".json", ".md", ".txt", ".alfredappearance", ".svg"}


@pytest.mark.parametrize("pid", PORT_IDS)
def test_text_outputs_carry_header(pid, outs):
    """Every file whose format has comments says where it came from. Strict JSON can't."""
    missing = [
        o.path
        for o in outs[pid]
        if isinstance(o.content, str)
        and Path(o.path).suffix.lower() not in HEADER_EXEMPT
        and Path(o.path).name != "LICENSE"
        and not Path(o.path).name.startswith(".")  # packaging dotfiles such as .vscodeignore
        and HEADER not in o.content
    ]
    assert not missing, f"no HEADER in {missing}"


def all_outputs_digest() -> str:
    h = hashlib.sha256()
    for pid, mod in build.discover().items():
        for o in mod.build(p.FLAVORS):
            h.update(f"{pid}/{o.path}\0{o.flavor}\0{o.dest}\0{o.how}\0{o.lang}\0{o.append}\0".encode())
            h.update(o.content if isinstance(o.content, bytes) else o.content.encode())
    return h.hexdigest()


def test_build_is_deterministic():
    assert all_outputs_digest() == all_outputs_digest()


def test_build_is_deterministic_across_hash_seeds():
    code = "import sys; sys.path.insert(0, 'tests'); from test_ports import all_outputs_digest; print(all_outputs_digest())"
    digests = {
        subprocess.run(
            [sys.executable, "-c", code],
            cwd=ROOT,
            env={**os.environ, "PYTHONHASHSEED": seed},
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        for seed in ("0", "1", "12345")
    }
    assert len(digests) == 1


def test_committed_dist_is_current():
    """dist/, the site tokens and README match a fresh build. Run ./build.py and commit if this fails."""
    result = subprocess.run(
        [sys.executable, "build.py", "--check"], cwd=ROOT, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stdout[-3000:] + result.stderr[-2000:]


@pytest.mark.xfail(
    strict=False,
    reason="Some ports still give prose as a dest. Flip to a plain test once every package has merged.",
)
def test_build_has_no_warnings(rendered):
    _, warnings = rendered
    assert not warnings, "\n".join(warnings)


def test_manifest_matches_ports(entries, outs):
    data = json.loads(build.manifest(entries))
    ids = [e["id"] for e in data["ports"]]
    assert ids == PORT_IDS, "the manifest lists ports in category, then name order"
    assert data["version"] == VERSION
    assert [f["id"] for f in data["flavors"]] == [f.id for f in p.FLAVORS]
    for e in data["ports"]:
        assert [f["path"] for f in e["files"]] == [f"{e['id']}/{o.path}" for o in outs[e["id"]]]
        if e["enable"]:
            assert set(e["enable"]) == FLAVOR_IDS


# ── install.tsv ────────────────────────────────────────────────────────────
def install_records() -> dict[str, list[str]]:
    """Record layouts from install_table()'s docstring, e.g. {"file": ["<id>", "<flavor|*>", …]}."""
    records = {}
    for line in build.install_table.__doc__.splitlines():
        m = re.match(r"\s*([a-z]+)\s+(<.*)$", line)
        if m:
            layout = m.group(2).split("  # ")[0]  # drop the trailing comment
            records[m.group(1)] = re.findall(r"<[^>]+>", layout)
    return records


def test_install_tsv_parses(entries, files):
    """dist/install.tsv matches the record layouts install_table() documents."""
    records = install_records()
    assert "file" in records and "detect" in records, "install_table()'s docstring lists the record layouts"
    table = build.install_table(entries)
    assert table.endswith("\n")
    seen = set()
    for n, line in enumerate(table.splitlines(), 1):
        if line.startswith("#"):
            continue
        kind, *fields = line.split("\t")
        assert kind in records, f"line {n}: unknown record {kind!r}"
        assert len(fields) == len(records[kind]), f"line {n}: {kind} has {len(fields)} fields, not {records[kind]}"
        for token, value in zip(records[kind], fields, strict=True):
            if token == "<id>":
                ids = FLAVOR_IDS if kind == "flavor" else set(entries)
                assert value in ids, f"line {n}: unknown id {value!r}"
            elif token == "<flavor>":
                assert value in FLAVOR_IDS, f"line {n}: unknown flavor {value!r}"
            elif token == "<flavor|*>":
                assert value in FLAVOR_IDS | {"*"}, f"line {n}: unknown flavor {value!r}"
            elif token == "<src under dist/>" and value:
                assert value in files, f"line {n}: {value} isn't a generated file"
            elif token == "<link|append>":
                assert value in ("link", "append"), f"line {n}: mode {value!r}"
        seen.add(kind)
    assert "file" in seen


# ── Spelling, hex and version hygiene ──────────────────────────────────────
# en-GB spellings to catch; matched at the start of a word, so "AccentRed" isn't "centre".
BRITISH = re.compile(
    r"(?<![A-Za-z])([Cc]olour\w*|[Ff]avour\w*|[Bb]ehaviour\w*|[Ff]lavour\w*|[Cc]entre[sd]?\b|[Ll]icence[sd]?\b|"
    r"[Aa]rtefacts?\b|[Cc]atalogue[sd]?\b|[Gg]rey\b|"
    r"(?:[Cc]ustom|[Oo]rgan|[Rr]ecogn|[Ss]tandard|[Nn]ormal|[Ii]nitial)is(?:e[sd]?|ing|ations?)\b)"
)
# Names an app defines, which must stay as the app spells them.
APP_IDENTIFIERS = [
    "display-panes-active-colour",  # tmux
    "display-panes-colour",  # tmux
    "clock-mode-colour",  # tmux
    "cursor-colour",  # tmux
    "colourful",  # eza
    "read_colours",  # bottom
    "write_colours",  # bottom
    "Current line background colour",  # Notepad++ style names
    "Selected text colour",
    "Bad brace colour",
    "Caret colour",
    "Edge colour",
    "Actions.Grey",  # JetBrains icon color keys
    "Objects.Grey",
]


def british(text: str) -> list[str]:
    for name in APP_IDENTIFIERS:
        text = text.replace(name, "")
    return BRITISH.findall(text)


def strings_in(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in strings_in(v)]
    if isinstance(value, list | tuple):
        return [s for v in value for s in strings_in(v)]
    return []


@pytest.mark.parametrize("pid", PORT_IDS)
def test_us_spelling(pid, mods, outs):
    found = {}
    for text in strings_in(mods[pid].META):
        if hits := british(text):
            found["META"] = hits
    for o in outs[pid]:
        texts = [o.how or "", o.dest or ""] + ([o.content] if isinstance(o.content, str) else [])
        if hits := [h for t in texts for h in british(t)]:
            found[o.path] = sorted(set(hits))
    assert not found, f"use US spelling (color, center, …): {found}"


DOCS = [
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "AGENTS.md",
    "docs/RELEASE.md",
    "site/README.md",
]


@pytest.mark.parametrize("doc", DOCS)
def test_docs_use_us_spelling(doc):
    path = ROOT / doc
    if not path.exists():
        pytest.skip(f"{doc} doesn't exist")
    prose = re.sub(r"`[^`\n]*`", "", path.read_text(encoding="utf-8"))  # code spans name app identifiers
    assert not british(prose), doc


# #RRGGBB, #RRGGBBAA and CSS #RGB; "#123-CD-456" (a Notepad++ style name) isn't a color.
HEX_LITERAL = re.compile(r"#(?:[0-9A-Fa-f]{8}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Za-z-])")
# Pure black and white, and black overlays, aren't palette colors.
ALLOWED_HEX = re.compile(r"#(000000([0-9A-Fa-f]{2})?|FFFFFF)", re.IGNORECASE)


def docstring_nodes(tree: ast.AST) -> set[int]:
    nodes = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Module | ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
                nodes.add(id(first.value))
    return nodes


def test_no_hex_literals_in_ports():
    """Colors come from palette roles and _lib derivations, never from a hex typed into a port."""
    found = []
    for path in sorted((ROOT / "ports").glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        docs = docstring_nodes(tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docs:
                found += [
                    f"{path.name}:{node.lineno} {m}"
                    for m in HEX_LITERAL.findall(node.value)
                    if not ALLOWED_HEX.fullmatch(m)
                ]
    assert not found, "hand-picked hex in ports/: " + ", ".join(found)


def test_version_single_source(files):
    """VERSION comes from pyproject.toml; every generated manifest carries it."""
    for path in sorted((ROOT / "ports").glob("*.py")):
        if path.name == "_lib.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "VERSION" for t in node.targets
            ):
                pytest.fail(f"{path.name}:{node.lineno} defines its own VERSION; import it from ports._lib")

    seen: dict[str, str] = {}
    for path, body in files.items():
        name = Path(path).name
        if isinstance(body, bytes):
            if name.endswith(".vsix"):
                with zipfile.ZipFile(io.BytesIO(body)) as z:
                    seen[path] = json.loads(z.read("extension/package.json"))["version"]
            continue
        if name in {"manifest.json", "package.json", "plugin.json"}:
            data = json.loads(body)
            if isinstance(data, dict) and "version" in data:
                seen[path] = data["version"]
        elif name in {"extension.toml", "pyproject.toml"}:
            data = tomllib.loads(body)
            seen[path] = data.get("version") or data["project"]["version"]
        elif name == "plugin.xml":
            seen[path] = ET.fromstring(body).findtext("version")
        elif m := re.search(r"^(?:;; Version:| \* @version) (\S+)$", body, re.MULTILINE):  # Emacs, Discord
            seen[path] = m.group(1)
    wrong = {path: v for path, v in seen.items() if v != VERSION}
    assert not wrong, f"expected {VERSION}: {wrong}"
    ports_with_version = {path.split("/", 1)[0] for path in seen}
    expected = {"vscode", "claude-code", "zed", "jetbrains", "emacs", "chrome", "firefox", "pygments"}
    assert expected <= ports_with_version, f"no version found for {expected - ports_with_version}"
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert re.search(rf"^## \[{re.escape(VERSION)}\]", changelog, re.MULTILINE), f"CHANGELOG has no ## [{VERSION}]"


# ── README, site tokens and the CLI ────────────────────────────────────────
def test_readme_tables_current(entries):
    text = build.README.read_text(encoding="utf-8")
    for name in ("flavors", "accents", "ports"):
        assert f"<!-- {name}:start -->" in text, f"README lost its {name} markers"
    assert build.fill_markers(text, build.readme_tables(entries)) == text, "run ./build.py"


def test_site_tokens_current():
    for name, body in build.site_tokens().items():
        assert (build.SITE_THEME / name).read_text(encoding="utf-8") == body, f"site/src/theme/{name}: run ./build.py"


@pytest.fixture
def scratch_dist(tmp_path, monkeypatch):
    """Point build.py at a copy of the committed manifest in a temporary dist/."""
    dist = tmp_path / "dist"
    dist.mkdir()
    shutil.copy(ROOT / "dist" / "manifest.json", dist / "manifest.json")
    readme = tmp_path / "README.md"
    shutil.copy(build.README, readme)
    monkeypatch.setattr(build, "DIST", dist)
    monkeypatch.setattr(build, "SITE_THEME", tmp_path / "theme")
    monkeypatch.setattr(build, "README", readme)
    return dist


def run_main(monkeypatch, *args: str) -> None:
    monkeypatch.setattr(sys, "argv", ["build.py", *args])
    build.main()


def test_only_preserves_manifest(scratch_dist, monkeypatch):
    before = [e["id"] for e in json.loads((scratch_dist / "manifest.json").read_text(encoding="utf-8"))["ports"]]
    run_main(monkeypatch, "--only", "ghostty,windows_terminal")
    after = [e["id"] for e in json.loads((scratch_dist / "manifest.json").read_text(encoding="utf-8"))["ports"]]
    assert after == before, "--only should keep every other port in the manifest, keyed by id"
    assert (scratch_dist / "ghostty" / "README.md").exists()
    assert not (scratch_dist / "vscode").exists(), "--only wrote a port it wasn't asked for"


def test_stale_cleanup_spares_files(scratch_dist, monkeypatch):
    (scratch_dist / "old-port").mkdir()
    (scratch_dist / "old-port" / "theme.conf").write_text("x", encoding="utf-8")
    (scratch_dist / "notes.txt").write_text("hand-placed", encoding="utf-8")
    run_main(monkeypatch)
    assert not (scratch_dist / "old-port").exists(), "a directory no port owns is removed"
    assert (scratch_dist / "notes.txt").read_text(encoding="utf-8") == "hand-placed", "loose files are left alone"
    assert (scratch_dist / "install.tsv").exists()


def test_cli_list_and_unknown_port():
    listed = subprocess.run(
        [sys.executable, "build.py", "--list"], cwd=ROOT, capture_output=True, text=True, check=True
    )
    assert f"{len(PORT_IDS)} ports" in listed.stdout
    unknown = subprocess.run(
        [sys.executable, "build.py", "--only", "no-such-port", "--no-manifest"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert unknown.returncode != 0
    assert "unknown port: no-such-port" in unknown.stderr
