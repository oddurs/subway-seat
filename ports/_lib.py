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

`build` receives every Flavor and returns files. A file tied to one flavor sets
`flavor=f.id`; a file covering all of them (a VS Code extension, an auto
light/dark theme) leaves it None. `dest` is where the user puts the file, shown
on the site; `lang` is the site's highlighter: conf, fish, toml, lua, json,
xml, yaml, css, ini, vim, elisp, sh, kdl, ron, typescript or text.
"""

from dataclasses import dataclass

import palette as p

HEADER = "Subway Seat — generated from palette.py by build.py. Edit the palette, not this file."
REPO = "https://github.com/oddurs/subway-seat"

CATEGORIES = [
    "Terminals",
    "Editors",
    "Agents",
    "Shell & prompt",
    "CLI & TUI",
    "Apps",
    "Palettes",
]


@dataclass
class Out:
    path: str
    content: str | bytes
    flavor: str | None = None
    dest: str | None = None
    lang: str = "text"
    append: bool = False


def h(color):
    """#RRGGBB → RRGGBB."""
    return color.lstrip("#")


def rgb(color):
    return p.hex_to_rgb(color)


def rgb_floats(color):
    return tuple(round(v / 255, 6) for v in p.hex_to_rgb(color))


# ── Tinted backgrounds (diffs, search, diagnostics) ────────────────────────
def tints(f):
    """Semantic tinted grounds, computed against the flavor's base."""
    k = 1.0 if f.dark else 0.85
    return {
        "add": f.mix("green", "base", 0.20 * k),
        "add_emph": f.mix("green", "base", 0.42 * k),
        "del": f.mix("red", "base", 0.22 * k),
        "del_emph": f.mix("red", "base", 0.46 * k),
        "chg": f.mix("yellow", "base", 0.14 * k),
        "chg_emph": f.mix("yellow", "base", 0.32 * k),
        "info": f.mix("denim", "base", 0.14 * k),
        "hint": f.mix("sage", "base", 0.14 * k),
        "search": f.mix("yellow", "base", 0.30 * k),
        "search_cur": f.mix("orange", "base", 0.50 * k),
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
    import re

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
        return p.alpha(c[role], pct / 100)
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
