"""Thunderbird: a theme per flavor (manifest + unsigned .xpi), Firefox's theme
colors plus Thunderbird's own panes through a theme_experiment."""

import json

from ports._lib import Out, ink, selection, ui_colors, zip_bytes
from ports.firefox import auto_manifest
from ports.firefox import colors as gecko_colors
from ports.firefox import manifest as gecko_manifest

META = {
    "id": "thunderbird",
    "name": "Thunderbird",
    "category": "Apps",
    "homepage": "https://www.thunderbird.net",
    "enable": {
        "where": "Thunderbird › Tools › Add-ons and Themes",
        "code": "⚙ › Install Add-on From File… › {slug}.xpi",
        "lang": "text",
    },
    "auto": {
        "where": "Thunderbird › Tools › Add-ons and Themes",
        "code": "⚙ › Install Add-on From File… › subway-seat-auto.xpi\n"
        "# Enamel while the system is light, Subway Seat (Walnut) while it's dark",
        "lang": "text",
    },
    "requires": "Thunderbird 115+",
    "detect": ["/Applications/Thunderbird.app", "thunderbird"],
    "notes": "The folder pane, message list, spaces toolbar and tabs, with burnt orange for the selected "
    "space and primary buttons. Thunderbird installs the unsigned .xpi directly.",
}

MIN_VERSION = "115.0"  # Supernova: the spaces toolbar and the variables below

# Thunderbird-only color slots, exposed to themes as CSS variables.
EXPERIMENT = {
    "spaces_bg": "--spaces-bg-color",
    "spaces_bg_active": "--spaces-button-active-bg-color",
    "spaces_button": "--spaces-button-active-text-color",
    "tree_view_bg": "--tree-view-bg",
    "button_primary_bg": "--button-primary-background-color",
    "button_text": "--button-primary-text-color",
    "tree_pane_bg": "--tree-pane-background",
    "tree_card_bg": "--tree-card-background",
    "button_bg": "--button-background-color",
    "list_container_background_selected_current": "--list-container-background-selected-current",
    "calendar_view_toggle_bg": "--calendar-view-toggle-background",
    "calendar_view_toggle_hover_bg": "--calendar-view-toggle-hover-background",
    "tabs_toolbar_bg": "--tabs-toolbar-background-color",
    "lwt_accent_color": "--lwt-accent-color",
    # mail/themes/shared/mail/layout.css: the main layout grounds, text and borders
    **{f"layout_bg_{i}": f"--layout-background-{i}" for i in range(5)},
    **{f"layout_color_{i}": f"--layout-color-{i}" for i in range(4)},
    **{f"layout_border_{i}": f"--layout-border-{i}" for i in range(3)},
}


def colors(f):
    d = f.dark
    c = gecko_colors(f)
    c |= {
        "spaces_bg": f.crust,
        "spaces_bg_active": f.orange,
        "spaces_button": ink(f),
        "tree_view_bg": f.base,
        "button_primary_bg": f.orange,
        "button_text": ink(f),
        "tree_pane_bg": f.mantle,
        "tree_card_bg": f.base,
        "button_bg": f.surface0 if d else f.mantle,
        "list_container_background_selected_current": selection(f),
        "calendar_view_toggle_bg": f.mantle,
        "calendar_view_toggle_hover_bg": f.surface0,
        "tabs_toolbar_bg": f.crust,
        "lwt_accent_color": c["frame"],
        # 0 page, 1 center panes and secondary sidebars, 2 primary sidebars, 3 blocks in the page, 4 elements in them
        "layout_bg_0": f.base,
        "layout_bg_1": f.mantle,
        "layout_bg_2": f.mantle,
        "layout_bg_3": ui_colors(f)["paper"],
        "layout_bg_4": f.surface1 if d else f.surface0,
        # 0 emphasis, 1 body, 2 less, 3 least
        "layout_color_0": f.text_hi,
        "layout_color_1": f.text,
        "layout_color_2": f.subtext1,
        "layout_color_3": f.overlay2,
        # 0 between layout sections, 1 part of an element, 2 strong
        "layout_border_0": f.surface0 if d else f.surface1,
        "layout_border_1": f.surface1 if d else f.surface2,
        "layout_border_2": f.overlay0,
    }
    return c


def with_experiment(m, slug):
    m["browser_specific_settings"]["gecko"] = {"id": f"{slug}-thunderbird@oddurs.github.io",
                                               "strict_min_version": MIN_VERSION}
    # Keep the manifest's key order readable: the experiment before the themes it declares.
    return {k: v for k, v in m.items() if "theme" not in k} | {"theme_experiment": {"colors": EXPERIMENT}} | {
        k: v for k, v in m.items() if "theme" in k}


def build(flavors):
    by = {f.id: f for f in flavors}
    how = "Add-ons and Themes › ⚙ › Install Add-on From File…"
    outs = []
    for f in flavors:
        m = json.dumps(with_experiment(gecko_manifest(f, colors_of=colors), f.slug), indent=2) + "\n"
        outs.append(Out(f"{f.slug}/manifest.json", m, flavor=f.id, lang="json", how=f"inside {f.slug}.xpi"))
        outs.append(Out(f"{f.slug}.xpi", zip_bytes({"manifest.json": m}), flavor=f.id, how=how))
    auto = with_experiment(auto_manifest(by["enamel"], by["walnut"], colors_of=colors), "subway-seat-auto")
    auto = json.dumps(auto, indent=2) + "\n"
    outs.append(Out("subway-seat-auto/manifest.json", auto, lang="json", how="inside subway-seat-auto.xpi"))
    outs.append(Out("subway-seat-auto.xpi", zip_bytes({"manifest.json": auto}), how=how))
    return outs
