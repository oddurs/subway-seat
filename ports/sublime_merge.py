"""Sublime Merge: a UI theme per flavor plus the diff color scheme it switches on.

Sublime Merge looks up per-theme settings by the theme's name
("Diff - <theme>.sublime-settings" and friends), so choosing the theme also
picks the matching color scheme for diffs, commit messages and inputs. The
color scheme is the Sublime Text port's, plus the rules only Merge uses
(side-by-side and three-way merge grounds, blame).
"""

import json

import palette as p
from ports._editors import ui
from ports._lib import HEADER, INK, Out, ink, resolve, solid, tints, ui_colors
from ports.sublime_text import scheme as text_scheme

META = {
    "id": "sublime-merge",
    "name": "Sublime Merge",
    "category": "Editors",
    "homepage": "https://www.sublimemerge.com",
    "detect": ["smerge", "/Applications/Sublime Merge.app"],
    "requires": "Sublime Merge 2",
    "enable": {
        "where": "Preferences › Edit Settings… (Preferences.sublime-settings)",
        "code": '"theme": "{name}.sublime-theme"',
        "lang": "json",
    },
    "auto": {
        "where": "Preferences › Edit Settings… (Preferences.sublime-settings)",
        "code": '"theme": "auto",\n'
        '"dark_theme": "Subway Seat.sublime-theme",\n'
        '"light_theme": "Subway Seat Enamel.sublime-theme"',
        "lang": "json",
    },
    "notes": "A walnut theme for the whole window and the diff colors to go with it: syntax colors stay on "
    "the green and red line tints, changed words sit on a stronger tint, the empty side of a side-by-side diff "
    "is a darker recess, and the merge tool marks lines taken from each side in avocado and gold. Choosing the "
    "theme also switches the diff, commit message and input colors. Sublime Merge applies themes only in "
    "licensed copies; an unlicensed copy still takes the diff colors from a `Diff - Merge.sublime-settings` in "
    'Packages/User containing `"color_scheme": "Subway Seat Enamel.sublime-color-scheme"`.',
}

HOW = "In Sublime Merge's Packages/User folder (Preferences › Browse Packages…)"


def rgba(expr, f):
    """A layering expression as the rgba() Sublime themes read."""
    value = resolve(expr, f)
    r, g, b = p.hex_to_rgb(value[:7])
    a = int(value[7:], 16) / 255 if len(value) == 9 else 1
    return f"rgba({r}, {g}, {b}, {a:.2f})" if a < 1 else value


def wash(level, f, role="text"):
    """A translucent layer of text (hover, pressed, selected), per the _lib ink levels."""
    return rgba(f"{role}@{level}", f)


