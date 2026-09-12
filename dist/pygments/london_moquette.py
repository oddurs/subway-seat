# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""London Moquette — a Pygments style. The seat you're sitting on. Corporate Blue, turned right down."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["LondonMoquetteStyle", "style"]


class LondonMoquetteStyle(Style):
    name = "london-moquette"
    background_color = "#1E2941"
    highlight_color = "#263451"
    line_number_color = "#576685"
    line_number_background_color = "#1E2941"
    line_number_special_color = "#F2C03F"
    line_number_special_background_color = "#263451"

    styles = {
        Token: "#D8DEEA",
        Token.Text: "#D8DEEA",
        Token.Error: "#DB6052",
        Token.Comment: "italic #73819C",
        Token.Comment.Hashbang: "italic #73819C",
        Token.Comment.Preproc: "italic #AE9EDC",
        Token.Keyword: "#DE8946",
        Token.Keyword.Constant: "#F17869",
        Token.Keyword.Type: "italic #54B4B5",
        Token.Operator: "#8F9AB0",
        Token.Operator.Word: "#DE8946",
        Token.Punctuation: "#8F9AB0",
        Token.Name: "#D8DEEA",
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
        Token.Name.Namespace: "#A9B2C4",
        Token.Name.Property: "#C1C9D8",
        Token.Name.Tag: "#DE8946",
        Token.Name.Variable: "#D8DEEA",
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
        Token.Generic.Emph: "italic #D8DEEA",
        Token.Generic.Strong: "bold #E9EDF5",
        Token.Generic.Deleted: "bg:#462B31 #F17869",
        Token.Generic.Inserted: "bg:#283E3A #77C581",
        Token.Generic.Error: "#DB6052",
        Token.Generic.Output: "#A9B2C4",
        Token.Generic.Prompt: "#DE8946",
        Token.Generic.Traceback: "#DB6052",
    }


style = LondonMoquetteStyle
