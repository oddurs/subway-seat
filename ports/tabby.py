"""Tabby: a custom colour scheme per flavor for `terminal.customColorSchemes`."""

from ports._lib import HEADER, Out
from ports._terminals import lit, selection

META = {
    "id": "tabby",
    "name": "Tabby",
    "category": "Terminals",
    "homepage": "https://tabby.sh",
    "enable": {
        "where": "Tabby's config.yaml (Settings › Config file), then Settings › Color scheme",
        "code": "terminal:\n  customColorSchemes:\n    - name: {name}   # paste the whole entry from {slug}.yaml",
        "lang": "yaml",
    },
    "notes": "Colours, cursor and selection. Tabby's default minimum contrast ratio of 4 nudges some "
    "colours; set `terminal.minimumContrastRatio: 1` to see the palette as designed.",
}


def scheme(f):
    colors = "\n".join(f"    - '{c}'" for c in f.ansi)
    return (
        f"# {HEADER}\n"
        "# One entry for terminal.customColorSchemes in Tabby's config.yaml.\n"
        f"- name: {f.name}\n"
        f"  foreground: '{f.text}'\n"
        f"  background: '{f.base}'\n"
        f"  cursor: '{lit(f)}'\n"
        f"  cursorAccent: '{f.base}'\n"
        f"  selection: '{selection(f)}'\n"
        f"  selectionForeground: '{f.text_hi}'\n"
        f"  colors:\n{colors}\n"
    )


def build(flavors):
    return [
        Out(
            f"{f.slug}.yaml",
            scheme(f),
            flavor=f.id,
            dest="Tabby config.yaml, under terminal.customColorSchemes",
            lang="yaml",
        )
        for f in flavors
    ]
