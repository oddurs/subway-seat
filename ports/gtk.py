"""GTK 4 / libadwaita (and GTK 3 through adw-gtk3): named-color overrides per flavor.

libadwaita reads its UI colors from named colors (`@define-color window_bg_color …`)
and, since 1.6, from CSS variables that default to them. Each file sets both, the way
adw-colors does, so it works on every libadwaita and wins over the system accent.
The layering is the workbench's: header bars and sidebars on mantle, windows and
views on base, popovers and dialogs on paper, cards a wash of text, and burnt orange
as the accent. adw-gtk3 reads the same names, so the GTK 3 file is the same palette
without the variables.
"""

import palette as p
from ports._lib import HEADER, Out, ink, resolve, ui_colors

META = {
    "id": "gtk",
    "name": "GTK and libadwaita",
    "category": "Desktop",
    "homepage": "https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/css-variables.html",
    "detect": ["gnome-shell", "~/.config/gtk-4.0", "~/.config/gtk-3.0"],
    "enable": {
        "where": "~/.config/gtk-4.0/gtk.css, then restart the apps",
        "code": '@import url("{slug}.css");',
        "lang": "css",
        "file": "~/.config/gtk-4.0/gtk.css",
    },
    "auto": {
        "where": "~/.config/gtk-4.0/gtk.css (GTK 4.20+, GNOME 49+)",
        "code": '@import url("subway-seat-enamel.css");\n'
        "@media (prefers-color-scheme: dark) {\n"
        '  @import url("subway-seat.css");\n'
        "}",
        "lang": "css",
        "file": "~/.config/gtk-4.0/gtk.css",
    },
    "notes": "Window, view, header bar, sidebar, card, dialog, popover and accent colors for libadwaita "
    "apps, as named colors and CSS variables. The GTK 3 file needs the adw-gtk3 theme. Flatpak apps "
    "only see these files after `flatpak override --user --filesystem=xdg-config/gtk-4.0:ro` "
    "(and `gtk-3.0`).",
}


def rgba(color):
    """#RRGGBB or #RRGGBBAA → a CSS color GTK 3 and 4 both parse."""
    if len(color) == 7:
        return color
    r, g, b = p.hex_to_rgb(color[:7])
    return f"rgba({r}, {g}, {b}, {round(int(color[7:], 16) / 255, 2):g})"


def colors(f):
    """libadwaita's named colors, in its own order. Levels are (dark, light) where they differ."""
    c = ui_colors(f)
    d = f.dark

    def x(dark_expr, light_expr=None):
        return rgba(resolve(dark_expr if d else (light_expr or dark_expr), f))

    on_accent = ink(f) if d else c["paper"]
    return {
        # accent and status: the fill, the text on it, and the color as text on the window
        "accent_bg_color": f.orange,
        "accent_fg_color": on_accent,
        "accent_color": f.orange,
        "destructive_bg_color": f.red,
        "destructive_fg_color": on_accent,
        "destructive_color": f.red_hi if d else f.red,
        "success_bg_color": f.green,
        "success_fg_color": on_accent,
        "success_color": f.green,
        "warning_bg_color": f.yellow,
        "warning_fg_color": on_accent,
        "warning_color": f.yellow,
        "error_bg_color": f.red,
        "error_fg_color": on_accent,
        "error_color": f.red_hi if d else f.red,
        # grounds
        "window_bg_color": f.base,
        "window_fg_color": f.text,
        "view_bg_color": f.base,
        "view_fg_color": f.text,
        "headerbar_bg_color": f.mantle,
        "headerbar_fg_color": f.text,
        "headerbar_border_color": f.text,
        "headerbar_backdrop_color": f.base,
        "headerbar_shade_color": x("shadow@36", "shadow@12"),
        "headerbar_darker_shade_color": x("shadow@90", "shadow@12"),
        "sidebar_bg_color": f.mantle,
        "sidebar_fg_color": f.subtext1,
        "sidebar_backdrop_color": f.mix("mantle", "base", 0.5),
        "sidebar_shade_color": x("shadow@25", "shadow@7"),
        "sidebar_border_color": x("crust", "text@EDGE"),
        "secondary_sidebar_bg_color": f.mix("mantle", "base", 0.5),
        "secondary_sidebar_fg_color": f.text,
        "secondary_sidebar_backdrop_color": f.base,
        "secondary_sidebar_shade_color": x("shadow@25", "shadow@7"),
        "secondary_sidebar_border_color": x("crust", "text@EDGE"),
        "card_bg_color": x("text@L2", "paper"),
        "card_fg_color": f.text,
        "card_shade_color": x("shadow@36", "shadow@7"),
        "dialog_bg_color": c["paper"],
        "dialog_fg_color": f.text,
        "popover_bg_color": c["paper"],
        "popover_fg_color": f.text,
        "popover_shade_color": x("shadow@25", "shadow@7"),
        "thumbnail_bg_color": c["paper"],
        "thumbnail_fg_color": f.text,
        "shade_color": x("shadow@25", "shadow@7"),
        "scrollbar_outline_color": x("shadow@95", "paper"),
    }


# libadwaita 1.6+ variables with no named color behind them
def variables(f):
    d = f.dark
    return {
        "active-toggle-bg-color": rgba(resolve("text@20", f)) if d else ui_colors(f)["paper"],
        "active-toggle-fg-color": f.text_hi if d else f.text,
        "overview-bg-color": f.mantle,
        "overview-fg-color": f.text,
    }


def gtk4(f):
    named = colors(f)
    lines = [f"/* {HEADER} */", f"/* {f.name} for GTK 4 and libadwaita */", ""]
    lines += [f"@define-color {k} {v};" for k, v in named.items()]
    lines += ["", ":root {"]
    lines += [f"  --{k.replace('_', '-')}: @{k};" for k in named]
    lines += [f"  --{k}: {v};" for k, v in variables(f).items()]
    lines += ["}", ""]
    return "\n".join(lines)


def gtk3(f):
    lines = [f"/* {HEADER} */", f"/* {f.name} for GTK 3 with the adw-gtk3 theme */", ""]
    lines += [f"@define-color {k} {v};" for k, v in colors(f).items() if not k.startswith("secondary_")]
    return "\n".join(lines) + "\n"


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(
            Out(f"gtk-4.0/{f.slug}.css", gtk4(f), flavor=f.id, dest=f"~/.config/gtk-4.0/{f.slug}.css", lang="css")
        )
        outs.append(
            Out(
                f"gtk-3.0/{f.slug}.css",
                gtk3(f),
                flavor=f.id,
                dest=f"~/.config/gtk-3.0/{f.slug}.css",
                lang="css",
                how=f'with the adw-gtk3 theme, add `@import url("{f.slug}.css");` to ~/.config/gtk-3.0/gtk.css',
            )
        )
    return outs
