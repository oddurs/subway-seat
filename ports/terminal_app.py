"""macOS Terminal.app: a .terminal profile per flavor.

Terminal stores each color as an NSKeyedArchiver-archived NSColor. We write the
archive by hand with plistlib, following mbadolato/iTerm2-Color-Schemes'
iterm2terminal.py, but tag the color as sRGB (NSCustomColorSpace, NSID 7) so the
hex values survive color management. The bare NSColorSpace 1 ("calibrated")
form decodes as Generic RGB and shifts #362619 to #463221; NSColorSpace 2 is
device RGB, which is unmanaged.
"""

import plistlib

from ports._lib import HEADER, Out, rgb_floats, selection
from ports._terminals import lit

META = {
    "id": "terminal-app",
    "name": "Terminal.app",
    "category": "Terminals",
    "homepage": "https://support.apple.com/guide/terminal/welcome/mac",
    "detect": ["/System/Applications/Utilities/Terminal.app"],
    "enable": {
        "where": "Terminal › Settings › Profiles (select it, then click Default)",
        "code": 'open "{name}.terminal"   # imports the profile and opens a window',
        "lang": "sh",
    },
    "notes": "The 16 ANSI colors plus background, text, bold text, selection and cursor. Terminal.app has "
    "no setting for cursor text or tab colors, and a profile doesn't switch with the macOS appearance, so "
    "pick one flavor.",
}

ANSI_KEYS = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]


def nscolor(hex_):
    """An archived sRGB NSColor, as AppKit's own NSKeyedArchiver writes it (minus the ICC blob)."""
    rgb = " ".join(f"{v:.6g}" for v in rgb_floats(hex_))
    archive = {
        "$version": 100000,
        "$archiver": "NSKeyedArchiver",
        "$top": {"root": plistlib.UID(1)},
        "$objects": [
            "$null",
            {
                "NSColorSpace": 1,
                "NSComponents": f"{rgb} 1".encode(),
                "NSRGB": f"{rgb}\0".encode(),
                "NSCustomColorSpace": plistlib.UID(2),
                "$class": plistlib.UID(4),
            },
            {"NSID": 7, "$class": plistlib.UID(3)},  # 7 = sRGB IEC61966-2.1
            {"$classname": "NSColorSpace", "$classes": ["NSColorSpace", "NSObject"]},
            {"$classname": "NSColor", "$classes": ["NSColor", "NSObject"]},
        ],
    }
    return plistlib.dumps(archive, fmt=plistlib.FMT_BINARY, sort_keys=False)


def profile(f):
    colors = {f"ANSI{n}Color": c for n, c in zip(ANSI_KEYS, f.ansi[:8], strict=True)}
    colors |= {f"ANSIBright{n}Color": c for n, c in zip(ANSI_KEYS, f.ansi[8:], strict=True)}
    colors |= {
        "BackgroundColor": f.base,
        "TextColor": f.text,
        "TextBoldColor": f.text_hi,
        "SelectionColor": selection(f),
        "CursorColor": lit(f),
    }
    d = {"name": f.name, "type": "Window Settings", "ProfileCurrentVersion": 2.09}
    d |= {k: nscolor(v) for k, v in colors.items()}
    head, _, rest = plistlib.dumps(d).partition(b"<plist")
    return head + f"<!-- {HEADER} -->\n".encode() + b"<plist" + rest


def build(flavors):
    return [
        Out(
            f"{f.name}.terminal",
            profile(f),
            flavor=f.id,
            lang="xml",
            how="Open the file to import it as a Terminal profile",
        )
        for f in flavors
    ]
