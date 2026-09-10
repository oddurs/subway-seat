"""herdr: token overrides on top of one of herdr's built-in themes.

herdr paints the built-in theme named in `[theme]`, then `[theme.custom]`, then,
with `auto_switch`, `[theme.custom.dark]` or `[theme.custom.light]`. Every token
herdr lets you override is set here, so the base only supplies what herdr
derives itself; Walnut and Tunnel sit on `catppuccin`, Enamel on the light
`catppuccin-latte`. `surface0`, `surface1`, `overlay0`, `overlay1` and
`subtext0` aren't in the 0.9 config reference, but the theme loader reads them.

The files hold tables only, never `[theme]` itself: herdr's default config
already has one, and TOML refuses a second.
"""

from ports._lib import HEADER, MARK_END, MARK_START, Out

META = {
    "id": "herdr",
    "name": "herdr",
    "category": "Agents",
    "homepage": "https://herdr.dev",
    "enable": {
        "where": "~/.config/herdr/config.toml, under your existing `[theme]`, then `herdr server reload-config`",
        "code": '[theme]\nname = "catppuccin"   # with Enamel: "catppuccin-latte"',
        "lang": "toml",
    },
    "auto": {
        "where": "~/.config/herdr/config.toml (herdr 0.9+), under your existing `[theme]`; append auto.toml for the colors",
        "code": '[theme]\nname = "catppuccin"\nauto_switch = true\ndark_name = "catppuccin"\nlight_name = "catppuccin-latte"',
        "lang": "toml",
    },
    "detect": ["herdr", "~/.config/herdr"],
    "notes": "Token overrides for the sidebar, agent states and accents, on herdr's Catppuccin base "
    "(Latte under Enamel). `auto.toml` (herdr 0.9+) pairs Walnut with Enamel and follows the terminal's light or dark mode. "
    "Append one file; to switch, replace the block between the markers.",
}


def tokens(f):
    return {
        "panel_bg": f.base,
        "sidebar_bg": f.mantle,
        "active_row_bg": f.surface0,
        "selection_bg": f.surface1,
        "surface_dim": f.mantle,
        "surface0": f.surface0,
        "surface1": f.surface1,
        "overlay0": f.overlay0,
        "overlay1": f.overlay1,
        "text": f.text,
        "subtext0": f.subtext0,
        "accent": f.orange,
        "mauve": f.clay,
        "peach": f.orange_hi,
        "yellow": f.yellow,
        "green": f.green,
        "red": f.red_hi,
        "blue": f.denim,
        "teal": f.sage,
    }


def table(name, f):
    return f"[{name}]\n" + "\n".join(f'{k} = "{v}"' for k, v in tokens(f).items()) + "\n"


def block(body):
    return f"{MARK_START}\n# {HEADER}\n{body}{MARK_END}\n"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    outs = [
        Out(f"{f.slug}.toml", block(f"# {f.name}; base theme: {'catppuccin' if f.dark else 'catppuccin-latte'}\n"
                                    + table("theme.custom", f)),
            flavor=f.id, dest="~/.config/herdr/config.toml", append=True, lang="toml")
        for f in flavors
    ]
    auto = block(
        "# Walnut when the terminal is dark, Enamel when it's light (needs auto_switch under [theme])\n"
        f"{table('theme.custom.dark', by_id['walnut'])}\n{table('theme.custom.light', by_id['enamel'])}"
    )
    outs.append(Out("auto.toml", auto, dest="~/.config/herdr/config.toml", append=True, lang="toml"))
    return outs
