"""Thunderbird: a theme per flavor (manifest + unsigned .xpi), Firefox's theme
colors plus Thunderbird's own panes through a theme_experiment."""

import json

from ports._apps import AUTHOR, DESCRIPTION, VERSION, ink, select, zip_bytes
from ports._lib import HEADER, REPO, Out
from ports.firefox import colors as gecko_colors

META = {
    "id": "thunderbird",
    "name": "Thunderbird",
    "category": "Apps",
    "homepage": "https://www.thunderbird.net",
    "enable": {
        "where": "Thunderbird → Tools → Add-ons and Themes",
        "code": "⚙ → Install Add-on From File… → {slug}.xpi",
        "lang": "text",
    },
    "notes": "The folder pane, message list, spaces toolbar and tabs, with burnt orange for the selected "
    "space and primary buttons. Thunderbird installs the unsigned .xpi directly.",
}

# Thunderbird-only color slots, exposed to themes as CSS variables.
EXPERIMENT = {
    "spaces_bg": "--spaces-bg-color",
    "spaces_bg_active": "--spaces-button-active-bg-color",
    "spaces_button": "--spaces-button-active-text-color",
    "tree_view_bg": "--tree-view-bg",
    "bg_color": "--bg-color",
    "button_primary_bg": "--button-primary-background-color",
    "button_text": "--button-primary-text-color",
    "tree_pane_bg": "--tree-pane-background",
    "tree_card_bg": "--tree-card-background",
    "layout_bg_0": "--layout-background-0",
    "layout_bg_1": "--layout-background-1",
    "button_bg": "--button-background-color",
    "list_container_background_selected_current": "--list-container-background-selected-current",
    "calendar_view_toggle_bg": "--calendar-view-toggle-background",
    "calendar_view_toggle_hover_bg": "--calendar-view-toggle-hover-background",
    "tabs_toolbar_bg": "--tabs-toolbar-background-color",
}


def colors(f):
    c = gecko_colors(f)
    c |= {
        "spaces_bg": f.crust,
        "spaces_bg_active": f.orange,
        "spaces_button": ink(f),
        "tree_view_bg": f.base,
        "bg_color": f.base,
        "button_primary_bg": f.orange,
        "button_text": ink(f),
        "tree_pane_bg": f.mantle,
        "tree_card_bg": f.base,
        "layout_bg_0": f.base,
        "layout_bg_1": f.mantle,
        "button_bg": f.surface0 if f.dark else f.mantle,
        "list_container_background_selected_current": select(f),
        "calendar_view_toggle_bg": f.mantle,
        "calendar_view_toggle_hover_bg": f.surface0,
        "tabs_toolbar_bg": f.crust,
    }
    return c


def manifest(f):
    return {
        "manifest_version": 2,
        "name": f.name,
        "version": VERSION,
        "description": f"{DESCRIPTION} {f.blurb} ({HEADER})",
        "author": AUTHOR,
        "homepage_url": REPO,
        "browser_specific_settings": {
            "gecko": {"id": f"{f.slug}-thunderbird@oddurs.github.io", "strict_min_version": "115.0"},
        },
        "theme_experiment": {"colors": EXPERIMENT},
        "theme": {
            "colors": colors(f),
            "properties": {
                "color_scheme": "dark" if f.dark else "light",
                "content_color_scheme": "dark" if f.dark else "light",
            },
        },
    }


def build(flavors):
    outs = []
    for f in flavors:
        m = json.dumps(manifest(f), indent=2) + "\n"
        outs.append(Out(f"{f.slug}/manifest.json", m, flavor=f.id, dest="inside the .xpi", lang="json"))
        outs.append(Out(f"{f.slug}.xpi", zip_bytes({"manifest.json": m}), flavor=f.id,
                        dest="Add-ons and Themes → ⚙ → Install Add-on From File"))
    return outs
