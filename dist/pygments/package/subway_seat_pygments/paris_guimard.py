# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Guimard — a Pygments style. Cast iron off a Metro entrance, which is nearly black. Brass leads."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisGuimardStyle", "style"]


class ParisGuimardStyle(Style):
    name = "paris-guimard"
    background_color = "#1E2E26"
    highlight_color = "#263930"
    line_number_color = "#586B61"
    line_number_background_color = "#1E2E26"
    line_number_special_color = "#EBC168"
    line_number_special_background_color = "#263930"

    styles = {
        Token: "#D9E1DB",
        Token.Text: "#D9E1DB",
        Token.Error: "#CD6B63",
        Token.Comment: "italic #74857C",
        Token.Comment.Hashbang: "italic #74857C",
        Token.Comment.Preproc: "italic #CE96B4",
        Token.Keyword: "#D0914F",
        Token.Keyword.Constant: "#E1837A",
        Token.Keyword.Type: "italic #6CA087",
        Token.Operator: "#909E96",
        Token.Operator.Word: "#D0914F",
        Token.Punctuation: "#909E96",
        Token.Name: "#D9E1DB",
        Token.Name.Attribute: "italic #EBC168",
        Token.Name.Builtin: "italic #EBC168",
        Token.Name.Builtin.Pseudo: "italic #E1837A",
        Token.Name.Class: "#6CA087",
        Token.Name.Constant: "#E1837A",
        Token.Name.Decorator: "italic #CE96B4",
        Token.Name.Entity: "#CE96B4",
        Token.Name.Exception: "#6CA087",
        Token.Name.Function: "#EBC168",
        Token.Name.Function.Magic: "italic #EBC168",
        Token.Name.Label: "italic #CE96B4",
        Token.Name.Namespace: "#A9B5AE",
        Token.Name.Property: "#C2CBC5",
        Token.Name.Tag: "#D0914F",
        Token.Name.Variable: "#D9E1DB",
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
        Token.Generic.Emph: "italic #D9E1DB",
        Token.Generic.Strong: "bold #E9EEEC",
        Token.Generic.Deleted: "bg:#432F2B #E1837A",
        Token.Generic.Inserted: "bg:#2B3F31 #80C28E",
        Token.Generic.Error: "#CD6B63",
        Token.Generic.Output: "#A9B5AE",
        Token.Generic.Prompt: "#D0914F",
        Token.Generic.Traceback: "#CD6B63",
    }


style = ParisGuimardStyle
