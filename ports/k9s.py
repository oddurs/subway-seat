from ports._cli import bar, ink
from ports._lib import HEADER, Out

META = {
    "id": "k9s",
    "name": "k9s",
    "category": "CLI & TUI",
    "homepage": "https://k9scli.io",
    "enable": {
        "where": "k9s config.yaml (`k9s info` shows where), with the skin in its skins/ folder",
        "code": "k9s:\n  ui:\n    skin: {slug}",
        "lang": "yaml",
    },
    "notes": "Gold breadcrumbs with the current view in orange, like a line of station signs, and "
    "resource states in avocado, gold, orange and red.",
}


def skin(f):
    on, strip = ink(f), bar(f)
    doc = {
        "body": {
            "fgColor": f.text, "bgColor": f.base, "logoColor": f.orange,
            "logoColorMsg": f.text, "logoColorInfo": f.green, "logoColorWarn": f.yellow,
            "logoColorError": f.red_hi,
        },
        "prompt": {
            "fgColor": f.text, "bgColor": strip, "suggestColor": f.overlay1,
            "border": {"default": f.sage, "command": f.orange},
        },
        "info": {
            "fgColor": f.orange, "sectionColor": f.text, "cpuColor": f.green,
            "memColor": f.yellow, "k9sRevColor": f.green_hi,
        },
        "help": {
            "fgColor": f.text, "bgColor": f.base, "sectionColor": f.green,
            "keyColor": f.yellow, "numKeyColor": f.red_hi,
        },
        "frame": {
            "title": {
                "fgColor": f.yellow, "bgColor": f.base, "highlightColor": f.orange,
                "counterColor": f.red_hi, "filterColor": f.green,
            },
            "border": {"fgColor": f.surface2, "focusColor": f.orange},
            "menu": {"fgColor": f.subtext1, "keyColor": f.yellow, "numKeyColor": f.red_hi},
            "crumbs": {"fgColor": on, "bgColor": f.yellow, "activeColor": f.orange},
            "status": {
                "newColor": f.sage, "modifyColor": f.yellow, "addColor": f.green,
                "pendingColor": f.orange, "errorColor": f.red_hi, "highlightColor": f.yellow_hi,
                "killColor": f.clay, "completedColor": f.overlay0,
            },
        },
        "views": {
            "table": {
                "fgColor": f.text, "bgColor": f.base, "cursorFgColor": f.text_hi,
                "cursorBgColor": f.surface1, "markColor": f.orange_hi,
                "header": {
                    "fgColor": f.subtext0, "bgColor": f.base, "sorterColor": f.orange,
                    "selectedSortColumnColor": f.orange,
                },
            },
            "xray": {
                "fgColor": f.text, "bgColor": f.base, "cursorColor": f.surface1,
                "cursorTextColor": f.text_hi, "graphicColor": f.sage,
            },
            "charts": {
                "bgColor": f.base, "chartBgColor": f.base, "dialBgColor": f.base,
                "defaultDialColors": [f.green, f.red_hi],
                "defaultChartColors": [f.green, f.red_hi],
                "resourceColors": {"cpu": [f.orange, f.yellow], "mem": [f.yellow, f.green]},
                "focusFgColor": on, "focusBgColor": f.orange,
            },
            "yaml": {"keyColor": f.yellow, "valueColor": f.text, "colonColor": f.overlay2},
            "logs": {
                "fgColor": f.text, "bgColor": f.base,
                "indicator": {
                    "fgColor": f.subtext0, "bgColor": f.base,
                    "toggleOnColor": f.green, "toggleOffColor": f.overlay0,
                },
            },
            "picker": {"mainColor": f.text, "focusColor": f.orange, "shortcutColor": f.yellow},
        },
        "dialog": {
            "fgColor": f.text, "bgColor": f.surface0, "buttonFgColor": f.text,
            "buttonBgColor": f.surface2, "buttonFocusFgColor": on, "buttonFocusBgColor": f.orange,
            "labelFgColor": f.yellow, "fieldFgColor": f.text,
        },
    }

    def emit(d, indent):
        lines = []
        for k, v in d.items():
            pad = " " * indent
            if isinstance(v, dict):
                lines += [f"{pad}{k}:", *emit(v, indent + 2)]
            elif isinstance(v, list):
                lines += [f"{pad}{k}:", *(f"{pad}  - '{c}'" for c in v)]
            else:
                lines.append(f"{pad}{k}: '{v}'")
        return lines

    return f"# {HEADER}\n# {f.name} skin for k9s.\nk9s:\n" + "\n".join(emit(doc, 2)) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.yaml", skin(f), flavor=f.id, dest=f"~/.config/k9s/skins/{f.slug}.yaml", lang="yaml")
        for f in flavors
    ]
