from ports._cli import MOVED
from ports._lib import HEADER, Out, tints

META = {
    "id": "delta",
    "name": "delta",
    "category": "CLI & TUI",
    "homepage": "https://github.com/dandavison/delta",
    "enable": {
        "where": "~/.gitconfig or ~/.config/git/config, with delta already set as your pager. "
        "If you have a `features` line, add the flavor to it instead",
        "code": "[include]\n\tpath = ~/.config/delta/{slug}.gitconfig\n[delta]\n\tfeatures = {slug}",
        "lang": "ini",
    },
    "detect": ["delta"],
    "notes": "Each flavor is a delta feature. Code keeps its syntax colors on avocado and redbird "
    "line tints, changed words sit on a stronger tint, and line numbers take the tint of their line. "
    "Moved code (with `diff.colorMoved`) gets fainter tints, in step with the git port. Syntax colors "
    "come from the bat theme of the same name, so install the bat port and run `bat cache --build`.",
}


def feature(f):
    t = tints(f)
    # moved code: fainter tints than real changes; the alternative blocks of a zebra use the change tint
    ground = {
        "oldMoved": t["del_dim"], "oldMovedAlternative": t["chg"],
        "newMoved": t["add_dim"], "newMovedAlternative": t["chg"],
    }
    moved = ", ".join(
        f'{git} => syntax "{ground[slot]}", bold "{f.colors[role]}" => syntax "{ground[slot]}"'
        for slot, (role, git) in MOVED.items()
    )
    blame = [f.base, f.mantle, f.surface0] if f.dark else [f.base, f.mantle, f.crust]
    return f"""[delta "{f.slug}"]
	{"dark" if f.dark else "light"} = true
	syntax-theme = {f.name}
	# changed lines: syntax colors on a tint; changed words on a stronger one
	plus-style = syntax "{t['add']}"
	plus-non-emph-style = syntax "{t['add']}"
	plus-emph-style = syntax "{t['add_emph']}"
	minus-style = syntax "{t['del']}"
	minus-non-emph-style = syntax "{t['del']}"
	minus-emph-style = syntax "{t['del_emph']}"
	zero-style = syntax
	whitespace-error-style = normal "{f.red}"
	# git --color-moved: git's defaults and the git port's colors
	map-styles = {moved}
	# line numbers (with line-numbers = true) in the color of their change
	line-numbers-plus-style = "{f.green}"
	line-numbers-minus-style = "{f.red_hi}"
	line-numbers-zero-style = "{f.overlay1}"
	line-numbers-left-style = "{f.overlay0}"
	line-numbers-right-style = "{f.overlay0}"
	# file and hunk headers
	file-style = "{f.text_hi}" bold
	file-decoration-style = "{f.orange}" ul
	hunk-header-style = file line-number syntax
	hunk-header-file-style = "{f.subtext1}"
	hunk-header-line-number-style = "{f.denim}"
	hunk-header-decoration-style = "{f.denim}" box
	commit-decoration-style = "{f.yellow}" box
	inline-hint-style = "{f.overlay1}"
	# git blame
	blame-palette = "{' '.join(blame)}"
	blame-separator-style = "{f.overlay0}"
	# git grep / rg --json
	grep-file-style = "{f.orange}"
	grep-line-number-style = "{f.green}"
	grep-match-line-style = syntax
	grep-match-word-style = "{f.text_hi}" "{t['search']}" bold
	grep-header-file-style = "{f.orange}" bold
	# merge conflicts (git's diff3 or zdiff3 conflict style)
	merge-conflict-ours-diff-header-style = "{f.yellow}" bold
	merge-conflict-ours-diff-header-decoration-style = "{f.yellow}" box
	merge-conflict-theirs-diff-header-style = "{f.sage}" bold
	merge-conflict-theirs-diff-header-decoration-style = "{f.sage}" box
"""


def build(flavors):
    outs = [
        Out(f"{f.slug}.gitconfig", f"# {HEADER}\n{feature(f)}", flavor=f.id,
            dest=f"~/.config/delta/{f.slug}.gitconfig", lang="ini")
        for f in flavors
    ]
    # every flavor in one file (include this one instead to switch with `features` alone)
    outs.append(Out("themes.gitconfig", f"# {HEADER}\n" + "\n".join(feature(f) for f in flavors),
                    dest="~/.config/delta/subway-seat-flavors.gitconfig", lang="ini"))
    return outs
