from ports._cli import MOVED, git_color
from ports._lib import HEADER, Out, tints

META = {
    "id": "git",
    "name": "Git",
    "category": "CLI & TUI",
    "homepage": "https://git-scm.com",
    "enable": {
        "where": "~/.config/git/config or ~/.gitconfig (an [include] at the end is fine)",
        "code": "[include]\n\tpath = ~/.config/git/{slug}.gitconfig",
        "lang": "ini",
        "file": "~/.config/git/config",
    },
    "detect": ["git"],
    "notes": "Git's own colors in palette hex: avocado added and redbird removed lines, denim hunk "
    "headers, bold file headers, moved code (with `diff.colorMoved`), diff-highlight words, status, "
    "branches, log decorations, grep and `add -p`. lazygit shows these in its diff pane when it runs "
    "without delta. With delta, delta draws the diffs and reads the same moved-code colors; context "
    "lines and grep matches stay on git's defaults so delta can recognize them.",
}


def colors(f):
    """{section: {slot: value}} for the gitconfig."""
    t = tints(f)
    bold, dim = "bold", "dim"
    moved = {slot: git_color(f.colors[role], bold) for slot, (role, _) in MOVED.items()}
    return {
        # `context` stays unset: delta keeps syntax colors only on context lines git leaves plain
        "color.diff": {
            "meta": git_color(f.text_hi, bold),
            "frag": git_color(f.denim),
            "func": git_color(f.subtext1),
            "old": git_color(f.red_hi),
            "new": git_color(f.green),
            "commit": git_color(f.yellow),
            "whitespace": git_color("normal", f.red),
            **moved,
            "oldMovedDimmed": git_color(f.overlay1),
            "oldMovedAlternativeDimmed": git_color(f.overlay1, "italic"),
            "newMovedDimmed": git_color(f.overlay1),
            "newMovedAlternativeDimmed": git_color(f.overlay1, "italic"),
            # git range-diff
            "contextDimmed": git_color(f.overlay1),
            "oldDimmed": git_color(f.red_hi, dim),
            "newDimmed": git_color(f.green, dim),
            "contextBold": git_color(f.text_hi, bold),
            "oldBold": git_color(f.red_hi, bold),
            "newBold": git_color(f.green, bold),
        },
        # contrib/diff-highlight (and anything that reads these keys): changed words on a tint
        "color.diff-highlight": {
            "oldNormal": git_color(f.red_hi),
            "oldHighlight": git_color(f.red_hi, t["del_emph"]),
            "newNormal": git_color(f.green),
            "newHighlight": git_color(f.green, t["add_emph"]),
        },
        "color.status": {
            "header": git_color(f.subtext1),
            "added": git_color(f.green),
            "changed": git_color(f.red_hi),
            "untracked": git_color(f.clay),
            "branch": git_color(f.green, bold),
            "nobranch": git_color(f.red_hi, bold),
            "localBranch": git_color(f.green),
            "remoteBranch": git_color(f.red_hi),
            "unmerged": git_color(f.red_hi, bold),
        },
        "color.branch": {
            "current": git_color(f.green, bold),
            "local": git_color(f.text),
            "remote": git_color(f.red_hi),
            "upstream": git_color(f.denim),
            "plain": git_color(f.subtext1),
            "worktree": git_color(f.sage),
        },
        "color.decorate": {
            "HEAD": git_color(f.sage, bold),
            "branch": git_color(f.green, bold),
            "remoteBranch": git_color(f.red_hi, bold),
            "tag": git_color(f.yellow, bold),
            "stash": git_color(f.orange, bold),
            "grafted": git_color(f.denim, bold),
        },
        # `match` stays git's bold red (Redbird in the terminal ports): delta finds matches by it
        "color.grep": {
            "context": git_color(f.subtext0),
            "filename": git_color(f.orange),
            "function": git_color(f.yellow),
            "lineNumber": git_color(f.green),
            "column": git_color(f.green),
            "selected": git_color(f.text),
            "separator": git_color(f.overlay1),
        },
        "color.interactive": {
            "prompt": git_color(f.orange, bold),
            "header": git_color(f.text_hi, bold),
            "help": git_color(f.yellow),
            "error": git_color(f.red_hi, bold),
        },
        "color.blame": {
            # oldest → newest: faded, then plain, then burnt orange for the last month
            "highlightRecent": f'"{f.overlay1},12 month ago,{f.subtext1},1 month ago,{f.orange}"'.lower(),
            "repeatedLines": git_color(f.overlay1),
        },
        "color.advice": {"hint": git_color(f.yellow)},
        "color.push": {"error": git_color(f.red_hi)},
        "color.transport": {"rejected": git_color(f.red_hi)},
        "color.remote": {
            "hint": git_color(f.yellow),
            "warning": git_color(f.yellow, bold),
            "success": git_color(f.green, bold),
            "error": git_color(f.red_hi, bold),
        },
    }


def gitconfig(f):
    out = [f"# {HEADER}", f"# {f.name} for Git. Include it from your gitconfig:",
           f"#   [include] path = ~/.config/git/{f.slug}.gitconfig"]
    for section, slots in colors(f).items():
        name, _, sub = section.partition(".")
        out += ["", f'[{name} "{sub}"]']
        out += [f"\t{k} = {v}" for k, v in slots.items()]
    return "\n".join(out) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.gitconfig", gitconfig(f), flavor=f.id, dest=f"~/.config/git/{f.slug}.gitconfig", lang="ini")
        for f in flavors
    ]
