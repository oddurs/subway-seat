"""Vimium: custom CSS for link hints, the Vomnibar, the find HUD and the help dialog."""

from ports._apps import rgba
from ports._lib import HEADER, Out, ink, selection, solid, ui_colors

META = {
    "id": "vimium",
    "name": "Vimium",
    "category": "Apps",
    "homepage": "https://vimium.github.io",
    "enable": {
        "where": "Vimium Options › Show advanced options › CSS for Vimium UI",
        "code": "Paste the contents of {slug}.css and click Save",
        "lang": "text",
    },
    "auto": {
        "where": "Vimium Options › Show advanced options › CSS for Vimium UI",
        "code": "Paste the contents of subway-seat-auto.css and click Save\n"
        "# Enamel while the system is light, Subway Seat (Walnut) while it's dark",
        "lang": "text",
    },
    "requires": "Vimium 2.0+",
    "notes": "Harvest-gold link hints, a walnut Vomnibar with denim URLs and orange matches, and the find "
    "bar and help dialog to match.",
}


def rules(f):
    d = f.dark
    selected = f.mix("orange", "base", 0.20 if d else 0.14)
    line = f.surface0 if d else f.surface1
    paper = ui_colors(f)["paper"]  # the Vomnibar and the find HUD float over the page
    edge = solid("text@EDGE", f, "paper")  # a hairline that shows on paper
    hint_border = f.mix("yellow", "crust", 0.55) if d else f.mix("yellow", "text_hi", 0.7)
    return f""":root {{
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
  background: {paper};
  color: {f.text};
  border: 1px solid {edge};
  border-radius: 8px;
  box-shadow: 0 12px 32px {rgba(f.crust if d else f.text_hi, 0.45 if d else 0.2)};
}}

#vomnibar #vomnibar-search-area {{
  background: {paper};
  border-bottom: 1px solid {edge};
}}

#vomnibar input {{
  color: {f.text_hi};
  background: {f.base};
  border: 1px solid {line};
  border-radius: 5px;
  box-shadow: none;
}}

#vomnibar input:focus {{
  border-color: {f.orange};
}}

#vomnibar input::selection {{
  background-color: {selection(f)};
  color: {f.text_hi};
}}

#vomnibar ul {{
  background: {paper};
}}

#vomnibar li {{
  border-bottom: 1px solid {edge};
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
  background-color: {paper};
  color: {f.text};
  border: 1px solid {edge};
  box-shadow: none;
}}

#hud-container #search-area,
#hud-container #hud {{
  background-color: {paper};
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


def css(f):
    return f"/* {HEADER} */\n/* {f.name} for Vimium: paste into Options › CSS for Vimium UI. */\n\n{rules(f)}"


def auto_css(light, dark):
    inner = "\n".join(f"  {line}" if line else "" for line in rules(dark).splitlines())
    return (
        f"/* {HEADER} */\n/* Subway Seat for Vimium, following the system: {light.name} when it's light, "
        f"{dark.name} when it's dark. */\n\n{rules(light)}\n@media (prefers-color-scheme: dark) {{\n{inner}\n}}\n"
    )


def build(flavors):
    by = {f.id: f for f in flavors}
    how = "paste into Vimium Options › CSS for Vimium UI"
    outs = [Out(f"{f.slug}.css", css(f), flavor=f.id, lang="css", how=how) for f in flavors]
    outs.append(Out("subway-seat-auto.css", auto_css(by["enamel"], by["walnut"]), lang="css", how=how))
    return outs
