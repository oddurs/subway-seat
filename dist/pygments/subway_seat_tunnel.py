# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Subway Seat Tunnel — a Pygments style. The late local after midnight: espresso-deep, same warm lights."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["SubwaySeatTunnelStyle", "style"]


class SubwaySeatTunnelStyle(Style):
    name = "subway-seat-tunnel"
    background_color = "#24180E"
    highlight_color = "#302115"
    line_number_color = "#6A523C"
    line_number_background_color = "#24180E"
    line_number_special_color = "#F3BF45"
    line_number_special_background_color = "#302115"

    styles = {
        Token: "#E9D8B6",
        Token.Text: "#E9D8B6",
        Token.Error: "#D2503A",
        Token.Comment: "italic #8A7053",
        Token.Comment.Hashbang: "italic #8A7053",
        Token.Comment.Preproc: "italic #E0956C",
        Token.Keyword: "#EC7F31",
        Token.Keyword.Constant: "#EC6A50",
        Token.Keyword.Type: "italic #86AD95",
        Token.Operator: "#A48B6C",
        Token.Operator.Word: "#EC7F31",
        Token.Punctuation: "#A48B6C",
        Token.Name: "#E9D8B6",
        Token.Name.Attribute: "italic #F3BF45",
        Token.Name.Builtin: "italic #F3BF45",
        Token.Name.Builtin.Pseudo: "italic #EC6A50",
        Token.Name.Class: "#86AD95",
        Token.Name.Constant: "#EC6A50",
        Token.Name.Decorator: "italic #E0956C",
        Token.Name.Entity: "#E0956C",
        Token.Name.Exception: "#86AD95",
        Token.Name.Function: "#F3BF45",
        Token.Name.Function.Magic: "italic #F3BF45",
        Token.Name.Label: "italic #E0956C",
        Token.Name.Namespace: "#C0AA88",
        Token.Name.Property: "#D6C3A0",
        Token.Name.Tag: "#EC7F31",
        Token.Name.Variable: "#E9D8B6",
        Token.Name.Variable.Magic: "italic #EC6A50",
        Token.Literal.Date: "#EC6A50",
        Token.Literal.String: "#A3AE4B",
        Token.Literal.String.Affix: "#EC7F31",
        Token.Literal.String.Escape: "#E0956C",
        Token.Literal.String.Interpol: "#E0956C",
        Token.Literal.String.Regex: "#E0956C",
        Token.Literal.String.Symbol: "#EC6A50",
        Token.Literal.Number: "#EC6A50",
        Token.Generic.Heading: "bold #F3BF45",
        Token.Generic.Subheading: "bold #F3BF45",
        Token.Generic.Emph: "italic #E9D8B6",
        Token.Generic.Strong: "bold #F6EAD1",
        Token.Generic.Deleted: "#EC6A50",
        Token.Generic.Inserted: "#A3AE4B",
        Token.Generic.Error: "#D2503A",
        Token.Generic.Output: "#C0AA88",
        Token.Generic.Prompt: "#EC7F31",
        Token.Generic.Traceback: "#D2503A",
    }


style = SubwaySeatTunnelStyle
