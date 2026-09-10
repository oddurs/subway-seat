"""Rio: a TOML theme per flavor for `~/.config/rio/themes`."""

from ports._lib import ANSI_NAMES, HEADER, Out, selection
from ports._terminals import dim, lit, search, search_cur, split

META = {
    "id": "rio",
    "name": "Rio",
    "category": "Terminals",
    "homepage": "https://rioterm.com",
    "detect": ["rio", "/Applications/Rio.app"],
    "enable": {
        "where": "~/.config/rio/config.toml, at the top level (above any [section])",
        "code": 'theme = "{slug}"',
        "lang": "toml",
    },
    "auto": {
        "where": "~/.config/rio/config.toml",
        "code": '[adaptive-theme]\nlight = "subway-seat-enamel"\ndark = "subway-seat"',
        "lang": "toml",
    },
    "notes": "Normal, light and dim colors, both cursors, tabs, splits, selection, search and hints.",
}


def theme(f):
    rows = {"foreground": f.text, "background": f.base}
    rows |= dict(zip(ANSI_NAMES, f.ansi[:8], strict=True))
    rows |= {
        "cursor": lit(f),
        "vi-cursor": f.sage,
        "tabs": f.overlay1,
        "tabs-active": lit(f),
        "split": split(f),
        "split-active": lit(f),
        "selection-foreground": f.text_hi,
        "selection-background": selection(f),
        "search-match-foreground": f.text,
        "search-match-background": search(f),
        "search-focused-match-foreground": f.text_hi,
        "search-focused-match-background": search_cur(f),
        "hint-foreground": f.base,
        "hint-background": lit(f),
        "dim-foreground": f.overlay2,
        "light-foreground": f.text_hi,
    }
    rows |= {f"dim-{n}": dim(f, c) for n, c in zip(ANSI_NAMES, f.ansi[:8], strict=True)}
    rows |= {f"light-{n}": c for n, c in zip(ANSI_NAMES, f.ansi[8:], strict=True)}
    width = max(map(len, rows))
    return f"# {HEADER}\n[colors]\n" + "\n".join(f"{k:<{width}} = '{v}'" for k, v in rows.items()) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.toml", theme(f), flavor=f.id, dest=f"~/.config/rio/themes/{f.slug}.toml", lang="toml")
        for f in flavors
    ]
