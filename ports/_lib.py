"""Shared contract and helpers for ports.

A port is a module in ports/ (no leading underscore) that defines:

    META = {
        "id": "ghostty",                # dist/<id>/, URL slug
        "name": "Ghostty",              # display name
        "category": "Terminals",        # see CATEGORIES
        "homepage": "https://ghostty.org",
        "enable": {                     # how to switch it on, per flavor
            "where": "~/.config/ghostty/config",
            "code": "theme = {name}",   # formatted with the Flavor (name, slug, snake, id)
            "lang": "conf",
        },
        "notes": "One or two sentences shown on the site.",
    }

    def build(flavors) -> list[Out]

Optional META keys:

    "auto": {"where", "code", "lang"}   # how to follow the OS light/dark setting
                                        # (code is shown as-is, not formatted)
    "requires": "Ghostty 1.3+"          # the oldest version the files work with, or
                                        # a prerequisite ("Raycast Pro")
    "detect": ["ghostty", "/Applications/Ghostty.app"]
                                        # the app is installed if any command is on
                                        # PATH or any path (~, /, $VAR) exists
    enable["sh"]                        # a POSIX-shell line when `code` is fish
    enable["file"]                      # the config file `code` can be appended to
                                        # (between MARK_START/MARK_END) by install.sh;
                                        # leave it out when turning on needs a person

`build` receives every Flavor and returns files. A file tied to one flavor sets
`flavor=f.id`; a file covering all of them (a VS Code extension, an auto
light/dark theme) leaves it None. `dest` is a path (`~/…`, `/…`, `%APPDATA%\…`)
the file is copied to, or None; anything that isn't a path (an import dialog,
"packaged in the extension") goes in `how`. `append=True` means the file's text
is added to the file at `dest`; wrap it in MARK_START/MARK_END so it can be
removed again. `lang` is one of LANGS below (the site's highlighter).

Shared helpers live here: `pair(f)`, `family_of(f)`, `ink(f)`, `selection(f)`, `tints(f)`, the layering
system (`resolve`, `solid`, `ui_colors`), `ANSI_NAMES`, `zip_bytes` and VERSION
(read from pyproject.toml, the one place the version lives).
"""

import io
import re
import tomllib
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, NotRequired, TypedDict

import palette as p

ROOT = Path(__file__).resolve().parent.parent
VERSION: str = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]

HEADER = "Subway Seat — generated from palette.py by build.py. Edit the palette, not this file."
REPO = "https://github.com/oddurs/subway-seat"
SITE = "https://oddurs.github.io/subway-seat"

CATEGORIES = [
    "Terminals",
    "Editors",
    "Agents",
    "Shell & prompt",
    "CLI & TUI",
    "Apps",
    "Desktop",
    "Palettes",
]


# Languages the site knows how to highlight (see site/src/lib/highlight.ts).
Lang = Literal[
    "conf", "fish", "sh", "toml", "lua", "json", "xml", "yaml", "css", "scss", "ini", "vim",
    "elisp", "kdl", "ron", "typescript", "js", "python", "go", "nushell", "powershell", "text",
]
LANGS: tuple[str, ...] = Lang.__args__


class Enable(TypedDict):
    where: str
    code: str  # formatted with the Flavor: {name} {slug} {snake} {id}
    lang: Lang
    sh: NotRequired[str]  # POSIX-shell equivalent of a fish `code`, formatted the same way
    file: NotRequired[str]  # config file install.sh may append `code` to, e.g. "~/.config/ghostty/config"


class Auto(TypedDict):
    where: str
    code: str  # shown as-is (it names every flavor itself)
    lang: Lang
    file: NotRequired[str]


class Meta(TypedDict):
    id: str
    name: str
    category: str
    homepage: str
    notes: str
    enable: NotRequired[Enable]
    auto: NotRequired[Auto]
    requires: NotRequired[str]
    detect: NotRequired[list[str]]


@dataclass(frozen=True, slots=True)
class Out:
    path: str
    content: str | bytes
    flavor: str | None = None
    dest: str | None = None
    lang: Lang = "text"
    append: bool = False
    how: str | None = None  # prose install step when there's no path to copy to


# Markers around appended blocks, so uninstalling is deleting one block.
MARK_START = "# >>> subway-seat >>>"
MARK_END = "# <<< subway-seat <<<"


ANSI_NAMES = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")


def pair(f):
    """The (dark, light) flavors of f's own family.

    For themes that follow the OS setting: a port must never name a flavor id,
    or it breaks the moment a second family exists."""
    fam = p.FAMILY[f.family]
    return (f if f.dark else fam.default), fam.light


