"""Spicetify (Spotify): one theme folder with every flavor as a colour scheme."""

import json

import palette as p
from ports._apps import AUTHOR, AUTHOR_URL, DESCRIPTION, ink, select
from ports._lib import HEADER, REPO, Out

META = {
    "id": "spicetify",
    "name": "Spotify (Spicetify)",
    "category": "Apps",
    "homepage": "https://spicetify.app",
    "enable": {
        "where": "~/.config/spicetify/Themes/subway-seat/",
        "code": "spicetify config current_theme subway-seat color_scheme {id}\nspicetify apply",
        "lang": "sh",
    },
    "notes": "Spicetify's colour keys plus the whole palette as `--spice-*` variables, and a small user.css "
    "that turns Spotify's green accent into burnt orange.",
}


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
        "notification": f.denim,
        "notification-error": f.red,
        "equalizer": f.orange,
        "misc": f.overlay1,
        # Extras for user.css (and your own snippets): the whole palette.
        "ink": ink(f),
        "selection": select(f),
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
/* Subway Seat for Spicetify: the colour scheme does most of the work; this only
   swaps Spotify's green accent for the scheme's button colour and tidies a few
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

::selection {{
  background-color: var(--spice-selection);
  color: var(--spice-text-hi);
}}

:focus-visible {{
  outline-color: var(--spice-button);
}}
"""


def marketplace_manifest():
    return json.dumps([{
        "name": "Subway Seat",
        "description": DESCRIPTION,
        "preview": "preview.png",
        "readme": "README.md",
        "usercss": "subway-seat/user.css",
        "schemes": "subway-seat/color.ini",
        "authors": [{"name": AUTHOR, "url": AUTHOR_URL}],
        "tags": ["dark", "light", "warm", "retro", "70s"],
    }], indent=2) + "\n"


def build(flavors):
    return [
        Out("subway-seat/color.ini", color_ini(flavors), dest="~/.config/spicetify/Themes/subway-seat/color.ini",
            lang="ini"),
        Out("subway-seat/user.css", USER_CSS, dest="~/.config/spicetify/Themes/subway-seat/user.css", lang="css"),
        Out("manifest.json", marketplace_manifest(),
            dest="repo root, for the Spicetify Marketplace (paths are relative to it)", lang="json"),
    ]
