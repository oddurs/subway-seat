"""JetBrains IDEs: a theme plugin (UI theme + editor color scheme per flavor), assembled as a JAR."""

import io
import json
import zipfile
from xml.sax.saxutils import escape, quoteattr

import palette as p
from ports._editors import ui
from ports._lib import HEADER, REPO, Out, h, tints

META = {
    "id": "jetbrains",
    "name": "JetBrains IDEs",
    "category": "Editors",
    "homepage": "https://www.jetbrains.com",
    "enable": {
        "where": "Settings → Plugins → ⚙ → Install Plugin from Disk… (subway-seat-jetbrains.jar), "
        "then Settings → Appearance & Behavior → Appearance",
        "code": "Theme: {name}\nEditor → Color Scheme: {name}",
        "lang": "text",
    },
    "notes": "One plugin for IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider and the rest: a UI theme and a "
    "matching editor color scheme for each flavor. The .icls files import on their own if you only want the editor colours.",
}

VERSION = "0.2.0"  # matches the VS Code extension
PLUGIN_ID = "com.oddurs.subway-seat"
JAR = "subway-seat-jetbrains.jar"


# ── Editor color scheme (.icls) ─────────────────────────────────────────────
BOLD, ITALIC = 1, 2
BOXED, UNDERLINE, WAVE, STRIKE, BOLD_UNDERLINE, DOTTED = 0, 1, 2, 3, 4, 5


def A(fg=None, bg=None, st=(), effect=None, etype=None, stripe=None):
    """One TextAttributes value. `st` ⊂ {"bold", "italic"}."""
    return {"fg": fg, "bg": bg, "st": set(st), "effect": effect, "etype": etype, "stripe": stripe}


def colors(f):
    """<colors>: editor chrome that isn't a text attribute."""
    u = ui(f)
    vcs = [f.mix("orange", "base", a) for a in (0.30, 0.24, 0.18, 0.12, 0.06)]
    return {
        "CARET_COLOR": u["cursor"],
        "CARET_ROW_COLOR": u["line"],
        "SELECTION_BACKGROUND": u["selection"],
        "SELECTION_FOREGROUND": "",
        "LINE_NUMBERS_COLOR": u["line_nr"],
        "LINE_NUMBER_ON_CARET_ROW_COLOR": u["line_nr_cur"],
        "GUTTER_BACKGROUND": f.base,
        "READONLY_BACKGROUND": f.base,
        "READONLY_FRAGMENT_BACKGROUND": f.mantle,
        "INDENT_GUIDE": f.surface0,
        "VISUAL_INDENT_GUIDE": f.surface0,
        "SELECTED_INDENT_GUIDE": f.surface2,
        "MATCHED_BRACES_INDENT_GUIDE_COLOR": f.overlay0,
        "RIGHT_MARGIN_COLOR": f.surface0,
        "SOFT_WRAP_SIGN_COLOR": f.overlay0,
        "WHITESPACES": f.surface1,
        "WHITESPACES_MODIFIED_LINES_COLOR": f.surface2,
        "TEARLINE_COLOR": f.surface0,
        "SELECTED_TEARLINE_COLOR": f.surface1,
        "METHOD_SEPARATORS_COLOR": f.surface0,
        "FOLDED_TEXT_BORDER_COLOR": f.surface1,
        "CONSOLE_BACKGROUND_KEY": f.mantle,
        "TERMINAL_BACKGROUND": f.mantle,
        "BLOCK_TERMINAL_DEFAULT_BACKGROUND": f.mantle,
        "BLOCK_TERMINAL_DEFAULT_FOREGROUND": f.text,
        "BLOCK_TERMINAL_BLOCK_BACKGROUND_START": f.mantle,
        "BLOCK_TERMINAL_BLOCK_BACKGROUND_END": f.mantle,
        "BLOCK_TERMINAL_SELECTED_BLOCK_BACKGROUND": f.surface0,
        "BLOCK_TERMINAL_SELECTED_BLOCK_STROKE_COLOR": f.orange,
        "BLOCK_TERMINAL_INACTIVE_SELECTED_BLOCK_BACKGROUND": f.surface0,
        "BLOCK_TERMINAL_INACTIVE_SELECTED_BLOCK_STROKE_COLOR": f.overlay0,
        "BLOCK_TERMINAL_ERROR_BLOCK_STROKE_COLOR": f.red_hi,
        "BLOCK_TERMINAL_PROMPT_SEPARATOR_COLOR": f.surface1,
        "ADDED_LINES_COLOR": f.green,
        "MODIFIED_LINES_COLOR": f.yellow,
        "DELETED_LINES_COLOR": f.red_hi,
        "IGNORED_ADDED_LINES_BORDER_COLOR": f.green,
        "IGNORED_MODIFIED_LINES_BORDER_COLOR": f.yellow,
        "IGNORED_DELETED_LINES_BORDER_COLOR": f.red_hi,
        "DIFF_SEPARATORS_BACKGROUND": f.surface0,
        "ANNOTATIONS_COLOR": f.overlay1,
        "ANNOTATIONS_LAST_COMMIT_COLOR": f.subtext1,
        **{f"VCS_ANNOTATIONS_COLOR_{i + 1}": c for i, c in enumerate(vcs)},
        "DOCUMENTATION_COLOR": f.mantle,
        "DOC_COMMENT_LINK": f.denim,
        "NOTIFICATION_BACKGROUND": f.mantle,
        "LOOKUP_COLOR": f.mantle,
        "INFORMATION_HINT": f.mantle,
        "QUESTION_HINT": f.mantle,
        "ERROR_HINT": f.mix("red", "mantle", 0.25),
        "PROMOTION_PANE": f.surface0,
        "RECENT_LOCATIONS_SELECTION": f.surface1,
        "INLINE_REFACTORING_SETTINGS_DEFAULT": f.surface0,
        "INLINE_REFACTORING_SETTINGS_FOCUSED": f.surface1,
        "INLINE_REFACTORING_SETTINGS_HOVERED": f.surface1,
        "TAB_UNDERLINE": f.orange,
        "TAB_UNDERLINE_INACTIVE": f.overlay0,
        "MODIFIED_TAB_ICON": f.yellow,
        "ScrollBar.thumbColor": f.surface1,
        "ScrollBar.thumbBorderColor": f.surface1,
        "ScrollBar.hoverThumbColor": f.surface2,
        "ScrollBar.hoverThumbBorderColor": f.surface2,
        "ScrollBar.Mac.thumbColor": f.surface1,
        "ScrollBar.Mac.thumbBorderColor": f.surface1,
        "ScrollBar.Mac.hoverThumbColor": f.surface2,
        "ScrollBar.Mac.hoverThumbBorderColor": f.surface2,
        "ScrollBar.Mac.Transparent.thumbColor": f.surface1,
        "ScrollBar.Mac.Transparent.thumbBorderColor": f.surface1,
        "ScrollBar.Mac.Transparent.hoverThumbColor": f.surface2,
        "ScrollBar.Mac.Transparent.hoverThumbBorderColor": f.surface2,
        # VCS file status (project view, tabs, changes)
        "FILESTATUS_ADDED": f.green_hi,
        "FILESTATUS_COPIED": f.green,
        "FILESTATUS_DELETED": f.red_hi,
        "FILESTATUS_MODIFIED": f.yellow,
        "FILESTATUS_MERGED": f.orange,
        "FILESTATUS_UNKNOWN": f.green,
        "FILESTATUS_SWITCHED": f.sage,
        "FILESTATUS_HIJACKED": f.yellow,
        "FILESTATUS_SUPPRESSED": f.overlay0,
        "FILESTATUS_NOT_CHANGED_IMMEDIATE": f.yellow,
        "FILESTATUS_NOT_CHANGED_RECURSIVE": f.yellow,
        "FILESTATUS_addedOutside": f.green,
        "FILESTATUS_modifiedOutside": f.yellow,
        "FILESTATUS_changelistConflict": f.red_hi,
        "FILESTATUS_IDEA_FILESTATUS_IGNORED": f.overlay0,
        "FILESTATUS_IGNORE.PROJECT_VIEW.IGNORED": f.overlay0,
        "FILESTATUS_IDEA_FILESTATUS_DELETED_FROM_FILE_SYSTEM": f.overlay0,
        "FILESTATUS_IDEA_FILESTATUS_MERGED_WITH_CONFLICTS": f.orange,
        "FILESTATUS_IDEA_FILESTATUS_MERGED_WITH_BOTH_CONFLICTS": f.orange,
        "FILESTATUS_IDEA_FILESTATUS_MERGED_WITH_PROPERTY_CONFLICTS": f.orange,
        "FILESTATUS_IDEA_SVN_FILESTATUS_EXTERNAL": f.sage,
        # HTML/XML tag tree (painted faintly by the IDE)
        **{f"HTML_TAG_TREE_LEVEL{i}": c for i, c in enumerate([f.orange, f.yellow, f.green, f.sage, f.denim, f.clay])},
    }


