import palette as p
from ports._lib import HEADER, Out, rgb
from ports._palettes import label

META = {
    "id": "gimp",
    "name": "GIMP, Inkscape, Krita",
    "category": "Palettes",
    "homepage": "https://www.gimp.org",
    "enable": {
        "where": "GIMP: Palettes ▸ Import Palette. Krita: Settings ▸ Manage Resources ▸ Import. Inkscape (Linux path shown):",
        "code": 'cp "{name}.gpl" ~/.config/inkscape/palettes/',
        "lang": "sh",
    },
    "notes": "A .gpl palette per flavor, laid out as two rows of 13: the grounds and text, then the accents.",
}


def gpl(f):
    rows = "\n".join("{:>3} {:>3} {:>3}\t{}".format(*rgb(f.colors[r]), label(r)) for r in p.ROLES)
    return f"GIMP Palette\nName: {f.name}\nColumns: 13\n# {HEADER}\n# {f.blurb}\n{rows}\n"


def build(flavors):
    return [
        Out(f"{f.name}.gpl", gpl(f), flavor=f.id, dest=f"~/.config/GIMP/3.0/palettes/{f.name}.gpl", lang="text")
        for f in flavors
    ]
