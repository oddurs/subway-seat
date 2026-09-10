"""iTerm2: an .itermcolors color preset per flavor."""

import plistlib

from ports._lib import HEADER, Out, rgb_floats
from ports._terminals import lit, search, selection

META = {
    "id": "iterm2",
    "name": "iTerm2",
    "category": "Terminals",
    "homepage": "https://iterm2.com",
    "enable": {
        "where": "iTerm2 › Settings › Profiles › Colors › Color Presets… › Import…",
        "code": 'open "{name}.itermcolors"   # imports the preset\n# then Color Presets… › {name}',
        "lang": "sh",
    },
    "notes": "ANSI colors plus cursor, cursor guide, selection, link, search match, badge and tab color. "
    "Tab Color only shows once the profile's Tab Color box is ticked.",
}


def color(hex_, a=1.0):
    r, g, b = rgb_floats(hex_)
    return {
        "Red Component": r,
        "Green Component": g,
        "Blue Component": b,
        "Alpha Component": a,
        "Color Space": "sRGB",
    }


def preset(f):
    d = {f"Ansi {i} Color": color(c) for i, c in enumerate(f.ansi)}
    d |= {
        "Background Color": color(f.base),
        "Foreground Color": color(f.text),
        "Bold Color": color(f.text_hi),
        "Cursor Color": color(lit(f)),
        "Cursor Text Color": color(f.base),
        "Cursor Guide Color": color(f.text, 0.08),
        "Link Color": color(f.denim),
        "Selection Color": color(selection(f)),
        "Selected Text Color": color(f.text_hi),
        "Match Background Color": color(search(f)),
        "Badge Color": color(f.orange, 0.5),
        "Tab Color": color(f.crust),
    }
    xml = plistlib.dumps(d, sort_keys=False).decode()
    # A comment after the DOCTYPE is legal plist XML; iTerm2 and plutil skip it.
    head, _, rest = xml.partition("<plist")
    return f"{head}<!-- {HEADER} -->\n<plist{rest}"


def build(flavors):
    return [
        Out(
            f"{f.name}.itermcolors",
            preset(f),
            flavor=f.id,
            dest="iTerm2 (open the file to import it as a preset)",
            lang="xml",
        )
        for f in flavors
    ]
