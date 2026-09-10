"""Neovim: a full colorscheme plugin (setup(), flavors, lualine themes)."""

from ports._lib import HEADER, Out, resolve, solid, tints

META = {
    "id": "nvim",
    "name": "Neovim",
    "category": "Editors",
    "homepage": "https://neovim.io",
    "enable": {"where": "init.lua", "code": 'vim.cmd.colorscheme("{slug}")', "lang": "lua"},
    "notes": "A plugin, not a single file: `setup({ flavor, transparent, italics, overrides })`, "
    "`colorscheme subway-seat` follows `background` (light → Enamel), lualine themes, and highlight "
    "groups for ~40 popular plugins. Install it with lazy.nvim: "
    '`{ "oddurs/subway-seat.nvim", lazy = false, priority = 1000 }`.',
}


def groups(f):
    c = f
    t = tints(f)
    cur = f.yellow if f.dark else f.orange
    # The same layering as the VS Code theme, flattened (Neovim has no alpha):
    # floats lifted onto paper with a hairline edge, washes of text for lines and selections.
    paper = resolve("paper", f)
    edge = solid("text@EDGE", f, "paper")
    line = solid("text@L1", f)
    ref = solid("text@L2", f)
    sel = solid("text@L4", f)
    pick = solid("text@L3", f, "paper")
    S = lambda role: {"fg": f.syntax(role)[0], **{k: True for k in f.syntax(role)[1]}}
    groups = {
        # editor UI
        "Normal": {"fg": c.text, "bg": c.base},
        "NormalNC": {"fg": c.text, "bg": c.base},
        "NormalFloat": {"fg": c.text, "bg": paper},
        "FloatBorder": {"fg": edge, "bg": paper},
        "FloatTitle": {"fg": c.yellow, "bg": paper, "bold": True},
        "ColorColumn": {"bg": line},
        "Conceal": {"fg": c.overlay0},
        "Cursor": {"fg": c.base, "bg": cur},
        "lCursor": {"fg": c.base, "bg": cur},
        "CursorIM": {"fg": c.base, "bg": cur},
        "TermCursor": {"fg": c.base, "bg": cur},
        "CursorLine": {"bg": line},
        "CursorColumn": {"bg": line},
        "CursorLineNr": {"fg": cur, "bold": True},
        "LineNr": {"fg": c.overlay0},
        "SignColumn": {"fg": c.overlay0},
        "FoldColumn": {"fg": c.overlay0},
        "Folded": {"fg": c.overlay1, "bg": ref},
        "Directory": {"fg": c.yellow},
        "EndOfBuffer": {"fg": c.surface1},
        "NonText": {"fg": c.surface2},
        "Whitespace": {"fg": c.surface1},
        "SpecialKey": {"fg": c.surface2},
        "WinSeparator": {"fg": c.crust, "bg": c.crust},
        "VertSplit": {"link": "WinSeparator"},
        "Visual": {"bg": sel},
        "VisualNOS": {"bg": sel},
        "Search": {"bg": t["search"]},
        "IncSearch": {"fg": c.crust if f.dark else c.base, "bg": c.orange, "bold": True},
        "CurSearch": {"link": "IncSearch"},
        "Substitute": {"fg": c.crust, "bg": c.red_hi},
        "MatchParen": {"fg": c.yellow_hi if f.dark else c.orange, "bg": ref, "bold": True},
        "ModeMsg": {"fg": c.subtext1, "bold": True},
        "MoreMsg": {"fg": c.green},
        "Question": {"fg": c.green},
        "ErrorMsg": {"fg": c.red_hi, "bold": True},
        "WarningMsg": {"fg": c.yellow},
        "Title": {"fg": c.yellow, "bold": True},
        "Pmenu": {"fg": c.subtext1, "bg": paper},
        "PmenuSel": {"fg": c.text_hi, "bg": pick, "bold": True},
        "PmenuSbar": {"bg": paper},
        "PmenuThumb": {"bg": solid("text@L5", f, "paper")},
        "PmenuKind": {"fg": c.sage, "bg": paper},
        "PmenuExtra": {"fg": c.overlay1, "bg": paper},
        "PmenuMatch": {"fg": c.yellow, "bg": paper, "bold": True},
        "PmenuMatchSel": {"fg": c.yellow_hi if f.dark else c.yellow, "bg": pick, "bold": True},
        "WildMenu": {"bg": c.surface1},
        "QuickFixLine": {"bg": c.surface1, "bold": True},
        "StatusLine": {"fg": c.subtext1, "bg": c.mantle},
        "StatusLineNC": {"fg": c.overlay0, "bg": c.crust},
        "TabLine": {"fg": c.overlay1, "bg": c.mantle},
        "TabLineFill": {"bg": c.mantle},
        "TabLineSel": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "WinBar": {"fg": c.subtext0},
        "WinBarNC": {"fg": c.overlay0},
        "SpellBad": {"sp": c.red_hi, "undercurl": True},
        "SpellCap": {"sp": c.yellow, "undercurl": True},
        "SpellLocal": {"sp": c.sage, "undercurl": True},
        "SpellRare": {"sp": c.clay, "undercurl": True},
        "DiffAdd": {"bg": t["add"]},
        "DiffChange": {"bg": t["chg"]},
        "DiffDelete": {"fg": c.red, "bg": t["del"]},
        "DiffText": {"bg": t["chg_emph"]},
        "Added": {"fg": c.green},
        "Changed": {"fg": c.yellow},
        "Removed": {"fg": c.red_hi},
        # legacy syntax groups
        "Comment": S("comment"),
        "Constant": S("constant"),
        "String": S("string"),
        "Character": S("string"),
        "Number": S("number"),
        "Float": S("number"),
        "Boolean": S("boolean"),
        "Identifier": S("variable"),
        "Function": S("function"),
        "Statement": S("keyword"),
        "Conditional": S("keyword"),
        "Repeat": S("keyword"),
        "Label": S("decorator"),
        "Operator": S("operator"),
        "Keyword": S("keyword"),
        "Exception": S("keyword"),
        "PreProc": {"fg": c.clay},
        "Include": S("keyword"),
        "Define": S("keyword"),
        "Macro": {"fg": c.clay},
        "PreCondit": {"fg": c.clay},
        "Type": S("type"),
        "StorageClass": S("storage"),
        "Structure": S("type"),
        "Typedef": S("type"),
        "Special": {"fg": c.clay},
        "SpecialChar": S("string.escape"),
        "Tag": S("tag"),
        "Delimiter": S("punctuation"),
        "SpecialComment": {"fg": c.overlay2, "italic": True},
        "Debug": {"fg": c.red_hi},
        "Underlined": {"fg": c.denim, "underline": True},
        "Error": {"fg": c.red_hi},
        "Todo": {"fg": c.crust, "bg": c.yellow, "bold": True},
        # diagnostics
        "DiagnosticError": {"fg": c.red_hi},
        "DiagnosticWarn": {"fg": c.yellow},
        "DiagnosticInfo": {"fg": c.denim},
        "DiagnosticHint": {"fg": c.sage},
        "DiagnosticOk": {"fg": c.green},
        "DiagnosticUnderlineError": {"sp": c.red_hi, "undercurl": True},
        "DiagnosticUnderlineWarn": {"sp": c.yellow, "undercurl": True},
        "DiagnosticUnderlineInfo": {"sp": c.denim, "undercurl": True},
        "DiagnosticUnderlineHint": {"sp": c.sage, "undercurl": True},
        "DiagnosticVirtualTextError": {"fg": c.red_hi, "bg": f.mix("red", "base", 0.12)},
        "DiagnosticVirtualTextWarn": {"fg": c.yellow, "bg": f.mix("yellow", "base", 0.1)},
        "DiagnosticVirtualTextInfo": {"fg": c.denim, "bg": f.mix("denim", "base", 0.1)},
        "DiagnosticVirtualTextHint": {"fg": c.sage, "bg": f.mix("sage", "base", 0.1)},
        "DiagnosticDeprecated": {"strikethrough": True},
        "DiagnosticUnnecessary": {"fg": c.overlay1},
        "LspReferenceText": {"bg": ref},
        "LspReferenceRead": {"bg": ref},
        "LspReferenceWrite": {"bg": solid("denim@18", f), "underline": True},
        "LspInlayHint": {"fg": c.overlay1, "bg": f.mix("surface0", "base", 0.6), "italic": True},
        "LspSignatureActiveParameter": {"fg": c.yellow_hi, "bold": True, "underline": True},
        "LspCodeLens": {"fg": c.overlay1},
        # treesitter
        "@variable": S("variable"),
        "@variable.builtin": S("variable.builtin"),
        "@variable.parameter": S("parameter"),
        "@variable.parameter.builtin": S("variable.builtin"),
        "@variable.member": S("property"),
        "@property": S("property"),
        "@constant": S("constant"),
        "@constant.builtin": S("constant"),
        "@constant.macro": {"fg": c.clay},
        "@module": S("namespace"),
        "@module.builtin": S("namespace"),
        "@label": S("decorator"),
        "@string": S("string"),
        "@string.documentation": {"fg": c.green, "italic": True},
        "@string.escape": S("string.escape"),
        "@string.regexp": S("regexp"),
        "@string.special": {"fg": c.clay},
        "@string.special.symbol": {"fg": c.clay},
        "@string.special.url": {"fg": c.denim, "underline": True},
        "@string.special.path": {"fg": c.green},
        "@character": S("string"),
        "@character.special": S("string.escape"),
        "@boolean": S("boolean"),
        "@number": S("number"),
        "@number.float": S("number"),
        "@type": S("type"),
        "@type.builtin": S("type.builtin"),
        "@type.definition": S("type"),
        "@attribute": S("decorator"),
        "@attribute.builtin": S("decorator"),
        "@function": S("function"),
        "@function.builtin": S("function.builtin"),
        "@function.call": S("function"),
        "@function.macro": {"fg": c.clay},
        "@function.method": S("function"),
        "@function.method.call": S("function"),
        "@constructor": S("type"),
        "@operator": S("operator"),
        "@keyword": S("keyword"),
        "@keyword.coroutine": S("keyword"),
        "@keyword.function": S("keyword"),
        "@keyword.operator": S("keyword"),
        "@keyword.import": S("keyword"),
        "@keyword.type": S("keyword"),
        "@keyword.modifier": S("keyword"),
        "@keyword.repeat": S("keyword"),
        "@keyword.return": S("keyword"),
        "@keyword.exception": S("keyword"),
        "@keyword.conditional": S("keyword"),
        "@keyword.directive": {"fg": c.clay},
        "@punctuation.delimiter": S("punctuation"),
        "@punctuation.bracket": S("punctuation"),
        "@punctuation.special": {"fg": c.clay},
        "@comment": S("comment"),
        "@comment.documentation": S("comment"),
        "@comment.error": {"fg": c.crust, "bg": c.red_hi, "bold": True},
        "@comment.warning": {"fg": c.crust, "bg": c.yellow, "bold": True},
        "@comment.todo": {"link": "Todo"},
        "@comment.note": {"fg": c.crust, "bg": c.sage, "bold": True},
        "@markup.strong": S("strong"),
        "@markup.italic": S("emphasis"),
        "@markup.strikethrough": {"strikethrough": True},
        "@markup.underline": {"underline": True},
        "@markup.heading": S("heading"),
        "@markup.heading.1": {"fg": c.orange, "bold": True},
        "@markup.heading.2": {"fg": c.yellow, "bold": True},
        "@markup.heading.3": {"fg": c.green, "bold": True},
        "@markup.heading.4": {"fg": c.sage, "bold": True},
        "@markup.heading.5": {"fg": c.clay, "bold": True},
        "@markup.heading.6": {"fg": c.subtext1, "bold": True},
        "@markup.quote": S("quote"),
        "@markup.math": {"fg": c.clay},
        "@markup.link": S("link"),
        "@markup.link.label": {"fg": c.sage},
        "@markup.link.url": {"fg": c.denim, "underline": True},
        "@markup.raw": S("code"),
        "@markup.list": {"fg": c.orange},
        "@markup.list.checked": {"fg": c.green},
        "@markup.list.unchecked": {"fg": c.overlay1},
        "@tag": S("tag"),
        "@tag.builtin": S("tag"),
        "@tag.attribute": S("attribute"),
        "@tag.delimiter": S("punctuation"),
        "@diff.plus": {"fg": c.green},
        "@diff.minus": {"fg": c.red_hi},
        "@diff.delta": {"fg": c.yellow},
        "@lsp.type.namespace": {"link": "@module"},
        "@lsp.type.typeParameter": {"fg": c.sage, "italic": True},
        "@lsp.type.enumMember": {"link": "@constant"},
        "@lsp.mod.deprecated": {"strikethrough": True},
        "@lsp.typemod.function.defaultLibrary": {"link": "@function.builtin"},
        "@lsp.typemod.variable.defaultLibrary": {"link": "@variable.builtin"},
        # plugins: gitsigns, telescope, neo-tree/nvim-tree, indent-blankline, which-key, mini, lazy
        "GitSignsAdd": {"fg": c.green},
        "GitSignsChange": {"fg": c.yellow},
        "GitSignsDelete": {"fg": c.red_hi},
        "TelescopeNormal": {"fg": c.subtext1, "bg": paper},
        "TelescopeBorder": {"fg": edge, "bg": paper},
        "TelescopeTitle": {"fg": c.crust, "bg": c.orange, "bold": True},
        "TelescopePromptPrefix": {"fg": c.orange},
        "TelescopeSelection": {"fg": c.text_hi, "bg": c.surface1, "bold": True},
        "TelescopeSelectionCaret": {"fg": c.orange, "bg": c.surface1},
        "TelescopeMatching": {"fg": c.yellow, "bold": True},
        "NeoTreeNormal": {"fg": c.subtext0, "bg": c.mantle},
        "NeoTreeNormalNC": {"fg": c.subtext0, "bg": c.mantle},
        "NeoTreeDirectoryName": {"fg": c.subtext1},
        "NeoTreeDirectoryIcon": {"fg": c.yellow},
        "NeoTreeRootName": {"fg": c.orange, "bold": True},
        "NeoTreeGitModified": {"fg": c.yellow},
        "NeoTreeGitUntracked": {"fg": c.green},
        "NvimTreeNormal": {"fg": c.subtext0, "bg": c.mantle},
        "NvimTreeFolderIcon": {"fg": c.yellow},
        "NvimTreeRootFolder": {"fg": c.orange, "bold": True},
        "IblIndent": {"fg": solid("text@7", f), "nocombine": True},
        "IblScope": {"fg": solid("text@20", f), "nocombine": True},
        "MiniIndentscopeSymbol": {"fg": c.surface2},
        "WhichKey": {"fg": c.yellow},
        "WhichKeyGroup": {"fg": c.orange},
        "WhichKeyDesc": {"fg": c.subtext1},
        "WhichKeySeparator": {"fg": c.overlay0},
        "LazyH1": {"fg": c.crust, "bg": c.orange, "bold": True},
        "LazyButtonActive": {"fg": c.crust, "bg": c.yellow, "bold": True},
        "BlinkCmpMenu": {"link": "Pmenu"},
        "BlinkCmpMenuSelection": {"link": "PmenuSel"},
        "BlinkCmpLabelMatch": {"fg": c.yellow, "bold": True},
    }
    return groups


