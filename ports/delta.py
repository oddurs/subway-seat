from ports._lib import HEADER, Out, tints

META = {
    "id": "delta",
    "name": "delta",
    "category": "CLI & TUI",
    "homepage": "https://github.com/dandavison/delta",
    "enable": {
        "where": "~/.gitconfig (include the file first)",
        "code": "[delta]\n\tfeatures = {slug}",
        "lang": "conf",
    },
    "notes": "Each flavor is a delta feature: diff tints, line numbers, file and hunk headers. "
    "Syntax colors come from the bat theme, so install that too.",
}


def feature(f):
    t = tints(f)
    return f"""[delta "{f.slug}"]
	dark = {"true" if f.dark else "false"}
	syntax-theme = {f.name}
	plus-style = syntax "{t['add']}"
	plus-emph-style = syntax "{t['add_emph']}"
	minus-style = syntax "{t['del']}"
	minus-emph-style = syntax "{t['del_emph']}"
	map-styles = bold purple => syntax "{f.mix('clay', 'base', 0.25)}", bold cyan => syntax "{f.mix('sage', 'base', 0.25)}"
	line-numbers-plus-style = "{f.green}"
	line-numbers-minus-style = "{f.red_hi}"
	line-numbers-zero-style = "{f.overlay0}"
	line-numbers-left-style = "{f.surface2}"
	line-numbers-right-style = "{f.surface2}"
	file-style = "{f.yellow}" bold
	file-decoration-style = "{f.orange}" ul
	hunk-header-style = file line-number syntax
	hunk-header-decoration-style = "{f.surface2}" box
	hunk-header-line-number-style = "{f.orange}"
	commit-decoration-style = "{f.orange}" box
	blame-palette = "{f.base} {f.mantle} {f.surface0}"
	merge-conflict-begin-symbol = ~
	merge-conflict-end-symbol = ~
	merge-conflict-ours-diff-header-style = "{f.yellow}" bold
	merge-conflict-theirs-diff-header-style = "{f.sage}" bold
"""


def build(flavors):
    outs = [
        Out(f"{f.slug}.gitconfig", f"# {HEADER}\n{feature(f)}", flavor=f.id,
            dest=f"~/.config/delta/{f.slug}.gitconfig", lang="conf")
        for f in flavors
    ]
    outs.append(Out("themes.gitconfig", f"# {HEADER}\n" + "\n".join(feature(f) for f in flavors),
                    dest="~/.config/delta/subway-seat.gitconfig", lang="conf"))
    return outs
