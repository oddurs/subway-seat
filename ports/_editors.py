"""Shared UI choices for the editor ports, so every editor reads the same room.

`ui(f)` names the handful of UI decisions that differ between the dark and light
flavors (cursor, current line, selection …); syntax comes from `f.syntax(role)`.
"""

from ports._lib import tints


def ui(f):
    t = tints(f)
    return {
        "ink": f.crust if f.dark else f.base,  # text on an accent fill
        "cursor": f.yellow if f.dark else f.orange,
        "line": f.surface0 if f.dark else f.mantle,  # current-line ground
        "selection": f.surface2 if f.dark else f.surface1,
        "line_nr": f.overlay0,
        "line_nr_cur": f.yellow if f.dark else f.orange,
        "bracket_fg": f.yellow_hi,
        "bracket_bg": f.surface1,
        "search": t["search"],
        "search_cur": t["search_cur"],
        "error": f.red_hi,
        "warning": f.yellow,
        "info": f.denim,
        "hint": f.sage,
    }
