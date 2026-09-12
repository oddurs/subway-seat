# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Guimard — a Pygments style. Cast-iron green off a Metro entrance. The original green."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisGuimardStyle", "style"]


class ParisGuimardStyle(Style):
    name = "paris-guimard"
    background_color = "#0E3125"
    highlight_color = "#113E2E"
    line_number_color = "#47705F"
    line_number_background_color = "#0E3125"
    line_number_special_color = "#EBC342"
    line_number_special_background_color = "#113E2E"

    styles = {
        Token: "#D3E2DB",
        Token.Text: "#D3E2DB",
        Token.Error: "#DA6058",
        Token.Comment: "italic #67897A",
        Token.Comment.Hashbang: "italic #67897A",
        Token.Comment.Preproc: "italic #E783BD",
        Token.Keyword: "#D78E3C",
        Token.Keyword.Constant: "#EF796F",
        Token.Keyword.Type: "italic #6FB393",
        Token.Operator: "#86A195",
        Token.Operator.Word: "#D78E3C",
        Token.Punctuation: "#86A195",
        Token.Name: "#D3E2DB",
        Token.Name.Attribute: "italic #EBC342",
        Token.Name.Builtin: "italic #EBC342",
        Token.Name.Builtin.Pseudo: "italic #EF796F",
        Token.Name.Class: "#6FB393",
        Token.Name.Constant: "#EF796F",
        Token.Name.Decorator: "italic #E783BD",
        Token.Name.Entity: "#E783BD",
        Token.Name.Exception: "#6FB393",
        Token.Name.Function: "#EBC342",
        Token.Name.Function.Magic: "italic #EBC342",
        Token.Name.Label: "italic #E783BD",
        Token.Name.Namespace: "#A2B7AE",
        Token.Name.Property: "#BBCDC5",
        Token.Name.Tag: "#D78E3C",
        Token.Name.Variable: "#D3E2DB",
        Token.Name.Variable.Magic: "italic #EF796F",
        Token.Literal.Date: "#EF796F",
        Token.Literal.String: "#73C686",
        Token.Literal.String.Affix: "#D78E3C",
        Token.Literal.String.Escape: "#E783BD",
        Token.Literal.String.Interpol: "#E783BD",
        Token.Literal.String.Regex: "#E783BD",
        Token.Literal.String.Symbol: "#EF796F",
        Token.Literal.Number: "#EF796F",
        Token.Generic.Heading: "bold #EBC342",
        Token.Generic.Subheading: "bold #EBC342",
        Token.Generic.Emph: "italic #D3E2DB",
        Token.Generic.Strong: "bold #E6F0EB",
        Token.Generic.Deleted: "bg:#402E26 #EF796F",
        Token.Generic.Inserted: "bg:#21422E #73C686",
        Token.Generic.Error: "#DA6058",
        Token.Generic.Output: "#A2B7AE",
        Token.Generic.Prompt: "#D78E3C",
        Token.Generic.Traceback: "#DA6058",
    }


style = ParisGuimardStyle
