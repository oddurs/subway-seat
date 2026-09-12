# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Guimard — a Pygments style. Cast iron off a Metro entrance, which is nearly black. Brass leads."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisGuimardStyle", "style"]


class ParisGuimardStyle(Style):
    name = "paris-guimard"
    background_color = "#212D27"
    highlight_color = "#2A3831"
    line_number_color = "#5B6A62"
    line_number_background_color = "#212D27"
    line_number_special_color = "#EBC168"
    line_number_special_background_color = "#2A3831"

    styles = {
        Token: "#DAE0DC",
        Token.Text: "#DAE0DC",
        Token.Error: "#CD6B63",
        Token.Comment: "italic #77847D",
        Token.Comment.Hashbang: "italic #77847D",
        Token.Comment.Preproc: "italic #CE96B4",
        Token.Keyword: "#D0914F",
        Token.Keyword.Constant: "#E1837A",
        Token.Keyword.Type: "italic #7BB096",
        Token.Operator: "#929D97",
        Token.Operator.Word: "#D0914F",
        Token.Punctuation: "#929D97",
        Token.Name: "#DAE0DC",
        Token.Name.Attribute: "italic #EBC168",
        Token.Name.Builtin: "italic #EBC168",
        Token.Name.Builtin.Pseudo: "italic #E1837A",
        Token.Name.Class: "#7BB096",
        Token.Name.Constant: "#E1837A",
        Token.Name.Decorator: "italic #CE96B4",
        Token.Name.Entity: "#CE96B4",
        Token.Name.Exception: "#7BB096",
        Token.Name.Function: "#EBC168",
        Token.Name.Function.Magic: "italic #EBC168",
        Token.Name.Label: "italic #CE96B4",
        Token.Name.Namespace: "#ABB4AF",
        Token.Name.Property: "#C3CAC6",
        Token.Name.Tag: "#D0914F",
        Token.Name.Variable: "#DAE0DC",
        Token.Name.Variable.Magic: "italic #E1837A",
        Token.Literal.Date: "#E1837A",
        Token.Literal.String: "#80C28E",
        Token.Literal.String.Affix: "#D0914F",
        Token.Literal.String.Escape: "#CE96B4",
        Token.Literal.String.Interpol: "#CE96B4",
        Token.Literal.String.Regex: "#CE96B4",
        Token.Literal.String.Symbol: "#E1837A",
        Token.Literal.Number: "#E1837A",
        Token.Generic.Heading: "bold #EBC168",
        Token.Generic.Subheading: "bold #EBC168",
        Token.Generic.Emph: "italic #DAE0DC",
        Token.Generic.Strong: "bold #EAEEEC",
        Token.Generic.Deleted: "bg:#442F2B #E1837A",
        Token.Generic.Inserted: "bg:#2C3F31 #80C28E",
        Token.Generic.Error: "#CD6B63",
        Token.Generic.Output: "#ABB4AF",
        Token.Generic.Prompt: "#D0914F",
        Token.Generic.Traceback: "#CD6B63",
    }


style = ParisGuimardStyle
