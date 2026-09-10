from ports._lib import HEADER, Out, tints
from ports._palettes import css_decls, selection

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
    "notes": "A highlight.js stylesheet per flavor, using the same syntax colors as the editor themes.",
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


def stylesheet(f):
    t = tints(f)
    rules = "\n".join(f"{sel} {{ {css_decls(f, key)} }}" for sel, key in RULES)
    return f"""/* {HEADER} */
/* {f.name} for highlight.js */

pre code.hljs {{ display: block; overflow-x: auto; padding: 1em; }}
code.hljs {{ padding: 3px 5px; }}

.hljs {{ color: {f.text}; background: {f.base}; }}
.hljs::selection, .hljs ::selection {{ color: {f.text_hi}; background: {selection(f)}; }}

{rules}
.hljs-link {{ color: {f.denim}; text-decoration: underline; }}
.hljs-addition {{ color: {f.green}; background: {t['add']}; }}
.hljs-deletion {{ color: {f.red_hi}; background: {t['del']}; }}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.css", stylesheet(f), flavor=f.id, dest=f"your site's assets, e.g. css/{f.slug}.css", lang="css")
        for f in flavors
    ]
