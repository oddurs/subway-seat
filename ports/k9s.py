from ports._cli import bar, row
from ports._lib import HEADER, Out, ink

META = {
    "id": "k9s",
    "name": "k9s",
    "category": "CLI & TUI",
    "homepage": "https://k9scli.io",
    "enable": {
        "where": "k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: "
        "~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set)",
        "code": "k9s:\n  ui:\n    skin: {slug}",
        "lang": "yaml",
    },
    "detect": ["k9s"],
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
                "cursorBgColor": row(f), "markColor": f.orange_hi,
                "header": {
                    "fgColor": f.subtext0, "bgColor": f.base, "sorterColor": f.orange,
                    "selectedSortColumnColor": f.orange,
                },
            },
            "xray": {
                "fgColor": f.text, "bgColor": f.base, "cursorColor": row(f),
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
        Out(f"{f.slug}.yaml", skin(f), flavor=f.id, dest=f"~/Library/Application Support/k9s/skins/{f.slug}.yaml",
            lang="yaml", how="on Linux the folder is ~/.config/k9s/skins")
        for f in flavors
    ]
