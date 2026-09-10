from ports._cli import ink
from ports._lib import HEADER, Out

META = {
    "id": "lazygit",
    "name": "lazygit",
    "category": "CLI & TUI",
    "homepage": "https://github.com/jesseduffield/lazygit",
    "enable": {
        "where": "your shell (lazygit merges every file listed in LG_CONFIG_FILE)",
        "code": "set -Ux LG_CONFIG_FILE (lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/{slug}.yml",
        "lang": "fish",
    },
    "notes": "Orange borders on the focused panel, gold while searching, and warm grounds for the "
    "selected line. Pair it with the delta port for on-theme diffs.",
}


def theme(f):
    rows = {
        "activeBorderColor": [f.orange, "bold"],
        "inactiveBorderColor": [f.overlay0],
        "searchingActiveBorderColor": [f.yellow, "bold"],
        "optionsTextColor": [f.yellow],
        "selectedLineBgColor": [f.surface1],
        "inactiveViewSelectedLineBgColor": [f.surface0],
        "cherryPickedCommitFgColor": [f.clay],
        "cherryPickedCommitBgColor": [f.surface1],
        "markedBaseCommitFgColor": [ink(f)],
        "markedBaseCommitBgColor": [f.yellow],
        "unstagedChangesColor": [f.red_hi],
        "defaultFgColor": [f.text],
    }
    lines = []
    for key, values in rows.items():
        lines.append(f"    {key}:")
        lines += [f"      - '{v}'" for v in values]
    body = "\n".join(lines)
    return f"# {HEADER}\n# {f.name} for lazygit.\ngui:\n  theme:\n{body}\n  authorColors:\n    '*': '{f.sage}'\n"


def build(flavors):
    return [
        Out(f"{f.slug}.yml", theme(f), flavor=f.id, dest=f"~/.config/lazygit/{f.slug}.yml", lang="yaml")
        for f in flavors
    ]
