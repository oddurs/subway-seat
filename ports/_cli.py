"""Small helpers shared by the CLI & TUI ports."""

import palette as p


def ink(f):
    """Text that sits on a saturated accent background."""
    return f.crust if f.dark else f.base


def bar(f):
    """Ground for status bars and title strips: a step darker than base."""
    return f.mantle if f.dark else f.crust


def selection(f):
    return f.surface2 if f.dark else f.surface1


def stripe(f, n):
    """n colors along the 70s stripe: avocado → harvest gold → burnt orange → redbird."""
    stops = [f.green, f.yellow, f.orange, f.red]
    out = []
    for i in range(n):
        t = i / (n - 1) * (len(stops) - 1)
        seg = min(int(t), len(stops) - 2)
        out.append(p.blend(stops[seg + 1], stops[seg], t - seg))
    return out
