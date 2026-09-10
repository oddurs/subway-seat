"""fastfetch: a small config per flavor with the key, title and logo colors."""

import json

from ports._lib import HEADER, Out

META = {
    "id": "fastfetch",
    "name": "fastfetch",
    "category": "CLI & TUI",
    "homepage": "https://github.com/fastfetch-cli/fastfetch",
    "detect": ["fastfetch"],
    "requires": "fastfetch 2.14+",
    "enable": {
        "where": "your shell or an alias",
        "code": "fastfetch --config {slug}",
        "lang": "sh",
    },
    "notes": "Gold keys, an orange title, quiet separators, and percentage bars and temperatures that go "
    "avocado, gold, redbird. Logo colors are repainted along the 70s stripe, so the Apple logo comes out in "
    "avocado, gold, orange, redbird, terracotta and denim. The file lists fastfetch's default modules; "
    "to keep your own, copy its logo and display blocks into config.jsonc instead.",
}


# fastfetch shows nothing for a config without a module list, so this is the default list
# (`fastfetch --gen-config`, 2.68).
MODULES = [
    "title", "separator", "os", "host", "kernel", "uptime", "packages", "shell", "display", "de", "wm",
    "wmtheme", "theme", "icons", "font", "cursor", "terminal", "terminalfont", "cpu", "gpu", "memory", "swap",
    "disk", "localip", "battery", "poweradapter", "locale", "break", "colors",
]  # fmt: skip


def config(f):
    stripe = [f.green, f.yellow, f.orange, f.red, f.clay, f.denim, f.sage, f.orange_hi, f.yellow_hi]
    states = {"green": f.green, "yellow": f.yellow, "red": f.red_hi}
    doc = {
        "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
        "logo": {"color": {str(i): c for i, c in enumerate(stripe, 1)}},
        "display": {
            "color": {"keys": f.yellow, "title": f.orange, "output": f.text, "separator": f.overlay1},
            "percent": {"color": states},
            "temp": {"color": states},
        },
        "modules": MODULES,
    }
    return f"// {HEADER}\n// {f.name} for fastfetch.\n{json.dumps(doc, indent=2)}\n"


def build(flavors):
    return [
        Out(f"{f.slug}.jsonc", config(f), flavor=f.id, dest=f"~/.config/fastfetch/{f.slug}.jsonc", lang="json")
        for f in flavors
    ]
