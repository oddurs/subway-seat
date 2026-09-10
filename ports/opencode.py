"""opencode: JSON themes with dark and light halves; opencode picks the half that
matches the terminal's background (or the mode you pin).

Keys follow packages/tui/src/theme/index.ts. Agents cycle through secondary,
accent, success, warning, primary…, so the build agent rides in harvest gold and
plan in seafoam, as in Claude Code; shell mode lights the prompt burnt orange.
"""

import json

import palette as p
from ports._lib import Out, tints, ui_colors

META = {
    "id": "opencode",
    "name": "opencode",
    "category": "Agents",
    "homepage": "https://opencode.ai",
    "enable": {
        "where": "~/.config/opencode/tui.json after copying the theme to ~/.config/opencode/themes/, or pick it with /theme",
        "code": '{{\n  "$schema": "https://opencode.ai/tui.json",\n  "theme": "{slug}"\n}}',
        "lang": "json",
    },
    "auto": {
        "where": "~/.config/opencode/tui.json: Walnut and Tunnel carry Enamel as their light half",
        "code": '{\n  "$schema": "https://opencode.ai/tui.json",\n  "theme": "subway-seat"\n}',
        "lang": "json",
    },
    "detect": ["opencode", "~/.config/opencode"],
    "notes": "Walnut and Tunnel each pair with Enamel, and opencode switches halves with your terminal's "
    "background. `subway-seat-enamel` stays light whatever the terminal says.",
}

SCHEMA = "https://opencode.ai/theme.json"


def syn(role):
    return p.SYNTAX[role][0]


def spec(f):
    """opencode key → palette role name, or a computed hex."""
    dark = f.dark
    t = tints(f)
    return {
        "primary": "orange",
        "secondary": "yellow",
        "accent": "sage",
        "error": "red_hi",
        "warning": "yellow",
        "success": "green",
        "info": "denim",
        "text": "text",
        "textMuted": "overlay2",
        "selectedListItemText": "crust" if dark else "base",  # ink on the orange selection bar
        "background": "base",
        "backgroundPanel": "surface0" if dark else "mantle",   # user messages, tool blocks, dialogs
        "backgroundElement": "surface1" if dark else "crust",  # the prompt box, hovers
        "backgroundMenu": ui_colors(f)["paper"],                # autocomplete and dialog menus, raised
        "border": "surface2",
        "borderActive": "overlay0",
        "borderSubtle": "surface1",
        "diffAdded": "green",
        "diffRemoved": "red_hi",
        "diffContext": "overlay1",
        "diffHunkHeader": "denim",
        "diffHighlightAdded": "green_hi" if dark else "green",
        "diffHighlightRemoved": "red_hi" if dark else "red",
        "diffAddedBg": t["add"],
        "diffRemovedBg": t["del"],
        "diffContextBg": "base",
        "diffLineNumber": "overlay0",
        "diffAddedLineNumberBg": f.mix("green", "base", 0.1),
        "diffRemovedLineNumberBg": f.mix("red", "base", 0.11),
        "markdownText": "text",
        "markdownHeading": syn("heading"),
        "markdownLink": syn("link"),
        "markdownLinkText": "denim_hi",
        "markdownCode": syn("code"),
        "markdownBlockQuote": syn("quote"),
        "markdownEmph": syn("emphasis"),
        "markdownStrong": syn("strong"),
        "markdownHorizontalRule": "overlay0",
        "markdownListItem": "orange",
        "markdownListEnumeration": "orange",
        "markdownImage": syn("link"),
        "markdownImageText": "denim_hi",
        "markdownCodeBlock": "text",
        "syntaxComment": syn("comment"),
        "syntaxKeyword": syn("keyword"),
        "syntaxFunction": syn("function"),
        "syntaxVariable": syn("variable"),
        "syntaxString": syn("string"),
        "syntaxNumber": syn("number"),
        "syntaxType": syn("type"),
        "syntaxOperator": syn("operator"),
        "syntaxPunctuation": syn("punctuation"),
    }


def def_name(f, role):
    return f.id + "".join(w.title() for w in role.split("_"))


def ref(f, value):
    return value if value.startswith("#") else def_name(f, value)


def theme(dark, light):
    """A theme file; `dark` and `light` may be the same flavor (a pinned theme)."""
    flavors = [dark] if dark is light else [dark, light]
    defs = {def_name(f, r): f.colors[r] for f in flavors for r in p.ROLES}
    ds, ls = spec(dark), spec(light)
    body = {
        key: ref(dark, ds[key]) if dark is light else {"dark": ref(dark, ds[key]), "light": ref(light, ls[key])}
        for key in ds
    }
    return {"$schema": SCHEMA, "defs": defs, "theme": body}


def build(flavors):
    by = {f.id: f for f in flavors}
    walnut, tunnel, enamel = by["walnut"], by["tunnel"], by["enamel"]

    def out(name, doc, flavor=None):
        return Out(f"{name}.json", json.dumps(doc, indent=2) + "\n", flavor=flavor,
                   dest=f"~/.config/opencode/themes/{name}.json", lang="json")

    return [
        out(walnut.slug, theme(walnut, enamel), flavor=walnut.id),
        out(tunnel.slug, theme(tunnel, enamel), flavor=tunnel.id),
        out(enamel.slug, theme(enamel, enamel), flavor=enamel.id),
    ]
