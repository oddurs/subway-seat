from ports._lib import HEADER, Out, selection, tints
from ports._palettes import css_decls

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
    "auto": {
        "where": "your page's <head>, in place of a stock Prism theme",
        "code": '<link rel="stylesheet" href="subway-seat-auto.css">\n'
        "<!-- Enamel while the system is light, Subway Seat (Walnut) while it's dark -->",
        "lang": "xml",
    },
    "notes": "A Prism stylesheet per flavor, using the same syntax colors as the editor themes, and "
    "subway-seat-auto.css, which follows the system's light or dark setting. In diffs (and the diff-highlight "
    "plugin), added and removed lines sit on green and red grounds with their code colors kept, the + and - "
    "signs are green and red, and hunk headers are denim.",
}

# (selectors, syntax or color role)
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
    # JSON keys, colored like the editor themes do.
    (".language-json .token.property", "function"),
    (".token.tag", "tag"),
    (".token.attr-name, .token.selector", "attribute"),
    (".token.decorator, .token.annotation", "decorator"),
    (".token.title", "heading"),
    (".token.blockquote", "quote"),
    (".token.coord", "denim"),  # diff hunk headers
]


LAYOUT = """code[class*="language-"],
pre[class*="language-"] {
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
}

pre[class*="language-"] {
  padding: 1em;
  margin: 0.5em 0;
  overflow: auto;
  border-radius: 0.3em;
}

:not(pre) > code[class*="language-"] {
  padding: 0.1em 0.3em;
  border-radius: 0.3em;
  white-space: normal;
}

.token.important, .token.bold { font-weight: bold; }
.token.italic { font-style: italic; }
.token.entity { cursor: help; }

/* Diff lines fill the width, so their tint reads as a band. */
[class*="language-diff"] .token.inserted:not(.prefix),
[class*="language-diff"] .token.deleted:not(.prefix),
[class*="language-diff"] .token.diff:not(.prefix) { display: block; color: inherit; font-weight: inherit; }"""


def colors(f):
    """Every rule that depends on the flavor."""
    t = tints(f)
    rules = "\n".join(f"{sel} {{ {css_decls(f, key)} }}" for sel, key in RULES)
    diff = '[class*="language-diff"]'
    return f"""code[class*="language-"],
pre[class*="language-"] {{ color: {f.text}; }}
pre[class*="language-"] {{ background: {f.base}; }}
:not(pre) > code[class*="language-"] {{ background: {f.surface0}; }}

code[class*="language-"]::selection, code[class*="language-"] ::selection,
pre[class*="language-"]::selection, pre[class*="language-"] ::selection {{
  color: {f.text_hi};
  background: {selection(f)};
}}

{rules}
.token.url {{ color: {f.denim}; text-decoration: underline; }}

/* Diffs: the line keeps its code colors on a green or red tint, and the + / - sign carries the color.
   (Other languages mark a whole line as inserted or deleted, so it takes the color itself.) */
.token.inserted {{ color: {f.green}; }}
.token.deleted {{ color: {f.red_hi}; }}
{diff} .token.inserted:not(.prefix) {{ background: {t['add']}; }}
{diff} .token.deleted:not(.prefix) {{ background: {t['del']}; }}
{diff} .token.diff:not(.prefix) {{ background: {t['chg']}; }}
{diff} .token.prefix.inserted {{ color: {f.green}; }}
{diff} .token.prefix.deleted {{ color: {f.red_hi}; }}
{diff} .token.prefix.diff {{ color: {f.yellow}; }}"""


def stylesheet(f):
    return f"/* {HEADER} */\n/* {f.name} for Prism */\n\n{LAYOUT}\n\n{colors(f)}\n"


def auto_stylesheet(light, dark):
    night = "\n".join(f"  {line}" if line else "" for line in colors(dark).splitlines())
    return (
        f"/* {HEADER} */\n/* Subway Seat for Prism, following the system: {light.name} when it's light, "
        f"{dark.name} when it's dark. */\n\n{LAYOUT}\n\n{colors(light)}\n\n"
        f"@media (prefers-color-scheme: dark) {{\n{night}\n}}\n"
    )


def build(flavors):
    by = {f.id: f for f in flavors}
    how = "in your site's stylesheets"
    outs = [
        Out(f"{f.slug}.css", stylesheet(f), flavor=f.id, dest=f"styles/prism/{f.slug}.css", lang="css", how=how)
        for f in flavors
    ]
    outs.append(Out("subway-seat-auto.css", auto_stylesheet(by["enamel"], by["walnut"]),
                    dest="styles/prism/subway-seat-auto.css", lang="css", how=how))
    return outs
