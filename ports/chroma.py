"""Chroma: XML styles (what chroma keeps in styles/), and the same styles as CSS for
Hugo, which only loads chroma's built-in styles and takes anything else as CSS."""

from xml.sax.saxutils import quoteattr

from ports._lib import HEADER, Out
from ports._palettes import token_styles

META = {
    "id": "chroma",
    "name": "Chroma",
    "category": "Palettes",
    "homepage": "https://github.com/alecthomas/chroma",
    "enable": {
        "where": "Go code using chroma (glamour and Gitea pick it up by name once it ships in chroma's styles/)",
        "code": 'f, _ := os.Open("{slug}.xml")\nstyle, _ := chroma.NewXMLStyle(f)\nstyles.Register(style)',
        "lang": "go",
    },
    "notes": "Chroma styles in the XML format chroma keeps in its styles/ folder, the highlighter behind Hugo, "
    "glamour and Gitea, plus the same styles as CSS classes for Hugo sites.",
}


def entries(f):
    """(chroma token type, style string) — the XML style."""
    return [
        ("Background", f"{f.text} bg:{f.base}"),
        ("LineHighlight", f"bg:{f.surface0 if f.dark else f.mantle}"),
        ("LineNumbers", f.overlay0),
        ("LineNumbersTable", f.overlay0),
        *((path.replace(".", ""), s) for path, s in token_styles(f)),
        ("GenericUnderline", "underline"),
    ]


def xml(f):
    body = "\n".join(f"  <entry type={quoteattr(t)} style={quoteattr(s)}/>" for t, s in entries(f))
    return f'<!-- {HEADER} -->\n<style name="{f.slug}">\n{body}\n</style>\n'


# ── CSS, as chroma's own HTML formatter writes it ──────────────────────────
# Chroma's token types with their numbers (a type inherits from its hundred and its thousand)
# and CSS classes, from chroma v2 types.go. Negative types are the formatter's own boxes.
TYPES = """
Other -12 x|Error -11 err|CodeLine -10 cl|LineLink -9 lnlinks|LineTableTD -8 lntd|LineTable -7 lntable|
LineHighlight -6 hl|LineNumbersTable -5 lnt|LineNumbers -4 ln|Line -3 line|PreWrapper -2 chroma|Background -1 bg|
Keyword 1000 k|KeywordConstant 1001 kc|KeywordDeclaration 1002 kd|KeywordNamespace 1003 kn|KeywordPseudo 1004 kp|
KeywordReserved 1005 kr|KeywordType 1006 kt|Name 2000 n|NameAttribute 2001 na|NameClass 2002 nc|
NameConstant 2003 no|NameDecorator 2004 nd|NameEntity 2005 ni|NameException 2006 ne|NameLabel 2008 nl|
NameNamespace 2009 nn|NameOther 2011 nx|NameProperty 2013 py|NameTag 2014 nt|NameBuiltin 2100 nb|
NameBuiltinPseudo 2101 bp|NameVariable 2200 nv|NameVariableClass 2202 vc|NameVariableGlobal 2203 vg|
NameVariableInstance 2204 vi|NameVariableMagic 2205 vm|NameFunction 2300 nf|NameFunctionMagic 2301 fm|
Literal 3000 l|LiteralDate 3001 ld|LiteralString 3100 s|LiteralStringAffix 3101 sa|LiteralStringBacktick 3103 sb|
LiteralStringChar 3105 sc|LiteralStringDelimiter 3106 dl|LiteralStringDoc 3107 sd|LiteralStringDouble 3108 s2|
LiteralStringEscape 3109 se|LiteralStringHeredoc 3110 sh|LiteralStringInterpol 3111 si|LiteralStringOther 3113 sx|
LiteralStringRegex 3114 sr|LiteralStringSingle 3115 s1|LiteralStringSymbol 3116 ss|LiteralNumber 3200 m|
LiteralNumberBin 3201 mb|LiteralNumberFloat 3202 mf|LiteralNumberHex 3203 mh|LiteralNumberInteger 3204 mi|
LiteralNumberIntegerLong 3205 il|LiteralNumberOct 3206 mo|Operator 4000 o|OperatorWord 4001 ow|
OperatorReserved 4002 or|Punctuation 5000 p|Comment 6000 c|CommentHashbang 6001 ch|CommentMultiline 6002 cm|
CommentSingle 6003 c1|CommentSpecial 6004 cs|CommentPreproc 6100 cp|CommentPreprocFile 6101 cpf|Generic 7000 g|
GenericDeleted 7001 gd|GenericEmph 7002 ge|GenericError 7003 gr|GenericHeading 7004 gh|GenericInserted 7005 gi|
GenericOutput 7006 go|GenericPrompt 7007 gp|GenericStrong 7008 gs|GenericSubheading 7009 gu|
GenericTraceback 7010 gt|GenericUnderline 7011 gl|Text 8000 |TextWhitespace 8001 w
"""
TYPE_LIST = [(n, int(v), c) for n, v, *c in (item.split(" ") for item in TYPES.replace("\n", "").split("|"))]
TYPE_LIST = [(n, v, c[0] if c else "") for n, v, c in TYPE_LIST]
NUMBER = {n: v for n, v, _ in TYPE_LIST}
NAME = {v: n for n, v, _ in TYPE_LIST}
LINE_NUMBERS = "white-space: pre; -webkit-user-select: none; user-select: none; margin-right: 0.4em; padding: 0 0.4em 0 0.4em;"


