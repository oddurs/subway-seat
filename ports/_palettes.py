"""Helpers shared by the palette, design-format and web-highlighter ports."""

import colorsys

import palette as p


def kebab(role):
    """text_hi → text-hi (CSS, SCSS, Tailwind, design tokens)."""
    return role.replace("_", "-")


def label(role):
    """Swatch name for design apps: "Walnut (base)"."""
    return f"{p.ROLE_NAMES[role]} ({role})"


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


def selection(f):
    return f.surface2 if f.dark else f.surface1


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
    ("Generic.Deleted", "red_hi"),
    ("Generic.Inserted", "green"),
    ("Generic.Error", "invalid"),
    ("Generic.Output", "subtext0"),
    ("Generic.Prompt", "keyword"),
    ("Generic.Traceback", "invalid"),
]


def token_styles(f):
    """(token path, style string) in Pygments/chroma syntax: "italic #967B5C".

    Both inherit bold/italic from the parent token, so a child that shouldn't
    have them gets an explicit "noitalic"/"nobold".
    """
    resolved = {}
    for path, key in TOKENS:
        color, st = style(f, key)
        parent = path.rpartition(".")[0]
        while parent and parent not in resolved:
            parent = parent.rpartition(".")[0]
        inherited = resolved.get(parent, set())
        resolved[path] = st
        words = [s for s in ("bold", "italic") if s in st]
        words += [f"no{s}" for s in ("bold", "italic") if s in inherited and s not in st]
        yield path, " ".join([*words, color])
