"""Tabby: a custom color scheme per flavor for `terminal.customColorSchemes`, indented to
paste straight under that key."""

from ports._lib import HEADER, Out, selection
from ports._terminals import lit

META = {
    "id": "tabby",
    "name": "Tabby",
    "category": "Terminals",
    "homepage": "https://tabby.sh",
    "detect": ["tabby", "/Applications/Tabby.app"],
    "enable": {
        "where": "Tabby's config.yaml (Settings › Config file)",
        "code": "terminal:\n  customColorSchemes:\n    - name: {name}   # paste the whole entry from {slug}.yaml here\n"
        "# then pick {name} under Settings › Color scheme › Dark mode (the tab Tabby uses by default)",
        "lang": "yaml",
    },
    "auto": {
        "where": "Tabby › Settings › Color scheme, with both flavors pasted into config.yaml",
        "code": "Switch color scheme: From system\nDark mode tab: Subway Seat\nLight mode tab: Subway Seat Enamel",
        "lang": "text",
    },
    "notes": "Colors, cursor and selection. config.yaml lives in `~/Library/Application Support/tabby/` "
    "(macOS), `~/.config/tabby/` (Linux) or `%APPDATA%\\tabby\\` (Windows). Tabby's default minimum "
    "contrast ratio of 4 nudges some colors; set `terminal.minimumContrastRatio: 1` to see the palette as "
    "designed.",
}


def scheme(f):
    colors = "\n".join(f"        - '{c}'" for c in f.ansi)
    return (
        f"# {HEADER}\n"
        "# One entry for terminal.customColorSchemes in Tabby's config.yaml, indented to paste under that key.\n"
        f"    - name: {f.name}\n"
        f"      foreground: '{f.text}'\n"
        f"      background: '{f.base}'\n"
        f"      cursor: '{lit(f)}'\n"
        f"      cursorAccent: '{f.base}'\n"
        f"      selection: '{selection(f)}'\n"
        f"      selectionForeground: '{f.text_hi}'\n"
        f"      colors:\n{colors}\n"
    )


def build(flavors):
    return [
        Out(
            f"{f.slug}.yaml",
            scheme(f),
            flavor=f.id,
            lang="yaml",
            how="Paste under `terminal.customColorSchemes` in Tabby's config.yaml",
        )
        for f in flavors
    ]
