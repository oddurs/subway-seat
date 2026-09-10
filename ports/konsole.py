"""Konsole: a .colorscheme per flavor, plus a profile that uses it and sets the cursor
colors, which a color scheme can't carry."""

from ports._lib import HEADER, Out, rgb
from ports._terminals import dim, lit

META = {
    "id": "konsole",
    "name": "Konsole",
    "category": "Terminals",
    "homepage": "https://apps.kde.org/konsole/",
    "detect": ["konsole"],
    "enable": {
        "where": "~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default",
        "code": "[Desktop Entry]\nDefaultProfile={name}.profile",
        "lang": "ini",
    },
    "notes": "Background, foreground and the eight colors, each with intense (bright) and faint variants; the "
    "profile adds the cursor, focus border and tab activity colors. To keep your own profile instead, set "
    "`ColorScheme=subway-seat` (or `-tunnel`, `-enamel`) under its `[Appearance]`. Konsole doesn't follow "
    "the system light/dark setting, so pick one flavor.",
}


def triple(color):
    return ",".join(str(v) for v in rgb(color))


def entry(name, color):
    return f"[{name}]\nColor={triple(color)}\n"


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


def profile(f):
    return (
        f"# {HEADER}\n\n"
        f"[Appearance]\nColorScheme={f.slug}\nFocusBorderColor={triple(lit(f))}\nTabActivityColor={triple(f.orange)}\n\n"
        f"[Cursor Options]\nCustomCursorColor={triple(lit(f))}\nCustomCursorTextColor={triple(f.base)}\n"
        "UseCustomCursorColor=true\n\n"
        f"[General]\nName={f.name}\nParent=FALLBACK/\n"
    )


def build(flavors):
    outs = []
    for f in flavors:
        outs += [
            Out(
                f"{f.slug}.colorscheme",
                scheme(f),
                flavor=f.id,
                dest=f"~/.local/share/konsole/{f.slug}.colorscheme",
                lang="ini",
            ),
            Out(
                f"{f.name}.profile",
                profile(f),
                flavor=f.id,
                dest=f"~/.local/share/konsole/{f.name}.profile",
                lang="ini",
            ),
        ]
    return outs
