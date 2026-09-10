"""Xfce Terminal: a color scheme .theme per flavor."""

from ports._lib import HEADER, Out, selection
from ports._terminals import lit

META = {
    "id": "xfce-terminal",
    "name": "Xfce Terminal",
    "category": "Terminals",
    "homepage": "https://docs.xfce.org/apps/xfce4-terminal/start",
    "detect": ["xfce4-terminal"],
    "enable": {
        "where": "Edit › Preferences › Colors › Presets",
        "code": "{name}",
        "lang": "text",
    },
    "notes": "Palette, cursor, bold, selection and the tab activity color. Xfce Terminal doesn't follow the "
    "system light/dark setting, so pick one flavor.",
}


def theme(f):
    rows = {
        "Name": f.name,
        "ColorForeground": f.text,
        "ColorBackground": f.base,
        "ColorCursor": lit(f),
        "ColorCursorForeground": f.base,
        "ColorCursorUseDefault": "FALSE",
        "ColorBold": f.text_hi,
        "ColorBoldUseDefault": "FALSE",
        "ColorSelection": f.text_hi,
        "ColorSelectionBackground": selection(f),
        "ColorSelectionUseDefault": "FALSE",
        "TabActivityColor": f.orange,
        "ColorPalette": ";".join(f.ansi),
    }
    return f"# {HEADER}\n[Scheme]\n" + "\n".join(f"{k}={v}" for k, v in rows.items()) + "\n"


def build(flavors):
    return [
        Out(
            f"{f.slug}.theme",
            theme(f),
            flavor=f.id,
            dest=f"~/.local/share/xfce4/terminal/colorschemes/{f.slug}.theme",
            lang="ini",
        )
        for f in flavors
    ]
