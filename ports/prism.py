from ports._lib import HEADER, Out, tints
from ports._palettes import css_decls, selection

META = {
    "id": "prism",
    "name": "Prism",
    "category": "Palettes",
    "homepage": "https://prismjs.com",
    "enable": {
        "where": "your page's <head>, in place of a stock Prism theme",
        "code": '<link rel="stylesheet" href="{slug}.css">',
        "lang": "xml",
    },
    "notes": "A Prism stylesheet per flavor, using the same syntax colours as the editor themes.",
}

# (selectors, syntax or colour role)
RULES = [
    (".token.comment, .token.prolog, .token.doctype, .token.cdata", "comment"),
    (".token.punctuation", "punctuation"),
    (".token.operator", "operator"),
    (".token.namespace", "namespace"),
    (".token.keyword, .token.atrule, .token.rule, .token.list, .token.important", "keyword"),
    (".token.function", "function"),
    (".token.builtin", "function.builtin"),
    (".token.string, .token.char, .token.attr-value, .token.code", "string"),
    (".token.escape, .token.entity, .token.interpolation-punctuation", "string.escape"),
    (".token.regex", "regexp"),
    (".token.number", "number"),
    (".token.boolean", "boolean"),
    (".token.constant, .token.symbol", "constant"),
    (".token.class-name", "type"),
    (".token.variable", "variable"),
    (".token.parameter", "parameter"),
    (".token.property", "property"),
    # JSON keys, coloured like the editor themes do.
    (".language-json .token.property", "function"),
    (".token.tag", "tag"),
    (".token.attr-name, .token.selector", "attribute"),
    (".token.decorator, .token.annotation", "decorator"),
    (".token.title", "heading"),
    (".token.blockquote", "quote"),
    (".token.coord", "denim"),  # diff hunk headers
]


def stylesheet(f):
    t = tints(f)
    rules = "\n".join(f"{sel} {{ {css_decls(f, key)} }}" for sel, key in RULES)
    return f"""/* {HEADER} */
/* {f.name} for Prism */

code[class*="language-"],
pre[class*="language-"] {{
  color: {f.text};
  background: none;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  font-size: 1em;
  text-align: left;
  white-space: pre;
  word-spacing: normal;
  word-break: normal;
  word-wrap: normal;
  line-height: 1.5;
  tab-size: 4;
  hyphens: none;
}}

pre[class*="language-"] {{
  background: {f.base};
  padding: 1em;
  margin: 0.5em 0;
  overflow: auto;
  border-radius: 0.3em;
}}

:not(pre) > code[class*="language-"] {{
  background: {f.surface0};
  padding: 0.1em 0.3em;
  border-radius: 0.3em;
  white-space: normal;
}}

code[class*="language-"]::selection, code[class*="language-"] ::selection,
pre[class*="language-"]::selection, pre[class*="language-"] ::selection {{
  color: {f.text_hi};
  background: {selection(f)};
}}

{rules}
.token.url {{ color: {f.denim}; text-decoration: underline; }}
.token.inserted {{ color: {f.green}; background: {t['add']}; }}
.token.deleted {{ color: {f.red_hi}; background: {t['del']}; }}
.token.important, .token.bold {{ font-weight: bold; }}
.token.italic {{ font-style: italic; }}
.token.entity {{ cursor: help; }}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.css", stylesheet(f), flavor=f.id, dest=f"your site's assets, e.g. css/{f.slug}.css", lang="css")
        for f in flavors
    ]
