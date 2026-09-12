# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Carrelage — a Pygments style. Bevelled white tile under a vaulted platform. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCarrelageStyle", "style"]


class ParisCarrelageStyle(Style):
    name = "paris-carrelage"
    background_color = "#EEF2F1"
    highlight_color = "#E1E6E5"
    line_number_color = "#859792"
    line_number_background_color = "#EEF2F1"
    line_number_special_color = "#764C00"
    line_number_special_background_color = "#E1E6E5"

    styles = {
        Token: "#27342F",
        Token.Text: "#27342F",
        Token.Error: "#88251E",
        Token.Comment: "italic #6C7C76",
        Token.Comment.Hashbang: "italic #6C7C76",
        Token.Comment.Preproc: "italic #B36B51",
        Token.Keyword: "#764C00",
        Token.Keyword.Constant: "#AC3B32",
        Token.Keyword.Type: "italic #006267",
        Token.Operator: "#56645F",
        Token.Operator.Word: "#764C00",
        Token.Punctuation: "#56645F",
        Token.Name: "#27342F",
        Token.Name.Attribute: "italic #916D07",
        Token.Name.Builtin: "italic #916D07",
        Token.Name.Builtin.Pseudo: "italic #AC3B32",
        Token.Name.Class: "#006267",
        Token.Name.Constant: "#AC3B32",
        Token.Name.Decorator: "italic #B36B51",
        Token.Name.Entity: "#B36B51",
        Token.Name.Exception: "#006267",
        Token.Name.Function: "#916D07",
        Token.Name.Function.Magic: "italic #916D07",
        Token.Name.Label: "italic #B36B51",
        Token.Name.Namespace: "#4A5752",
        Token.Name.Property: "#3B4742",
        Token.Name.Tag: "#764C00",
        Token.Name.Variable: "#27342F",
        Token.Name.Variable.Magic: "italic #AC3B32",
        Token.Literal.Date: "#AC3B32",
        Token.Literal.String: "#218366",
        Token.Literal.String.Affix: "#764C00",
        Token.Literal.String.Escape: "#B36B51",
        Token.Literal.String.Interpol: "#B36B51",
        Token.Literal.String.Regex: "#B36B51",
        Token.Literal.String.Symbol: "#AC3B32",
        Token.Literal.Number: "#AC3B32",
        Token.Generic.Heading: "bold #916D07",
        Token.Generic.Subheading: "bold #916D07",
        Token.Generic.Emph: "italic #27342F",
        Token.Generic.Strong: "bold #19221E",
        Token.Generic.Deleted: "bg:#E7D3D2 #AC3B32",
        Token.Generic.Inserted: "bg:#C5DFD7 #218366",
        Token.Generic.Error: "#88251E",
        Token.Generic.Output: "#4A5752",
        Token.Generic.Prompt: "#764C00",
        Token.Generic.Traceback: "#88251E",
    }


style = ParisCarrelageStyle
