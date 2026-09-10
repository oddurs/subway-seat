"""Midnight Commander: a true-color skin per flavor."""

from ports._lib import HEADER, Out, ink, selection, tints, ui_colors

META = {
    "id": "midnight-commander",
    "name": "Midnight Commander",
    "category": "CLI & TUI",
    "homepage": "https://midnight-commander.org",
    "detect": ["mc"],
    "requires": "mc 4.8.19+ built with S-Lang",
    "enable": {
        "where": "the [Midnight-Commander] section of ~/.config/mc/ini, or Options › Appearance "
        "(then Options › Save setup)",
        "code": "skin={slug}",
        "lang": "ini",
    },
    "notes": "Panels on walnut with gold directories and marked files, menus and the button bar on the "
    "darker chrome, dialogs raised a step, and the diff viewer on the same tinted grounds as every other "
    "port. True-color skins need a terminal that sets COLORTERM=truecolor; without it mc falls back to "
    "its default skin and says why. To try one without saving it, run `mc -S subway-seat`. mcedit's "
    "syntax colors come from your terminal's palette.",
}

LINES = {
    "horiz": "─", "vert": "│", "lefttop": "┌", "righttop": "┐", "leftbottom": "└", "rightbottom": "┘",
    "topmiddle": "┬", "bottommiddle": "┴", "leftmiddle": "├", "rightmiddle": "┤", "cross": "┼",
    "dhoriz": "─", "dvert": "│", "dlefttop": "┌", "drighttop": "┐", "dleftbottom": "└", "drightbottom": "┘",
    "dtopmiddle": "┬", "dbottommiddle": "┴", "dleftmiddle": "├", "drightmiddle": "┤",
}  # fmt: skip

WIDGETS = {
    "widget-panel": {
        "sort-up-char": "▴", "sort-down-char": "▾",
        "hiddenfiles-show-char": "•", "hiddenfiles-hide-char": "○",
        "history-prev-item-char": "◂", "history-next-item-char": "▸", "history-show-list-char": "▾",
        "filename-scroll-left-char": "◂", "filename-scroll-right-char": "▸",
    },
    "widget-scrollbar": {
        "first-vert-char": "▴", "last-vert-char": "▾", "first-horiz-char": "◂", "last-horiz-char": "▸",
        "current-char": "■", "background-char": "░",
    },
    "widget-editor": {"window-state-char": "↕", "window-close-char": "✕"},
}  # fmt: skip


