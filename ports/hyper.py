"""Hyper: a local plugin per flavor that decorates the config."""

import json

import palette as p
from ports._lib import HEADER, Out
from ports._terminals import ANSI_NAMES, lit, split

META = {
    "id": "hyper",
    "name": "Hyper",
    "category": "Terminals",
    "homepage": "https://hyper.is",
    "enable": {
        "where": "~/.hyper.js",
        "code": "localPlugins: ['{slug}'],",
        "lang": "typescript",
    },
    "notes": "Colours, cursor, selection, borders and the tab strip. Hyper 3 loads local plugins from "
    "`~/.hyper_plugins/local/`; the Hyper 4 canary uses `~/.config/Hyper/plugins/local/`.",
}

def plugin(f):
    colors = dict(zip(ANSI_NAMES, f.ansi[:8]))
    colors |= {"light" + n.title(): c for n, c in zip(ANSI_NAMES, f.ansi[8:])}
    # Hyper 3's xterm.js paints the selection over the text, so it must be translucent.
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
