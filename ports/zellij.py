from ports._cli import bar
from ports._lib import HEADER, Out, ink

META = {
    "id": "zellij",
    "name": "Zellij",
    "category": "CLI & TUI",
    "homepage": "https://zellij.dev",
    "enable": {
        "where": "~/.config/zellij/config.kdl",
        "code": 'theme "{slug}"',
        "lang": "kdl",
    },
    "auto": {
        "where": "~/.config/zellij/config.kdl (a recent Zellij, in a terminal that reports light and dark)",
        "code": 'theme_dark "subway-seat"\ntheme_light "subway-seat-enamel"',
        "lang": "kdl",
    },
    "requires": "Zellij 0.42+ (a legacy file covers older releases)",
    "detect": ["zellij"],
    "notes": "Themes in Zellij's component spec: an orange frame on the focused pane, gold in other "
    "modes, orange ribbons for the active tab with their key hints in dark ink. A legacy color-list "
    "version is included for Zellij before 0.42.",
}


def component(base, background, e0, e1, e2, e3):
    """One UI component; 0 means "unused / terminal default", as in Zellij's own themes."""
    rows = [("base", base), ("background", background), ("emphasis_0", e0),
            ("emphasis_1", e1), ("emphasis_2", e2), ("emphasis_3", e3)]
    return "\n".join(f"            {k} " + ("0" if v == 0 else f'"{v}"') for k, v in rows)


def spec(f):
    on, strip = ink(f), bar(f)
    accents = (f.orange, f.sage, f.green, f.yellow)
    comps = {
        "text_unselected": (f.text, strip, *accents),
        "text_selected": (f.text_hi, f.surface1, *accents),
        "ribbon_unselected": (f.text, f.surface1, f.yellow, f.text_hi, f.sage, f.orange),
        # every emphasis in ink: accents on the orange ribbon would vanish
        "ribbon_selected": (on, f.orange, on, on, on, on),
        "table_title": (f.orange, 0, f.yellow, f.sage, f.green, f.clay),
        "table_cell_selected": (f.text_hi, f.surface1, *accents),
        "table_cell_unselected": (f.text, strip, *accents),
        "list_selected": (f.text_hi, f.surface1, *accents),
        "list_unselected": (f.text, strip, *accents),
        "frame_unselected": (f.surface2, 0, f.orange, f.sage, f.green, f.yellow),
        "frame_selected": (f.orange, 0, f.yellow, f.sage, f.green, 0),
        "frame_highlight": (f.yellow, 0, f.orange, f.yellow, f.yellow, f.yellow),
        "exit_code_success": (f.green, 0, f.sage, on, f.yellow, f.denim),
        "exit_code_error": (f.red_hi, 0, f.yellow, 0, 0, 0),
    }
    body = "\n".join(f"        {name} {{\n{component(*vals)}\n        }}" for name, vals in comps.items())
    players = [f.orange, f.yellow, f.green, f.sage, f.denim, f.clay, f.red_hi, f.green_hi, f.yellow_hi, f.sage_hi]
    body += "\n        multiplayer_user_colors {\n" + "\n".join(
        f'            player_{i} "{c}"' for i, c in enumerate(players, 1)
    ) + "\n        }"
    return f"// {HEADER}\n// {f.name}: Zellij 0.42+ component theme.\n\nthemes {{\n    {f.slug} {{\n{body}\n    }}\n}}\n"


def legacy(f):
    # Legacy themes are read by slot: `green` paints the focused frame and the
    # active tab, `orange` the frame in other modes. Burnt orange is the active
    # color everywhere else in Subway Seat, so the slots are shifted to match.
    slots = [
        ("fg", f.text, ""), ("bg", f.surface1, ""), ("black", f.mantle, ""),
        ("red", f.red_hi, ""), ("green", f.orange, "active frame, selected tab"),
        ("yellow", f.yellow, ""), ("blue", f.denim, ""), ("magenta", f.clay, ""),
        ("orange", f.yellow, "frame in other modes"), ("cyan", f.sage, ""), ("white", f.text_hi, ""),
    ]
    body = "\n".join(f'        {k} "{v}"' + (f" // {note}" if note else "") for k, v, note in slots)
    return (f"// {HEADER}\n// {f.name}: legacy color-list theme for Zellij before 0.42.\n\n"
            f"themes {{\n    {f.slug} {{\n{body}\n    }}\n}}\n")


def build(flavors):
    outs = []
    for f in flavors:
        dest = f"~/.config/zellij/themes/{f.slug}.kdl"
        outs.append(Out(f"themes/{f.slug}.kdl", spec(f), flavor=f.id, dest=dest, lang="kdl"))
        outs.append(Out(f"legacy/{f.slug}.kdl", legacy(f), flavor=f.id, lang="kdl",
                        how=f"for Zellij before 0.42, use this file as {dest} instead"))
    return outs
