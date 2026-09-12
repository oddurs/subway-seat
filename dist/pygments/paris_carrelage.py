# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Carrelage — a Pygments style. Bevelled white tile under a vaulted platform. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCarrelageStyle", "style"]


class ParisCarrelageStyle(Style):
    name = "paris-carrelage"
    background_color = "#EEF3ED"
    highlight_color = "#E1E7E0"
    line_number_color = "#879887"
    line_number_background_color = "#EEF3ED"
    line_number_special_color = "#804B00"
    line_number_special_background_color = "#E1E7E0"

    styles = {
        Token: "#2A342B",
        Token.Text: "#2A342B",
        Token.Error: "#932D29",
        Token.Comment: "italic #6E7C6E",
        Token.Comment.Hashbang: "italic #6E7C6E",
        Token.Comment.Preproc: "italic #98547C",
        Token.Keyword: "#804B00",
        Token.Keyword.Constant: "#BE423D",
        Token.Keyword.Type: "italic #006E6B",
        Token.Operator: "#586459",
        Token.Operator.Word: "#804B00",
        Token.Punctuation: "#586459",
        Token.Name: "#2A342B",
        Token.Name.Attribute: "italic #8E6B08",
        Token.Name.Builtin: "italic #8E6B08",
        Token.Name.Builtin.Pseudo: "italic #BE423D",
        Token.Name.Class: "#006E6B",
        Token.Name.Constant: "#BE423D",
        Token.Name.Decorator: "italic #98547C",
        Token.Name.Entity: "#98547C",
        Token.Name.Exception: "#006E6B",
        Token.Name.Function: "#8E6B08",
        Token.Name.Function.Magic: "italic #8E6B08",
        Token.Name.Label: "italic #98547C",
        Token.Name.Namespace: "#4C574D",
        Token.Name.Property: "#3D473E",
        Token.Name.Tag: "#804B00",
        Token.Name.Variable: "#2A342B",
        Token.Name.Variable.Magic: "italic #BE423D",
        Token.Literal.Date: "#BE423D",
        Token.Literal.String: "#207F41",
        Token.Literal.String.Affix: "#804B00",
        Token.Literal.String.Escape: "#98547C",
        Token.Literal.String.Interpol: "#98547C",
        Token.Literal.String.Regex: "#98547C",
        Token.Literal.String.Symbol: "#BE423D",
        Token.Literal.Number: "#BE423D",
        Token.Generic.Heading: "bold #8E6B08",
        Token.Generic.Subheading: "bold #8E6B08",
        Token.Generic.Emph: "italic #2A342B",
        Token.Generic.Strong: "bold #1B221C",
        Token.Generic.Deleted: "bg:#E9D5D4 #BE423D",
        Token.Generic.Inserted: "bg:#C5DECE #207F41",
        Token.Generic.Error: "#932D29",
        Token.Generic.Output: "#4C574D",
        Token.Generic.Prompt: "#804B00",
        Token.Generic.Traceback: "#932D29",
    }


style = ParisCarrelageStyle
