"""X resources: colours for xterm, urxvt, st and anything else that reads *.colorN."""

from ports._lib import HEADER, Out
from ports._terminals import ANSI_NAMES, lit, selection

META = {
    "id": "xresources",
    "name": "Xresources",
    "category": "Terminals",
    "homepage": "https://wiki.archlinux.org/title/X_resources",
    "enable": {
        "where": "~/.Xresources, then run `xrdb -merge ~/.Xresources`",
        "code": '#include "{slug}.Xresources"',
        "lang": "conf",
    },
    "notes": "Foreground, background, cursor, selection and the 16 ANSI colours as wildcard resources, "
    "so xterm, urxvt and other X terminals all pick them up.",
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
        Out(f"{f.slug}.Xresources", resources(f), flavor=f.id, dest=f"~/{f.slug}.Xresources", lang="conf")
        for f in flavors
    ]