def skin(f):
    c = ui_colors(f)
    t = tints(f)
    # Aliases name the roles once; the sections below refer to them.
    aliases = {
        "Ground": f.base, "Chrome": f.mantle, "Groove": f.crust, "Paper": c["paper"], "Raised": f.surface1,
        "Select": selection(f), "Ink": ink(f), "Text": f.text, "Bright": f.text_hi, "Quiet": f.subtext1,
        "Muted": f.subtext0, "Faint": f.overlay1, "Fainter": f.overlay0, "Label": f.overlay2,
        "Gold": f.yellow, "Orange": f.orange, "Red": f.red, "RedBright": f.red_hi, "Green": f.green,
        "Sage": f.sage, "Denim": f.denim, "Clay": f.clay, "OrangeBright": f.orange_hi,
        "Search": t["search"], "SearchCurrent": t["search_cur"],
        "DiffAdd": t["add"], "DiffDelete": t["del"], "DiffChange": t["chg"], "DiffChangeWord": t["chg_emph"],
    }  # fmt: skip
    sections = {
        "core": {
            "_default_": "Text;Ground",
            "selected": "Bright;Select",
            "marked": "Gold;;bold",
            "markselect": "Gold;Select;bold",
            "gauge": ";Orange",
            "input": "Text;Ground",
            "inputunchanged": "Muted;Ground",
            "inputmark": "Bright;Select",
            "disabled": "Faint;Paper",
            "reverse": "Bright;Raised",
            "commandlinemark": "Bright;Select",
            "header": "Orange;;bold",
            "inputhistory": "Label;Paper",
            "commandhistory": "Label;Ground",
            "shadow": "Fainter;Groove",
        },
        "dialog": {
            "_default_": "Text;Paper",
            "dfocus": "Bright;Select",
            "dhotnormal": "Orange;;underline",
            "dhotfocus": "Orange;Select;underline",
            "dtitle": "Gold;;bold",
        },
        "error": {
            "_default_": "Ink;Red",
            "errdfocus": "Red;Ink",
            "errdhotnormal": ";;underline",
            "errdhotfocus": "Red;Ink;underline",
            "errdtitle": ";;bold",
        },
        "filehighlight": {
            "directory": "Gold;;bold",
            "executable": "Green;;bold",
            "symlink": "Sage;",
            "hardlink": "",
            "stalelink": "RedBright;",
            "device": "OrangeBright;",
            "special": "Clay;",
            "core": "Red;",
            "temp": "Fainter;",
            "archive": "RedBright;",
            "doc": "Denim;",
            "source": "Sage;",
            "media": "Orange;",
            "graph": "Clay;",
            "database": "OrangeBright;",
        },
        "menu": {
            "_default_": "Quiet;Chrome",
            "menusel": "Bright;Select",
            "menuhot": "Orange;",
            "menuhotsel": "Orange;Select",
            "menuinactive": "Label;Chrome",
        },
        "popupmenu": {"_default_": "Text;Paper", "menusel": "Bright;Select", "menutitle": "Gold;;bold"},
        "buttonbar": {"hotkey": "Orange;Chrome;bold", "button": "Quiet;Chrome"},
        "statusbar": {"_default_": "Quiet;Chrome"},
        "help": {
            "_default_": "Text;Paper",
            "helpitalic": "Green;;italic",
            "helpbold": "Gold;;bold",
            "helplink": "Denim;;underline",
            "helpslink": "Ink;Denim",
            "helptitle": "Orange;;bold",
        },
        "editor": {
            "_default_": "Text;Ground",
            "editbold": "Bright;Search;bold",
            "editmarked": "Bright;Select",
            "editwhitespace": "Fainter;Ground",
            "editnonprintable": "Clay;Groove",
            "editlinestate": "Fainter;Ground",
            "bookmark": "Bright;Raised",
            "bookmarkfound": "Bright;SearchCurrent",
            "editrightmargin": "Fainter;Chrome",
            "editbg": ";Chrome",
            "editframe": "Faint;",
            "editframeactive": "Gold;",
            "editframedrag": "Orange;",
        },
        "viewer": {
            "_default_": "Text;Ground",
            "viewbold": "Bright;;bold",
            "viewunderline": "Sage;;underline",
            "viewselected": "Bright;SearchCurrent",
        },
        # mc paints a line that exists on one side only with "added" (on either side) and the blank
        # opposite it with "removed"; a changed line is "changedline", its changed characters "changednew".
        "diffviewer": {
            "added": "Text;DiffAdd",
            "changedline": "Text;DiffChange",
            "changednew": "Bright;DiffChangeWord",
            "changed": ";DiffChange",
            "removed": ";DiffDelete",
            "error": "Ink;Red",
        },
    }

    width = max(len(k) for k in aliases)
    out = [
        f"# {HEADER}",
        f"# {f.name} for Midnight Commander. Needs mc 4.8.19+ built with S-Lang and a true-color",
        "# terminal (COLORTERM=truecolor).",
        "",
        "[skin]",
        f"    description = {f.name}",
        "    truecolors = true",
        "",
        "[Lines]",
        *(f"    {k} = {v}" for k, v in LINES.items()),
        "",
        "[aliases]",
        *(f"    {k:<{width}} = {v}" for k, v in aliases.items()),
    ]
    for name, keys in {**sections, **WIDGETS}.items():
        out += ["", f"[{name}]", *(f"    {k} = {v}".rstrip() for k, v in keys.items())]
    return "\n".join(out) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.ini", skin(f), flavor=f.id, dest=f"~/.local/share/mc/skins/{f.slug}.ini", lang="ini")
        for f in flavors
    ]
