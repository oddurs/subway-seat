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
    line_number_special_color = "#8A5308"
    line_number_special_background_color = "#E1E7E0"

    styles = {
        Token: "#2A342B",
        Token.Text: "#2A342B",
        Token.Error: "#932D29",
        Token.Comment: "italic #6E7C6E",
        Token.Comment.Hashbang: "italic #6E7C6E",
        Token.Comment.Preproc: "italic #9A557D",
        Token.Keyword: "#8A5308",
        Token.Keyword.Constant: "#BB403B",
        Token.Keyword.Type: "italic #0B714D",
        Token.Operator: "#586459",
        Token.Operator.Word: "#8A5308",
        Token.Punctuation: "#586459",
        Token.Name: "#2A342B",
        Token.Name.Attribute: "italic #8A6700",
        Token.Name.Builtin: "italic #8A6700",
        Token.Name.Builtin.Pseudo: "italic #BB403B",
        Token.Name.Class: "#0B714D",
        Token.Name.Constant: "#BB403B",
        Token.Name.Decorator: "italic #9A557D",
        Token.Name.Entity: "#9A557D",
        Token.Name.Exception: "#0B714D",
        Token.Name.Function: "#8A6700",
        Token.Name.Function.Magic: "italic #8A6700",
        Token.Name.Label: "italic #9A557D",
        Token.Name.Namespace: "#4C574D",
        Token.Name.Property: "#3D473E",
        Token.Name.Tag: "#8A5308",
        Token.Name.Variable: "#2A342B",
        Token.Name.Variable.Magic: "italic #BB403B",
        Token.Literal.Date: "#BB403B",
        Token.Literal.String: "#207F41",
        Token.Literal.String.Affix: "#8A5308",
        Token.Literal.String.Escape: "#9A557D",
        Token.Literal.String.Interpol: "#9A557D",
        Token.Literal.String.Regex: "#9A557D",
        Token.Literal.String.Symbol: "#BB403B",
        Token.Literal.Number: "#BB403B",
        Token.Generic.Heading: "bold #8A6700",
        Token.Generic.Subheading: "bold #8A6700",
        Token.Generic.Emph: "italic #2A342B",
        Token.Generic.Strong: "bold #1B221C",
        Token.Generic.Deleted: "bg:#E9D5D4 #BB403B",
        Token.Generic.Inserted: "bg:#C5DECE #207F41",
        Token.Generic.Error: "#932D29",
        Token.Generic.Output: "#4C574D",
        Token.Generic.Prompt: "#8A5308",
        Token.Generic.Traceback: "#932D29",
    }


style = ParisCarrelageStyle
