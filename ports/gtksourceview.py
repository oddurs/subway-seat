"""GtkSourceView: a style scheme per flavor (GNOME Text Editor, Builder, gedit, Meld)."""

from xml.sax.saxutils import escape, quoteattr

import palette as p
from ports._editors import ui
from ports._lib import HEADER, Out, tints

META = {
    "id": "gtksourceview",
    "name": "GtkSourceView",
    "category": "Editors",
    "homepage": "https://gitlab.gnome.org/GNOME/gtksourceview",
    "enable": {
        "where": "a shell (GNOME Text Editor), or Preferences → Font & Colors in gedit and Builder",
        "code": "gsettings set org.gnome.TextEditor style-scheme '{slug}'",
        "lang": "sh",
    },
    "notes": "One style scheme for everything built on GtkSourceView: GNOME Text Editor and Builder read "
    "`~/.local/share/gtksourceview-5/styles`, gedit reads `gtksourceview-4/styles` (or "
    "`libgedit-gtksourceview-300/styles` from gedit 45). Walnut and Enamel are paired, so GNOME Text Editor "
    "switches between them with the system style.",
}

LIGHT = "subway-seat-enamel"
DARK = "subway-seat"


def styles(f):
    """name → attributes. Colour values are palette role names (or tint_* names)."""
    u = ui(f)
    ink = "crust" if f.dark else "base"
    role = {v: k for k, v in reversed(list(f.colors.items()))}
    t_names = {v: f"tint_{k}" for k, v in tints(f).items()}
    name = lambda hexc: role.get(hexc) or t_names[hexc]

    def S(syntax_role, **extra):
        hexc, st = f.syntax(syntax_role)
        a = {"foreground": name(hexc)}
        a.update({s: "true" for s in st if s in ("bold", "italic")})
        a.update(extra)
        return a

    fg = lambda r, **kw: {"foreground": r, **kw}
    headings = ["orange", "orange", "yellow", "green", "sage", "clay", "subtext1"]
    s = {
        # editor chrome
        "text": {"foreground": "text", "background": "base"},
        "selection": {"foreground": "text_hi", "background": name(u["selection"])},
        "selection-unfocused": {"foreground": "text", "background": "selection_unfocused"},
        "cursor": fg(name(u["cursor"])),
        "secondary-cursor": fg("overlay2"),
        "current-line": {"background": name(u["line"])},
        "line-numbers": {"foreground": name(u["line_nr"]), "background": "base"},
        "line-numbers-border": {"background": "base"},
        "current-line-number": {"foreground": name(u["line_nr_cur"]), "background": name(u["line"]), "bold": "true"},
        "bracket-match": {"foreground": name(u["bracket_fg"]), "background": name(u["bracket_bg"]), "bold": "true"},
        "bracket-mismatch": {"foreground": ink, "background": "red_hi"},
        "right-margin": {"foreground": "surface1", "background": "mantle"},
        "draw-spaces": fg("surface2"),
        "background-pattern": {"background": "mantle"},
        "search-match": {"foreground": "text_hi", "background": "tint_search"},
        "map-overlay": {"background": "surface1"},
        "snippet-focus": {"background": "tint_chg"},
        # defaults every language maps onto
        "def:comment": S("comment"),
        "def:shebang": S("comment", bold="true"),
        "def:doc-comment": S("comment"),
        "def:doc-comment-element": fg("overlay2", italic="true", bold="true"),
        "def:constant": S("constant"),
        "def:character": S("string"),
        "def:string": S("string"),
        "def:special-char": S("string.escape"),
        "def:number": S("number"),
        "def:floating-point": S("number"),
        "def:decimal": S("number"),
        "def:base-n-integer": S("number"),
        "def:complex": S("number"),
        "def:special-constant": S("constant"),
        "def:boolean": S("boolean"),
        "def:identifier": S("variable"),
        "def:function": S("function"),
        "def:builtin": S("function.builtin"),
        "def:statement": S("keyword"),
        "def:keyword": S("keyword"),
        "def:operator": S("operator"),
        "def:type": S("type"),
        "def:preprocessor": fg("clay"),
        "def:error": {"foreground": "red_hi", "underline": "error", "underline-color": "red_hi"},
        "def:warning": {"underline": "error", "underline-color": "yellow"},
        "def:note": {"foreground": ink, "background": "yellow", "bold": "true"},
        "def:net-address": fg("denim", underline="single"),
        "def:underlined": {"underline": "single"},
        "def:emphasis": S("emphasis"),
        "def:strong-emphasis": S("strong"),
        "def:inline-code": S("code"),
        "def:insertion": fg("green", underline="single"),
        "def:deletion": fg("red_hi", strikethrough="true"),
        "def:link-text": fg("sage"),
        "def:link-symbol": fg("overlay2"),
        "def:link-destination": fg("denim", underline="single"),
        "def:heading": S("heading"),
        **{f"def:heading{i}": fg(h, bold="true") for i, h in enumerate(headings)},
        "def:thematic-break": fg("overlay1", bold="true"),
        "def:preformatted-section": S("code"),
        "def:list-marker": fg("orange"),
        # C, C#, Go, Vala
        "c:preprocessor": fg("clay"),
        "c:included-file": S("string"),
        "c:common-defines": S("constant"),
        "c:printf": S("string.escape"),
        "c:signal-name": S("string"),
        "c:storage-class": S("storage"),
        "c:type-keyword": S("storage"),
        "c-sharp:format": S("string.escape"),
        "c-sharp:preprocessor": fg("clay"),
        "go:printf": S("string.escape"),
        "vala:attributes": S("decorator"),
        # CSS
        "css:property-name": S("property"),
        "css:type-selector": S("tag"),
        "css:id-selector": S("attribute"),
        "css:pseudo-selector": S("decorator"),
        "css:selector-symbol": S("operator"),
        "css:vendor-specific": fg("overlay1"),
        # diff
        "diff:added-line": fg("green"),
        "diff:removed-line": fg("red_hi"),
        "diff:changed-line": fg("yellow"),
        "diff:location": fg("denim"),
        "diff:diff-file": fg("denim", bold="true"),
        "diff:special-case": fg("clay"),
        # JavaScript, JSON
        "js:built-in-constructor": S("type"),
        "json:keyname": S("function"),  # JSON keys read like TextMate property-name.json
        # LaTeX
        "latex:command": S("keyword"),
        "latex:include": S("keyword"),
        "latex:display-math": fg("clay"),
        "latex:inline-math": fg("clay"),
        "latex:math-bound": fg("overlay2"),
        # Perl, Python
        "perl:pod": S("comment"),
        "python:builtin-function": S("function.builtin"),
        "python:builtin-constant": S("constant"),
        "python:builtin-object": S("type.builtin"),
        "python:boolean": S("boolean"),
        "python:class-name": S("type"),
        "python:module-handler": S("keyword"),
        "python:special-variable": S("variable.builtin"),
        "python:string-conversion": S("string.escape"),
        # Rust
        "rust:attribute": S("decorator"),
        "rust:lifetime": S("decorator"),
        "rust:macro": fg("clay"),
        "rust:scope": S("namespace"),
        # shell
        "sh:variable": S("variable"),
        "sh:variable-definition": S("variable"),
        # XML, HTML
        "xml:element-name": S("tag"),
        "xml:attribute-name": S("attribute"),
        "xml:attribute-value": S("string"),
        "xml:namespace": S("namespace"),
        "xml:processing-instruction": fg("clay"),
        "xml:doctype": fg("clay"),
        "xml:entity": S("string.escape"),
        "xml:cdata-delim": S("punctuation"),
    }
    return s


