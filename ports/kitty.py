"""kitty: a theme file per flavor in the format `kitten themes` reads."""

from ports._lib import HEADER, REPO, Out
from ports._terminals import ANSI_NAMES, lit, selection

META = {
    "id": "kitty",
    "name": "kitty",
    "category": "Terminals",
    "homepage": "https://sw.kovidgoyal.net/kitty/",
    "enable": {
        "where": "~/.config/kitty/kitty.conf",
        "code": "include themes/{slug}.conf\n# or choose it interactively: kitten themes",
        "lang": "conf",
    },
    "notes": "Colors, cursor, selection, borders, tab bar, title bar, scrollbar and marks. For light/dark "
    "following, copy the Enamel file to `light-theme.auto.conf` and a dark one to `dark-theme.auto.conf`.",
}


def theme(f):
    rows = [
        ("# The basic colors", None),
        ("foreground", f.text),
        ("background", f.base),
        ("selection_foreground", f.text_hi),
        ("selection_background", selection(f)),
        ("", None),
        ("# Cursor colors", None),
        ("cursor", lit(f)),
        ("cursor_text_color", f.base),
        ("", None),
        ("# Scrollbar colors", None),
        ("scrollbar_handle_color", f.overlay0),
        ("scrollbar_track_color", f.surface0),
        ("", None),
        ("# URL color when hovering with mouse", None),
        ("url_color", f.denim),
        ("", None),
        ("# Kitty window border colors and the visual bell", None),
        ("active_border_color", f.orange),
        ("inactive_border_color", f.surface1),
        ("bell_border_color", f.yellow),
        ("visual_bell_color", f.surface1),
        ("", None),
        ("# OS window titlebar colors", None),
        ("wayland_titlebar_color", f.crust),
        ("macos_titlebar_color", f.crust),
        ("", None),
        ("# Tab bar colors", None),
        ("active_tab_foreground", lit(f)),
        ("active_tab_background", f.base),
        ("inactive_tab_foreground", f.overlay1),
        ("inactive_tab_background", f.mantle),
        ("tab_bar_background", f.crust),
        ("tab_bar_margin_color", f.crust),
        ("", None),
        ("# Colors for marks (marked text in the terminal)", None),
        ("mark1_foreground", f.base),
        ("mark1_background", f.yellow),
        ("mark2_foreground", f.base),
        ("mark2_background", f.orange),
        ("mark3_foreground", f.base),
        ("mark3_background", f.sage),
        ("", None),
        ("# The 16 terminal colors", None),
    ]
    lines = [k if v is None else f"{k:<24}{v}" for k, v in rows]
    for i, name in enumerate(ANSI_NAMES):
        lines += ["", f"# {name}", f"{'color' + str(i):<24}{f.ansi[i]}", f"{'color' + str(i + 8):<24}{f.ansi[i + 8]}"]
    head = [
        "# vim:ft=kitty",
        f"# {HEADER}",
        "",
        f"## name:     {f.name}",
        "## author:   oddurs",
        f"## upstream: {REPO}",
        f"## blurb:    {f.blurb}",
        "",
    ]
    return "\n".join(head + lines) + "\n"


def build(flavors):
    return [
        Out(
            f"{f.slug}.conf",
            theme(f),
            flavor=f.id,
            dest=f"~/.config/kitty/themes/{f.slug}.conf",
            lang="conf",
        )
        for f in flavors
    ]
