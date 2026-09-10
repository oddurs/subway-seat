"""Shared chrome roles for the terminal ports, so every terminal lights the same things.

The Ghostty port set the conventions; these helpers name them. The selection
color and the ANSI names come from `_lib` (`selection`, `ANSI_NAMES`).
"""

from ports._lib import tints


def lit(f):
    """The "on" color: cursor, active tab, focused split. Gold on dark, burnt orange on light."""
    return f.yellow if f.dark else f.orange


def split(f):
    """Divider between panes."""
    return f.surface0 if f.dark else f.crust


def dim(f, color):
    """Faint text: the color pulled a third of the way into the ground."""
    return f.mix(color, "base", 0.66)


def search(f):
    return tints(f)["search"]


def search_cur(f):
    return tints(f)["search_cur"]


def dark_light(f, flavors):
    """(dark, light) for a file that carries both sides: the dark flavors pair with Enamel,
    and Enamel pairs with Walnut."""
    by_id = {x.id: x for x in flavors}
    return (f, by_id["enamel"]) if f.dark else (by_id["walnut"], f)
