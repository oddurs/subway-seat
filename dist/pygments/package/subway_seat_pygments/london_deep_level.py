# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""London Deep Level — a Pygments style. Below the cut-and-cover lines. The ground drops; the signals don't."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["LondonDeepLevelStyle", "style"]


class LondonDeepLevelStyle(Style):
    name = "london-deep-level"
    background_color = "#121A2D"
    highlight_color = "#1A243A"
    line_number_color = "#53617D"
    line_number_background_color = "#121A2D"
    line_number_special_color = "#F2C03F"
    line_number_special_background_color = "#1A243A"

    styles = {
        Token: "#D4DAE7",
        Token.Text: "#D4DAE7",
        Token.Error: "#DB6052",
        Token.Comment: "italic #6F7C97",
        Token.Comment.Hashbang: "italic #6F7C97",
        Token.Comment.Preproc: "italic #AE9EDC",
        Token.Keyword: "#DE8946",
        Token.Keyword.Constant: "#F17869",
        Token.Keyword.Type: "italic #54B4B5",
        Token.Operator: "#8B96AC",
        Token.Operator.Word: "#DE8946",
        Token.Punctuation: "#8B96AC",
        Token.Name: "#D4DAE7",
        Token.Name.Attribute: "italic #F2C03F",
        Token.Name.Builtin: "italic #F2C03F",
        Token.Name.Builtin.Pseudo: "italic #F17869",
        Token.Name.Class: "#54B4B5",
        Token.Name.Constant: "#F17869",
        Token.Name.Decorator: "italic #AE9EDC",
        Token.Name.Entity: "#AE9EDC",
        Token.Name.Exception: "#54B4B5",
        Token.Name.Function: "#F2C03F",
        Token.Name.Function.Magic: "italic #F2C03F",
        Token.Name.Label: "italic #AE9EDC",
        Token.Name.Namespace: "#A5AEC0",
        Token.Name.Property: "#BEC6D5",
        Token.Name.Tag: "#DE8946",
        Token.Name.Variable: "#D4DAE7",
        Token.Name.Variable.Magic: "italic #F17869",
        Token.Literal.Date: "#F17869",
        Token.Literal.String: "#77C581",
        Token.Literal.String.Affix: "#DE8946",
        Token.Literal.String.Escape: "#AE9EDC",
        Token.Literal.String.Interpol: "#AE9EDC",
        Token.Literal.String.Regex: "#AE9EDC",
        Token.Literal.String.Symbol: "#F17869",
        Token.Literal.Number: "#F17869",
        Token.Generic.Heading: "bold #F2C03F",
        Token.Generic.Subheading: "bold #F2C03F",
        Token.Generic.Emph: "italic #D4DAE7",
        Token.Generic.Strong: "bold #E7EBF3",
        Token.Generic.Deleted: "bg:#402327 #F17869",
        Token.Generic.Inserted: "bg:#22362F #77C581",
        Token.Generic.Error: "#DB6052",
        Token.Generic.Output: "#A5AEC0",
        Token.Generic.Prompt: "#DE8946",
        Token.Generic.Traceback: "#DB6052",
    }


style = LondonDeepLevelStyle
