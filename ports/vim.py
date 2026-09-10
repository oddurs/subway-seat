"""Vim: a Vimscript colorscheme per flavor (true color + nearest xterm-256), plus lightline and airline themes."""

import palette as p
from ports import nvim
from ports._editors import ui
from ports._lib import HEADER, REPO, Out, tints

META = {
    "id": "vim",
    "name": "Vim",
    "category": "Editors",
    "homepage": "https://www.vim.org",
    "enable": {
        "where": "~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc)",
        "code": "if has('termguicolors') | set termguicolors | endif\ncolorscheme subway-seat-{id}",
        "lang": "vim",
    },
    "auto": {
        "where": "~/.vimrc",
        "code": "\" subway-seat follows 'background': Walnut when dark, Enamel when light.\n"
        "\" Vim sets 'background' from the terminal's colors when the terminal reports them.\n"
        "if has('termguicolors') | set termguicolors | endif\n"
        "colorscheme subway-seat",
        "lang": "vim",
    },
    "detect": ["vim", "gvim", "mvim", "/Applications/MacVim.app"],
    "notes": "True-color and 256-color definitions in one file, with groups for ALE, coc, vim-lsp, GitGutter, "
    "Signify, fugitive, NERDTree, fern and more, plus lightline and airline themes "
    "(`let g:lightline = { 'colorscheme': 'subway_seat' }`, `let g:airline_theme = 'subway_seat'`). "
    "`colorscheme subway-seat` follows `background`. Install with vim-plug: "
    "`Plug 'oddurs/subway-seat', { 'rtp': 'dist/vim' }`, or copy the folders into `~/.vim`.",
}

AUTHOR = "Oddur Sigurdsson"

