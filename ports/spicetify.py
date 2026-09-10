"""Spicetify (Spotify): one theme folder with every flavor as a color scheme."""

import json

import palette as p
from ports._apps import AUTHOR, AUTHOR_URL, DESCRIPTION
from ports._lib import HEADER, REPO, Out, ink, selection

META = {
    "id": "spicetify",
    "name": "Spotify (Spicetify)",
    "category": "Apps",
    "homepage": "https://spicetify.app",
    "enable": {
        "where": "a terminal, with the theme in Spicetify's Themes folder",
        "code": "spicetify config current_theme subway-seat color_scheme {id}\nspicetify apply",
        "lang": "sh",
    },
    "detect": ["spicetify"],
    "notes": "Spicetify's color keys plus the whole palette as `--spice-*` variables, and a small user.css "
    "that turns Spotify's green accent into burnt orange and puts dark ink on its notification banners.",
}

# Spicetify's config folder is ~/.config/spicetify on macOS and Linux, %APPDATA%\spicetify on Windows.
THEME_DIR = "~/.config/spicetify/Themes/subway-seat"
WINDOWS = "on Windows, %APPDATA%\\spicetify\\Themes\\subway-seat\\"


def scheme(f):
    dark = f.dark
    return {
        "text": f.text,
        "subtext": f.subtext0 if dark else f.subtext1,
        "main": f.base,
        "main-elevated": f.surface0 if dark else f.mantle,
        "highlight": f.surface0,
        "highlight-elevated": f.surface1,
        "sidebar": f.mantle,
        "player": f.crust,
        "card": f.surface0 if dark else f.mantle,
        "shadow": f.crust if dark else f.overlay0,
        "selected-row": f.overlay2,
        "button": f.orange,
        "button-active": f.orange_hi,
        "button-disabled": f.overlay0,
        "tab-active": f.surface1,
        "notification": f.denim,        # banner grounds; user.css puts ink on them
        "notification-error": f.red,
        "equalizer": f.orange,
        "misc": f.overlay1,
        # Extras for user.css (and your own snippets): the whole palette.
        "ink": ink(f),
        "selection": selection(f),
        **{role.replace("_", "-"): f.colors[role] for role in p.ROLES},
    }


def color_ini(flavors):
    out = [f"; {HEADER}", f"; {REPO}", ""]
    for f in flavors:
        out.append(f"[{f.id}]")
        out.append(f"; {f.name} — {f.blurb}")
        s = scheme(f)
        width = max(map(len, s))
        out += [f"{k:<{width}} = {v.lstrip('#')}" for k, v in s.items()]
        out.append("")
    return "\n".join(out)


USER_CSS = f"""/* {HEADER} */
/* Subway Seat for Spicetify: the color scheme does most of the work; this only
   swaps Spotify's green accent for the scheme's button color and tidies a few
   details. Everything here reads --spice-* variables, so every flavor shares it. */

.encore-dark-theme,
.encore-light-theme,
.encore-dark-theme .encore-base-set,
.encore-light-theme .encore-base-set {{
  --text-bright-accent: var(--spice-button);
  --essential-bright-accent: var(--spice-button);
  --decorative-base: var(--spice-text);
  --background-base: var(--spice-main);
  --background-highlight: var(--spice-highlight);
  --background-press: var(--spice-highlight-elevated);
  --background-elevated-base: var(--spice-main-elevated);
  --background-elevated-highlight: var(--spice-highlight);
  --background-tinted-base: rgba(var(--spice-rgb-selected-row), 0.08);
  --background-tinted-highlight: rgba(var(--spice-rgb-selected-row), 0.14);
  --text-base: var(--spice-text);
  --text-subdued: var(--spice-subtext);
  --essential-base: var(--spice-text);
  --essential-subdued: var(--spice-button-disabled);
  --essential-announcement: var(--spice-denim);
  --essential-negative: var(--spice-notification-error);
  --essential-warning: var(--spice-yellow);
  --essential-positive: var(--spice-green);
}}

.encore-dark-theme .encore-bright-accent-set,
.encore-light-theme .encore-bright-accent-set {{
  --background-base: var(--spice-button);
  --background-highlight: var(--spice-button-active);
  --background-press: var(--spice-button-active);
  --background-elevated-base: var(--spice-button);
  --background-elevated-highlight: var(--spice-button-active);
  --text-base: var(--spice-ink);
  --essential-base: var(--spice-ink);
}}

/* Notification banners: ink on denim (info) and on red (errors), not light text. */
.encore-dark-theme .encore-announcement-set,
.encore-light-theme .encore-announcement-set,
.encore-dark-theme .encore-negative-set,
.encore-light-theme .encore-negative-set {{
  --text-base: var(--spice-ink);
  --text-subdued: var(--spice-ink);
  --essential-base: var(--spice-ink);
  --essential-subdued: var(--spice-ink);
  --decorative-base: var(--spice-ink);
}}

.encore-dark-theme .encore-announcement-set,
.encore-light-theme .encore-announcement-set {{
  --background-base: var(--spice-notification);
}}

.encore-dark-theme .encore-negative-set,
.encore-light-theme .encore-negative-set {{
  --background-base: var(--spice-notification-error);
}}

.encore-dark-theme .encore-announcement-set > *,
.encore-light-theme .encore-announcement-set > *,
.encore-dark-theme .encore-negative-set > *,
.encore-light-theme .encore-negative-set > * {{
  --parents-essential-base: var(--spice-ink);
}}

::selection {{
  background-color: var(--spice-selection);
  color: var(--spice-text-hi);
}}

:focus-visible {{
  outline-color: var(--spice-button);
}}
"""


# The Spicetify Marketplace reads manifest.json from the root of a repository tagged
# `spicetify-themes`, with every path relative to that root.
HERE = "dist/spicetify"


def marketplace_manifest():
    return json.dumps([{
        "name": "Subway Seat",
        "description": DESCRIPTION,
        "preview": "assets/previews/spicetify.webp",  # the per-port preview image (not captured yet)
        "readme": f"{HERE}/README.md",
        "usercss": f"{HERE}/subway-seat/user.css",
        "schemes": f"{HERE}/subway-seat/color.ini",
        "authors": [{"name": AUTHOR, "url": AUTHOR_URL}],
        "tags": ["dark", "light", "warm", "retro", "70s"],
    }], indent=2) + "\n"


def build(flavors):
    return [
        Out("subway-seat/color.ini", color_ini(flavors), dest=f"{THEME_DIR}/color.ini", lang="ini", how=WINDOWS),
        Out("subway-seat/user.css", USER_CSS, dest=f"{THEME_DIR}/user.css", lang="css", how=WINDOWS),
        Out("manifest.json", marketplace_manifest(), lang="json",
            how="for the Spicetify Marketplace: a copy belongs at the repository root, which its paths are relative to"),
    ]
