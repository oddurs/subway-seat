import palette as p
from ports._lib import Out
from ports._palettes import label

META = {
    "id": "txt",
    "name": "Hex list",
    "category": "Palettes",
    "homepage": "https://oddurs.github.io/subway-seat/palette/",
    "enable": {
        "where": "a terminal: copy the hex codes, for Coolors, Figma plugins or anything that takes a paste",
        "code": "cut -d' ' -f1 {slug}.txt | pbcopy          # macOS\n"
        "cut -d' ' -f1 {slug}.txt | wl-copy         # Linux, Wayland\n"
        "cut -d' ' -f1 {slug}.txt | xclip -sel clip # Linux, X11",
        "lang": "sh",
    },
    "notes": "Plain text, one color per line as #hex and its name. Most palette tools will take a paste of it.",
}


def build(flavors):
    return [
        Out(f"{f.slug}.txt", "".join(f"{f.colors[r]} {label(r, f)}\n" for r in p.ROLES), flavor=f.id, lang="text",
            how="paste it wherever you need the colors")
        for f in flavors
    ]
