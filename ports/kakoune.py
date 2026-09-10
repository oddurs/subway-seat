"""Kakoune: a colorscheme per flavor — builtin, code, markup and kakoune-lsp faces."""

import palette as p
from ports._editors import ui
from ports._lib import HEADER, Out, h

META = {
    "id": "kakoune",
    "name": "Kakoune",
    "category": "Editors",
    "homepage": "https://kakoune.org",
    "enable": {
        "where": "~/.config/kak/kakrc",
        "code": "colorscheme {slug}",
        "lang": "conf",
        "file": "~/.config/kak/kakrc",  # the last colorscheme line wins, so appending is enough
    },
    "notes": "Copy the `.kak` files to `~/.config/kak/colors/`. Covers the builtin, code and markup faces, "
    "plus kakoune-lsp's diagnostics, inlay hints and references.",
    "detect": ["kak"],
}


def faces(f):
    u = ui(f)

    def k(c):  # role or hex → rgb:RRGGBB
        return "rgb:" + h(f.colors.get(c, c))

    def face(fg="default", bg=None, attrs="", ul=None):
        v = k(fg) if fg != "default" else "default"
        if bg or ul:
            v += "," + (k(bg) if bg else "default")
        if ul:
            v += "," + k(ul)
        return v + (f"+{attrs}" if attrs else "")

    def S(role):
        color_role, styles = p.SYNTAX[role]
        return face(color_role, attrs="".join(a[0] for a in ("bold", "italic") if a in styles))

    select_cur = f.orange if f.dark else f.yellow  # the two warm lights swap
    return {
        # code
        "value": S("constant"),
        "type": S("type"),
        "variable": S("variable"),
        "module": S("namespace"),
        "function": S("function"),
        "string": S("string"),
        "keyword": S("keyword"),
        "operator": S("operator"),
        "attribute": S("decorator"),
        "comment": S("comment"),
        "documentation": "comment",
        "meta": face("clay"),
        "builtin": S("function.builtin"),
        # markup
        "title": face("orange", attrs="b"),
        "header": face("yellow", attrs="b"),
        "mono": S("code"),
        "block": S("code"),
        "link": face("denim", attrs="u"),
        "bullet": face("orange"),
        "list": face("orange"),
        # builtin faces
        "Default": face("text", "base"),
        "PrimarySelection": face("default", u["selection"]),
        "SecondarySelection": face("default", u["selection_inactive"]),
        "PrimaryCursor": face("base", u["cursor"], "fg"),
        "SecondaryCursor": face("base", f.mix(u["cursor"], "base", 0.55), "fg"),
        "PrimaryCursorEol": face("base", select_cur, "fg"),
        "SecondaryCursorEol": face("base", f.mix(select_cur, "base", 0.55), "fg"),
        "LineNumbers": face("overlay0", "base"),
        "LineNumberCursor": face(u["line_nr_cur"], "base", "b"),
        "LineNumbersWrapped": face("surface2", "base"),
        "MenuForeground": face("text_hi", u["row"], "b"),
        "MenuBackground": face("subtext1", u["paper"]),
        "MenuInfo": face("overlay1"),
        "Information": face("text", u["paper"]),
        "InlineInformation": face("text", u["paper"]),
        "Error": face("red_hi", attrs="b"),
        "DiagnosticError": face(ul="red_hi", attrs="c"),
        "DiagnosticWarning": face(ul="yellow", attrs="c"),
        "DiagnosticInfo": face(ul="denim", attrs="c"),
        "DiagnosticHint": face(ul="sage", attrs="c"),
        "DiagnosticTagDeprecated": "+s",
        "DiagnosticTagUnnecessary": face("overlay1"),
        "StatusLine": face("subtext1", "mantle"),
        "StatusLineMode": face(u["ink"], "orange", "b"),
        "StatusLineInfo": face("sage", "mantle"),
        "StatusLineValue": face("yellow", "mantle"),
        "StatusCursor": face("base", u["cursor"]),
        "Prompt": face("orange", "mantle", "b"),
        "MatchingChar": face(u["bracket_fg"], u["bracket_bg"], "b"),
        "Whitespace": face("surface1", attrs="f"),
        "WhitespaceIndent": "Whitespace",
        "WrapMarker": "Whitespace",
        "BufferPadding": face("surface1", "base"),
        # kakoune-lsp
        "InlayDiagnosticError": face("red_hi", u["error_bg"]),
        "InlayDiagnosticWarning": face("yellow", u["warning_bg"]),
        "InlayDiagnosticInfo": face("denim", u["info_bg"]),
        "InlayDiagnosticHint": face("sage", u["hint_bg"]),
        "LineFlagError": face("red_hi"),
        "LineFlagWarning": face("yellow"),
        "LineFlagInfo": face("denim"),
        "LineFlagHint": face("sage"),
        "Reference": face("default", u["bracket_bg"]),
        "ReferenceBind": face("default", u["bracket_bg"], "u"),
        "InlayHint": face("overlay1", u["inlay_bg"], "i"),
        "InlayCodeLens": face("overlay1", attrs="i"),
        "SnippetsNextPlaceholders": face("text", "surface1", "F"),
        "SnippetsOtherPlaceholders": face("subtext1", "surface0", "F"),
    }


def render(f):
    fs = faces(f)
    width = max(map(len, fs))
    lines = [f"# {HEADER}", f"# {f.name} — {f.blurb}", ""]
    lines += [f"face global {name:<{width}} {val}" for name, val in fs.items()]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"colors/{f.slug}.kak", render(f), flavor=f.id,
            dest=f"~/.config/kak/colors/{f.slug}.kak", lang="conf")
        for f in flavors
    ]
