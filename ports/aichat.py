from ports._lib import Out
from ports.bat import tmtheme

META = {
    "id": "aichat",
    "name": "AIChat",
    "category": "CLI & TUI",
    "homepage": "https://github.com/sigoden/aichat",
    "enable": {
        "where": "aichat's config.yaml (`aichat --info` shows the folder: ~/Library/Application Support/aichat "
        "on macOS, ~/.config/aichat on Linux, or $AICHAT_CONFIG_DIR)",
        "code": "theme: dark   # light for Subway Seat Enamel",
        "lang": "yaml",
    },
    "auto": {
        "where": "aichat's config.yaml, with Walnut's dark.tmTheme and Enamel's light.tmTheme both in the folder",
        "code": "# no `theme:` line: AIChat asks the terminal and picks dark.tmTheme or light.tmTheme",
        "lang": "yaml",
    },
    "detect": ["aichat"],
    "notes": "AIChat reads `dark.tmTheme` or `light.tmTheme` from its config folder, so each flavor "
    "ships under the name AIChat looks for. Walnut and Tunnel are both dark; keep the one you like.",
}


def build(flavors):
    return [
        Out(f"{f.slug}/{'dark' if f.dark else 'light'}.tmTheme", tmtheme(f), flavor=f.id,
            dest=f"~/Library/Application Support/aichat/{'dark' if f.dark else 'light'}.tmTheme", lang="xml",
            how="on Linux the folder is ~/.config/aichat")
        for f in flavors
    ]
