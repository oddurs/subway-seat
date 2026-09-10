"""Adobe Swatch Exchange, written by hand: 'ASEF', v1.0, then big-endian blocks."""

import struct

import palette as p
from ports._lib import Out, rgb_floats
from ports._palettes import label

META = {
    "id": "ase",
    "name": "Adobe Swatch Exchange",
    "category": "Palettes",
    "homepage": "https://helpx.adobe.com/illustrator/desktop/manage-colors/use-swatches/share-swatches-between-applications.html",
    "enable": {
        "where": "the Swatches panel menu",
        "code": "Illustrator: Open Swatch Library › Other Library… › {name}.ase\n"
        "Photoshop: Import Swatches… › {name}.ase\n"
        "InDesign: Load Swatches… › {name}.ase\n"
        "Affinity: Import Palette… › {name}.ase",
        "lang": "text",
    },
    "notes": "An .ase swatch library per flavor, one named group of all 26 colors. "
    "Photoshop, Illustrator, InDesign and the Affinity apps all import it.",
}

HOW = ("import it from the Swatches panel menu: Illustrator › Open Swatch Library › Other Library…, "
       "Photoshop › Import Swatches…, InDesign › Load Swatches…, Affinity › Import Palette…")

GROUP_START, GROUP_END, COLOR = 0xC001, 0xC002, 0x0001
NORMAL = 2  # color type: 0 global, 1 spot, 2 normal


def name_bytes(name):
    """uint16 length in UTF-16 code units (including the null), then UTF-16BE + null."""
    encoded = (name + "\0").encode("utf-16-be")
    return struct.pack(">H", len(encoded) // 2) + encoded


def block(kind, data=b""):
    return struct.pack(">HI", kind, len(data)) + data


def ase(f):
    blocks = [block(GROUP_START, name_bytes(f.name))]
    for role in p.ROLES:
        data = name_bytes(label(role, f)) + b"RGB " + struct.pack(">fff", *rgb_floats(f.colors[role])) + struct.pack(">H", NORMAL)
        blocks.append(block(COLOR, data))
    blocks.append(block(GROUP_END))
    return b"ASEF" + struct.pack(">HHI", 1, 0, len(blocks)) + b"".join(blocks)


def build(flavors):
    return [
        Out(f"{f.name}.ase", ase(f), flavor=f.id, lang="text", how=HOW)
        for f in flavors
    ]
