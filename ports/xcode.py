"""Xcode: a .xccolortheme per flavor."""

import plistlib

from ports._editors import ui
from ports._lib import HEADER, Out, rgb_floats

META = {
    "id": "xcode",
    "name": "Xcode",
    "category": "Editors",
    "homepage": "https://developer.apple.com/xcode/",
    "enable": {
        "where": "Terminal, then Xcode › Settings… › Themes",
        "code": "mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes\n"
        'cp "{name}.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/\n'
        "# restart Xcode, then pick {name} under Settings › Themes",
        "lang": "sh",
    },
    "auto": {
        "where": "Terminal, with Xcode closed (Xcode keeps one theme for light mode and one for dark)",
        "code": "defaults write com.apple.dt.Xcode XCFontAndColorCurrentTheme -string 'Subway Seat Enamel.xccolortheme'\n"
        "defaults write com.apple.dt.Xcode XCFontAndColorCurrentDarkTheme -string 'Subway Seat.xccolortheme'",
        "lang": "sh",
    },
    "detect": ["/Applications/Xcode.app", "/Applications/Xcode-beta.app"],
    "notes": "Source editor, console and rendered documentation colors in SF Mono, with comments in "
    "italic. Change the font size in Xcode's Themes settings; the colors stay. Xcode remembers the theme "
    "you pick separately for light and dark mode, so it can follow the system.",
}

SIZE = "13.0"
FONTS = {
    (): "SFMono-Regular",
    ("italic",): "SFMono-RegularItalic",
    ("bold",): "SFMono-Bold",
    ("bold", "italic"): "SFMono-BoldItalic",
    ("semibold",): "SFMono-Semibold",
    ("semibold", "italic"): "SFMono-SemiboldItalic",
}

# xcode.syntax.* → syntax role (or (color role, styles))
SYNTAX = {
    "attribute": "decorator",
    "character": "string",
    "comment": "comment",
    "comment.doc": "comment",
    "comment.doc.keyword": ("overlay2", ("semibold", "italic")),
    "declaration.other": "function",
    "declaration.type": "type",
    "identifier.class": "type",
    "identifier.class.system": "type.builtin",
    "identifier.constant": "constant",
    "identifier.constant.system": "constant",
    "identifier.function": "function",
    "identifier.function.system": "function.builtin",
    "identifier.macro": ("clay", ()),
    "identifier.macro.system": ("clay", ("italic",)),
    "identifier.type": "type",
    "identifier.type.system": "type.builtin",
    "identifier.variable": "property",
    "identifier.variable.system": "property",
    "keyword": "keyword",
    "mark": "heading",
    "markup.code": "code",
    "number": "number",
    "plain": "variable",
    "preprocessor": ("clay", ()),
    "regex": "regexp",
    "regex.capturename": "property",
    "regex.charname": ("sage", ()),
    "regex.number": "number",
    "regex.other": ("orange", ()),
    "string": "string",
    "url": "link",
}


def col(color, a=1):
    return " ".join(f"{x:g}" for x in (*rgb_floats(color), a))


def font(styles=(), size=SIZE):
    key = tuple(s for s in ("bold", "semibold", "italic") if s in styles)
    return f"{FONTS[key]} - {size}"


