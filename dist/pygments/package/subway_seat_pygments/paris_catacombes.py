# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Catacombes — a Pygments style. Under the quarries: the same green with the lights turned down."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCatacombesStyle", "style"]


class ParisCatacombesStyle(Style):
    name = "paris-catacombes"
    background_color = "#062017"
    highlight_color = "#0A2B20"
    line_number_color = "#456A5B"
    line_number_background_color = "#062017"
    line_number_special_color = "#EBC342"
    line_number_special_background_color = "#0A2B20"

    styles = {
        Token: "#CFDED7",
        Token.Text: "#CFDED7",
        Token.Error: "#DA6058",
        Token.Comment: "italic #648576",
        Token.Comment.Hashbang: "italic #648576",
        Token.Comment.Preproc: "italic #E783BD",
        Token.Keyword: "#D78E3C",
        Token.Keyword.Constant: "#EF796F",
        Token.Keyword.Type: "italic #6FB393",
        Token.Operator: "#829D91",
        Token.Operator.Word: "#D78E3C",
        Token.Punctuation: "#829D91",
        Token.Name: "#CFDED7",
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
        Token.Name.Namespace: "#9EB3AA",
        Token.Name.Property: "#B8CAC2",
        Token.Name.Tag: "#D78E3C",
        Token.Name.Variable: "#CFDED7",
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
        Token.Generic.Emph: "italic #CFDED7",
        Token.Generic.Strong: "bold #E4EEE9",
        Token.Generic.Deleted: "bg:#3C2620 #EF796F",
        Token.Generic.Inserted: "bg:#1D3A27 #73C686",
        Token.Generic.Error: "#DA6058",
        Token.Generic.Output: "#9EB3AA",
        Token.Generic.Prompt: "#D78E3C",
        Token.Generic.Traceback: "#DA6058",
    }


style = ParisCatacombesStyle
