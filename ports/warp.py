"""Warp: a custom theme YAML per flavor."""

from ports._lib import ANSI_NAMES, HEADER, Out
from ports._terminals import lit

META = {
    "id": "warp",
    "name": "Warp",
    "category": "Terminals",
    "homepage": "https://www.warp.dev",
    "detect": ["warp-terminal", "/Applications/Warp.app"],
    "enable": {
        "where": "a shell on macOS, then Warp › Settings › Appearance › Themes",
        "code": "mkdir -p ~/.warp/themes && cp {slug}.yaml ~/.warp/themes/   # then pick {name} in the theme picker",
        "lang": "sh",
    },
    "auto": {
        "where": "Warp › Settings › Appearance",
        "code": "Sync with OS: on\nLight: Subway Seat Enamel\nDark: Subway Seat",
        "lang": "text",
    },
    "notes": "Background, text, accent, cursor and the 16 ANSI colors. On Linux the themes folder is "
    "`~/.local/share/warp-terminal/themes/`; on Windows, `%APPDATA%\\warp\\Warp\\data\\themes\\`. Warp can "
    "take a few minutes to notice a new themes folder; restarting it is quicker.",
}


def theme(f):
    def block(colors):
        return "\n".join(f"    {n}: '{c}'" for n, c in zip(ANSI_NAMES, colors, strict=True))

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
        Out(f"{f.slug}.yaml", theme(f), flavor=f.id, dest=f"~/.warp/themes/{f.slug}.yaml", lang="yaml") for f in flavors
    ]
