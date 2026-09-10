"""Ptyxis: a .palette per flavor with a [Light] and a [Dark] face.

Ptyxis picks the face that matches its style, so each file pairs its flavor with the
opposite-brightness one, like the foot port: the dark flavors bring Enamel as their
light face, and Enamel brings Walnut as its dark face.
"""

from ports._lib import HEADER, Out, tints
from ports._terminals import lit

META = {
    "id": "ptyxis",
    "name": "Ptyxis",
    "category": "Terminals",
    "homepage": "https://gitlab.gnome.org/GNOME/ptyxis",
    "requires": "Ptyxis 46+",
    "detect": ["ptyxis", "~/.var/app/app.devsuite.Ptyxis", "/var/lib/flatpak/app/app.devsuite.Ptyxis"],
    "enable": {
        "where": "Preferences › Profiles › your profile › Color Palette (under Show All), or a shell",
        "code": 'uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "\'")\n'
        "gsettings set \"org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/\" palette '{slug}'",
        "lang": "sh",
    },
    "auto": {
        "where": "the main menu's style buttons (Follow System Style), or a shell",
        "code": "gsettings set org.gnome.Ptyxis interface-style 'system'",
        "lang": "sh",
    },
    "notes": "The 16 colors, cursor, header bar, bell flash, and the header tints for root and SSH "
    "sessions, in a light and a dark face. Ptyxis switches faces with its style; from Ptyxis 49 that "
    "style is dark until you choose Follow System Style. The Flatpak reads palettes from "
    "`~/.var/app/app.devsuite.Ptyxis/data/app.devsuite.Ptyxis/palettes/`. The cursor text color needs Ptyxis 50.",
}


def face(f, section):
    t = tints(f)
    rows = {
        "Foreground": f.text,
        "Background": f.base,
        "Cursor": lit(f),
        "CursorForeground": f.base,
        **{f"Color{i}": c for i, c in enumerate(f.ansi)},
        "TitlebarForeground": f.text,
        "TitlebarBackground": f.mantle,
        "BellForeground": f.text_hi,
        "BellBackground": f.mix("yellow", "mantle", 0.25),
        "SuperuserForeground": f.text_hi,
        "SuperuserBackground": t["del"],
        "RemoteForeground": f.text_hi,
        "RemoteBackground": t["info"],
    }
    return f"# {f.name}\n[{section}]\n" + "\n".join(f"{k}={v}" for k, v in rows.items()) + "\n"


def palette(f, by_id):
    partner = by_id["enamel"] if f.dark else by_id["walnut"]
    dark, light = (f, partner) if f.dark else (partner, f)
    return f"# {HEADER}\n\n[Palette]\nName={f.name}\n\n{face(light, 'Light')}\n{face(dark, 'Dark')}"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    return [
        Out(
            f"{f.slug}.palette",
            palette(f, by_id),
            flavor=f.id,
            dest=f"~/.local/share/org.gnome.Ptyxis/palettes/{f.slug}.palette",
            lang="ini",
        )
        for f in flavors
    ]
