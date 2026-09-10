"""Chrome (and Chromium browsers that take Chrome themes): a theme extension per flavor."""

import json

from ports._apps import rgb_list
from ports._lib import HEADER, VERSION, Out, zip_bytes

META = {
    "id": "chrome",
    "name": "Chrome",
    "category": "Apps",
    "homepage": "https://www.google.com/chrome/",
    "enable": {
        "where": "chrome://extensions (Developer mode on)",
        "code": "Unzip {slug}.zip, then Load unpacked → pick the {slug} folder",
        "lang": "text",
    },
    "detect": [
        "/Applications/Google Chrome.app", "/Applications/Brave Browser.app", "/Applications/Microsoft Edge.app",
        "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "brave-browser", "microsoft-edge",
    ],
    "notes": "Colors the tab strip, toolbar, address bar and new-tab page; incognito windows get a faint "
    "terracotta frame so you can tell them apart. Works in Edge and Brave too.",
}

# The Chrome Web Store cuts descriptions off at 132 characters.
DESCRIPTION_LIMIT = 132


def description(f):
    text = f"Harvest gold, burnt orange and avocado on walnut. {f.blurb}"
    if len(text) > DESCRIPTION_LIMIT:
        raise SystemExit(f"chrome: the {f.name} description is {len(text)} characters (limit {DESCRIPTION_LIMIT})")
    return text


def colors(f):
    incognito = f.mix("clay", "crust", 0.16 if f.dark else 0.2)
    c = {
        "frame": f.crust,
        "frame_inactive": f.crust if f.dark else f.mantle,
        "frame_incognito": incognito,
        "frame_incognito_inactive": incognito,
        "background_tab": f.crust,
        "background_tab_inactive": f.crust if f.dark else f.mantle,
        "background_tab_incognito": incognito,
        "background_tab_incognito_inactive": incognito,
        "toolbar": f.base,
        "tab_text": f.text,
        "tab_background_text": f.overlay2,
        "tab_background_text_inactive": f.overlay1,
        "tab_background_text_incognito": f.subtext0,
        "tab_background_text_incognito_inactive": f.overlay2,
        "bookmark_text": f.subtext1,
        "toolbar_button_icon": f.subtext1,
        "toolbar_text": f.text,
        "omnibox_background": f.mantle,
        "omnibox_text": f.text,
        "ntp_background": f.base,
        "ntp_text": f.text,
        "ntp_link": f.denim,
        "ntp_header": f.orange,
        "button_background": f.crust,
    }
    return {k: rgb_list(v) for k, v in c.items()}


def manifest(f):
    m = {
        "manifest_version": 3,
        "name": f.name,
        "version": VERSION,
        "description": description(f),
        "theme": {"colors": colors(f)},
    }
    if f.dark:
        m["theme"]["properties"] = {"ntp_logo_alternate": 1}  # light Google logo on the dark new-tab page
    return json.dumps(m, indent=2) + "\n"


def build(flavors):
    outs = []
    for f in flavors:
        m = manifest(f)
        readme = f"{HEADER}\nUnzip, open chrome://extensions, turn on Developer mode, then Load unpacked → this folder.\n"
        outs.append(Out(f"{f.slug}/manifest.json", m, flavor=f.id, lang="json",
                        how="the unpacked extension: chrome://extensions › Load unpacked › this folder"))
        outs.append(Out(f"{f.slug}.zip", zip_bytes({f"{f.slug}/manifest.json": m, f"{f.slug}/README.txt": readme}),
                        flavor=f.id, how="unzip anywhere, then chrome://extensions › Load unpacked"))
    return outs
