"""Helix: a standalone TOML theme per flavor, with a named palette."""

import palette as p
from ports._editors import ui
from ports._lib import HEADER, Out, tints

META = {
    "id": "helix",
    "name": "Helix",
    "category": "Editors",
    "homepage": "https://helix-editor.com",
    "enable": {
        "where": "~/.config/helix/config.toml",
        "code": 'theme = "{snake}"',
        "lang": "toml",
    },
    "notes": "Copy the themes to `~/.config/helix/themes/`. To follow the terminal's light or dark mode, use "
    '`[theme]` with `dark = "subway_seat"` and `light = "subway_seat_enamel"`.',
}


def theme(f):
    u = ui(f)
    t = tints(f)
    # Palette: every role, plus the few computed grounds the theme needs.
    pal = dict(f.colors)
    extra = {
        "cursor": u["cursor"],
        "cursor_select": f.orange if f.dark else f.yellow,  # the two warm lights swap
        "cursor_secondary": f.mix(u["cursor"], "base", 0.55),
        "cursor_secondary_insert": f.mix("green", "base", 0.55),
        "cursor_secondary_select": f.mix(f.orange if f.dark else f.yellow, "base", 0.55),
        "cursorline": u["line"],
        "cursorline_secondary": f.mix(u["line"], "base", 0.5),
        "selection": u["selection"],
        "selection_secondary": f.mix(u["selection"], "base", 0.6),
        "inlay_bg": f.mix("surface0", "base", 0.6),
        "ink": u["ink"],
        "error_bg": f.mix("red", "base", 0.12),
        "warning_bg": f.mix("yellow", "base", 0.1),
        "info_bg": f.mix("denim", "base", 0.1),
        "hint_bg": f.mix("sage", "base", 0.1),
        "frameline": t["chg"],
    }
    pal.update(extra)
    name = {v: k for k, v in reversed(list(pal.items()))}  # hex → first palette name

    def st(fg=None, bg=None, mods=(), ul=None, ul_style="line"):
        d = {}
        if fg:
            d["fg"] = fg if fg in pal else name[fg]
        if bg:
            d["bg"] = bg if bg in pal else name[bg]
        if ul:
            d["underline"] = {"color": ul if ul in pal else name[ul], "style": ul_style}
        if mods:
            d["modifiers"] = list(mods)
        return d

    MODS = {"bold": "bold", "italic": "italic", "strikethrough": "crossed_out"}

    def S(role):
        colour_role, styles = p.SYNTAX[role]
        return st(colour_role, mods=[MODS[x] for x in ("bold", "italic") if x in styles])

    s = {
        # ── syntax ─────────────────────────────────────────────────────────
        "attribute": S("decorator"),
        "type": S("type"),
        "type.builtin": S("type.builtin"),
        "type.parameter": st("sage", mods=["italic"]),
        "type.enum.variant": S("constant"),
        "constructor": S("type"),
        "constant": S("constant"),
        "constant.builtin": S("constant"),
        "constant.builtin.boolean": S("boolean"),
        "constant.character": S("string"),
        "constant.character.escape": S("string.escape"),
        "constant.numeric": S("number"),
        "string": S("string"),
        "string.regexp": S("regexp"),
        "string.special": st("clay"),
        "string.special.path": st("green"),
        "string.special.url": st("denim", ul="denim"),
        "string.special.symbol": st("clay"),
        "comment": S("comment"),
        "comment.line.documentation": S("comment"),
        "comment.block.documentation": S("comment"),
        "comment.unused": st("overlay1"),
        "variable": S("variable"),
        "variable.builtin": S("variable.builtin"),
        "variable.parameter": S("parameter"),
        "variable.other.member": S("property"),
        "variable.other.member.private": S("property"),
        "label": S("decorator"),
        "punctuation": S("punctuation"),
        "punctuation.delimiter": S("punctuation"),
        "punctuation.bracket": S("punctuation"),
        "punctuation.special": st("clay"),
        "keyword": S("keyword"),
        "keyword.control": S("keyword"),
        "keyword.control.conditional": S("keyword"),
        "keyword.control.repeat": S("keyword"),
        "keyword.control.import": S("keyword"),
        "keyword.control.return": S("keyword"),
        "keyword.control.exception": S("keyword"),
        "keyword.operator": S("keyword"),
        "keyword.directive": st("clay"),
        "keyword.function": S("keyword"),
        "keyword.storage": S("storage"),
        "keyword.storage.type": S("storage"),
        "keyword.storage.modifier": S("storage"),
        "operator": S("operator"),
        "function": S("function"),
        "function.builtin": S("function.builtin"),
        "function.method": S("function"),
        "function.macro": st("clay"),
        "function.special": st("clay"),
        "tag": S("tag"),
        "tag.builtin": S("tag"),
        "namespace": S("namespace"),
        "special": st("yellow", mods=["bold"]),  # fuzzy-match letters in pickers
        "embedded": S("variable"),
        # markup
        "markup.heading": S("heading"),
        "markup.heading.marker": st("overlay2", mods=["bold"]),
        "markup.heading.1": st("orange", mods=["bold"]),
        "markup.heading.2": st("yellow", mods=["bold"]),
        "markup.heading.3": st("green", mods=["bold"]),
        "markup.heading.4": st("sage", mods=["bold"]),
        "markup.heading.5": st("clay", mods=["bold"]),
        "markup.heading.6": st("subtext1", mods=["bold"]),
        "markup.list": st("orange"),
        "markup.list.unnumbered": st("orange"),
        "markup.list.numbered": st("orange"),
        "markup.list.checked": st("green"),
        "markup.list.unchecked": st("overlay1"),
        "markup.bold": S("strong"),
        "markup.italic": S("emphasis"),
        "markup.strikethrough": st(mods=["crossed_out"]),
        "markup.link": S("link"),
        "markup.link.url": st("denim", ul="denim"),
        "markup.link.label": st("sage"),
        "markup.link.text": st("sage"),
        "markup.quote": S("quote"),
        "markup.raw": S("code"),
        "markup.raw.inline": S("code"),
        "markup.raw.block": S("code"),
        "markup.normal.completion": st("text"),
        "markup.normal.hover": st("text"),
        "markup.heading.completion": st("yellow", mods=["bold"]),
        "markup.heading.hover": st("yellow", mods=["bold"]),
        "markup.raw.inline.completion": st("green"),
        "markup.raw.inline.hover": st("green"),
        # diff
        "diff.plus": st("green"),
        "diff.plus.gutter": st("green"),
        "diff.minus": st("red_hi"),
        "diff.minus.gutter": st("red_hi"),
        "diff.delta": st("yellow"),
        "diff.delta.gutter": st("yellow"),
        "diff.delta.moved": st("sage"),
        "diff.delta.conflict": st("orange"),
        # ── interface ──────────────────────────────────────────────────────
        "ui.background": st("text", "base"),
        "ui.background.separator": st("surface1"),
        "ui.text": st("text"),
        "ui.text.focus": st("text_hi", "surface1", ["bold"]),
        "ui.text.inactive": st("overlay1"),
        "ui.text.info": st("subtext1"),
        "ui.text.directory": st("yellow"),
        "ui.text.symlink": st("sage"),
        "ui.cursor": st("base", "cursor_secondary"),
        "ui.cursor.normal": st("base", "cursor_secondary"),
        "ui.cursor.insert": st("base", "cursor_secondary_insert"),
        "ui.cursor.select": st("base", "cursor_secondary_select"),
        "ui.cursor.match": st("yellow_hi", "surface1", ["bold"]),
        "ui.cursor.primary": st("base", "cursor"),
        "ui.cursor.primary.normal": st("base", "cursor"),
        "ui.cursor.primary.insert": st("base", "green"),
        "ui.cursor.primary.select": st("base", "cursor_select"),
        "ui.cursorline.primary": st(bg="cursorline"),
        "ui.cursorline.secondary": st(bg="cursorline_secondary"),
        "ui.cursorcolumn.primary": st(bg="cursorline"),
        "ui.cursorcolumn.secondary": st(bg="cursorline_secondary"),
        "ui.selection": st(bg="selection_secondary"),
        "ui.selection.primary": st(bg="selection"),
        "ui.highlight": st(bg="surface1"),
        "ui.highlight.frameline": st(bg="frameline"),
        "ui.gutter": st(bg="base"),
        "ui.linenr": st("overlay0"),
        "ui.linenr.selected": st(u["line_nr_cur"], mods=["bold"]),
        "ui.debug.breakpoint": st("red_hi"),
        "ui.debug.active": st("yellow"),
        "ui.statusline": st("subtext1", "mantle"),
        "ui.statusline.inactive": st("overlay0", "crust"),
        "ui.statusline.normal": st("ink", "orange", ["bold"]),
        "ui.statusline.insert": st("ink", "green", ["bold"]),
        "ui.statusline.select": st("ink", "yellow", ["bold"]),
        "ui.statusline.separator": st("surface1"),
        "ui.bufferline": st("overlay1", "crust"),
        "ui.bufferline.active": st("text_hi", "base", ["bold"], ul="orange"),
        "ui.bufferline.background": st(bg="crust"),
        "ui.popup": st("text", "mantle"),
        "ui.popup.info": st("text", "mantle"),
        "ui.picker.header": st("subtext0", "mantle", ["bold"]),
        "ui.picker.header.column": st("overlay1"),
        "ui.picker.header.column.active": st("yellow", mods=["bold"]),
        "ui.window": st("crust"),
        "ui.help": st("subtext1", "mantle"),
        "ui.menu": st("subtext1", "mantle"),
        "ui.menu.selected": st("text_hi", "surface1", ["bold"]),
        "ui.menu.scroll": st("overlay0", "surface0"),
        "ui.virtual.whitespace": st("surface1"),
        "ui.virtual.ruler": st(bg="surface0"),
        "ui.virtual.indent-guide": st("surface0"),
        "ui.virtual.inlay-hint": st("overlay1", "inlay_bg", ["italic"]),
        "ui.virtual.inlay-hint.parameter": st("overlay1", "inlay_bg", ["italic"]),
        "ui.virtual.inlay-hint.type": st("overlay1", "inlay_bg", ["italic"]),
        "ui.virtual.wrap": st("surface2"),
        "ui.virtual.jump-label": st("ink", "orange", ["bold"]),
        "tabstop": st(bg="surface1"),
        # ── diagnostics ────────────────────────────────────────────────────
        "error": st("red_hi"),
        "warning": st("yellow"),
        "info": st("denim"),
        "hint": st("sage"),
        "error.diagnostic.inline": st("red_hi", "error_bg"),
        "warning.diagnostic.inline": st("yellow", "warning_bg"),
        "info.diagnostic.inline": st("denim", "info_bg"),
        "hint.diagnostic.inline": st("sage", "hint_bg"),
        "diagnostic": st(ul="overlay1", ul_style="curl"),
        "diagnostic.error": st(ul="red_hi", ul_style="curl"),
        "diagnostic.warning": st(ul="yellow", ul_style="curl"),
        "diagnostic.info": st(ul="denim", ul_style="curl"),
        "diagnostic.hint": st(ul="sage", ul_style="curl"),
        "diagnostic.unnecessary": st("overlay1"),
        "diagnostic.deprecated": st(mods=["crossed_out"]),
    }
    rainbow = ["red_hi", "orange", "yellow", "green", "sage", "denim", "clay"]
    return s, rainbow, pal


def toml_value(v):
    if isinstance(v, str):
        return f'"{v}"'
    if isinstance(v, list):
        return "[" + ", ".join(toml_value(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{ " + ", ".join(f"{k} = {toml_value(x)}" for k, x in v.items()) + " }"
    raise TypeError(v)


def render(f):
    scopes, rainbow, pal = theme(f)
    lines = [f"# {HEADER}", f"# {f.name} — {f.blurb}", ""]
    for key, spec in scopes.items():
        # a bare fg is written as a plain string, like Helix's own themes
        val = spec["fg"] if list(spec) == ["fg"] else spec
        lines.append(f'"{key}" = {toml_value(val)}')
    lines += ["", f"rainbow = {toml_value(rainbow)}", "", "[palette]"]
    lines += [f'{k} = "{v.lower()}"' for k, v in pal.items()]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.snake}.toml", render(f), flavor=f.id,
            dest=f"~/.config/helix/themes/{f.snake}.toml", lang="toml")
        for f in flavors
    ]