def theme(f):
    c = f
    u = ui(f)
    colors, fonts = {}, {}
    for key, spec in SYNTAX.items():
        if isinstance(spec, str):
            hexc, st = f.syntax(spec)
        else:
            hexc, st = f.colors[spec[0]], spec[1]
        colors[f"xcode.syntax.{key}"] = col(hexc)
        fonts[f"xcode.syntax.{key}"] = font(st)
    ui_font = ".AppleSystemUIFont"
    return {
        "DVTFontAndColorVersion": 1,
        "DVTLineSpacing": 1.1,
        # source editor
        "DVTSourceTextBackground": col(c.base),
        "DVTSourceTextCurrentLineHighlightColor": col(u["line"]),
        "DVTSourceTextInsertionPointColor": col(u["cursor"]),
        "DVTSourceTextInvisiblesColor": col(c.surface1),
        "DVTSourceTextSelectionColor": col(u["selection"]),
        "DVTSourceTextBlockDimBackgroundColor": col(c.crust),
        "DVTSourceTextSyntaxColors": colors,
        "DVTSourceTextSyntaxFonts": fonts,
        "DVTDebuggerInstructionPointerColor": col(c.green),
        # scrollbar markers
        "DVTScrollbarMarkerAnalyzerColor": col(c.denim),
        "DVTScrollbarMarkerBreakpointColor": col(c.denim),
        "DVTScrollbarMarkerDiffColor": col(c.overlay1),
        "DVTScrollbarMarkerDiffConflictColor": col(c.orange),
        "DVTScrollbarMarkerErrorColor": col(u["error"]),
        "DVTScrollbarMarkerRuntimeIssueColor": col(c.clay),
        "DVTScrollbarMarkerWarningColor": col(u["warning"]),
        # rendered documentation (Quick Help, doc comments)
        "DVTMarkupTextBackgroundColor": col(c.mantle),
        "DVTMarkupTextBorderColor": col(c.surface1),
        "DVTMarkupTextCodeFont": font(size="10.0"),
        "DVTMarkupTextEmphasisColor": col(c.text),
        "DVTMarkupTextEmphasisFont": f"{ui_font}Italic - 10.0",
        "DVTMarkupTextInlineCodeColor": col(c.green),
        "DVTMarkupTextLinkColor": col(c.denim),
        "DVTMarkupTextLinkFont": f"{ui_font} - 10.0",
        "DVTMarkupTextNormalColor": col(c.text),
        "DVTMarkupTextNormalFont": f"{ui_font} - 10.0",
        "DVTMarkupTextOtherHeadingColor": col(c.subtext1),
        "DVTMarkupTextOtherHeadingFont": f"{ui_font} - 14.0",
        "DVTMarkupTextPrimaryHeadingColor": col(c.yellow),
        "DVTMarkupTextPrimaryHeadingFont": f"{ui_font} - 24.0",
        "DVTMarkupTextSecondaryHeadingColor": col(c.yellow),
        "DVTMarkupTextSecondaryHeadingFont": f"{ui_font} - 18.0",
        "DVTMarkupTextStrongColor": col(c.text_hi),
        "DVTMarkupTextStrongFont": f"{ui_font}Bold - 10.0",
        # console (a panel: one step down)
        "DVTConsoleDebuggerInputTextColor": col(c.text),
        "DVTConsoleDebuggerInputTextFont": font(("bold",)),
        "DVTConsoleDebuggerOutputTextColor": col(c.subtext1),
        "DVTConsoleDebuggerOutputTextFont": font(),
        "DVTConsoleDebuggerPromptTextColor": col(c.orange),
        "DVTConsoleDebuggerPromptTextFont": font(("bold",)),
        "DVTConsoleExectuableInputTextColor": col(c.text),  # sic — Xcode's own spelling
        "DVTConsoleExectuableInputTextFont": font(),
        "DVTConsoleExectuableOutputTextColor": col(c.text),
        "DVTConsoleExectuableOutputTextFont": font(),
        "DVTConsoleTextBackgroundColor": col(c.mantle),
        "DVTConsoleTextInsertionPointColor": col(u["cursor"]),
        "DVTConsoleTextSelectionColor": col(u["selection"]),
    }


def build(flavors):
    outs = []
    for f in flavors:
        xml = plistlib.dumps(theme(f)).decode()
        head, rest = xml.split("\n", 1)
        outs.append(Out(f"{f.name}.xccolortheme", f"{head}\n<!-- {HEADER} -->\n{rest}", flavor=f.id,
                        dest=f"~/Library/Developer/Xcode/UserData/FontAndColorThemes/{f.name}.xccolortheme",
                        lang="xml"))
    return outs
