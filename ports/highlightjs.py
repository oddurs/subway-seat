from ports._lib import HEADER, Out, selection, tints
from ports._palettes import css_decls

META = {
    "id": "highlightjs",
    "name": "highlight.js",
    "category": "Palettes",
    "homepage": "https://highlightjs.org",
    "enable": {
        "where": "your page's <head>, in place of a stock highlight.js theme",
        "code": '<link rel="stylesheet" href="{slug}.css">',
        "lang": "xml",
    },
    "auto": {
        "where": "your page's <head>, in place of a stock highlight.js theme",
        "code": '<link rel="stylesheet" href="subway-seat-auto.css">\n'
        "<!-- Enamel while the system is light, Subway Seat (Walnut) while it's dark -->",
        "lang": "xml",
    },
    "notes": "A highlight.js stylesheet per flavor, using the same syntax colors as the editor themes, and "
    "subway-seat-auto.css, which follows the system's light or dark setting. In diffs, added and removed "
    "lines sit on green and red grounds and hunk headers are denim.",
}

# (selectors, syntax or color role)
RULES = [
    (".hljs-comment", "comment"),
    (".hljs-quote", "quote"),
    (".hljs-doctag, .hljs-meta, .hljs-meta .hljs-keyword", "decorator"),
    (".hljs-meta .hljs-string", "string"),
    (".hljs-keyword, .hljs-template-tag", "keyword"),
    (".hljs-operator", "operator"),
    (".hljs-punctuation, .hljs-tag", "punctuation"),
    # .hljs-attr is JSON/YAML keys, which the editor themes color like functions.
    (".hljs-title, .hljs-title.function_, .hljs-title.function_.invoke__, .hljs-attr", "function"),
    (".hljs-built_in", "function.builtin"),
    (".hljs-string, .hljs-code", "string"),
    (".hljs-char.escape_", "string.escape"),
    (".hljs-regexp", "regexp"),
    (".hljs-number", "number"),
    (".hljs-literal, .hljs-symbol, .hljs-variable.constant_, .hljs-formula", "constant"),
    (".hljs-title.class_, .hljs-title.class_.inherited__", "type"),
    (".hljs-type", "type.builtin"),
    (".hljs-variable, .hljs-template-variable, .hljs-subst", "variable"),
    (".hljs-variable.language_", "variable.builtin"),
    (".hljs-params", "parameter"),
    (".hljs-property, .hljs-attribute", "property"),
    (".hljs-name, .hljs-selector-tag", "tag"),
    (".hljs-selector-id, .hljs-selector-class, .hljs-selector-attr, .hljs-selector-pseudo", "attribute"),
    (".hljs-section", "heading"),
    (".hljs-bullet", "keyword"),
    (".hljs-emphasis", "emphasis"),
    (".hljs-strong", "strong"),
]

LAYOUT = """pre code.hljs { display: block; overflow-x: auto; padding: 1em; }
code.hljs { padding: 3px 5px; }
.hljs-addition, .hljs-deletion { display: inline-block; width: 100%; } /* diff lines as full-width bands */"""


def colors(f):
    """Every rule that depends on the flavor."""
    t = tints(f)
    rules = "\n".join(f"{sel} {{ {css_decls(f, key)} }}" for sel, key in RULES)
    return f""".hljs {{ color: {f.text}; background: {f.base}; }}
.hljs::selection, .hljs ::selection {{ color: {f.text_hi}; background: {selection(f)}; }}

{rules}
.hljs-link {{ color: {f.denim}; text-decoration: underline; }}

/* Diffs: a diff line is one token, so it takes green or red_hi on its tint.
   highlight.js marks hunk headers as meta and file headers as comments. */
.hljs-addition {{ color: {f.green}; background: {t['add']}; }}
.hljs-deletion {{ color: {f.red_hi}; background: {t['del']}; }}
.language-diff .hljs-meta {{ color: {f.denim}; font-style: normal; }}
.language-diff .hljs-comment {{ color: {f.text_hi}; font-style: normal; font-weight: bold; }}"""


def stylesheet(f):
    return f"/* {HEADER} */\n/* {f.name} for highlight.js */\n\n{LAYOUT}\n\n{colors(f)}\n"


def auto_stylesheet(light, dark):
    night = "\n".join(f"  {line}" if line else "" for line in colors(dark).splitlines())
    return (
        f"/* {HEADER} */\n/* Subway Seat for highlight.js, following the system: {light.name} when it's light, "
        f"{dark.name} when it's dark. */\n\n{LAYOUT}\n\n{colors(light)}\n\n"
        f"@media (prefers-color-scheme: dark) {{\n{night}\n}}\n"
    )


def build(flavors):
    by = {f.id: f for f in flavors}
    how = "in your site's stylesheets"
    outs = [
        Out(f"{f.slug}.css", stylesheet(f), flavor=f.id, dest=f"styles/highlightjs/{f.slug}.css", lang="css", how=how)
        for f in flavors
    ]
    outs.append(Out("subway-seat-auto.css", auto_stylesheet(by["enamel"], by["walnut"]),
                    dest="styles/highlightjs/subway-seat-auto.css", lang="css", how=how))
    return outs
