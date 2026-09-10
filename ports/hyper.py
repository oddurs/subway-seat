"""Hyper: a local plugin per flavor that decorates the config."""

import json

import palette as p
from ports._lib import ANSI_NAMES, HEADER, Out
from ports._terminals import lit, split

META = {
    "id": "hyper",
    "name": "Hyper",
    "category": "Terminals",
    "homepage": "https://hyper.is",
    "detect": ["hyper", "/Applications/Hyper.app"],
    "enable": {
        "where": "~/.hyper.js",
        "code": "localPlugins: ['{slug}'],",
        "lang": "typescript",
    },
    "notes": "Colors, cursor, selection, borders and the tab strip. Hyper 3 loads local plugins from "
    "`~/.hyper_plugins/local/` (`$XDG_CONFIG_HOME/hyper/.hyper_plugins/local/` when that's set, "
    "`%APPDATA%\\Hyper\\.hyper_plugins\\local\\` on Windows). The Hyper 4 canary reads `hyper.json` and "
    "`~/.config/Hyper/plugins/local/`. Hyper doesn't follow the system light/dark setting, so pick one flavor.",
}


def plugin(f):
    colors = dict(zip(ANSI_NAMES, f.ansi[:8], strict=True))
    colors |= {"light" + n.title(): c for n, c in zip(ANSI_NAMES, f.ansi[8:], strict=True)}
    theme = {
        "backgroundColor": f.base,
        "foregroundColor": f.text,
        "cursorColor": lit(f),
        "cursorAccentColor": f.base,
        "selectionColor": p.alpha(f.text, 0.2),
        "borderColor": split(f),
        "colors": colors,
    }
    css = f"""
  .tabs_nav, .tabs_list {{ background-color: {f.crust}; }}
  .tabs_title {{ color: {f.subtext0}; }}
  .tab_tab {{ color: {f.overlay1}; background-color: {f.crust}; }}
  .tab_tab.tab_active {{ color: {f.text_hi}; background-color: {f.base}; box-shadow: inset 0 -2px 0 {lit(f)}; }}
"""
    return f"""// {HEADER}
// {f.name}. Enable with localPlugins: ["{f.slug}"] in ~/.hyper.js.
// selectionColor is a translucent wash of the text color, not the solid selection color the other
// terminals use: Hyper's xterm.js draws the selection over the glyphs, so an opaque color would hide them.
"use strict";

const theme = {json.dumps(theme, indent=2)};

const css = `{css}`;

exports.decorateConfig = (config) =>
  Object.assign({{}}, config, theme, {{ css: `${{css}}${{config.css || ""}}` }});
"""


def build(flavors):
    return [
        Out(
            f"{f.slug}/index.js",
            plugin(f),
            flavor=f.id,
            dest=f"~/.hyper_plugins/local/{f.slug}/index.js",
            lang="typescript",
        )
        for f in flavors
    ]