def plugin_groups(f):
    """Highlight groups for popular plugins, beyond what groups() covers."""
    c = f
    t = tints(f)
    float_bg = resolve("paper", f)
    kinds = {
        "Text": c.text, "Method": c.yellow, "Function": c.yellow, "Constructor": c.sage,
        "Field": c.subtext1, "Variable": c.text, "Class": c.sage, "Interface": c.sage,
        "Module": c.subtext0, "Property": c.subtext1, "Unit": c.red_hi, "Value": c.red_hi,
        "Enum": c.sage, "Keyword": c.orange, "Snippet": c.clay, "Color": c.clay, "File": c.text,
        "Reference": c.denim, "Folder": c.yellow, "EnumMember": c.red_hi, "Constant": c.red_hi,
        "Struct": c.sage, "Event": c.clay, "Operator": c.overlay2, "TypeParameter": c.sage,
        "Copilot": c.green, "Codeium": c.green, "Supermaven": c.green,
    }
    g = {}
    for kind, col in kinds.items():
        g[f"CmpItemKind{kind}"] = {"fg": col}
        g[f"BlinkCmpKind{kind}"] = {"fg": col}
        g[f"NavicIcons{kind}"] = {"fg": col}
    g.update({
        # nvim-cmp / blink.cmp
        "CmpItemAbbr": {"fg": c.subtext1},
        "CmpItemAbbrDeprecated": {"fg": c.overlay0, "strikethrough": True},
        "CmpItemAbbrMatch": {"fg": c.yellow, "bold": True},
        "CmpItemAbbrMatchFuzzy": {"fg": c.yellow},
        "CmpItemMenu": {"fg": c.overlay1, "italic": True},
        "BlinkCmpMenuBorder": {"fg": c.surface2, "bg": float_bg},
        "BlinkCmpDoc": {"fg": c.text, "bg": float_bg},
        "BlinkCmpDocBorder": {"fg": c.surface2, "bg": float_bg},
        "BlinkCmpSignatureHelp": {"fg": c.text, "bg": float_bg},
        "BlinkCmpSignatureHelpBorder": {"fg": c.surface2, "bg": float_bg},
        "BlinkCmpGhostText": {"fg": c.overlay0, "italic": True},
        # gitsigns (more)
        "GitSignsAddNr": {"fg": c.green},
        "GitSignsChangeNr": {"fg": c.yellow},
        "GitSignsDeleteNr": {"fg": c.red_hi},
        "GitSignsAddLn": {"bg": t["add"]},
        "GitSignsChangeLn": {"bg": t["chg"]},
        "GitSignsDeleteLn": {"bg": t["del"]},
        "GitSignsCurrentLineBlame": {"fg": c.overlay0, "italic": True},
        "GitSignsAddInline": {"bg": t["add_emph"]},
        "GitSignsDeleteInline": {"bg": t["del_emph"]},
        "GitSignsChangeInline": {"bg": t["chg_emph"]},
        # diffview / neogit
        "DiffviewFilePanelTitle": {"fg": c.orange, "bold": True},
        "DiffviewFilePanelCounter": {"fg": c.yellow},
        "DiffviewNormal": {"fg": c.subtext0, "bg": c.mantle},
        "NeogitBranch": {"fg": c.yellow, "bold": True},
        "NeogitRemote": {"fg": c.sage, "bold": True},
        "NeogitHunkHeader": {"fg": c.subtext1, "bg": c.surface0},
        "NeogitHunkHeaderHighlight": {"fg": c.text_hi, "bg": c.surface1, "bold": True},
        "NeogitDiffAddHighlight": {"fg": c.green, "bg": t["add"]},
        "NeogitDiffDeleteHighlight": {"fg": c.red_hi, "bg": t["del"]},
        "NeogitDiffContextHighlight": {"bg": c.mantle},
        # telescope (more) / fzf-lua / snacks picker
        "TelescopePromptNormal": {"fg": c.text, "bg": c.surface0},
        "TelescopePromptBorder": {"fg": c.surface0, "bg": c.surface0},
        "TelescopePromptTitle": {"fg": c.crust, "bg": c.orange, "bold": True},
        "TelescopePreviewTitle": {"fg": c.crust, "bg": c.green, "bold": True},
        "TelescopeResultsTitle": {"fg": c.mantle, "bg": c.mantle},
        "TelescopeResultsNormal": {"fg": c.subtext1, "bg": float_bg},
        "TelescopeResultsBorder": {"fg": float_bg, "bg": float_bg},
        "TelescopePreviewBorder": {"fg": float_bg, "bg": float_bg},
        "FzfLuaNormal": {"fg": c.text, "bg": float_bg},
        "FzfLuaBorder": {"fg": c.surface2, "bg": float_bg},
        "FzfLuaTitle": {"fg": c.crust, "bg": c.orange, "bold": True},
        "FzfLuaCursorLine": {"bg": c.surface1},
        "FzfLuaFzfMatch": {"fg": c.yellow, "bold": True},
        "SnacksPickerMatch": {"fg": c.yellow, "bold": True},
        "SnacksPickerDir": {"fg": c.overlay1},
        "SnacksPickerTitle": {"fg": c.crust, "bg": c.orange, "bold": True},
        "SnacksPickerBorder": {"fg": c.surface2, "bg": float_bg},
        "SnacksDashboardHeader": {"fg": c.orange},
        "SnacksDashboardKey": {"fg": c.yellow, "bold": True},
        "SnacksDashboardDesc": {"fg": c.subtext1},
        "SnacksDashboardIcon": {"fg": c.sage},
        "SnacksDashboardFooter": {"fg": c.overlay1, "italic": True},
        "SnacksIndent": {"fg": c.surface0},
        "SnacksIndentScope": {"fg": c.surface2},
        "SnacksNotifierInfo": {"fg": c.denim},
        "SnacksNotifierWarn": {"fg": c.yellow},
        "SnacksNotifierError": {"fg": c.red_hi},
        # noice / notify
        "NoiceCmdlinePopup": {"fg": c.text, "bg": float_bg},
        "NoiceCmdlinePopupBorder": {"fg": c.orange, "bg": float_bg},
        "NoiceCmdlinePopupTitle": {"fg": c.orange, "bold": True},
        "NoiceCmdlineIcon": {"fg": c.orange},
        "NoiceCmdlinePopupBorderSearch": {"fg": c.yellow, "bg": float_bg},
        "NoiceCmdlineIconSearch": {"fg": c.yellow},
        "NoiceConfirmBorder": {"fg": c.yellow, "bg": float_bg},
        "NotifyBackground": {"bg": float_bg},
        "NotifyERRORBorder": {"fg": c.red, "bg": float_bg},
        "NotifyWARNBorder": {"fg": c.yellow, "bg": float_bg},
        "NotifyINFOBorder": {"fg": c.denim, "bg": float_bg},
        "NotifyDEBUGBorder": {"fg": c.overlay0, "bg": float_bg},
        "NotifyTRACEBorder": {"fg": c.clay, "bg": float_bg},
        "NotifyERRORIcon": {"fg": c.red_hi}, "NotifyERRORTitle": {"fg": c.red_hi, "bold": True},
        "NotifyWARNIcon": {"fg": c.yellow}, "NotifyWARNTitle": {"fg": c.yellow, "bold": True},
        "NotifyINFOIcon": {"fg": c.denim}, "NotifyINFOTitle": {"fg": c.denim, "bold": True},
        "NotifyDEBUGIcon": {"fg": c.overlay1}, "NotifyDEBUGTitle": {"fg": c.overlay1, "bold": True},
        "NotifyTRACEIcon": {"fg": c.clay}, "NotifyTRACETitle": {"fg": c.clay, "bold": True},
        # trouble / flash / leap / hop
        "TroubleNormal": {"fg": c.subtext1, "bg": c.mantle},
        "TroubleNormalNC": {"fg": c.subtext1, "bg": c.mantle},
        "TroubleText": {"fg": c.subtext1},
        "TroubleCount": {"fg": c.orange, "bg": c.surface0},
        "FlashLabel": {"fg": c.crust, "bg": c.orange, "bold": True},
        "FlashMatch": {"fg": c.text_hi, "bg": c.surface2},
        "FlashCurrent": {"fg": c.crust, "bg": c.yellow},
        "FlashBackdrop": {"fg": c.overlay0},
        "LeapLabel": {"fg": c.orange, "bold": True},
        "LeapMatch": {"fg": c.yellow_hi, "underline": True, "bold": True},
        "HopNextKey": {"fg": c.orange, "bold": True},
        "HopNextKey1": {"fg": c.yellow, "bold": True},
        "HopNextKey2": {"fg": c.clay},
        # bufferline / lualine-adjacent / winbar crumbs
        "BufferLineFill": {"bg": c.crust},
        "BufferLineBackground": {"fg": c.overlay1, "bg": c.crust},
        "BufferLineBufferSelected": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "BufferLineIndicatorSelected": {"fg": c.orange, "bg": c.base},
        "BufferLineModifiedSelected": {"fg": c.yellow, "bg": c.base},
        "BufferLineSeparator": {"fg": c.crust, "bg": c.crust},
        "NavicText": {"fg": c.subtext0},
        "NavicSeparator": {"fg": c.overlay0},
        "DropBarIconUISeparator": {"fg": c.overlay0},
        # treesitter-context / render-markdown / markview
        "TreesitterContext": {"bg": c.mantle},
        "TreesitterContextLineNumber": {"fg": c.orange, "bg": c.mantle},
        "TreesitterContextBottom": {"sp": c.surface1, "underline": True},
        "RenderMarkdownH1Bg": {"bg": f.mix("orange", "base", 0.16)},
        "RenderMarkdownH2Bg": {"bg": f.mix("yellow", "base", 0.14)},
        "RenderMarkdownH3Bg": {"bg": f.mix("green", "base", 0.14)},
        "RenderMarkdownH4Bg": {"bg": f.mix("sage", "base", 0.14)},
        "RenderMarkdownH5Bg": {"bg": f.mix("clay", "base", 0.14)},
        "RenderMarkdownH6Bg": {"bg": c.surface0},
        "RenderMarkdownCode": {"bg": c.mantle},
        "RenderMarkdownCodeInline": {"fg": c.green, "bg": c.mantle},
        "RenderMarkdownBullet": {"fg": c.orange},
        "RenderMarkdownTableHead": {"fg": c.yellow},
        "RenderMarkdownTableRow": {"fg": c.surface2},
        # dashboards / mason / lazy / oil / dap / illuminate / mini
        "AlphaHeader": {"fg": c.orange}, "AlphaButtons": {"fg": c.subtext1},
        "AlphaShortcut": {"fg": c.yellow}, "AlphaFooter": {"fg": c.overlay1, "italic": True},
        "DashboardHeader": {"fg": c.orange}, "DashboardKey": {"fg": c.yellow},
        "DashboardDesc": {"fg": c.subtext1}, "DashboardIcon": {"fg": c.sage},
        "MasonHeader": {"fg": c.crust, "bg": c.orange, "bold": True},
        "MasonHighlight": {"fg": c.yellow},
        "MasonHighlightBlockBold": {"fg": c.crust, "bg": c.yellow, "bold": True},
        "MasonMuted": {"fg": c.overlay1},
        "LazyNormal": {"fg": c.text, "bg": float_bg},
        "LazyProgressDone": {"fg": c.orange},
        "LazyProgressTodo": {"fg": c.surface1},
        "LazySpecial": {"fg": c.yellow},
        "LazyReasonPlugin": {"fg": c.sage},
        "OilDir": {"fg": c.yellow, "bold": True},
        "OilDirIcon": {"fg": c.yellow},
        "OilCreate": {"fg": c.green}, "OilDelete": {"fg": c.red_hi},
        "OilMove": {"fg": c.clay}, "OilCopy": {"fg": c.sage},
        "DapBreakpoint": {"fg": c.red_hi},
        "DapStopped": {"fg": c.yellow},
        "DapStoppedLine": {"bg": t["chg"]},
        "DapUIScope": {"fg": c.orange}, "DapUIType": {"fg": c.sage},
        "DapUIValue": {"fg": c.text}, "DapUIVariable": {"fg": c.subtext1},
        "IlluminatedWordText": {"bg": c.surface1},
        "IlluminatedWordRead": {"bg": c.surface1},
        "IlluminatedWordWrite": {"bg": c.surface1, "underline": True},
        "MiniStatuslineModeNormal": {"fg": c.crust, "bg": c.orange, "bold": True},
        "MiniStatuslineModeInsert": {"fg": c.crust, "bg": c.green, "bold": True},
        "MiniStatuslineModeVisual": {"fg": c.crust, "bg": c.yellow, "bold": True},
        "MiniStatuslineModeReplace": {"fg": c.crust, "bg": c.red_hi, "bold": True},
        "MiniStatuslineModeCommand": {"fg": c.crust, "bg": c.sage, "bold": True},
        "MiniStatuslineDevinfo": {"fg": c.subtext1, "bg": c.surface1},
        "MiniStatuslineFilename": {"fg": c.subtext0, "bg": c.mantle},
        "MiniStatuslineFileinfo": {"fg": c.subtext1, "bg": c.surface1},
        "MiniTablineCurrent": {"fg": c.text_hi, "bg": c.base, "bold": True},
        "MiniTablineVisible": {"fg": c.subtext0, "bg": c.mantle},
        "MiniTablineHidden": {"fg": c.overlay1, "bg": c.crust},
        "MiniCursorword": {"bg": c.surface1},
        "MiniHipatternsTodo": {"fg": c.crust, "bg": c.yellow, "bold": True},
        "MiniHipatternsFixme": {"fg": c.crust, "bg": c.red_hi, "bold": True},
        "MiniHipatternsHack": {"fg": c.crust, "bg": c.clay, "bold": True},
        "MiniHipatternsNote": {"fg": c.crust, "bg": c.sage, "bold": True},
        "MiniPickMatchCurrent": {"bg": c.surface1},
        "MiniPickPrompt": {"fg": c.orange},
        "MiniFilesTitleFocused": {"fg": c.orange, "bold": True},
        "MiniClueTitle": {"fg": c.orange, "bold": True},
        "MiniJump2dSpot": {"fg": c.orange, "bold": True, "underline": True},
        "MiniStarterHeader": {"fg": c.orange}, "MiniStarterItemPrefix": {"fg": c.yellow},
        # neo-tree / nvim-tree extras
        "NeoTreeWinSeparator": {"fg": c.crust, "bg": c.crust},
        "NeoTreeIndentMarker": {"fg": c.surface1},
        "NeoTreeFileNameOpened": {"fg": c.text_hi},
        "NeoTreeDimText": {"fg": c.overlay0},
        "NeoTreeTitleBar": {"fg": c.crust, "bg": c.orange},
        "NvimTreeIndentMarker": {"fg": c.surface1},
        "NvimTreeGitDirty": {"fg": c.yellow},
        "NvimTreeGitNew": {"fg": c.green},
        "NvimTreeGitDeleted": {"fg": c.red_hi},
        "NvimTreeSpecialFile": {"fg": c.clay, "underline": True},
        "NvimTreeWinSeparator": {"fg": c.crust, "bg": c.crust},
        # which-key extras / harpoon / aerial / outline
        "WhichKeyBorder": {"fg": c.surface2, "bg": float_bg},
        "WhichKeyNormal": {"bg": float_bg},
        "WhichKeyValue": {"fg": c.overlay1},
        "HarpoonWindow": {"fg": c.text, "bg": float_bg},
        "HarpoonBorder": {"fg": c.surface2, "bg": float_bg},
        "AerialLine": {"bg": c.surface1},
        "OutlineCurrent": {"fg": c.orange, "bold": True},
        # rainbow delimiters: the 70s stripe
        "RainbowDelimiterRed": {"fg": c.red_hi},
        "RainbowDelimiterOrange": {"fg": c.orange},
        "RainbowDelimiterYellow": {"fg": c.yellow},
        "RainbowDelimiterGreen": {"fg": c.green},
        "RainbowDelimiterCyan": {"fg": c.sage},
        "RainbowDelimiterBlue": {"fg": c.denim},
        "RainbowDelimiterViolet": {"fg": c.clay},
    })
    return g


