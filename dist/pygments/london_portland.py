# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""London Portland — a Pygments style. Holden's Portland stone. Links are the exact Corporate Blue."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["LondonPortlandStyle", "style"]


class LondonPortlandStyle(Style):
    name = "london-portland"
    background_color = "#E5EAF4"
    highlight_color = "#DAE0EB"
    line_number_color = "#8291AE"
    line_number_background_color = "#E5EAF4"
    line_number_special_color = "#A45600"
    line_number_special_background_color = "#DAE0EB"

    styles = {
        Token: "#293040",
        Token.Text: "#293040",
        Token.Error: "#A40005",
        Token.Comment: "italic #697794",
        Token.Comment.Hashbang: "italic #697794",
        Token.Comment.Preproc: "italic #7660AB",
        Token.Keyword: "#A45600",
        Token.Keyword.Constant: "#C92B23",
        Token.Keyword.Type: "italic #007376",
        Token.Operator: "#556179",
        Token.Operator.Word: "#A45600",
        Token.Punctuation: "#556179",
        Token.Name: "#293040",
        Token.Name.Attribute: "italic #896800",
        Token.Name.Builtin: "italic #896800",
        Token.Name.Builtin.Pseudo: "italic #C92B23",
        Token.Name.Class: "#007376",
        Token.Name.Constant: "#C92B23",
        Token.Name.Decorator: "italic #7660AB",
        Token.Name.Entity: "#7660AB",
        Token.Name.Exception: "#007376",
        Token.Name.Function: "#896800",
        Token.Name.Function.Magic: "italic #896800",
        Token.Name.Label: "italic #7660AB",
        Token.Name.Namespace: "#4A5469",
        Token.Name.Property: "#3C4557",
        Token.Name.Tag: "#A45600",
        Token.Name.Variable: "#293040",
        Token.Name.Variable.Magic: "italic #C92B23",
        Token.Literal.Date: "#C92B23",
        Token.Literal.String: "#00822E",
        Token.Literal.String.Affix: "#A45600",
        Token.Literal.String.Escape: "#7660AB",
        Token.Literal.String.Interpol: "#7660AB",
        Token.Literal.String.Regex: "#7660AB",
        Token.Literal.String.Symbol: "#C92B23",
        Token.Literal.Number: "#C92B23",
        Token.Generic.Heading: "bold #896800",
        Token.Generic.Subheading: "bold #896800",
        Token.Generic.Emph: "italic #293040",
        Token.Generic.Strong: "bold #1B202B",
        Token.Generic.Deleted: "bg:#EDCCCD #C92B23",
        Token.Generic.Inserted: "bg:#BDDEC9 #00822E",
        Token.Generic.Error: "#A40005",
        Token.Generic.Output: "#4A5469",
        Token.Generic.Prompt: "#A45600",
        Token.Generic.Traceback: "#A40005",
    }


style = LondonPortlandStyle