def family_of(f):
    return p.FAMILY[f.family]


def ink(f):
    """Text that sits on an accent fill (buttons, badges, cursor text)."""
    return f.crust if f.dark else f.base


def selection(f):
    """The one solid selection color for apps without alpha."""
    return f.surface2 if f.dark else f.surface1


def zip_bytes(files: dict[str, str | bytes], compress: bool = True) -> bytes:
    """A deterministic zip: fixed timestamps, Unix attributes, stable order."""
    buf = io.BytesIO()
    method = zipfile.ZIP_DEFLATED if compress else zipfile.ZIP_STORED
    with zipfile.ZipFile(buf, "w", method) as z:
        for name, body in files.items():
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = method
            info.create_system = 3
            info.external_attr = 0o644 << 16
            z.writestr(info, body if isinstance(body, bytes) else body.encode("utf-8"))
    return buf.getvalue()


def h(color):
    """#RRGGBB → RRGGBB."""
    return color.lstrip("#")


def rgb(color):
    return p.hex_to_rgb(color)


def rgb_floats(color):
    return tuple(round(v / 255, 6) for v in p.hex_to_rgb(color))


# ── Tinted backgrounds (diffs, search, diagnostics) ────────────────────────
def tints(f):
    """Semantic tinted grounds.

    Diff grounds shift hue, not lightness: on dark flavors the accent is mixed
    into crust (so a green line stays about as dark as base), on Enamel into
    white. Every syntax color keeps at least ~3:1 on a line tint and comments
    stay readable on word emphasis, so highlighted code on top of a diff still
    reads. `*_dim` is for diffs shown faded (rejected or collapsed hunks)."""
    g = "crust" if f.dark else "#FFFFFF"
    return {
        "add": f.mix("green", g, 0.22 if f.dark else 0.26),
        "add_emph": f.mix("green", g, 0.34 if f.dark else 0.40),
        "add_dim": f.mix("green", g, 0.14 if f.dark else 0.16),
        "del": f.mix("red", g, 0.26 if f.dark else 0.20),
        "del_emph": f.mix("red", g, 0.40 if f.dark else 0.32),
        "del_dim": f.mix("red", g, 0.17 if f.dark else 0.12),
        "chg": f.mix("yellow", g, 0.16 if f.dark else 0.26),
        # kept clearly apart from the search tint, so a match inside a diff reads as a match
        "chg_emph": f.mix("yellow", g, 0.26 if f.dark else 0.32),
        "info": f.mix("denim", "base", 0.14),
        "hint": f.mix("sage", "base", 0.14),
        "search": f.mix("yellow", "base", 0.30),
        "search_cur": f.mix("orange", "base", 0.50),
    }


# ── UI layering (VS Code, Zed, JetBrains, the site) ────────────────────────
# One chrome ground (mantle), crust only as 1px grooves, popovers raised on
# "paper", and every hover/selection a translucent layer of text so it sits
# right on any ground. Levels are (dark %, light %).
INK = {"L1": (4, 4), "L2": (8, 7), "L3": (12, 10), "L4": (16, 13), "L5": (24, 20), "EDGE": (12, 14)}


def ui_colors(f):
    """The flavor's roles plus the derived `paper` and `shadow`."""
    c = dict(f.colors)
    if f.dark:
        c["shadow"] = p.blend(c["crust"], "#000000", 0.5)
        c["paper"] = c["surface0"]
    else:
        c["shadow"] = c["text"]
        c["paper"] = p.blend("#FFFFFF", c["base"], 0.5)
    return c


def resolve(expr, f):
    """Resolve a layering expression for flavor f:
    `role`, `role@L3` / `role@35` (alpha), `mix(a,b,t)`, `transparent`, or `#hex`."""
    c = ui_colors(f)
    expr = expr.strip()
    if expr == "transparent":
        return "#00000000"
    if expr.startswith("#"):
        return expr
    m = re.fullmatch(r"mix\((#?\w+),\s*(#?\w+),\s*([\d.]+)\)", expr)
    if m:
        a, b, t = m.groups()
        return p.blend(c.get(a, a), c.get(b, b), float(t))
    m = re.fullmatch(r"(\w+)@(\w+)", expr)
    if m:
        role, level = m.groups()
        pct = INK[level][0 if f.dark else 1] if level in INK else int(level)
        if role not in c:
            raise ValueError(f"unknown role {role!r} in layering expression {expr!r}")
        return p.alpha(c[role], pct / 100)
    if expr not in c:
        raise ValueError(f"unknown role or expression {expr!r}")
    return c[expr]


