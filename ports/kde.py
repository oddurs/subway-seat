"""KDE Plasma: a .colors scheme per flavor, with every [Colors:*] group and [WM].

The layering follows the VS Code workbench: chrome (window, header, title bar) on
mantle, views on base, raised buttons and tooltips a step toward the light, hover a
translucent wash of text, and the selection a burnt-orange wash, all flattened onto
their ground because a .colors file has no alpha. Qt's single highlight color also
fills progress bars, sliders and checked boxes, so it has to be a color and not only
a wash of text. Enamel's complementary areas (lock screen, OSDs) use Walnut, the way
Breeze Light's are dark.
"""

from ports._desktop import readable
from ports._lib import HEADER, Out, rgb, solid, ui_colors

META = {
    "id": "kde",
    "name": "KDE Plasma",
    "category": "Desktop",
    "homepage": "https://kde.org/plasma-desktop/",
    "detect": ["plasmashell", "plasma-apply-colorscheme"],
    "enable": {
        "where": "System Settings › Colors & Themes › Colors, or a shell",
        "code": "plasma-apply-colorscheme {slug}",
        "lang": "sh",
    },
    "notes": "Every color group Plasma reads (window, view, button, header, active and inactive, "
    "selection, tooltip, complementary) plus the window-manager title colors. KDE apps, Plasma itself and, "
    "through Plasma's GTK settings, GTK apps pick it up. Konsole has its own port. Plasma's automatic "
    "light and dark switching changes global themes, not color schemes, so pick a flavor.",
}


def foregrounds(f, ground):
    """The eight foreground roles, each checked against the group's own ground."""
    return {
        "ForegroundActive": readable(f, "orange", ground),
        "ForegroundInactive": readable(f, "subtext0", ground),
        "ForegroundLink": readable(f, "denim", ground),
        "ForegroundNegative": readable(f, "red_hi" if f.dark else "red", ground),
        "ForegroundNeutral": readable(f, "yellow", ground),
        "ForegroundNormal": f.text,
        "ForegroundPositive": readable(f, "green", ground),
        "ForegroundVisited": readable(f, "clay", ground),
    }


def decorations(f):
    return {
        "DecorationFocus": f.orange,
        "DecorationHover": solid("text@35", f, over="base"),
    }


def group(f, normal, alternate):
    return {"BackgroundAlternate": alternate, "BackgroundNormal": normal, **decorations(f), **foregrounds(f, normal)}


def groups(f, partner):
    c = ui_colors(f)
    raised = f.surface1 if f.dark else c["paper"]
    selection = solid("orange@55", f, over="base")
    on_selection = {
        "ForegroundActive": f.text_hi,
        "ForegroundInactive": readable(f, "subtext1", selection, 4.5),
        "ForegroundLink": readable(f, "denim_hi" if f.dark else "denim", selection),
        "ForegroundNegative": readable(f, "red_hi" if f.dark else "red", selection),
        "ForegroundNeutral": readable(f, "yellow_hi" if f.dark else "yellow", selection),
        "ForegroundNormal": f.text_hi,
        "ForegroundPositive": readable(f, "green_hi" if f.dark else "green", selection),
        "ForegroundVisited": readable(f, "clay", selection),
    }
    comp = f if f.dark else partner  # Breeze Light keeps its complementary areas dark too
    window = group(f, f.mantle, solid("text@L1", f, over="mantle"))
    return {
        "Colors:Button": group(f, raised, solid("orange@25", f, over="base")),
        "Colors:Complementary": group(comp, comp.crust, comp.mantle),
        "Colors:Header": group(f, f.mantle, f.crust),
        # Plasma copies the Window group here when it applies a scheme, so match it
        "Colors:Header][Inactive": window,
        "Colors:Selection": {
            "BackgroundAlternate": solid("orange@25", f, over="base"),
            "BackgroundNormal": selection,
            **decorations(f),
            **on_selection,
        },
        "Colors:Tooltip": group(f, c["paper"], solid("text@L1", f, over="paper")),
        "Colors:View": group(f, f.base, solid("text@L1", f, over="base")),
        "Colors:Window": window,
    }


def triplet(color):
    return ",".join(str(v) for v in rgb(color))


def scheme(f, partner):
    sections = [
        # Breeze's effect settings: disabled widgets fade toward the ground, inactive windows don't change
        (
            "ColorEffects:Disabled",
            {
                "Color": triplet(f.base),
                "ColorAmount": "0",
                "ColorEffect": "0",
                "ContrastAmount": "0.65",
                "ContrastEffect": "1",
                "IntensityAmount": "0.1",
                "IntensityEffect": "2",
            },
        ),
        (
            "ColorEffects:Inactive",
            {
                "ChangeSelectionColor": "true",
                "Color": triplet(f.overlay1),
                "ColorAmount": "0.025",
                "ColorEffect": "2",
                "ContrastAmount": "0.1",
                "ContrastEffect": "2",
                "Enable": "false",
                "IntensityAmount": "0",
                "IntensityEffect": "0",
            },
        ),
    ]
    sections += [(name, {k: triplet(v) for k, v in sorted(keys.items())}) for name, keys in groups(f, partner).items()]
    inactive = readable(f, "subtext0", f.mantle)
    sections += [
        (
            "General",
            {"ColorScheme": f.slug, "Name": f.name, "accentActiveTitlebar": "false", "shadeSortColumn": "true"},
        ),
        ("KDE", {"contrast": "4"}),
        (
            "WM",
            {
                "activeBackground": triplet(f.mantle),
                "activeBlend": triplet(f.text),
                "activeForeground": triplet(f.text),
                "inactiveBackground": triplet(f.mantle),
                "inactiveBlend": triplet(inactive),
                "inactiveForeground": triplet(inactive),
            },
        ),
    ]
    body = "\n\n".join(f"[{name}]\n" + "\n".join(f"{k}={v}" for k, v in keys.items()) for name, keys in sections)
    return f"# {HEADER}\n\n{body}\n"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    return [
        Out(
            f"{f.slug}.colors",
            scheme(f, by_id["walnut"]),
            flavor=f.id,
            dest=f"~/.local/share/color-schemes/{f.slug}.colors",
            lang="ini",
        )
        for f in flavors
    ]
