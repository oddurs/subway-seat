"""micro: a true-color colorscheme per flavor."""

from ports._editors import ui
from ports._lib import HEADER, Out

META = {
    "id": "micro",
    "name": "micro",
    "category": "Editors",
    "homepage": "https://micro-editor.github.io",
    "enable": {
        "where": "~/.config/micro/settings.json",
        "code": '"colorscheme": "{slug}"',
        "lang": "json",
    },
    "notes": "Copy the `.micro` files to `~/.config/micro/colorschemes/` (on Windows, `%USERPROFILE%\\.config\\micro\\colorschemes`), "
    "then pick one with `set colorscheme <name>` from micro's command bar or in `settings.json`. "
    "True-color hex; micro maps it to 256 colors when the terminal can't show it.",
    "detect": ["micro"],
}


def links(f):
    u = ui(f)

    def c(fg=None, bg=None, *styles):
        spec = (fg or "") + (f",{bg}" if bg else "")
        return " ".join([*styles, spec])

    def S(role):
        color, styles = f.syntax(role)
        return c(color, None, *[s for s in ("bold", "italic") if s in styles])

    return {
        "default": c(f.text, f.base),
        "comment": S("comment"),
        "comment.bright": c(f.overlay2, None, "italic"),
        "identifier": S("function"),
        "identifier.class": S("function"),  # micro's syntax files also use it for functions
        "identifier.macro": S("decorator"),
        "identifier.var": S("variable"),
        "constant": S("constant"),
        "constant.bool": S("boolean"),
        "constant.number": S("number"),
        "constant.specialChar": S("string.escape"),
        "constant.string": S("string"),
        "constant.string.url": c(f.denim, None, "underline"),
        "statement": S("keyword"),
        "symbol": S("operator"),
        "symbol.brackets": S("punctuation"),
        "symbol.operator": S("operator"),
        "symbol.tag": S("tag"),
        "preproc": c(f.clay),
        "preproc.shebang": S("comment"),
        "type": S("type"),
        "type.keyword": S("storage"),
        "type.extended": S("type"),
        "special": c(f.clay),
        "underlined": c(f.denim, None, "underline"),
        "error": c(f.red_hi),
        "todo": c(u["ink"], f.yellow, "bold"),
        # interface
        "selection": c(f.text_hi, u["selection"]),
        "cursor-line": c(u["line"]),  # micro paints the fg as the line's background
        "color-column": c(f.surface0),  # likewise
        "line-number": c(u["line_nr"], f.base),
        "current-line-number": c(u["line_nr_cur"], u["line"], "bold"),
        "gutter-info": c(u["info"]),
        "gutter-warning": c(u["warning"]),
        "gutter-error": c(u["error"]),
        "diff-added": c(f.green),
        "diff-modified": c(f.yellow),
        "diff-deleted": c(f.red_hi),
        "statusline": c(f.subtext1, f.mantle),
        "statusline.inactive": c(f.overlay0, f.crust),
        "statusline.suggestions": c(f.subtext1, f.mantle),
        "tabbar": c(f.overlay1, f.crust),
        "tabbar.active": c(f.text_hi, f.base, "bold"),
        "indent-char": c(f.surface1),
        "divider": c(f.crust, f.crust),
        "scrollbar": c(f.surface2),
        "message": c(f.subtext1),
        "error-message": c(u["error"], None, "bold"),
        "match-brace": c(u["bracket_fg"], u["bracket_bg"], "bold"),
        "hlsearch": c(f.text, u["search"]),  # micro has no separate current-match group
        "tab-error": c(None, u["error_bg"]),
        "trailingws": c(None, u["error_bg"]),
        "ignore": c(f.overlay0),
    }


def render(f):
    lines = [f"# {HEADER}", f"# {f.name} — {f.blurb}", ""]
    lines += [f'color-link {name} "{spec}"' for name, spec in links(f).items()]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"colorschemes/{f.slug}.micro", render(f), flavor=f.id,
            dest=f"~/.config/micro/colorschemes/{f.slug}.micro", lang="conf")
        for f in flavors
    ]
