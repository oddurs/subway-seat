"""Shared chrome roles for the terminal ports, so every terminal lights the same things.

The Ghostty port set the conventions; these helpers name them.
"""

from ports._lib import tints

ANSI_NAMES = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]


def lit(f):
    """The "on" color: cursor, active tab, focused split. Gold on dark, burnt orange on light."""
    return f.yellow if f.dark else f.orange


def selection(f):
    return f.surface2 if f.dark else f.surface1


def split(f):
    return f.surface0 if f.dark else f.crust


def dim(f, color):
    """Faint text: the color pulled a third of the way into the ground."""
    return f.mix(color, "base", 0.66)


def search(f):
    return tints(f)["search"]


def search_cur(f):
    return tints(f)["search_cur"]