def scheme(f):
    u = ui(f)
    colors = {r: f.colors[r] for r in p.ROLES}
    colors.update({f"tint_{k}": v for k, v in tints(f).items()})
    colors["selection_unfocused"] = f.mix(u["selection"], "base", 0.55)
    if f.dark:
        variants = [("variant", "dark"), ("light-variant", LIGHT)]
    else:
        variants = [("variant", "light"), ("dark-variant", DARK)]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f"<!-- {HEADER} -->",
        f'<style-scheme id="{f.slug}" name="{f.name}" version="1.0">',
        "  <author>Oddur Sigurdsson</author>",
        f"  <description>{escape(f.blurb)}</description>",
        "  <metadata>",
        *(f'    <property name="{k}">{v}</property>' for k, v in variants),
        "  </metadata>",
        "",
        *(f'  <color name="{k}" value="{v}"/>' for k, v in colors.items()),
        "",
    ]
    for name, attrs in styles(f).items():
        for v in attrs.values():  # every colour must be a declared name
            assert v in colors or v in {"true", "false", "single", "error", "low", "double", "none"}, (name, v)
        a = " ".join(f"{k}={quoteattr(v)}" for k, v in attrs.items())
        lines.append(f'  <style name="{name}" {a}/>')
    lines.append("</style-scheme>")
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}.xml", scheme(f), flavor=f.id,
            dest=f"~/.local/share/gtksourceview-5/styles/{f.slug}.xml", lang="xml")
        for f in flavors
    ]
