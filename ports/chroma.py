from xml.sax.saxutils import quoteattr

from ports._lib import HEADER, Out
from ports._palettes import token_styles

META = {
    "id": "chroma",
    "name": "Chroma",
    "category": "Palettes",
    "homepage": "https://github.com/alecthomas/chroma",
    "enable": {
        "where": "Go code using chroma (Hugo and glamour pick it up by name once it ships in chroma's styles/)",
        "code": 'f, _ := os.Open("{slug}.xml")\nstyle, _ := chroma.NewXMLStyle(f)\nstyles.Register(style)',
        "lang": "text",
    },
    "notes": "Chroma styles in the XML format chroma keeps in its styles/ folder, the highlighter behind Hugo, "
    "glamour and Gitea.",
}


def xml(f):
    entries = [
        ("Background", f"{f.text} bg:{f.base}"),
        ("LineHighlight", f"bg:{f.surface0 if f.dark else f.mantle}"),
        ("LineNumbers", f.overlay0),
        ("LineNumbersTable", f.overlay0),
        *((path.replace(".", ""), s) for path, s in token_styles(f)),
        ("GenericUnderline", "underline"),
    ]
    body = "\n".join(f"  <entry type={quoteattr(t)} style={quoteattr(s)}/>" for t, s in entries)
    return f'<!-- {HEADER} -->\n<style name="{f.slug}">\n{body}\n</style>\n'


def build(flavors):
    return [
        Out(f"{f.slug}.xml", xml(f), flavor=f.id, dest=f"chroma's styles/{f.slug}.xml", lang="xml")
        for f in flavors
    ]
