# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Subway Seat — a Pygments style. Walnut paneling and orange bucket seats. The original."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["SubwaySeatStyle", "style"]


class SubwaySeatStyle(Style):
    name = "subway-seat"
    background_color = "#362619"
    highlight_color = "#43301F"
    line_number_color = "#7B6047"
    line_number_background_color = "#362619"
    line_number_special_color = "#F3BF45"
    line_number_special_background_color = "#43301F"

    styles = {
        Token: "#EDDCBC",
        Token.Text: "#EDDCBC",
        Token.Error: "#E05C45",
        Token.Comment: "italic #967B5C",
        Token.Comment.Hashbang: "italic #967B5C",
        Token.Comment.Preproc: "italic #F4A87E",
        Token.Keyword: "#EC7F31",
        Token.Keyword.Constant: "#FF8373",
        Token.Keyword.Type: "italic #86AD95",
        Token.Operator: "#AE9575",
        Token.Operator.Word: "#EC7F31",
        Token.Punctuation: "#AE9575",
        Token.Name: "#EDDCBC",
        Token.Name.Attribute: "italic #F3BF45",
        Token.Name.Builtin: "italic #F3BF45",
        Token.Name.Builtin.Pseudo: "italic #FF8373",
        Token.Name.Class: "#86AD95",
        Token.Name.Constant: "#FF8373",
        Token.Name.Decorator: "italic #F4A87E",
        Token.Name.Entity: "#F4A87E",
        Token.Name.Exception: "#86AD95",
        Token.Name.Function: "#F3BF45",
        Token.Name.Function.Magic: "italic #F3BF45",
        Token.Name.Label: "italic #F4A87E",
        Token.Name.Namespace: "#C4AE8C",
        Token.Name.Property: "#D9C6A3",
        Token.Name.Tag: "#EC7F31",
        Token.Name.Variable: "#EDDCBC",
        Token.Name.Variable.Magic: "italic #FF8373",
        Token.Literal.Date: "#FF8373",
        Token.Literal.String: "#ADB956",
        Token.Literal.String.Affix: "#EC7F31",
        Token.Literal.String.Escape: "#F4A87E",
        Token.Literal.String.Interpol: "#F4A87E",
        Token.Literal.String.Regex: "#F4A87E",
        Token.Literal.String.Symbol: "#FF8373",
        Token.Literal.Number: "#FF8373",
        Token.Generic.Heading: "bold #F3BF45",
        Token.Generic.Subheading: "bold #F3BF45",
        Token.Generic.Emph: "italic #EDDCBC",
        Token.Generic.Strong: "bold #F8ECD4",
        Token.Generic.Deleted: "bg:#52281C #FF8373",
        Token.Generic.Inserted: "bg:#3F3A1E #ADB956",
        Token.Generic.Error: "#E05C45",
        Token.Generic.Output: "#C4AE8C",
        Token.Generic.Prompt: "#EC7F31",
        Token.Generic.Traceback: "#E05C45",
    }


style = SubwaySeatStyle
