"""Warp: a custom theme YAML per flavor."""

from ports._lib import HEADER, Out
from ports._terminals import ANSI_NAMES, lit

META = {
    "id": "warp",
    "name": "Warp",
    "category": "Terminals",
    "homepage": "https://www.warp.dev",
    "enable": {
        "where": "Warp › Settings › Appearance › Themes",
        "code": "cp {slug}.yaml ~/.warp/themes/   # then pick {name} in the theme picker",
        "lang": "sh",
    },
    "notes": "Background, text, accent, cursor and the 16 ANSI colors. On Linux the themes folder is "
    "`~/.local/share/warp-terminal/themes/`; on Windows, `%APPDATA%\\warp\\Warp\\data\\themes\\`.",
}


def theme(f):
    def block(colors):
        return "\n".join(f"    {n}: '{c}'" for n, c in zip(ANSI_NAMES, colors))

    return (
        f"# {HEADER}\n"
        f"name: {f.name}\n"
        f"accent: '{f.orange}'\n"
        f"cursor: '{lit(f)}'\n"
        f"background: '{f.base}'\n"
        f"foreground: '{f.text}'\n"
        f"details: {'darker' if f.dark else 'lighter'}\n"
        "terminal_colors:\n"
        f"  normal:\n{block(f.ansi[:8])}\n"
        f"  bright:\n{block(f.ansi[8:])}\n"
    )


def build(flavors):
    return [
        Out(f"{f.slug}.yaml", theme(f), flavor=f.id, dest=f"~/.warp/themes/{f.slug}.yaml", lang="yaml")
        for f in flavors
    ]
