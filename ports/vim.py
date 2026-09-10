"""Vim: a Vimscript colorscheme per flavor (true color + nearest xterm-256), plus lightline and airline themes."""

from ports import nvim
from ports._editors import ui
from ports._lib import HEADER, REPO, Out, tints

META = {
    "id": "vim",
    "name": "Vim",
    "category": "Editors",
    "homepage": "https://www.vim.org",
    "enable": {"where": "~/.vimrc", "code": "set termguicolors\ncolorscheme {slug}", "lang": "vim"},
    "notes": "True-color and 256-color definitions in one file, with groups for ALE, coc, vim-lsp, GitGutter, "
    "NERDTree, fugitive and more, plus lightline and airline themes. `colorscheme subway-seat` follows "
    "`background`, so `set background=light` gives you Enamel.",
}

AUTHOR = "Oddur Sigurdsson"

# ── Nearest xterm-256 color (16–255; 0–15 belong to the terminal's own palette) ──
_LEVELS = (0, 95, 135, 175, 215, 255)
XTERM = {16 + i: (_LEVELS[i // 36], _LEVELS[i // 6 % 6], _LEVELS[i % 6]) for i in range(216)}
XTERM.update({232 + i: (8 + 10 * i,) * 3 for i in range(24)})


def xterm(color):
    r, g, b = (int(color[i : i + 2], 16) for i in (1, 3, 5))

    def dist(c):  # "redmean" weighted distance: cheap and close to perceptual
        rm = (r + c[0]) / 2
        return (2 + rm / 256) * (r - c[0]) ** 2 + 4 * (g - c[1]) ** 2 + (2 + (255 - rm) / 256) * (b - c[2]) ** 2

    return min(XTERM, key=lambda i: dist(XTERM[i]))


# Groups nvim.groups() defines that Vim has too (the rest are Neovim-only).
VIM_GROUPS = set("""
ColorColumn Conceal Cursor lCursor CursorIM CursorColumn CursorLine Directory DiffAdd DiffChange DiffDelete DiffText
EndOfBuffer ErrorMsg Folded FoldColumn SignColumn IncSearch LineNr CursorLineNr MatchParen ModeMsg MoreMsg
NonText Normal Pmenu PmenuSel PmenuKind PmenuExtra PmenuSbar PmenuThumb PmenuMatch PmenuMatchSel Question QuickFixLine
Search CurSearch SpecialKey SpellBad SpellCap SpellLocal SpellRare StatusLine StatusLineNC TabLine TabLineFill
TabLineSel Title Visual VisualNOS WarningMsg WildMenu Added Changed Removed
Comment Constant String Character Number Float Boolean Identifier Function Statement Conditional Repeat Label
Operator Keyword Exception PreProc Include Define Macro PreCondit Type StorageClass Structure Typedef Special
SpecialChar Tag Delimiter SpecialComment Debug Underlined Error Todo
""".split())


def groups(f):
    c, u, t = f, ui(f), tints(f)
    ink = u["ink"]
    S = lambda role: {"fg": f.syntax(role)[0], **{k: True for k in f.syntax(role)[1]}}
    link = lambda target: {"link": target}
    float_bg = c.mantle
    inlay_bg = f.mix("surface0", "base", 0.6)

    g = {k: dict(v) for k, v in nvim.groups(f).items() if k in VIM_GROUPS}
    g.update({
        # the per-flavor UI decisions shared by every editor port
        "Cursor": {"fg": ink, "bg": u["cursor"]},
        "lCursor": {"fg": ink, "bg": u["cursor"]},
        "CursorIM": {"fg": ink, "bg": u["cursor"]},
        "CursorLine": {"bg": u["line"]},
        "CursorColumn": {"bg": u["line"]},
        "ColorColumn": {"bg": u["line"]},
        "CursorLineNr": {"fg": u["line_nr_cur"], "bold": True},
        "LineNr": {"fg": u["line_nr"]},
        "Visual": {"bg": u["selection"]},
        "VisualNOS": {"bg": u["selection"]},
        "Search": {"bg": u["search"]},
        "IncSearch": {"fg": c.text_hi, "bg": u["search_cur"], "bold": True},
        "CurSearch": link("IncSearch"),
        "MatchParen": {"fg": u["bracket_fg"], "bg": u["bracket_bg"], "bold": True},
        "VertSplit": {"fg": c.crust, "bg": c.crust},
        "Todo": {"fg": ink, "bg": c.yellow, "bold": True},
        # Vim-only UI groups
        "LineNrAbove": link("LineNr"),
        "LineNrBelow": link("LineNr"),
        "CursorLineSign": link("SignColumn"),
        "CursorLineFold": link("FoldColumn"),
        "StatusLineTerm": link("StatusLine"),
        "StatusLineTermNC": link("StatusLineNC"),
        "Terminal": {"fg": c.text, "bg": c.base},
        "PmenuKindSel": {"fg": c.sage, "bg": c.surface1, "bold": True},
        "PmenuExtraSel": {"fg": c.overlay1, "bg": c.surface1},
        "PmenuBorder": {"fg": c.surface2, "bg": float_bg},
        "PmenuShadow": {"bg": c.crust},
        "PreInsert": {"fg": c.overlay0, "italic": True},
        "PopupSelected": link("PmenuSel"),
        "PopupNotification": {"fg": c.text, "bg": float_bg},
        "MessageWindow": link("Pmenu"),
        "DiffTextAdd": {"bg": t["add_emph"]},
        "TabPanel": {"fg": c.overlay1, "bg": c.crust},
        "TabPanelFill": {"bg": c.crust},
        "TabPanelSel": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "TitleBar": {"fg": c.subtext0, "bg": c.crust},
        "TitleBarNC": {"fg": c.overlay0, "bg": c.crust},
        "ToolbarLine": {"bg": c.mantle},
        "ToolbarButton": {"fg": c.text, "bg": c.surface1, "bold": True},
        "Menu": {"fg": c.subtext1, "bg": c.mantle},
        "Scrollbar": {"fg": c.overlay0, "bg": c.mantle},
        "Tooltip": {"fg": c.text, "bg": c.mantle},
        "debugPC": {"bg": t["chg"]},
        "debugBreakpoint": {"fg": c.red_hi, "bg": t["del"]},
        "qfFileName": {"fg": c.yellow},
        "qfLineNr": {"fg": c.overlay0},
    })

    # diagnostics: ALE, coc.nvim, vim-lsp, yegappan/lsp
    levels = [
        # ALE, coc, vim-lsp, yegappan/lsp level names; color; virtual-text ground
        ("Error", "Error", "Error", "Error", u["error"], f.mix("red", "base", 0.12)),
        ("Warning", "Warning", "Warning", "Warning", u["warning"], f.mix("yellow", "base", 0.1)),
        ("Info", "Info", "Information", "Info", u["info"], f.mix("denim", "base", 0.1)),
        (None, "Hint", "Hint", "Hint", u["hint"], f.mix("sage", "base", 0.1)),
    ]
    for ale, coc, vlsp, ylsp, col, vbg in levels:
        curl = {"sp": col, "undercurl": True}
        if ale:
            g[f"ALE{ale}Sign"] = {"fg": col}
            g[f"ALE{ale}"] = curl
            g[f"ALEVirtualText{ale}"] = {"fg": col, "bg": vbg}
        g[f"Coc{coc}Sign"] = {"fg": col}
        g[f"Coc{coc}Highlight"] = curl
        g[f"Coc{coc}VirtualText"] = {"fg": col, "bg": vbg}
        g[f"Lsp{vlsp}Text"] = {"fg": col}
        g[f"Lsp{vlsp}Highlight"] = curl
        g[f"Lsp{vlsp}VirtualText"] = {"fg": col, "bg": vbg}
        g[f"LspDiagSign{ylsp}Text"] = {"fg": col}
        g[f"LspDiagVirtualText{ylsp}"] = {"fg": col, "bg": vbg}
        g[f"LspDiagInline{ylsp}"] = curl

    g.update({
        "CocFloating": {"fg": c.text, "bg": float_bg},
        "CocFloatBorder": {"fg": c.surface2, "bg": float_bg},
        "CocMenuSel": link("PmenuSel"),
        "CocSearch": {"fg": c.yellow, "bold": True},
        "CocPumSearch": {"fg": c.yellow, "bold": True},
        "CocHighlightText": {"bg": c.surface1},
        "CocInlayHint": {"fg": c.overlay1, "bg": inlay_bg, "italic": True},
        "CocUnusedHighlight": {"fg": c.overlay1},
        "CocDeprecatedHighlight": {"strikethrough": True},
        "CocFadeOut": {"fg": c.overlay0},
        "lspReference": {"bg": c.surface1},
        "lspInlayHintsType": {"fg": c.overlay1, "bg": inlay_bg, "italic": True},
        "lspInlayHintsParameter": {"fg": c.overlay1, "bg": inlay_bg, "italic": True},
        "LspInlayHintsType": {"fg": c.overlay1, "bg": inlay_bg, "italic": True},
        "LspInlayHintsParam": {"fg": c.overlay1, "bg": inlay_bg, "italic": True},
        "LspSigActiveParameter": {"fg": c.yellow_hi, "bold": True, "underline": True},
        "CopilotSuggestion": {"fg": c.overlay0, "italic": True},
        "CopilotAnnotation": {"fg": c.overlay0, "italic": True},
        # git: GitGutter, Signify, fugitive, the diff and gitcommit syntaxes
        "GitGutterAdd": {"fg": c.green},
        "GitGutterChange": {"fg": c.yellow},
        "GitGutterDelete": {"fg": c.red_hi},
        "GitGutterChangeDelete": {"fg": c.clay},
        "GitGutterAddLine": {"bg": t["add"]},
        "GitGutterChangeLine": {"bg": t["chg"]},
        "GitGutterDeleteLine": {"bg": t["del"]},
        "GitGutterAddIntraLine": {"bg": t["add_emph"]},
        "GitGutterDeleteIntraLine": {"bg": t["del_emph"]},
        "SignifySignAdd": {"fg": c.green},
        "SignifySignChange": {"fg": c.yellow},
        "SignifySignDelete": {"fg": c.red_hi},
        "SignifySignDeleteFirstLine": {"fg": c.red_hi},
        "SignifySignChangeDelete": {"fg": c.clay},
        "diffAdded": {"fg": c.green},
        "diffRemoved": {"fg": c.red_hi},
        "diffChanged": {"fg": c.yellow},
        "diffFile": {"fg": c.denim, "bold": True},
        "diffNewFile": {"fg": c.green},
        "diffOldFile": {"fg": c.red_hi},
        "diffIndexLine": {"fg": c.overlay1},
        "diffLine": {"fg": c.denim},
        "diffSubname": {"fg": c.subtext0},
        "fugitiveHeading": S("heading"),
        "fugitiveHeader": {"fg": c.orange, "bold": True},
        "fugitiveUntrackedHeading": S("heading"),
        "fugitiveUnstagedHeading": S("heading"),
        "fugitiveStagedHeading": S("heading"),
        "fugitiveUntrackedModifier": {"fg": c.overlay1},
        "fugitiveUnstagedModifier": {"fg": c.yellow},
        "fugitiveStagedModifier": {"fg": c.green},
        "fugitiveHash": {"fg": c.overlay1},
        "fugitiveSymbolicRef": {"fg": c.yellow, "bold": True},
        "gitcommitSummary": {"fg": c.text_hi},
        "gitcommitOverflow": {"fg": c.red_hi},
        "gitcommitBranch": {"fg": c.yellow, "bold": True},
        "gitcommitHeader": {"fg": c.subtext0},
        "gitcommitSelectedType": {"fg": c.green},
        "gitcommitSelectedFile": {"fg": c.green},
        "gitcommitDiscardedType": {"fg": c.red_hi},
        "gitcommitDiscardedFile": {"fg": c.red_hi},
        "gitcommitUntrackedFile": {"fg": c.overlay1},
        # file trees: NERDTree, fern, netrw
        "NERDTreeDir": {"fg": c.subtext1},
        "NERDTreeDirSlash": {"fg": c.yellow},
        "NERDTreeOpenable": {"fg": c.yellow},
        "NERDTreeClosable": {"fg": c.yellow},
        "NERDTreeFile": {"fg": c.subtext0},
        "NERDTreeExecFile": {"fg": c.clay},
        "NERDTreeUp": {"fg": c.overlay1},
        "NERDTreeCWD": {"fg": c.orange, "bold": True},
        "NERDTreeHelp": {"fg": c.overlay1, "italic": True},
        "NERDTreeLinkTarget": {"fg": c.denim},
        "NERDTreeFlags": {"fg": c.overlay0},
        "FernRootSymbol": {"fg": c.orange},
        "FernRootText": {"fg": c.orange, "bold": True},
        "FernBranchSymbol": {"fg": c.yellow},
        "FernBranchText": {"fg": c.subtext1},
        "FernLeafSymbol": {"fg": c.overlay0},
        "FernLeafText": {"fg": c.subtext0},
        "FernMarkedLine": {"bg": c.surface1},
        "FernMarkedText": {"fg": c.yellow},
        "netrwTreeBar": {"fg": c.surface1},
        "netrwClassify": {"fg": c.yellow},
        "netrwExe": {"fg": c.clay},
        "netrwSymLink": {"fg": c.denim},
        # pickers, motion, keys, start screens
        "CtrlPMatch": {"fg": c.yellow, "bold": True},
        "CtrlPNoEntries": {"fg": c.red_hi},
        "CtrlPPrtBase": {"fg": c.overlay0},
        "CtrlPPrtText": {"fg": c.text},
        "CtrlPPrtCursor": {"fg": ink, "bg": u["cursor"]},
        "CtrlPLinePre": {"fg": c.overlay0},
        "CtrlPMode1": {"fg": ink, "bg": c.orange, "bold": True},
        "CtrlPMode2": {"fg": c.subtext1, "bg": c.surface1},
        "CtrlPStats": {"fg": c.overlay1, "bg": c.mantle},
        "EasyMotionTarget": {"fg": c.orange, "bold": True},
        "EasyMotionTarget2First": {"fg": c.yellow, "bold": True},
        "EasyMotionTarget2Second": {"fg": c.clay, "bold": True},
        "EasyMotionShade": {"fg": c.overlay0},
        "EasyMotionMoveHL": {"fg": ink, "bg": c.yellow},
        "EasyMotionIncSearch": {"fg": c.text_hi, "bg": c.surface2},
        "Sneak": {"fg": ink, "bg": c.orange, "bold": True},
        "SneakLabel": {"fg": ink, "bg": c.orange, "bold": True},
        "SneakLabelMask": {"fg": c.orange, "bg": c.orange},
        "SneakScope": {"bg": c.surface2},
        "WhichKey": {"fg": c.yellow},
        "WhichKeyGroup": {"fg": c.orange},
        "WhichKeyDesc": {"fg": c.subtext1},
        "WhichKeySeperator": {"fg": c.overlay0},  # sic: vim-which-key's spelling
        "WhichKeySeparator": {"fg": c.overlay0},
        "WhichKeyFloating": {"fg": c.subtext1, "bg": float_bg},
        "StartifyHeader": {"fg": c.orange},
        "StartifySection": S("heading"),
        "StartifyNumber": {"fg": c.yellow},
        "StartifyBracket": {"fg": c.overlay0},
        "StartifyFile": {"fg": c.subtext1},
        "StartifyPath": {"fg": c.overlay1},
        "StartifySlash": {"fg": c.overlay0},
        "StartifySpecial": {"fg": c.overlay1},
        "StartifyFooter": {"fg": c.overlay1, "italic": True},
        "IndentGuidesOdd": {"bg": f.mix("surface0", "base", 0.4)},
        "IndentGuidesEven": {"bg": f.mix("surface0", "base", 0.8)},
        "illuminatedWord": {"bg": c.surface1},
        "illuminatedCurWord": {"bg": c.surface1},
        "TagbarKind": {"fg": c.orange},
        "TagbarScope": {"fg": c.sage},
        "TagbarType": {"fg": c.sage},
        "TagbarSignature": {"fg": c.overlay1},
        "TagbarFoldIcon": {"fg": c.yellow},
        "TagbarHighlight": {"bg": c.surface1},
        "UndotreeNode": {"fg": c.orange},
        "UndotreeNodeCurrent": {"fg": c.yellow, "bold": True},
        "UndotreeSeq": {"fg": c.clay},
        "UndotreeBranch": {"fg": c.overlay1},
        "UndotreeTimeStamp": {"fg": c.overlay1},
        "UndotreeSavedSmall": {"fg": c.green},
        "UndotreeSavedBig": {"fg": c.green, "bold": True},
        # Vim's own syntax files: markdown, html/xml, help, python
        "markdownH1": nvim_heading(f, 1),
        "markdownH2": nvim_heading(f, 2),
        "markdownH3": nvim_heading(f, 3),
        "markdownH4": nvim_heading(f, 4),
        "markdownH5": nvim_heading(f, 5),
        "markdownH6": nvim_heading(f, 6),
        **{f"markdownH{n}Delimiter": link(f"markdownH{n}") for n in range(1, 7)},
        "markdownCode": S("code"),
        "markdownCodeBlock": S("code"),
        "markdownCodeDelimiter": {"fg": c.overlay1},
        "markdownLinkText": {"fg": c.sage},
        "markdownUrl": {"fg": c.denim, "underline": True},
        "markdownLinkDelimiter": S("punctuation"),
        "markdownLinkTextDelimiter": S("punctuation"),
        "markdownBold": S("strong"),
        "markdownItalic": S("emphasis"),
        "markdownBoldItalic": {"fg": c.text_hi, "bold": True, "italic": True},
        "markdownStrike": {"fg": c.overlay1, "strikethrough": True},
        "markdownListMarker": {"fg": c.orange},
        "markdownOrderedListMarker": {"fg": c.orange},
        "markdownBlockquote": S("quote"),
        "markdownRule": {"fg": c.overlay0},
        "htmlTag": S("punctuation"),
        "htmlEndTag": S("punctuation"),
        "htmlTagName": S("tag"),
        "htmlSpecialTagName": S("tag"),
        "htmlArg": S("attribute"),
        "htmlLink": {"fg": c.denim, "underline": True},
        "htmlBold": S("strong"),
        "htmlItalic": S("emphasis"),
        **{f"htmlH{n}": nvim_heading(f, n) for n in range(1, 7)},
        "xmlTag": S("punctuation"),
        "xmlEndTag": S("tag"),
        "xmlTagName": S("tag"),
        "xmlAttrib": S("attribute"),
        "helpHyperTextJump": S("link"),
        "helpHyperTextEntry": {"fg": c.yellow},
        "helpHeader": S("heading"),
        "helpHeadline": S("heading"),
        "helpSectionDelim": {"fg": c.overlay0},
        "helpExample": S("code"),
        "helpCommand": S("code"),
        "helpOption": {"fg": c.sage},
        "helpSpecial": {"fg": c.clay},
        "helpNote": {"fg": ink, "bg": c.sage, "bold": True},
        "helpWarning": {"fg": ink, "bg": c.yellow, "bold": True},
        "helpDeprecated": {"fg": c.red_hi},
        "vimCommentTitle": {"fg": c.overlay2, "bold": True, "italic": True},
        "pythonBuiltin": S("function.builtin"),
        "pythonDecorator": S("decorator"),
        "pythonDecoratorName": S("decorator"),
        "pythonExceptions": S("type"),
    })
    return g


def nvim_heading(f, n):
    return dict(nvim.groups(f)[f"@markup.heading.{n}"])


ATTRS = ("bold", "italic", "underline", "undercurl", "strikethrough", "reverse", "nocombine")


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


def nvim_handoff(arg):
    """In Neovim with the Lua plugin installed alongside, let the plugin do it."""
    return [
        "if has('nvim') && !empty(nvim_get_runtime_file('lua/subway-seat/init.lua', v:false))",
        f"  lua require('subway-seat').load({arg})",
        "  finish",
        "endif",
        "",
    ]


def colorscheme(f):
    lines = preamble(f.name, f.blurb) + nvim_handoff(f"'{f.id}'")
    lines += [
        f"set background={'dark' if f.dark else 'light'}",
        "hi clear",
        f"let g:colors_name = '{f.slug}'",
        "",
    ]
    lines += body(f)
    return "\n".join(lines) + "\n"


def auto(walnut, enamel):
    """colors/subway-seat.vim: Walnut on a dark background, Enamel on a light one."""
    lines = preamble("Subway Seat", "Walnut when 'background' is dark, Enamel when it is light.")
    lines += nvim_handoff("")
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
    e = lambda fg, bg, *attr: [fg, bg, xterm(fg), xterm(bg), *attr]
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
    lines = [f'" {HEADER}', f'" lightline: let g:lightline = {{ \'colorscheme\': \'{name}\' }}', ""]
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
    e = lambda fg, bg, *attr: [fg, bg, xterm(fg), xterm(bg), *attr]
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
    outs = []
    for f in flavors:
        text = auto(walnut, enamel) if f is walnut else colorscheme(f)
        outs.append(Out(f"colors/{f.slug}.vim", text, flavor=f.id,
                        dest=f"~/.vim/colors/{f.slug}.vim", lang="vim"))
        pair = [walnut, enamel] if f is walnut else [f]
        outs.append(Out(f"autoload/lightline/colorscheme/{f.snake}.vim", lightline(f.snake, pair), flavor=f.id,
                        dest=f"~/.vim/autoload/lightline/colorscheme/{f.snake}.vim", lang="vim"))
        outs.append(Out(f"autoload/airline/themes/{f.snake}.vim", airline(f.snake, pair), flavor=f.id,
                        dest=f"~/.vim/autoload/airline/themes/{f.snake}.vim", lang="vim"))
    return outs
