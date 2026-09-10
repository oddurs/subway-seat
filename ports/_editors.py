"""Shared UI choices for the editor ports, so every editor reads the same room.

`ui(f)` names the UI decisions that differ between the dark and light flavors
(cursor, current line, selection, matches, popovers …); syntax comes from
`f.syntax(role)`, diff grounds from `tints(f)`.

Each role is one recipe with two forms. Apps without alpha use the solid color
from `ui(f)`. Apps that paint these grounds translucently under the text (VS
Code, Zed) use `glaze(f, ui(f)[role])`, a #RRGGBBAA that lands on exactly the
same color over the editor ground and still lets what's underneath show
through. So the selection, a search hit and the current match look the same in
every editor:

- selection: `_lib.selection(f)` (surface2 dark, surface1 Enamel)
- every match: `tints.search`; the current match: `tints.search_cur` with text_hi on it
- matching bracket: yellow_hi (dark) or orange (Enamel) on a quiet ground
- popovers (completion, hover, pickers) on `paper`, the selected row a wash of text
"""

import palette as p
from ports._lib import ink, resolve, selection, solid, tints, ui_colors


def ui(f):
    t = tints(f)
    return {
        "ink": ink(f),  # text on an accent fill
        "cursor": f.yellow if f.dark else f.orange,
        "line": f.surface0 if f.dark else f.mantle,  # current-line ground
        "selection": selection(f),
        "selection_inactive": f.mix(selection(f), "base", 0.55),  # unfocused window, secondary cursors
        "line_nr": f.overlay0,
        "line_nr_cur": f.yellow if f.dark else f.orange,
        "bracket_fg": f.yellow_hi if f.dark else f.orange,
        "bracket_bg": f.surface1 if f.dark else solid("text@L2", f),
        "search": t["search"],  # every match
        "search_cur": t["search_cur"],  # the current match, with `search_cur_fg` on it
        "search_cur_fg": f.text_hi,
        # popovers: completion menus, hovers, pickers, signature help
        "paper": ui_colors(f)["paper"],
        "edge": solid("text@EDGE", f, "paper"),  # hairline around a popover
        "row": solid("text@L3", f, "paper"),  # the selected row in a popover list
        # diagnostics: the hue, and the faint ground behind inline messages
        "error": f.red_hi,
        "warning": f.yellow,
        "info": f.denim,
        "hint": f.sage,
        "error_bg": f.mix("red", "base", 0.12),
        "warning_bg": f.mix("yellow", "base", 0.10),
        "info_bg": t["info"],
        "hint_bg": t["hint"],
        "inlay_bg": f.mix("surface0", "base", 0.6),  # inlay hints
    }


def glaze(f, color, over="base", min_alpha=0.5):
    """A translucent #RRGGBBAA that composites over `over` (a role or hex) to exactly `color`.

    The alpha is the lowest (from `min_alpha` up) at which the tinted color stays
    in gamut, so the ground underneath shows through as much as it can."""
    target = p.hex_to_rgb(color)
    ground = p.hex_to_rgb(resolve(over, f))
    for n in range(max(1, round(min_alpha * 255)), 256):
        a = n / 255
        rgb = [round(g + (t - g) / a) for t, g in zip(target, ground, strict=True)]
        if all(0 <= v <= 255 for v in rgb):
            return "#{:02X}{:02X}{:02X}{:02X}".format(*rgb, n) if n < 255 else color
    return color


# TextMate scopes the shared `_lib.SCOPES` table leaves to each grammar's
# defaults, added after it (later, equally specific rules win). Used by the
# VS Code and Sublime Text ports.
EXTRA_SCOPES = [
    ("entity.name.constant, constant.other.symbol", "constant"),
    ("entity.name.trait, entity.name.impl, entity.name.union, entity.name.type.trait", "type"),
    ("entity.name.scope-resolution, entity.name.type.namespace", "namespace"),
    ("support.variable.magic.python, variable.language.special", "variable.builtin"),
    ("keyword.operator.word", "keyword"),
    ("constant.other.character-class.regexp, constant.character.character-class.regexp", "regexp"),
    ("constant.character.entity, punctuation.definition.entity", "string.escape"),
    ("constant.other.reference.link.markdown, string.other.link.title.markdown", "link"),
    # macros read like decorators and attributes: clay italic
    ("entity.name.function.macro, entity.name.macro, support.macro, support.function.macro, "
     "meta.attribute.rust, punctuation.definition.attribute.rust", "decorator"),
    # diff file headers (--- a/x, +++ b/x): bold text; the -/+ signs keep red and green
    ("meta.diff.header.from-file, meta.diff.header.to-file, meta.diff.index", "strong"),
    # JSON, YAML and TOML keys in Sublime's own syntaxes (the key→gold rule in _lib covers VS Code's)
    ("meta.mapping.key string, meta.mapping.key.json string.quoted.double.json", "function"),
]


def extra_scope_rules(f):
    """(scope, hex, styles) for EXTRA_SCOPES, like `_lib.scope_rules`."""
    for scope, role in EXTRA_SCOPES:
        color, styles = f.syntax(role)
        yield scope, color, styles