def lualine(f):
    """A lualine theme: route-bullet coloured mode segments."""
    c = f
    ink = c.crust if f.dark else c.base
    mode = lambda bg: {
        "a": {"fg": ink, "bg": bg, "gui": "bold"},
        "b": {"fg": c.subtext1, "bg": c.surface1},
        "c": {"fg": c.subtext0, "bg": c.mantle},
    }
    theme = {
        "normal": mode(c.orange), "insert": mode(c.green), "visual": mode(c.yellow),
        "replace": mode(c.red_hi), "command": mode(c.sage), "terminal": mode(c.clay),
        "inactive": {
            "a": {"fg": c.overlay1, "bg": c.crust}, "b": {"fg": c.overlay1, "bg": c.crust},
            "c": {"fg": c.overlay0, "bg": c.crust},
        },
    }
    return "-- " + HEADER + "\nreturn " + lua(theme) + "\n"


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
    return "{ " + ", ".join(f"{k} = {lua(val)}" for k, val in d.items()) + " }"


INIT = """-- {header}
local M = {{}}

M.flavors = {{ "walnut", "tunnel", "enamel" }}

M.config = {{
  -- "auto" follows vim.o.background: light → enamel, dark → walnut.
  flavor = "auto",
  -- Leave Normal/NormalNC/SignColumn backgrounds unset so the terminal shows through.
  transparent = false,
  -- Set false to drop every italic (comments, parameters, builtins …).
  italics = true,
  -- function(colors, flavor) return {{ GroupName = {{ fg = colors.orange }} }} end
  overrides = nil,
}}

function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", M.config, opts or {{}})
end

local function resolve(flavor)
  flavor = flavor or M.config.flavor
  if flavor == "auto" then
    return vim.o.background == "light" and "enamel" or "walnut"
  end
  return flavor
end

--- The palette for a flavor, as role → "#RRGGBB".
function M.colors(flavor)
  return require("subway-seat.palette")[resolve(flavor)]
end

function M.load(flavor)
  flavor = resolve(flavor)
  local colors = M.colors(flavor)
  local groups = vim.deepcopy(require("subway-seat.groups." .. flavor))

  if M.config.transparent then
    for _, name in ipairs({{ "Normal", "NormalNC", "SignColumn", "FoldColumn", "EndOfBuffer", "StatusLine" }}) do
      if groups[name] then groups[name].bg = nil end
    end
  end
  if not M.config.italics then
    for _, spec in pairs(groups) do spec.italic = nil end
  end
  if type(M.config.overrides) == "function" then
    for name, spec in pairs(M.config.overrides(colors, flavor) or {{}}) do
      groups[name] = spec
    end
  end

  if vim.g.colors_name then vim.cmd("highlight clear") end
  if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
  -- Changing 'background' re-sources the active colorscheme; drop the name first.
  vim.g.colors_name = nil
  local bg = flavor == "enamel" and "light" or "dark"
  if vim.o.background ~= bg then vim.o.background = bg end
  vim.o.termguicolors = true
  vim.g.colors_name = flavor == "walnut" and "subway-seat" or ("subway-seat-" .. flavor)

  for name, spec in pairs(groups) do
    vim.api.nvim_set_hl(0, name, spec)
  end
  for i, c in ipairs(require("subway-seat.palette").ansi[flavor]) do
    vim.g["terminal_color_" .. (i - 1)] = c
  end
end

return M
"""


