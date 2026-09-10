"""Procreate .swatches: a ZIP holding Swatches.json, colors in HSB (0..1)."""

import io
import json
import zipfile

import palette as p
from ports._lib import Out
from ports._palettes import hsv

META = {
    "id": "procreate",
    "name": "Procreate",
    "category": "Palettes",
    "homepage": "https://procreate.com",
    "enable": {
        "where": "your iPad",
        "code": "Open {name}.swatches from Files or AirDrop; it lands in Colors ▸ Palettes.",
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
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        # Fixed timestamp so rebuilding an unchanged palette gives identical bytes.
        z.writestr(zipfile.ZipInfo("Swatches.json", date_time=(1980, 1, 1, 0, 0, 0)), json.dumps(data, indent=2))
    return buf.getvalue()


def build(flavors):
    return [
        Out(f"{f.name}.swatches", swatches(f), flavor=f.id, dest="Procreate (open the file on your iPad)", lang="text")
        for f in flavors
    ]
