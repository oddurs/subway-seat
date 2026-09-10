"""Konsole: a .colorscheme per flavor."""

from ports._lib import HEADER, Out, rgb
from ports._terminals import dim

META = {
    "id": "konsole",
    "name": "Konsole",
    "category": "Terminals",
    "homepage": "https://konsole.kde.org",
    "enable": {
        "where": "Settings › Edit Current Profile › Appearance, or the profile file",
        "code": "# ~/.local/share/konsole/<your profile>.profile\n[Appearance]\nColorScheme={slug}",
        "lang": "ini",
    },
    "notes": "Background, foreground and the eight colours, each with intense (bright) and faint variants.",
}


def entry(name, color):
    return f"[{name}]\nColor={','.join(str(v) for v in rgb(color))}\n"


def scheme(f):
    parts = [
        entry("Background", f.base),
        entry("BackgroundFaint", f.base),
        entry("BackgroundIntense", f.base),
    ]
    for i in range(8):
        parts += [
            entry(f"Color{i}", f.ansi[i]),
            entry(f"Color{i}Faint", dim(f, f.ansi[i])),
            entry(f"Color{i}Intense", f.ansi[i + 8]),
        ]
    parts += [
        entry("Foreground", f.text),
        entry("ForegroundFaint", f.overlay2),
        entry("ForegroundIntense", f.text_hi),
        f"[General]\nBlur=false\nColorRandomization=false\nDescription={f.name}\nOpacity=1\nWallpaper=\n",
    ]
    return f"# {HEADER}\n\n" + "\n".join(parts)


def build(flavors):
    return [
        Out(
            f"{f.slug}.colorscheme",
            scheme(f),
            flavor=f.id,
            dest=f"~/.local/share/konsole/{f.slug}.colorscheme",
            lang="ini",
        )
        for f in flavors
    ]