def theme_variables(f):
    c = ui_colors(f)
    t = tints(f)
    on = ink(f)
    bar = f.mantle if f.dark else f.crust  # title and tab bars
    chrome = f.mantle  # side bar and table of contents; dialogs and popovers sit on paper
    rows = solid("mix(mantle, base, 0.5)", f)  # the commit list, between chrome and the diff
    edges = [f.orange, f.yellow, f.green, f.sage, f.denim, f.clay]
    v = {
        # palette
        "red": f.red,
        "darker_red": f.red,
        "orange": f.orange,
        "yellow": f.yellow,
        "green": f.green,
        "teal": f.sage,
        "blue": f.denim,
        "purple": f.clay,
        "magenta": f.orange_hi,
        "light_blue": t["info"],
        "light_red": t["del"],
        "light_orange": t["chg"],
        "light_green": t["add"],
        "dark_red": t["del"],
        "dark_teal": t["add"],
        "dark_blue": t["chg"],
        # grays, darkest ground → lightest (dark) or the reverse (Enamel)
        "dark_gray": f.crust,
        "dark_gray-medium": bar,
        "dark_gray-light": chrome,
        "dark_gray-lightest": rows,
        "medium_gray-dark": f.overlay0,
        "medium_gray": f.overlay1,
        "medium_gray-light": f.overlay2 if f.dark else f.surface2,
        "light_gray-dark": bar,
        "light_gray-medium": chrome,
        "light_gray": rows,
        # text
        "text-heading": f.text_hi,
        "text": f.text,
        "label_color": f.text,
        "link_label_color": f.denim,
        "help_label_color": f.subtext0,
        "branch_stats_label_bg": f.overlay1,
        # header
        "title_bar_style": "dark" if f.dark else "light",
        "header_bg": bar,
        "header_fg": f.text,
        "header_button_bg": wash("L3", f),
        "icon_button_fg": f.text_hi,
        "hidden_slash": f.orange,
        "info_shadow": rgba("shadow@20", f),
        "info-progress_bar_bg": f.surface1,
        "info-progress_bar_fg": f.overlay1,
        "diverged_bg": f.orange,
        "diverged_button_bg": wash("L4", f, "crust" if f.dark else "base"),
        "diverged_button_fg": on,
        "diverged_button_shadow": "transparent",
        "diverged_icon_bg": on,
        "diverged_icon_fg": f.orange,
        # output status
        "output_fg": f.text,
        "output_succeeded_fg": f.green,
        "output_failed_fg": f.red_hi,
        "output_running_fg": f.denim,
        "output_cancelled_fg": f.subtext0,
        "command_status_label_error_fg": f.red_hi,
        "scroll_shadow": rgba(f"shadow@{30 if f.dark else 12}", f),
        "focus_highlight_color": f.orange,
        "overlay_bg": c["paper"],
        # welcome and preferences
        "welcome_bg": f.base,
        "recent_repositories_row_bg-hover": wash("L2", f),
        "preferences_overlay_bg": bar,
        "preferences_section_table_bg": rows,
        # location bar (side bar)
        "location_bar_fg": f.subtext1,
        "location_bar_heading_fg": f.text,
        "location_bar_fg-faded": f.subtext0,
        "location_bar_heading_shadow": "transparent",
        "location_bar_row_bg-hover": wash("L2", f),
        "disclosure_fg": f.text,
        "submodule_stat_bg": f.orange,
        "submodule_stat_fg": on,
        "side_bar_container_bg": chrome,
        "side_bar_container_with_graph_bg": rows,
        # commit list
        "commit_list_bg": rows,
        "commit_row_bg-hover": wash("L2", f),
        "commit_summary_fg-primary": f.text,
        "commit_summary_fg-secondary": f.subtext0,
        **{f"commit_edge_{i}": color for i, color in enumerate(edges)},
        # table of contents
        "table_of_contents_bg": chrome,
        "table_of_contents_fg": f.subtext1,
        "table_of_contents_heading_fg": f.text,
        "table_of_contents_row_bg": wash("L3", f),
        # detail panel
        "detail_panel_bg": "var(--background)",
        "field_name_fg": f.subtext0,
        "author_fg": f.subtext0,
        "terminator_fg": f.overlay0,
        # annotations (branch, tag, stash and file labels)
        "commit_annotation_fg": f.text,
        "commit_annotation_fg_inverted": on,
        "commit_annotation_bg": wash("L3", f),
        **{f"commit_annotation_fg_{i}_border": f"var(commit_edge_{i})" for i in range(6)},
        **{f"commit_annotation_bg_inverted_{i}": f"var(commit_edge_{i})" for i in range(6)},
        "tag_ann_fg": on,
        "tag_ann_bg": f.yellow,
        "tag_ann_opacity": 0.6,
        "stash_ann_fg": f.yellow,
        "stash_ann_bg": rgba(f"yellow@{30 if f.dark else 22}", f),
        "file_ann_fg": f.text,
        "file_ann_bg": wash("L4", f),
        "submodule_ann_fg": f.text,
        "submodule_ann_bg": wash("L3", f),
        "submodule_light_ann_fg": f.subtext0,
        "submodule_light_ann_bg": wash("L2", f),
        "inserted_ann_bg": t["add_emph"],
        "deleted_ann_bg": t["del_emph"],
        "lfs_ann_bg": wash("L4", f),
        # file and hunk headers
        "file_diff_shadow": rgba(f"shadow@{40 if f.dark else 10}", f),
        "file_icon_bg": wash("L4", f),
        "hunk_button_fg": f.text,
        "hunk_button_shadow": "transparent",
        "file_header_bg": solid("text@L3", f),
        "file_header_bg-hover": solid("text@L4", f),
        "hunk_header_bg": solid("text@L1", f),
        "deleted_icon_fg": f.red_hi,
        "deleted_header_bg": t["del"],
        "deleted_header_bg-hover": t["del_emph"],
        "unmerged_icon_fg": f.orange,
        "unmerged_header_bg": t["chg"],
        "unmerged_header_bg-hover": t["chg_emph"],
        "recent_icon_fg": f.yellow,
        "recent_icon_bg": "transparent",
        "untracked_header_bg": solid("text@L2", f),
        "untracked_header_bg-hover": solid("text@L3", f),
        "staged_icon_fg": f.green,
        "renamed_file_inserted": f.green,
        "renamed_file_deleted": f.red_hi,
        "full_context_icon_bg": f.overlay1,
        # image diffs
        "onion_skin_slider_puck_bg": f.orange,
        "onion_skin_slider_puck_border_bg": f.overlay0,
        "onion_skin_slider_track_bg": f.overlay0,
        "image_diff_bg": "var(detail_panel_bg)",
        "image_diff_fg": f.text,
        "image_diff_checkerboard_main_bg": "var(--background)",
        "image_diff_checkerboard_alt_bg": f.surface0 if f.dark else f.crust,
        "image_unchanged_label_fg": f.subtext1,
        "image_unchanged_label_bg": c["paper"],
        # blame
        "blame_popup_bg": c["paper"],
        # buttons
        "button_bg": wash("L4", f),
        "button_fg": f.text,
        "button_shadow": "transparent",
        "split_button_line": "var(--background)",
        "highlighted_button_light_bg": f.orange,
        "highlighted_button_light_fg": on,
        "highlighted_button_dark_bg": f.orange,
        "highlighted_button_dark_fg": on,
        "highlighted_button_shadow": "transparent",
        "toggle_button_bg": wash("L3", f),
        "toggle_button_fg": f.subtext0,
        "toggle_button_fg_selected": f.text,
        "toggle_button_bg-details": wash("L4", f),
        # tabs
        "tab_bar_bg": bar,
        "file_tab_bg": "var(file_header_bg)",
        "untracked_file_tab_bg": "var(untracked_header_bg)",
        "unmerged_file_tab_bg": "var(unmerged_header_bg)",
        "location_tab_bg": "var(detail_panel_bg)",
        "tab_button_fg": f.text,
        "tab_separator_bg": f.surface1 if f.dark else f.surface0,
        "repository_tab_bar_bg": f.crust,
        "repository_tab_bar_border_bg": f.crust,
        # hazard (discard) buttons
        "hazard_button_bg": f.red,
        "hazard_button_fg": on,
        "hazard_button_shadow": "transparent",
        "use_hunk_button_fg": "var(--foreground)",
        # radio buttons and checkboxes
        "radio_back": "var(--background)",
        "radio_border-unselected": f.overlay0,
        "radio_selected": f.orange,
        "radio_border-selected": f.orange,
        "checkbox_back": "var(--background)",
        "checkbox_border-unselected": f.overlay0,
        "checkbox_selected": f.orange,
        "checkbox_border-selected": f.orange,
        "checkbox-disabled": f.surface2,
        # dialogs, progress, quick panel, tool tips
        "dialog_bg": c["paper"],
        "dialog_button_bg": wash("L4", f),
        "progress_bg": wash("L3", f),
        "progress_fg": f.orange,
        "quick_panel_bg": c["paper"],
        "quick_panel_row_bg": wash("L4", f),
        "quick_panel_fg": f.subtext1,
        "quick_panel_fg-match": f.yellow if f.dark else f.orange,
        "quick_panel_fg-selected": f.text_hi,
        "quick_panel_fg-selected-match": f.yellow if f.dark else f.orange,
        "quick_panel_path_fg": f.subtext0,
        "quick_panel_path_fg-match": f.yellow if f.dark else f.orange,
        "quick_panel_path_fg-selected": f.subtext1,
        "quick_panel_path_fg-selected-match": f.yellow if f.dark else f.orange,
        "switch_repo_bg": c["paper"],
        "tool_tip_bg": c["paper"],
        "tool_tip_fg": f.text,
        "tool_tip_border": f.surface1 if f.dark else f.surface0,
        # hints and errors
        "hint_bg": c["paper"],
        "hint_fg": f.text,
        "success_hint_bg": c["paper"],
        "success_hint_fg": f.text,
        "success_hint_accent": f.green,
        "error_hint_bg": c["paper"],
        "error_hint_fg": f.text,
        "error_hint_accent": f.red_hi,
        "failed_label_bg": f.red_hi,
        "failed_label_fg": on,
        "loading_ball_1": f.overlay0,
        "loading_ball_2": f.orange,
        "preview_fg": f.text_hi,
        "merge_helper_highlight_bg": wash("L3", f),
        "console_border": f.crust if f.dark else f.surface0,
        # file badges in the file list
        "file_badge_modified_bg": rgba(f"yellow@{INK['L5'][0 if f.dark else 1]}", f),
        "file_badge_modified_fg": f.yellow,
        "file_badge_unmerged_bg": rgba(f"orange@{INK['L5'][0 if f.dark else 1]}", f),
        "file_badge_unmerged_fg": f.orange,
        "file_badge_untracked_bg": rgba(f"green@{INK['L5'][0 if f.dark else 1]}", f),
        "file_badge_untracked_fg": f.green,
        "file_badge_staged_bg": wash("L4", f),
        "file_badge_staged_fg": f.subtext1,
    }
    return v


