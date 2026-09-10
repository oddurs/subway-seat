"""foot: an include file per flavor with [colors-dark] and [colors-light] (foot 1.26+).

foot switches between the two sections at runtime, so each file pairs its flavor
with the opposite-brightness Subway Seat flavor: the dark flavors bring Enamel
as their light side, and Enamel brings Walnut as its dark side.
"""

from ports._lib import HEADER, Out, h
from ports._terminals import dim, lit, selection

META = {
    "id": "foot",
    "name": "foot",
    "category": "Terminals",
    "homepage": "https://codeberg.org/dnkl/foot",
    "enable": {
        "where": "~/.config/foot/foot.ini",
        "code": "[main]\ninclude=~/.config/foot/{slug}.ini",
        "lang": "ini",
    },
    "notes": "Colors, dim colors, cursor, selection, search box, jump labels, URLs and the bell flash, in "
    "both a dark and a light section. Needs foot 1.26 or later, which replaced `[colors]` with "
    "`[colors-dark]` and `[colors-light]`.",
}


def section(f, name):
    rows = {
        "cursor": f"{h(f.base)} {h(lit(f))}",
        "foreground": h(f.text),
        "background": h(f.base),
    }
    rows |= {f"regular{i}": h(c) for i, c in enumerate(f.ansi[:8])}
    rows |= {f"bright{i}": h(c) for i, c in enumerate(f.ansi[8:])}
    rows |= {f"dim{i}": h(dim(f, c)) for i, c in enumerate(f.ansi[:8])}
    rows |= {
        "selection-foreground": h(f.text_hi),
        "selection-background": h(selection(f)),
        "jump-labels": f"{h(f.base)} {h(f.orange)}",
        "scrollback-indicator": f"{h(f.text)} {h(f.surface1)}",
        "search-box-no-match": f"{h(f.base)} {h(f.red)}",
        "search-box-match": f"{h(f.text)} {h(f.surface0)}",
        "urls": h(f.denim),
        "flash": h(f.yellow),
    }
    return f"# {f.name}\n[{name}]\n" + "\n".join(f"{k}={v}" for k, v in rows.items()) + "\n"


def config(f, by_id):
    partner = by_id["walnut"] if not f.dark else by_id["enamel"]
    dark, light = (f, partner) if f.dark else (partner, f)
    main = "" if f.dark else "[main]\ninitial-color-theme=light\n\n"
    return f"# {HEADER}\n\n{main}{section(dark, 'colors-dark')}\n{section(light, 'colors-light')}"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    return [
        Out(f"{f.slug}.ini", config(f, by_id), flavor=f.id, dest=f"~/.config/foot/{f.slug}.ini", lang="ini")
        for f in flavors
    ]
