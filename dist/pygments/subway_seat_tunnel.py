# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Subway Seat Tunnel — a Pygments style. The late local after midnight: espresso-deep, same warm lights."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["SubwaySeatTunnelStyle", "style"]


class SubwaySeatTunnelStyle(Style):
    name = "subway-seat-tunnel"
    background_color = "#24180E"
    highlight_color = "#302115"
    line_number_color = "#745B45"
    line_number_background_color = "#24180E"
    line_number_special_color = "#F3BF45"
    line_number_special_background_color = "#302115"

    styles = {
        Token: "#E9D8B6",
        Token.Text: "#E9D8B6",
        Token.Error: "#E05C45",
        Token.Comment: "italic #917759",
        Token.Comment.Hashbang: "italic #917759",
        Token.Comment.Preproc: "italic #E0956C",
        Token.Keyword: "#EC7F31",
        Token.Keyword.Constant: "#F97160",
        Token.Keyword.Type: "italic #86AD95",
        Token.Operator: "#AA9171",
        Token.Operator.Word: "#EC7F31",
        Token.Punctuation: "#AA9171",
        Token.Name: "#E9D8B6",
        Token.Name.Attribute: "italic #F3BF45",
        Token.Name.Builtin: "italic #F3BF45",
        Token.Name.Builtin.Pseudo: "italic #F97160",
        Token.Name.Class: "#86AD95",
        Token.Name.Constant: "#F97160",
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
        Token.Name.Variable.Magic: "italic #F97160",
        Token.Literal.Date: "#F97160",
        Token.Literal.String: "#ADB956",
        Token.Literal.String.Affix: "#EC7F31",
        Token.Literal.String.Escape: "#E0956C",
        Token.Literal.String.Interpol: "#E0956C",
        Token.Literal.String.Regex: "#E0956C",
        Token.Literal.String.Symbol: "#F97160",
        Token.Literal.Number: "#F97160",
        Token.Generic.Heading: "bold #F3BF45",
        Token.Generic.Subheading: "bold #F3BF45",
        Token.Generic.Emph: "italic #E9D8B6",
        Token.Generic.Strong: "bold #F6EAD1",
        Token.Generic.Deleted: "bg:#492217 #F97160",
        Token.Generic.Inserted: "bg:#363318 #ADB956",
        Token.Generic.Error: "#E05C45",
        Token.Generic.Output: "#C0AA88",
        Token.Generic.Prompt: "#EC7F31",
        Token.Generic.Traceback: "#E05C45",
    }


style = SubwaySeatTunnelStyle
