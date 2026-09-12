# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Carrelage — a Pygments style. Bevelled white tile under a vaulted platform. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCarrelageStyle", "style"]


class ParisCarrelageStyle(Style):
    name = "paris-carrelage"
    background_color = "#E2EDE8"
    highlight_color = "#D5E3DD"
    line_number_color = "#759A8A"
    line_number_background_color = "#E2EDE8"
    line_number_special_color = "#9B5D00"
    line_number_special_background_color = "#D5E3DD"

    styles = {
        Token: "#21352D",
        Token.Text: "#21352D",
        Token.Error: "#A30013",
        Token.Comment: "italic #5C8171",
        Token.Comment.Hashbang: "italic #5C8171",
        Token.Comment.Preproc: "italic #B43586",
        Token.Keyword: "#9B5D00",
        Token.Keyword.Constant: "#C82C2C",
        Token.Keyword.Type: "italic #007752",
        Token.Operator: "#4A695C",
        Token.Operator.Word: "#9B5D00",
        Token.Punctuation: "#4A695C",
        Token.Name: "#21352D",
        Token.Name.Attribute: "italic #856A00",
        Token.Name.Builtin: "italic #856A00",
        Token.Name.Builtin.Pseudo: "italic #C82C2C",
        Token.Name.Class: "#007752",
        Token.Name.Constant: "#C82C2C",
        Token.Name.Decorator: "italic #B43586",
        Token.Name.Entity: "#B43586",
        Token.Name.Exception: "#007752",
        Token.Name.Function: "#856A00",
        Token.Name.Function.Magic: "italic #856A00",
        Token.Name.Label: "italic #B43586",
        Token.Name.Namespace: "#405B4F",
        Token.Name.Property: "#334A41",
        Token.Name.Tag: "#9B5D00",
        Token.Name.Variable: "#21352D",
        Token.Name.Variable.Magic: "italic #C82C2C",
        Token.Literal.Date: "#C82C2C",
        Token.Literal.String: "#00823B",
        Token.Literal.String.Affix: "#9B5D00",
        Token.Literal.String.Escape: "#B43586",
        Token.Literal.String.Interpol: "#B43586",
        Token.Literal.String.Regex: "#B43586",
        Token.Literal.String.Symbol: "#C82C2C",
        Token.Literal.Number: "#C82C2C",
        Token.Generic.Heading: "bold #856A00",
        Token.Generic.Subheading: "bold #856A00",
        Token.Generic.Emph: "italic #21352D",
        Token.Generic.Strong: "bold #16241E",
        Token.Generic.Deleted: "bg:#EDCCD0 #C82C2C",
        Token.Generic.Inserted: "bg:#BDDECC #00823B",
        Token.Generic.Error: "#A30013",
        Token.Generic.Output: "#405B4F",
        Token.Generic.Prompt: "#9B5D00",
        Token.Generic.Traceback: "#A30013",
    }


style = ParisCarrelageStyle
