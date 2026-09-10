"""Windows Terminal: a colour scheme and a matching window theme per flavor."""

import json

from ports._lib import Out
from ports._terminals import lit, selection

META = {
    "id": "windows-terminal",
    "name": "Windows Terminal",
    "category": "Terminals",
    "homepage": "https://github.com/microsoft/terminal",
    "enable": {
        "where": "settings.json (Settings › Open JSON file), after merging the `schemes` and `themes` entries",
        "code": '"theme": "{name}",\n"profiles": {{ "defaults": {{ "colorScheme": "{name}" }} }}',
        "lang": "json",
    },
    "notes": "Each flavor is a colour scheme plus a theme for the tab row and tabs. For light/dark "
    'following, use `"colorScheme": {"light": "Subway Seat Enamel", "dark": "Subway Seat"}` and the same '
    "shape for `theme`.",
}

NAMES = ["black", "red", "green", "yellow", "blue", "purple", "cyan", "white"]


def scheme(f):
    s = {
        "name": f.name,
        "background": f.base,
        "foreground": f.text,
        "cursorColor": lit(f),
        "selectionBackground": selection(f),
    }
    s |= dict(zip(NAMES, f.ansi[:8]))
    s |= {"bright" + n.title(): c for n, c in zip(NAMES, f.ansi[8:])}
    return s


def theme(f):
    return {
        "name": f.name,
        "window": {"applicationTheme": "dark" if f.dark else "light", "useMica": False},
        "tabRow": {"background": f"{f.crust}FF", "unfocusedBackground": f"{f.crust}FF"},
        "tab": {"background": f"{f.base}FF", "unfocusedBackground": f"{f.mantle}FF"},
    }


def dump(obj):
    return json.dumps(obj, indent=4) + "\n"


def build(flavors):
    outs = [
        Out(
            f"{f.slug}.json",
            dump({"schemes": [scheme(f)], "themes": [theme(f)]}),
            flavor=f.id,
            dest="settings.json → merge into the top-level `schemes` and `themes` arrays",
            lang="json",
        )
        for f in flavors
    ]
    outs.append(
        Out(
            "subway-seat-all.json",
            dump({"schemes": [scheme(f) for f in flavors], "themes": [theme(f) for f in flavors]}),
            dest="settings.json → merge into the top-level `schemes` and `themes` arrays",
            lang="json",
        )
    )
    return outs
