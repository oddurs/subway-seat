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
    line_number_special_color = "#F1BF4B"
    line_number_special_background_color = "#1A2921"

    styles = {
        Token: "#D4DDD7",
        Token.Text: "#D4DDD7",
        Token.Error: "#C7665B",
        Token.Comment: "italic #708178",
        Token.Comment.Hashbang: "italic #708178",
        Token.Comment.Preproc: "italic #FAB49C",
        Token.Keyword: "#CA9245",
        Token.Keyword.Constant: "#E7877B",
        Token.Keyword.Type: "italic #549B9F",
        Token.Operator: "#8C9A92",
        Token.Operator.Word: "#CA9245",
        Token.Punctuation: "#8C9A92",
        Token.Name: "#D4DDD7",
        Token.Name.Attribute: "italic #F1BF4B",
        Token.Name.Builtin: "italic #F1BF4B",
        Token.Name.Builtin.Pseudo: "italic #E7877B",
        Token.Name.Class: "#549B9F",
        Token.Name.Constant: "#E7877B",
        Token.Name.Decorator: "italic #FAB49C",
        Token.Name.Entity: "#FAB49C",
        Token.Name.Exception: "#549B9F",
        Token.Name.Function: "#F1BF4B",
        Token.Name.Function.Magic: "italic #F1BF4B",
        Token.Name.Label: "italic #FAB49C",
        Token.Name.Namespace: "#A5B1AA",
        Token.Name.Property: "#BFC8C2",
        Token.Name.Tag: "#CA9245",
        Token.Name.Variable: "#D4DDD7",
        Token.Name.Variable.Magic: "italic #E7877B",
        Token.Literal.Date: "#E7877B",
        Token.Literal.String: "#70CAA9",
        Token.Literal.String.Affix: "#CA9245",
        Token.Literal.String.Escape: "#FAB49C",
        Token.Literal.String.Interpol: "#FAB49C",
        Token.Literal.String.Regex: "#FAB49C",
        Token.Literal.String.Symbol: "#E7877B",
        Token.Literal.Number: "#E7877B",
        Token.Generic.Heading: "bold #F1BF4B",
        Token.Generic.Subheading: "bold #F1BF4B",
        Token.Generic.Emph: "italic #D4DDD7",
        Token.Generic.Strong: "bold #E7ECEA",
        Token.Generic.Deleted: "bg:#3B2621 #E7877B",
        Token.Generic.Inserted: "bg:#20392F #70CAA9",
        Token.Generic.Error: "#C7665B",
        Token.Generic.Output: "#A5B1AA",
        Token.Generic.Prompt: "#CA9245",
        Token.Generic.Traceback: "#C7665B",
    }


style = ParisCatacombesStyle