# ── Nearest xterm-256 color (16–255; 0–15 belong to the terminal's own palette) ──
_LEVELS = (0, 95, 135, 175, 215, 255)
XTERM = {16 + i: (_LEVELS[i // 36], _LEVELS[i // 6 % 6], _LEVELS[i % 6]) for i in range(216)}
XTERM.update({232 + i: (8 + 10 * i,) * 3 for i in range(24)})


def _oklab(rgb):
    lin = [((v / 255 + 0.055) / 1.055) ** 2.4 if v / 255 > 0.04045 else v / 255 / 12.92 for v in rgb]
    r, g, b = lin
    lms = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b,
           0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b,
           0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b)
    l_, m_, s_ = (x ** (1 / 3) for x in lms)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


_XTERM_LAB = {i: _oklab(rgb) for i, rgb in XTERM.items()}


def xterm(color):
    """Nearest xterm-256 index in OKLab, with hue and chroma weighted double so a muted
    accent keeps its hue instead of landing on a grey of the same lightness."""
    L, a, b = _oklab(p.hex_to_rgb(color))

    def dist(i):
        L2, a2, b2 = _XTERM_LAB[i]
        return (L - L2) ** 2 + 2 * ((a - a2) ** 2 + (b - b2) ** 2)

    return min(XTERM, key=dist)


# Groups nvim.groups() defines that Vim has too (the rest are Neovim-only).
VIM_GROUPS = {
    "ColorColumn", "Conceal", "Cursor", "lCursor", "CursorIM", "CursorColumn", "CursorLine", "Directory",
    "DiffAdd", "DiffChange", "DiffDelete", "DiffText", "DiffTextAdd", "EndOfBuffer", "ErrorMsg", "Folded",
    "FoldColumn", "SignColumn", "IncSearch", "LineNr", "CursorLineNr", "MatchParen", "ModeMsg", "MoreMsg",
    "NonText", "Normal", "Pmenu", "PmenuSel", "PmenuKind", "PmenuKindSel", "PmenuExtra", "PmenuExtraSel",
    "PmenuSbar", "PmenuThumb", "PmenuMatch", "PmenuMatchSel", "PmenuBorder", "PmenuShadow", "PreInsert",
    "Question", "QuickFixLine", "Search", "CurSearch", "SpecialKey", "SpellBad", "SpellCap", "SpellLocal",
    "SpellRare", "StatusLine", "StatusLineNC", "TabLine", "TabLineFill", "TabLineSel", "Title", "Visual",
    "VisualNOS", "WarningMsg", "WildMenu", "Added", "Changed", "Removed", "Comment", "Constant", "String",
    "Character", "Number", "Float", "Boolean", "Identifier", "Function", "Statement", "Conditional", "Repeat",
    "Label", "Operator", "Keyword", "Exception", "PreProc", "Include", "Define", "Macro", "PreCondit", "Type",
    "StorageClass", "Structure", "Typedef", "Special", "SpecialChar", "Tag", "Delimiter", "SpecialComment",
    "Debug", "Underlined", "Ignore", "Error", "Todo", "Bold", "Italic",
}


def groups(f):
    c, u, t = f, ui(f), tints(f)
    ink = u["ink"]
    paper = u["paper"]

    def link(target):
        return {"link": target}

    g = {k: dict(v) for k, v in nvim.groups(f).items() if k in VIM_GROUPS}
    g.update({
        # Vim's pop-up menu has no blend or shadow attribute; a solid edge instead
        "PmenuShadow": {"bg": c.crust},
        "VertSplit": {"fg": c.crust, "bg": c.crust},
        "VertSplitNC": {"fg": c.crust, "bg": c.crust},
        # Vim-only UI groups
        "LineNrAbove": link("LineNr"),
        "LineNrBelow": link("LineNr"),
        "CursorLineSign": link("SignColumn"),
        "CursorLineFold": link("FoldColumn"),
        "StatusLineTerm": link("StatusLine"),
        "StatusLineTermNC": link("StatusLineNC"),
        "Terminal": {"fg": c.text, "bg": c.base},
        "ComplMatchIns": {},
        "PopupSelected": link("PmenuSel"),
        "PopupNotification": {"fg": c.text, "bg": paper},
        "MessageWindow": link("Pmenu"),
        "TabPanel": {"fg": c.overlay1, "bg": c.crust},
        "TabPanelFill": {"bg": c.crust},
        "TabPanelSel": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "TitleBar": {"fg": c.subtext0, "bg": c.crust},
        "TitleBarNC": {"fg": c.overlay0, "bg": c.crust},
        "ToolbarLine": {"bg": c.mantle},
        "ToolbarButton": {"fg": c.text, "bg": c.surface1, "bold": True},
        "Menu": {"fg": c.subtext1, "bg": c.mantle},
        "Scrollbar": {"fg": c.overlay0, "bg": c.mantle},
        "Tooltip": {"fg": c.text, "bg": paper},
        "debugPC": {"bg": t["chg"]},
        "debugBreakpoint": {"fg": c.red_hi, "bg": t["del"]},
        "Todo": {"fg": ink, "bg": c.yellow, "bold": True},
    })
    g.update(nvim.syntax_files(f))
    g.update(nvim.shared_plugins(f))
    return g


ATTRS = ("bold", "italic", "underline", "undercurl", "underdouble", "strikethrough", "reverse", "nocombine")


def hi(name, spec):
    if "link" in spec:
        return f"hi! link {name} {spec['link']}"
    attrs = ",".join(a for a in ATTRS if spec.get(a)) or "NONE"
    fg, bg, sp = (spec.get(k, "NONE") for k in ("fg", "bg", "sp"))
    cfg, cbg = (xterm(x) if x != "NONE" else "NONE" for x in (fg, bg))
    return (f"hi {name} guifg={fg} guibg={bg} guisp={sp} gui={attrs} "
            f"ctermfg={cfg} ctermbg={cbg} cterm={attrs}")


def body(f):
    """The flavor's highlight commands: definitions first, then links."""
    g = groups(f)
    ansi = ", ".join(f"'{x}'" for x in f.ansi)
    defs = sorted((n, s) for n, s in g.items() if "link" not in s)
    links = sorted((n, s) for n, s in g.items() if "link" in s)
    lines = [f"let g:terminal_ansi_colors = [{ansi}]"]
    lines += [hi(n, s) for n, s in defs]
    lines += [hi(n, s) for n, s in links]
    return lines


def preamble(title, blurb):
    return [
        f'" Name:        {title}',
        f'" Description: {blurb}',
        f'" Author:      {AUTHOR}',
        f'" URL:         {REPO}',
        '" License:     MIT',
        f'" {HEADER}',
        "",
    ]


def nvim_handoff(name):
    """In Neovim with the Lua plugin installed alongside, let the plugin do it."""
    return [
        "if has('nvim') && !empty(nvim_get_runtime_file('lua/subway-seat/init.lua', v:false))",
        f"  lua require('subway-seat').colorscheme('{name}')",
        "  finish",
        "endif",
        "",
    ]


def colorscheme(f):
    """colors/subway-seat-<flavor>.vim: one flavor."""
    name = f"subway-seat-{f.id}"
    bg, other = ("dark", "light") if f.dark else ("light", "dark")
    to = "'enamel'" if f.dark else "get(g:, 'subway_seat_dark', 'walnut')"
    lines = preamble(f.name, f.blurb) + nvim_handoff(name)
    lines += [
        "\" 'background' changed while this flavor was on: follow it, as `colorscheme subway-seat` does.",
        f"if get(g:, 'colors_name', '') ==# '{name}' && &background ==# '{other}'",
        f"  execute 'runtime colors/subway-seat-' . {to} . '.vim'",
        "  finish",
        "endif",
        "",
        f"set background={bg}",
        "hi clear",
        f"let g:colors_name = '{name}'",
    ]
    if f.dark:
        lines.append(f"let g:subway_seat_dark = '{f.id}'")
    lines.append("")
    lines += body(f)
    return "\n".join(lines) + "\n"


def auto(walnut, enamel):
    """colors/subway-seat.vim: Walnut on a dark background, Enamel on a light one."""
    lines = preamble("Subway Seat", "Walnut when 'background' is dark, Enamel when it is light.")
    lines += nvim_handoff("subway-seat")
    lines += [
        "hi clear",
        "let g:colors_name = 'subway-seat'",
        "",
        "if &background ==# 'light'",
        *("  " + x for x in body(enamel)),
        "else",
        *("  " + x for x in body(walnut)),
        "endif",
    ]
    return "\n".join(lines) + "\n"


# ── lightline and airline: route-bullet mode segments, mirroring nvim's lualine ──
def _modes(f):
    return {"normal": f.orange, "insert": f.green, "visual": f.yellow, "replace": f.red_hi,
            "command": f.sage, "terminal": f.clay}


def lightline_palette(f):
    ink = ui(f)["ink"]

    def e(fg, bg, *attr):
        return [fg, bg, xterm(fg), xterm(bg), *attr]

    b, cc = e(f.subtext1, f.surface1), e(f.subtext0, f.mantle)
    pal = {}
    for mode, col in _modes(f).items():
        a = e(ink, col, "bold")
        pal[mode] = {"left": [a, b], "middle": [cc], "right": [a, b]}
    pal["normal"]["error"] = [e(ink, f.red_hi)]
    pal["normal"]["warning"] = [e(ink, f.yellow)]
    dim = e(f.overlay1, f.crust)
    pal["inactive"] = {"left": [dim, dim], "middle": [e(f.overlay0, f.crust)], "right": [dim, dim]}
    pal["tabline"] = {"left": [dim], "tabsel": [e(f.text_hi, f.base, "bold")],
                      "middle": [e(f.overlay0, f.crust)], "right": [dim]}
    return pal


def vimlit(v):
    if isinstance(v, dict):
        return "{" + ", ".join(f"'{k}': {vimlit(x)}" for k, x in v.items()) + "}"
    if isinstance(v, list):
        return "[" + ", ".join(vimlit(x) for x in v) + "]"
    if isinstance(v, int):
        return str(v)
    return f"'{v}'"


def lightline(name, flavors_by_bg):
    var = f"g:lightline#colorscheme#{name}#palette"
    lines = [f'" {HEADER}', f"\" lightline: let g:lightline = {{ 'colorscheme': '{name}' }}", ""]
    if len(flavors_by_bg) == 1:
        lines.append(f"let {var} = {vimlit(lightline_palette(flavors_by_bg[0]))}")
    else:
        dark, light = flavors_by_bg
        lines += [
            "if &background ==# 'light'",
            f"  let {var} = {vimlit(lightline_palette(light))}",
            "else",
            f"  let {var} = {vimlit(lightline_palette(dark))}",
            "endif",
        ]
    return "\n".join(lines) + "\n"


def airline_palette(f, var):
    ink = ui(f)["ink"]

    def e(fg, bg, *attr):
        return [fg, bg, xterm(fg), xterm(bg), *attr]

    n2, n3 = e(f.subtext1, f.surface1), e(f.subtext0, f.mantle)
    modes = {"normal": f.orange, "insert": f.green, "visual": f.yellow, "replace": f.red_hi,
             "commandline": f.sage, "terminal": f.clay}
    lines = [f"let {var} = {{}}"]
    for mode, col in modes.items():
        lines.append(f"let {var}.{mode} = airline#themes#generate_color_map("
                     f"{vimlit(e(ink, col, 'bold'))}, {vimlit(n2)}, {vimlit(n3)})")
        lines.append(f"let {var}.{mode}.airline_warning = {vimlit(e(ink, f.yellow))}")
        lines.append(f"let {var}.{mode}.airline_error = {vimlit(e(ink, f.red_hi))}")
    dim = e(f.overlay1, f.crust)
    lines.append(f"let {var}.inactive = airline#themes#generate_color_map("
                 f"{vimlit(dim)}, {vimlit(dim)}, {vimlit(e(f.overlay0, f.crust))})")
    lines.append(f"let {var}.accents = {{'red': {vimlit([f.red_hi, '', xterm(f.red_hi), ''])}}}")
    return lines


def airline(name, flavors_by_bg):
    var = f"g:airline#themes#{name}#palette"
    lines = [f'" {HEADER}', f"\" airline: let g:airline_theme = '{name}'", ""]
    if len(flavors_by_bg) == 1:
        lines += airline_palette(flavors_by_bg[0], var)
    else:
        dark, light = flavors_by_bg
        lines += ["if &background ==# 'light'", *("  " + x for x in airline_palette(light, var)),
                  "else", *("  " + x for x in airline_palette(dark, var)), "endif"]
    return "\n".join(lines) + "\n"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    walnut, enamel = by_id["walnut"], by_id["enamel"]
    outs = [Out("colors/subway-seat.vim", auto(walnut, enamel), dest="~/.vim/colors/subway-seat.vim", lang="vim")]
    for f in flavors:
        outs.append(Out(f"colors/subway-seat-{f.id}.vim", colorscheme(f), flavor=f.id,
                        dest=f"~/.vim/colors/subway-seat-{f.id}.vim", lang="vim"))
    for f in flavors:
        # subway_seat pairs Walnut and Enamel by 'background'; the others are one flavor
        pair = [walnut, enamel] if f is walnut else [f]
        flavor = None if f is walnut else f.id
        outs.append(Out(f"autoload/lightline/colorscheme/{f.snake}.vim", lightline(f.snake, pair), flavor=flavor,
                        dest=f"~/.vim/autoload/lightline/colorscheme/{f.snake}.vim", lang="vim"))
        outs.append(Out(f"autoload/airline/themes/{f.snake}.vim", airline(f.snake, pair), flavor=flavor,
                        dest=f"~/.vim/autoload/airline/themes/{f.snake}.vim", lang="vim"))
    return outs
