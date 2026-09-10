"""Sublime Text 4: a .sublime-color-scheme per flavor."""

import json

import palette as p
from ports._editors import extra_scope_rules, ui
from ports._lib import HEADER, Out, scope_rules, tints

META = {
    "id": "sublime-text",
    "name": "Sublime Text",
    "category": "Editors",
    "homepage": "https://www.sublimetext.com",
    "enable": {
        "where": "Preferences › Settings",
        "code": '"color_scheme": "{name}.sublime-color-scheme"',
        "lang": "json",
    },
    "auto": {
        "where": "Preferences › Settings",
        "code": '"color_scheme": "auto",\n'
        '"dark_color_scheme": "Subway Seat.sublime-color-scheme",\n'
        '"light_color_scheme": "Subway Seat Enamel.sublime-color-scheme",\n'
        '"theme": "auto"',
        "lang": "json",
    },
    "requires": "Sublime Text 4",
    "detect": ["subl", "/Applications/Sublime Text.app"],
    "notes": "A color scheme with gutter diff marks, inline diff, bracket and find highlights, and hover popups "
    "raised on the same paper as the other editors' menus. Copy it to Packages/User; Preferences › Browse "
    "Packages… opens the Packages folder.",
}

# Packages/User on each OS; Preferences › Browse Packages… opens the Packages folder.
USER_DIR = "~/Library/Application Support/Sublime Text/Packages/User"
HOW = "Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\\Sublime Text\\Packages\\User"

FONT_STYLES = ("bold", "italic", "underline")


def scheme(f):
    c = f
    u = ui(f)
    t = tints(f)
    roles = {c.colors[r]: r for r in reversed(p.ROLES)}  # hex → first role with that color
    variables = {r: c.colors[r] for r in p.ROLES}
    variables.update({f"tint_{k}": v for k, v in t.items()})
    variables["inactive_selection"] = u["selection_inactive"]
    variables["paper"] = u["paper"]

    def v(color):
        if color in roles:
            return f"var({roles[color]})"
        for k, val in t.items():
            if val == color:
                return f"var(tint_{k})"
        return color

    popup_css = (
        f"html {{ background-color: {u['paper']}; color: {c.text}; }} "
        f"a {{ color: {c.denim}; }} "
        f"code, .highlight {{ background-color: {c.base}; color: {c.green}; }} "
        f"h1, h2, h3 {{ color: {c.yellow}; }} "
        f".error, .errors {{ color: {c.red_hi}; }} "
        f".warning, .warnings {{ color: {c.yellow}; }} "
        f".info {{ color: {c.denim}; }} "
        f".hint {{ color: {c.sage}; }}"
    )
    globals_ = {
        "background": "var(base)",
        "foreground": "var(text)",
        "caret": v(u["cursor"]),
        "block_caret": v(u["cursor"]),
        "block_caret_border": v(u["cursor"]),
        "invisibles": "var(surface1)",
        "line_highlight": v(u["line"]),
        "misspelling": "var(red_hi)",
        "fold_marker": "var(overlay1)",
        "minimap_border": "var(surface2)",
        "accent": "var(orange)",
        "popup_css": popup_css,
        "phantom_css": popup_css,
        "gutter": "var(base)",
        "gutter_foreground": v(u["line_nr"]),
        "gutter_foreground_highlight": v(u["line_nr_cur"]),
        "line_diff_width": "2",
        "line_diff_added": "var(green)",
        "line_diff_modified": "var(yellow)",
        "line_diff_deleted": "var(red_hi)",
        "selection": v(u["selection"]),
        "selection_border": v(u["selection"]),
        "selection_border_width": "1",
        "inactive_selection": "var(inactive_selection)",
        "inactive_selection_border": "var(inactive_selection)",
        "selection_corner_style": "round",
        "selection_corner_radius": "2",
        "highlight": "var(yellow)",
        "find_highlight": v(u["search_cur"]),
        "find_highlight_foreground": v(u["search_cur_fg"]),
        "scroll_highlight": "var(yellow)",
        "scroll_selected_highlight": "var(orange)",
        "rulers": "var(surface0)",
        "ruler_style": "solid",
        "guide": "var(surface0)",
        "active_guide": "var(surface2)",
        "stack_guide": "var(surface1)",
        "brackets_options": "foreground bold",
        "brackets_foreground": v(u["bracket_fg"]),
        "bracket_contents_options": "underline",
        "bracket_contents_foreground": "var(surface2)",
        "tags_options": "stippled_underline",
        "tags_foreground": "var(orange)",
        "shadow": "color(var(crust) alpha(0.5))" if f.dark else "color(var(overlay1) alpha(0.25))",
        "shadow_width": "6",
    }

    def rule(scope, fg=None, bg=None, styles=()):
        r = {"scope": scope}
        if fg:
            r["foreground"] = v(fg)
        if bg:
            r["background"] = v(bg)
        fs = " ".join(s for s in FONT_STYLES if s in styles)
        if fs:
            r["font_style"] = fs
        return r

    rules = [rule(scope, color, styles=st) for scope, color, st in (*scope_rules(f), *extra_scope_rules(f))]
    rules += [
        # inline diff (Sublime's incremental diff, Sublime Merge-style views)
        rule("diff.inserted", bg=t["add"]),
        rule("diff.inserted.char", bg=t["add_emph"]),
        rule("diff.deleted", bg=t["del"]),
        rule("diff.deleted.char", bg=t["del_emph"]),
        rule("markup.inserted.diff", c.green, t["add"]),
        rule("markup.deleted.diff", c.red_hi, t["del"]),
        # GitGutter
        rule("markup.inserted.git_gutter", c.green),
        rule("markup.changed.git_gutter", c.yellow),
        rule("markup.deleted.git_gutter", c.red_hi),
        rule("markup.ignored.git_gutter", c.overlay0),
        rule("markup.untracked.git_gutter", c.overlay1),
        # diagnostics (LSP, SublimeLinter) and the regions plugins draw with
        rule("markup.error", u["error"]),
        rule("markup.warning", u["warning"]),
        rule("markup.info", u["info"]),
        rule("markup.info.hint", u["hint"]),
        rule("markup.unnecessary", c.overlay1),
        rule("region.redish", c.red_hi),
        rule("region.orangish", c.orange),
        rule("region.yellowish", c.yellow),
        rule("region.greenish", c.green),
        rule("region.cyanish", c.sage),
        rule("region.bluish", c.denim),
        rule("region.purplish", c.clay),
        rule("region.pinkish", c.red),
        rule("region.blackish", c.overlay0),
    ]
    return {
        "name": f.name,
        "author": "Oddur Sigurdsson",
        "variables": variables,
        "globals": globals_,
        "rules": rules,
    }


def build(flavors):
    outs = []
    for f in flavors:
        body = json.dumps(scheme(f), indent=2, ensure_ascii=False)
        # Sublime reads JSON with comments; the header is the only one.
        outs.append(Out(f"{f.name}.sublime-color-scheme", f"// {HEADER}\n{body}\n", flavor=f.id,
                        dest=f"{USER_DIR}/{f.name}.sublime-color-scheme", how=HOW, lang="json"))
    return outs
