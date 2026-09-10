from ports._cli import row
from ports._lib import HEADER, Out, ink

LG = "$HOME/.config/lazygit"

META = {
    "id": "lazygit",
    "name": "lazygit",
    "category": "CLI & TUI",
    "homepage": "https://github.com/jesseduffield/lazygit",
    "enable": {
        "where": "fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops "
        "if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list",
        "code": "set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml\n"
        f'set -Ux LG_CONFIG_FILE "$dir/config.yml,{LG}/{{slug}}.yml"',
        "lang": "fish",
        "sh": 'dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"\n'
        f"# then in ~/.zshrc or ~/.bashrc:\n"
        f'export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,{LG}/{{slug}}.yml"',
    },
    "detect": ["lazygit"],
    "notes": "Orange borders on the focused panel, gold while searching, warm grounds for the selected "
    "line, and copied and rebase-base commits marked in sage and gold. The diff pane shows git's own "
    "colors, so install the git port; or add the `-delta.yml` file to run diffs through delta with "
    "the delta port's feature (it uses `git.diffRenderers`, the key in lazygit 0.65; older releases "
    "call it `git.paging`).",
}


def theme(f):
    rows = {
        "activeBorderColor": [f.orange, "bold"],
        "inactiveBorderColor": [f.overlay0],
        "searchingActiveBorderColor": [f.yellow, "bold"],
        "optionsTextColor": [f.yellow],
        "selectedLineBgColor": [row(f)],
        "inactiveViewSelectedLineBgColor": [f.surface0 if f.dark else f.mantle],
        "cherryPickedCommitFgColor": [ink(f)],
        "cherryPickedCommitBgColor": [f.sage],
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


def delta(f):
    return f"""# {HEADER}
# {f.name}: lazygit's diff pane through delta, with the delta port's {f.slug} feature.
# Needs delta, the delta port's include in your gitconfig, and the bat theme.
git:
  diffRenderers:
    - colorArg: always
      command: delta --features {f.slug} --paging=never
"""


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(Out(f"{f.slug}.yml", theme(f), flavor=f.id, dest=f"~/.config/lazygit/{f.slug}.yml", lang="yaml"))
        outs.append(Out(f"{f.slug}-delta.yml", delta(f), flavor=f.id,
                        dest=f"~/.config/lazygit/{f.slug}-delta.yml", lang="yaml"))
    return outs
