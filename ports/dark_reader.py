"""Dark Reader: the custom colours to paste into its Colors panel, per flavor."""

import json

from ports._apps import select
from ports._lib import HEADER, Out

META = {
    "id": "dark-reader",
    "name": "Dark Reader",
    "category": "Apps",
    "homepage": "https://darkreader.org",
    "enable": {
        "where": "Dark Reader → See all options → Colors",
        "code": "Paste the values from {slug}.json: background, text, selection\n"
        "(set Selection from Automatic to Custom first).",
        "lang": "text",
    },
    "notes": "Dark Reader takes only a background, a text colour and a selection colour, so this is just "
    "those, for both its dark and light schemes. Keys match Dark Reader's own setting names.",
}


def scheme(dark, light, active):
    return {
        "_comment": HEADER,
        "name": active.name,
        "mode": "dark" if active.dark else "light",
        "darkSchemeBackgroundColor": dark.base,
        "darkSchemeTextColor": dark.text,
        "lightSchemeBackgroundColor": light.base,
        "lightSchemeTextColor": light.text,
        "selectionColor": select(active),
        "scrollbarColor": active.surface2 if active.dark else active.surface1,
    }


def build(flavors):
    by = {f.id: f for f in flavors}
    outs = []
    for f in flavors:
        dark = f if f.dark else by["walnut"]
        body = json.dumps(scheme(dark, by["enamel"], f), indent=2) + "\n"
        outs.append(Out(f"{f.slug}.json", body, flavor=f.id, dest="Dark Reader → See all options → Colors",
                        lang="json"))
    return outs