def solid(expr, f, over="base"):
    """A layering expression flattened onto a ground, for apps without alpha."""
    value = resolve(expr, f)
    if len(value) == 9:  # #RRGGBBAA
        a = int(value[7:], 16) / 255
        return p.blend(value[:7], resolve(over, f), a)
    return value


# ── TextMate scopes (VS Code tokenColors, .tmTheme, Sublime) ───────────────
# Order matters: later, equally-specific rules win.
SCOPES = [
    ("variable, variable.other.readwrite, variable.other.constant, meta.definition.variable", "variable"),
    ("punctuation, meta.brace, punctuation.definition.tag, punctuation.separator, punctuation.terminator, punctuation.accessor", "punctuation"),
    ("keyword.operator, storage.type.function.arrow, punctuation.separator.key-value", "operator"),
    ("keyword, keyword.control, keyword.other, storage.modifier, keyword.operator.new, keyword.operator.expression, keyword.operator.logical.python, keyword.operator.wordlike, keyword.control.import, keyword.control.from", "keyword"),
    ("storage, storage.type", "storage"),
    ("entity.name.function, support.function, variable.function, meta.function-call entity.name.function, entity.name.function.macro, support.function.any-method", "function"),
    ("support.function.builtin, support.function.console", "function.builtin"),
    ("string, string.quoted, string.template, punctuation.definition.string, string.unquoted", "string"),
    ("constant.character.escape, constant.other.placeholder, punctuation.definition.template-expression, punctuation.section.embedded", "string.escape"),
    ("string.regexp", "regexp"),
    ("constant.numeric, keyword.other.unit", "number"),
    ("constant.language, support.constant, variable.other.enummember, constant.other.caps, constant.other.color", "constant"),
    ("constant.language.boolean", "boolean"),
    ("entity.name.type, entity.name.class, entity.name.struct, entity.name.enum, entity.name.interface, entity.other.inherited-class, support.class, support.type, entity.name.type.class", "type"),
    ("support.type.primitive, support.type.builtin, storage.type.primitive, keyword.type, storage.type.built-in, storage.type.numeric.go, storage.type.string.go, storage.type.boolean.go, storage.type.byte.go, storage.type.error.go", "type.builtin"),
    ("variable.language, variable.parameter.language, variable.language.this, variable.language.self, variable.language.special.self, variable.parameter.function.language.special.self", "variable.builtin"),
    ("variable.parameter, meta.parameter variable, variable.parameter.function", "parameter"),
    ("variable.other.property, variable.other.object.property, support.variable.property, meta.object-literal.key, variable.other.member, entity.name.variable.field, support.type.property-name.css", "property"),
    ("entity.name.namespace, entity.name.module, entity.name.type.module, entity.name.package, storage.modifier.package, storage.modifier.import", "namespace"),
    ("entity.name.tag, entity.name.tag.css", "tag"),
    ("entity.other.attribute-name, entity.other.attribute-name.class.css", "attribute"),
    ("meta.decorator, entity.name.function.decorator, punctuation.decorator, meta.annotation, variable.annotation, punctuation.definition.annotation, storage.type.annotation, entity.name.label, entity.name.function.preprocessor, keyword.control.directive", "decorator"),
    ("support.type.property-name.json, support.type.property-name.toml, entity.name.tag.yaml, keyword.key.toml, support.type.property-name", "function"),
    ("comment, punctuation.definition.comment, string.comment", "comment"),
    ("markup.heading, entity.name.section, markup.heading punctuation.definition.heading", "heading"),
    ("markup.underline.link, string.other.link, markup.link", "link"),
    ("markup.inline.raw, markup.fenced_code, markup.raw, markup.inline.raw.string.markdown", "code"),
    ("markup.italic", "emphasis"),
    ("markup.bold", "strong"),
    ("markup.quote", "quote"),
    ("punctuation.definition.list.begin.markdown, punctuation.definition.list", "keyword"),
    ("invalid, invalid.illegal", "invalid"),
]


def scope_rules(f):
    """(scope, hex, styles) for every TextMate rule, resolved for flavor f."""
    for scope, role in SCOPES:
        color, styles = f.syntax(role)
        yield scope, color, styles
    yield "markup.inserted, meta.diff.header.to-file, punctuation.definition.inserted", f.green, set()
    yield "markup.deleted, meta.diff.header.from-file, punctuation.definition.deleted", f.red_hi, set()
    yield "markup.changed, punctuation.definition.changed", f.yellow, set()
    yield "meta.diff.range, meta.diff.header", f.denim, set()
    yield "markup.strikethrough", f.overlay1, {"strikethrough"}
