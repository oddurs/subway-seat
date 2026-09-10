"""GitHub Copilot CLI, Amp and goose: agents without theme files that draw with
the terminal's 16 colors. The files are the settings that make them do so."""

from ports._lib import HEADER, MARK_END, MARK_START, Out

META = {
    "id": "terminal-agents",
    "name": "Copilot CLI, Amp & goose",
    "category": "Agents",
    "homepage": "https://github.com/github/copilot-cli",
    "enable": {
        "where": "each agent, inside a terminal running a Subway Seat theme",
        "code": "/settings theme default   # GitHub Copilot CLI (Base-16 terminal colors)\n"
        "/t ansi                   # goose (saved as GOOSE_CLI_THEME)\n"
        "# Amp: nothing to set",
        "lang": "text",
    },
    "detect": ["copilot", "goose", "amp"],
    "notes": "These agents have no theme files; they use your terminal's colors, so a Subway Seat "
    "terminal theme dresses them too. Copilot CLI needs its `default` theme and goose "
    "(github.com/aaif-goose/goose) its `ansi` theme; Amp needs nothing.",
}


def build(flavors):
    return [
        Out("copilot-settings.json", '{\n  "theme": "default"\n}\n',
            how="merge into ~/.copilot/settings.json", lang="json"),
        Out("goose-config.yaml",
            f"{MARK_START}\n# {HEADER}\n# goose's ANSI markdown theme draws with your terminal's colors.\n"
            f"GOOSE_CLI_THEME: ansi\n{MARK_END}\n",
            dest="~/.config/goose/config.yaml", append=True, lang="yaml"),
    ]
