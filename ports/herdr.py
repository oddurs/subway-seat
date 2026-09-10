from ports._lib import HEADER, Out

META = {
    "id": "herdr",
    "name": "herdr",
    "category": "Agents",
    "homepage": "https://herdr.dev",
    "enable": {
        "where": "~/.config/herdr/config.toml, then `herdr server reload-config`",
        "code": '[theme]\nname = "catppuccin"',
        "lang": "toml",
    },
    "notes": "Token overrides on herdr's Catppuccin base: sidebar, agent states, accents. "
    "`auto.toml` (herdr 0.9+) pairs Walnut and Enamel and follows the terminal.",
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


def build(flavors):
    by_id = {f.id: f for f in flavors}
    outs = [
        Out(f"{f.slug}.toml", f"# {HEADER}\n{table('theme.custom', f)}", flavor=f.id,
            dest="~/.config/herdr/config.toml", append=True, lang="toml")
        for f in flavors
    ]
    auto = (
        f"# {HEADER}\n[theme]\nname = \"catppuccin\"\nauto_switch = true\n"
        f"dark_name = \"catppuccin\"\nlight_name = \"catppuccin-latte\"\n\n"
        f"{table('theme.custom.dark', by_id['walnut'])}\n{table('theme.custom.light', by_id['enamel'])}"
    )
    outs.append(Out("auto.toml", auto, dest="~/.config/herdr/config.toml", append=True, lang="toml"))
    return outs
