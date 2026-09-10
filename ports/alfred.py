"""Alfred: an .alfredappearance theme per flavor."""

import json

from ports._apps import AUTHOR
from ports._lib import Out

META = {
    "id": "alfred",
    "name": "Alfred",
    "category": "Apps",
    "homepage": "https://www.alfredapp.com",
    "enable": {
        "where": "Alfred Preferences → Appearance",
        "code": "Double-click {name}.alfredappearance, then pick {name} under Appearance",
        "lang": "text",
    },
    "notes": "A walnut window with a recessed search field; the selected result sits on a soft orange "
    "tint with its hotkey in orange. Theming Alfred needs the Powerpack.",
}


def c(color, a=1.0):
    return f"{color}{round(a * 255):02X}"


def appearance(f):
    dark = f.dark
    selected = f.mix("orange", "base", 0.22 if dark else 0.16)
    return {
        "alfredtheme": {
            "result": {
                "textSpacing": 6,
                "subtext": {"size": 12, "colorSelected": c(f.subtext1), "font": "System", "color": c(f.overlay2)},
                "shortcut": {"size": 16, "colorSelected": c(f.orange_hi if dark else f.orange), "font": "System",
                             "color": c(f.overlay1)},
                "backgroundSelected": c(selected),
                "text": {"size": 18, "colorSelected": c(f.text_hi), "font": "System", "color": c(f.text)},
                "iconPaddingHorizontal": 6,
                "roundness": 8,
                "paddingVertical": 4,
                "iconSize": 38,
            },
            "search": {
                "backgroundSelected": c(f.surface2 if dark else f.surface1),
                "paddingHorizontal": 10,
                "spacing": 10,
                "text": {"size": 30, "colorSelected": c(f.text_hi), "font": "System Light", "color": c(f.text)},
                "background": c(f.mantle if dark else f.crust),
                "roundness": 8,
                "paddingVertical": 6,
            },
            "window": {
                "color": c(f.base, 0.97),
                "paddingHorizontal": 10,
                "width": 620,
                "borderPadding": 0,
                "borderColor": c(f.surface0 if dark else f.surface1),
                "blur": 12,
                "roundness": 14,
                "paddingVertical": 10,
            },
            "separator": {"color": c(f.surface0 if dark else f.crust), "thickness": 1},
            "scrollbar": {"color": c(f.surface2 if dark else f.surface1), "thickness": 3},
            "name": f.name,
            "credit": AUTHOR,
        }
    }


def build(flavors):
    return [
        Out(f"{f.name}.alfredappearance", json.dumps(appearance(f), indent=2) + "\n", flavor=f.id,
            dest="double-click to import into Alfred", lang="json")
        for f in flavors
    ]
