"""waybar: a GTK CSS palette per flavor, as `@define-color` names to use in style.css.

Every palette role, plus the layers the other ports use: `paper` for popovers, and
`edge`, `hover` and `selection` as translucent washes of text (waybar's GTK CSS has
`alpha()`), so they sit right on the bar, on paper, or on a module's own color.
"""

import palette as p
from ports._lib import HEADER, INK, Out, ui_colors

META = {
    "id": "waybar",
    "name": "waybar",
    "category": "Desktop",
    "homepage": "https://github.com/Alexays/Waybar",
    "detect": ["waybar"],
    "enable": {
        "where": "~/.config/waybar/style.css, at the top",
        "code": '@import "{slug}.css";\n\n'
        "window#waybar {{ background: @mantle; color: @text; border-bottom: 1px solid @crust; }}\n"
        "#workspaces button {{ color: @subtext0; }}\n"
        "#workspaces button:hover {{ background: @hover; }}\n"
        "#workspaces button.active, #workspaces button.focused {{ color: @text_hi; box-shadow: inset 0 -2px @yellow; }}\n"
        "#workspaces button.urgent {{ color: @orange; }}\n"
        "#battery.warning {{ color: @yellow; }}\n"
        "#battery.critical {{ color: @orange; }}",
        "lang": "css",
    },
    "notes": "Colors only: waybar's look lives in your own style.css, so this is a palette of "
    "`@define-color` names (every role, plus `paper`, `edge`, `hover` and `selection`) to use in it. "
    "The example marks the focused workspace in gold and urgent ones in orange.",
}


def wash(f, level):
    return f"alpha(@text, {INK[level][0 if f.dark else 1] / 100:g})"


def css(f):
    lines = [f"/* {HEADER} */", f"/* {f.name} for waybar: @import it at the top of style.css. */", ""]
    lines += [f"@define-color {role} {f.colors[role]};" for role in p.ROLES]
    lines += [
        "",
        "/* Layers: a raised ground for popovers, and washes of text for borders, hover and selection */",
        f"@define-color paper {ui_colors(f)['paper']};",
        f"@define-color edge {wash(f, 'EDGE')};",
        f"@define-color hover {wash(f, 'L2')};",
        f"@define-color selection {wash(f, 'L4')};",
    ]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.css", css(f), flavor=f.id, dest=f"~/.config/waybar/{f.slug}.css", lang="css") for f in flavors
    ]
