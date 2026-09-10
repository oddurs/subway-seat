"""Godot 4: a text editor theme (.tet) per flavor, plus the interface theme values."""

import palette as p
from ports._editors import ui
from ports._lib import HEADER, Out, ink, resolve

META = {
    "id": "godot",
    "name": "Godot",
    "category": "Editors",
    "homepage": "https://godotengine.org",
    "detect": ["godot", "/Applications/Godot.app", "/Applications/Godot_mono.app"],
    "requires": "Godot 4.0+",
    "enable": {
        "where": "Editor › Editor Settings › Text Editor › Theme",
        "code": "Color Theme: {name}",
        "lang": "text",
    },
    "notes": "The script editor in Subway Seat: gold functions, orange keywords, sage types, avocado strings "
    "and terracotta annotations, with translucent current-line, selection and search layers so error and "
    "warning lines still show through. Godot's own interface takes its colors from a base and an accent "
    "color; the interface file for each flavor lists the values to enter under Interface › Theme.",
}

# Where each .tet key's color comes from: a syntax role, a `ui(f)` key, or a
# layering expression for `resolve` (hue@alpha, so line layers stack).
# Every key Godot saves in a .tet (get_godot2_text_editor_theme on master), sorted.
# Godot skips keys it doesn't know, so one file serves every 4.x: 4.7 has no
# *_underline_color yet, and releases before 4.5/4.6 lack the comment-marker
# and string-placeholder keys.
KEYS = {
    "background_color": "base",
    "base_type_color": "syntax:type.builtin",
    "bookmark_color": "ui:info",
    "brace_mismatch_color": "ui:error",
    "breakpoint_color": "ui:error",
    "caret_background_color": "ink",
    "caret_color": "ui:cursor",
    "code_folding_color": "overlay1",
    "comment_color": "syntax:comment",
    "comment_markers/critical_color": "ui:error",
    "comment_markers/notice_color": "ui:hint",
    "comment_markers/warning_color": "ui:warning",
    "completion_background_color": "paper",
    "completion_existing_color": ("yellow@15", "yellow@22"),
    "completion_font_color": "text",
    "completion_scroll_color": "overlay0",
    "completion_scroll_hovered_color": "overlay1",
    "completion_selected_color": "text@L3",
    "control_flow_keyword_color": "syntax:keyword",
    "current_line_color": "text@L1",
    "doc_comment_color": "overlay2",
    "engine_type_color": "syntax:type",
    "error_underline_color": "ui:error",
    "executing_line_color": "yellow",
    "folded_code_region_color": ("denim@14", "denim@12"),
    "function_color": "syntax:function",
    "gdscript/annotation_color": "syntax:decorator",
    "gdscript/function_definition_color": "syntax:function",
    "gdscript/global_function_color": "syntax:function.builtin",
    "gdscript/node_path_color": "syntax:string.escape",
    "gdscript/node_reference_color": "sage_hi",
    "gdscript/string_name_color": "syntax:constant",
    "keyword_color": "syntax:keyword",
    "line_length_guideline_color": "text@L2",
    "line_number_color": "ui:line_nr",
    "mark_color": ("red@22", "red@16"),
    "member_variable_color": "syntax:property",
    "number_color": "syntax:number",
    "safe_line_number_color": "green@55",
    "search_result_border_color": "yellow@45",
    "search_result_color": ("yellow@15", "yellow@22"),
    "selection_color": "text@L4",
    "string_color": "syntax:string",
    "string_placeholder_color": "syntax:string.escape",
    "symbol_color": "syntax:operator",
    "text_color": "text",
    "text_selected_color": "transparent",  # keep syntax colors inside a selection
    "user_type_color": "syntax:type",
    "warning_color": ("yellow@12", "yellow@16"),
    "warning_underline_color": "ui:warning",
    "word_highlighted_color": "text@L2",
}


def color(f, source):
    if isinstance(source, tuple):
        source = source[0] if f.dark else source[1]
    if source.startswith("syntax:"):
        return f.syntax(source.removeprefix("syntax:"))[0]
    if source.startswith("ui:"):
        return ui(f)[source.removeprefix("ui:")]
    if source == "ink":
        return ink(f)
    return resolve(source, f)


def html(value):
    """#RRGGBB[AA] → rrggbbaa, the way Godot's Color.to_html() writes it."""
    value = value.lstrip("#").lower()
    return value if len(value) == 8 else value + "ff"


def tet(f):
    lines = [f"; {HEADER}", f"; {f.name} for Godot's script editor.", "[color_theme]", ""]
    lines += [f'{key}="{html(color(f, KEYS[key]))}"' for key in sorted(KEYS)]
    return "\n".join(lines) + "\n"


def contrast(f):
    """Godot darkens the base color by contrast × 1.15 for its deepest panels; aim that at crust."""
    step = 1 - max(p.hex_to_rgb(f.crust)) / max(p.hex_to_rgb(f.mantle))
    return round(step / 1.15, 2)


def interface(f):
    return f"""# {HEADER}
# {f.name}: Godot's interface theme. Enter these in Editor › Editor Settings › Interface › Theme.
# (Godot 4.6+ labels the first one "Color Preset"; 4.0 to 4.5 call it "Preset".)
Color Preset: Custom
Base Color: {f.mantle}
Accent Color: {f.orange}
Contrast: {contrast(f)}
Icon Saturation: 1

# And in Text Editor › Theme:
Color Theme: {f.name}
"""


def build(flavors):
    folders = "Linux: ~/.config/godot/text_editor_themes/ · Windows: %APPDATA%\\Godot\\text_editor_themes\\"
    outs = []
    for f in flavors:
        outs.append(
            Out(
                f"{f.name}.tet",
                tet(f),
                flavor=f.id,
                lang="ini",
                dest=f"~/Library/Application Support/Godot/text_editor_themes/{f.name}.tet",
                how=f"that's the macOS folder; {folders}",
            )
        )
        outs.append(
            Out(
                f"{f.slug}-interface.txt",
                interface(f),
                flavor=f.id,
                how="enter the values in Editor › Editor Settings › Interface › Theme",
            )
        )
    return outs
