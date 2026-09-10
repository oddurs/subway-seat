"""Zed: one theme family with all three flavors, packaged as a Zed extension.

Style keys follow crates/settings_content/src/theme.rs (the v0.2.0 JSON schema
is stale and misses newer keys). Layering, darkest to lightest in both flavors:
crust chrome (title/status bars) → mantle panels and tab bar → base editor →
popovers on paper. Hovers are a warm veil (overlay1 at low alpha) so they
compose over any ground: it lightens the dark grounds and darkens Enamel's
cream ones. The selection, matches and diff rows are the shared editor recipes
from `_editors`, glazed so they land on exactly the same colors as the other
editors over the editor ground.
"""

import json

import palette as p
from ports._editors import glaze, ui
from ports._lib import ANSI_NAMES, HEADER, REPO, VERSION, Out, tints

a = p.alpha

META = {
    "id": "zed",
    "name": "Zed",
    "category": "Editors",
    "homepage": "https://zed.dev",
    "enable": {
        "where": "settings.json",
        "code": '"theme": "{name}"',
        "lang": "json",
    },
    "auto": {
        "where": "settings.json",
        "code": '"theme": {\n  "mode": "system",\n  "light": "Subway Seat Enamel",\n  "dark": "Subway Seat"\n}',
        "lang": "json",
    },
    "detect": ["zed", "zeditor", "/Applications/Zed.app"],
    "notes": "All three flavors in one theme family: copy the theme file, or install the dist/zed folder of a "
    "clone with Zed › Extensions › Install Dev Extension. The title and status bars sit darkest, panels a step "
    "lighter, the editor lighter again, and menus and popovers are raised above it. Selections, search "
    "matches and diffs use the same colors as the other editor ports, and the agent panel's diffs follow them.",
}

# Zed syntax capture → SYNTAX role, or (color role, styles) where the palette has no role.
CAPTURES = {
    "attribute": "attribute",
    "attribute.builtin": "decorator",
    "boolean": "boolean",
    "character": "string",
    "comment": "comment",
    "comment.doc": ("overlay2", {"italic"}),
    "comment.documentation": ("overlay2", {"italic"}),
    "concept": "type",
    "constant": "constant",
    "constant.builtin": "constant",
    "constructor": "type",
    "diff.minus": ("red_hi", set()),
    "diff.plus": ("green", set()),
    "embedded": "variable",
    "emphasis": "emphasis",
    "emphasis.strong": "strong",
    "enum": "type",
    "function": "function",
    "function.builtin": "function.builtin",
    "function.decorator": "decorator",
    "function.macro": "decorator",
    "hint": ("overlay1", set()),
    "keyword": "keyword",
    "keyword.operator": "keyword",  # and, or, not, in: words, so they read as keywords (as in Neovim)
    "label": "decorator",
    "lifetime": "decorator",
    "link_text": "link",
    "link_uri": ("denim", {"italic"}),
    "module": "namespace",
    "namespace": "namespace",
    "number": "number",
    "operator": "operator",
    "parameter": "parameter",
    "predictive": ("overlay1", {"italic"}),
    "preproc": "decorator",
    "primary": "variable",
    "property": "property",
    "property.json_key": "function",  # JSON keys in gold, like the TextMate ports
    "punctuation": "punctuation",
    "punctuation.bracket": "punctuation",
    "punctuation.delimiter": "punctuation",
    "punctuation.list_marker": "keyword",
    "punctuation.markup": "punctuation",
    "punctuation.special": "string.escape",
    "selector": ("yellow", set()),
    "selector.pseudo": ("clay", set()),
    "string": "string",
    "string.doc": ("green", {"italic"}),
    "string.escape": "string.escape",
    "string.regex": "regexp",
    "string.special": "string.escape",
    "string.special.path": ("green", set()),
    "string.special.symbol": "constant",
    "string.special.url": "link",
    "tag": "tag",
    "tag.attribute": "attribute",
    "tag.component": "type",
    "tag.delimiter": "punctuation",
    "text.literal": "code",
    "title": "heading",
    "type": "type",
    "type.builtin": "type.builtin",
    "variable": "variable",
    "variable.builtin": "variable.builtin",
    "variable.member": "property",
    "variable.parameter": "parameter",
    "variable.special": "variable.builtin",
    "variant": "constant",
}


# Comment tags as small badges: ink on the accent, as in Neovim.
BADGES = {"comment.todo": "yellow", "comment.note": "sage", "comment.warning": "yellow", "comment.error": "red_hi"}


def syntax(f):
    out = {}
    for capture, spec in CAPTURES.items():
        color, styles = f.syntax(spec) if isinstance(spec, str) else (f.colors[spec[0]], spec[1])
        s = {"color": color}
        if "italic" in styles:
            s["font_style"] = "italic"
        if "bold" in styles:
            s["font_weight"] = 700
        out[capture] = s
    for capture, role in BADGES.items():
        out[capture] = {"color": ui(f)["ink"], "background_color": f.colors[role], "font_weight": 700}
    return dict(sorted(out.items()))


