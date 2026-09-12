# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Catacombes — a Pygments style. Under the quarries: the same green with the lights turned down."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCatacombesStyle", "style"]


class ParisCatacombesStyle(Style):
    name = "paris-catacombes"
    background_color = "#141D19"
    highlight_color = "#1D2822"
    line_number_color = "#57645D"
    line_number_background_color = "#141D19"
    line_number_special_color = "#EBC168"
    line_number_special_background_color = "#1D2822"

    styles = {
        Token: "#D5DCD8",
        Token.Text: "#D5DCD8",
        Token.Error: "#CD6B63",
        Token.Comment: "italic #738079",
        Token.Comment.Hashbang: "italic #738079",
        Token.Comment.Preproc: "italic #CE96B4",
        Token.Keyword: "#D0914F",
        Token.Keyword.Constant: "#E1837A",
        Token.Keyword.Type: "italic #7BB096",
        Token.Operator: "#8E9993",
        Token.Operator.Word: "#D0914F",
        Token.Punctuation: "#8E9993",
        Token.Name: "#D5DCD8",
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
        Token.Name.Namespace: "#A7B0AB",
        Token.Name.Property: "#C0C7C3",
        Token.Name.Tag: "#D0914F",
        Token.Name.Variable: "#D5DCD8",
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
        Token.Generic.Emph: "italic #D5DCD8",
        Token.Generic.Strong: "bold #E8ECEA",
        Token.Generic.Deleted: "bg:#3D2823 #E1837A",
        Token.Generic.Inserted: "bg:#253729 #80C28E",
        Token.Generic.Error: "#CD6B63",
        Token.Generic.Output: "#A7B0AB",
        Token.Generic.Prompt: "#D0914F",
        Token.Generic.Traceback: "#CD6B63",
    }


style = ParisCatacombesStyle
