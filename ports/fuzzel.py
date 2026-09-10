"""fuzzel: a [colors] include per flavor (RRGGBBAA)."""

from ports._desktop import bare, readable, roles
from ports._lib import HEADER, Out

META = {
    "id": "fuzzel",
    "name": "fuzzel",
    "category": "Desktop",
    "homepage": "https://codeberg.org/dnkl/fuzzel",
    "requires": "fuzzel 1.10+",
    "detect": ["fuzzel"],
    "enable": {
        "where": "~/.config/fuzzel/fuzzel.ini",
        "code": "[main]\ninclude=~/.config/fuzzel/{slug}.ini",
        "lang": "ini",
        "file": "~/.config/fuzzel/fuzzel.ini",
    },
    "notes": "Every color fuzzel has: the launcher on the raised paper ground with a quiet border, a "
    "text-wash selection, and matched letters in gold. The explicit `[main]` makes the include work "
    "at the end of the file too.",
}


def colors(f):
    r = roles(f)
    return {
        "background": r["paper"],
        "text": r["text"],
        "message": r["muted"],
        "prompt": r["muted"],
        "placeholder": r["faint"],
        "input": r["strong"],
        "match": r["match"],
        "selection": r["selection"],
        "selection-text": r["strong"],
        "selection-match": readable(f, "yellow_hi" if f.dark else "yellow", r["selection"]),
        "counter": r["faint"],
        "border": r["edge"],
    }


def ini(f):
    body = "\n".join(f"{k}={bare(v)}ff" for k, v in colors(f).items())
    return f"# {HEADER}\n# {f.name} for fuzzel\n\n[colors]\n{body}\n"


def build(flavors):
    return [
        Out(f"{f.slug}.ini", ini(f), flavor=f.id, dest=f"~/.config/fuzzel/{f.slug}.ini", lang="ini") for f in flavors
    ]
