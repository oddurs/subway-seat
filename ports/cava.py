from ports._cli import stripe
from ports._lib import HEADER, Out

META = {
    "id": "cava",
    "name": "cava",
    "category": "CLI & TUI",
    "homepage": "https://github.com/karlstav/cava",
    "enable": {
        "where": "~/.config/cava/config, with the theme file in ~/.config/cava/themes/",
        "code": "[color]\ntheme = '{slug}'",
        "lang": "ini",
    },
    "detect": ["cava"],
    "notes": "Bars rise through the 70s stripe: avocado at the floor, then harvest gold, burnt orange "
    "and redbird at the peaks. On cava without theme files, paste the `[color]` block into your config.",
}


def theme(f):
    stops = "\n".join(f"gradient_color_{i} = '{c}'" for i, c in enumerate(stripe(f, 8), 1))
    return f"""# {HEADER}
# {f.name} for cava: gradient from the bottom of the screen to the top.
[color]
gradient = 1
{stops}
"""


def build(flavors):
    return [
        Out(f"themes/{f.slug}", theme(f), flavor=f.id, dest=f"~/.config/cava/themes/{f.slug}", lang="ini")
        for f in flavors
    ]
