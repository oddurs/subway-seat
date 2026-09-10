"""Termux: colors.properties per flavor."""

from ports._lib import HEADER, Out
from ports._terminals import lit

META = {
    "id": "termux",
    "name": "Termux",
    "category": "Terminals",
    "homepage": "https://termux.dev",
    "enable": {
        "where": "Termux, after copying the file to ~/.termux/colors.properties",
        "code": "termux-reload-settings",
        "lang": "sh",
    },
    "notes": "Background, foreground, cursor and the 16 ANSI colors. Termux reads one color file, so "
    "switching flavors means replacing it.",
}


def props(f):
    rows = [f"background: {f.base}", f"foreground: {f.text}", f"cursor:     {lit(f)}", ""]
    for i in range(8):
        rows += [f"color{i}:     {f.ansi[i]}", f"color{i + 8}:{' ' * (5 - len(str(i + 8)))}{f.ansi[i + 8]}", ""]
    return f"# {HEADER}\n# {f.name}\n\n" + "\n".join(rows)


def build(flavors):
    return [
        Out(f"{f.slug}.properties", props(f), flavor=f.id, dest="~/.termux/colors.properties", lang="ini")
        for f in flavors
    ]
