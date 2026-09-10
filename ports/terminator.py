"""Terminator: a profile snippet per flavor for the [profiles] section of its config."""

from ports._lib import HEADER, Out
from ports._terminals import lit

META = {
    "id": "terminator",
    "name": "Terminator",
    "category": "Terminals",
    "homepage": "https://gnome-terminator.org",
    "requires": "Terminator 2.1.2+",
    "detect": ["terminator"],
    "enable": {
        "where": "right-click › Profiles, or from a shell",
        "code": 'terminator -p "{name}"',
        "lang": "sh",
    },
    "notes": "Palette, cursor and the title bar colors for the focused, broadcast-receiving and inactive "
    "terminals. Paste the snippet under the existing `[profiles]` heading. Terminator doesn't follow the "
    "system light/dark setting, so pick one flavor.",
}


def profile(f):
    rows = {
        "background_color": f.base,
        "foreground_color": f.text,
        "cursor_color_default": "False",
        "cursor_bg_color": lit(f),
        "cursor_fg_color": f.base,
        "palette": ":".join(f.ansi),
        "use_theme_colors": "False",
        "title_transmit_fg_color": f.base,
        "title_transmit_bg_color": f.orange,
        "title_receive_fg_color": f.base,
        "title_receive_bg_color": f.denim,
        "title_inactive_fg_color": f.overlay1,
        "title_inactive_bg_color": f.crust,
    }
    body = "\n".join(f'    {k} = "{v}"' if v.startswith("#") else f"    {k} = {v}" for k, v in rows.items())
    return f"# {HEADER}\n# Paste under [profiles] in ~/.config/terminator/config.\n  [[{f.name}]]\n{body}\n"


def build(flavors):
    return [
        Out(
            f"{f.slug}.config",
            profile(f),
            flavor=f.id,
            lang="ini",
            how="Paste under [profiles] in ~/.config/terminator/config",
        )
        for f in flavors
    ]
