"""Small helpers shared by the CLI & TUI ports. The general ones (`ink`,
`selection`, `tints`, the markers) live in _lib."""

import palette as p
from ports._lib import MARK_END, MARK_START


def bar(f):
    """Ground for status bars and title strips: a step darker than base."""
    return f.mantle if f.dark else f.crust


def row(f):
    """Ground for the highlighted row in a list or table (lighter than a text selection)."""
    return f.surface1 if f.dark else f.surface0


def stripe(f, n):
    """n colors along the 70s stripe: avocado → harvest gold → burnt orange → redbird."""
    stops = [f.green, f.yellow, f.orange, f.red]
    out = []
    for i in range(n):
        t = i / (n - 1) * (len(stops) - 1)
        seg = min(int(t), len(stops) - 2)
        out.append(p.blend(stops[seg + 1], stops[seg], t - seg))
    return out


def marked(body):
    """A block for appending to someone else's config, between the uninstall markers."""
    return f"{MARK_START}\n{body.strip()}\n{MARK_END}\n"


# Git's moved-code slots (diff.colorMoved), with git's own defaults. The git
# port writes them in palette colors and the delta port maps both spellings, so
# delta recognizes moved lines with or without the git port installed.
MOVED = {
    #  slot                   role     git's default
    "oldMoved": ("orange", "bold purple"),
    "oldMovedAlternative": ("denim", "bold blue"),
    "newMoved": ("sage", "bold cyan"),
    "newMovedAlternative": ("yellow", "bold yellow"),
}


def git_color(*parts):
    """A git color value: colors (#hex), then attributes, quoted for gitconfig."""
    return '"' + " ".join(x.lower() if x.startswith("#") else x for x in parts) + '"'
