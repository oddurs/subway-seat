"""Tilix: a JSON color scheme per flavor."""

import json

from ports._lib import Out, selection
from ports._terminals import lit

META = {
    "id": "tilix",
    "name": "Tilix",
    "category": "Terminals",
    "homepage": "https://gnunn1.github.io/tilix-web/",
    "detect": ["tilix"],
    "enable": {
        "where": "Preferences › Profiles › Color › Color scheme",
        "code": "{name}",
        "lang": "text",
    },
    "notes": "Palette, cursor, selection highlight, bold and badge colors. Tilix doesn't switch color "
    "schemes with the system style, so pick one flavor.",
}


def scheme(f):
    return {
        "name": f.name,
        "comment": f.blurb,
        "use-theme-colors": False,
        "background-color": f.base,
        "foreground-color": f.text,
        "palette": f.ansi,
        "use-cursor-color": True,
        "cursor-background-color": lit(f),
        "cursor-foreground-color": f.base,
        "use-highlight-color": True,
        "highlight-background-color": selection(f),
        "highlight-foreground-color": f.text_hi,
        "use-bold-color": True,
        "bold-color": f.text_hi,
        "use-badge-color": True,
        "badge-color": f.orange,
    }


def build(flavors):
    return [
        Out(
            f"{f.slug}.json",
            json.dumps(scheme(f), indent=2) + "\n",
            flavor=f.id,
            dest=f"~/.config/tilix/schemes/{f.slug}.json",
            lang="json",
        )
        for f in flavors
    ]
