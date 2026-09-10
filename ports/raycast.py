"""Raycast: a ray.so theme per flavor, plus links that import it."""

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
        "where": "Raycast › Settings › General › Appearance",
        "code": "Open the raycast://theme link in {slug}.link.txt, and Raycast asks to add {name}.\n"
        "Or open the ray.so link beside it to preview the theme first.",
        "lang": "text",
    },
    "auto": {
        "where": "Raycast › Settings › General › Appearance",
        "code": "Keep Follow System Appearance on. Select Subway Seat Enamel and run Set as Light Theme\n"
        "from the Action Panel (⌘K), then select Subway Seat (or Tunnel) and run Set as Dark Theme.",
        "lang": "text",
    },
    "requires": "Raycast Pro (custom themes)",
    "detect": ["/Applications/Raycast.app"],
    "notes": "Raycast themes are twelve colors: a walnut gradient, parchment text, a soft orange "
    "selection and the palette's accents for icons and tags.",
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
            # No purple or magenta in the room: terracotta and Sixth Avenue orange stand in.
            "purple": f.clay,
            "magenta": f.orange_hi,
        },
    }


def query(t):
    """Mirror of ray.so's makeRaycastImportUrl (app/(navigation)/themes/lib/url.ts)."""
    params = [f"{quote(k, safe='')}={quote(str(v), safe='')}" for k, v in t.items() if k != "colors"]
    params.append("colors=" + ",".join(quote(t["colors"][k], safe="") for k in ORDER))
    return "&".join(params)


def links(f, t):
    q = query(t)
    return (
        f"# {f.name} for Raycast. Open the first link to add it to Raycast;\n"
        "# the second shows it on ray.so first, with an Add to Raycast button.\n"
        f"raycast://theme?{q}\n"
        f"https://ray.so/themes?{q}\n"
    )


def build(flavors):
    outs = []
    for f in flavors:
        t = theme(f)
        outs.append(Out(f"{f.slug}.json", json.dumps(t, indent=2) + "\n", flavor=f.id, lang="json",
                        how="the theme as ray.so stores it; the links in the .link.txt file import it"))
        outs.append(Out(f"{f.slug}.link.txt", links(f, t), flavor=f.id, lang="text",
                        how="open a link in your browser, or run `open` on it"))
    return outs
