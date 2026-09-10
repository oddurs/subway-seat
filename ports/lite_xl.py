"""Lite XL: a colors/ module per flavor, in the lite-xl-colors format."""

from ports._editors import ui
from ports._lib import HEADER, Out, rgb, ui_colors

META = {
    "id": "lite-xl",
    "name": "Lite XL",
    "category": "Editors",
    "homepage": "https://lite-xl.com",
    "enable": {
        "where": "~/.config/lite-xl/init.lua",
        "code": 'core.reload_module("colors.{slug}")',
        "lang": "lua",
    },
    "notes": "Copy the files to `~/.config/lite-xl/colors/` (on Windows, `%USERPROFILE%\\.config\\lite-xl\\colors`), "
    "then pick one in the settings plugin or load it from `init.lua`. Also colors the indentguide and "
    "bracketmatch plugins.",
    "detect": ["lite-xl", "/Applications/Lite XL.app"],
}


def colors(f):
    u = ui(f)

    def rgba(c, a):
        return "rgba({}, {}, {}, {})".format(*rgb(c), a)

    def syn(role):
        return f.syntax(role)[0]

    shadow = ui_colors(f)["shadow"]
    style = {
        "background": f.base,  # document
        "background2": f.mantle,  # tree view, status bar
        "background3": u["paper"],  # command view, autocomplete and other popups
        "text": f.subtext1,
        "caret": u["cursor"],
        "accent": u["line_nr_cur"],
        "dim": f.overlay1,
        "divider": f.crust,
        "selection": u["selection"],
        "line_number": u["line_nr"],
        "line_number2": u["line_nr_cur"],
        "line_highlight": u["line"],
        "scrollbar": f.surface2,
        "scrollbar2": f.overlay0,
        "scrollbar_track": f.mantle,
        "nagbar": f.red,
        "nagbar_text": u["ink"],
        "nagbar_dim": rgba(shadow, 0.45),
        "drag_overlay": rgba(f.text, 0.1),
        "drag_overlay_tab": u["cursor"],
        "good": f.green,
        "warn": f.yellow,
        "error": f.red_hi,
        "modified": f.yellow,
        # plugins: indentguide, bracketmatch
        "guide": f.surface0,
        "guide_highlight": f.surface2,
        "bracketmatch_color": u["bracket_fg"],
        "bracketmatch_char_color": u["bracket_fg"],
        "bracketmatch_block_color": u["bracket_bg"],
        "bracketmatch_frame_color": f.surface2,
    }
    syntax = {
        "normal": syn("variable"),
        "symbol": syn("variable"),
        "comment": syn("comment"),
        "keyword": syn("keyword"),
        "keyword2": syn("type"),  # types, self, builtins
        "number": syn("number"),
        "literal": syn("constant"),  # true, false, nil
        "string": syn("string"),
        "operator": syn("operator"),
        "function": syn("function"),
    }
    return style, syntax


def render(f):
    style, syntax = colors(f)
    width = max(map(len, style))
    lines = [
        f"-- {HEADER}",
        f"-- {f.name} — {f.blurb}",
        "",
        'local style = require "core.style"',
        'local common = require "core.common"',
        "",
    ]
    lines += [f'style.{k:<{width}} = {{ common.color "{v}" }}' for k, v in style.items()]
    lines.append("")
    keys = {k: f'style.syntax["{k}"]' for k in syntax}
    lines += [f'{keys[k]:<24} = {{ common.color "{v}" }}' for k, v in syntax.items()]
    lines += [
        "",
        'style.log["INFO"]  = { icon = "i", color = style.text }',
        'style.log["WARN"]  = { icon = "!", color = style.warn }',
        'style.log["ERROR"] = { icon = "!", color = style.error }',
        "",
        "return style",
    ]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"colors/{f.slug}.lua", render(f), flavor=f.id,
            dest=f"~/.config/lite-xl/colors/{f.slug}.lua", lang="lua")
        for f in flavors
    ]
