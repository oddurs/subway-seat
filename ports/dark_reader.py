"""Dark Reader: the custom colors to paste into its Colors panel, per flavor."""

import json

from ports._lib import HEADER, Out, selection

META = {
    "id": "dark-reader",
    "name": "Dark Reader",
    "category": "Apps",
    "homepage": "https://darkreader.org",
    "enable": {
        "where": "Dark Reader › See all options › Colors",
        "code": "Paste the values from {slug}.json: Background, Text, Scrollbar and Selection,\n"
        "once with Dark mode on and once with Light mode on.",
        "lang": "text",
    },
    "auto": {
        "where": "Dark Reader › Settings › Automation",
        "code": "Turn on “Use system color scheme”, then set the behavior to “Toggle dark/light”.",
        "lang": "text",
    },
    "notes": "Dark Reader takes a background and a text color for each of its dark and light schemes, plus a "
    "scrollbar and a selection color, so the file is just those. The keys are Dark Reader's own setting names.",
}


def scheme(dark, light, active):
    return {
        "_comment": HEADER,
        "name": active.name,
        "mode": 1 if active.dark else 0,  # Dark Reader's own encoding: 1 = dark, 0 = light
        "darkSchemeBackgroundColor": dark.base,
        "darkSchemeTextColor": dark.text,
        "lightSchemeBackgroundColor": light.base,
        "lightSchemeTextColor": light.text,
        "scrollbarColor": selection(active),
        "selectionColor": selection(active),
    }


def build(flavors):
    by = {f.id: f for f in flavors}
    outs = []
    for f in flavors:
        dark = f if f.dark else by["walnut"]
        body = json.dumps(scheme(dark, by["enamel"], f), indent=2) + "\n"
        outs.append(Out(f"{f.slug}.json", body, flavor=f.id, lang="json",
                        how="copy the values into Dark Reader › See all options › Colors"))
    return outs
