"""Raycast: a ray.so theme per flavor, plus the raycast://theme import link."""

import json
from urllib.parse import quote

from ports._apps import AUTHOR
from ports._lib import Out

META = {
    "id": "raycast",
    "name": "Raycast",
    "category": "Apps",
    "homepage": "https://www.raycast.com",
    "enable": {
        "where": "Raycast → Settings → Appearance (custom themes need Raycast Pro)",
        "code": "Open the raycast://theme link in {slug}.link.txt — Raycast asks to add {name}.",
        "lang": "text",
    },
    "notes": "Raycast themes are twelve colours: a walnut gradient, parchment text, a soft orange "
    "selection and the palette's accents for icons and tags. Custom themes need Raycast Pro.",
}

ORDER = ["background", "backgroundSecondary", "text", "selection", "loader",
         "red", "orange", "yellow", "green", "blue", "purple", "magenta"]


def theme(f):
    # Same key order as ray.so's own theme files; makeRaycastImportUrl reads it back in this order.
    return {
        "author": AUTHOR,
        "authorUsername": "oddurs",
        "version": "1",
        "name": f.name,
        "appearance": "dark" if f.dark else "light",
        "colors": {
            "background": f.base,
            "backgroundSecondary": f.mantle,
            "text": f.text,
            "selection": f.orange,   # ray.so draws the selected row at 10% of this
            "loader": f.yellow,
            "red": f.red_hi if f.dark else f.red,
            "orange": f.orange,
            "yellow": f.yellow,
            "green": f.green,
            "blue": f.denim,
            "purple": f.sage,
            "magenta": f.clay,
        },
    }


def deeplink(t):
    """Mirror of ray.so's makeRaycastImportUrl (app/(navigation)/themes/lib/url.ts)."""
    params = [f"{quote(k, safe='')}={quote(str(v), safe='')}" for k, v in t.items() if k != "colors"]
    params.append("colors=" + ",".join(quote(t["colors"][k], safe="") for k in ORDER))
    return "raycast://theme?" + "&".join(params)


def build(flavors):
    outs = []
    for f in flavors:
        t = theme(f)
        outs.append(Out(f"{f.slug}.json", json.dumps(t, indent=2) + "\n", flavor=f.id,
                        dest="Raycast → Settings → Appearance → import, or ray.so/themes", lang="json"))
        outs.append(Out(f"{f.slug}.link.txt", f"# {f.name} for Raycast: open this link to import\n{deeplink(t)}\n",
                        flavor=f.id, dest="open in a browser or with `open`", lang="text"))
    return outs
