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
    line_number_special_color = "#F1BF4B"
    line_number_special_background_color = "#263930"

    styles = {
        Token: "#D9E1DB",
        Token.Text: "#D9E1DB",
        Token.Error: "#C7665B",
        Token.Comment: "italic #74857C",
        Token.Comment.Hashbang: "italic #74857C",
        Token.Comment.Preproc: "italic #FAB49C",
        Token.Keyword: "#CA9245",
        Token.Keyword.Constant: "#E7877B",
        Token.Keyword.Type: "italic #549B9F",
        Token.Operator: "#909E96",
        Token.Operator.Word: "#CA9245",
        Token.Punctuation: "#909E96",
        Token.Name: "#D9E1DB",
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
        Token.Name.Namespace: "#A9B5AE",
        Token.Name.Property: "#C2CBC5",
        Token.Name.Tag: "#CA9245",
        Token.Name.Variable: "#D9E1DB",
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
        Token.Generic.Emph: "italic #D9E1DB",
        Token.Generic.Strong: "bold #E9EEEC",
        Token.Generic.Deleted: "bg:#422E29 #E7877B",
        Token.Generic.Inserted: "bg:#274137 #70CAA9",
        Token.Generic.Error: "#C7665B",
        Token.Generic.Output: "#A9B5AE",
        Token.Generic.Prompt: "#CA9245",
        Token.Generic.Traceback: "#C7665B",
    }


style = ParisGuimardStyle
