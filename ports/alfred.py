"""Alfred: an .alfredappearance theme per flavor."""

import json

import palette as p
from ports._apps import AUTHOR
from ports._lib import Out, selection

META = {
    "id": "alfred",
    "name": "Alfred",
    "category": "Apps",
    "homepage": "https://www.alfredapp.com",
    "enable": {
        "where": "Alfred Preferences › Appearance",
        "code": "Double-click {name}.alfredappearance, then pick {name} under Appearance",
        "lang": "text",
    },
    "auto": {
        "where": "Alfred Preferences › Appearance",
        "code": "Alfred keeps one theme for macOS Light mode and one for Dark mode:\n"
        "with macOS in Light mode, pick Subway Seat Enamel;\n"
        "switch macOS to Dark mode, then pick Subway Seat (or Subway Seat Tunnel).",
        "lang": "text",
    },
    "requires": "Alfred 5 with the Powerpack",
    "detect": ["/Applications/Alfred 5.app"],
    "notes": "A walnut window with a recessed search field; the selected result sits on a soft orange "
    "tint with its hotkey in orange.",
}


def appearance(f):
    dark = f.dark
    c = p.alpha  # Alfred colors are #RRGGBBAA
    selected = f.mix("orange", "base", 0.22 if dark else 0.16)
    return {
        "alfredtheme": {
            "result": {
                "textSpacing": 6,
                "subtext": {"size": 12, "colorSelected": c(f.subtext1, 1), "font": "System", "color": c(f.overlay2, 1)},
                "shortcut": {"size": 16, "colorSelected": c(f.orange_hi if dark else f.orange, 1), "font": "System",
                             "color": c(f.overlay1, 1)},
                "backgroundSelected": c(selected, 1),
                "text": {"size": 18, "colorSelected": c(f.text_hi, 1), "font": "System", "color": c(f.text, 1)},
                "iconPaddingHorizontal": 6,
                "roundness": 8,
                "paddingVertical": 4,
                "iconSize": 38,
            },
            "search": {
                "backgroundSelected": c(selection(f), 1),
                "paddingHorizontal": 10,
                "spacing": 10,
                "text": {"size": 30, "colorSelected": c(f.text_hi, 1), "font": "System Light", "color": c(f.text, 1)},
                "background": c(f.mantle if dark else f.crust, 1),
                "roundness": 8,
                "paddingVertical": 6,
            },
            "window": {
                "color": c(f.base, 0.97),
                "paddingHorizontal": 10,
                "width": 620,
                "borderPadding": 0,
                "borderColor": c(f.surface0 if dark else f.surface1, 1),
                "blur": 12,
                "roundness": 14,
                "paddingVertical": 10,
            },
            "separator": {"color": c(f.surface0 if dark else f.crust, 1), "thickness": 1},
            "scrollbar": {"color": c(selection(f), 1), "thickness": 3},
            "name": f.name,
            "credit": AUTHOR,
        }
    }


def build(flavors):
    return [
        Out(f"{f.name}.alfredappearance", json.dumps(appearance(f), indent=2) + "\n", flavor=f.id, lang="json",
            how="double-click it to import into Alfred")
        for f in flavors
    ]
