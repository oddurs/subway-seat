"""Shared roles for the Linux desktop ports (Hyprland, waybar, rofi, fuzzel, dunst, mako).

Launchers and notifications are popovers, so they sit on the raised `paper` ground
with a quiet `edge`; hover and selection are text washes flattened onto paper. Accents
are kept for meaning: gold for focus and matches, orange for urgent, denim for info.
"""

import palette as p
from ports._lib import solid, ui_colors


def roles(f):
    paper = ui_colors(f)["paper"]
    return {
        "bar": f.mantle,  # chrome: status bars
        "paper": paper,  # launchers, notifications
        "text": f.text,
        "strong": f.text_hi,
        "muted": f.subtext1,  # prompts, secondary lines
        "faint": f.overlay1,  # placeholders, counters
        "edge": solid("text@EDGE", f, over="paper"),
        "hover": solid("text@L2", f, over="paper"),
        "selection": solid("text@L5", f, over="paper"),
        "focus": f.yellow,
        "match": f.yellow,
        "urgent": f.orange,
        "info": f.denim,
        "good": f.green,
        "bad": f.red_hi if f.dark else f.red,
        "inactive": f.surface1,  # borders of unfocused windows
    }


def bare(color):
    """#RRGGBB → RRGGBB."""
    return color.lstrip("#").upper()


def contrast(a, b):
    """WCAG contrast ratio of two #RRGGBB colors."""

    def lum(color):
        def ch(v):
            v /= 255
            return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

        r, g, b_ = (ch(v) for v in p.hex_to_rgb(color))
        return 0.2126 * r + 0.7152 * g + 0.0722 * b_

    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def readable(f, role, ground, minimum=3.0):
    """`role` if it reads on `ground`, else the role pulled toward the text until it does."""
    for t in (0, 0.25, 0.5, 0.75, 1):
        color = f.mix("text_hi", role, t)
        if contrast(color, ground) >= minimum:
            return color
    return f.text_hi
