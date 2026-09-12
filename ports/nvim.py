"""Neovim: a colorscheme plugin (setup(), flavors that follow 'background', lualine themes).

Layout of dist/nvim, which is a plugin root (lazy.nvim, vim-plug `rtp`, or copied into ~/.config/nvim):

    colors/subway-seat.lua           follows 'background': Walnut when dark, Enamel when light
    colors/subway-seat-<flavor>.lua  one flavor; also where its highlight groups live
    lua/subway-seat/init.lua         setup() and the loader
    lua/subway-seat/palette.lua      the palette, for overrides and statuslines
    lua/lualine/themes/*.lua         lualine themes, named like the colorschemes
    doc/subway-seat.txt              :help subway-seat

A colors file works on its own too (no options): copy the colors/ folder and it
applies the groups it carries. With lua/ on 'runtimepath' it hands off to the
plugin, which reads the same groups from it.
"""

from ports._editors import ui
from ports._lib import HEADER, VERSION, Out, resolve, solid, tints

META = {
    "id": "nvim",
    "name": "Neovim",
    "category": "Editors",
    "homepage": "https://neovim.io",
    "enable": {
        "where": "init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua)",
        "code": 'vim.cmd.colorscheme("{prefix}-{id}")',
        "lang": "lua",
    },
    "auto": {
        "where": "init.lua",
        "code": "-- `subway-seat` follows 'background': Walnut when dark, Enamel when light.\n"
        "-- Neovim sets 'background' from the terminal; auto-dark-mode.nvim sets it from the OS.\n"
        'require("subway-seat").setup({ background = { dark = "walnut", light = "enamel" } }) -- or dark = "tunnel"\n'
        'vim.cmd.colorscheme("subway-seat")\n'
        "\n"
        "-- lazy.nvim, to follow the OS light/dark setting:\n"
        '-- { "f-person/auto-dark-mode.nvim", opts = {} }',
        "lang": "lua",
    },
    "requires": "Neovim 0.9+",
    "detect": ["nvim"],
    "notes": "A plugin: `setup({ background, transparent, italics, overrides })`, flavors that follow "
    "`background` (flip it and Walnut becomes Enamel and back), lualine themes, and groups for Tree-sitter, "
    "LSP and about 70 plugins (mini, snacks, blink.cmp, telescope, gitsigns, diffview, neogit and more). "
    "Install with lazy.nvim: "
    '`{ "oddurs/subway-seat", lazy = false, priority = 1000, config = function(p) '
    'vim.opt.rtp:append(p.dir .. "/dist/nvim"); vim.cmd.colorscheme("subway-seat") end }`, '
    "or vim-plug: `Plug 'oddurs/subway-seat', { 'rtp': 'dist/nvim' }`. "
    "Or copy `dist/nvim` into `~/.config/nvim`; the colors files also work on their own.",
}

HEADINGS = ("orange", "yellow", "green", "sage", "clay", "subtext1")


def S(f, role, **extra):
    """A syntax role as a highlight spec, plus any extra attributes."""
    color, styles = f.syntax(role)
    return {"fg": color, **{k: True for k in sorted(styles)}, **extra}


def link(target):
    return {"link": target}


# ── Neovim's own groups: editor UI, syntax, diagnostics, LSP, Tree-sitter ──────
def groups(f):
    c, u, t = f, ui(f), tints(f)
    ink = u["ink"]
    paper, edge, row = u["paper"], u["edge"], u["row"]
    ref = solid("text@L2", f)  # reference highlights, folds
    shadow = resolve("shadow", f)
    ok_bg = f.mix("green", "base", 0.10)
    g = {
        # editor UI
        "Normal": {"fg": c.text, "bg": c.base},
        "NormalNC": {"fg": c.text, "bg": c.base},
        "NormalFloat": {"fg": c.text, "bg": paper},
        "FloatBorder": {"fg": edge, "bg": paper},
        "FloatTitle": {"fg": c.yellow, "bg": paper, "bold": True},
        "FloatFooter": {"fg": c.overlay1, "bg": paper},
        "FloatShadow": {"bg": shadow, "blend": 80},
        "FloatShadowThrough": {"bg": shadow, "blend": 100},
        "ColorColumn": {"bg": u["line"]},
        "Conceal": {"fg": c.overlay0},
        "Cursor": {"fg": ink, "bg": u["cursor"]},
        "lCursor": {"fg": ink, "bg": u["cursor"]},
        "CursorIM": {"fg": ink, "bg": u["cursor"]},
        "TermCursor": {"fg": ink, "bg": u["cursor"]},
        "CursorLine": {"bg": u["line"]},
        "CursorColumn": {"bg": u["line"]},
        "CursorLineNr": {"fg": u["line_nr_cur"], "bold": True},
        "LineNr": {"fg": u["line_nr"]},
        "SignColumn": {"fg": c.overlay0},
        "FoldColumn": {"fg": c.overlay0},
        "Folded": {"fg": c.overlay1, "bg": ref},
        "Directory": {"fg": c.yellow},
        "EndOfBuffer": {"fg": c.surface1},
        "NonText": {"fg": c.surface2},
        "Whitespace": {"fg": c.surface1},
        "SpecialKey": {"fg": c.surface2},
        "WinSeparator": {"fg": c.crust, "bg": c.crust},
        "VertSplit": link("WinSeparator"),
        "Visual": {"bg": u["selection"]},
        "VisualNOS": {"bg": u["selection"]},
        "Search": {"bg": u["search"]},
        "IncSearch": {"fg": u["search_cur_fg"], "bg": u["search_cur"], "bold": True},
        "CurSearch": link("IncSearch"),
        "Substitute": {"fg": ink, "bg": c.red_hi},
        "MatchParen": {"fg": u["bracket_fg"], "bg": u["bracket_bg"], "bold": True},
        "ModeMsg": {"fg": c.subtext1, "bold": True},
        "MsgArea": {"fg": c.text},
        "MsgSeparator": {"fg": c.crust, "bg": c.mantle},
        "MoreMsg": {"fg": c.green},
        "OkMsg": {"fg": c.green},
        "Question": {"fg": c.green},
        "ErrorMsg": {"fg": c.red_hi, "bold": True},
        "WarningMsg": {"fg": c.yellow},
        "StderrMsg": {"fg": c.red_hi},
        "NvimInternalError": {"fg": ink, "bg": c.red},
        "Title": {"fg": c.yellow, "bold": True},
        "Pmenu": {"fg": c.subtext1, "bg": paper},
        "PmenuSel": {"fg": c.text_hi, "bg": row, "bold": True},
        "PmenuSbar": {"bg": paper},
        "PmenuThumb": {"bg": solid("text@L5", f, "paper")},
        "PmenuKind": {"fg": c.sage, "bg": paper},
        "PmenuKindSel": {"fg": c.sage, "bg": row, "bold": True},
        "PmenuExtra": {"fg": c.overlay1, "bg": paper},
        "PmenuExtraSel": {"fg": c.overlay2, "bg": row},
        "PmenuMatch": {"fg": c.yellow, "bg": paper, "bold": True},
        "PmenuMatchSel": {"fg": c.yellow_hi if f.dark else c.yellow, "bg": row, "bold": True},
        "PmenuBorder": {"fg": edge, "bg": paper},
        "PmenuShadow": {"bg": shadow, "blend": 80},
        "PmenuShadowThrough": {"bg": shadow, "blend": 100},
        "ComplHint": {"fg": c.overlay0, "italic": True},
        "ComplHintMore": {"fg": c.overlay1},
        "PreInsert": {"fg": c.overlay0, "italic": True},
        "WildMenu": {"fg": c.text_hi, "bg": row},
        "QuickFixLine": {"bg": u["selection"], "bold": True},
        "StatusLine": {"fg": c.subtext1, "bg": c.mantle},
        "StatusLineNC": {"fg": c.overlay0, "bg": c.crust},
        "StatusLineTerm": link("StatusLine"),
        "StatusLineTermNC": link("StatusLineNC"),
        "TabLine": {"fg": c.overlay1, "bg": c.mantle},
        "TabLineFill": {"bg": c.mantle},
        "TabLineSel": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "WinBar": {"fg": c.subtext0},
        "WinBarNC": {"fg": c.overlay0},
        "SnippetTabstop": {"bg": ref},
        "SnippetTabstopActive": {"bg": u["selection"]},
        "SpellBad": {"sp": c.red_hi, "undercurl": True},
        "SpellCap": {"sp": c.yellow, "undercurl": True},
        "SpellLocal": {"sp": c.sage, "undercurl": True},
        "SpellRare": {"sp": c.clay, "undercurl": True},
        "RedrawDebugNormal": {"reverse": True},
        "RedrawDebugClear": {"bg": t["chg_emph"]},
        "RedrawDebugComposed": {"bg": t["add_emph"]},
        "RedrawDebugRecompose": {"bg": t["del_emph"]},
        # diffs: whole lines on the tint, changed words on the stronger tint, syntax kept on top
        "DiffAdd": {"bg": t["add"]},
        "DiffChange": {"bg": t["chg"]},
        "DiffDelete": {"fg": c.red_hi if f.dark else c.red, "bg": t["del"]},  # the filler lines
        "DiffText": {"bg": t["chg_emph"]},
        "DiffTextAdd": {"bg": t["add_emph"]},
        "Added": {"fg": c.green},
        "Changed": {"fg": c.yellow},
        "Removed": {"fg": c.red_hi},
        # legacy syntax groups
        "Comment": S(f, "comment"),
        "Constant": S(f, "constant"),
        "String": S(f, "string"),
        "Character": S(f, "string"),
        "Number": S(f, "number"),
        "Float": S(f, "number"),
        "Boolean": S(f, "boolean"),
        "Identifier": S(f, "variable"),
        "Function": S(f, "function"),
        "Statement": S(f, "keyword"),
        "Conditional": S(f, "keyword"),
        "Repeat": S(f, "keyword"),
        "Label": S(f, "decorator"),
        "Operator": S(f, "operator"),
        "Keyword": S(f, "keyword"),
        "Exception": S(f, "keyword"),
        "PreProc": {"fg": c.clay},
        "Include": S(f, "keyword"),
        "Define": {"fg": c.clay},
        "Macro": S(f, "decorator"),
        "PreCondit": {"fg": c.clay},
        "Type": S(f, "type"),
        "StorageClass": S(f, "storage"),
        "Structure": S(f, "type"),
        "Typedef": S(f, "type"),
        "Special": {"fg": c.clay},
        "SpecialChar": S(f, "string.escape"),
        "Tag": S(f, "tag"),
        "Delimiter": S(f, "punctuation"),
        "SpecialComment": {"fg": c.overlay2, "italic": True},
        "Debug": {"fg": c.red_hi},
        "Underlined": {"fg": c.denim, "underline": True},
        "Ignore": {"fg": c.overlay0},
        "Error": S(f, "invalid"),
        "Todo": {"fg": ink, "bg": c.yellow, "bold": True},
        "Bold": {"bold": True},
        "Italic": {"italic": True},
        # diagnostics
        "DiagnosticError": {"fg": u["error"]},
        "DiagnosticWarn": {"fg": u["warning"]},
        "DiagnosticInfo": {"fg": u["info"]},
        "DiagnosticHint": {"fg": u["hint"]},
        "DiagnosticOk": {"fg": c.green},
        "DiagnosticUnderlineError": {"sp": u["error"], "undercurl": True},
        "DiagnosticUnderlineWarn": {"sp": u["warning"], "undercurl": True},
        "DiagnosticUnderlineInfo": {"sp": u["info"], "undercurl": True},
        "DiagnosticUnderlineHint": {"sp": u["hint"], "undercurl": True},
        "DiagnosticUnderlineOk": {"sp": c.green, "undercurl": True},
        "DiagnosticVirtualTextError": {"fg": u["error"], "bg": u["error_bg"]},
        "DiagnosticVirtualTextWarn": {"fg": u["warning"], "bg": u["warning_bg"]},
        "DiagnosticVirtualTextInfo": {"fg": u["info"], "bg": u["info_bg"]},
        "DiagnosticVirtualTextHint": {"fg": u["hint"], "bg": u["hint_bg"]},
        "DiagnosticVirtualTextOk": {"fg": c.green, "bg": ok_bg},
        "DiagnosticDeprecated": {"sp": c.overlay1, "strikethrough": True},
        "DiagnosticUnnecessary": {"fg": c.overlay1},
        "LspReferenceText": {"bg": ref},
        "LspReferenceRead": {"bg": ref},
        "LspReferenceWrite": {"bg": solid("denim@18", f), "underline": True, "sp": c.denim},
        "LspReferenceTarget": {"bg": ref, "bold": True},
        "LspInlayHint": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "LspSignatureActiveParameter": {"fg": c.yellow_hi if f.dark else c.orange, "bold": True, "underline": True},
        "LspCodeLens": {"fg": c.overlay1},
        "LspCodeLensSeparator": {"fg": c.overlay0},
        "LspInfoBorder": {"fg": edge, "bg": paper},
    }
    g.update(treesitter(f))
    g.update(semantic_tokens(f))
    return g


