"""Codex CLI: the bat TextMate theme, tuned for how Codex reads it.

Codex (codex-rs/tui/src/render/highlight.rs) takes only foreground and bold from
a theme, with one exception: diff line backgrounds come from the background of
`markup.inserted` / `markup.deleted` (falling back to `diff.inserted` /
`diff.deleted`), resolved for that bare scope. bat puts its tints on the more
specific `markup.inserted.diff`, which a bare lookup never reaches, so this adds
rules that give both scopes a foreground and a tinted background. syntect lets a
later rule of equal specificity win, so they go last.

The status line borrows syntax colours by scope (status_line_style.rs): model
sage, path avocado, branch gold, state and mode burnt orange, usage redbird,
thread gold.
"""

import plistlib

from ports._lib import HEADER, Out, tints
from ports.bat import tmtheme

META = {
    "id": "codex",
    "name": "Codex CLI",
    "category": "Agents",
    "homepage": "https://github.com/openai/codex",
    "enable": {
        "where": "~/.codex/config.toml, after copying the theme to ~/.codex/themes/ (or pick it with /theme)",
        "code": '[tui]\ntheme = "{slug}"',
        "lang": "toml",
    },
    "notes": "TextMate themes tuned for Codex, whose diff backgrounds come from the theme's added and removed "
    "scopes. The status line picks up the same warm syntax colours.",
}


def codex_tmtheme(f):
    t = tints(f)
    doc = plistlib.loads(tmtheme(f).encode())
    doc["settings"] += [
        {"scope": "markup.inserted, diff.inserted", "settings": {"foreground": f.green, "background": t["add"]}},
        {"scope": "markup.deleted, diff.deleted", "settings": {"foreground": f.red_hi, "background": t["del"]}},
    ]
    body = plistlib.dumps(doc).decode()
    return body.replace("?>\n", f"?>\n<!-- {HEADER} -->\n", 1)


def build(flavors):
    return [
        Out(f"{f.slug}.tmTheme", codex_tmtheme(f), flavor=f.id, dest=f"~/.codex/themes/{f.slug}.tmTheme", lang="xml")
        for f in flavors
    ]