def attributes(f):
    """<attributes>: text attributes. Values are A(...) dicts or a base-attribute name (str)."""
    u, t = ui(f), tints(f)

    def S(role, st=()):
        color, styles = f.syntax(role)
        return A(fg=color, st=styles | set(st))

    ansi = f.ansi
    fn_call = S("function")
    attrs = {
        "TEXT": A(fg=f.text, bg=f.base),
        # ── language defaults: every language inherits from these ──
        "DEFAULT_KEYWORD": S("keyword"),
        "DEFAULT_IDENTIFIER": S("variable"),
        "DEFAULT_LOCAL_VARIABLE": S("variable"),
        "DEFAULT_REASSIGNED_LOCAL_VARIABLE": "DEFAULT_LOCAL_VARIABLE",
        "DEFAULT_GLOBAL_VARIABLE": S("variable"),
        "DEFAULT_PARAMETER": S("parameter"),
        "DEFAULT_REASSIGNED_PARAMETER": "DEFAULT_PARAMETER",
        "DEFAULT_INSTANCE_FIELD": S("property"),
        "DEFAULT_STATIC_FIELD": S("property", st={"italic"}),
        "DEFAULT_CONSTANT": S("constant"),
        "DEFAULT_NUMBER": S("number"),
        "DEFAULT_STRING": S("string"),
        "DEFAULT_VALID_STRING_ESCAPE": S("string.escape"),
        "DEFAULT_INVALID_STRING_ESCAPE": A(fg=f.clay, effect=f.red_hi, etype=WAVE),
        "DEFAULT_LINE_COMMENT": S("comment"),
        "DEFAULT_BLOCK_COMMENT": S("comment"),
        "DEFAULT_DOC_COMMENT": S("comment"),
        "DEFAULT_DOC_COMMENT_TAG": A(fg=f.overlay2, st={"italic", "bold"}),
        "DEFAULT_DOC_COMMENT_TAG_VALUE": S("parameter"),
        "DEFAULT_DOC_MARKUP": A(fg=f.overlay1),
        "DEFAULT_OPERATION_SIGN": S("operator"),
        "DEFAULT_BRACES": S("punctuation"),
        "DEFAULT_BRACKETS": S("punctuation"),
        "DEFAULT_PARENTHS": S("punctuation"),
        "DEFAULT_COMMA": S("punctuation"),
        "DEFAULT_SEMICOLON": S("punctuation"),
        "DEFAULT_DOT": S("punctuation"),
        "DEFAULT_FUNCTION_DECLARATION": S("function"),
        "DEFAULT_FUNCTION_CALL": fn_call,
        "DEFAULT_INSTANCE_METHOD": S("function"),
        "DEFAULT_STATIC_METHOD": S("function"),
        "DEFAULT_CLASS_NAME": S("type"),
        "DEFAULT_CLASS_REFERENCE": S("type"),
        "DEFAULT_INTERFACE_NAME": S("type"),
        "DEFAULT_PREDEFINED_SYMBOL": S("variable.builtin"),
        "DEFAULT_METADATA": S("decorator"),
        "DEFAULT_ATTRIBUTE": S("attribute"),
        "DEFAULT_TAG": S("punctuation"),
        "DEFAULT_ENTITY": S("string.escape"),
        "DEFAULT_LABEL": S("decorator"),
        "DEFAULT_TEMPLATE_LANGUAGE_COLOR": A(fg=f.clay),
        "TYPE_PARAMETER_NAME_ATTRIBUTES": A(fg=f.sage, st={"italic"}),
        "CUSTOM_KEYWORD1_ATTRIBUTES": "DEFAULT_KEYWORD",
        "CUSTOM_KEYWORD2_ATTRIBUTES": S("type"),
        "CUSTOM_KEYWORD3_ATTRIBUTES": S("function"),
        "CUSTOM_KEYWORD4_ATTRIBUTES": S("constant"),
        "CUSTOM_STRING_ATTRIBUTES": "DEFAULT_STRING",
        "CUSTOM_VALID_STRING_ESCAPE_ATTRIBUTES": "DEFAULT_VALID_STRING_ESCAPE",
        "CUSTOM_LINE_COMMENT_ATTRIBUTES": "DEFAULT_LINE_COMMENT",
        "CUSTOM_NUMBER_ATTRIBUTES": "DEFAULT_NUMBER",
        # ── diagnostics & inspections ──
        "ERRORS_ATTRIBUTES": A(effect=u["error"], etype=WAVE, stripe=u["error"]),
        "WRONG_REFERENCES_ATTRIBUTES": A(fg=u["error"], effect=u["error"], etype=WAVE, stripe=u["error"]),
        "WARNING_ATTRIBUTES": A(effect=u["warning"], etype=WAVE, stripe=u["warning"]),
        "GENERIC_SERVER_ERROR_OR_WARNING": A(effect=u["warning"], etype=WAVE, stripe=u["warning"]),
        "INFO_ATTRIBUTES": A(effect=u["info"], etype=WAVE, stripe=u["info"]),  # "Weak warning"
        "TYPO": A(effect=u["hint"], etype=WAVE),
        "RUNTIME_ERROR": A(effect=u["error"], etype=DOTTED, stripe=u["error"]),
        "BAD_CHARACTER": A(effect=u["error"], etype=WAVE),
        "DEPRECATED_ATTRIBUTES": A(effect=f.overlay1, etype=STRIKE),
        "MARKED_FOR_REMOVAL_ATTRIBUTES": A(effect=f.red_hi, etype=STRIKE),
        "NOT_USED_ELEMENT_ATTRIBUTES": A(fg=f.overlay1),
        "UNMATCHED_BRACE_ATTRIBUTES": A(fg=f.red_hi, bg=t["del"], st={"bold"}),
        "MATCHED_BRACE_ATTRIBUTES": A(fg=u["bracket_fg"], bg=u["bracket_bg"], st={"bold"}),
        "IDENTIFIER_UNDER_CARET_ATTRIBUTES": A(bg=f.surface1 if f.dark else f.surface0, stripe=f.overlay2),
        "WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES": A(bg=f.surface1 if f.dark else f.surface0,
                                                     effect=f.overlay1, etype=UNDERLINE, stripe=f.orange),
        "SEARCH_RESULT_ATTRIBUTES": A(bg=u["search"], stripe=f.yellow),
        "WRITE_SEARCH_RESULT_ATTRIBUTES": A(bg=u["search_cur"], stripe=f.orange),
        "TEXT_SEARCH_RESULT_ATTRIBUTES": A(bg=u["search"], stripe=f.yellow),
        "HYPERLINK_ATTRIBUTES": A(fg=f.denim, effect=f.denim, etype=UNDERLINE),
        "FOLLOWED_HYPERLINK_ATTRIBUTES": A(fg=f.denim_hi, effect=f.denim_hi, etype=UNDERLINE),
        "INACTIVE_HYPERLINK_ATTRIBUTES": A(fg=f.denim),
        "CTRL_CLICKABLE": A(fg=f.denim, effect=f.denim, etype=UNDERLINE),
        "TODO_DEFAULT_ATTRIBUTES": A(fg=f.yellow, st={"bold", "italic"}, stripe=f.yellow),
        "LIVE_TEMPLATE_ATTRIBUTES": A(effect=f.orange, etype=BOXED),
        "LIVE_TEMPLATE_INACTIVE_SEGMENT": A(effect=f.surface2, etype=BOXED),
        "TEMPLATE_VARIABLE_ATTRIBUTES": A(fg=f.clay),
        "FOLDED_TEXT_ATTRIBUTES": A(fg=f.overlay1, bg=f.surface0),
        "INJECTED_LANGUAGE_FRAGMENT": A(),
        "BOOKMARKS_ATTRIBUTES": A(stripe=f.denim),
        "CODE_LENS_BORDER_COLOR": A(effect=f.surface1, etype=BOXED),
        "INLAY_DEFAULT": A(fg=f.overlay1, bg=f.mix("surface0", "base", 0.6), st={"italic"}),
        "INLAY_TEXT_WITHOUT_BACKGROUND": A(fg=f.overlay1, st={"italic"}),
        "INLINE_PARAMETER_HINT": A(fg=f.overlay1, bg=f.mix("surface0", "base", 0.6), st={"italic"}),
        "INLINE_PARAMETER_HINT_CURRENT": A(fg=f.yellow_hi, bg=f.surface1, st={"bold"}),
        "INLINE_PARAMETER_HINT_HIGHLIGHTED": A(fg=f.text, bg=f.surface1),
        "INLINE_REFACTORING_SETTINGS_DEFAULT": A(bg=f.surface0),
        "BREADCRUMBS_DEFAULT": A(fg=f.overlay1),
        "BREADCRUMBS_HOVERED": A(fg=f.text, bg=f.surface0),
        "BREADCRUMBS_CURRENT": A(fg=f.text_hi),
        "BREADCRUMBS_INACTIVE": A(fg=f.overlay0),
        "TAB_SELECTED": A(fg=f.text_hi, bg=f.base),
        "TAB_SELECTED_INACTIVE": A(fg=f.subtext0, bg=f.base),
        # ── diff, VCS, debugger, coverage ──
        "DIFF_INSERTED": A(bg=t["add"], stripe=f.green),
        "DIFF_DELETED": A(bg=t["del"], stripe=f.red_hi),
        "DIFF_MODIFIED": A(bg=t["chg"], stripe=f.yellow),
        "DIFF_CONFLICT": A(bg=f.mix("orange", "base", 0.22 if f.dark else 0.18), stripe=f.orange),
        "DELETED_TEXT_ATTRIBUTES": A(fg=f.overlay1, effect=f.red_hi, etype=STRIKE),
        "EXECUTIONPOINT_ATTRIBUTES": A(bg=t["chg_emph"]),
        "BREAKPOINT_ATTRIBUTES": A(bg=t["del"]),
        "NOT_TOP_FRAME_ATTRIBUTES": A(bg=f.surface0),
        "INLINE_STACK_FRAMES": A(bg=f.surface0),
        "DEBUGGER_INLINED_VALUES": A(fg=f.overlay1, st={"italic"}),
        "DEBUGGER_INLINED_VALUES_EXECUTION_LINE": A(fg=f.overlay2, st={"italic"}),
        "DEBUGGER_INLINED_VALUES_MODIFIED": A(fg=f.orange, st={"italic"}),
        "DEBUGGER_SMART_STEP_INTO_SELECTION": "LIVE_TEMPLATE_ATTRIBUTES",
        "DEBUGGER_SMART_STEP_INTO_TARGET": "SEARCH_RESULT_ATTRIBUTES",
        "EVALUATED_EXPRESSION_ATTRIBUTES": A(bg=f.surface0),
        "EVALUATED_EXPRESSION_EXECUTION_LINE_ATTRIBUTES": A(bg=f.surface1),
        "LINE_FULL_COVERAGE": A(fg=f.green),
        "LINE_PARTIAL_COVERAGE": A(fg=f.yellow),
        "LINE_NONE_COVERAGE": A(fg=f.red_hi),
        # ── console & terminal ──
        "CONSOLE_NORMAL_OUTPUT": A(fg=f.text),
        "CONSOLE_ERROR_OUTPUT": A(fg=f.red_hi),
        "CONSOLE_SYSTEM_OUTPUT": A(fg=f.overlay1),
        "CONSOLE_USER_INPUT": A(fg=f.green, st={"italic"}),
        "CONSOLE_RANGE_TO_EXECUTE": A(effect=f.orange, etype=BOXED),
        "TERMINAL_COMMAND_TO_RUN_USING_IDE": A(bg=f.surface1),
        "BLOCK_TERMINAL_COMMAND": A(fg=f.yellow, st={"bold"}),
        "BLOCK_TERMINAL_SEARCH_ENTRY": A(fg=f.text, bg=u["search"]),
        "BLOCK_TERMINAL_CURRENT_SEARCH_ENTRY": A(fg=f.text_hi, bg=u["search_cur"]),
        "LOG_ERROR_OUTPUT": A(fg=f.red_hi),
        "LOG_WARNING_OUTPUT": A(fg=f.yellow),
        "LOG_INFO_OUTPUT": A(fg=f.denim),
        "LOG_DEBUG_OUTPUT": A(fg=f.overlay1),
        "LOG_VERBOSE_OUTPUT": A(fg=f.overlay0),
        "LOG_EXPIRED_ENTRY": A(fg=f.surface2),
        "LOGCAT_ASSERT_OUTPUT": A(fg=f.red_hi, st={"bold"}),
        "LOGCAT_ERROR_OUTPUT": A(fg=f.red_hi),
        "LOGCAT_WARNING_OUTPUT": A(fg=f.yellow),
        "LOGCAT_INFO_OUTPUT": A(fg=f.denim),
        "LOGCAT_DEBUG_OUTPUT": A(fg=f.overlay1),
        "LOGCAT_VERBOSE_OUTPUT": A(fg=f.overlay0),
        # ── rainbow brackets & semantic highlighting: the 70s stripe ──
        **rainbow(f),
        # ── Java / Kotlin (shared Java keys have no prefix) ──
        "CLASS_NAME_ATTRIBUTES": "DEFAULT_CLASS_NAME",
        "INTERFACE_NAME_ATTRIBUTES": "DEFAULT_INTERFACE_NAME",
        "ABSTRACT_CLASS_NAME_ATTRIBUTES": S("type", st={"italic"}),
        "ENUM_NAME_ATTRIBUTES": "DEFAULT_CLASS_NAME",
        "ANNOTATION_NAME_ATTRIBUTES": "DEFAULT_METADATA",
        "ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES": S("parameter"),
        "ENUM_CONST": S("constant"),
        "STATIC_FIELD_ATTRIBUTES": "DEFAULT_STATIC_FIELD",
        "STATIC_FINAL_FIELD_ATTRIBUTES": S("constant"),
        "INSTANCE_FIELD_ATTRIBUTES": "DEFAULT_INSTANCE_FIELD",
        "INSTANCE_FINAL_FIELD_ATTRIBUTES": "DEFAULT_INSTANCE_FIELD",
        "STATIC_METHOD_ATTRIBUTES": "DEFAULT_STATIC_METHOD",
        "METHOD_CALL_ATTRIBUTES": "DEFAULT_FUNCTION_CALL",
        "METHOD_DECLARATION_ATTRIBUTES": "DEFAULT_FUNCTION_DECLARATION",
        "ABSTRACT_METHOD_ATTRIBUTES": S("function", st={"italic"}),
        "INHERITED_METHOD_ATTRIBUTES": "DEFAULT_INSTANCE_METHOD",
        "CONSTRUCTOR_CALL_ATTRIBUTES": S("type"),
        "CONSTRUCTOR_DECLARATION_ATTRIBUTES": S("type"),
        "PARAMETER_ATTRIBUTES": "DEFAULT_PARAMETER",
        "LOCAL_VARIABLE_ATTRIBUTES": "DEFAULT_LOCAL_VARIABLE",
        "REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES": "DEFAULT_REASSIGNED_LOCAL_VARIABLE",
        "IMPLICIT_ANONYMOUS_CLASS_PARAMETER_ATTRIBUTES": S("parameter"),
        "KOTLIN_CLASS": "DEFAULT_CLASS_NAME",
        "KOTLIN_TRAIT": "DEFAULT_INTERFACE_NAME",
        "KOTLIN_OBJECT": "DEFAULT_CLASS_NAME",
        "KOTLIN_TYPE_ALIAS": "DEFAULT_CLASS_NAME",
        "KOTLIN_ANNOTATION": "DEFAULT_METADATA",
        "KOTLIN_CONSTRUCTOR": S("type"),
        "KOTLIN_ENUM_ENTRY": S("constant"),
        "KOTLIN_TYPE_PARAMETER": "TYPE_PARAMETER_NAME_ATTRIBUTES",
        "KOTLIN_NAMED_ARGUMENT": S("parameter"),
        "KOTLIN_CLOSURE_DEFAULT_PARAMETER": S("variable.builtin"),
        "KOTLIN_LABEL": "DEFAULT_LABEL",
        "KOTLIN_INSTANCE_PROPERTY": "DEFAULT_INSTANCE_FIELD",
        "KOTLIN_PACKAGE_PROPERTY": "DEFAULT_STATIC_FIELD",
        "KOTLIN_BACKING_FIELD_VARIABLE": S("property"),
        "KOTLIN_EXTENSION_PROPERTY": S("property", st={"italic"}),
        "KOTLIN_EXTENSION_FUNCTION_CALL": S("function", st={"italic"}),
        "KOTLIN_PACKAGE_FUNCTION_CALL": "DEFAULT_FUNCTION_CALL",
        "KOTLIN_DYNAMIC_FUNCTION_CALL": S("function", st={"italic"}),
        "KOTLIN_DYNAMIC_PROPERTY_CALL": S("property", st={"italic"}),
        "KOTLIN_VARIABLE_AS_FUNCTION": S("function"),
        "KOTLIN_VARIABLE_AS_FUNCTION_LIKE": S("function"),
        "KOTLIN_FUNCTION_LITERAL_BRACES_AND_ARROW": A(fg=f.overlay2, st={"bold"}),
        "KOTLIN_EXCLEXCL": A(fg=f.clay, st={"bold"}),
        "KOTLIN_QUEST": S("operator"),
        "KOTLIN_SMART_CAST_VALUE": A(bg=f.surface0),
        "KOTLIN_SMART_CAST_RECEIVER": A(bg=f.surface0),
        "KOTLIN_SMART_CONSTANT": A(bg=f.surface0),
        "KOTLIN_MUTABLE_VARIABLE": A(),
        # ── Python ──
        "PY.KEYWORD": "DEFAULT_KEYWORD",
        "PY.FUNC_DEFINITION": "DEFAULT_FUNCTION_DECLARATION",
        "PY.CLASS_DEFINITION": "DEFAULT_CLASS_NAME",
        "PY.BUILTIN_NAME": S("function.builtin"),
        "PY.PREDEFINED_DEFINITION": S("function.builtin"),
        "PY.PREDEFINED_USAGE": S("function.builtin"),
        "PY.SELF_PARAMETER": S("variable.builtin"),
        "PY.KEYWORD_ARGUMENT": S("parameter"),
        "PY.DECORATOR": S("decorator"),
        "PY.ANNOTATION": S("type"),
        "PY.DOC_COMMENT": A(fg=f.green, st={"italic"}),
        "PY.STRING.B": "DEFAULT_STRING",
        # ── JavaScript / TypeScript ──
        "JS.GLOBAL_VARIABLE": "DEFAULT_GLOBAL_VARIABLE",
        "JS.GLOBAL_FUNCTION": "DEFAULT_FUNCTION_DECLARATION",
        "JS.LOCAL_VARIABLE": "DEFAULT_LOCAL_VARIABLE",
        "JS.PARAMETER": "DEFAULT_PARAMETER",
        "JS.INSTANCE_MEMBER_FUNCTION": "DEFAULT_INSTANCE_METHOD",
        "JS.INSTANCE_MEMBER_VARIABLE": "DEFAULT_INSTANCE_FIELD",
        "JS.STATIC_MEMBER_FUNCTION": "DEFAULT_STATIC_METHOD",
        "JS.STATIC_MEMBER_VARIABLE": "DEFAULT_STATIC_FIELD",
        "JS.REGEXP": S("regexp"),
        "JS.DECORATOR": S("decorator"),
        "TS.TYPE_PARAMETER": "TYPE_PARAMETER_NAME_ATTRIBUTES",
        "TS.MODULE_NAME": S("namespace"),
        "TS.TYPE_GUARD": S("keyword"),
        # ── Rust ──
        "org.rust.CRATE": S("namespace"),
        "org.rust.MODULE": S("namespace"),
        "org.rust.STRUCT": "DEFAULT_CLASS_NAME",
        "org.rust.ENUM": "DEFAULT_CLASS_NAME",
        "org.rust.UNION": "DEFAULT_CLASS_NAME",
        "org.rust.TRAIT": "DEFAULT_INTERFACE_NAME",
        "org.rust.TYPE_ALIAS": "DEFAULT_CLASS_NAME",
        "org.rust.TYPE_PARAMETER": "TYPE_PARAMETER_NAME_ATTRIBUTES",
        "org.rust.PRIMITIVE_TYPE": S("type.builtin"),
        "org.rust.ENUM_VARIANT": S("constant"),
        "org.rust.CONSTANT": S("constant"),
        "org.rust.STATIC": S("constant"),
        "org.rust.FIELD": "DEFAULT_INSTANCE_FIELD",
        "org.rust.FUNCTION": "DEFAULT_FUNCTION_DECLARATION",
        "org.rust.FUNCTION_CALL": "DEFAULT_FUNCTION_CALL",
        "org.rust.METHOD": "DEFAULT_INSTANCE_METHOD",
        "org.rust.METHOD_CALL": "DEFAULT_FUNCTION_CALL",
        "org.rust.ASSOC_FUNCTION": "DEFAULT_STATIC_METHOD",
        "org.rust.ASSOC_FUNCTION_CALL": "DEFAULT_STATIC_METHOD",
        "org.rust.MACRO": A(fg=f.clay),
        "org.rust.MACRO_EXCL": A(fg=f.clay),
        "org.rust.ATTRIBUTE": S("decorator"),
        "org.rust.LIFETIME": S("decorator"),
        "org.rust.SELF_PARAMETER": S("variable.builtin"),
        "org.rust.MUT_SELF_PARAMETER": S("variable.builtin"),
        "org.rust.SELF_EXPRESSION": S("variable.builtin"),
        "org.rust.PARAMETER": "DEFAULT_PARAMETER",
        "org.rust.MUT_PARAMETER": "DEFAULT_REASSIGNED_PARAMETER",
        "org.rust.VARIABLE": S("variable"),
        "org.rust.MUT_BINDING": "DEFAULT_REASSIGNED_LOCAL_VARIABLE",
        "org.rust.Q_OPERATOR": S("keyword"),
        "org.rust.DOC_LINK": S("link"),
        "org.rust.CFG_DISABLED_CODE": A(fg=f.overlay0),
        "org.rust.UNSAFE_CODE": A(),
        # ── Go ──
        "GO_PACKAGE": S("namespace"),
        "GO_TYPE_REFERENCE": S("type"),
        "GO_BUILTIN_TYPE_REFERENCE": S("type.builtin"),
        "GO_BUILTIN_FUNCTION_CALL": S("function.builtin"),
        "GO_BUILTIN_CONSTANT": S("constant"),
        "GO_BUILTIN_VARIABLE": S("variable.builtin"),
        "GO_LOCAL_CONSTANT": S("constant"),
        "GO_PACKAGE_LOCAL_CONSTANT": S("constant"),
        "GO_PACKAGE_EXPORTED_CONSTANT": S("constant"),
        "GO_METHOD_RECEIVER": S("variable.builtin"),
        "GO_STRUCT_EXPORTED_MEMBER": "DEFAULT_INSTANCE_FIELD",
        "GO_STRUCT_LOCAL_MEMBER": "DEFAULT_INSTANCE_FIELD",
        "GO_EXPORTED_FUNCTION_CALL": "DEFAULT_FUNCTION_CALL",
        "GO_LOCAL_FUNCTION_CALL": "DEFAULT_FUNCTION_CALL",
        "GO_COMMENT_REFERENCE": A(fg=f.overlay2, st={"italic"}),
        # ── XML / HTML ──
        "XML_TAG": "DEFAULT_TAG",
        "XML_TAG_NAME": S("tag"),
        "XML_CUSTOM_TAG_NAME": "XML_TAG_NAME",
        "XML_ATTRIBUTE_NAME": "DEFAULT_ATTRIBUTE",
        "XML_ATTRIBUTE_VALUE": "DEFAULT_STRING",
        "XML_ENTITY_REFERENCE": "DEFAULT_ENTITY",
        "XML_NS_PREFIX": S("namespace"),
        "XML_PROLOGUE": S("decorator"),
        "XML_TAG_DATA": "TEXT",
        "HTML_TAG": "DEFAULT_TAG",
        "HTML_TAG_NAME": S("tag"),
        "HTML_CUSTOM_TAG_NAME": "HTML_TAG_NAME",
        "HTML_ATTRIBUTE_NAME": "DEFAULT_ATTRIBUTE",
        "HTML_ATTRIBUTE_VALUE": "DEFAULT_STRING",
        "HTML_ENTITY_REFERENCE": "DEFAULT_ENTITY",
        # ── CSS ──
        "CSS.TAG_NAME": S("tag"),
        "CSS.CLASS_NAME": S("attribute"),
        "CSS.HASH": S("attribute"),
        "CSS.PSEUDO": A(fg=f.clay),
        "CSS.PROPERTY_NAME": S("property"),
        "CSS.PROPERTY_VALUE": A(fg=f.text),
        "CSS.IDENT": A(fg=f.text),
        "CSS.KEYWORD": S("keyword"),
        "CSS.IMPORTANT": A(fg=f.orange, st={"bold"}),
        "CSS.FUNCTION": S("function"),
        "CSS.COLOR": S("constant"),
        "CSS.NUMBER": S("number"),
        "CSS.UNIT": S("number"),
        "CSS.URL": S("link"),
        "CSS.STRING": "DEFAULT_STRING",
        "CSS.BRACKETS": S("punctuation"),
        "CSS.OPERATORS": S("operator"),
        "SASS_VARIABLE": S("variable"),
        "SASS_MIXIN": S("function"),
        "LESS_VARIABLE": S("variable"),
        # ── Markdown ──
        **{f"MARKDOWN_HEADER_LEVEL_{i + 1}": A(fg=c, st={"bold"})
           for i, c in enumerate([f.orange, f.yellow, f.green, f.sage, f.clay, f.subtext1])},
        "MARKDOWN_BOLD": S("strong"),
        "MARKDOWN_ITALIC": S("emphasis"),
        "MARKDOWN_STRIKETHROUGH": A(fg=f.overlay1, effect=f.overlay1, etype=STRIKE),
        "MARKDOWN_BOLD_MARKER": S("punctuation"),
        "MARKDOWN_ITALIC_MARKER": S("punctuation"),
        "MARKDOWN_CODE_SPAN": S("code"),
        "MARKDOWN_CODE_SPAN_MARKER": S("punctuation"),
        "MARKDOWN_CODE_BLOCK": S("code"),
        "MARKDOWN_CODE_FENCE": S("code"),
        "MARKDOWN_CODE_FENCE_MARKER": S("punctuation"),
        "MARKDOWN_CODE_FENCE_LANGUAGE": A(fg=f.sage),
        "MARKDOWN_BLOCK_QUOTE": S("quote"),
        "MARKDOWN_BLOCK_QUOTE_MARKER": S("punctuation"),
        "MARKDOWN_LIST_MARKER": A(fg=f.orange),
        "MARKDOWN_LIST_ITEM": A(fg=f.text),
        "MARKDOWN_ORDERED_LIST": A(fg=f.text),
        "MARKDOWN_UNORDERED_LIST": A(fg=f.text),
        "MARKDOWN_LINK_TEXT": A(fg=f.sage),
        "MARKDOWN_LINK_LABEL": A(fg=f.sage),
        "MARKDOWN_LINK_DESTINATION": A(fg=f.denim, effect=f.denim, etype=UNDERLINE),
        "MARKDOWN_LINK_TITLE": A(fg=f.subtext0, st={"italic"}),
        "MARKDOWN_AUTO_LINK": A(fg=f.denim, effect=f.denim, etype=UNDERLINE),
        "MARKDOWN_HRULE": A(fg=f.overlay1),
        "MARKDOWN_TABLE_SEPARATOR": A(fg=f.overlay1),
        "MARKDOWN_HTML_BLOCK": A(fg=f.text),
        # ── data & config: JSON, YAML, TOML, properties, INI ──
        "JSON.PROPERTY_KEY": S("function"),
        "JSON.KEYWORD": S("constant"),
        "YAML_SCALAR_KEY": S("function"),
        "YAML_SCALAR_VALUE": S("string"),
        "YAML_SCALAR_STRING": S("string"),
        "YAML_SCALAR_DSTRING": S("string"),
        "YAML_SCALAR_LIST": S("string"),
        "YAML_TEXT": S("string"),
        "YAML_ANCHOR": A(fg=f.clay),
        "YAML_SIGN": S("punctuation"),
        "org.toml.KEY": S("function"),
        "PROPERTIES.KEY": S("function"),
        "PROPERTIES.VALUE": S("string"),
        "PROPERTIES.KEY_VALUE_SEPARATOR": "DEFAULT_OPERATION_SIGN",
        "PROPERTIES.VALID_STRING_ESCAPE": "DEFAULT_VALID_STRING_ESCAPE",
        "PROPERTIES.INVALID_STRING_ESCAPE": "DEFAULT_INVALID_STRING_ESCAPE",
        "INI.SECTION": S("heading"),
        # ── shell ──
        "BASH.EXTERNAL_COMMAND": S("function"),
        "BASH.INTERNAL_COMMAND": S("function.builtin"),
        "BASH.FUNCTION_DEF_NAME": S("function"),
        "BASH.VAR_USE_BUILTIN": S("variable.builtin"),
        "BASH.SHEBANG": S("comment"),
        "BASH.HERE_DOC": S("string"),
        "BASH.HERE_DOC_START": "DEFAULT_KEYWORD",
        "BASH.HERE_DOC_END": "DEFAULT_KEYWORD",
        # ── regular expressions ──
        "REGEXP.CHARACTER": S("string"),
        "REGEXP.META": A(fg=f.clay, st={"bold"}),
        "REGEXP.ESC_CHARACTER": S("regexp"),
        "REGEXP.CHAR_CLASS": S("regexp"),
        "REGEXP.QUANTIFIER": S("regexp"),
        "REGEXP.QUOTE_CHARACTER": S("regexp"),
        "REGEXP.BRACES": S("regexp"),
        "REGEXP.BRACKETS": S("regexp"),
        "REGEXP.PARENTHS": S("regexp"),
        "REGEXP.REDUNDANT_ESCAPE": "DEFAULT_VALID_STRING_ESCAPE",
    }
    # the 16 console colours, straight from the flavor's ANSI palette
    names = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"]
    for i, n in enumerate(names):
        attrs[f"CONSOLE_{n}_OUTPUT"] = A(fg=ansi[i])
        attrs[f"BLOCK_TERMINAL_{n}"] = A(fg=ansi[i], bg=ansi[i])
        if i:
            attrs[f"CONSOLE_{n}_BRIGHT_OUTPUT"] = A(fg=ansi[i + 8])
        attrs[f"BLOCK_TERMINAL_{n}_BRIGHT"] = A(fg=ansi[i + 8], bg=ansi[i + 8])
    attrs["CONSOLE_GRAY_OUTPUT"] = A(fg=ansi[7])  # ANSI white
    attrs["CONSOLE_DARKGRAY_OUTPUT"] = A(fg=ansi[8])  # bright black
    attrs["CONSOLE_WHITE_OUTPUT"] = A(fg=ansi[15])  # bright white
    attrs["BLOCK_TERMINAL_WHITE"] = A(fg=ansi[7], bg=ansi[7])
    attrs["BLOCK_TERMINAL_WHITE_BRIGHT"] = A(fg=ansi[15], bg=ansi[15])
    return attrs