def parse(style):
    """A chroma style string → {"color", "bg", "bold", "italic", "underline"} (tri-states as True/False)."""
    e = {}
    for part in style.split():
        if part.startswith("bg:"):
            e["bg"] = part[3:]
        elif part.startswith("#"):
            e["color"] = part
        elif part.startswith("no"):
            e[part[2:]] = False
        else:
            e[part] = True
    return e


def trunc(t, n):
    return int(t / n) * n  # Go's integer division truncates toward zero


def css(f):
    styles = {NUMBER[t]: parse(s) for t, s in entries(f)}

    def get(t):
        """chroma's Style.Get: own entry, then sub-category, category, Text and Background fill gaps."""
        out = dict(styles.get(t, {}))
        for ancestor in (trunc(t, 100), trunc(t, 1000), NUMBER["Text"], NUMBER["Background"]):
            for k, v in styles.get(ancestor, {}).items():
                out.setdefault(k, v)
        return out

    def declarations(e):
        parts = []
        if "color" in e:
            parts.append(f"color: {e['color']}")
        if "bg" in e:
            parts.append(f"background-color: {e['bg']}")
        parts += [decl for key, decl in (("bold", "font-weight: bold"), ("italic", "font-style: italic"),
                                         ("underline", "text-decoration: underline")) if e.get(key)]
        return "; ".join(parts)

    bg = get(NUMBER["Background"])
    rules = {}
    for _, t, _ in TYPE_LIST:
        e = get(t)
        if t != NUMBER["Background"]:
            e = {k: v for k, v in e.items() if bg.get(k) != v}  # chroma's Sub(bg)
        if declarations(e):
            rules[t] = declarations(e)
    rules[NUMBER["Background"]] += ";"
    rules[NUMBER["PreWrapper"]] = rules.get(NUMBER["PreWrapper"], "") + rules[NUMBER["Background"]]
    rules[NUMBER["PreWrapper"]] += " -webkit-text-size-adjust: none;"
    rules[NUMBER["Line"]] = "display: flex;" + rules.get(NUMBER["Line"], "")
    rules[NUMBER["LineNumbers"]] = LINE_NUMBERS + rules.get(NUMBER["LineNumbers"], "")
    rules[NUMBER["LineNumbersTable"]] = LINE_NUMBERS + rules.get(NUMBER["LineNumbersTable"], "")
    rules[NUMBER["LineTable"]] = "border-spacing: 0; padding: 0; margin: 0; border: 0;" + rules.get(NUMBER["LineTable"], "")
    rules[NUMBER["LineTableTD"]] = "vertical-align: top; padding: 0; margin: 0; border: 0;" + rules.get(NUMBER["LineTableTD"], "")
    rules[NUMBER["LineLink"]] = "outline: none; text-decoration: none; color: inherit" + rules.get(NUMBER["LineLink"], "")

    target = declarations(get(NUMBER["LineHighlight"]))
    classes = {v: c for _, v, c in TYPE_LIST}
    lines = [
        f"/* {HEADER} */",
        f"/* {f.name} for chroma's HTML classes (Hugo: markup.highlight.noClasses = false). */",
        f"/* Background */ .bg {{ {rules[NUMBER['Background']]} }}",
        f"/* PreWrapper */ .chroma {{ {rules[NUMBER['PreWrapper']]} }}",
        f"/* LineNumbers targeted by URL anchor */ .chroma .ln:target {{ {target} }}",
        f"/* LineNumbersTable targeted by URL anchor */ .chroma .lnt:target {{ {target} }}",
    ]
    for t in sorted(rules):
        if t in (NUMBER["Background"], NUMBER["PreWrapper"]) or not classes[t]:
            continue
        lines.append(f"/* {NAME[t]} */ .chroma .{classes[t]} {{ {rules[t]} }}")
    return "\n".join(lines) + "\n"


def build(flavors):
    outs = [
        Out(f"{f.slug}.xml", xml(f), flavor=f.id, lang="xml",
            how="load it with chroma.NewXMLStyle, or add it to chroma's styles/ folder")
        for f in flavors
    ]
    outs += [
        Out(f"css/{f.slug}.css", css(f), flavor=f.id, dest=f"static/css/{f.slug}.css", lang="css",
            how=f'in your Hugo site: set markup.highlight.noClasses = false in hugo.toml and add '
            f'<link rel="stylesheet" href="/css/{f.slug}.css"> to your templates')
        for f in flavors
    ]
    return outs
