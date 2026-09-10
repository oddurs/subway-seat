"""kitty: a theme file per flavor in the format `kitten themes` reads, the three
`*-theme.auto.conf` files kitty uses to follow the OS, and colors for `kitten diff`."""

from ports._lib import ANSI_NAMES, HEADER, REPO, Out, selection, tints
from ports._terminals import dark_light, lit, split

META = {
    "id": "kitty",
    "name": "kitty",
    "category": "Terminals",
    "homepage": "https://sw.kovidgoyal.net/kitty/",
    "requires": "kitty 0.43+",
    "detect": ["kitty", "/Applications/kitty.app"],
    "enable": {
        "where": "~/.config/kitty/kitty.conf",
        "code": "include themes/{slug}.conf",
        "lang": "conf",
        "file": "~/.config/kitty/kitty.conf",
    },
    "auto": {
        "where": "a shell, in dist/kitty (kitty 0.38+; restart kitty after)",
        "code": "cp auto/*-theme.auto.conf ~/.config/kitty/   # Walnut for dark, Enamel for light\n"
        "# Tunnel for dark instead: cp subway-seat-tunnel.conf ~/.config/kitty/dark-theme.auto.conf",
        "lang": "sh",
    },
    "notes": "Colors, cursor, selection, borders, tab bar, title bar, scrollbar and marks, plus the diff "
    "kitten's colors. `kitten themes` also lists the flavors once they're in `~/.config/kitty/themes/`. "
    "GNOME reports light mode as no-preference, so `no-preference-theme.auto.conf` is Enamel too.",
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
        ("active_border_color", lit(f)),
        ("inactive_border_color", split(f)),
        ("bell_border_color", f.orange if f.dark else f.yellow),
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


def diff_rows(f):
    """kitten diff colors from the shared diff tints; syntax colors on top come from pygments_style."""
    t = tints(f)
    return [
        ("foreground", f.text),
        ("background", f.base),
        ("title_fg", f.text_hi),
        ("title_bg", f.mantle),
        ("margin_fg", f.overlay2),  # line numbers and hunk headers; ≥3:1 on every margin tint
        ("margin_bg", f.mantle),
        ("removed_bg", t["del"]),
        ("highlight_removed_bg", t["del_emph"]),
        ("removed_margin_bg", t["del_emph"]),
        ("added_bg", t["add"]),
        ("highlight_added_bg", t["add_emph"]),
        ("added_margin_bg", t["add_emph"]),
        ("moved_bg", t["chg"]),
        ("moved_margin_bg", t["chg_emph"]),
        ("filler_bg", f.mantle),
        ("hunk_margin_bg", t["info"]),
        ("hunk_bg", t["info"]),
        ("search_bg", t["search"]),
        ("search_fg", f.text),
        ("select_bg", selection(f)),
        ("select_fg", f.text_hi),
    ]


def diff(f, flavors):
    dark, light = dark_light(f, flavors)
    head = [
        "# vim:ft=kitty",
        f"# {HEADER}",
        f"# Colors for kitten diff: {light.name} when the terminal is light, {dark.name} (the dark_* keys)",
        "# when it is dark. Include it from ~/.config/kitty/diff.conf. Needs kitty 0.39+ (moved_* 0.46.1+).",
        "",
    ]
    width = max(len(k) for k, _ in diff_rows(f)) + len("dark_") + 1
    body = [f"{k:<{width}}{v}" for k, v in diff_rows(light)]
    body += [""] + [f"{'dark_' + k:<{width}}{v}" for k, v in diff_rows(dark)]
    return "\n".join(head + body) + "\n"


def auto(side, f):
    return f"# kitty loads this file while the OS is in {side} mode (kitty 0.38+).\n" + theme(f)


def build(flavors):
    outs = [
        Out(f"{f.slug}.conf", theme(f), flavor=f.id, dest=f"~/.config/kitty/themes/{f.slug}.conf", lang="conf")
        for f in flavors
    ]
    outs += [
        Out(
            f"diff/{f.slug}.conf",
            diff(f, flavors),
            flavor=f.id,
            dest=f"~/.config/kitty/{f.slug}-diff.conf",
            lang="conf",
            how=f"then add `include {f.slug}-diff.conf` to ~/.config/kitty/diff.conf",
        )
        for f in flavors
    ]
    by_id = {f.id: f for f in flavors}
    how = "Optional: copy to ~/.config/kitty/ to follow the OS light/dark setting"
    for side, fid in (("dark", "walnut"), ("light", "enamel"), ("no-preference", "enamel")):
        f = by_id[fid]
        outs.append(Out(f"auto/{side}-theme.auto.conf", auto(side, f), lang="conf", how=how))
    return outs
