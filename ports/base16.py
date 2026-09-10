"""tinted-theming schemes: base16 and base24 (spec 0.11 YAML), and tinted8 (styling spec 0.2, as tinty 0.34 reads it)."""

import palette as p
from ports._lib import HEADER, REPO, Out, ink, selection, tints, ui_colors
from ports._palettes import role_name

META = {
    "id": "base16",
    "name": "Base16 / Base24 / Tinted8",
    "category": "Palettes",
    "homepage": "https://github.com/tinted-theming/home",
    "enable": {
        "where": "tinty, or any tinted-theming builder",
        "code": 'd="$(tinty config --data-dir-path)/custom-schemes/base16"\n'
        'mkdir -p "$d" && cp base16/{slug}.yaml "$d/"\n'
        "tinty apply base16-{slug}",
        "lang": "sh",
    },
    "notes": "Base16, Base24 and Tinted8 schemes. In base16 and base24 the accent slots follow the terminal colors, "
    "so keywords stay burnt orange and strings avocado, but their templates show functions in denim and classes "
    "in harvest gold. Tinted8 sets every syntax and UI color by name, so its templates use the editor themes' "
    "colors. The Tinted8 files use the key names tinty 0.34 reads.",
}

AUTHOR = f"oddurs ({REPO})"
DATA_DIR = "~/.local/share/tinted-theming/tinty"  # tinty's default; `tinty config --data-dir-path` prints yours


def slots(f):
    """base0X → role. Grounds run base → text_hi; accents keep base16's terminal hues
    (08 red, 0A yellow, 0B green, 0C cyan, 0D blue, 0E magenta), which is where this
    palette already puts them: burnt orange is the magenta, so keywords (0E) stay orange."""
    return {
        "base00": "base",
        "base01": "surface0",                          # lighter background: status bars, line numbers
        "base02": "surface2" if f.dark else "surface1",  # selection, as in every other port
        "base03": "overlay1",                          # comments
        "base04": "subtext0",                          # dark foreground
        "base05": "text",
        "base06": "text_hi",
        "base07": "text_hi",                           # no brighter step in the palette
        "base08": "red",                               # variables, tags, deletions; ANSI red
        "base09": "red_hi",                            # numbers, constants, booleans
        "base0A": "yellow",                            # classes, search; ANSI yellow
        "base0B": "green",                             # strings, insertions
        "base0C": "sage",                              # support, regex; ANSI cyan
        "base0D": "denim",                             # functions, headings; ANSI blue
        "base0E": "orange",                            # keywords, storage; ANSI magenta
        "base0F": "clay",                              # deprecated, embedded tags
    }


BASE24 = {
    "base10": "mantle",    # darker background
    "base11": "crust",     # darkest background
    "base12": "red_hi",    # bright red
    "base13": "yellow_hi",  # bright yellow
    "base14": "green_hi",  # bright green
    "base15": "sage_hi",   # bright cyan
    "base16": "denim_hi",  # bright blue
    "base17": "orange_hi",  # bright magenta
}


def scheme(f, system):
    mapping = slots(f) | (BASE24 if system == "base24" else {})
    palette = "\n".join(
        f'  {slot}: "{f.colors[role]}" # {role} ({role_name(f, role)})' for slot, role in mapping.items()
    )
    return (
        f"# {HEADER}\n"
        f'system: "{system}"\nname: "{f.name}"\nauthor: "{AUTHOR}"\n'
        f'variant: "{"dark" if f.dark else "light"}"\npalette:\n{palette}\n'
    )


# ── Tinted8 ────────────────────────────────────────────────────────────────
# The palette: black and white are the anchors (the ground and the text in a dark scheme,
# the other way round in a light one); -dim and -bright step away from and toward the text.
def tinted8_palette(f):
    if f.dark:
        anchors = {
            "black": f.base, "black-bright": f.surface1, "black-dim": f.mantle,
            "white": f.text, "white-bright": f.text_hi, "white-dim": f.subtext1,
            "gray": f.overlay1, "gray-bright": f.overlay2, "gray-dim": f.overlay0,
        }
    else:
        anchors = {
            "black": f.text, "black-bright": f.subtext1, "black-dim": f.text_hi,
            "white": f.base, "white-bright": ui_colors(f)["paper"], "white-dim": f.mantle,
            "gray": f.overlay1, "gray-bright": f.overlay0, "gray-dim": f.overlay2,
        }
    # Magenta is burnt orange here, as in every terminal port; brown is terracotta.
    hues = {"red": "red", "green": "green", "yellow": "yellow", "blue": "denim", "magenta": "orange",
            "cyan": "sage", "orange": "orange"}
    accents = {}
    for name, role in hues.items():
        accents[name] = f.colors[role]
        accents[f"{name}-bright"] = f.colors[f"{role}_hi"]
    return {**anchors, **accents, "brown": f.clay}