def rainbow(f):
    stripe = [f.yellow, f.orange, f.sage, f.clay, f.green]  # VS Code's bracket-pair order
    out = {}
    for kind in ("ROUND", "SQUARE", "SQUIGGLY", "ANGLE"):
        for i, c in enumerate(stripe):
            out[f"{kind}_BRACKETS_RAINBOW_COLOR{i}"] = A(fg=c)
    for i, c in enumerate(stripe):
        out[f"INDENT_GUIDES_RAINBOW_COLOR{i}"] = A(fg=f.mix(c, "base", 0.35))
        out[f"RAINBOW_COLOR{i}"] = A(fg=f.mix(c, "text", 0.6))  # semantic highlighting
    for i, c in enumerate([f.orange, f.yellow, f.green, f.sage, f.denim, f.clay]):
        out[f"CodeWithMe.USER_{i + 1}_MARKER"] = A(bg=c)
        out[f"CodeWithMe.USER_{i + 1}_SELECTION"] = A(bg=f.mix(c, "base", 0.3))
    return out


def icls(f):
    def value(a):
        rows = []
        if a["fg"]:
            rows.append(("FOREGROUND", h(a["fg"])))
        if a["bg"]:
            rows.append(("BACKGROUND", h(a["bg"])))
        font = (BOLD if "bold" in a["st"] else 0) | (ITALIC if "italic" in a["st"] else 0)
        if font:
            rows.append(("FONT_TYPE", str(font)))
        if a["effect"]:
            rows.append(("EFFECT_COLOR", h(a["effect"])))
            if a["etype"] is not None:
                rows.append(("EFFECT_TYPE", str(a["etype"])))
        if a["stripe"]:
            rows.append(("ERROR_STRIPE_COLOR", h(a["stripe"])))
        if not rows:
            return "      <value/>"
        body = "\n".join(f'        <option name="{k}" value="{v}"/>' for k, v in rows)
        return f"      <value>\n{body}\n      </value>"

    col = colors(f)
    color_lines = "\n".join(
        f'    <option name={quoteattr(k)} value="{h(v) if v else ""}"/>' for k, v in sorted(col.items())
    )
    attr_lines = []
    for name, a in sorted(attributes(f).items()):
        if isinstance(a, str):
            attr_lines.append(f"    <option name={quoteattr(name)} baseAttributes={quoteattr(a)}/>")
        else:
            attr_lines.append(f"    <option name={quoteattr(name)}>\n{value(a)}\n    </option>")
    parent = "Darcula" if f.dark else "Default"
    return f"""<!-- {HEADER} -->
<scheme name={quoteattr(f.name)} version="142" parent_scheme="{parent}">
  <metaInfo>
    <property name="ide">idea</property>
    <property name="originalScheme">{escape(f.name)}</property>
  </metaInfo>
  <colors>
{color_lines}
  </colors>
  <attributes>
{"\n".join(attr_lines)}
  </attributes>
</scheme>
"""


