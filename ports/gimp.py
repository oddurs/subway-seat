import palette as p
from ports._lib import HEADER, Out, rgb
from ports._palettes import label

META = {
    "id": "gimp",
    "name": "GIMP, Inkscape, Krita",
    "category": "Palettes",
    "homepage": "https://www.gimp.org",
    "enable": {
        "where": "GIMP, Inkscape or Krita",
        "code": "GIMP: copy {name}.gpl to its palettes folder, or Palettes panel menu › Import Palette…\n"
        "Krita: Settings › Manage Resources… › Import Resources › {name}.gpl\n"
        "Inkscape: copy {name}.gpl to its palettes folder, then restart Inkscape",
        "lang": "text",
    },
    "notes": "A .gpl palette per flavor, laid out as two rows of 13: the grounds and text, then the accents.",
}

FOLDERS = (
    "GIMP's palettes folder on Linux. On macOS: ~/Library/Application Support/GIMP/3.0/palettes; "
    "on Windows: %APPDATA%\\GIMP\\3.0\\palettes. Inkscape: ~/.config/inkscape/palettes (Linux), "
    "~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/palettes (macOS), "
    "%APPDATA%\\inkscape\\palettes (Windows)."
)


def gpl(f):
    rows = "\n".join("{:>3} {:>3} {:>3}\t{}".format(*rgb(f.colors[r]), label(r, f)) for r in p.ROLES)
    return f"GIMP Palette\nName: {f.name}\nColumns: 13\n# {HEADER}\n# {f.blurb}\n{rows}\n"


def build(flavors):
    return [
        Out(f"{f.name}.gpl", gpl(f), flavor=f.id, dest=f"~/.config/GIMP/3.0/palettes/{f.name}.gpl", lang="text",
            how=FOLDERS)
        for f in flavors
    ]
