"""Vivaldi: an importable theme (a zip holding settings.json) per flavor."""

import json

from ports._apps import stable_uuid
from ports._lib import Out, zip_bytes

META = {
    "id": "vivaldi",
    "name": "Vivaldi",
    "category": "Apps",
    "homepage": "https://vivaldi.com",
    "enable": {
        "where": "Vivaldi › Settings › Themes › Library",
        "code": "Import Theme › {slug}.zip",
        "lang": "text",
    },
    "auto": {
        "where": "Vivaldi › Settings › Themes › Theme Schedule",
        "code": "Follow the operating system's schedule, with Subway Seat Enamel for light\n"
        "and Subway Seat (or Subway Seat Tunnel) for dark",
        "lang": "text",
    },
    "detect": ["/Applications/Vivaldi.app", "vivaldi", "vivaldi-stable"],
    "notes": "Toolbars and panels on the flavor's base, the window frame one step deeper, and burnt orange "
    "for the active tab and focus. Vivaldi works out readable text on the accent by itself.",
}


def settings(f):
    # Key set and defaults follow a theme exported from Vivaldi (as in catppuccin/vivaldi's base_settings.json).
    return {
        "accentFromPage": False,
        "accentOnWindow": False,
        "accentSaturationLimit": 1,
        "alpha": 1,
        "backgroundImage": "",
        "backgroundPosition": "stretch",
        "blur": 0,
        "colorAccentBg": f.orange,
        "colorBg": f.base,
        "colorFg": f.text,
        "colorHighlightBg": f.orange,
        "colorWindowBg": f.crust,
        "contrast": 0,
        "dimBlurred": False,
        "engineVersion": 1,
        "id": stable_uuid(f"vivaldi/{f.slug}"),
        "name": f.name,
        "preferSystemAccent": False,
        "radius": 6,
        "simpleScrollbar": True,
        "transparencyTabBar": False,
        "transparencyTabs": False,
        "url": "",
        "version": 1,
    }


def build(flavors):
    outs = []
    for f in flavors:
        s = json.dumps(settings(f), indent=3) + "\n"
        outs.append(Out(f"{f.slug}/settings.json", s, flavor=f.id, lang="json", how=f"inside {f.slug}.zip"))
        outs.append(Out(f"{f.slug}.zip", zip_bytes({"settings.json": s}), flavor=f.id,
                        how="Vivaldi › Settings › Themes › Library › Import Theme"))
    return outs