# ── UI theme (.theme.json) ──────────────────────────────────────────────────
def theme(f):
    u = ui(f)
    named = {r: f.colors[r] for r in p.ROLES}
    named.update({
        "ink": u["ink"],
        "accent": f.orange,
        "accentHover": f.orange_hi,
        "focus": f.mix("orange", "mantle", 0.6),
        "editorBackground": f.base,
        "panelBackground": f.mantle,
        "barBackground": f.crust,
        "popupBackground": f.mantle,
        "inputBackground": f.crust,
        "hoverBackground": f.surface0,
        "pressedBackground": f.surface1,
        "selectionBackground": f.surface1,
        "selectionInactiveBackground": f.surface0,
        "borderColor": f.crust,
        "separatorColor": f.surface0,
        "controlBorder": f.surface1,
        "searchMatch": u["search"],
        "errorBackground": f.mix("red", "mantle", 0.14),
        "warningBackground": f.mix("yellow", "mantle", 0.12),
        "infoBackground": f.mix("denim", "mantle", 0.12),
        "errorBorder": f.mix("red", "mantle", 0.45),
        "warningBorder": f.mix("yellow", "mantle", 0.4),
        "infoBorder": f.mix("denim", "mantle", 0.4),
    })
    fc = lambda c: f.mix(c, "mantle", 0.16)  # file colours: a faint wash
    theme_ui = {
        "*": {
            "background": "panelBackground",
            "foreground": "subtext1",
            "infoForeground": "overlay1",
            "disabledForeground": "overlay0",
            "disabledBackground": "panelBackground",
            "inactiveBackground": "panelBackground",
            "inactiveForeground": "overlay0",
            "selectionBackground": "selectionBackground",
            "selectionForeground": "text_hi",
            "selectionInactiveBackground": "selectionInactiveBackground",
            "selectionInactiveForeground": "text",
            "selectionBackgroundInactive": "selectionInactiveBackground",
            "hoverBackground": "hoverBackground",
            "borderColor": "borderColor",
            "separatorColor": "separatorColor",
            "focusColor": "focus",
            "focusedBorderColor": "focus",
            "errorForeground": "red_hi",
            "acceleratorForeground": "overlay1",
            "acceleratorSelectionForeground": "subtext1",
        },
        "ActionButton": {
            "hoverBackground": "hoverBackground", "hoverBorderColor": "hoverBackground",
            "pressedBackground": "pressedBackground", "pressedBorderColor": "pressedBackground",
            "focusedBorderColor": "focus",
        },
        "Banner": {
            "errorBackground": "errorBackground", "errorBorderColor": "errorBorder",
            "warningBackground": "warningBackground", "warningBorderColor": "warningBorder",
            "infoBackground": "infoBackground", "infoBorderColor": "infoBorder",
            "successBackground": f.mix("green", "mantle", 0.12), "successBorderColor": f.mix("green", "mantle", 0.4),
            "foreground": "text",
        },
        "Bookmark": {
            "iconBackground": "accent",
            "Mnemonic": {"iconBackground": "surface0", "iconBorderColor": "accent", "iconForeground": "text"},
            "MnemonicAssigned": {"background": "surface1", "borderColor": "surface2", "foreground": "text"},
            "MnemonicCurrent": {"background": "accent", "borderColor": "accent", "foreground": "ink"},
            "MnemonicAvailable": {"background": "panelBackground", "borderColor": "controlBorder", "foreground": "subtext1"},
        },
        "BookmarkMnemonicAssigned": {"background": "surface1", "borderColor": "surface2", "foreground": "text"},
        "Borders": {"color": "borderColor", "ContrastBorderColor": "borderColor"},
        "Button": {
            "startBackground": "surface1", "endBackground": "surface1",
            "startBorderColor": "surface1", "endBorderColor": "surface1",
            "foreground": "text", "focusedBorderColor": "focus", "disabledBorderColor": "surface0",
            "disabledText": "overlay0", "shadowColor": "borderColor",
            "default": {
                "startBackground": "accent", "endBackground": "accent",
                "startBorderColor": "accent", "endBorderColor": "accent",
                "foreground": "ink", "focusColor": "focus", "focusedBorderColor": "accentHover",
                "shadowColor": "borderColor",
            },
        },
        "CheckBox": {"background": "panelBackground", "foreground": "subtext1"},
        "CheckBoxMenuItem": {"selectionBackground": "selectionBackground", "selectionForeground": "text_hi"},
        "ColorChooser": {"background": "panelBackground", "swatchesDefaultRecentColor": "surface2"},
        "ComboBox": {
            "background": "inputBackground", "foreground": "text",
            "nonEditableBackground": "surface0", "disabledForeground": "overlay0",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "modifiedItemForeground": "accent",
            "ArrowButton": {
                "background": "surface0", "nonEditableBackground": "surface0",
                "iconColor": "subtext0", "disabledIconColor": "overlay0",
            },
        },
        "ComboBoxButton": {"background": "surface0"},
        "CompletionPopup": {
            "background": "popupBackground", "foreground": "subtext1",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "selectionInactiveBackground": "selectionInactiveBackground",
            "matchForeground": "yellow", "matchSelectionForeground": "yellow_hi",
            "selectionInfoForeground": "overlay2", "infoForeground": "overlay1",
            "Advertiser": {"background": "barBackground", "foreground": "overlay1"},
        },
        "Component": {
            "borderColor": "controlBorder", "focusColor": "focus", "focusedBorderColor": "focus",
            "disabledBorderColor": "surface0", "hoverIconColor": "text", "iconColor": "subtext0",
            "infoForeground": "overlay1",
            "errorFocusColor": "red_hi", "inactiveErrorFocusColor": "errorBorder",
            "warningFocusColor": "yellow", "inactiveWarningFocusColor": "warningBorder",
        },
        "Counter": {"background": "accent", "foreground": "ink"},
        "Debugger": {
            "Variables": {
                "valueForeground": "green", "stringForeground": "green", "numberForeground": "red_hi",
                "typeForeground": "sage", "changedValueForeground": "orange", "modifyingValueForeground": "yellow",
                "errorMessageForeground": "red_hi", "exceptionForeground": "red_hi",
                "collectingDataForeground": "overlay1", "evaluatingExpressionForeground": "overlay1",
            },
        },
        "DebuggerPopup": {"borderColor": "controlBorder"},
        "DefaultTabs": {
            "background": "panelBackground", "borderColor": "borderColor", "foreground": "subtext0",
            "hoverBackground": "hoverBackground", "inactiveUnderlineColor": "overlay0",
            "underlineColor": "accent", "underlinedTabBackground": "editorBackground",
            "underlinedTabForeground": "text_hi",
        },
        "DragAndDrop": {
            "areaBackground": f.mix("orange", "mantle", 0.12), "areaBorderColor": "accent",
            "areaForeground": "text", "borderColor": "accent",
            "rowBackground": f.mix("orange", "mantle", 0.15),
        },
        "Editor": {
            "background": "editorBackground", "foreground": "text", "shortcutForeground": "yellow",
            "SearchField": {"background": "inputBackground", "borderColor": "controlBorder"},
            "Toolbar": {"borderColor": "separatorColor"},
        },
        "EditorPane": {
            "background": "editorBackground", "foreground": "text",
            "inactiveBackground": "panelBackground", "splitBorder": "borderColor",
        },
        "EditorTabs": {
            "background": "panelBackground", "borderColor": "borderColor", "underTabsBorderColor": "borderColor",
            "hoverBackground": "hoverBackground", "inactiveColoredFileBackground": "panelBackground",
            "selectedBackground": "editorBackground", "selectedForeground": "text_hi",
            "underlinedTabBackground": "editorBackground", "underlinedTabForeground": "text_hi",
            "inactiveUnderlinedTabBackground": "editorBackground", "inactiveUnderlinedTabForeground": "subtext0",
            "underlineColor": "accent", "inactiveUnderlineColor": "overlay0",
        },
        "FileColor": {
            "Blue": fc("denim"), "Green": fc("green"), "Orange": fc("orange"), "Rose": fc("red"),
            "Violet": fc("clay"), "Yellow": fc("yellow"), "Gray": fc("overlay0"),
        },
        "FormattedTextField": {"background": "inputBackground", "foreground": "text"},
        "GotItTooltip": {
            "background": "popupBackground", "foreground": "text", "borderColor": "controlBorder",
            "linkForeground": "denim", "shortcutForeground": "yellow", "codeForeground": "green",
            "stepForeground": "overlay1", "Button": {"foreground": "ink", "startBackground": "accent", "endBackground": "accent"},
        },
        "Group": {"separatorColor": "separatorColor", "disabledSeparatorColor": "separatorColor"},
        "InplaceRefactoringPopup": {"background": "popupBackground", "borderColor": "controlBorder"},
        "Label": {
            "foreground": "subtext1", "disabledForeground": "overlay0", "infoForeground": "overlay1",
            "errorForeground": "red_hi", "selectedForeground": "text_hi", "selectedDisabledForeground": "overlay1",
        },
        "Link": {
            "activeForeground": "denim", "hoverForeground": "denim_hi", "pressedForeground": "denim_hi",
            "visitedForeground": "denim", "secondaryForeground": "overlay1",
        },
        "List": {
            "background": "panelBackground", "foreground": "subtext1",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "selectionInactiveBackground": "selectionInactiveBackground", "selectionInactiveForeground": "text",
            "hoverBackground": "hoverBackground", "hoverInactiveBackground": "hoverBackground",
            "dropLineColor": "accent", "Button": {"hoverBackground": "hoverBackground"},
            "Tag": {"background": "surface0", "foreground": "subtext1"},
        },
        "MainMenu": {
            "background": "barBackground", "foreground": "subtext1",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
        },
        "MainToolbar": {
            "background": "barBackground", "inactiveBackground": "barBackground",
            "foreground": "subtext0", "inactiveForeground": "overlay0", "separatorColor": "separatorColor",
            "borderColor": "borderColor",
            "Icon": {"hoverBackground": "hoverBackground", "pressedBackground": "pressedBackground"},
            "Dropdown": {"hoverBackground": "hoverBackground", "pressedBackground": "pressedBackground"},
            "SplitDropdown": {"hoverBackground": "hoverBackground", "separatorColor": "separatorColor"},
        },
        "MainWindow": {
            "Tab": {
                "background": "barBackground", "foreground": "overlay1", "borderColor": "borderColor",
                "hoverBackground": "hoverBackground", "hoverForeground": "text",
                "selectedBackground": "panelBackground", "selectedForeground": "text_hi",
                "selectedInactiveBackground": "panelBackground", "separatorColor": "separatorColor",
            },
        },
        "MemoryIndicator": {"allocatedBackground": "surface0", "usedBackground": "surface1"},
        "Menu": {
            "background": "popupBackground", "foreground": "text", "borderColor": "controlBorder",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "separatorColor": "surface1", "disabledForeground": "overlay0",
            "acceleratorForeground": "overlay1", "acceleratorSelectionForeground": "subtext1",
        },
        "MenuBar": {
            "background": "barBackground", "foreground": "subtext1", "borderColor": "borderColor",
            "selectionBackground": "hoverBackground", "selectionForeground": "text",
        },
        "MenuItem": {
            "background": "popupBackground", "foreground": "text",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "disabledForeground": "overlay0",
            "acceleratorForeground": "overlay1", "acceleratorSelectionForeground": "subtext1",
        },
        "NavBar": {"borderColor": "borderColor"},
        "NewClass": {
            "Panel": {"background": "popupBackground"},
            "SearchField": {"background": "inputBackground"},
        },
        "Notification": {
            "background": "popupBackground", "foreground": "text", "borderColor": "controlBorder",
            "errorBackground": "errorBackground", "errorBorderColor": "errorBorder", "errorForeground": "text",
            "linkForeground": "denim", "iconHoverBackground": "hoverBackground",
            "MoreButton": {"background": "surface0", "foreground": "subtext1", "innerBorderColor": "surface1"},
            "Shadow": {"bottom0Color": "#00000000", "bottom1Color": "#00000000"},
            "ToolWindow": {
                "errorBackground": "errorBackground", "errorBorderColor": "errorBorder", "errorForeground": "text",
                "warningBackground": "warningBackground", "warningBorderColor": "warningBorder", "warningForeground": "text",
                "informativeBackground": "infoBackground", "informativeBorderColor": "infoBorder",
                "informativeForeground": "text",
            },
        },
        "NotificationsToolwindow": {
            "newNotification": {"background": "surface0", "hoverBackground": "surface1"},
            "Notification": {"hoverBackground": "hoverBackground"},
        },
        "OnePixelDivider": {"background": "borderColor"},
        "OptionPane": {"background": "panelBackground", "foreground": "subtext1", "messageForeground": "text"},
        "Panel": {"background": "panelBackground", "foreground": "subtext1"},
        "ParameterInfo": {
            "background": "popupBackground", "foreground": "subtext1", "borderColor": "controlBorder",
            "currentOverloadBackground": "selectionBackground", "currentParameterForeground": "yellow_hi",
            "disabledForeground": "overlay0", "infoForeground": "overlay1", "lineSeparatorColor": "surface1",
        },
        "PasswordField": {"background": "inputBackground", "foreground": "text", "capsLockIconColor": "yellow"},
        "Plugins": {
            "background": "panelBackground", "borderColor": "borderColor",
            "hoverBackground": "hoverBackground", "lightSelectionBackground": "selectionBackground",
            "tagBackground": "surface0", "tagForeground": "subtext1",
            "disabledForeground": "overlay0", "eapTagBackground": "surface1",
            "paidTagBackground": "surface1", "trialTagBackground": "surface1",
            "SearchField": {"background": "inputBackground", "borderColor": "controlBorder"},
            "SectionHeader": {"background": "panelBackground", "foreground": "subtext1"},
            "Tab": {
                "hoverBackground": "hoverBackground", "selectedBackground": "selectionBackground",
                "selectedForeground": "text_hi",
            },
            "Button": {
                "installBackground": "panelBackground", "installBorderColor": "green",
                "installForeground": "green", "installFillBackground": "green", "installFillForeground": "ink",
                "installFocusedBackground": "surface0",
                "updateBackground": "accent", "updateBorderColor": "accent", "updateForeground": "ink",
            },
        },
        "Popup": {
            "background": "popupBackground", "borderColor": "controlBorder",
            "inactiveBorderColor": "separatorColor", "innerBorderColor": "separatorColor",
            "separatorColor": "surface1", "separatorForeground": "overlay1",
            "paintBorder": True, "borderWidth": 1,
            "Header": {"activeBackground": "barBackground", "inactiveBackground": "barBackground", "foreground": "subtext1"},
            "Toolbar": {"background": "barBackground", "borderColor": "separatorColor"},
            "Advertiser": {"background": "barBackground", "foreground": "overlay1", "borderColor": "separatorColor"},
        },
        "PopupMenu": {
            "background": "popupBackground", "foreground": "text", "borderColor": "controlBorder",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "translucentBackground": "popupBackground",
        },
        "ProgressBar": {
            "trackColor": "surface1", "progressColor": "accent",
            "indeterminateStartColor": "accent", "indeterminateEndColor": "yellow",
            "passedColor": "green", "passedEndColor": "green_hi",
            "failedColor": "red_hi", "failedEndColor": "red",
            "warningColor": "yellow", "warningEndColor": "yellow_hi",
            "selectionForeground": "ink", "selectionBackground": "text",
        },
        "RadioButton": {"background": "panelBackground", "foreground": "subtext1"},
        "RadioButtonMenuItem": {"selectionBackground": "selectionBackground", "selectionForeground": "text_hi"},
        "RunWidget": {
            "background": "surface0", "foreground": "text", "iconColor": "subtext1",
            "hoverBackground": "surface1", "pressedBackground": "surface2", "separatorColor": "separatorColor",
            "runningBackground": "green", "runningForeground": "ink", "runningIconColor": "ink",
            "stopBackground": "red", "Running": {"background": "green", "foreground": "ink"},
        },
        "ScrollBar": {
            "background": "panelBackground", "trackColor": "#00000000",
            "thumbColor": "surface1", "thumbBorderColor": "surface1",
            "hoverTrackColor": "#00000000", "hoverThumbColor": "surface2", "hoverThumbBorderColor": "surface2",
            "Mac": {
                "trackColor": "#00000000", "hoverTrackColor": "#00000000",
                "thumbColor": "surface1", "thumbBorderColor": "surface1",
                "hoverThumbColor": "surface2", "hoverThumbBorderColor": "surface2",
                "Transparent": {
                    "thumbColor": "surface1", "thumbBorderColor": "surface1",
                    "hoverThumbColor": "surface2", "hoverThumbBorderColor": "surface2",
                },
            },
            "Transparent": {
                "thumbColor": "surface1", "thumbBorderColor": "surface1",
                "hoverThumbColor": "surface2", "hoverThumbBorderColor": "surface2",
            },
        },
        "SearchEverywhere": {
            "Header": {"background": "popupBackground"},
            "Advertiser": {"background": "barBackground", "foreground": "overlay1"},
            "List": {"separatorColor": "separatorColor", "separatorForeground": "overlay1"},
            "SearchField": {"background": "inputBackground", "borderColor": "controlBorder", "infoForeground": "overlay0"},
            "Tab": {"selectedBackground": "selectionBackground", "selectedForeground": "text_hi"},
        },
        "SearchFieldWithExtension": {"background": "inputBackground"},
        "SearchMatch": {"startBackground": "searchMatch", "endBackground": "searchMatch"},
        "SegmentedButton": {
            "selectedButtonColor": "surface1", "focusedSelectedButtonColor": "surface2",
            "selectedStartBorderColor": "surface1", "selectedEndBorderColor": "surface1",
        },
        "Separator": {"separatorColor": "separatorColor"},
        "SidePanel": {"background": "panelBackground"},
        "Slider": {
            "background": "panelBackground", "buttonColor": "subtext1", "buttonBorderColor": "surface2",
            "trackColor": "surface1", "tickColor": "overlay0",
        },
        "SpeedSearch": {
            "background": "surface0", "borderColor": "controlBorder",
            "foreground": "text", "errorForeground": "red_hi",
        },
        "StatusBar": {
            "background": "barBackground", "borderColor": "borderColor", "hoverBackground": "hoverBackground",
            "Widget": {"hoverBackground": "hoverBackground", "pressedBackground": "pressedBackground",
                       "hoverForeground": "text", "foreground": "subtext0"},
            "Breadcrumbs": {
                "foreground": "subtext0", "hoverBackground": "hoverBackground", "hoverForeground": "text",
                "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
                "selectionInactiveBackground": "selectionInactiveBackground",
                "floatingBackground": "popupBackground", "floatingForeground": "subtext1",
            },
        },
        "TabbedPane": {
            "background": "panelBackground", "foreground": "subtext0", "contentAreaColor": "borderColor",
            "focusColor": "surface0", "hoverColor": "hoverBackground", "underlineColor": "accent",
            "disabledUnderlineColor": "overlay0", "disabledForeground": "overlay0",
        },
        "Table": {
            "background": "panelBackground", "foreground": "subtext1", "gridColor": "separatorColor",
            "hoverBackground": "hoverBackground", "hoverInactiveBackground": "hoverBackground",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "selectionInactiveBackground": "selectionInactiveBackground", "selectionInactiveForeground": "text",
            "lightSelectionBackground": "surface0", "lightSelectionForeground": "text",
            "lightSelectionInactiveBackground": "surface0",
            "stripeColor": f.mix("surface0", "mantle", 0.4), "dropLineColor": "accent",
            "sortIconColor": "overlay1", "focusCellBackground": "selectionBackground",
        },
        "TableHeader": {
            "background": "panelBackground", "foreground": "subtext0",
            "bottomSeparatorColor": "separatorColor", "separatorColor": "separatorColor",
        },
        "TextArea": {
            "background": "inputBackground", "foreground": "text",
            "selectionBackground": u["selection"], "caretForeground": u["cursor"],
        },
        "TextField": {
            "background": "inputBackground", "foreground": "text", "borderColor": "controlBorder",
            "focusedBorderColor": "focus", "inactiveForeground": "overlay0",
            "selectionBackground": u["selection"], "selectionForeground": "text_hi",
            "caretForeground": u["cursor"],
        },
        "TextPane": {"background": "panelBackground", "foreground": "text", "caretForeground": u["cursor"]},
        "TitlePane": {
            "background": "barBackground", "inactiveBackground": "barBackground",
            "foreground": "subtext0", "inactiveForeground": "overlay0",
            "infoForeground": "overlay1", "inactiveInfoForeground": "overlay0",
            "Button": {"hoverBackground": "hoverBackground"},
        },
        "ToggleButton": {
            "onBackground": "accent", "onForeground": "ink",
            "offBackground": "surface1", "offForeground": "overlay1",
            "buttonColor": "text_hi" if f.dark else "base", "borderColor": "surface2",
        },
        "ToolBar": {"background": "panelBackground", "borderHandleColor": "surface2", "separatorColor": "separatorColor"},
        "ToolTip": {
            "background": "popupBackground", "foreground": "text", "borderColor": "controlBorder",
            "infoForeground": "overlay1", "shortcutForeground": "yellow", "linkForeground": "denim",
            "Actions": {"background": "barBackground", "infoForeground": "overlay1"},
        },
        "ToolWindow": {
            "background": "panelBackground",
            "Header": {
                "background": "panelBackground", "inactiveBackground": "panelBackground",
                "borderColor": "borderColor",
            },
            "HeaderTab": {
                "hoverBackground": "hoverBackground", "hoverInactiveBackground": "hoverBackground",
                "selectedInactiveBackground": "selectionInactiveBackground",
                "underlineColor": "accent", "inactiveUnderlineColor": "overlay0",
                "underlinedTabBackground": "selectionInactiveBackground",
                "underlinedTabInactiveBackground": "panelBackground",
            },
            "Button": {
                "hoverBackground": "hoverBackground", "selectedBackground": "selectionBackground",
                "selectedForeground": "text_hi",
            },
            "Stripe": {"background": "barBackground", "borderColor": "borderColor"},
        },
        "Tree": {
            "background": "panelBackground", "foreground": "subtext1",
            "selectionBackground": "selectionBackground", "selectionForeground": "text_hi",
            "selectionInactiveBackground": "selectionInactiveBackground", "selectionInactiveForeground": "text",
            "hoverBackground": "hoverBackground", "hoverInactiveBackground": "hoverBackground",
            "modifiedItemForeground": "yellow", "errorForeground": "red_hi", "hash": "surface1",
        },
        "ValidationTooltip": {
            "errorBackground": "errorBackground", "errorBorderColor": "errorBorder",
            "warningBackground": "warningBackground", "warningBorderColor": "warningBorder",
        },
        "VersionControl": {
            "FileHistory": {"Commit": {"selectedBranchBackground": "surface0"}},
            "GitLog": {
                "headIconColor": "yellow", "localBranchIconColor": "green",
                "remoteBranchIconColor": "denim", "tagIconColor": "orange", "otherIconColor": "sage",
            },
            "Log": {
                "Commit": {
                    "currentBranchBackground": f.mix("orange", "mantle", 0.06),
                    "hoveredBackground": "hoverBackground", "unmatchedForeground": "overlay0",
                    "selectionInactiveBackground": "selectionInactiveBackground",
                },
            },
            "RefLabel": {"foreground": "text"},
            "MarkerPopup": {"borderColor": "controlBorder", "Toolbar": {"background": "barBackground"}},
        },
        "WelcomeScreen": {
            "background": "panelBackground", "separatorColor": "separatorColor",
            "SidePanel": {"background": "barBackground"},
            "Details": {"background": "panelBackground"},
            "Projects": {
                "background": "panelBackground", "selectionBackground": "selectionBackground",
                "selectionInactiveBackground": "selectionInactiveBackground",
                "actions": {"background": "surface0", "selectionBackground": "surface1"},
            },
        },
    }
    icons = {
        "Actions.Blue": f.denim, "Actions.Green": f.green, "Actions.Grey": f.overlay1,
        "Actions.GreyInline": f.overlay1, "Actions.GreyInline.Dark": f.overlay1,
        "Actions.Red": f.red_hi, "Actions.Yellow": f.yellow,
        "Objects.BlackText": u["ink"], "Objects.Blue": f.denim, "Objects.Green": f.green,
        "Objects.GreenAndroid": f.green, "Objects.Grey": f.overlay1, "Objects.Pink": f.clay,
        "Objects.Purple": f.clay, "Objects.Red": f.red_hi, "Objects.RedStatus": f.red_hi,
        "Objects.Yellow": f.yellow, "Objects.YellowDark": f.orange,
        "Tree.iconColor": f.subtext0,
    }
    for suffix in ("", ".Dark"):  # the IDE reads the .Dark variant when the theme is dark
        icons.update({
            f"Checkbox.Background.Default{suffix}": f.crust,
            f"Checkbox.Background.Disabled{suffix}": f.mantle,
            f"Checkbox.Background.Selected{suffix}": f.orange,
            f"Checkbox.Border.Default{suffix}": f.surface2,
            f"Checkbox.Border.Disabled{suffix}": f.surface1,
            f"Checkbox.Border.Selected{suffix}": f.orange,
            f"Checkbox.Foreground.Disabled{suffix}": f.overlay0,
            f"Checkbox.Foreground.Selected{suffix}": u["ink"],
            f"Checkbox.Focus.Wide{suffix}": f.mix("orange", "mantle", 0.6),
            f"Checkbox.Focus.Thin.Default{suffix}": f.orange_hi,
            f"Checkbox.Focus.Thin.Selected{suffix}": f.orange_hi,
        })
    return {
        "name": f.name,
        "dark": f.dark,
        "author": "Oddur Sigurdsson",
        "editorScheme": f"/schemes/{f.slug}.xml",
        "colors": named,
        "ui": theme_ui,
        "icons": {"ColorPalette": icons},
    }


