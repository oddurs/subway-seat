# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""London Portland — a Pygments style. Holden's Portland stone. Links are the exact Corporate Blue."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["LondonPortlandStyle", "style"]


class LondonPortlandStyle(Style):
    name = "london-portland"
    background_color = "#E5EAF6"
    highlight_color = "#D9E0EC"
    line_number_color = "#8A919F"
    line_number_background_color = "#E5EAF6"
    line_number_special_color = "#9F591B"
    line_number_special_background_color = "#D9E0EC"

    styles = {
        Token: "#2F3033",
        Token.Text: "#2F3033",
        Token.Error: "#A40005",
        Token.Comment: "italic #727781",
        Token.Comment.Hashbang: "italic #727781",
        Token.Comment.Preproc: "italic #7660AB",
        Token.Keyword: "#9F591B",
        Token.Keyword.Constant: "#CA2822",
        Token.Keyword.Type: "italic #007376",
        Token.Operator: "#5D6168",
        Token.Operator.Word: "#9F591B",
        Token.Punctuation: "#5D6168",
        Token.Name: "#2F3033",
        Token.Name.Attribute: "italic #896800",
        Token.Name.Builtin: "italic #896800",
        Token.Name.Builtin.Pseudo: "italic #CA2822",
        Token.Name.Class: "#007376",
        Token.Name.Constant: "#CA2822",
        Token.Name.Decorator: "italic #7660AB",
        Token.Name.Entity: "#7660AB",
        Token.Name.Exception: "#007376",
        Token.Name.Function: "#896800",
        Token.Name.Function.Magic: "italic #896800",
        Token.Name.Label: "italic #7660AB",
        Token.Name.Namespace: "#515459",
        Token.Name.Property: "#434548",
        Token.Name.Tag: "#9F591B",
        Token.Name.Variable: "#2F3033",
        Token.Name.Variable.Magic: "italic #CA2822",
        Token.Literal.Date: "#CA2822",
        Token.Literal.String: "#357D41",
        Token.Literal.String.Affix: "#9F591B",
        Token.Literal.String.Escape: "#7660AB",
        Token.Literal.String.Interpol: "#7660AB",
        Token.Literal.String.Regex: "#7660AB",
        Token.Literal.String.Symbol: "#CA2822",
        Token.Literal.Number: "#CA2822",
        Token.Generic.Heading: "bold #896800",
        Token.Generic.Subheading: "bold #896800",
        Token.Generic.Emph: "italic #2F3033",
        Token.Generic.Strong: "bold #1F2022",
        Token.Generic.Deleted: "bg:#EDCCCD #CA2822",
        Token.Generic.Inserted: "bg:#CADDCE #357D41",
        Token.Generic.Error: "#A40005",
        Token.Generic.Output: "#515459",
        Token.Generic.Prompt: "#9F591B",
        Token.Generic.Traceback: "#A40005",
    }


style = LondonPortlandStyle
