# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""Paris Carrelage — a Pygments style. Bevelled white tile under a vaulted platform. The light one."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["ParisCarrelageStyle", "style"]


class ParisCarrelageStyle(Style):
    name = "paris-carrelage"
    background_color = "#E4EDE8"
    highlight_color = "#D8E3DC"
    line_number_color = "#7B9989"
    line_number_background_color = "#E4EDE8"
    line_number_special_color = "#9B5D00"
    line_number_special_background_color = "#D8E3DC"

    styles = {
        Token: "#25352C",
        Token.Text: "#25352C",
        Token.Error: "#9E171B",
        Token.Comment: "italic #627F70",
        Token.Comment.Hashbang: "italic #627F70",
        Token.Comment.Preproc: "italic #9A557D",
        Token.Keyword: "#9B5D00",
        Token.Keyword.Constant: "#BB403B",
        Token.Keyword.Type: "italic #277555",
        Token.Operator: "#4F675B",
        Token.Operator.Word: "#9B5D00",
        Token.Punctuation: "#4F675B",
        Token.Name: "#25352C",
        Token.Name.Attribute: "italic #8A6700",
        Token.Name.Builtin: "italic #8A6700",
        Token.Name.Builtin.Pseudo: "italic #BB403B",
        Token.Name.Class: "#277555",
        Token.Name.Constant: "#BB403B",
        Token.Name.Decorator: "italic #9A557D",
        Token.Name.Entity: "#9A557D",
        Token.Name.Exception: "#277555",
        Token.Name.Function: "#8A6700",
        Token.Name.Function.Magic: "italic #8A6700",
        Token.Name.Label: "italic #9A557D",
        Token.Name.Namespace: "#45594F",
        Token.Name.Property: "#374940",
        Token.Name.Tag: "#9B5D00",
        Token.Name.Variable: "#25352C",
        Token.Name.Variable.Magic: "italic #BB403B",
        Token.Literal.Date: "#BB403B",
        Token.Literal.String: "#18803F",
        Token.Literal.String.Affix: "#9B5D00",
        Token.Literal.String.Escape: "#9A557D",
        Token.Literal.String.Interpol: "#9A557D",
        Token.Literal.String.Regex: "#9A557D",
        Token.Literal.String.Symbol: "#BB403B",
        Token.Literal.Number: "#BB403B",
        Token.Generic.Heading: "bold #8A6700",
        Token.Generic.Subheading: "bold #8A6700",
        Token.Generic.Emph: "italic #25352C",
        Token.Generic.Strong: "bold #18231D",
        Token.Generic.Deleted: "bg:#ECD1D1 #BB403B",
        Token.Generic.Inserted: "bg:#C3DECD #18803F",
        Token.Generic.Error: "#9E171B",
        Token.Generic.Output: "#45594F",
        Token.Generic.Prompt: "#9B5D00",
        Token.Generic.Traceback: "#9E171B",
    }


style = ParisCarrelageStyle