# ── plugin.xml + JAR ────────────────────────────────────────────────────────
def plugin_xml(flavors):
    providers = "\n".join(
        f'    <themeProvider id="{PLUGIN_ID}.{f.id}" path="/themes/{f.slug}.theme.json"/>' for f in flavors
    )
    schemes = "\n".join(
        f'    <bundledColorScheme id="{PLUGIN_ID}.{f.id}.scheme" path="/schemes/{f.slug}"/>' for f in flavors
    )
    names = ", ".join(f"<strong>{f.name}</strong>" for f in flavors)
    return f"""<!-- {HEADER} -->
<idea-plugin>
  <id>{PLUGIN_ID}</id>
  <name>Subway Seat Theme</name>
  <version>{VERSION}</version>
  <vendor url="{REPO}">Oddur Sigurdsson</vendor>
  <idea-version since-build="232"/>
  <description><![CDATA[
<p>A 1970s New York subway car for your IDE: walnut-brown ground, parchment text, harvest gold,
burnt orange and avocado. Three flavors, each a UI theme with a matching editor color scheme:
{names}.</p>
<p>Pick one in <strong>Settings → Appearance &amp; Behavior → Appearance</strong>; the editor scheme
follows, or choose it on its own under <strong>Editor → Color Scheme</strong>.</p>
<p><a href="{REPO}">Source and other ports</a> · MIT license</p>
]]></description>
  <depends>com.intellij.modules.platform</depends>
  <extensions defaultExtensionNs="com.intellij">
{providers}
{schemes}
  </extensions>
</idea-plugin>
"""


