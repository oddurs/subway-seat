"""Gemini CLI: a custom theme per flavor, as a file and as a `ui.customThemes` block.

Gemini builds its highlight.js colours from a fixed map (createCustomTheme in
packages/cli/src/ui/themes/theme.ts), and the nested keys override the flat
ones they share a slot with. That forces two trade-offs:

- `status.warning` *is* AccentYellow, which also colours strings; `status.success`
  *is* AccentGreen, which also colours numbers. Warnings must still look like
  warnings, so strings are harvest gold and numbers avocado here, the reverse of
  the other ports.
- `text.link` would repaint AccentBlue, AccentCyan and LightBlue (keywords, types,
  attributes) in one colour, so it is left unset and links take AccentBlue, burnt
  orange.

The rest keeps the usual roles: keywords, literals and tag names burnt orange,
built-ins and types sage, JSON keys and attributes almond (strings took gold),
variables terracotta, comments cardboard.
"""

import json

from ports._lib import Out, tints

META = {
    "id": "gemini-cli",
    "name": "Gemini CLI",
    "category": "Agents",
    "homepage": "https://github.com/google-gemini/gemini-cli",
    "enable": {
        "where": "~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory)",
        "code": '{{\n  "ui": {{ "theme": "$HOME/.gemini/themes/{slug}.json" }}\n}}',
        "lang": "json",
    },
    "notes": "A custom theme file per flavor, plus the same theme as a `ui.customThemes` settings block. "
    "Gemini ties string colour to its warning colour, so strings are harvest gold here instead of avocado.",
}


def theme(f):
    t = tints(f)
    gradient = [f.red, f.orange, f.yellow, f.green]  # the 70s stripe
    border = f.surface2
    return {
        "name": f.name,
        "type": "custom",
        # flat keys: the highlight.js map reads these
        "Background": f.base,
        "Foreground": f.text,
        "LightBlue": f.subtext1,     # attr, attribute, builtin-name
        "AccentBlue": f.orange,      # keyword, literal, symbol, name, link; ui.active
        "AccentPurple": f.clay,      # variable, template-variable; text.accent
        "AccentCyan": f.sage,        # built_in, type
        "AccentGreen": f.green,      # number, class; status.success
        "AccentYellow": f.yellow,    # string, section, bullet, selectors; status.warning
        "AccentRed": f.red_hi,       # regexp, template-tag; status.error
        "DiffAdded": t["add"],
        "DiffRemoved": t["del"],
        "Comment": f.overlay1,
        "Gray": f.overlay2,
        "DarkGray": border,
        "GradientColors": gradient,
        # nested keys: the UI's semantic colours (kept equal to the flat keys they override)
        "text": {"primary": f.text, "secondary": f.overlay2, "accent": f.clay, "response": f.text},
        "background": {"primary": f.base, "diff": {"added": t["add"], "removed": t["del"]}},
        "border": {"default": border},
        "ui": {"comment": f.overlay1, "symbol": f.yellow, "active": f.orange, "focus": f.yellow,
               "gradient": gradient},
        "status": {"success": f.green, "warning": f.yellow, "error": f.red_hi},
    }


def build(flavors):
    outs = []
    for f in flavors:
        th = theme(f)
        outs.append(Out(f"{f.slug}.json", json.dumps(th, indent=2) + "\n", flavor=f.id,
                        dest=f"~/.gemini/themes/{f.slug}.json", lang="json"))
        settings = {"ui": {"customThemes": {f.name: th}, "theme": f.name}}
        outs.append(Out(f"settings/{f.slug}.json", json.dumps(settings, indent=2) + "\n", flavor=f.id,
                        dest="merged into ~/.gemini/settings.json", lang="json"))
    return outs
