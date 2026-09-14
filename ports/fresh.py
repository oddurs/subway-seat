"""Fresh: a JSON theme per flavor, RGB triples, for the terminal IDE.

Keys follow crates/fresh-editor/plugins/schemas/theme.schema.json. `extends`
carries the built-in dark or light theme underneath, so this file only has to
name what Subway Seat actually decides — anything omitted inherits rather than
rendering black.

Fresh takes [r, g, b], not hex, which is why every value goes through rgb().
"""

import json

import palette as p
from ports._lib import Out, tints, ui_colors

META = {
    "id": "fresh",
    "name": "Fresh",
    "category": "Editors",
    "homepage": "https://getfresh.dev",
    "enable": {
        "where": "~/.config/fresh/config.json",
        "code": '{{\n  "theme": "{slug}.json"\n}}',
        "lang": "json",
    },
    "detect": ["fresh", "~/.config/fresh"],
    "notes": "Fresh reads themes from ~/.config/fresh/themes/. A theme names a file, "
    "not an id, so the .json extension is part of the value.",
}


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return [int(h[i : i + 2], 16) for i in (0, 2, 4)]


def syn(f, role):
    """A syntax entry: a bare colour, or one bundled with its modifiers."""
    name, mods = p.SYNTAX[role]
    color = rgb(f.colors[name])
    if not mods:
        return color
    return {"color": color, "modifier": sorted(mods)}


