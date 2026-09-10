import palette as p
from ports._lib import Out
from ports._palettes import label

META = {
    "id": "txt",
    "name": "Hex list",
    "category": "Palettes",
    "homepage": "https://coolors.co",
    "enable": {
        "where": "Coolors, Figma plugins, or anything that takes pasted hex codes",
        "code": "cut -d' ' -f1 {slug}.txt | pbcopy",
        "lang": "sh",
    },
    "notes": "Plain text, one colour per line as #hex and its name. Most palette tools will take a paste of it.",
}


def build(flavors):
    return [
        Out(f"{f.slug}.txt", "".join(f"{f.colors[r]} {label(r)}\n" for r in p.ROLES), flavor=f.id,
            dest="anywhere; paste it where you need it", lang="text")
        for f in flavors
    ]
