from ports._lib import Out
from ports.bat import tmtheme

META = {
    "id": "aichat",
    "name": "AIChat",
    "category": "CLI & TUI",
    "homepage": "https://github.com/sigoden/aichat",
    "enable": {
        "where": "aichat's config.yaml (`aichat --info` shows the config dir)",
        "code": "theme: dark   # light for Subway Seat Enamel",
        "lang": "yaml",
    },
    "notes": "AIChat reads `dark.tmTheme` or `light.tmTheme` from its config directory, so each flavor "
    "ships under the name AIChat looks for. Walnut and Tunnel are both dark; keep the one you like.",
}


def build(flavors):
    return [
        Out(f"{f.slug}/{'dark' if f.dark else 'light'}.tmTheme", tmtheme(f), flavor=f.id,
            dest=f"~/.config/aichat/{'dark' if f.dark else 'light'}.tmTheme", lang="xml")
        for f in flavors
    ]
