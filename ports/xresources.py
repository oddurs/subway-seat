"""X resources: colors for xterm, urxvt, st and anything else that reads *.colorN."""

from ports._lib import ANSI_NAMES, HEADER, Out, selection
from ports._terminals import lit

META = {
    "id": "xresources",
    "name": "Xresources",
    "category": "Terminals",
    "homepage": "https://wiki.archlinux.org/title/X_resources",
    "detect": ["xrdb"],
    "enable": {
        "where": "~/.Xresources, then run `xrdb -merge ~/.Xresources`",
        "code": '#include ".config/X11/{slug}.Xresources"',
        "lang": "conf",
    },
    "notes": "Foreground, background, cursor, selection and the 16 ANSI colors as wildcard resources, "
    "so xterm, urxvt and other X terminals all pick them up. X resources are read once, so there's no "
    "light/dark following; pick one flavor.",
}


def resources(f):
    rows = [
        f"*.foreground: {f.text}",
        f"*.background: {f.base}",
        f"*.cursorColor: {lit(f)}",
        f"*.highlightColor: {selection(f)}",
        f"*.highlightTextColor: {f.text_hi}",
    ]
    for i, name in enumerate(ANSI_NAMES):
        rows += ["", f"! {name}", f"*.color{i}: {f.ansi[i]}", f"*.color{i + 8}: {f.ansi[i + 8]}"]
    return f"! {HEADER}\n! {f.name}\n\n" + "\n".join(rows) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.Xresources", resources(f), flavor=f.id, dest=f"~/.config/X11/{f.slug}.Xresources", lang="conf")
        for f in flavors
    ]
