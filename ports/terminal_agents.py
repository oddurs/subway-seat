"""GitHub Copilot CLI, Amp and Goose: agents without theme files that draw with
the terminal's 16 colors. The files are the settings that make them do so."""

from ports._lib import HEADER, Out

META = {
    "id": "terminal-agents",
    "name": "Copilot CLI, Amp & Goose",
    "category": "Agents",
    "homepage": "https://github.com/github/copilot-cli",
    "enable": {
        "where": "each agent, inside a terminal running a Subway Seat theme",
        "code": "/settings theme default   # GitHub Copilot CLI (Base-16 terminal colors)\n"
        "/t ansi                   # Goose (saved as GOOSE_CLI_THEME)\n"
        "# Amp: nothing to set",
        "lang": "text",
    },
    "notes": "These agents have no theme files; they use your terminal's colors, so a Subway Seat "
    "terminal theme dresses them too. Copilot CLI needs its `default` theme and Goose its `ansi` theme; Amp needs nothing.",
}


def build(flavors):
    return [
        Out("copilot-settings.json", '{\n  "theme": "default"\n}\n',
            dest="merged into ~/.copilot/settings.json", lang="json"),
        Out("goose-config.yaml", f"# {HEADER}\n# goose's ANSI markdown theme draws with your terminal's colors.\nGOOSE_CLI_THEME: ansi\n",
            dest="~/.config/goose/config.yaml", append=True, lang="yaml"),
    ]
