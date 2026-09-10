"""iTerm2: an .itermcolors color preset per flavor, plus one preset that carries Walnut and
Enamel under iTerm2 3.5's " (Dark)"/" (Light)" keys, so the profile follows macOS."""

import plistlib

from ports._lib import HEADER, Out, rgb_floats, selection
from ports._terminals import lit, search

AUTO = "Subway Seat Light and Dark"

META = {
    "id": "iterm2",
    "name": "iTerm2",
    "category": "Terminals",
    "homepage": "https://iterm2.com",
    "detect": ["/Applications/iTerm.app"],
    "enable": {
        "where": "iTerm2 › Settings › Profiles › Colors › Color Presets… › Import…",
        "code": 'open "{name}.itermcolors"   # imports the preset\n# then Color Presets… › {name}',
        "lang": "sh",
    },
    "auto": {
        "where": "iTerm2 3.5+ › Settings › Profiles › Colors",
        "code": f'open "{AUTO}.itermcolors"   # imports the preset\n'
        f"# then Color Presets… › {AUTO} (choose Update Both Modes if asked)",
        "lang": "sh",
    },
    "notes": "ANSI colors plus cursor, cursor guide, selection, link, search match, underline, badge and tab "
    "color. Tab Color and Underline Color only show once their boxes are ticked in the profile.",
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


def colors(f, suffix=""):
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
        "Underline Color": color(lit(f)),
        "Badge Color": color(f.orange, 0.5),
        "Tab Color": color(f.crust),
    }
    return {k + suffix: v for k, v in d.items()}


def plist(d):
    xml = plistlib.dumps(d, sort_keys=False).decode()
    # A comment after the DOCTYPE is legal plist XML; iTerm2 and plutil skip it.
    head, _, rest = xml.partition("<plist")
    return f"{head}<!-- {HEADER} -->\n<plist{rest}"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    how = "Open the file to import it as a color preset"
    outs = [Out(f"{f.name}.itermcolors", plist(colors(f)), flavor=f.id, lang="xml", how=how) for f in flavors]
    # The unsuffixed Walnut keys are what iTerm2 before 3.5 reads.
    both = colors(by_id["walnut"]) | colors(by_id["walnut"], " (Dark)") | colors(by_id["enamel"], " (Light)")
    outs.append(
        Out(
            f"{AUTO}.itermcolors",
            plist(both),
            lang="xml",
            how=f"{how}; it switches with the macOS appearance (iTerm2 3.5+)",
        )
    )
    return outs
