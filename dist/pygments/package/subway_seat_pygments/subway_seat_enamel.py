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
    line_number_special_color = "#C4561A"
    line_number_special_background_color = "#EBDEC6"

    styles = {
        Token: "#3E2C1E",
        Token.Text: "#3E2C1E",
        Token.Error: "#B43B27",
        Token.Comment: "italic #8C7254",
        Token.Comment.Hashbang: "italic #8C7254",
        Token.Comment.Preproc: "italic #AE5F3A",
        Token.Keyword: "#C4561A",
        Token.Keyword.Constant: "#C44A33",
        Token.Keyword.Type: "italic #3E7157",
        Token.Operator: "#735C44",
        Token.Operator.Word: "#C4561A",
        Token.Punctuation: "#735C44",
        Token.Name: "#3E2C1E",
        Token.Name.Attribute: "italic #A56E00",
        Token.Name.Builtin: "italic #A56E00",
        Token.Name.Builtin.Pseudo: "italic #C44A33",
        Token.Name.Class: "#3E7157",
        Token.Name.Constant: "#C44A33",
        Token.Name.Decorator: "italic #AE5F3A",
        Token.Name.Entity: "#AE5F3A",
        Token.Name.Exception: "#3E7157",
        Token.Name.Function: "#A56E00",
        Token.Name.Function.Magic: "italic #A56E00",
        Token.Name.Label: "italic #AE5F3A",
        Token.Name.Namespace: "#654F3B",
        Token.Name.Property: "#54402F",
        Token.Name.Tag: "#C4561A",
        Token.Name.Variable: "#3E2C1E",
        Token.Name.Variable.Magic: "italic #C44A33",
        Token.Literal.Date: "#C44A33",
        Token.Literal.String: "#697813",
        Token.Literal.String.Affix: "#C4561A",
        Token.Literal.String.Escape: "#AE5F3A",
        Token.Literal.String.Interpol: "#AE5F3A",
        Token.Literal.String.Regex: "#AE5F3A",
        Token.Literal.String.Symbol: "#C44A33",
        Token.Literal.Number: "#C44A33",
        Token.Generic.Heading: "bold #A56E00",
        Token.Generic.Subheading: "bold #A56E00",
        Token.Generic.Emph: "italic #3E2C1E",
        Token.Generic.Strong: "bold #2A1D13",
        Token.Generic.Deleted: "#C44A33",
        Token.Generic.Inserted: "#697813",
        Token.Generic.Error: "#B43B27",
        Token.Generic.Output: "#654F3B",
        Token.Generic.Prompt: "#C4561A",
        Token.Generic.Traceback: "#B43B27",
    }


style = SubwaySeatEnamelStyle