def jar(files):
    """A ready-to-install plugin: a zip with META-INF/plugin.xml at its root. Reproducible."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in files:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    return buf.getvalue()


def build(flavors):
    outs, members = [], []
    manifest = "Manifest-Version: 1.0\r\nCreated-By: subway-seat build.py\r\n\r\n"
    members.append(("META-INF/MANIFEST.MF", manifest))
    pxml = plugin_xml(flavors)
    members.append(("META-INF/plugin.xml", pxml))
    for f in flavors:
        scheme = icls(f)
        th = json.dumps(theme(f), indent=2) + "\n"
        members.append((f"themes/{f.slug}.theme.json", th))
        members.append((f"schemes/{f.slug}.xml", scheme))
        outs.append(Out(f"schemes/{f.slug}.icls", scheme, flavor=f.id,
                        dest="Settings → Editor → Color Scheme → ⚙ → Import Scheme… (editor colours only)", lang="xml"))
        outs.append(Out(f"themes/{f.slug}.theme.json", th, flavor=f.id, dest="packaged in the plugin JAR", lang="json"))
    outs.append(Out("META-INF/plugin.xml", pxml, dest="packaged in the plugin JAR", lang="xml"))
    outs.append(Out(JAR, jar(members), dest="Settings → Plugins → ⚙ → Install Plugin from Disk…", lang="text"))
    return outs