def treesitter(f):
    c = f
    ink = ui(f)["ink"]
    g = {
        "@variable": S(f, "variable"),
        "@variable.builtin": S(f, "variable.builtin"),
        "@variable.parameter": S(f, "parameter"),
        "@variable.parameter.builtin": S(f, "variable.builtin"),
        "@variable.member": S(f, "property"),
        "@property": S(f, "property"),
        # JSON, YAML and TOML keys are gold, like the other editors' key rule
        "@property.json": S(f, "function"),
        "@property.jsonc": S(f, "function"),
        "@property.json5": S(f, "function"),
        "@property.yaml": S(f, "function"),
        "@property.toml": S(f, "function"),
        "@constant": S(f, "constant"),
        "@constant.builtin": S(f, "constant"),
        "@constant.macro": S(f, "decorator"),
        "@module": S(f, "namespace"),
        "@module.builtin": S(f, "namespace", italic=True),
        "@label": S(f, "decorator"),
        "@string": S(f, "string"),
        "@string.documentation": {"fg": c.green, "italic": True},
        "@string.escape": S(f, "string.escape"),
        "@string.regexp": S(f, "regexp"),
        "@string.special": {"fg": c.clay},
        "@string.special.symbol": {"fg": c.clay},
        "@string.special.url": {"fg": c.denim, "underline": True},
        "@string.special.path": {"fg": c.green},
        "@character": S(f, "string"),
        "@character.special": S(f, "string.escape"),
        "@character.printf": S(f, "string.escape"),
        "@boolean": S(f, "boolean"),
        "@number": S(f, "number"),
        "@number.float": S(f, "number"),
        "@type": S(f, "type"),
        "@type.builtin": S(f, "type.builtin"),
        "@type.definition": S(f, "type"),
        "@attribute": S(f, "decorator"),
        "@attribute.builtin": S(f, "decorator"),
        "@function": S(f, "function"),
        "@function.builtin": S(f, "function.builtin"),
        "@function.call": S(f, "function"),
        "@function.macro": S(f, "decorator"),
        "@function.method": S(f, "function"),
        "@function.method.call": S(f, "function"),
        "@constructor": S(f, "type"),
        "@operator": S(f, "operator"),
        "@keyword": S(f, "keyword"),
        "@keyword.coroutine": S(f, "keyword"),
        "@keyword.function": S(f, "keyword"),
        "@keyword.operator": S(f, "keyword"),
        "@keyword.import": S(f, "keyword"),
        "@keyword.type": S(f, "keyword"),
        "@keyword.modifier": S(f, "storage"),
        "@keyword.storage": S(f, "storage"),
        "@keyword.repeat": S(f, "keyword"),
        "@keyword.return": S(f, "keyword"),
        "@keyword.debug": S(f, "keyword"),
        "@keyword.exception": S(f, "keyword"),
        "@keyword.conditional": S(f, "keyword"),
        "@keyword.conditional.ternary": S(f, "operator"),
        "@keyword.directive": {"fg": c.clay},
        "@keyword.directive.define": {"fg": c.clay},
        "@punctuation": S(f, "punctuation"),
        "@punctuation.delimiter": S(f, "punctuation"),
        "@punctuation.bracket": S(f, "punctuation"),
        "@punctuation.special": {"fg": c.clay},
        "@comment": S(f, "comment"),
        "@comment.documentation": S(f, "comment"),
        "@comment.error": {"fg": ink, "bg": c.red_hi, "bold": True},
        "@comment.warning": {"fg": ink, "bg": c.yellow, "bold": True},
        "@comment.todo": link("Todo"),
        "@comment.note": {"fg": ink, "bg": c.sage, "bold": True},
        "@comment.hint": {"fg": ink, "bg": c.sage, "bold": True},
        "@comment.info": {"fg": ink, "bg": c.denim, "bold": True},
        "@none": {},
        "@markup": {},
        "@markup.strong": S(f, "strong"),
        "@markup.italic": S(f, "emphasis"),
        "@markup.strikethrough": {"fg": c.overlay1, "strikethrough": True},
        "@markup.underline": {"underline": True},
        "@markup.heading": S(f, "heading"),
        **{f"@markup.heading.{i + 1}": {"fg": getattr(c, r), "bold": True} for i, r in enumerate(HEADINGS)},
        # :help's ==== and ---- rules: hide the characters, draw a quiet rule under them
        "@markup.heading.1.delimiter.vimdoc": {"fg": c.base, "bg": c.base, "sp": c.overlay0,
                                               "underdouble": True, "nocombine": True},
        "@markup.heading.2.delimiter.vimdoc": {"fg": c.base, "bg": c.base, "sp": c.overlay0,
                                               "underline": True, "nocombine": True},
        "@markup.quote": S(f, "quote"),
        "@markup.math": {"fg": c.clay},
        "@markup.environment": {"fg": c.clay},
        "@markup.environment.name": S(f, "type"),
        "@markup.link": S(f, "link"),
        "@markup.link.label": S(f, "link"),
        "@markup.link.url": {"fg": c.denim, "underline": True},
        "@markup.raw": S(f, "code"),
        "@markup.raw.block": S(f, "code"),
        "@markup.list": {"fg": c.orange},
        "@markup.list.checked": {"fg": c.green},
        "@markup.list.unchecked": {"fg": c.overlay1},
        "@tag": S(f, "tag"),
        "@tag.builtin": S(f, "tag"),
        "@tag.attribute": S(f, "attribute"),
        "@tag.delimiter": S(f, "punctuation"),
        "@diff.plus": {"fg": c.green},
        "@diff.minus": {"fg": c.red_hi},
        "@diff.delta": {"fg": c.yellow},
    }
    # nvim-treesitter's names before the 0.10 rename, still used by some parsers and plugins
    legacy = {
        "@field": "@variable.member", "@parameter": "@variable.parameter", "@namespace": "@module",
        "@method": "@function.method", "@method.call": "@function.method.call", "@float": "@number.float",
        "@symbol": "@string.special.symbol", "@string.regex": "@string.regexp", "@storageclass": "@keyword.modifier",
        "@conditional": "@keyword.conditional", "@repeat": "@keyword.repeat", "@include": "@keyword.import",
        "@exception": "@keyword.exception", "@define": "@keyword.directive.define", "@preproc": "@keyword.directive",
        "@type.qualifier": "@keyword.modifier", "@text.title": "@markup.heading", "@text.literal": "@markup.raw",
        "@text.uri": "@markup.link.url", "@text.reference": "@markup.link", "@text.emphasis": "@markup.italic",
        "@text.strong": "@markup.strong", "@text.strike": "@markup.strikethrough", "@text.todo": "@comment.todo",
        "@text.note": "@comment.note", "@text.warning": "@comment.warning", "@text.danger": "@comment.error",
        "@text.diff.add": "@diff.plus", "@text.diff.delete": "@diff.minus", "@text.math": "@markup.math",
        "@text.quote": "@markup.quote",
    }
    g.update({k: link(v) for k, v in legacy.items()})
    return g


def semantic_tokens(f):
    """LSP semantic tokens: defer to Tree-sitter where it already knows better."""
    links = {
        "@lsp.type.boolean": "@boolean", "@lsp.type.builtinType": "@type.builtin", "@lsp.type.class": "@type",
        "@lsp.type.comment": "@comment", "@lsp.type.decorator": "@attribute", "@lsp.type.deriveHelper": "@attribute",
        "@lsp.type.enum": "@type", "@lsp.type.enumMember": "@constant", "@lsp.type.escapeSequence": "@string.escape",
        "@lsp.type.event": "@type", "@lsp.type.formatSpecifier": "@string.escape", "@lsp.type.function": "@function",
        "@lsp.type.generic": "@variable", "@lsp.type.interface": "@type", "@lsp.type.keyword": "@keyword",
        "@lsp.type.lifetime": "@label", "@lsp.type.macro": "@function.macro", "@lsp.type.method": "@function.method",
        "@lsp.type.modifier": "@keyword.modifier", "@lsp.type.namespace": "@module", "@lsp.type.number": "@number",
        "@lsp.type.operator": "@operator", "@lsp.type.parameter": "@variable.parameter",
        "@lsp.type.property": "@property", "@lsp.type.regexp": "@string.regexp",
        "@lsp.type.selfKeyword": "@variable.builtin", "@lsp.type.selfTypeKeyword": "@variable.builtin",
        "@lsp.type.string": "@string", "@lsp.type.struct": "@type", "@lsp.type.type": "@type",
        "@lsp.type.typeAlias": "@type.definition",
        "@lsp.typemod.class.defaultLibrary": "@type.builtin", "@lsp.typemod.enum.defaultLibrary": "@type.builtin",
        "@lsp.typemod.enumMember.defaultLibrary": "@constant.builtin",
        "@lsp.typemod.function.defaultLibrary": "@function.builtin",
        "@lsp.typemod.keyword.async": "@keyword.coroutine", "@lsp.typemod.keyword.injected": "@keyword",
        "@lsp.typemod.macro.defaultLibrary": "@function.builtin",
        "@lsp.typemod.method.defaultLibrary": "@function.builtin",
        "@lsp.typemod.operator.injected": "@operator", "@lsp.typemod.string.injected": "@string",
        "@lsp.typemod.struct.defaultLibrary": "@type.builtin", "@lsp.typemod.type.defaultLibrary": "@type.builtin",
        "@lsp.typemod.typeAlias.defaultLibrary": "@type.builtin",
        "@lsp.typemod.variable.callable": "@function", "@lsp.typemod.variable.defaultLibrary": "@variable.builtin",
        "@lsp.typemod.variable.injected": "@variable", "@lsp.typemod.variable.static": "@constant",
    }
    g = {k: link(v) for k, v in links.items()}
    g.update({
        "@lsp.type.variable": {},  # plain variables: let Tree-sitter's captures show
        "@lsp.type.typeParameter": {"fg": f.sage, "italic": True},
        "@lsp.type.unresolvedReference": {"sp": f.red_hi, "undercurl": True},
        "@lsp.mod.deprecated": {"strikethrough": True},
    })
    return g


# ── Groups from Vim's runtime syntax files (Neovim uses them without Tree-sitter) ──
def syntax_files(f):
    c = f
    ink = ui(f)["ink"]
    heading = {n: {"fg": getattr(c, r), "bold": True} for n, r in enumerate(HEADINGS, 1)}
    return {
        # diff and git: foreground only, since these color text, not lines
        "diffAdded": {"fg": c.green},
        "diffRemoved": {"fg": c.red_hi},
        "diffChanged": {"fg": c.yellow},
        "diffFile": {"fg": c.text_hi, "bold": True},
        "diffNewFile": {"fg": c.text_hi, "bold": True},
        "diffOldFile": {"fg": c.text_hi, "bold": True},
        "diffIndexLine": {"fg": c.overlay1},
        "diffLine": {"fg": c.denim},
        "diffSubname": {"fg": c.subtext0},
        "diffComment": S(f, "comment"),
        "gitcommitSummary": {"fg": c.text_hi},
        "gitcommitOverflow": {"fg": c.red_hi},
        "gitcommitBranch": {"fg": c.yellow, "bold": True},
        "gitcommitHeader": {"fg": c.subtext0},
        "gitcommitSelectedType": {"fg": c.green},
        "gitcommitSelectedFile": {"fg": c.green},
        "gitcommitDiscardedType": {"fg": c.red_hi},
        "gitcommitDiscardedFile": {"fg": c.red_hi},
        "gitcommitUntrackedFile": {"fg": c.overlay1},
        # markdown
        **{f"markdownH{n}": dict(spec) for n, spec in heading.items()},
        **{f"markdownH{n}Delimiter": link(f"markdownH{n}") for n in heading},
        "markdownHeadingDelimiter": {"fg": c.overlay2, "bold": True},
        "markdownCode": S(f, "code"),
        "markdownCodeBlock": S(f, "code"),
        "markdownCodeDelimiter": {"fg": c.overlay1},
        "markdownLinkText": S(f, "link"),
        "markdownUrl": {"fg": c.denim, "underline": True},
        "markdownLinkDelimiter": S(f, "punctuation"),
        "markdownLinkTextDelimiter": S(f, "punctuation"),
        "markdownBold": S(f, "strong"),
        "markdownItalic": S(f, "emphasis"),
        "markdownBoldItalic": {"fg": c.text_hi, "bold": True, "italic": True},
        "markdownStrike": {"fg": c.overlay1, "strikethrough": True},
        "markdownListMarker": {"fg": c.orange},
        "markdownOrderedListMarker": {"fg": c.orange},
        "markdownBlockquote": S(f, "quote"),
        "markdownRule": {"fg": c.overlay0},
        # html and xml
        "htmlTag": S(f, "punctuation"),
        "htmlEndTag": S(f, "punctuation"),
        "htmlTagName": S(f, "tag"),
        "htmlSpecialTagName": S(f, "tag"),
        "htmlArg": S(f, "attribute"),
        "htmlLink": {"fg": c.denim, "underline": True},
        "htmlBold": S(f, "strong"),
        "htmlItalic": S(f, "emphasis"),
        **{f"htmlH{n}": dict(spec) for n, spec in heading.items()},
        "xmlTag": S(f, "punctuation"),
        "xmlEndTag": S(f, "punctuation"),
        "xmlTagName": S(f, "tag"),
        "xmlAttrib": S(f, "attribute"),
        # help, vim, python, csv
        "helpHyperTextJump": S(f, "link"),
        "helpHyperTextEntry": {"fg": c.yellow},
        "helpHeader": S(f, "heading"),
        "helpHeadline": S(f, "heading"),
        "helpSectionDelim": {"fg": c.overlay0},
        "helpExample": S(f, "code"),
        "helpCommand": S(f, "code"),
        "helpOption": {"fg": c.sage},
        "helpSpecial": {"fg": c.clay},
        "helpNote": {"fg": ink, "bg": c.sage, "bold": True},
        "helpWarning": {"fg": ink, "bg": c.yellow, "bold": True},
        "helpDeprecated": {"fg": c.red_hi},
        "vimCommentTitle": {"fg": c.overlay2, "bold": True, "italic": True},
        "pythonBuiltin": S(f, "function.builtin"),
        "pythonDecorator": S(f, "decorator"),
        "pythonDecoratorName": S(f, "decorator"),
        "pythonExceptions": S(f, "type"),
        # csv.vim / rainbow_csv columns: the 70s stripe
        **{f"csvCol{i}": {"fg": col} for i, col in enumerate(stripe(f, 9))},
        "qfFileName": {"fg": c.yellow},
        "qfLineNr": {"fg": c.overlay0},
        "dirMark": {"fg": c.overlay1},  # :help dirvish
    }


