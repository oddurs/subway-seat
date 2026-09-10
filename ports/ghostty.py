"""Ghostty: a theme file per flavor, named after the flavor so `theme = Subway Seat` finds it."""

from ports._lib import HEADER, Out, selection
from ports._terminals import lit, search, search_cur, split

META = {
    "id": "ghostty",
    "name": "Ghostty",
    "category": "Terminals",
    "homepage": "https://ghostty.org",
    "requires": "Ghostty 1.3+",
    "detect": ["ghostty", "/Applications/Ghostty.app"],
    "enable": {
        "where": "~/.config/ghostty/config (or config.ghostty)",
        "code": "theme = {name}",
        "lang": "conf",
        "file": "~/.config/ghostty/config",
    },
    "auto": {
        "where": "~/.config/ghostty/config (or config.ghostty)",
        "code": "theme = light:Subway Seat Enamel,dark:Subway Seat",
        "lang": "conf",
        "file": "~/.config/ghostty/config",
    },
    "notes": "The 16 ANSI colors, cursor, selection, search matches, split divider and unfocused-split fill. "
    "Ghostty 1.2 reports the search keys as unknown but applies the rest.",
}


def theme(f):
    rows = [f"palette = {i}={c}" for i, c in enumerate(f.ansi)]
    rows += [
        f"background = {f.base}",
        f"foreground = {f.text}",
        f"cursor-color = {lit(f)}",
        f"cursor-text = {f.base}",
        f"selection-background = {selection(f)}",
        f"selection-foreground = {f.text_hi}",
        f"search-background = {search(f)}",
        f"search-foreground = {f.text}",
        f"search-selected-background = {search_cur(f)}",
        f"search-selected-foreground = {f.text_hi}",
        f"split-divider-color = {split(f)}",
        f"unfocused-split-fill = {f.crust}",
    ]
    return f"# {HEADER}\n" + "\n".join(rows) + "\n"


def build(flavors):
    return [Out(f.name, theme(f), flavor=f.id, dest=f"~/.config/ghostty/themes/{f.name}", lang="conf") for f in flavors]
