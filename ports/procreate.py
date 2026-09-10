"""Procreate .swatches: a ZIP holding Swatches.json, colors in HSB (0..1)."""

import json

import palette as p
from ports._lib import Out, zip_bytes
from ports._palettes import hsv

META = {
    "id": "procreate",
    "name": "Procreate",
    "category": "Palettes",
    "homepage": "https://procreate.com",
    "enable": {
        "where": "your iPad",
        "code": "Open {name}.swatches from Files or AirDrop; it lands in Colors › Palettes.",
        "lang": "text",
    },
    "notes": "A Procreate palette per flavor with all 26 colors in role order: grounds, text, then accents. "
    "Procreate palettes don't carry swatch names.",
}


def swatches(f):
    data = [{
        "name": f.name,
        "swatches": [
            {"hue": h, "saturation": s, "brightness": v, "alpha": 1, "colorSpace": 0}
            for h, s, v in (hsv(f.colors[r]) for r in p.ROLES)
        ],
    }]
    return zip_bytes({"Swatches.json": json.dumps(data, indent=2)}, compress=False)


def build(flavors):
    return [
        Out(f"{f.name}.swatches", swatches(f), flavor=f.id, lang="text",
            how="open it on your iPad (Files or AirDrop) and Procreate imports it")
        for f in flavors
    ]
