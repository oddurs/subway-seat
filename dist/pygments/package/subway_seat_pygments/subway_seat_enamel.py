# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Subway Seat Enamel — a Pygments style. Cream enamel panels in the morning sun. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["SubwaySeatEnamelStyle", "style"]


class SubwaySeatEnamelStyle(Style):
    name = "subway-seat-enamel"
    background_color = "#F4E9D4"
    highlight_color = "#EBDEC6"
    line_number_color = "#A58C6A"
    line_number_background_color = "#F4E9D4"
    line_number_special_color = "#AD4E00"
    line_number_special_background_color = "#EBDEC6"

    styles = {
        Token: "#3E2C1E",
        Token.Text: "#3E2C1E",
        Token.Error: "#992418",
        Token.Comment: "italic #8C7254",
        Token.Comment.Hashbang: "italic #8C7254",
        Token.Comment.Preproc: "italic #A65633",
        Token.Keyword: "#AD4E00",
        Token.Keyword.Constant: "#BC4031",
        Token.Keyword.Type: "italic #3E7157",
        Token.Operator: "#735C44",
        Token.Operator.Word: "#AD4E00",
        Token.Punctuation: "#735C44",
        Token.Name: "#3E2C1E",
        Token.Name.Attribute: "italic #936200",
        Token.Name.Builtin: "italic #936200",
        Token.Name.Builtin.Pseudo: "italic #BC4031",
        Token.Name.Class: "#3E7157",
        Token.Name.Constant: "#BC4031",
        Token.Name.Decorator: "italic #A65633",
        Token.Name.Entity: "#A65633",
        Token.Name.Exception: "#3E7157",
        Token.Name.Function: "#936200",
        Token.Name.Function.Magic: "italic #936200",
        Token.Name.Label: "italic #A65633",
        Token.Name.Namespace: "#654F3B",
        Token.Name.Property: "#54402F",
        Token.Name.Tag: "#AD4E00",
        Token.Name.Variable: "#3E2C1E",
        Token.Name.Variable.Magic: "italic #BC4031",
        Token.Literal.Date: "#BC4031",
        Token.Literal.String: "#66740F",
        Token.Literal.String.Affix: "#AD4E00",
        Token.Literal.String.Escape: "#A65633",
        Token.Literal.String.Interpol: "#A65633",
        Token.Literal.String.Regex: "#A65633",
        Token.Literal.String.Symbol: "#BC4031",
        Token.Literal.Number: "#BC4031",
        Token.Generic.Heading: "bold #936200",
        Token.Generic.Subheading: "bold #936200",
        Token.Generic.Emph: "italic #3E2C1E",
        Token.Generic.Strong: "bold #2A1D13",
        Token.Generic.Deleted: "bg:#EBD3D1 #BC4031",
        Token.Generic.Inserted: "bg:#D7DBC1 #66740F",
        Token.Generic.Error: "#992418",
        Token.Generic.Output: "#654F3B",
        Token.Generic.Prompt: "#AD4E00",
        Token.Generic.Traceback: "#992418",
    }


style = SubwaySeatEnamelStyle
