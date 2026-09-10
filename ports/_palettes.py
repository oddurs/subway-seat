"""Helpers shared by the palette, design-format and web-highlighter ports."""

import colorsys

import palette as p
from ports._lib import tints


def kebab(role):
    """text_hi → text-hi (CSS, SCSS, Tailwind, design tokens)."""
    return role.replace("_", "-")


def role_name(f, role):
    """What a role is called in flavor f. ROLE_NAMES is the dark reading (base is "Paneling",
    text "Parchment"); a light flavor's grounds and text run the other way, so there they get a
    plain name ("Enamel base"). Accents keep their names in every flavor."""
    if f.dark or role in p.ACCENTS:
        return p.ROLE_NAMES[role]
    return f"{f.id.title()} {role.replace('_', ' ')}"


def label(role, f):
    """Swatch name for design apps: "Paneling (base)", or "Enamel base" in a light flavor."""
    name = role_name(f, role)
    return name if name != p.ROLE_NAMES[role] else f"{name} ({role})"


# The diff tints from _lib.tints as named tokens, for the CSS, Sass, Tailwind and JSON ports.
DIFF = [
    ("diff-add", "add"), ("diff-add-emph", "add_emph"), ("diff-add-dim", "add_dim"),
    ("diff-del", "del"), ("diff-del-emph", "del_emph"), ("diff-del-dim", "del_dim"),
    ("diff-chg", "chg"), ("diff-chg-emph", "chg_emph"),
]


def diff_tokens(f):
    """{"diff-add": hex, …}: line and word grounds for added, removed and changed text."""
    t = tints(f)
    return {name: t[key] for name, key in DIFF}


def hsl(color):
    """#RRGGBB → (hue°, saturation %, lightness %), rounded."""
    r, g, b = (v / 255 for v in p.hex_to_rgb(color))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    return round(hue * 360), round(sat * 100), round(light * 100)


def hsv(color):
    """#RRGGBB → (hue, saturation, value), each 0..1."""
    return colorsys.rgb_to_hsv(*(v / 255 for v in p.hex_to_rgb(color)))


def style(f, key):
    """(hex, styles) for a syntax role ("keyword") or a color role ("green")."""
    return f.syntax(key) if key in p.SYNTAX else (f.colors[key], set())


def css_decls(f, key):
    """CSS declarations for a syntax or color role."""
    color, st = style(f, key)
    out = [f"color: {color};"]
    if "italic" in st:
        out.append("font-style: italic;")
    if "bold" in st:
        out.append("font-weight: bold;")
    return " ".join(out)


# ── Pygments-style token tree (Pygments and chroma share it) ────────────────
# (token path, syntax or color role). Chroma drops the dots: Name.Builtin → NameBuiltin.
TOKENS = [
    ("Text", "variable"),
    ("Error", "invalid"),
    ("Comment", "comment"),
    ("Comment.Hashbang", "comment"),
    ("Comment.Preproc", "decorator"),
    ("Keyword", "keyword"),
    ("Keyword.Constant", "constant"),
    ("Keyword.Type", "type.builtin"),
    ("Operator", "operator"),
    ("Operator.Word", "keyword"),
    ("Punctuation", "punctuation"),
    ("Name", "variable"),
    ("Name.Attribute", "attribute"),
    ("Name.Builtin", "function.builtin"),
    ("Name.Builtin.Pseudo", "variable.builtin"),
    ("Name.Class", "type"),
    ("Name.Constant", "constant"),
    ("Name.Decorator", "decorator"),
    ("Name.Entity", "string.escape"),
    ("Name.Exception", "type"),
    ("Name.Function", "function"),
    ("Name.Function.Magic", "function.builtin"),
    ("Name.Label", "decorator"),
    ("Name.Namespace", "namespace"),
    ("Name.Property", "property"),
    ("Name.Tag", "tag"),
    ("Name.Variable", "variable"),
    ("Name.Variable.Magic", "variable.builtin"),
    ("Literal.Date", "number"),
    ("Literal.String", "string"),
    ("Literal.String.Affix", "storage"),
    ("Literal.String.Escape", "string.escape"),
    ("Literal.String.Interpol", "string.escape"),
    ("Literal.String.Regex", "regexp"),
    ("Literal.String.Symbol", "constant"),
    ("Literal.Number", "number"),
    ("Generic.Heading", "heading"),
    ("Generic.Subheading", "heading"),
    ("Generic.Emph", "emphasis"),
    ("Generic.Strong", "strong"),
    ("Generic.Deleted", "red_hi"),     # the whole line is one token: red_hi on the del tint
    ("Generic.Inserted", "green"),     # green on the add tint
    ("Generic.Error", "invalid"),
    ("Generic.Output", "subtext0"),
    ("Generic.Prompt", "keyword"),
    ("Generic.Traceback", "invalid"),
]


# Diff lines get a ground as well as a color.
TOKEN_GROUNDS = {"Generic.Deleted": "del", "Generic.Inserted": "add"}


def token_styles(f):
    """(token path, style string) in Pygments/chroma syntax: "italic #967B5C".

    Both inherit bold/italic from the parent token, so a child that shouldn't
    have them gets an explicit "noitalic"/"nobold".
    """
    resolved = {}
    grounds = tints(f)
    for path, key in TOKENS:
        color, st = style(f, key)
        parent = path.rpartition(".")[0]
        while parent and parent not in resolved:
            parent = parent.rpartition(".")[0]
        inherited = resolved.get(parent, set())
        resolved[path] = st
        words = [s for s in ("bold", "italic") if s in st]
        words += [f"no{s}" for s in ("bold", "italic") if s in inherited and s not in st]
        if path in TOKEN_GROUNDS:
            words.append(f"bg:{grounds[TOKEN_GROUNDS[path]]}")
        yield path, " ".join([*words, color])
