"""Vimium: custom CSS for link hints, the Vomnibar, the find HUD and the help dialog."""

from ports._apps import ink, rgba
from ports._lib import HEADER, Out

META = {
    "id": "vimium",
    "name": "Vimium",
    "category": "Apps",
    "homepage": "https://vimium.github.io",
    "enable": {
        "where": "Vimium Options → Show advanced options → CSS for Vimium UI",
        "code": "Paste the contents of {slug}.css and click Save",
        "lang": "text",
    },
    "notes": "Harvest-gold link hints, a walnut Vomnibar with denim URLs and orange matches, and the find "
    "bar and help dialog to match. Selectors follow Vimium 2.x.",
}


def css(f):
    d = f.dark
    selected = f.mix("orange", "base", 0.20 if d else 0.14)
    line = f.surface0 if d else f.surface1
    hint_border = f.mix("yellow", "crust", 0.55) if d else f.mix("yellow", "text_hi", 0.7)
    return f"""/* {HEADER} */
/* {f.name} for Vimium — paste into Options → CSS for Vimium UI. */

:root {{
  --vimium-background-color: {f.base};
  --vimium-background-text-color: {f.text};
  --vimium-foreground-color: {f.mantle};
  --vimium-foreground-text-color: {f.text};
  --vimium-link-color: {f.denim};
}}

/* Link hints */
div.internal-vimium-hint-marker {{
  padding: 1px 4px;
  background: {f.yellow};
  border: 1px solid {hint_border};
  border-radius: 3px;
  box-shadow: 0 2px 6px {rgba(f.crust if d else f.text_hi, 0.35)};
}}

div.internal-vimium-hint-marker span {{
  color: {ink(f)};
  text-shadow: none;
}}

div.internal-vimium-hint-marker > .matchingCharacter {{
  color: {f.mix("yellow", "crust" if d else "text_hi", 0.5)};
}}

div > .vimiumActiveHintMarker span {{
  color: {f.mix("red", "crust", 0.8) if d else f.crust} !important;
}}

div.internal-vimium-input-hint {{
  background-color: {rgba(f.yellow, 0.2)};
  border: 1px solid {f.yellow};
}}

div.internal-vimium-selected-input-hint {{
  background-color: {rgba(f.orange, 0.25)};
  border: 1px solid {f.orange} !important;
}}

div.vimium-flash {{
  box-shadow: 0 0 4px 2px {f.orange};
}}

body.vimium-find-mode ::selection {{
  background: {f.orange};
  color: {ink(f)};
}}

/* Vomnibar */
#vomnibar {{
  background: {f.base};
  color: {f.text};
  border: 1px solid {line};
  border-radius: 8px;
  box-shadow: 0 12px 32px {rgba(f.crust if d else f.text_hi, 0.45 if d else 0.2)};
}}

#vomnibar #vomnibar-search-area {{
  background: {f.base};
  border-bottom: 1px solid {line};
}}

#vomnibar input {{
  color: {f.text_hi};
  background: {f.mantle};
  border: 1px solid {line};
  border-radius: 5px;
  box-shadow: none;
}}

#vomnibar input:focus {{
  border-color: {f.orange};
}}

#vomnibar input::selection {{
  background-color: {f.surface2 if d else f.surface1};
  color: {f.text_hi};
}}

#vomnibar ul {{
  background: {f.base};
}}

#vomnibar li {{
  border-bottom: 1px solid {f.surface0 if d else f.mantle};
}}

#vomnibar li .source {{
  color: {f.overlay1};
}}

#vomnibar li .title,
#vomnibar li em {{
  color: {f.text};
}}

#vomnibar li .url {{
  color: {f.denim};
}}

#vomnibar li .match,
#vomnibar li .title .match {{
  color: {f.orange};
  font-weight: bold;
}}

#vomnibar li .relevancy {{
  color: {f.overlay0};
}}

#vomnibar li.selected {{
  background-color: {selected};
}}

/* Find HUD */
#hud-container {{
  background-color: {f.mantle};
  color: {f.text};
  border: 1px solid {line};
  box-shadow: none;
}}

#hud-container #search-area,
#hud-container #hud {{
  background-color: {f.mantle};
  color: {f.text};
}}

span#hud-match-count {{
  color: {f.overlay1};
}}

/* Help dialog */
#container {{
  background-color: {f.base};
  border: 1px solid {line};
}}

#dialog {{
  background-color: {f.base};
  color: {f.text};
}}

#dialog a,
#dialog h1 .vim {{
  color: {f.orange};
}}

#dialog a#close {{
  color: {f.overlay1};
}}

#dialog a#close:hover {{
  color: {f.text_hi};
}}

#dialog h2,
#dialog .help-description {{
  color: {f.text};
}}

#dialog div.divider {{
  background-color: {line};
}}

#dialog .key,
body.vimium-body .key {{
  color: {f.text};
  background-color: {f.mantle};
  border: 1px solid {line};
  border-bottom-color: {f.surface1 if d else f.surface2};
  box-shadow: none;
}}

/* Options and exclusions pages */
body.vimium-body {{
  background-color: {f.base};
  color: {f.text};
}}

body.vimium-body a,
body.vimium-body a:visited {{
  color: {f.denim};
}}

body.vimium-body textarea,
body.vimium-body input {{
  background-color: {f.mantle};
  border-color: {line};
  color: {f.text};
}}

body.vimium-body div.example {{
  color: {f.overlay2};
}}
"""


def build(flavors):
    return [Out(f"{f.slug}.css", css(f), flavor=f.id, dest="Vimium Options → CSS for Vimium UI", lang="css")
            for f in flavors]
