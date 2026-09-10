from ports._cli import bar, row
from ports._lib import HEADER, Out, ink
from ports.bat import tmtheme

META = {
    "id": "gitui",
    "name": "gitui",
    "category": "CLI & TUI",
    "homepage": "https://github.com/gitui-org/gitui",
    "enable": {
        "where": "the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron)",
        "code": "gitui -t {slug}.ron",
        "lang": "sh",
    },
    "requires": "gitui 0.28+",
    "detect": ["gitui"],
    "notes": "Orange titles on the focused panel, avocado added and redbird removed lines that keep "
    "their color when selected, gold commit hashes. The file viewer's syntax colors come from the "
    "tmTheme next to it.",
}


def theme(f):
    rows = {
        "selected_tab": f.orange,
        "command_fg": f.text,
        "selection_bg": row(f),
        "selection_fg": f.text_hi,
        "cmdbar_bg": bar(f),
        # also hunk headers and unfocused borders, so a step brighter than the gutter color
        "disabled_fg": f.overlay1,
        "diff_line_add": f.green,
        "diff_line_delete": f.red_hi,
        "diff_file_added": f.green,
        "diff_file_removed": f.red_hi,
        "diff_file_moved": f.sage,
        "diff_file_modified": f.yellow,
        "commit_hash": f.yellow,
        "commit_time": f.subtext0,
        "commit_author": f.sage,
        "danger_fg": f.red_hi,
        "push_gauge_bg": f.orange,
        "push_gauge_fg": ink(f),
        "tag_fg": f.clay,
        "branch_fg": f.green,
        "block_title_focused": f.orange,
        "syntax": f.slug,
    }
    body = ",\n".join(f'    {k}: Some("{v}")' for k, v in rows.items())
    # keep the diff's avocado and redbird on the selected line instead of recoloring it
    body += ",\n    use_selection_fg: Some(false)"
    return f"// {HEADER}\n// {f.name} for gitui.\n(\n{body},\n)\n"


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(Out(f"{f.slug}.ron", theme(f), flavor=f.id, dest=f"~/.config/gitui/{f.slug}.ron", lang="ron"))
        outs.append(Out(f"{f.slug}.tmTheme", tmtheme(f), flavor=f.id,
                        dest=f"~/.config/gitui/{f.slug}.tmTheme", lang="xml"))
    return outs