def style(f):
    c = f
    dark = f.dark
    u, t = ui(f), tints(f)
    ink = u["ink"]
    k = 1.0 if dark else 1.2           # accent tints need a little more alpha on cream

    def veil(x):
        return a(c.overlay1, x)

    def tint(color, x):
        return a(color, min(1.0, x * k))

    # Popovers are raised onto paper: surface0 in the dark flavors; on Enamel the
    # surface ramp darkens, so paper lifts toward white instead (enamel catching the sun).
    lifted = u["paper"]
    border = c.crust if dark else f.mix("surface0", "surface1", 0.5)
    hairline = veil(0.22)
    selection = glaze(f, u["selection"])
    cursor = u["cursor"]

    s = {
        "background.appearance": "opaque",
        # borders: quiet seams, orange only for focus
        "border": border,
        "border.variant": hairline,
        "border.focused": a(c.orange, 0.55),
        "border.selected": a(c.orange, 0.7),
        "border.transparent": "#00000000",
        "border.disabled": veil(0.12),
        # grounds
        "background": c.crust,
        "surface.background": c.mantle,
        "elevated_surface.background": lifted,
        "title_bar.background": c.crust,
        "title_bar.inactive_background": f.mix("crust", "mantle", 0.5),
        "status_bar.background": c.crust,
        "toolbar.background": c.base,
        "tab_bar.background": c.mantle,
        "tab.inactive_background": c.mantle,
        "tab.active_background": c.base,
        "panel.background": c.mantle,
        "panel.focused_border": a(c.orange, 0.4),
        "panel.indent_guide": veil(0.2),
        "panel.indent_guide_hover": veil(0.38),
        "panel.indent_guide_active": veil(0.5),
        "panel.overlay_background": c.mantle,
        "panel.overlay_hover": p.blend(c.overlay1, c.mantle, 0.12),
        "pane.focused_border": a(c.orange, 0.4),
        "pane_group.border": border,
        # elements (own background) and ghost elements (sit on their surface)
        "element.background": veil(0.1),
        "element.hover": veil(0.16),
        "element.active": veil(0.26),
        "element.selected": veil(0.22),
        "element.disabled": veil(0.05),
        "element.selection_background": selection,
        "ghost_element.background": "#00000000",
        "ghost_element.hover": veil(0.12),
        "ghost_element.active": veil(0.2),
        "ghost_element.selected": veil(0.17),
        "ghost_element.disabled": "#00000000",
        "drop_target.background": a(c.orange, 0.12),
        "drop_target.border": a(c.orange, 0.6),
        # text and icons
        "text": c.text,
        "text.muted": c.overlay2,
        "text.placeholder": c.overlay1,
        "text.disabled": c.overlay0,
        "text.accent": c.orange,
        "icon": c.subtext0,
        "icon.muted": c.overlay2,
        "icon.disabled": c.overlay0,
        "icon.placeholder": c.overlay1,
        "icon.accent": c.orange,
        "link_text.hover": c.denim_hi if dark else c.denim,
        "debugger.accent": c.red_hi,
        # search
        "search.match_background": glaze(f, u["search"]),
        "search.active_match_background": glaze(f, u["search_cur"]),
        # scrollbars and minimap
        "scrollbar.thumb.background": veil(0.25),
        "scrollbar.thumb.hover_background": veil(0.4),
        "scrollbar.thumb.active_background": veil(0.52),
        "scrollbar.thumb.border": "#00000000",
        "scrollbar.track.background": "#00000000",
        "scrollbar.track.border": "#00000000",
        "minimap.thumb.background": veil(0.16),
        "minimap.thumb.hover_background": veil(0.26),
        "minimap.thumb.active_background": veil(0.36),
        "minimap.thumb.border": "#00000000",
        # editor
        "editor.foreground": c.text,
        "editor.background": c.base,
        "editor.gutter.background": c.base,
        "editor.subheader.background": c.mantle,
        "editor.active_line.background": veil(0.1 if dark else 0.08),
        "editor.highlighted_line.background": veil(0.16),
        "editor.debugger_active_line.background": glaze(f, t["chg"]),
        "editor.line_number": c.overlay0,
        "editor.active_line_number": u["line_nr_cur"],
        "editor.hover_line_number": c.overlay2,
        "editor.invisible": c.surface2,
        "editor.wrap_guide": veil(0.1),
        "editor.active_wrap_guide": veil(0.2),
        "editor.indent_guide": veil(0.14),
        "editor.indent_guide_active": veil(0.38),
        "editor.document_highlight.read_background": veil(0.2),
        "editor.document_highlight.write_background": tint(c.orange, 0.18),
        "editor.document_highlight.bracket_background": glaze(f, u["bracket_bg"]),
        # diff rows use the shared line tints; hollow rows (staged hunks) the faded ones
        "editor.diff_hunk.added.background": glaze(f, t["add"]),
        "editor.diff_hunk.added.hollow_background": glaze(f, t["add_dim"]),
        "editor.diff_hunk.added.hollow_border": a(c.green, 0.45),
        "editor.diff_hunk.deleted.background": glaze(f, t["del"]),
        "editor.diff_hunk.deleted.hollow_background": glaze(f, t["del_dim"]),
        "editor.diff_hunk.deleted.hollow_border": a(c.red_hi, 0.45),
        # version control: gutter marks and file status; changed words sit on the row tint
        "version_control.added": c.green,
        "version_control.deleted": c.red_hi,
        "version_control.modified": c.yellow,
        "version_control.renamed": c.sage,
        "version_control.conflict": c.orange,
        "version_control.ignored": c.overlay0,
        "version_control.word_added": glaze(f, t["add_emph"], over=t["add"]),
        "version_control.word_deleted": glaze(f, t["del_emph"], over=t["del"]),
        "version_control.conflict_marker.ours": glaze(f, t["add"]),
        "version_control.conflict_marker.theirs": glaze(f, t["info"]),
        # terminal
        "terminal.background": c.base,
        "terminal.ansi.background": c.base,
        "terminal.foreground": c.text,
        "terminal.bright_foreground": c.text_hi,
        "terminal.dim_foreground": c.overlay1,
    }
    for i, name in enumerate(ANSI_NAMES):
        s[f"terminal.ansi.{name}"] = f.ansi[i]
        s[f"terminal.ansi.bright_{name}"] = f.ansi[i + 8]
        # dimmed toward the ground; less on cream, where dimming washes the darker inks out fast
        s[f"terminal.ansi.dim_{name}"] = p.blend(f.ansi[i], c.base, 0.65 if dark else 0.8)

    # vim / helix mode chips: a route bullet per mode, ink letters
    modes = {"normal": c.sage, "insert": c.green, "replace": c.red_hi, "visual": c.orange,
             "visual_line": c.clay, "visual_block": c.yellow, "helix_normal": c.sage, "helix_select": c.orange}
    for mode, color in modes.items():
        s[f"vim.{mode}.background"] = color
        s[f"vim.{mode}.foreground"] = ink
    s["vim.yank.background"] = tint(c.yellow, 0.3)
    s["vim.helix_jump_label.foreground"] = c.orange

    # status colors: a hue, a wash behind it and a quiet opaque edge
    status = {
        "conflict": c.orange, "created": c.green, "deleted": c.red_hi, "error": c.red_hi,
        "hidden": c.overlay0, "hint": c.sage, "ignored": c.overlay0, "info": c.denim,
        "modified": c.yellow, "predictive": c.overlay1, "renamed": c.sage, "success": c.green,
        "unreachable": c.overlay1, "warning": c.yellow,
    }
    for name, color in status.items():
        s[name] = color
        s[f"{name}.background"] = tint(color, 0.12)
        s[f"{name}.border"] = f.mix(color, "base", 0.4 if dark else 0.5)

    others = [c.orange if dark else c.yellow, c.sage, c.clay, c.green, c.denim, c.red_hi, c.denim_hi]
    s["players"] = [{"cursor": cursor, "background": cursor, "selection": selection}] + [
        {"cursor": color, "background": color, "selection": tint(color, 0.22)} for color in others
    ]
    s["accents"] = [c.yellow, c.orange, c.sage, c.clay, c.green, c.denim, c.red_hi]
    s["syntax"] = syntax(f)
    return s


def family(flavors):
    return {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Subway Seat",
        "author": "Oddur Sigurdsson",
        "themes": [
            {"name": f.name, "appearance": "dark" if f.dark else "light", "style": style(f)} for f in flavors
        ],
    }


EXTENSION = f"""# {HEADER}
id = "subway-seat-theme"
name = "Subway Seat"
version = "{VERSION}"
schema_version = 1
authors = ["Oddur Sigurdsson"]
description = "A walnut-brown 1970s NYC subway theme: parchment text, harvest gold, burnt orange, avocado. Dark, deep dark and light."
repository = "{REPO}"
"""

LICENSE = """MIT License

Copyright (c) 2026 Oddur Sigurdsson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def build(flavors):
    dev = "part of the dev extension: Zed › Extensions › Install Dev Extension, then pick this folder"
    return [
        Out("themes/subway-seat.json", json.dumps(family(flavors), indent=2) + "\n",
            dest="~/.config/zed/themes/subway-seat.json", how="Windows: %APPDATA%\\Zed\\themes", lang="json"),
        Out("extension.toml", EXTENSION, how=dev, lang="toml"),
        Out("LICENSE", LICENSE, how=dev, lang="text"),
    ]
