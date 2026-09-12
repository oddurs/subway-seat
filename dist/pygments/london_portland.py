# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
"""London Portland — a Pygments style. Holden's Portland stone. Links are the exact Corporate Blue."""

from pygments.style import Style
from pygments.token import Token

__all__ = ["LondonPortlandStyle", "style"]


class LondonPortlandStyle(Style):
    name = "london-portland"
    background_color = "#E8F0FF"
    highlight_color = "#DCE5F7"
    line_number_color = "#8192B4"
    line_number_background_color = "#E8F0FF"
    line_number_special_color = "#A54300"
    line_number_special_background_color = "#DCE5F7"

    styles = {
        Token: "#293040",
        Token.Text: "#293040",
        Token.Error: "#9B211A",
        Token.Comment: "italic #697794",
        Token.Comment.Hashbang: "italic #697794",
        Token.Comment.Preproc: "italic #755FA9",
        Token.Keyword: "#A54300",
        Token.Keyword.Constant: "#CC2E25",
        Token.Keyword.Type: "italic #007376",
        Token.Operator: "#556179",
        Token.Operator.Word: "#A54300",
        Token.Punctuation: "#556179",
        Token.Name: "#293040",
        Token.Name.Attribute: "italic #8D6C08",
        Token.Name.Builtin: "italic #8D6C08",
        Token.Name.Builtin.Pseudo: "italic #CC2E25",
        Token.Name.Class: "#007376",
        Token.Name.Constant: "#CC2E25",
        Token.Name.Decorator: "italic #755FA9",
        Token.Name.Entity: "#755FA9",
        Token.Name.Exception: "#007376",
        Token.Name.Function: "#8D6C08",
        Token.Name.Function.Magic: "italic #8D6C08",
        Token.Name.Label: "italic #755FA9",
        Token.Name.Namespace: "#4A5469",
        Token.Name.Property: "#3C4557",
        Token.Name.Tag: "#A54300",
        Token.Name.Variable: "#293040",
        Token.Name.Variable.Magic: "italic #CC2E25",
        Token.Literal.Date: "#CC2E25",
        Token.Literal.String: "#0D8131",
        Token.Literal.String.Affix: "#A54300",
        Token.Literal.String.Escape: "#755FA9",
        Token.Literal.String.Interpol: "#755FA9",
        Token.Literal.String.Regex: "#755FA9",
        Token.Literal.String.Symbol: "#CC2E25",
        Token.Literal.Number: "#CC2E25",
        Token.Generic.Heading: "bold #8D6C08",
        Token.Generic.Subheading: "bold #8D6C08",
        Token.Generic.Emph: "italic #293040",
        Token.Generic.Strong: "bold #1B202B",
        Token.Generic.Deleted: "bg:#EBD3D1 #CC2E25",
        Token.Generic.Inserted: "bg:#C0DEC9 #0D8131",
        Token.Generic.Error: "#9B211A",
        Token.Generic.Output: "#4A5469",
        Token.Generic.Prompt: "#A54300",
        Token.Generic.Traceback: "#9B211A",
    }


style = LondonPortlandStyle
