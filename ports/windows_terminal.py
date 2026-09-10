"""Windows Terminal: a color scheme and a matching window theme per flavor, plus a
schemes-only JSON fragment Windows Terminal picks up without editing settings.json."""

import json

from ports._lib import Out, selection
from ports._terminals import lit

META = {
    "id": "windows-terminal",
    "name": "Windows Terminal",
    "category": "Terminals",
    "homepage": "https://learn.microsoft.com/windows/terminal/",
    "detect": ["wt.exe"],
    "enable": {
        "where": "settings.json (Settings › Open JSON file), after merging the `schemes` and `themes` entries",
        "code": '// at the top level\n"theme": "{name}",\n'
        '// inside your existing "profiles": {{ "defaults": {{ … }} }}\n"colorScheme": "{name}"',
        "lang": "json",
    },
    "auto": {
        "where": "settings.json, with every flavor's `schemes` and `themes` merged (subway-seat-all.json)",
        "code": '// at the top level\n"theme": { "light": "Subway Seat Enamel", "dark": "Subway Seat" },\n'
        '// inside your existing "profiles": { "defaults": { … } }\n'
        '"colorScheme": { "light": "Subway Seat Enamel", "dark": "Subway Seat" }',
        "lang": "json",
    },
    "notes": "Each flavor is a color scheme plus a theme for the tab row, tabs and window frame. The fragment "
    "adds all three schemes on its own; the themes still go into settings.json.",
}

NAMES = ["black", "red", "green", "yellow", "blue", "purple", "cyan", "white"]
MERGE = "Merge into the top-level `schemes` and `themes` arrays of settings.json (Settings › Open JSON file)"


def scheme(f):
    s = {
        "name": f.name,
        "background": f.base,
        "foreground": f.text,
        "cursorColor": lit(f),
        "selectionBackground": selection(f),
    }
    s |= dict(zip(NAMES, f.ansi[:8], strict=True))
    s |= {"bright" + n.title(): c for n, c in zip(NAMES, f.ansi[8:], strict=True)}
    return s


def theme(f):
    return {
        "name": f.name,
        "window": {
            "applicationTheme": "dark" if f.dark else "light",
            "useMica": False,
            "frame": f"{f.crust}FF",
            "unfocusedFrame": f"{f.crust}FF",
        },
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
            lang="json",
            how=MERGE,
        )
        for f in flavors
    ]
    outs.append(
        Out(
            "subway-seat-all.json",
            dump({"schemes": [scheme(f) for f in flavors], "themes": [theme(f) for f in flavors]}),
            lang="json",
            how=MERGE,
        )
    )
    outs.append(
        Out(
            "fragment/subway-seat.json",
            dump({"schemes": [scheme(f) for f in flavors]}),
            dest=r"%LOCALAPPDATA%\Microsoft\Windows Terminal\Fragments\SubwaySeat\subway-seat.json",
            lang="json",
        )
    )
    return outs