def theme(f):
    u = ui(f)
    blame = [f.orange, f.yellow, f.green, f.sage, f.denim, f.clay]
    doc = {
        "extends": "Merge Dark.sublime-theme" if f.dark else "Merge.sublime-theme",
        "variables": theme_variables(f),
        "rules": [
            {
                "class": "diff_text_control",
                "line_selection_color": rgba(f"orange@{8 if f.dark else 10}", f),
                "line_selection_border_color": u["cursor"],
                "line_selection_border_width": 2.0,
                "line_selection_border_radius": 2.0,
            },
            {
                "class": "blame_text_control",
                "settings": ["!kelly_colors"],
                "num_colors": len(blame),
                **{f"color{i}": color for i, color in enumerate(blame)},
            },
        ],
    }
    return f"// {HEADER}\n" + json.dumps(doc, indent="\t", ensure_ascii=False) + "\n"


def color_scheme(f):
    """The Sublime Text scheme plus the scopes only Merge paints."""
    t = tints(f)
    doc = text_scheme(f)
    gap = f.mantle  # the empty side of a side-by-side diff: a recess, not a line
    doc["rules"] += [
        {"scope": "diff.inserted.side-by-side", "background": t["add"]},
        {"scope": "diff.inserted.char.side-by-side", "background": t["add_emph"]},
        {"scope": "diff.deleted.side-by-side", "background": t["del"]},
        {"scope": "diff.deleted.char.side-by-side", "background": t["del_emph"]},
        {"scope": "diff.fill", "background": gap},
        # three-way merge: what each side adds, on the added (left) and changed (right) tints
        {"scope": "diff.inserted.merge-left", "background": t["add"]},
        {"scope": "diff.inserted.char.merge-left", "background": t["add_emph"]},
        {"scope": "diff.border.merge-left", "background": f.green},
        {"scope": "diff.inserted.merge-right", "background": t["chg"]},
        {"scope": "diff.inserted.char.merge-right", "background": t["chg_emph"]},
        {"scope": "diff.border.merge-right", "background": f.yellow},
        {"scope": "diff.border.merge-conflict", "background": f.red_hi},
        {"scope": "diff.border.merge-merged", "background": f.overlay1},
        {"scope": "blame.border", "background": f.surface1 if f.dark else f.surface0},
        {"scope": "blame.age-icon", "foreground": f.yellow if f.dark else f.orange},
        {"scope": "source.sublime-merge.preferences.git_binary", "foreground": f.yellow if f.dark else f.orange},
    ]
    return f"// {HEADER}\n" + json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def widget_scheme(f):
    """Text inputs (search, location and branch fields)."""
    c = ui_colors(f)
    u = ui(f)
    doc = {
        "name": f"{f.name} Widgets",
        "globals": {
            "foreground": f.text,
            "background": c["paper"],
            "caret": u["cursor"],
            "line_highlight": c["paper"],
            "selection": u["selection"],
            "selection_border": u["selection"],
            "inactive_selection": u["selection"],
        },
        "rules": [
            {"scope": "comment", "foreground": f.syntax("comment")[0]},
            {"scope": "keyword, storage", "foreground": f.syntax("keyword")[0]},
            {"scope": "constant", "foreground": f.syntax("constant")[0]},
            {"scope": "string", "foreground": f.syntax("string")[0]},
            {"scope": "constant.character.escape", "foreground": f.syntax("string.escape")[0]},
        ],
    }
    return f"// {HEADER}\n" + json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def settings(**values):
    return f"// {HEADER}\n" + json.dumps(values, indent="\t") + "\n"


def build(flavors):
    outs = []
    for f in flavors:
        name = f.name
        scheme_file = f"{name}.sublime-color-scheme"
        files = {
            f"{name}.sublime-theme": theme(f),
            scheme_file: color_scheme(f),
            f"Widget - {name}.hidden-color-scheme": widget_scheme(f),
            f"Widget - {name}.sublime-settings": settings(
                color_scheme=f"Widget - {name}.hidden-color-scheme", draw_shadows=False
            ),
        }
        # Merge picks these up by the theme's name, so the theme brings its color scheme along
        for view in ("Diff", "Commit Message", "File Mode", "Git Output"):
            files[f"{view} - {name}.sublime-settings"] = settings(color_scheme=scheme_file)
        for path, content in files.items():
            outs.append(Out(path, content, flavor=f.id, dest=f"Packages/User/{path}", lang="json", how=HOW))
    return outs
