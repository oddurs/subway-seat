# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Catacombes — a Pygments style. Under the quarries: the same green with the lights turned down."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCatacombesStyle", "style"]


class ParisCatacombesStyle(Style):
    name = "paris-catacombes"
    background_color = "#121E19"
    highlight_color = "#1A2921"
    line_number_color = "#54655C"
    line_number_background_color = "#121E19"
    line_number_special_color = "#F2BF4B"
    line_number_special_background_color = "#1A2921"

    styles = {
        Token: "#D4DDD7",
        Token.Text: "#D4DDD7",
        Token.Error: "#CD6B63",
        Token.Comment: "italic #708178",
        Token.Comment.Hashbang: "italic #708178",
        Token.Comment.Preproc: "italic #CE96B4",
        Token.Keyword: "#D0914F",
        Token.Keyword.Constant: "#EE8F85",
        Token.Keyword.Type: "italic #5FA09D",
        Token.Operator: "#8C9A92",
        Token.Operator.Word: "#D0914F",
        Token.Punctuation: "#8C9A92",
        Token.Name: "#D4DDD7",
        Token.Name.Attribute: "italic #F2BF4B",
        Token.Name.Builtin: "italic #F2BF4B",
        Token.Name.Builtin.Pseudo: "italic #EE8F85",
        Token.Name.Class: "#5FA09D",
        Token.Name.Constant: "#EE8F85",
        Token.Name.Decorator: "italic #CE96B4",
        Token.Name.Entity: "#CE96B4",
        Token.Name.Exception: "#5FA09D",
        Token.Name.Function: "#F2BF4B",
        Token.Name.Function.Magic: "italic #F2BF4B",
        Token.Name.Label: "italic #CE96B4",
        Token.Name.Namespace: "#A5B1AA",
        Token.Name.Property: "#BFC8C2",
        Token.Name.Tag: "#D0914F",
        Token.Name.Variable: "#D4DDD7",
        Token.Name.Variable.Magic: "italic #EE8F85",
        Token.Literal.Date: "#EE8F85",
        Token.Literal.String: "#80C28E",
        Token.Literal.String.Affix: "#D0914F",
        Token.Literal.String.Escape: "#CE96B4",
        Token.Literal.String.Interpol: "#CE96B4",
        Token.Literal.String.Regex: "#CE96B4",
        Token.Literal.String.Symbol: "#EE8F85",
        Token.Literal.Number: "#EE8F85",
        Token.Generic.Heading: "bold #F2BF4B",
        Token.Generic.Subheading: "bold #F2BF4B",
        Token.Generic.Emph: "italic #D4DDD7",
        Token.Generic.Strong: "bold #E7ECEA",
        Token.Generic.Deleted: "bg:#3D2823 #EE8F85",
        Token.Generic.Inserted: "bg:#243729 #80C28E",
        Token.Generic.Error: "#CD6B63",
        Token.Generic.Output: "#A5B1AA",
        Token.Generic.Prompt: "#D0914F",
        Token.Generic.Traceback: "#CD6B63",
    }


style = ParisCatacombesStyle
