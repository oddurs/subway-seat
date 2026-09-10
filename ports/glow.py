import json

from ports._cli import ink
from ports._lib import Out

META = {
    "id": "glow",
    "name": "Glow",
    "category": "CLI & TUI",
    "homepage": "https://github.com/charmbracelet/glow",
    "enable": {
        "where": "config.fish (GLAMOUR_STYLE also reaches gh and other Glamour apps)",
        "code": "set -Ux GLAMOUR_STYLE ~/.config/glamour/{slug}.json\nset -Ux GLOW_STYLE $GLAMOUR_STYLE",
        "lang": "fish",
    },
    "notes": "A Glamour style: top-level headings as orange station signs, the rest stepping down the "
    "stripe from orange to sage, and code blocks colored like the editor ports.",
}


def st(role, f):
    """A chroma token style from a shared syntax role (palette.SYNTAX)."""
    color, styles = f.syntax(role)
    return {"color": color, **{s: True for s in sorted(styles & {"bold", "italic"})}}


def style(f):
    chroma = {
        "text": {"color": f.text},
        "error": {"color": f.text_hi, "background_color": f.red},
        "comment": st("comment", f),
        "comment_preproc": st("decorator", f),
        "keyword": st("keyword", f),
        "keyword_reserved": st("keyword", f),
        "keyword_namespace": st("keyword", f),
        "keyword_type": st("type.builtin", f),
        "operator": st("operator", f),
        "punctuation": st("punctuation", f),
        "name": st("variable", f),
        "name_builtin": st("function.builtin", f),
        "name_tag": st("tag", f),
        "name_attribute": st("attribute", f),
        "name_class": st("type", f),
        "name_constant": st("constant", f),
        "name_decorator": st("decorator", f),
        "name_exception": st("type", f),
        "name_function": st("function", f),
        "name_other": st("variable", f),
        "literal": st("constant", f),
        "literal_number": st("number", f),
        "literal_date": st("constant", f),
        "literal_string": st("string", f),
        "literal_string_escape": st("string.escape", f),
        "generic_deleted": {"color": f.red_hi},
        "generic_emph": {"color": f.text, "italic": True},
        "generic_inserted": {"color": f.green},
        "generic_strong": {"color": f.text_hi, "bold": True},
        "generic_subheading": {"color": f.denim},
        "background": {"background_color": f.mantle},
    }
    return {
        "document": {"block_prefix": "\n", "block_suffix": "\n", "color": f.text, "margin": 2},
        "block_quote": {"indent": 1, "indent_token": "│ ", "color": f.subtext0, "italic": True},
        "paragraph": {},
        "list": {"level_indent": 2},
        "heading": {"block_suffix": "\n", "color": f.yellow, "bold": True},
        "h1": {"prefix": " ", "suffix": " ", "color": ink(f), "background_color": f.orange, "bold": True},
        "h2": {"prefix": "## ", "color": f.orange},
        "h3": {"prefix": "### ", "color": f.yellow},
        "h4": {"prefix": "#### ", "color": f.green},
        "h5": {"prefix": "##### ", "color": f.sage},
        "h6": {"prefix": "###### ", "color": f.subtext0, "bold": False},
        "text": {},
        "strikethrough": {"crossed_out": True},
        "emph": {"italic": True},
        "strong": {"color": f.text_hi, "bold": True},
        "hr": {"color": f.surface2, "format": "\n--------\n"},
        "item": {"block_prefix": "• "},
        "enumeration": {"block_prefix": ". "},
        "task": {"ticked": "[✓] ", "unticked": "[ ] "},
        "link": {"color": f.denim, "underline": True},
        "link_text": {"color": f.denim_hi, "bold": True},
        "image": {"color": f.denim, "underline": True},
        "image_text": {"color": f.sage, "format": "Image: {{.text}} →"},
        "code": {"prefix": " ", "suffix": " ", "color": f.green, "background_color": f.surface0},
        "code_block": {"color": f.overlay1, "margin": 2, "chroma": chroma},
        "table": {"color": f.overlay0, "center_separator": "┼", "column_separator": "│", "row_separator": "─"},
        "definition_list": {},
        "definition_term": {"color": f.yellow},
        "definition_description": {"block_prefix": "\n🠶 "},
        "html_block": {},
        "html_span": {},
    }


def build(flavors):
    # JSON has no comments, so this port carries no header line.
    return [
        Out(f"{f.slug}.json", json.dumps(style(f), indent=2, ensure_ascii=False) + "\n", flavor=f.id,
            dest=f"~/.config/glamour/{f.slug}.json", lang="json")
        for f in flavors
    ]