def build(flavors):
    outs = []
    palette = {f.id: dict(f.colors) for f in flavors}
    ansi = {f.id: f.ansi for f in flavors}
    pal_lua = "-- " + HEADER + "\nlocal M = " + lua(palette) + "\nM.ansi = " + lua(ansi) + "\nreturn M\n"
    outs.append(Out("lua/subway-seat/palette.lua", pal_lua, lang="lua"))
    outs.append(Out("lua/subway-seat/init.lua", INIT.format(header=HEADER), lang="lua"))
    for f in flavors:
        allg = {**groups(f), **plugin_groups(f)}
        body = "\n".join(f'  ["{name}"] = {compact(spec)},' for name, spec in allg.items())
        outs.append(Out(f"lua/subway-seat/groups/{f.id}.lua", f"-- {HEADER}\nreturn {{\n{body}\n}}\n",
                        flavor=f.id, lang="lua"))
        outs.append(Out(f"lua/lualine/themes/{f.snake}.lua", lualine(f), flavor=f.id, lang="lua"))
        arg = "" if f.id == "walnut" else f'"{f.id}"'
        outs.append(Out(f"colors/{f.slug}.lua",
                        f'-- {HEADER}\nrequire("subway-seat").load({arg})\n',
                        flavor=f.id, dest=f"~/.config/nvim/colors/{f.slug}.lua (or install the plugin)", lang="lua"))
    return outs
