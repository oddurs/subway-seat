"""television: a theme file per flavor, in the fzf port's colors."""

from ports._lib import HEADER, Out, ink

META = {
    "id": "television",
    "name": "television",
    "category": "CLI & TUI",
    "homepage": "https://github.com/alexpasmantier/television",
    "detect": ["tv"],
    "requires": "television 0.10+",
    "enable": {
        "where": "the [ui] table of ~/.config/television/config.toml",
        "code": 'theme = "{slug}"',
        "lang": "toml",
    },
    "notes": "The fzf port's colors for tv: gold matches, a raised row for the selection, quiet counts and "
    "borders, and the mode badge in burnt orange. File previews come from bat, so the bat port colors "
    "those. tv falls back to its default theme without a word if a theme file doesn't parse.",
}


def theme(f):
    keys = {
        "# general": None,
        "background": f.base,
        "border_fg": f.surface2,
        "text_fg": f.text,
        "dimmed_text_fg": f.overlay1,
        "# input": None,
        "input_text_fg": f.text,
        "result_count_fg": f.overlay1,
        "# results": None,
        "result_name_fg": f.subtext1,
        "result_line_number_fg": f.overlay1,
        "result_value_fg": f.text,
        "selection_bg": f.surface0,
        "selection_fg": f.text_hi,
        "match_fg": f.yellow,
        "# preview": None,
        "preview_title_fg": f.subtext1,
        "# modes": None,
        "channel_mode_fg": ink(f),
        "channel_mode_bg": f.orange,
        "remote_control_mode_fg": ink(f),
        "remote_control_mode_bg": f.yellow,
        "action_picker_mode_fg": ink(f),
        "action_picker_mode_bg": f.sage,
    }
    lines = [f"# {HEADER}", f"# {f.name} for television."]
    for key, value in keys.items():
        lines.append(key if value is None else f"{key} = '{value}'")
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.toml", theme(f), flavor=f.id, dest=f"~/.config/television/themes/{f.slug}.toml", lang="toml")
        for f in flavors
    ]