def theme(f):
    c = {r: rgb(v) for r, v in f.colors.items()}
    u = {k: rgb(v) for k, v in ui_colors(f).items()}
    t = {k: rgb(v) for k, v in tints(f).items()}

    editor = {
        "bg": u["base"],
        "fg": c["text"],
        "cursor": c["orange"],
        "inactive_cursor": c["overlay0"],
        "selection_bg": c["surface1"],
        "current_line_bg": c["surface0"],
        "line_number_fg": c["overlay0"],
        "line_number_bg": u["base"],
        "diff_add_bg": t["add"],
        "diff_remove_bg": t["del"],
        "diff_add_highlight_bg": t["add_emph"],
        "diff_remove_highlight_bg": t["del_emph"],
        "diff_modify_bg": t["chg"],
        "ruler_bg": c["surface0"],
        "indentation_guide_fg": c["surface2"],
        "whitespace_indicator_fg": c["surface2"],
        "whitespace_indicator_selected_fg": c["overlay0"],
        "bracket_match_fg": c["orange_hi"],
        "after_eof_bg": u["mantle"],
        # The two rainbows walk the accents in the order the palette lists
        # them, so nesting reads as a progression rather than a lucky draw.
        **{
            f"indent_rainbow_{i}": c[r]
            for i, r in enumerate(["overlay0", "denim", "sage", "yellow", "orange", "clay"], start=1)
        },
        **{
            f"bracket_rainbow_{i}": c[r]
            for i, r in enumerate(["orange", "yellow", "sage", "denim", "clay", "red"], start=1)
        },
    }

    ui = {
        "tab_active_fg": c["text_hi"],
        "tab_active_bg": u["base"],
        "tab_inactive_fg": c["overlay2"],
        "tab_inactive_bg": u["mantle"],
        "tab_separator_bg": u["mantle"],
        "tab_hover_bg": c["surface0"],
        "tab_close_hover_fg": c["red"],
        "menu_bg": u["mantle"],
        "menu_fg": c["subtext1"],
        "menu_active_bg": c["surface1"],
        "menu_active_fg": c["text_hi"],
        "menu_dropdown_bg": u["paper"],
        "menu_dropdown_fg": c["text"],
        "menu_highlight_bg": c["orange"],
        "menu_highlight_fg": u["crust"],
        "menu_border_fg": c["surface2"],
        "menu_separator_fg": c["surface1"],
        "menu_hover_bg": c["surface0"],
        "menu_hover_fg": c["text_hi"],
        "menu_disabled_fg": c["overlay0"],
        "status_bar_fg": c["subtext0"],
        "status_bar_bg": u["mantle"],
        "status_palette_fg": u["crust"],
        "status_palette_bg": c["orange"],
        "status_separator_fg": c["surface2"],
        "status_separator_bg": u["mantle"],
        "status_lsp_on_fg": c["green"],
        "status_lsp_on_bg": u["mantle"],
        "status_lsp_actionable_fg": c["yellow"],
        "status_lsp_actionable_bg": u["mantle"],
        "prompt_fg": c["text"],
        "prompt_bg": u["paper"],
        "prompt_selection_fg": u["crust"],
        "prompt_selection_bg": c["orange"],
        "popup_border_fg": c["surface2"],
        "popup_bg": u["paper"],
        "popup_text_fg": c["text"],
        "popup_selection_bg": c["surface1"],
        "popup_selection_fg": c["text_hi"],
        "text_input_selection_bg": c["surface1"],
        "suggestion_bg": u["paper"],
        "suggestion_fg": c["subtext1"],
        "suggestion_selected_bg": c["surface1"],
        "help_bg": u["paper"],
        "help_fg": c["subtext1"],
        "help_key_fg": c["orange"],
        "help_separator_fg": c["surface2"],
        "help_indicator_fg": c["subtext0"],
        "help_indicator_bg": u["mantle"],
        "inline_code_bg": c["surface0"],
        "split_separator_fg": c["surface1"],
        "split_separator_hover_fg": c["overlay0"],
        "scrollbar_track_fg": c["surface0"],
        "scrollbar_thumb_fg": c["surface2"],
        "scrollbar_track_hover_fg": c["surface1"],
        "scrollbar_thumb_hover_fg": c["overlay0"],
        "compose_margin_bg": u["mantle"],
        "blame_header_fg": c["overlay2"],
        "blame_header_bg": u["mantle"],
        "semantic_highlight_bg": c["surface1"],
        "tour_step_bg": u["paper"],
        # The embedded terminal is the editor's own window, not a second theme.
        "terminal_bg": u["base"],
        "terminal_fg": c["text"],
        "status_warning_indicator_fg": u["crust"],
        "status_warning_indicator_bg": c["yellow"],
        "status_error_indicator_fg": u["crust"],
        "status_error_indicator_bg": c["red"],
        "status_warning_indicator_hover_fg": u["crust"],
        "status_warning_indicator_hover_bg": c["yellow_hi"],
        "status_error_indicator_hover_fg": u["crust"],
        "status_error_indicator_hover_bg": c["red_hi"],
        "tab_drop_zone_bg": c["surface0"],
        "tab_drop_zone_border": c["orange"],
        "settings_selected_bg": c["surface1"],
        "settings_selected_fg": c["text_hi"],
        # git status in the file tree, same roles the diff uses
        "file_status_added_fg": c["green"],
        "file_status_modified_fg": c["yellow"],
        "file_status_deleted_fg": c["red"],
        "file_status_renamed_fg": c["denim"],
        "file_status_untracked_fg": c["overlay1"],
        "file_status_conflicted_fg": c["orange"],
    }

    search = {
        "match_bg": t["search"],
        "match_fg": c["text_hi"],
        "label_bg": c["orange"],
        "label_fg": u["crust"],
    }

    diagnostic = {
        "error_fg": c["red"],
        "error_bg": u["base"],
        "warning_fg": c["yellow"],
        "warning_bg": u["base"],
        "info_fg": c["denim"],
        "info_bg": u["base"],
        "hint_fg": c["sage"],
        "hint_bg": u["base"],
    }

    syntax = {
        "keyword": syn(f, "keyword"),
        "string": syn(f, "string"),
        "comment": syn(f, "comment"),
        "function": syn(f, "function"),
        "type": syn(f, "type"),
        "variable": syn(f, "variable"),
        "variable_builtin": syn(f, "variable.builtin"),
        "constant": syn(f, "constant"),
        "operator": syn(f, "operator"),
        "punctuation_bracket": syn(f, "punctuation"),
        "punctuation_delimiter": syn(f, "punctuation"),
    }

    return {
        "name": f.name,
        "extends": "builtin://dark" if f.dark else "builtin://light",
        "editor": editor,
        "ui": ui,
        "search": search,
        "diagnostic": diagnostic,
        "syntax": syntax,
    }


def build(flavors):
    return [
        Out(
            f"{f.slug}.json",
            json.dumps(theme(f), indent=2) + "\n",
            flavor=f.id,
            dest=f"~/.config/fresh/themes/{f.slug}.json",
            lang="json",
        )
        for f in flavors
    ]