# tinted8 syntax key → Subway Seat syntax role (palette.SYNTAX) or color role. A key set here also
# decides its unset descendants, so parents come first and children that differ are set too.
TINTED8_SYNTAX = [
    ("comment", "comment"),
    ("punctuation.definition.comment", "comment"),
    ("constant", "constant"),
    ("constant.numeric", "number"),
    ("constant.language", "boolean"),
    ("constant.character", "string.escape"),
    ("entity.name", "variable"),
    ("entity.name.function", "function"),
    ("entity.name.class", "type"),
    ("entity.name.type", "type"),
    ("entity.name.namespace", "namespace"),
    ("entity.name.tag", "tag"),
    ("entity.name.label", "decorator"),
    ("entity.name.section", "heading"),
    ("entity.other", "variable"),
    ("entity.other.attribute-name", "attribute"),
    ("entity.other.inherited-class", "type"),
    ("invalid", "invalid"),
    ("invalid.deprecated", "clay"),
    ("keyword", "keyword"),
    ("keyword.operator", "operator"),
    ("markup", "text"),
    ("markup.bold", "strong"),
    ("markup.italic", "emphasis"),
    ("markup.heading", "heading"),
    ("markup.link", "link"),
    ("markup.list", "keyword"),
    ("markup.quote", "quote"),
    ("markup.raw", "code"),
    ("markup.inserted", "green"),
    ("markup.deleted", "red_hi"),
    ("markup.changed", "yellow"),
    ("meta", "text"),
    ("meta.annotation", "decorator"),
    ("punctuation", "punctuation"),
    ("punctuation.definition.string", "string"),
    ("punctuation.section", "punctuation"),
    ("storage", "storage"),
    ("string", "string"),
    ("string.regexp", "regexp"),
    ("string.interpolated", "string.escape"),
    ("support", "function"),
    ("support.class", "type"),
    ("support.type", "type.builtin"),
    ("support.constant", "constant"),
    ("support.function.builtin", "function.builtin"),
    ("support.variable", "variable.builtin"),
    ("variable", "variable"),
    ("variable.language", "variable.builtin"),
    ("variable.parameter", "parameter"),
    ("variable.other.property", "property"),
]


def tinted8_ui(f):
    """UI colors, with the key names tinty 0.34 (tinted-builder 0.16) reads. The styling spec's
    draft has since renamed a few (global.normal.background for global.background.normal, and
    so on); the schemes in tinted-theming/schemes still use these."""
    c = ui_colors(f)
    d = f.dark
    t = tints(f)
    line = f.surface0 if d else f.surface1
    return {
        "accent": {"normal": f.orange},
        "border": {"normal": line},
        # normal is the app chrome, dark the recessed surface, light the raised one
        "chrome": {
            "background": {"normal": f.mantle, "dark": f.crust, "light": c["paper"]},
            "foreground": {"normal": f.subtext1, "dark": f.subtext0, "light": f.text},
        },
        "cursor": {
            "normal": {"background": f.yellow if d else f.orange, "foreground": ink(f)},
            "muted": {"background": f.overlay1, "foreground": f.base},
        },
        "deprecated": f.clay,
        "global": {
            "background": {"normal": f.base, "dark": f.mantle, "light": c["paper"]},
            "foreground": {"normal": f.text, "dark": f.subtext1, "light": f.text_hi},
        },
        "gutter": {"background": f.base, "foreground": f.overlay1},
        "highlight": {
            "button": {"background": f.surface1 if d else f.surface0, "foreground": f.text_hi},
            "line": {"background": f.surface0 if d else f.mantle, "foreground": f.yellow if d else f.orange},
            "search": {"background": t["search"], "foreground": f.text_hi},
            "text": {
                "background": f.surface1 if d else f.surface0, "foreground": f.text,
                "active-background": selection(f), "active-foreground": f.text_hi,
            },
        },
        "indent-guide": {"background": f.surface1 if d else f.surface0, "active-background": f.overlay0},
        "link": {"normal": {"background": f.base, "foreground": f.denim}},
        "selection": {
            "background": selection(f), "foreground": f.text_hi,
            "inactive-background": f.surface1 if d else f.surface0,
        },
        "status": {"error": f.red_hi if d else f.red, "info": f.denim, "success": f.green, "warning": f.yellow},
        "tooltip": {"background": c["paper"], "foreground": f.text},
        "whitespace": {"foreground": f.overlay0},
    }


def _yaml_map(d, indent):
    lines = []
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{indent}{k}:")
            lines += _yaml_map(v, indent + "  ")
        else:
            lines.append(f'{indent}{k}: "{v}"')
    return lines


def tinted8(f):
    color = {role: f.syntax(role)[0] for role in p.SYNTAX} | f.colors
    style = f.name.removeprefix("Subway Seat").strip() or "Walnut"
    lines = [
        f"# {HEADER}",
        "scheme:",
        '  system: "tinted8"',
        "  supports:",
        '    styling-spec: "0.2.0"',
        f'  author: "{AUTHOR}"',
        f'  name: "{f.name}"',
        f'  slug: "{f.slug}"',
        '  family: "Subway Seat"',
        f'  style: "{style}"',
        f'  description: "{f.blurb}"',
        f'variant: "{"dark" if f.dark else "light"}"',
        "palette:",
        *(f'  {k}: "{v}"' for k, v in tinted8_palette(f).items()),
        "syntax:",
        *(f'  {k}: "{color[role]}" # {role}' for k, role in TINTED8_SYNTAX),
        "ui:",
        *_yaml_map(tinted8_ui(f), "  "),
    ]
    return "\n".join(lines) + "\n"


def build(flavors):
    outs = [
        Out(f"{system}/{f.slug}.yaml", scheme(f, system), flavor=f.id, lang="yaml",
            dest=f"{DATA_DIR}/custom-schemes/{system}/{f.slug}.yaml",
            how="tinty's data folder; `tinty config --data-dir-path` shows where yours is")
        for system in ("base16", "base24")
        for f in flavors
    ]
    outs += [
        Out(f"tinted8/{f.slug}.yaml", tinted8(f), flavor=f.id, lang="yaml",
            dest=f"{DATA_DIR}/custom-schemes/tinted8/{f.slug}.yaml",
            how="tinty's data folder; `tinty apply tinted8-…` needs templates that support Tinted8")
        for f in flavors
    ]
    return outs
