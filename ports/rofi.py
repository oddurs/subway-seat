"""rofi: a theme per flavor on rofi's own default layout.

The theme imports rofi's built-in default and sets its color variables, so the
layout stays rofi's and only the colors change: the window on paper with a quiet
edge, the selected row a wash of text, matches in gold, active entries in denim and
urgent ones in orange. Every palette role is defined too, for your own tweaks.
"""

import palette as p
from ports._desktop import readable, roles
from ports._lib import HEADER, Out

META = {
    "id": "rofi",
    "name": "rofi",
    "category": "Desktop",
    "homepage": "https://github.com/davatorium/rofi",
    "requires": "rofi 1.7+",
    "detect": ["rofi"],
    "enable": {
        "where": "~/.config/rofi/config.rasi, at the end (or pick it in `rofi-theme-selector`)",
        "code": '@theme "{slug}"',
        "lang": "css",
        "file": "~/.config/rofi/config.rasi",
    },
    "notes": "Colors on rofi's default layout: the window on the raised paper ground, a text-wash "
    "selection, gold matches, denim for active entries and orange for urgent ones. The palette's roles "
    "are defined as variables (`@text-hi`, `@orange`) for anything you add after `@theme`.",
}


def kebab(role):
    return role.replace("_", "-")


def theme(f):
    r = roles(f)
    sel = r["selection"]
    on_sel = {
        "active": readable(f, "denim_hi" if f.dark else "denim", sel),
        "urgent": readable(f, "orange_hi" if f.dark else "orange", sel),
    }
    width = max(len(kebab(role)) for role in p.ROLES) + 1
    lines = [f"/* {HEADER} */", f"/* {f.name} for rofi */", "", '@import "default"', "", "* {"]
    lines += [f"    {kebab(role) + ':':<{width}} {f.colors[role]};" for role in p.ROLES]
    lines += [
        "",
        f"    {'paper:':<{width}} {r['paper']};",
        f"    {'edge:':<{width}} {r['edge']};",
        f"    {'hover:':<{width}} {r['hover']};",
        f"    {'selection:':<{width}} {sel};",
        "",
        "    /* the default theme's variables */",
    ]
    variables = {
        "background": "@paper",
        "foreground": "@text",
        "lightbg": "@hover",
        "lightfg": "@subtext1",
        "red": "@red",
        "blue": "@denim",
        "border-color": "@edge",
        "separatorcolor": "@edge",
        "normal-background": "@paper",
        "normal-foreground": "@text",
        "alternate-normal-background": "@paper",
        "alternate-normal-foreground": "@text",
        "active-background": "@paper",
        "active-foreground": "@denim",
        "alternate-active-background": "@paper",
        "alternate-active-foreground": "@denim",
        "urgent-background": "@paper",
        "urgent-foreground": "@orange",
        "alternate-urgent-background": "@paper",
        "alternate-urgent-foreground": "@orange",
        "selected-normal-background": "@selection",
        "selected-normal-foreground": "@text-hi",
        "selected-active-background": "@selection",
        "selected-active-foreground": on_sel["active"],
        "selected-urgent-background": "@selection",
        "selected-urgent-foreground": on_sel["urgent"],
    }
    vw = max(len(k) for k in variables) + 1
    lines += [f"    {k + ':':<{vw}} {v};" for k, v in variables.items()]
    lines += [
        "}",
        "",
        "element-text {",
        f"    highlight: bold {r['match']};",
        "}",
        "",
        "entry {",
        f"    placeholder-color: {r['faint']};",
        "}",
        "",
        "prompt {",
        "    text-color: @subtext1;",
        "}",
        "",
        "num-filtered-rows, num-rows, textbox-num-sep {",
        f"    text-color: {r['faint']};",
        "}",
        "",
        "scrollbar {",
        f"    handle-color: {r['faint']};",
        "}",
        "",
    ]
    return "\n".join(lines)


def build(flavors):
    return [
        Out(f"{f.slug}.rasi", theme(f), flavor=f.id, dest=f"~/.local/share/rofi/themes/{f.slug}.rasi", lang="css")
        for f in flavors
    ]