def stripe(f, n):
    """The warm stripe used for rainbow brackets, csv columns and graph lanes."""
    base = [f.yellow, f.orange, f.sage, f.clay, f.green, f.red_hi, f.denim, f.subtext1, f.yellow_hi]
    return (base * (n // len(base) + 1))[:n]


def kinds(f):
    """LSP completion/symbol kind → color."""
    c = f
    return {
        "Text": c.text, "Method": c.yellow, "Function": c.yellow, "Constructor": c.sage,
        "Field": c.subtext1, "Variable": c.text, "Class": c.sage, "Interface": c.sage,
        "Module": c.subtext0, "Namespace": c.subtext0, "Package": c.subtext0, "Property": c.subtext1,
        "Unit": c.red_hi, "Value": c.red_hi, "Enum": c.sage, "Keyword": c.orange, "Snippet": c.clay,
        "Color": c.clay, "File": c.text, "Reference": c.denim, "Folder": c.yellow, "EnumMember": c.red_hi,
        "Constant": c.red_hi, "Struct": c.sage, "Event": c.clay, "Operator": c.overlay2,
        "TypeParameter": c.sage, "String": c.green, "Number": c.red_hi, "Boolean": c.red_hi,
        "Array": c.clay, "Object": c.sage, "Key": c.yellow, "Null": c.red_hi, "Parameter": c.subtext1,
        "StaticMethod": c.yellow, "TypeAlias": c.sage, "Macro": c.clay,
        "Copilot": c.green, "Codeium": c.green, "Supermaven": c.green, "TabNine": c.green,
    }


# ── Plugins for Vim and Neovim alike ──────────────────────────────────────────
def shared_plugins(f):
    """ALE, coc.nvim, vim-lsp, GitGutter, Signify, fugitive, NERDTree, Fern, Sneak and friends."""
    c, u, t = f, ui(f), tints(f)
    ink = u["ink"]
    g = {}
    # diagnostics: ALE, coc.nvim, vim-lsp, yegappan/lsp level names; color; virtual-text ground
    levels = [
        ("Error", "Error", "Error", "Error", u["error"], u["error_bg"]),
        ("Warning", "Warning", "Warning", "Warning", u["warning"], u["warning_bg"]),
        ("Info", "Info", "Information", "Info", u["info"], u["info_bg"]),
        (None, "Hint", "Hint", "Hint", u["hint"], u["hint_bg"]),
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
        "CocFloating": {"fg": c.text, "bg": u["paper"]},
        "CocFloatBorder": {"fg": u["edge"], "bg": u["paper"]},
        "CocMenuSel": {"fg": c.text_hi, "bg": u["row"], "bold": True},
        "CocSearch": {"fg": c.yellow, "bold": True},
        "CocPumSearch": {"fg": c.yellow, "bold": True},
        "CocHighlightText": {"bg": solid("text@L2", f)},
        "CocInlayHint": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "CocUnusedHighlight": {"fg": c.overlay1},
        "CocDeprecatedHighlight": {"strikethrough": True},
        "CocFadeOut": {"fg": c.overlay0},
        "lspReference": {"bg": solid("text@L2", f)},
        "lspInlayHintsType": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "lspInlayHintsParameter": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "LspInlayHintsType": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "LspInlayHintsParam": {"fg": c.overlay1, "bg": u["inlay_bg"], "italic": True},
        "LspSigActiveParameter": {"fg": c.yellow_hi if f.dark else c.orange, "bold": True, "underline": True},
        "LspPopup": {"fg": c.text, "bg": u["paper"]},
        "LspPopupBorder": {"fg": u["edge"], "bg": u["paper"]},
        # AI suggestions
        "CopilotSuggestion": {"fg": c.overlay0, "italic": True},
        "CopilotAnnotation": {"fg": c.overlay0, "italic": True},
        "CodeiumSuggestion": {"fg": c.overlay0, "italic": True},
        "SupermavenSuggestion": {"fg": c.overlay0, "italic": True},
        # git gutters: green added, gold changed, red removed, clay for changed-then-removed
        "GitGutterAdd": {"fg": c.green},
        "GitGutterChange": {"fg": c.yellow},
        "GitGutterDelete": {"fg": c.red_hi},
        "GitGutterChangeDelete": {"fg": c.clay},
        "GitGutterAddLineNr": {"fg": c.green},
        "GitGutterChangeLineNr": {"fg": c.yellow},
        "GitGutterDeleteLineNr": {"fg": c.red_hi},
        "GitGutterChangeDeleteLineNr": {"fg": c.clay},
        "GitGutterAddLine": {"bg": t["add"]},
        "GitGutterChangeLine": {"bg": t["chg"]},
        "GitGutterDeleteLine": {"bg": t["del"]},
        "GitGutterChangeDeleteLine": {"bg": t["chg"]},
        "GitGutterAddIntraLine": {"bg": t["add_emph"]},
        "GitGutterDeleteIntraLine": {"bg": t["del_emph"]},
        "SignifySignAdd": {"fg": c.green},
        "SignifySignChange": {"fg": c.yellow},
        "SignifySignDelete": {"fg": c.red_hi},
        "SignifySignDeleteFirstLine": {"fg": c.red_hi},
        "SignifySignChangeDelete": {"fg": c.clay},
        "SignifyLineAdd": {"bg": t["add"]},
        "SignifyLineChange": {"bg": t["chg"]},
        "SignifyLineDelete": {"bg": t["del"]},
        # fugitive
        "fugitiveHeading": S(f, "heading"),
        "fugitiveHeader": {"fg": c.orange, "bold": True},
        "fugitiveUntrackedHeading": S(f, "heading"),
        "fugitiveUnstagedHeading": S(f, "heading"),
        "fugitiveStagedHeading": S(f, "heading"),
        "fugitiveUntrackedModifier": {"fg": c.overlay1},
        "fugitiveUnstagedModifier": {"fg": c.yellow},
        "fugitiveStagedModifier": {"fg": c.green},
        "fugitiveHash": {"fg": c.overlay1},
        "fugitiveSymbolicRef": {"fg": c.yellow, "bold": True},
        "fugitiveCount": {"fg": c.orange},
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
        "FernMarkedLine": {"bg": u["selection"]},
        "FernMarkedText": {"fg": c.yellow},
        "netrwTreeBar": {"fg": c.surface1},
        "netrwClassify": {"fg": c.yellow},
        "netrwExe": {"fg": c.clay},
        "netrwSymLink": {"fg": c.denim},
        "netrwDir": {"fg": c.yellow},
        # icon colors from vim-fern's glyph-palette
        **{f"GlyphPalette{i}": {"fg": col} for i, col in
           zip(range(1, 10), [c.red_hi, c.green, c.yellow, c.denim, c.clay, c.sage, c.text, c.overlay1, c.red],
               strict=True)},
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
        "EasyMotionIncSearch": {"fg": u["search_cur_fg"], "bg": u["search_cur"]},
        "Sneak": {"fg": ink, "bg": c.orange, "bold": True},
        "SneakLabel": {"fg": ink, "bg": c.orange, "bold": True},
        "SneakLabelMask": {"fg": c.orange, "bg": c.orange},
        "SneakScope": {"bg": u["selection"]},
        "WhichKey": {"fg": c.yellow},
        "WhichKeyGroup": {"fg": c.orange},
        "WhichKeyDesc": {"fg": c.subtext1},
        "WhichKeySeperator": {"fg": c.overlay0},  # sic: vim-which-key's spelling
        "WhichKeySeparator": {"fg": c.overlay0},
        "WhichKeyFloating": {"fg": c.subtext1, "bg": u["paper"]},
        "StartifyHeader": {"fg": c.orange},
        "StartifySection": S(f, "heading"),
        "StartifyNumber": {"fg": c.yellow},
        "StartifyBracket": {"fg": c.overlay0},
        "StartifyFile": {"fg": c.subtext1},
        "StartifyPath": {"fg": c.overlay1},
        "StartifySlash": {"fg": c.overlay0},
        "StartifySpecial": {"fg": c.overlay1},
        "StartifyFooter": {"fg": c.overlay1, "italic": True},
        "IndentGuidesOdd": {"bg": f.mix("surface0", "base", 0.4)},
        "IndentGuidesEven": {"bg": f.mix("surface0", "base", 0.8)},
        "illuminatedWord": {"bg": solid("text@L2", f)},
        "illuminatedCurWord": {"bg": solid("text@L2", f)},
        "TagbarKind": {"fg": c.orange},
        "TagbarScope": {"fg": c.sage},
        "TagbarType": {"fg": c.sage},
        "TagbarSignature": {"fg": c.overlay1},
        "TagbarFoldIcon": {"fg": c.yellow},
        "TagbarHighlight": {"bg": u["selection"]},
        "UndotreeNode": {"fg": c.orange},
        "UndotreeNodeCurrent": {"fg": c.yellow, "bold": True},
        "UndotreeSeq": {"fg": c.clay},
        "UndotreeBranch": {"fg": c.overlay1},
        "UndotreeTimeStamp": {"fg": c.overlay1},
        "UndotreeSavedSmall": {"fg": c.green},
        "UndotreeSavedBig": {"fg": c.green, "bold": True},
        # luochen1990/rainbow (Vim) and nvim-ts-rainbow's rainbow1..7
        **{f"rainbow{i}": {"fg": col} for i, col in enumerate(stripe(f, 7), 1)},
    })
    return g


# ── Neovim (Lua) plugins ──────────────────────────────────────────────────────
def lua_plugins(f):
    c, u, t = f, ui(f), tints(f)
    ink = u["ink"]
    paper, edge, row = u["paper"], u["edge"], u["row"]
    ref = solid("text@L2", f)
    title = {"fg": ink, "bg": c.orange, "bold": True}

    def dim(col):  # staged hunks, unfocused marks
        return f.mix(col, "base", 0.55)

    g = {}
    for kind, col in kinds(f).items():
        for fam in ("CmpItemKind{}", "BlinkCmpKind{}", "NavicIcons{}", "LspKind{}", "Aerial{}Icon",
                    "DropBarKind{}", "NoiceCompletionItemKind{}"):
            g[fam.format(kind)] = {"fg": col}
    g.update({"CmpItemKindDefault": {"fg": c.subtext1}, "BlinkCmpKindDefault": {"fg": c.subtext1},
              "NoiceCompletionItemKindDefault": {"fg": c.subtext1}})
    icons = {"Grey": c.subtext0, "Purple": c.clay, "Blue": c.denim, "Azure": c.sage_hi, "Cyan": c.sage,
             "Green": c.green, "Yellow": c.yellow, "Orange": c.orange, "Red": c.red_hi}
    g.update({f"MiniIcons{k}": {"fg": v} for k, v in icons.items()})
    g.update({
        # nvim-cmp / blink.cmp
        "CmpItemAbbr": {"fg": c.subtext1},
        "CmpItemAbbrDeprecated": {"fg": c.overlay0, "strikethrough": True},
        "CmpItemAbbrMatch": {"fg": c.yellow, "bold": True},
        "CmpItemAbbrMatchFuzzy": {"fg": c.yellow},
        "CmpItemMenu": {"fg": c.overlay1, "italic": True},
        "CmpDocumentation": {"fg": c.text, "bg": paper},
        "CmpDocumentationBorder": {"fg": edge, "bg": paper},
        "CmpGhostText": {"fg": c.overlay0, "italic": True},
        "BlinkCmpMenu": link("Pmenu"),
        "BlinkCmpMenuSelection": link("PmenuSel"),
        "BlinkCmpMenuBorder": {"fg": edge, "bg": paper},
        "BlinkCmpLabel": {"fg": c.subtext1},
        "BlinkCmpLabelMatch": {"fg": c.yellow, "bold": True},
        "BlinkCmpLabelDeprecated": {"fg": c.overlay0, "strikethrough": True},
        "BlinkCmpLabelDetail": {"fg": c.overlay1},
        "BlinkCmpLabelDescription": {"fg": c.overlay1},
        "BlinkCmpSource": {"fg": c.overlay1},
        "BlinkCmpKind": {"fg": c.sage},
        "BlinkCmpScrollBarThumb": {"bg": solid("text@L5", f, "paper")},
        "BlinkCmpScrollBarGutter": {"bg": paper},
        "BlinkCmpDoc": {"fg": c.text, "bg": paper},
        "BlinkCmpDocBorder": {"fg": edge, "bg": paper},
        "BlinkCmpDocSeparator": {"fg": edge, "bg": paper},
        "BlinkCmpSignatureHelp": {"fg": c.text, "bg": paper},
        "BlinkCmpSignatureHelpBorder": {"fg": edge, "bg": paper},
        "BlinkCmpSignatureHelpActiveParameter": link("LspSignatureActiveParameter"),
        "BlinkCmpGhostText": {"fg": c.overlay0, "italic": True},
        "BlinkIndent": {"fg": solid("text@7", f)},
        "BlinkIndentScope": {"fg": solid("text@20", f)},
        **{f"BlinkIndent{n}": {"fg": col} for n, col in (("Red", c.red_hi), ("Orange", c.orange),
           ("Yellow", c.yellow), ("Green", c.green), ("Cyan", c.sage), ("Blue", c.denim), ("Violet", c.clay))},
        **{f"BlinkPairs{n}": {"fg": col} for n, col in (("Red", c.red_hi), ("Orange", c.orange),
           ("Yellow", c.yellow), ("Green", c.green), ("Cyan", c.sage), ("Blue", c.denim), ("Purple", c.clay))},
        "BlinkPairsMatchParen": link("MatchParen"),
        "BlinkPairsUnmatched": {"fg": c.red_hi, "bold": True},
        # gitsigns: signs, numbers, line and word tints, staged marks dimmed
        "GitSignsAdd": {"fg": c.green},
        "GitSignsChange": {"fg": c.yellow},
        "GitSignsDelete": {"fg": c.red_hi},
        "GitSignsChangedelete": {"fg": c.clay},
        "GitSignsTopdelete": {"fg": c.red_hi},
        "GitSignsUntracked": {"fg": c.overlay1},
        "GitSignsAddNr": {"fg": c.green},
        "GitSignsChangeNr": {"fg": c.yellow},
        "GitSignsDeleteNr": {"fg": c.red_hi},
        "GitSignsChangedeleteNr": {"fg": c.clay},
        "GitSignsTopdeleteNr": {"fg": c.red_hi},
        "GitSignsUntrackedNr": {"fg": c.overlay1},
        "GitSignsAddLn": {"bg": t["add"]},
        "GitSignsChangeLn": {"bg": t["chg"]},
        "GitSignsDeleteLn": {"bg": t["del"]},
        "GitSignsChangedeleteLn": {"bg": t["chg"]},
        "GitSignsUntrackedLn": {"bg": t["add_dim"]},
        "GitSignsAddInline": {"bg": t["add_emph"]},
        "GitSignsChangeInline": {"bg": t["chg_emph"]},
        "GitSignsDeleteInline": {"bg": t["del_emph"]},
        "GitSignsAddLnInline": {"bg": t["add_emph"]},
        "GitSignsChangeLnInline": {"bg": t["chg_emph"]},
        "GitSignsDeleteLnInline": {"bg": t["del_emph"]},
        "GitSignsAddPreview": link("DiffAdd"),
        "GitSignsDeletePreview": {"bg": t["del"]},
        "GitSignsDeleteVirtLn": {"bg": t["del"]},
        "GitSignsDeleteVirtLnInLine": {"bg": t["del_emph"]},
        "GitSignsVirtLnum": {"fg": c.overlay0, "bg": t["del"]},
        "GitSignsCurrentLineBlame": {"fg": c.overlay0, "italic": True},
        **{f"GitSignsStaged{k}": {"fg": dim(col)} for k, col in (("Add", c.green), ("Change", c.yellow),
           ("Delete", c.red_hi), ("Changedelete", c.clay), ("Topdelete", c.red_hi))},
        **{f"GitSignsStaged{k}Nr": {"fg": dim(col)} for k, col in (("Add", c.green), ("Change", c.yellow),
           ("Delete", c.red_hi), ("Changedelete", c.clay), ("Topdelete", c.red_hi))},
        # mini.diff
        "MiniDiffSignAdd": {"fg": c.green},
        "MiniDiffSignChange": {"fg": c.yellow},
        "MiniDiffSignDelete": {"fg": c.red_hi},
        "MiniDiffOverAdd": {"bg": t["add_emph"]},
        "MiniDiffOverChange": {"bg": t["chg_emph"]},
        "MiniDiffOverChangeBuf": {"bg": t["chg_emph"]},
        "MiniDiffOverContext": {"bg": t["chg"]},
        "MiniDiffOverContextBuf": {"bg": t["chg"]},
        "MiniDiffOverDelete": {"bg": t["del_emph"]},
        # diffview
        "DiffviewDiffAdd": {"bg": t["add"]},
        "DiffviewDiffAddAsDelete": {"bg": t["del"]},
        "DiffviewDiffChange": {"bg": t["chg"]},
        "DiffviewDiffText": {"bg": t["chg_emph"]},
        "DiffviewDiffDelete": {"fg": c.surface2, "bg": c.base},  # filler lines: quiet, not red
        "DiffviewDiffDeleteDim": {"fg": c.surface2},
        "DiffviewNormal": {"fg": c.subtext0, "bg": c.mantle},
        "DiffviewWinSeparator": {"fg": c.crust, "bg": c.crust},
        "DiffviewCursorLine": {"bg": row},
        "DiffviewFilePanelTitle": {"fg": c.orange, "bold": True},
        "DiffviewFilePanelCounter": {"fg": c.yellow},
        "DiffviewFilePanelFileName": {"fg": c.subtext1},
        "DiffviewFilePanelPath": {"fg": c.overlay1},
        "DiffviewFilePanelRootPath": {"fg": c.orange, "bold": True},
        "DiffviewFilePanelSelected": {"fg": c.yellow, "bold": True},
        "DiffviewFilePanelInsertions": {"fg": c.green},
        "DiffviewFilePanelDeletions": {"fg": c.red_hi},
        "DiffviewFilePanelConflicts": {"fg": c.orange},
        "DiffviewFolderName": {"fg": c.subtext1},
        "DiffviewFolderSign": {"fg": c.yellow},
        "DiffviewHash": {"fg": c.overlay1},
        "DiffviewReference": {"fg": c.yellow},
        "DiffviewReflogSelector": {"fg": c.clay},
        "DiffviewPrimary": {"fg": c.orange},
        "DiffviewSecondary": {"fg": c.sage},
        "DiffviewDim1": {"fg": c.overlay0},
        "DiffviewStatusAdded": {"fg": c.green},
        "DiffviewStatusUntracked": {"fg": c.green},
        "DiffviewStatusModified": {"fg": c.yellow},
        "DiffviewStatusRenamed": {"fg": c.sage},
        "DiffviewStatusCopied": {"fg": c.sage},
        "DiffviewStatusTypeChange": {"fg": c.yellow},
        "DiffviewStatusUnmerged": {"fg": c.orange},
        "DiffviewStatusUnknown": {"fg": c.red_hi},
        "DiffviewStatusDeleted": {"fg": c.red_hi},
        "DiffviewStatusBroken": {"fg": c.red_hi},
        "DiffviewStatusIgnored": {"fg": c.overlay0},
        # neogit
        "NeogitBranch": {"fg": c.yellow, "bold": True},
        "NeogitBranchHead": {"fg": c.yellow, "bold": True, "underline": True},
        "NeogitRemote": {"fg": c.sage, "bold": True},
        "NeogitObjectId": {"fg": c.overlay1},
        "NeogitStash": {"fg": c.clay},
        "NeogitFilePath": {"fg": c.denim},
        "NeogitSectionHeader": {"fg": c.orange, "bold": True},
        "NeogitTagName": {"fg": c.clay},
        "NeogitTagDistance": {"fg": c.overlay1},
        "NeogitHunkHeader": {"fg": c.subtext1, "bg": c.surface0},
        "NeogitHunkHeaderHighlight": {"fg": c.text_hi, "bg": c.surface1, "bold": True},
        "NeogitHunkHeaderCursor": {"fg": c.text_hi, "bg": c.surface1, "bold": True},
        "NeogitDiffHeader": {"fg": c.text_hi, "bg": c.mantle, "bold": True},
        "NeogitDiffHeaderHighlight": {"fg": c.orange, "bg": c.mantle, "bold": True},
        "NeogitDiffContext": {"bg": c.base},
        "NeogitDiffContextHighlight": {"bg": c.mantle},
        "NeogitDiffContextCursor": {"bg": u["line"]},
        "NeogitDiffAdd": {"fg": c.green, "bg": t["add_dim"]},
        "NeogitDiffAddHighlight": {"fg": c.green, "bg": t["add"]},
        "NeogitDiffAddCursor": {"fg": c.green, "bg": t["add_emph"]},
        "NeogitDiffAddInline": {"bg": t["add_emph"]},
        "NeogitDiffDelete": {"fg": c.red_hi, "bg": t["del_dim"]},
        "NeogitDiffDeleteHighlight": {"fg": c.red_hi, "bg": t["del"]},
        "NeogitDiffDeleteCursor": {"fg": c.red_hi, "bg": t["del_emph"]},
        "NeogitDiffDeleteInline": {"bg": t["del_emph"]},
        "NeogitChangeAdded": {"fg": c.green, "bold": True},
        "NeogitChangeNewFile": {"fg": c.green, "bold": True},
        "NeogitChangeModified": {"fg": c.yellow, "bold": True},
        "NeogitChangeUpdated": {"fg": c.yellow, "bold": True},
        "NeogitChangeRenamed": {"fg": c.sage, "bold": True},
        "NeogitChangeCopied": {"fg": c.sage, "bold": True},
        "NeogitChangeDeleted": {"fg": c.red_hi, "bold": True},
        "NeogitChangeBothModified": {"fg": c.orange, "bold": True},
        "NeogitPopupSectionTitle": {"fg": c.orange, "bold": True},
        "NeogitPopupActionKey": {"fg": c.yellow},
        "NeogitPopupOptionKey": {"fg": c.yellow},
        "NeogitPopupSwitchKey": {"fg": c.yellow},
        "NeogitPopupConfigKey": {"fg": c.yellow},
        "NeogitPopupBold": {"bold": True},
        "NeogitUnstagedchanges": {"fg": c.orange, "bold": True},
        "NeogitStagedchanges": {"fg": c.orange, "bold": True},
        "NeogitUntrackedfiles": {"fg": c.orange, "bold": True},
        "NeogitUnmergedchanges": {"fg": c.orange, "bold": True},
        "NeogitUnpulledchanges": {"fg": c.orange, "bold": True},
        "NeogitUnpushedchanges": {"fg": c.orange, "bold": True},
        "NeogitRecentcommits": {"fg": c.orange, "bold": True},
        "NeogitStashes": {"fg": c.orange, "bold": True},
        "NeogitRebasing": {"fg": c.orange, "bold": True},
        "NeogitRebaseDone": {"fg": c.green},
        "NeogitUnmergedInto": {"fg": c.sage, "bold": True},
        "NeogitUnpulledFrom": {"fg": c.sage, "bold": True},
        "NeogitUnpushedTo": {"fg": c.sage, "bold": True},
        "NeogitCommitViewHeader": {"fg": c.text_hi, "bg": c.surface0, "bold": True},
        "NeogitNotificationInfo": {"fg": c.denim},
        "NeogitNotificationWarning": {"fg": c.yellow},
        "NeogitNotificationError": {"fg": c.red_hi},
        "NeogitWinSeparator": {"fg": c.crust, "bg": c.crust},
        **{f"NeogitGraph{n}": {"fg": col} for n, col in (("Red", c.red_hi), ("Orange", c.orange),
           ("Yellow", c.yellow), ("Green", c.green), ("Cyan", c.sage), ("Blue", c.denim), ("Purple", c.clay),
           ("Gray", c.overlay1), ("White", c.text))},
        **{f"NeogitGraphBold{n}": {"fg": col, "bold": True} for n, col in (("Red", c.red_hi),
           ("Yellow", c.yellow), ("Green", c.green), ("Cyan", c.sage), ("Blue", c.denim), ("Purple", c.clay),
           ("Gray", c.overlay1), ("White", c.text))},
        # gitgraph.nvim
        **{f"GitGraphBranch{i}": {"fg": col} for i, col in enumerate(stripe(f, 5), 1)},
        "GitGraphHash": {"fg": c.overlay1},
        "GitGraphTimestamp": {"fg": c.overlay1},
        "GitGraphAuthor": {"fg": c.clay},
        "GitGraphBranchName": {"fg": c.yellow, "bold": True},
        "GitGraphBranchTag": {"fg": c.clay},
        "GitGraphBranchMsg": {"fg": c.text},
        # telescope
        "TelescopeNormal": {"fg": c.subtext1, "bg": paper},
        "TelescopeBorder": {"fg": edge, "bg": paper},
        "TelescopeTitle": title,
        "TelescopePromptNormal": {"fg": c.text, "bg": paper},
        "TelescopePromptBorder": {"fg": edge, "bg": paper},
        "TelescopePromptTitle": title,
        "TelescopePromptPrefix": {"fg": c.orange},
        "TelescopePromptCounter": {"fg": c.overlay1},
        "TelescopeResultsNormal": {"fg": c.subtext1, "bg": paper},
        "TelescopeResultsBorder": {"fg": edge, "bg": paper},
        "TelescopeResultsTitle": {"fg": c.overlay1, "bg": paper},
        "TelescopeResultsComment": {"fg": c.overlay1},
        "TelescopePreviewNormal": {"fg": c.text, "bg": paper},
        "TelescopePreviewBorder": {"fg": edge, "bg": paper},
        "TelescopePreviewTitle": {"fg": ink, "bg": c.green, "bold": True},
        "TelescopeSelection": {"fg": c.text_hi, "bg": row, "bold": True},
        "TelescopeSelectionCaret": {"fg": c.orange, "bg": row},
        "TelescopeMultiSelection": {"fg": c.yellow, "bg": u["selection"]},
        "TelescopeMultiIcon": {"fg": c.yellow},
        "TelescopeMatching": {"fg": c.yellow, "bold": True},
        # fzf-lua
        "FzfLuaNormal": {"fg": c.text, "bg": paper},
        "FzfLuaBorder": {"fg": edge, "bg": paper},
        "FzfLuaTitle": title,
        "FzfLuaPreviewTitle": {"fg": ink, "bg": c.green, "bold": True},
        "FzfLuaBackdrop": {"bg": resolve("shadow", f)},
        "FzfLuaCursor": {"fg": ink, "bg": u["cursor"]},
        "FzfLuaCursorLine": {"bg": row},
        "FzfLuaCursorLineNr": {"fg": u["line_nr_cur"], "bg": row},
        "FzfLuaSearch": {"bg": u["search"]},
        "FzfLuaHeaderBind": {"fg": c.yellow},
        "FzfLuaHeaderText": {"fg": c.overlay1},
        "FzfLuaPathColNr": {"fg": c.overlay1},
        "FzfLuaPathLineNr": {"fg": c.overlay1},
        "FzfLuaBufName": {"fg": c.subtext1},
        "FzfLuaBufNr": {"fg": c.overlay1},
        "FzfLuaBufFlagCur": {"fg": c.orange},
        "FzfLuaBufFlagAlt": {"fg": c.sage},
        "FzfLuaTabTitle": {"fg": c.orange, "bold": True},
        "FzfLuaTabMarker": {"fg": c.yellow},
        "FzfLuaLiveSym": {"fg": c.yellow},
        "FzfLuaDirPart": {"fg": c.overlay1},
        "FzfLuaFilePart": {"fg": c.text},
        "FzfLuaFzfNormal": {"fg": c.subtext1},
        "FzfLuaFzfCursorLine": {"fg": c.text_hi, "bg": row},
        "FzfLuaFzfMatch": {"fg": c.yellow, "bold": True},
        "FzfLuaFzfPointer": {"fg": c.orange},
        "FzfLuaFzfMarker": {"fg": c.yellow},
        "FzfLuaFzfPrompt": {"fg": c.orange},
        "FzfLuaFzfSeparator": {"fg": edge},
        "FzfLuaFzfBorder": {"fg": edge},
        "FzfLuaFzfGutter": {"bg": paper},
        "FzfLuaFzfInfo": {"fg": c.overlay1},
        "FzfLuaFzfHeader": {"fg": c.overlay1},
        "FzfLuaFzfQuery": {"fg": c.text},
        "FzfLuaFzfSpinner": {"fg": c.orange},
        # snacks.nvim
        "SnacksNormal": {"fg": c.text, "bg": paper},
        "SnacksNormalNC": {"fg": c.text, "bg": paper},
        "SnacksWinBar": {"fg": c.yellow, "bold": True},
        "SnacksWinBarNC": {"fg": c.overlay1},
        "SnacksBackdrop": {"bg": resolve("shadow", f)},
        "SnacksFooterKey": {"fg": ink, "bg": c.yellow},
        "SnacksFooterDesc": {"fg": c.subtext1, "bg": paper},
        "SnacksInputBorder": {"fg": edge, "bg": paper},
        "SnacksInputTitle": {"fg": c.orange, "bold": True},
        "SnacksInputIcon": {"fg": c.orange},
        "SnacksPicker": {"fg": c.text, "bg": paper},
        "SnacksPickerBorder": {"fg": edge, "bg": paper},
        "SnacksPickerTitle": title,
        "SnacksPickerBoxTitle": title,
        "SnacksPickerInputTitle": title,
        "SnacksPickerListTitle": {"fg": c.overlay1, "bg": paper},
        "SnacksPickerPreviewTitle": {"fg": ink, "bg": c.green, "bold": True},
        "SnacksPickerInput": {"fg": c.text, "bg": paper},
        "SnacksPickerInputBorder": {"fg": edge, "bg": paper},
        "SnacksPickerPrompt": {"fg": c.orange},
        "SnacksPickerMatch": {"fg": c.yellow, "bold": True},
        "SnacksPickerSelected": {"fg": c.yellow},
        "SnacksPickerCursorLine": {"bg": row},
        "SnacksPickerListCursorLine": {"bg": row},
        "SnacksPickerDir": {"fg": c.overlay1},
        "SnacksPickerFile": {"fg": c.text},
        "SnacksPickerTotals": {"fg": c.overlay1},
        "SnacksPickerToggle": {"fg": ink, "bg": c.sage},
        "SnacksPickerPickWin": {"fg": ink, "bg": c.orange, "bold": True},
        "SnacksPickerPickWinCurrent": {"fg": ink, "bg": c.yellow, "bold": True},
        "SnacksDashboardNormal": {"fg": c.text},
        "SnacksDashboardHeader": {"fg": c.orange},
        "SnacksDashboardTitle": {"fg": c.yellow, "bold": True},
        "SnacksDashboardKey": {"fg": c.yellow, "bold": True},
        "SnacksDashboardDesc": {"fg": c.subtext1},
        "SnacksDashboardIcon": {"fg": c.sage},
        "SnacksDashboardFile": {"fg": c.text},
        "SnacksDashboardDir": {"fg": c.overlay1},
        "SnacksDashboardSpecial": {"fg": c.clay},
        "SnacksDashboardFooter": {"fg": c.overlay1, "italic": True},
        "SnacksDashboardTerminal": {"fg": c.text},
        "SnacksIndent": {"fg": solid("text@7", f)},
        "SnacksIndentScope": {"fg": solid("text@20", f)},
        "SnacksIndentChunk": {"fg": solid("text@20", f)},
        **{f"SnacksIndent{i}": {"fg": f.mix(col, "base", 0.45)} for i, col in enumerate(stripe(f, 8), 1)},
        "SnacksZenIcon": {"fg": c.orange},
        "SnacksGhDiffHeader": {"fg": c.denim, "bg": c.mantle},
        "SnacksGhLabel": {"fg": c.clay},
        "SnacksDiffLabel": {"fg": c.clay},
        "SnacksProfilerIconInfo": {"fg": c.denim},
        "SnacksProfilerBadgeInfo": {"fg": c.denim, "bg": u["info_bg"]},
        "SnacksProfilerIconTrace": {"fg": c.clay},
        "SnacksProfilerBadgeTrace": {"fg": c.clay, "bg": u["line"]},
        # noice / nvim-notify / snacks notifier / mini.notify / fidget
        "NoiceCmdline": {"fg": c.text},
        "NoiceCmdlinePopup": {"fg": c.text, "bg": paper},
        "NoiceCmdlinePopupBorder": {"fg": c.orange, "bg": paper},
        "NoiceCmdlinePopupTitle": {"fg": c.orange, "bold": True},
        "NoiceCmdlineIcon": {"fg": c.orange},
        "NoiceCmdlinePopupBorderSearch": {"fg": c.yellow, "bg": paper},
        "NoiceCmdlinePopupTitleSearch": {"fg": c.yellow, "bold": True},
        "NoiceCmdlineIconSearch": {"fg": c.yellow},
        "NoiceCmdlinePopupBorderLua": {"fg": c.sage, "bg": paper},
        "NoiceCmdlinePopupTitleLua": {"fg": c.sage, "bold": True},
        "NoiceCmdlineIconLua": {"fg": c.sage},
        "NoiceCmdlinePopupBorderInput": {"fg": c.clay, "bg": paper},
        "NoiceCmdlinePopupTitleInput": {"fg": c.clay, "bold": True},
        "NoiceCmdlineIconInput": {"fg": c.clay},
        "NoiceConfirm": {"fg": c.text, "bg": paper},
        "NoiceConfirmBorder": {"fg": c.yellow, "bg": paper},
        "NoiceMini": {"fg": c.subtext1, "bg": c.mantle},
        "NoicePopup": {"fg": c.text, "bg": paper},
        "NoicePopupBorder": {"fg": edge, "bg": paper},
        "NoicePopupmenu": link("Pmenu"),
        "NoicePopupmenuSelected": link("PmenuSel"),
        "NoicePopupmenuBorder": {"fg": edge, "bg": paper},
        "NoicePopupmenuMatch": {"fg": c.yellow, "bold": True},
        "NoiceFormatProgressDone": {"fg": ink, "bg": c.orange},
        "NoiceFormatProgressTodo": {"fg": c.subtext1, "bg": c.surface1},
        "NoiceLspProgressTitle": {"fg": c.overlay1},
        "NoiceLspProgressClient": {"fg": c.orange},
        "NoiceLspProgressSpinner": {"fg": c.yellow},
        "NoiceVirtualText": {"fg": c.overlay1, "italic": True},
        "NotifyBackground": {"bg": paper},
        "FidgetTitle": {"fg": c.orange, "bold": True},
        "FidgetTask": {"fg": c.overlay1},
        "MiniNotifyNormal": {"fg": c.text, "bg": paper},
        "MiniNotifyBorder": {"fg": edge, "bg": paper},
        "MiniNotifyTitle": {"fg": c.yellow, "bold": True},
        # trouble
        "TroubleNormal": {"fg": c.subtext1, "bg": c.mantle},
        "TroubleNormalNC": {"fg": c.subtext1, "bg": c.mantle},
        "TroubleText": {"fg": c.subtext1},
        "TroubleCount": {"fg": c.orange, "bg": c.surface0},
        "TroubleCode": {"fg": c.overlay1},
        "TroubleSource": {"fg": c.overlay1},
        "TroublePos": {"fg": c.overlay0},
        "TroubleIndent": {"fg": c.surface2},
        "TroubleIndentFoldClosed": {"fg": c.overlay1},
        "TroubleFsCount": {"fg": c.orange},
        "TroubleDirectory": {"fg": c.yellow},
        "TroubleIconDirectory": {"fg": c.yellow},
        "TroubleFilename": {"fg": c.text},
        "TroublePreview": {"bg": u["selection"]},
        # flash / leap / hop
        "FlashLabel": {"fg": ink, "bg": c.orange, "bold": True},
        "FlashMatch": {"bg": u["search"]},
        "FlashCurrent": {"fg": u["search_cur_fg"], "bg": u["search_cur"]},
        "FlashBackdrop": {"fg": c.overlay0},
        "FlashPrompt": {"fg": c.text, "bg": c.mantle},
        "FlashPromptIcon": {"fg": c.orange, "bg": c.mantle},
        "LeapLabel": {"fg": c.orange, "bold": True},
        "LeapMatch": {"fg": c.yellow_hi if f.dark else c.yellow, "underline": True, "bold": True},
        "LeapBackdrop": {"fg": c.overlay0},
        "HopNextKey": {"fg": c.orange, "bold": True},
        "HopNextKey1": {"fg": c.yellow, "bold": True},
        "HopNextKey2": {"fg": c.clay},
        "HopUnmatched": {"fg": c.overlay0},
        # which-key
        "WhichKeyNormal": {"bg": paper},
        "WhichKeyBorder": {"fg": edge, "bg": paper},
        "WhichKeyTitle": {"fg": c.orange, "bg": paper, "bold": True},
        "WhichKeyValue": {"fg": c.overlay1},
        "WhichKeyIcon": {"fg": c.sage},
        **{f"WhichKeyIcon{n}": {"fg": col} for n, col in icons.items()},
        # neo-tree / nvim-tree
        "NeoTreeNormal": {"fg": c.subtext0, "bg": c.mantle},
        "NeoTreeNormalNC": {"fg": c.subtext0, "bg": c.mantle},
        "NeoTreeDirectoryName": {"fg": c.subtext1},
        "NeoTreeDirectoryIcon": {"fg": c.yellow},
        "NeoTreeRootName": {"fg": c.orange, "bold": True},
        "NeoTreeFileName": {"fg": c.subtext0},
        "NeoTreeFileNameOpened": {"fg": c.text_hi},
        "NeoTreeFileIcon": {"fg": c.subtext0},
        "NeoTreeSymbolicLinkTarget": {"fg": c.denim},
        "NeoTreeExpander": {"fg": c.overlay1},
        "NeoTreeIndentMarker": {"fg": c.surface1},
        "NeoTreeDimText": {"fg": c.overlay0},
        "NeoTreeFilterTerm": {"fg": c.yellow, "bold": True},
        "NeoTreeModified": {"fg": c.yellow},
        "NeoTreeGitAdded": {"fg": c.green},
        "NeoTreeGitModified": {"fg": c.yellow},
        "NeoTreeGitDeleted": {"fg": c.red_hi},
        "NeoTreeGitRenamed": {"fg": c.sage},
        "NeoTreeGitConflict": {"fg": c.orange, "bold": True},
        "NeoTreeGitUntracked": {"fg": c.green, "italic": True},
        "NeoTreeGitIgnored": {"fg": c.overlay0},
        "NeoTreeGitStaged": {"fg": c.green_hi},
        "NeoTreeGitUnstaged": {"fg": c.yellow},
        "NeoTreeTitleBar": {"fg": ink, "bg": c.orange},
        "NeoTreeFloatBorder": {"fg": edge, "bg": paper},
        "NeoTreeFloatTitle": {"fg": c.orange, "bg": paper, "bold": True},
        "NeoTreeCursorLine": {"bg": row},
        "NeoTreeWinSeparator": {"fg": c.crust, "bg": c.crust},
        "NeoTreeVertSplit": {"fg": c.crust, "bg": c.crust},
        "NeoTreeStatusLineNC": {"fg": c.mantle, "bg": c.mantle},
        "NeoTreeTabActive": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "NeoTreeTabInactive": {"fg": c.overlay1, "bg": c.mantle},
        "NeoTreeTabSeparatorActive": {"fg": c.base, "bg": c.base},
        "NeoTreeTabSeparatorInactive": {"fg": c.mantle, "bg": c.mantle},
        "NvimTreeNormal": {"fg": c.subtext0, "bg": c.mantle},
        "NvimTreeNormalNC": {"fg": c.subtext0, "bg": c.mantle},
        "NvimTreeFolderName": {"fg": c.subtext1},
        "NvimTreeOpenedFolderName": {"fg": c.text_hi},
        "NvimTreeEmptyFolderName": {"fg": c.overlay1},
        "NvimTreeFolderIcon": {"fg": c.yellow},
        "NvimTreeRootFolder": {"fg": c.orange, "bold": True},
        "NvimTreeIndentMarker": {"fg": c.surface1},
        "NvimTreeGitDirty": {"fg": c.yellow},
        "NvimTreeGitNew": {"fg": c.green},
        "NvimTreeGitDeleted": {"fg": c.red_hi},
        "NvimTreeGitStaged": {"fg": c.green_hi},
        "NvimTreeGitMerge": {"fg": c.orange},
        "NvimTreeGitRenamed": {"fg": c.sage},
        "NvimTreeGitIgnored": {"fg": c.overlay0},
        "NvimTreeSpecialFile": {"fg": c.clay, "underline": True},
        "NvimTreeImageFile": {"fg": c.clay},
        "NvimTreeSymlink": {"fg": c.denim},
        "NvimTreeCursorLine": {"bg": row},
        "NvimTreeWinSeparator": {"fg": c.crust, "bg": c.crust},
        "NvimTreeVertSplit": {"fg": c.crust, "bg": c.crust},
        # oil
        "OilDir": {"fg": c.yellow, "bold": True},
        "OilDirIcon": {"fg": c.yellow},
        "OilLink": {"fg": c.denim},
        "OilFile": {"fg": c.text},
        "OilCreate": {"fg": c.green},
        "OilDelete": {"fg": c.red_hi},
        "OilMove": {"fg": c.clay},
        "OilCopy": {"fg": c.sage},
        "OilChange": {"fg": c.yellow},
        # indent-blankline
        "IblIndent": {"fg": solid("text@7", f), "nocombine": True},
        "IblWhitespace": {"fg": solid("text@7", f), "nocombine": True},
        "IblScope": {"fg": solid("text@20", f), "nocombine": True},
        # render-markdown / markview / headlines
        **{f"RenderMarkdownH{i + 1}": {"fg": getattr(c, r), "bold": True} for i, r in enumerate(HEADINGS)},
        **{f"RenderMarkdownH{i + 1}Bg": {"bg": f.mix(r, "base", 0.14)} for i, r in enumerate(HEADINGS[:5])},
        "RenderMarkdownH6Bg": {"bg": u["line"]},
        "RenderMarkdownCode": {"bg": c.mantle},
        "RenderMarkdownCodeInline": {"fg": c.green, "bg": c.mantle},
        "RenderMarkdownCodeBorder": {"bg": c.crust if f.dark else c.surface0},
        "RenderMarkdownBullet": {"fg": c.orange},
        "RenderMarkdownQuote": {"fg": c.overlay1},
        "RenderMarkdownDash": {"fg": c.overlay0},
        "RenderMarkdownLink": {"fg": c.denim},
        "RenderMarkdownChecked": {"fg": c.green},
        "RenderMarkdownUnchecked": {"fg": c.overlay1},
        "RenderMarkdownTodo": {"fg": c.yellow},
        "RenderMarkdownTableHead": {"fg": c.yellow},
        "RenderMarkdownTableRow": {"fg": c.surface2},
        "RenderMarkdownTableFill": {"fg": c.surface2},
        "RenderMarkdownSuccess": {"fg": c.green},
        "RenderMarkdownInfo": {"fg": c.denim},
        "RenderMarkdownHint": {"fg": c.sage},
        "RenderMarkdownWarn": {"fg": c.yellow},
        "RenderMarkdownError": {"fg": c.red_hi},
        **{f"MarkviewPalette{i}": {"fg": getattr(c, r), "bg": f.mix(r, "base", 0.14)}
           for i, r in enumerate(("overlay1", *HEADINGS, "denim"))},
        **{f"MarkviewPalette{i}Fg": {"fg": getattr(c, r)} for i, r in enumerate(("overlay1", *HEADINGS, "denim"))},
        **{f"MarkviewPalette{i}Bg": {"bg": f.mix(r, "base", 0.14)}
           for i, r in enumerate(("overlay1", *HEADINGS, "denim"))},
        "MarkviewCode": {"bg": c.mantle},
        "MarkviewCodeInfo": {"fg": c.overlay1, "bg": c.mantle},
        "MarkviewCodeFg": {"fg": c.mantle},
        "MarkviewInlineCode": {"fg": c.green, "bg": c.mantle},
        "MarkviewHyperlink": {"fg": c.denim, "underline": True},
        "MarkviewTableHeader": {"fg": c.yellow, "bold": True},
        "MarkviewTableBorder": {"fg": c.surface2},
        "MarkviewBlockQuoteDefault": {"fg": c.overlay1},
        "MarkviewBlockQuoteNote": {"fg": c.denim},
        "MarkviewBlockQuoteOk": {"fg": c.green},
        "MarkviewBlockQuoteWarn": {"fg": c.yellow},
        "MarkviewBlockQuoteError": {"fg": c.red_hi},
        "MarkviewBlockQuoteSpecial": {"fg": c.clay},
        **{f"Headline{i + 1}": {"bg": f.mix(r, "base", 0.14)} for i, r in enumerate(HEADINGS)},
        "CodeBlock": {"bg": c.mantle},
        "Dash": {"fg": c.overlay0, "bold": True},
        # treesitter-context
        "TreesitterContext": {"bg": c.mantle},
        "TreesitterContextLineNumber": {"fg": c.orange, "bg": c.mantle},
        "TreesitterContextBottom": {"sp": c.surface1, "underline": True},
        "TreesitterContextSeparator": {"fg": c.surface1},
        # dashboards: alpha, dashboard-nvim, mini.starter
        "AlphaHeader": {"fg": c.orange},
        "AlphaHeaderLabel": {"fg": c.yellow},
        "AlphaButtons": {"fg": c.subtext1},
        "AlphaShortcut": {"fg": c.yellow},
        "AlphaFooter": {"fg": c.overlay1, "italic": True},
        "DashboardHeader": {"fg": c.orange},
        "DashboardCenter": {"fg": c.subtext1},
        "DashboardShortCut": {"fg": c.yellow},
        "DashboardShortCutIcon": {"fg": c.sage},
        "DashboardFooter": {"fg": c.overlay1, "italic": True},
        "DashboardKey": {"fg": c.yellow},
        "DashboardDesc": {"fg": c.subtext1},
        "DashboardIcon": {"fg": c.sage},
        "DashboardFiles": {"fg": c.text},
        "DashboardMruTitle": {"fg": c.orange, "bold": True},
        "DashboardMruIcon": {"fg": c.sage},
        "DashboardProjectTitle": {"fg": c.orange, "bold": True},
        "DashboardProjectTitleIcon": {"fg": c.orange},
        "DashboardProjectIcon": {"fg": c.sage},
        # lazy.nvim / mason
        "LazyNormal": {"fg": c.text, "bg": paper},
        "LazyH1": title,
        "LazyH2": {"fg": c.orange, "bold": True},
        "LazyButton": {"fg": c.subtext1, "bg": u["line"]},
        "LazyButtonActive": {"fg": ink, "bg": c.yellow, "bold": True},
        "LazyProgressDone": {"fg": c.orange},
        "LazyProgressTodo": {"fg": c.surface2},
        "LazySpecial": {"fg": c.yellow},
        "LazyProp": {"fg": c.overlay1},
        "LazyValue": {"fg": c.green},
        "LazyDimmed": {"fg": c.overlay0},
        "LazyComment": {"fg": c.overlay1, "italic": True},
        "LazyCommit": {"fg": c.overlay1},
        "LazyCommitType": {"fg": c.clay},
        "LazyCommitScope": {"fg": c.sage, "italic": True},
        "LazyReasonPlugin": {"fg": c.sage},
        "LazyReasonEvent": {"fg": c.yellow},
        "LazyReasonKeys": {"fg": c.orange},
        "LazyReasonCmd": {"fg": c.clay},
        "LazyReasonFt": {"fg": c.denim},
        "LazyReasonStart": {"fg": c.green},
        "LazyReasonSource": {"fg": c.subtext1},
        "LazyReasonRequire": {"fg": c.clay},
        "LazyReasonRuntime": {"fg": c.denim},
        "LazyReasonImport": {"fg": c.subtext1},
        "LazyUrl": {"fg": c.denim, "underline": True},
        "LazyTaskOutput": {"fg": c.text},
        "LazyTaskError": {"fg": c.red_hi},
        "MasonNormal": {"fg": c.text, "bg": paper},
        "MasonHeader": title,
        "MasonHeaderSecondary": {"fg": ink, "bg": c.sage, "bold": True},
        "MasonHeading": {"fg": c.orange, "bold": True},
        "MasonHighlight": {"fg": c.yellow},
        "MasonHighlightSecondary": {"fg": c.sage},
        "MasonHighlightBlock": {"fg": ink, "bg": c.yellow},
        "MasonHighlightBlockBold": {"fg": ink, "bg": c.yellow, "bold": True},
        "MasonHighlightBlockSecondary": {"fg": ink, "bg": c.sage},
        "MasonHighlightBlockBoldSecondary": {"fg": ink, "bg": c.sage, "bold": True},
        "MasonLink": {"fg": c.denim, "underline": True},
        "MasonMuted": {"fg": c.overlay1},
        "MasonMutedBlock": {"fg": c.subtext1, "bg": u["line"]},
        "MasonMutedBlockBold": {"fg": c.subtext1, "bg": u["line"], "bold": True},
        "MasonError": {"fg": c.red_hi},
        "MasonWarning": {"fg": c.yellow},
        # bufferline (applies when bufferline's `themable` is on, its default)
        "BufferLineFill": {"bg": c.crust},
        "BufferLineBackground": {"fg": c.overlay1, "bg": c.crust},
        "BufferLineBuffer": {"fg": c.overlay1, "bg": c.crust},
        "BufferLineBufferVisible": {"fg": c.subtext0, "bg": c.mantle},
        "BufferLineBufferSelected": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "BufferLineTab": {"fg": c.overlay1, "bg": c.crust},
        "BufferLineTabSelected": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "BufferLineTabClose": {"fg": c.overlay1, "bg": c.crust},
        "BufferLineIndicatorSelected": {"fg": c.orange, "bg": c.base},
        "BufferLineIndicatorVisible": {"fg": c.mantle, "bg": c.mantle},
        "BufferLineModified": {"fg": dim(c.yellow), "bg": c.crust},
        "BufferLineModifiedVisible": {"fg": c.yellow, "bg": c.mantle},
        "BufferLineModifiedSelected": {"fg": c.yellow, "bg": c.base},
        "BufferLineSeparator": {"fg": c.crust, "bg": c.crust},
        "BufferLineSeparatorVisible": {"fg": c.crust, "bg": c.mantle},
        "BufferLineSeparatorSelected": {"fg": c.crust, "bg": c.base},
        "BufferLineCloseButton": {"fg": c.overlay0, "bg": c.crust},
        "BufferLineCloseButtonVisible": {"fg": c.overlay1, "bg": c.mantle},
        "BufferLineCloseButtonSelected": {"fg": c.red_hi, "bg": c.base},
        "BufferLineDuplicate": {"fg": c.overlay0, "bg": c.crust, "italic": True},
        "BufferLineDuplicateSelected": {"fg": c.overlay1, "bg": c.base, "italic": True},
        "BufferLineDuplicateVisible": {"fg": c.overlay0, "bg": c.mantle, "italic": True},
        "BufferLinePick": {"fg": ink, "bg": c.orange, "bold": True},
        "BufferLinePickVisible": {"fg": ink, "bg": c.orange, "bold": True},
        "BufferLinePickSelected": {"fg": ink, "bg": c.yellow, "bold": True},
        "BufferLineOffsetSeparator": {"fg": c.crust, "bg": c.mantle},
        # rainbow-delimiters: the 70s stripe
        "RainbowDelimiterRed": {"fg": c.red_hi},
        "RainbowDelimiterOrange": {"fg": c.orange},
        "RainbowDelimiterYellow": {"fg": c.yellow},
        "RainbowDelimiterGreen": {"fg": c.green},
        "RainbowDelimiterCyan": {"fg": c.sage},
        "RainbowDelimiterBlue": {"fg": c.denim},
        "RainbowDelimiterViolet": {"fg": c.clay},
        # neotest
        "NeotestPassed": {"fg": c.green},
        "NeotestFailed": {"fg": c.red_hi},
        "NeotestRunning": {"fg": c.yellow},
        "NeotestSkipped": {"fg": c.denim},
        "NeotestUnknown": {"fg": c.overlay1},
        "NeotestWatching": {"fg": c.clay},
        "NeotestTest": {"fg": c.text},
        "NeotestNamespace": {"fg": c.sage},
        "NeotestFocused": {"bold": True, "underline": True},
        "NeotestFile": {"fg": c.subtext1},
        "NeotestDir": {"fg": c.yellow},
        "NeotestIndent": {"fg": c.surface2},
        "NeotestExpandMarker": {"fg": c.overlay1},
        "NeotestAdapterName": {"fg": c.orange, "bold": True},
        "NeotestWinSelect": {"fg": c.orange, "bold": True},
        "NeotestMarked": {"fg": c.yellow, "bold": True},
        "NeotestTarget": {"fg": c.orange},
        "NeotestBorder": {"fg": edge},
        # grug-far
        "GrugFarHelpHeader": {"fg": c.overlay1},
        "GrugFarHelpHeaderKey": {"fg": c.yellow},
        "GrugFarHelpWinActionKey": {"fg": c.yellow},
        "GrugFarHelpWinActionText": {"fg": c.subtext1},
        "GrugFarInputLabel": {"fg": c.orange, "bold": True},
        "GrugFarInputPlaceholder": {"fg": c.overlay0, "italic": True},
        "GrugFarResultsHeader": {"fg": c.orange, "bold": True},
        "GrugFarResultsStats": {"fg": c.overlay1},
        "GrugFarResultsPath": {"fg": c.denim},
        "GrugFarResultsLineNo": {"fg": c.overlay1},
        "GrugFarResultsLineColumn": {"fg": c.overlay0},
        "GrugFarResultsMatch": {"fg": u["search_cur_fg"], "bg": u["search_cur"]},
        "GrugFarResultsMatchAdded": {"bg": t["add_emph"]},
        "GrugFarResultsMatchRemoved": {"bg": t["del_emph"], "strikethrough": True},
        "GrugFarResultsChangeIndicator": {"fg": c.yellow},
        "GrugFarResultsAddIndicator": {"fg": c.green},
        "GrugFarResultsRemoveIndicator": {"fg": c.red_hi},
        # octo.nvim
        "OctoEditable": {"bg": c.mantle},
        "OctoNormalFront": {"fg": c.text},
        "OctoUser": {"fg": c.yellow},
        "OctoUserViewer": {"fg": ink, "bg": c.yellow},
        "OctoViewer": {"fg": ink, "bg": c.orange},
        "OctoIssueId": {"fg": c.overlay1},
        "OctoIssueTitle": {"fg": c.text_hi, "bold": True},
        "OctoDate": {"fg": c.overlay1},
        "OctoDetailsLabel": {"fg": c.orange, "bold": True},
        "OctoDetailsValue": {"fg": c.subtext1},
        "OctoMissingDetails": {"fg": c.overlay0},
        "OctoEmpty": {"fg": c.overlay0},
        "OctoTimelineItemHeading": {"fg": c.overlay1},
        "OctoSymbol": {"fg": c.overlay1},
        "OctoDirty": {"fg": c.yellow, "bold": True},
        "OctoCommentLine": {"bg": c.mantle},
        "OctoStatusColumn": {"fg": c.orange},
        "OctoFilePanelTitle": {"fg": c.orange, "bold": True},
        "OctoFilePanelCounter": {"fg": c.yellow},
        "OctoPullAdditions": {"fg": c.green},
        "OctoPullDeletions": {"fg": c.red_hi},
        "OctoPullModifications": {"fg": c.yellow},
        "OctoReviewDiffAddText": {"bg": t["add_emph"]},
        "OctoReviewDiffDeleteText": {"bg": t["del_emph"]},
        "OctoDiffHunkPosition": {"fg": c.denim},
        "OctoPassingTest": {"fg": c.green},
        "OctoFailingTest": {"fg": c.red_hi},
        "OctoReaction": {"fg": c.subtext1, "bg": u["line"]},
        "OctoReactionViewer": {"fg": c.text_hi, "bg": u["selection"]},
        "OctoBubble": {"fg": c.text, "bg": u["line"]},
        **{f"Octo{n}": {"fg": col} for n, col in (("Green", c.green), ("Red", c.red_hi), ("Purple", c.clay),
           ("Yellow", c.yellow), ("Blue", c.denim), ("Grey", c.overlay1))},
        **{f"Octo{n}Float": {"fg": col, "bg": paper} for n, col in (("Green", c.green), ("Red", c.red_hi),
           ("Purple", c.clay), ("Yellow", c.yellow), ("Blue", c.denim), ("Grey", c.overlay1))},
        **{f"OctoBubble{n}": {"fg": ink, "bg": col} for n, col in (("Green", c.green), ("Red", c.red_hi),
           ("Purple", c.clay), ("Yellow", c.yellow), ("Blue", c.denim), ("Grey", c.overlay1))},
        **{f"OctoBubbleDelimiter{n}": {"fg": col} for n, col in (("Green", c.green), ("Red", c.red_hi),
           ("Purple", c.clay), ("Yellow", c.yellow), ("Blue", c.denim), ("Grey", c.overlay1))},
        **{f"OctoState{n}": {"fg": col, "bold": True} for n, col in (("Open", c.green), ("Closed", c.red_hi),
           ("Merged", c.clay), ("Pending", c.yellow), ("Approved", c.green), ("ChangesRequested", c.red_hi),
           ("Commented", c.denim), ("Dismissed", c.overlay1))},
        **{f"OctoState{n}Float": {"fg": col, "bg": paper, "bold": True} for n, col in (("Open", c.green),
           ("Closed", c.red_hi), ("Merged", c.clay), ("Pending", c.yellow), ("Approved", c.green),
           ("ChangesRequested", c.red_hi), ("Commented", c.denim), ("Dismissed", c.overlay1))},
        "OctoStateSubmittedBubble": {"fg": ink, "bg": c.green},
        # yanky / fidget-adjacent / illuminate / cursorword
        "YankyPut": {"bg": u["search"]},
        "YankyYanked": {"bg": u["search"]},
        "IlluminatedWordText": {"bg": ref},
        "IlluminatedWordRead": {"bg": ref},
        "IlluminatedWordWrite": {"bg": ref, "underline": True, "sp": c.overlay1},
        # lspsaga
        "SagaNormal": {"fg": c.text, "bg": paper},
        "SagaBorder": {"fg": edge, "bg": paper},
        "SagaTitle": {"fg": c.orange, "bold": True},
        "SagaText": {"fg": c.text},
        "SagaSelect": {"fg": c.yellow, "bold": True},
        "SagaSearch": {"bg": u["search"]},
        "SagaCount": {"fg": c.overlay1},
        "SagaDetail": {"fg": c.overlay1, "italic": True},
        "SagaToggle": {"fg": c.green},
        "SagaBeacon": {"bg": u["search_cur"]},
        "SagaVirtLine": {"fg": c.surface2},
        "SagaSpinner": {"fg": c.orange, "bold": True},
        "SagaSpinnerTitle": {"fg": c.orange, "bold": True},
        "SagaFinderFname": {"fg": c.subtext0, "bold": True},
        "SagaFileName": {"fg": c.overlay2, "bold": True},
        "SagaFolderName": {"fg": c.overlay2, "bold": True},
        "SagaInCurrent": {"fg": c.orange},
        "SagaImpIcon": {"fg": c.clay},
        "SagaLightBulb": {"fg": c.yellow},
        "SagaWinbarSep": {"fg": c.overlay0},
        "ActionFix": {"fg": c.clay},
        "CodeActionText": {"fg": c.green},
        "CodeActionNumber": {"fg": c.clay},
        "RenameNormal": {"fg": c.text},
        "RenameMatch": {"bg": u["search"]},
        # avante
        "AvanteTitle": {"fg": ink, "bg": c.orange, "bold": True},
        "AvanteReversedTitle": {"fg": c.orange},
        "AvanteSubtitle": {"fg": ink, "bg": c.yellow},
        "AvanteReversedSubtitle": {"fg": c.yellow},
        "AvanteThirdTitle": {"fg": ink, "bg": c.sage},
        "AvanteReversedThirdTitle": {"fg": c.sage},
        "AvanteInlineHint": {"fg": c.overlay0, "italic": True},
        "AvantePopupHint": {"fg": c.overlay0},
        "AvanteAnnotation": {"fg": c.overlay0},
        "AvanteSuggestion": {"fg": c.overlay0, "italic": True},
        "AvanteConflictCurrent": {"bg": t["del"]},
        "AvanteConflictCurrentLabel": {"fg": c.red_hi, "bg": t["del_emph"], "bold": True},
        "AvanteConflictIncoming": {"bg": t["add"]},
        "AvanteConflictIncomingLabel": {"fg": c.green, "bg": t["add_emph"], "bold": True},
        "AvanteConflictAncestor": {"bg": t["chg"]},
        "AvanteConflictAncestorLabel": {"fg": c.yellow, "bg": t["chg_emph"], "bold": True},
        "AvanteToBeDeleted": {"bg": t["del"], "strikethrough": True},
        "AvanteSidebarWinSeparator": {"fg": c.crust, "bg": c.crust},
        "AvantePromptInput": {"fg": c.text, "bg": paper},
        "AvantePromptInputBorder": {"fg": edge, "bg": paper},
        # overseer
        "OverseerPENDING": {"fg": c.overlay1},
        "OverseerRUNNING": {"fg": c.yellow},
        "OverseerSUCCESS": {"fg": c.green},
        "OverseerCANCELED": {"fg": c.overlay2},
        "OverseerFAILURE": {"fg": c.red_hi},
        "OverseerDISPOSED": {"fg": c.overlay0},
        "OverseerTask": {"fg": c.text},
        "OverseerTaskBorder": {"fg": edge},
        "OverseerOutput": {"fg": c.text},
        "OverseerComponent": {"fg": c.clay},
        "OverseerField": {"fg": c.sage},
        # nvim-ufo, dropbar, navic, aerial, outline
        "UfoFoldedFg": {"fg": c.overlay1},
        "UfoFoldedBg": {"bg": ref},
        "UfoFoldedEllipsis": {"fg": c.overlay1, "bg": ref},
        "UfoCursorFoldedLine": {"bg": u["line"], "bold": True},
        "UfoPreviewWinBar": {"fg": c.overlay1, "bg": paper},
        "UfoPreviewCursorLine": {"bg": row},
        "DropBarIconUISeparator": {"fg": c.overlay0},
        "DropBarMenuHoverEntry": {"bg": row},
        "DropBarMenuHoverIcon": {"fg": c.orange, "bg": row},
        "DropBarMenuHoverSymbol": {"bold": True},
        "DropBarMenuCurrentContext": {"bg": row},
        **{f"DropBarKind{k}": {"fg": c.orange} for k in ("BreakStatement", "CaseStatement", "ContinueStatement",
           "DoStatement", "ElseStatement", "ForStatement", "IfStatement", "Repeat", "Statement",
           "SwitchStatement", "WhileStatement", "Specifier", "Declaration", "Delete")},
        **{f"DropBarKindMarkdownH{i + 1}": {"fg": getattr(c, r), "bold": True} for i, r in enumerate(HEADINGS)},
        "DropBarKindCall": {"fg": c.yellow},
        "DropBarKindIdentifier": {"fg": c.text},
        "DropBarKindList": {"fg": c.clay},
        "DropBarKindScope": {"fg": c.subtext0},
        "DropBarKindType": {"fg": c.sage},
        "DropBarKindDir": {"fg": c.yellow},
        "NavicText": {"fg": c.subtext0},
        "NavicSeparator": {"fg": c.overlay0},
        "AerialLine": {"bg": u["selection"]},
        "AerialNormal": {"fg": c.subtext1},
        "AerialGuide": {"fg": c.surface2},
        "OutlineCurrent": {"fg": c.orange, "bold": True},
        "OutlineGuides": {"fg": c.surface2},
        "OutlineFoldMarker": {"fg": c.overlay1},
        # dap / dap-ui
        "DapBreakpoint": {"fg": c.red_hi},
        "DapBreakpointCondition": {"fg": c.yellow},
        "DapBreakpointRejected": {"fg": c.overlay1},
        "DapLogPoint": {"fg": c.denim},
        "DapStopped": {"fg": c.yellow},
        "DapStoppedLine": {"bg": t["chg"]},
        "DapUIScope": {"fg": c.orange},
        "DapUIType": {"fg": c.sage},
        "DapUIValue": {"fg": c.text},
        "DapUIVariable": {"fg": c.subtext1},
        "DapUIModifiedValue": {"fg": c.orange, "bold": True},
        "DapUIDecoration": {"fg": c.overlay1},
        "DapUIThread": {"fg": c.green},
        "DapUIStoppedThread": {"fg": c.yellow},
        "DapUISource": {"fg": c.denim},
        "DapUILineNumber": {"fg": c.overlay1},
        "DapUIFloatBorder": {"fg": edge, "bg": paper},
        "DapUIWatchesEmpty": {"fg": c.overlay0},
        "DapUIWatchesValue": {"fg": c.green},
        "DapUIWatchesError": {"fg": c.red_hi},
        "DapUIBreakpointsPath": {"fg": c.denim},
        "DapUIBreakpointsInfo": {"fg": c.green},
        "DapUIBreakpointsCurrentLine": {"fg": c.yellow, "bold": True},
        "DapUIBreakpointsDisabledLine": {"fg": c.overlay0},
        "DapUIWinSelect": {"fg": c.orange, "bold": True},
        **{f"DapUI{n}": {"fg": col} for n, col in (("PlayPause", c.green), ("Restart", c.green),
           ("Stop", c.red_hi), ("StepOver", c.denim), ("StepInto", c.denim), ("StepBack", c.denim),
           ("StepOut", c.denim), ("Unavailable", c.overlay0))},
        **{f"DapUI{n}NC": {"fg": col} for n, col in (("PlayPause", c.green), ("Restart", c.green),
           ("Stop", c.red_hi), ("StepOver", c.denim), ("StepInto", c.denim), ("StepBack", c.denim),
           ("StepOut", c.denim), ("Unavailable", c.overlay0))},
        # harpoon, scrollbar, sidekick
        "HarpoonWindow": {"fg": c.text, "bg": paper},
        "HarpoonBorder": {"fg": edge, "bg": paper},
        "ScrollbarHandle": {"bg": solid("text@L3", f)},
        "ScrollbarSearch": {"fg": c.yellow},
        "ScrollbarSearchHandle": {"fg": c.yellow, "bg": solid("text@L3", f)},
        "ScrollbarError": {"fg": u["error"]},
        "ScrollbarErrorHandle": {"fg": u["error"], "bg": solid("text@L3", f)},
        "ScrollbarWarn": {"fg": u["warning"]},
        "ScrollbarWarnHandle": {"fg": u["warning"], "bg": solid("text@L3", f)},
        "ScrollbarInfo": {"fg": u["info"]},
        "ScrollbarInfoHandle": {"fg": u["info"], "bg": solid("text@L3", f)},
        "ScrollbarHint": {"fg": u["hint"]},
        "ScrollbarHintHandle": {"fg": u["hint"], "bg": solid("text@L3", f)},
        "ScrollbarMisc": {"fg": c.clay},
        "ScrollbarMiscHandle": {"fg": c.clay, "bg": solid("text@L3", f)},
        "SidekickDiffAdd": {"bg": t["add"]},
        "SidekickDiffDelete": {"bg": t["del"]},
        "SidekickDiffContext": {"bg": c.mantle},
        "SidekickSignAdd": {"fg": c.green},
        "SidekickSignChange": {"fg": c.yellow},
        "SidekickSignDelete": {"fg": c.red_hi},
    })
    # notification levels: nvim-notify and snacks.nvim's notifier
    levels = {"Error": c.red_hi, "Warn": c.yellow, "Info": c.denim, "Debug": c.overlay1, "Trace": c.clay}
    for level, col in levels.items():
        up = level.upper()
        g[f"Notify{up}Border"] = {"fg": col, "bg": paper}
        g[f"Notify{up}Icon"] = {"fg": col}
        g[f"Notify{up}Title"] = {"fg": col, "bold": True}
        g[f"Notify{up}Body"] = {"fg": c.text, "bg": paper}
        g[f"SnacksNotifier{level}"] = {"fg": c.text, "bg": paper}
        g[f"SnacksNotifierIcon{level}"] = {"fg": col}
        g[f"SnacksNotifierTitle{level}"] = {"fg": col, "bold": True}
        g[f"SnacksNotifierBorder{level}"] = {"fg": col, "bg": paper}
        g[f"SnacksNotifierFooter{level}"] = {"fg": col, "bg": paper}
    g.update(mini(f))
    return g


def mini(f):
    """mini.nvim, module by module (mini.icons and mini.diff are above)."""
    c, u = f, ui(f)
    ink = u["ink"]
    paper, edge, row = u["paper"], u["edge"], u["row"]

    def mode(col):
        return {"fg": ink, "bg": col, "bold": True}

    return {
        "MiniAnimateCursor": {"reverse": True, "nocombine": True},
        "MiniAnimateNormalFloat": {"fg": c.text, "bg": paper},
        "MiniClueBorder": {"fg": edge, "bg": paper},
        "MiniClueDescGroup": {"fg": c.orange},
        "MiniClueDescSingle": {"fg": c.subtext1},
        "MiniClueNextKey": {"fg": c.yellow, "bold": True},
        "MiniClueNextKeyWithPostkeys": {"fg": c.red_hi, "bold": True},
        "MiniClueSeparator": {"fg": c.overlay0},
        "MiniClueTitle": {"fg": c.orange, "bg": paper, "bold": True},
        "MiniCompletionActiveParameter": {"underline": True, "bold": True},
        "MiniCompletionInfoBorderOutdated": {"fg": c.red_hi, "bg": paper},
        "MiniCursorword": {"bg": solid("text@L2", f)},
        "MiniCursorwordCurrent": {"bg": solid("text@L2", f)},
        "MiniDepsChangeAdded": {"fg": c.green},
        "MiniDepsChangeRemoved": {"fg": c.red_hi},
        "MiniDepsHint": {"fg": c.sage},
        "MiniDepsInfo": {"fg": c.denim},
        "MiniDepsMsgBreaking": {"fg": c.yellow},
        "MiniDepsPlaceholder": {"fg": c.overlay0},
        "MiniDepsTitle": {"fg": c.orange, "bold": True},
        "MiniDepsTitleError": {"fg": ink, "bg": c.red_hi},
        "MiniDepsTitleSame": {"fg": c.overlay1},
        "MiniDepsTitleUpdate": {"fg": ink, "bg": c.green},
        "MiniFilesBorder": {"fg": edge, "bg": paper},
        "MiniFilesBorderModified": {"fg": c.yellow, "bg": paper},
        "MiniFilesCursorLine": {"bg": row},
        "MiniFilesDirectory": {"fg": c.yellow},
        "MiniFilesFile": {"fg": c.text},
        "MiniFilesNormal": {"fg": c.text, "bg": paper},
        "MiniFilesTitle": {"fg": c.overlay1, "bg": paper},
        "MiniFilesTitleFocused": {"fg": c.orange, "bg": paper, "bold": True},
        "MiniHipatternsFixme": {"fg": ink, "bg": c.red_hi, "bold": True},
        "MiniHipatternsHack": {"fg": ink, "bg": c.clay, "bold": True},
        "MiniHipatternsNote": {"fg": ink, "bg": c.sage, "bold": True},
        "MiniHipatternsTodo": {"fg": ink, "bg": c.yellow, "bold": True},
        "MiniIndentscopeSymbol": {"fg": solid("text@20", f), "nocombine": True},
        "MiniIndentscopeSymbolOff": {"fg": c.red_hi, "nocombine": True},
        "MiniJump": {"fg": ink, "bg": c.orange},
        "MiniJump2dDim": {"fg": c.overlay0},
        "MiniJump2dSpot": {"fg": c.orange, "bold": True, "nocombine": True},
        "MiniJump2dSpotAhead": {"fg": c.sage, "nocombine": True},
        "MiniJump2dSpotUnique": {"fg": c.yellow, "bold": True, "nocombine": True},
        "MiniMapNormal": {"fg": c.overlay1, "bg": c.mantle},
        "MiniMapSymbolCount": {"fg": c.clay},
        "MiniMapSymbolLine": {"fg": c.orange},
        "MiniMapSymbolView": {"fg": c.yellow},
        "MiniOperatorsExchangeFrom": {"bg": u["search"]},
        "MiniPickBorder": {"fg": edge, "bg": paper},
        "MiniPickBorderBusy": {"fg": c.yellow, "bg": paper},
        "MiniPickBorderText": {"fg": c.orange, "bg": paper, "bold": True},
        "MiniPickCursor": {"blend": 100, "nocombine": True},
        "MiniPickIconDirectory": {"fg": c.yellow},
        "MiniPickIconFile": {"fg": c.text},
        "MiniPickHeader": {"fg": c.orange, "bold": True},
        "MiniPickMatchCurrent": {"bg": row},
        "MiniPickMatchMarked": {"bg": u["selection"]},
        "MiniPickMatchRanges": {"fg": c.yellow, "bold": True},
        "MiniPickNormal": {"fg": c.subtext1, "bg": paper},
        "MiniPickPreviewLine": {"bg": row},
        "MiniPickPreviewRegion": {"bg": u["search"]},
        "MiniPickPrompt": {"fg": c.text, "bg": paper},
        "MiniPickPromptCaret": {"fg": u["cursor"], "bg": paper},
        "MiniPickPromptPrefix": {"fg": c.orange, "bg": paper},
        "MiniStarterCurrent": {"nocombine": True},
        "MiniStarterFooter": {"fg": c.overlay1, "italic": True},
        "MiniStarterHeader": {"fg": c.orange},
        "MiniStarterInactive": {"fg": c.overlay0},
        "MiniStarterItem": {"fg": c.text},
        "MiniStarterItemBullet": {"fg": c.overlay0},
        "MiniStarterItemPrefix": {"fg": c.yellow},
        "MiniStarterQuery": {"fg": c.yellow, "bold": True},
        "MiniStarterSection": {"fg": c.orange, "bold": True},
        "MiniStatuslineModeNormal": mode(c.orange),
        "MiniStatuslineModeInsert": mode(c.green),
        "MiniStatuslineModeVisual": mode(c.yellow),
        "MiniStatuslineModeReplace": mode(c.red_hi),
        "MiniStatuslineModeCommand": mode(c.sage),
        "MiniStatuslineModeOther": mode(c.clay),
        "MiniStatuslineDevinfo": {"fg": c.subtext1, "bg": c.surface1},
        "MiniStatuslineFilename": {"fg": c.subtext0, "bg": c.mantle},
        "MiniStatuslineFileinfo": {"fg": c.subtext1, "bg": c.surface1},
        "MiniStatuslineInactive": {"fg": c.overlay0, "bg": c.crust},
        "MiniSurround": {"fg": u["search_cur_fg"], "bg": u["search_cur"]},
        "MiniTablineCurrent": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "MiniTablineVisible": {"fg": c.subtext0, "bg": c.mantle},
        "MiniTablineHidden": {"fg": c.overlay1, "bg": c.crust},
        "MiniTablineModifiedCurrent": {"fg": c.yellow, "bg": c.base, "bold": True},
        "MiniTablineModifiedVisible": {"fg": c.yellow, "bg": c.mantle},
        "MiniTablineModifiedHidden": {"fg": f.mix("yellow", "crust", 0.7), "bg": c.crust},
        "MiniTablineFill": {"bg": c.crust},
        "MiniTablineTabpagesection": {"fg": ink, "bg": c.orange, "bold": True},
        "MiniTablineTrunc": {"fg": c.overlay1, "bg": c.crust},
        "MiniTestEmphasis": {"bold": True},
        "MiniTestFail": {"fg": c.red_hi, "bold": True},
        "MiniTestPass": {"fg": c.green, "bold": True},
        "MiniTrailspace": {"bg": c.red_hi},
    }


# ── lualine ──────────────────────────────────────────────────────────────────
def lualine_theme(f):
    """A lualine theme: route-bullet colored mode segments."""
    c = f
    ink = ui(f)["ink"]

    def mode(bg):
        return {"a": {"fg": ink, "bg": bg, "gui": "bold"}, "b": {"fg": c.subtext1, "bg": c.surface1},
                "c": {"fg": c.subtext0, "bg": c.mantle}}

    return {
        "normal": mode(c.orange), "insert": mode(c.green), "visual": mode(c.yellow),
        "replace": mode(c.red_hi), "command": mode(c.sage), "terminal": mode(c.clay),
        "inactive": {
            "a": {"fg": c.overlay1, "bg": c.crust}, "b": {"fg": c.overlay1, "bg": c.crust},
            "c": {"fg": c.overlay0, "bg": c.crust},
        },
    }


LUALINE_AUTO = """-- {header}
-- lualine's theme = "auto" loads the theme named like g:colors_name; this one
-- shows whichever flavor `colorscheme subway-seat` put on screen.
local ok, ss = pcall(require, "subway-seat")
local flavor = ok and ss.current or (vim.o.background == "light" and "enamel" or "walnut")
return require("lualine.themes.subway-seat-" .. flavor)
"""


# ── Lua ──────────────────────────────────────────────────────────────────────
def lua(v, indent=0):
    pad = "  " * indent
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return '"' + v + '"'
    if isinstance(v, dict):
        if not v:
            return "{}"
        inner = ",\n".join(f'{pad}  ["{k}"] = {lua(val, indent + 1)}' for k, val in v.items())
        return "{\n" + inner + ",\n" + pad + "}"
    if isinstance(v, (list, tuple)):
        return "{ " + ", ".join(lua(x) for x in v) + " }"
    raise TypeError(v)


def compact(d):
    """One group per line: { fg = "#…", bold = true }."""
    if not d:
        return "{}"
    return "{ " + ", ".join(f"{k} = {lua(val)}" for k, val in d.items()) + " }"


def all_groups(f):
    return {**groups(f), **syntax_files(f), **shared_plugins(f), **lua_plugins(f)}


# Applies `spec` as colorscheme `name`, without options; shared by the colors files
# when the plugin's lua/ folder isn't on 'runtimepath'.
APPLY = """vim.cmd("hi clear")
if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
vim.o.termguicolors = true
vim.g.colors_name = {name}
for group, hl in pairs(spec.groups) do vim.api.nvim_set_hl(0, group, hl) end
for i, color in ipairs(spec.ansi) do vim.g["terminal_color_" .. (i - 1)] = color end"""


def colors_flavor(f):
    """colors/subway-seat-<flavor>.lua: this flavor's groups, applied by the plugin or on their own."""
    name = f"{f.prefix}-{f.id}"
    body = "\n".join(f'    ["{g}"] = {compact(spec)},' for g, spec in all_groups(f).items())
    ansi = ", ".join(f'"{x}"' for x in f.ansi)
    bg = "dark" if f.dark else "light"
    return f"""-- {HEADER}
-- {f.name}: {f.blurb}
-- With the plugin's lua/ folder on 'runtimepath' this hands off to require("subway-seat")
-- (options, following 'background'); on its own it applies the groups below.

local spec = {{
  flavor = "{f.id}",
  background = "{bg}",
  ansi = {{ {ansi} }},
  groups = {{
{body}
  }},
}}

-- The plugin reads the groups from here: loadfile(this file)("subway-seat").
if ... == "subway-seat" then return spec end

if vim.api.nvim_get_runtime_file("lua/subway-seat/init.lua", false)[1] then
  return require("subway-seat").colorscheme("{name}")
end

-- On its own. A flip of 'background' re-runs this file; keep the flavor rather than fight it.
if vim.g.colors_name ~= "{name}" and vim.o.background ~= spec.background then
  vim.g.colors_name = nil -- so Neovim doesn't re-run the previous colorscheme for the new 'background'
  vim.o.background = spec.background
end
{APPLY.format(name=f'"{name}"')}
"""


def colors_auto():
    """colors/subway-seat.lua: Walnut on a dark 'background', Enamel on a light one."""
    return f"""-- {HEADER}
-- Subway Seat, following 'background': Walnut when it's dark, Enamel when it's light
-- (with the plugin, whatever `setup({{ background = {{ dark = …, light = … }} }})` names).
-- Neovim re-runs this file when 'background' changes, so flipping it flips the flavor.

if vim.api.nvim_get_runtime_file("lua/subway-seat/init.lua", false)[1] then
  return require("subway-seat").colorscheme("subway-seat")
end

-- On its own: read the flavor from its colors file next to this one.
local flavor = vim.o.background == "light" and "enamel" or "walnut"
local path = vim.api.nvim_get_runtime_file("colors/subway-seat-" .. flavor .. ".lua", false)[1]
if not path then
  error("subway-seat: colors/subway-seat-" .. flavor .. ".lua is missing; copy the whole colors/ folder")
end
local spec = assert(loadfile(path))("subway-seat")
{APPLY.format(name='"subway-seat"')}
"""


INIT = """-- {header}
-- Subway Seat for Neovim. `:colorscheme subway-seat` follows 'background';
-- `subway-seat-walnut`, `-tunnel` and `-enamel` pick one flavor. See :help subway-seat.
local M = {{}}

M.flavors = {{ {flavor_list} }}

-- Every flavor's file stem, and which of them are light. Both come from
-- palette.py, so a new family needs no change here.
M.prefix = {{ {prefix_map} }}
M.light = {{ {light_map} }}

M.config = {{
  -- The flavor `:colorscheme subway-seat` shows for each 'background'.
  background = {{ dark = "walnut", light = "enamel" }},
  -- Leave the editor and gutter backgrounds unset so the terminal shows through.
  transparent = false,
  -- Set false to drop every italic (comments, parameters, builtins …).
  italics = true,
  -- function(colors, flavor) return {{ GroupName = {{ fg = colors.orange }} }} end
  overrides = nil,
  -- Before 0.3: a fixed flavor for `:colorscheme subway-seat` ("auto" follows 'background').
  flavor = "auto",
}}

--- The flavor on screen ("walnut", "tunnel" or "enamel"), or nil before the first load.
M.current = nil

local default = {{ dark = "walnut", light = "enamel" }}
local shown = {{}} -- 'background' → the flavor last shown with it
local transparent = {{
  "Normal", "NormalNC", "SignColumn", "FoldColumn", "EndOfBuffer", "LineNr", "CursorLineNr",
  "StatusLine", "StatusLineNC", "TabLineFill", "WinBar", "WinBarNC",
  "NeoTreeNormal", "NeoTreeNormalNC", "NvimTreeNormal", "NvimTreeNormalNC", "TroubleNormal", "TroubleNormalNC",
}}

function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", M.config, opts or {{}})
end

--- The palette for a flavor (default: the one on screen), as role → "#RRGGBB".
function M.colors(flavor)
  return require("subway-seat.palette")[flavor or M.current or default[vim.o.background] or "walnut"]
end

local function is_light(flavor)
  return M.light[flavor] == true
end

-- A flavor's groups live in its colors file, which returns them when called with "subway-seat".
local function read(flavor)
  local file = "colors/subway-seat-" .. flavor .. ".lua"
  local path = vim.api.nvim_get_runtime_file(file, false)[1]
  if not path then
    error("subway-seat: " .. file .. " isn't on 'runtimepath'")
  end
  return assert(loadfile(path))("subway-seat")
end

local function apply(flavor, name, set_background)
  local spec = read(flavor)
  if set_background and vim.o.background ~= spec.background then
    -- Drop the name first, so Neovim doesn't re-run the previous colorscheme for the new 'background'.
    vim.g.colors_name = nil
    vim.o.background = spec.background
  end

  local groups = vim.deepcopy(spec.groups)
  if M.config.transparent then
    for _, group in ipairs(transparent) do
      if groups[group] then groups[group].bg = nil end
    end
  end
  if not M.config.italics then
    for _, hl in pairs(groups) do hl.italic = nil end
  end
  if type(M.config.overrides) == "function" then
    for group, hl in pairs(M.config.overrides(M.colors(flavor), flavor) or {{}}) do
      groups[group] = hl
    end
  end

  vim.cmd("hi clear")
  if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
  vim.o.termguicolors = true
  vim.g.colors_name = name
  for group, hl in pairs(groups) do
    vim.api.nvim_set_hl(0, group, hl)
  end
  for i, color in ipairs(spec.ansi) do
    vim.g["terminal_color_" .. (i - 1)] = color
  end
  M.current = flavor
  shown[vim.o.background] = flavor
end

local function follow(bg)
  return M.config.background[bg] or default[bg]
end

--- Entry point of the colors/ files. Neovim re-runs the current one when 'background'
--- changes; then the flavor follows 'background' instead of setting it back.
function M.colorscheme(name)
  local bg = vim.o.background
  local reloading = vim.g.colors_name == name and M.current ~= nil
  local flavor = name:match("^subway%-seat%-(%a+)$")
  if not flavor then -- "subway-seat"
    local fixed = M.config.flavor ~= "auto" and M.config.flavor or nil
    if fixed and (is_light(fixed) == (bg == "light") or not reloading) then
      return apply(fixed, name, true)
    end
    return apply(follow(bg), name, false)
  end
  if reloading and is_light(flavor) ~= (bg == "light") then
    local to = shown[bg] or follow(bg)
    return apply(to, "subway-seat-" .. to, false)
  end
  apply(flavor, name, true)
end

--- Load a flavor ("walnut", "tunnel", "enamel"), or follow 'background' when nil.
function M.load(flavor)
  M.colorscheme((flavor == nil or flavor == "auto") and "subway-seat" or ("subway-seat-" .. flavor))
end

return M
"""

DOC = """*subway-seat.txt*  A warm 1970s subway-car colorscheme          {version}

SUBWAY SEAT                                                      *subway-seat*

Walnut paneling, parchment text, harvest gold and burnt orange. Three flavors:

  subway-seat-walnut   the original dark
  subway-seat-tunnel   a deeper dark
  subway-seat-enamel   the light one

`:colorscheme subway-seat` follows 'background': Walnut when it's dark, Enamel
when it's light. Change 'background' and the flavor changes with it; that
also works after picking one flavor by name.

==============================================================================
SETUP                                                      *subway-seat-setup*

Call setup() before the colorscheme. Every option is optional:
>lua
    require("subway-seat").setup({{
      -- the flavor `subway-seat` shows for each 'background'
      background = {{ dark = "walnut", light = "enamel" }}, -- or dark = "tunnel"
      transparent = false, -- leave the editor background to the terminal
      italics = true,      -- false drops every italic
      overrides = function(colors, flavor)
        return {{ CursorLine = {{ bg = colors.surface1 }} }}
      end,
    }})
    vim.cmd.colorscheme("subway-seat")
<
==============================================================================
LUA API                                                      *subway-seat-api*

require("subway-seat").colors([{{flavor}}])                *subway-seat.colors()*
    The palette as role → "#RRGGBB" (`base`, `text`, `orange`, …), for the
    flavor on screen by default.

require("subway-seat").load([{{flavor}}])                    *subway-seat.load()*
    Load "walnut", "tunnel" or "enamel"; nil follows 'background'.

require("subway-seat").current                           *subway-seat.current*
    The flavor on screen.

==============================================================================
LUALINE                                                    *subway-seat-lualine*

lualine's default `theme = "auto"` picks the theme named like the
colorscheme. To name one: `subway-seat`, `subway-seat-walnut`,
`subway-seat-tunnel` or `subway-seat-enamel`.

==============================================================================
ON ITS OWN                                                  *subway-seat-files*

The files in colors/ also work without the lua/ folder: copy colors/ into
your config's colors/ folder. They carry the groups themselves; setup()
options need the lua/ folder.

 vim:tw=78:ts=8:ft=help:norl:
"""


def build(flavors):
    outs = []
    cfg = "~/.config/nvim"
    palette = {f.id: dict(f.colors) for f in flavors}
    ansi = {f.id: f.ansi for f in flavors}
    pal_lua = "-- " + HEADER + "\nlocal M = " + lua(palette) + "\nM.ansi = " + lua(ansi) + "\nreturn M\n"
    outs.append(Out("colors/subway-seat.lua", colors_auto(), dest=f"{cfg}/colors/subway-seat.lua", lang="lua"))
    for f in flavors:
        outs.append(Out(f"colors/{f.prefix}-{f.id}.lua", colors_flavor(f), flavor=f.id,
                        dest=f"{cfg}/colors/{f.prefix}-{f.id}.lua", lang="lua"))
    lua_list = ", ".join(f'"{f.id}"' for f in flavors)
    prefix_map = ", ".join(f'{f.id} = "{f.prefix}"' for f in flavors)
    light_map = ", ".join(f"{f.id} = true" for f in flavors if not f.dark)
    outs.append(Out("lua/subway-seat/init.lua",
                    INIT.format(header=HEADER, flavor_list=lua_list,
                                prefix_map=prefix_map, light_map=light_map),
                    dest=f"{cfg}/lua/subway-seat/init.lua", lang="lua"))
    outs.append(Out("lua/subway-seat/palette.lua", pal_lua, dest=f"{cfg}/lua/subway-seat/palette.lua", lang="lua"))
    themes = "lua/lualine/themes"
    outs.append(Out(f"{themes}/subway-seat.lua", LUALINE_AUTO.format(header=HEADER),
                    dest=f"{cfg}/{themes}/subway-seat.lua", lang="lua"))
    for f in flavors:
        body = "-- " + HEADER + "\nreturn " + lua(lualine_theme(f)) + "\n"
        outs.append(Out(f"{themes}/{f.prefix}-{f.id}.lua", body, flavor=f.id,
                        dest=f"{cfg}/{themes}/{f.prefix}-{f.id}.lua", lang="lua"))
        # the snake_case names from before 0.3
        alias = f"-- {HEADER}\nreturn require(\"lualine.themes.{f.prefix}-{f.id}\")\n"
        outs.append(Out(f"{themes}/{f.snake}.lua", alias, flavor=f.id, dest=f"{cfg}/{themes}/{f.snake}.lua",
                        lang="lua"))
    outs.append(Out("doc/subway-seat.txt", DOC.format(version=f"v{VERSION}"),
                    dest=f"{cfg}/doc/subway-seat.txt", lang="text"))
    return outs

