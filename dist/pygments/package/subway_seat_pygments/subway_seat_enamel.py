# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Subway Seat Enamel — a Pygments style. Cream enamel panels in the morning sun. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["SubwaySeatEnamelStyle", "style"]


class SubwaySeatEnamelStyle(Style):
    name = "subway-seat-enamel"
    background_color = "#F8EFDF"
    highlight_color = "#EEE4D0"
    line_number_color = "#A58D6D"
    line_number_background_color = "#F8EFDF"
    line_number_special_color = "#A04800"
    line_number_special_background_color = "#EEE4D0"

    styles = {
        Token: "#3E2C1E",
        Token.Text: "#3E2C1E",
        Token.Error: "#992418",
        Token.Comment: "italic #8C7254",
        Token.Comment.Hashbang: "italic #8C7254",
        Token.Comment.Preproc: "italic #843811",
        Token.Keyword: "#A04800",
        Token.Keyword.Constant: "#BF4233",
        Token.Keyword.Type: "italic #3E7157",
        Token.Operator: "#735C44",
        Token.Operator.Word: "#A04800",
        Token.Punctuation: "#735C44",
        Token.Name: "#3E2C1E",
        Token.Name.Attribute: "italic #976608",
        Token.Name.Builtin: "italic #976608",
        Token.Name.Builtin.Pseudo: "italic #BF4233",
        Token.Name.Class: "#3E7157",
        Token.Name.Constant: "#BF4233",
        Token.Name.Decorator: "italic #843811",
        Token.Name.Entity: "#843811",
        Token.Name.Exception: "#3E7157",
        Token.Name.Function: "#976608",
        Token.Name.Function.Magic: "italic #976608",
        Token.Name.Label: "italic #843811",
        Token.Name.Namespace: "#654F3B",
        Token.Name.Property: "#54402F",
        Token.Name.Tag: "#A04800",
        Token.Name.Variable: "#3E2C1E",
        Token.Name.Variable.Magic: "italic #BF4233",
        Token.Literal.Date: "#BF4233",
        Token.Literal.String: "#66740F",
        Token.Literal.String.Affix: "#A04800",
        Token.Literal.String.Escape: "#843811",
        Token.Literal.String.Interpol: "#843811",
        Token.Literal.String.Regex: "#843811",
        Token.Literal.String.Symbol: "#BF4233",
        Token.Literal.Number: "#BF4233",
        Token.Generic.Heading: "bold #976608",
        Token.Generic.Subheading: "bold #976608",
        Token.Generic.Emph: "italic #3E2C1E",
        Token.Generic.Strong: "bold #2A1D13",
        Token.Generic.Deleted: "bg:#EBD3D1 #BF4233",
        Token.Generic.Inserted: "bg:#D7DBC1 #66740F",
        Token.Generic.Error: "#992418",
        Token.Generic.Output: "#654F3B",
        Token.Generic.Prompt: "#A04800",
        Token.Generic.Traceback: "#992418",
    }


style = SubwaySeatEnamelStyle
