"""macOS color list (.clr): an NSKeyedArchiver binary plist, written with plistlib.

The layout mirrors what `NSColorList.write(to:)` produces: $top holds NSKeys and
NSColors (two NSMutableArrays); each color is an NSColor whose NSComponents are
sRGB, tied to an NSColorSpace archived by its id (NSID 7 is sRGB), which AppKit
resolves without the embedded ICC profile Apple's own writer adds.
"""

import plistlib
from plistlib import UID

import palette as p
from ports._lib import Out, rgb_floats
from ports._palettes import label

META = {
    "id": "clr",
    "name": "macOS color list",
    "category": "Palettes",
    "homepage": "https://developer.apple.com/documentation/appkit/nscolorlist",
    "enable": {
        "where": "the macOS color picker (Format › Font › Show Colors, ⇧⌘C in TextEdit and Pages)",
        "code": "Color Palettes tab › pick “{name}” from the list",
        "lang": "text",
    },
    "notes": "A color list per flavor for the system color picker, so Keynote, Pages, Xcode, Sketch and "
    "every other AppKit app can pick the 26 roles by name. Colors are stored in sRGB, the space the "
    "palette is defined in.",
}

SRGB = 7  # NSColorSpace model id AppKit archives for sRGB


def clr(f):
    objects = ["$null"]

    def add(obj):
        objects.append(obj)
        return UID(len(objects) - 1)

    array_class = {"$classes": ["NSMutableArray", "NSArray", "NSObject"], "$classname": "NSMutableArray"}
    keys = {"NS.objects": []}
    keys_uid = add(keys)
    keys["NS.objects"] = [add(label(role)) for role in p.ROLES]
    keys["$class"] = add(array_class)
    colors = {"$class": keys["$class"], "NS.objects": []}
    colors_uid = add(colors)
    space = add({"NSID": SRGB})
    objects[space.data]["$class"] = add({"$classes": ["NSColorSpace", "NSObject"], "$classname": "NSColorSpace"})
    color_class = add({"$classes": ["NSColor", "NSObject"], "$classname": "NSColor"})
    for role in p.ROLES:
        r, g, b = (f"{v:g}" for v in rgb_floats(f.colors[role]))
        colors["NS.objects"].append(
            add(
                {
                    "$class": color_class,
                    "NSColorSpace": 1,
                    "NSComponents": f"{r} {g} {b} 1".encode(),
                    "NSCustomColorSpace": space,
                    # fallback for readers that predate custom color spaces
                    "NSRGB": f"{r} {g} {b}".encode() + b"\0",
                }
            )
        )
    archive = {
        "$archiver": "NSKeyedArchiver",
        "$objects": objects,
        "$top": {"NSColors": colors_uid, "NSKeys": keys_uid},
        "$version": 100000,
    }
    return plistlib.dumps(archive, fmt=plistlib.FMT_BINARY, sort_keys=True)


def build(flavors):
    return [Out(f"{f.name}.clr", clr(f), flavor=f.id, dest=f"~/Library/Colors/{f.name}.clr") for f in flavors]
