"""Subway Seat — the single source of truth for every generated theme.

A 1970s palette: walnut-brown ground, parchment cream text, harvest-gold and
burnt-orange accents, avocado green. The blues and purples of a "normal"
16-color palette are deliberately faded (denim) or re-assigned (magenta is
burnt orange) so the whole screen stays in the same warm room.

Every flavor defines the same roles, so a port written against roles works for
all of them. Ports read colors as attributes: `f.base`, `f.orange`, `f.text_hi`.
"""

from dataclasses import dataclass, field

# Role order, darkest → lightest ground, then text, then accents.
GROUND = ["crust", "mantle", "base", "surface0", "surface1", "surface2", "overlay0", "overlay1", "overlay2"]
TEXT = ["subtext0", "subtext1", "text", "text_hi"]
ACCENTS = [
    "yellow", "yellow_hi", "orange", "orange_hi", "red", "red_hi", "green", "green_hi",
    "sage", "sage_hi", "denim", "denim_hi", "clay",
]
ROLES = GROUND + TEXT + ACCENTS

# What each role is called on the site and in docs (the dark-flavor reading).
ROLE_NAMES = {
    "crust": "Blackout", "mantle": "Espresso", "base": "Paneling", "surface0": "Coppertone",
    "surface1": "Saddle", "surface2": "Corduroy", "overlay0": "Pecan", "overlay1": "Cardboard",
    "overlay2": "Burlap", "subtext0": "Khaki", "subtext1": "Almond", "text": "Parchment",
    "text_hi": "Ivory", "yellow": "Harvest gold", "yellow_hi": "Broadway yellow",
    "orange": "Burnt orange", "orange_hi": "Sixth Avenue", "red": "Redbird", "red_hi": "Redbird bright",
    "green": "Avocado", "green_hi": "Avocado bright", "sage": "Seafoam tile", "sage_hi": "Seafoam bright",
    "denim": "Faded denim", "denim_hi": "Denim bright", "clay": "Terracotta",
}

# What each accent does (the syntax role it leads), for docs and the site.
ACCENT_ROLES = {
    "orange": "keywords, tags, the Claude spinner",
    "yellow": "functions, commands, the cursor",
    "green": "strings, additions",
    "sage": "types, classes, options",
    "red_hi": "numbers, constants, deletions",
    "clay": "escapes, regex, decorators",
    "denim": "links and info, the only cool color",
}

# What every role is used for, for the site's palette page and dist/json.
ROLE_USES = {
    "crust": "grooves and borders between panes",
    "mantle": "chrome: sidebars, title and status bars",
    "base": "the editor and terminal ground",
    "surface0": "the current line, inputs, popovers",
    "surface1": "raised controls, terminal black",
    "surface2": "selection",
    "overlay0": "gutters, whitespace, indent guides",
    "overlay1": "comments, line numbers, bright black",
    "overlay2": "punctuation, muted labels",
    "subtext0": "placeholders, quiet labels",
    "subtext1": "sidebar and secondary text",
    "text": "body text, variables",
    "text_hi": "headings, the active line number, bold",
    **ACCENT_ROLES,
    "yellow_hi": "bright yellow, emphasis on gold",
    "orange_hi": "bright magenta, the Claude spinner shimmer",
    "red": "errors, terminal red",
    "green_hi": "bright green",
    "sage_hi": "bright cyan",
    "denim_hi": "bright blue",
}


@dataclass(frozen=True)
class Flavor:
    id: str        # "walnut" | "tunnel" | "enamel"
    name: str      # "Subway Seat", "Subway Seat Tunnel", …
    slug: str      # "subway-seat", "subway-seat-tunnel", …
    dark: bool
    blurb: str
    colors: dict = field(repr=False)
    # ANSI 0–15 as role names
    ansi_roles: tuple = field(repr=False, default=())

    def __getattr__(self, role):
        try:
            return self.colors[role]
        except KeyError:
            raise AttributeError(role) from None

    @property
    def ansi(self):
        return [self.colors[r] for r in self.ansi_roles]

    @property
    def snake(self):
        return self.slug.replace("-", "_")

    def syntax(self, role):
        """(hex, styles) for a syntax role."""
        color_role, styles = SYNTAX[role]
        return self.colors[color_role], styles

    def mix(self, a, b, t):
        """Mix role/hex `a` into `b` by t (0..1): t=0 → b, t=1 → a."""
        return blend(self.colors.get(a, a), self.colors.get(b, b), t)


DARK_ANSI = (
    "surface1", "red", "green", "yellow", "denim", "orange", "sage", "subtext1",
    "overlay1", "red_hi", "green_hi", "yellow_hi", "denim_hi", "orange_hi", "sage_hi", "text_hi",
)
LIGHT_ANSI = (
    "subtext1", "red", "green", "yellow", "denim", "orange", "sage", "surface2",
    "overlay1", "red_hi", "green_hi", "yellow_hi", "denim_hi", "orange_hi", "sage_hi", "surface1",
)

DARK_ACCENTS = {
    "yellow": "#F3BF45", "yellow_hi": "#FFD36B",
    "orange": "#EC7F31", "orange_hi": "#FF9D55",
    "red": "#E05C45", "red_hi": "#F97160",
    "green": "#ADB956", "green_hi": "#BFCB63",
    "sage": "#86AD95", "sage_hi": "#A5C9B0",
    "denim": "#7F9BAE", "denim_hi": "#9DB6C6",
    "clay": "#E0956C",
}

WALNUT = Flavor(
    id="walnut",
    name="Subway Seat",
    slug="subway-seat",
    dark=True,
    blurb="Walnut paneling and orange bucket seats. The original.",
    colors={
        "crust": "#20160E", "mantle": "#2A1D13", "base": "#362619",
        "surface0": "#43301F", "surface1": "#513B27", "surface2": "#634932",
        "overlay0": "#7B6047", "overlay1": "#967B5C", "overlay2": "#AE9575",
        "subtext0": "#C4AE8C", "subtext1": "#D9C6A3", "text": "#EDDCBC", "text_hi": "#F8ECD4",
        **DARK_ACCENTS,
    },
    ansi_roles=DARK_ANSI,
)

TUNNEL = Flavor(
    id="tunnel",
    name="Subway Seat Tunnel",
    slug="subway-seat-tunnel",
    dark=True,
    blurb="The late local after midnight: espresso-deep, same warm lights.",
    colors={
        "crust": "#140D07", "mantle": "#1B120A", "base": "#24180E",
        "surface0": "#302115", "surface1": "#3D2C1D", "surface2": "#4F3927",
        "overlay0": "#745B45", "overlay1": "#917759", "overlay2": "#AA9171",
        "subtext0": "#C0AA88", "subtext1": "#D6C3A0", "text": "#E9D8B6", "text_hi": "#F6EAD1",
        **DARK_ACCENTS,
    },
    ansi_roles=DARK_ANSI,
)

ENAMEL = Flavor(
    id="enamel",
    name="Subway Seat Enamel",
    slug="subway-seat-enamel",
    dark=False,
    blurb="Cream enamel panels in the morning sun. The light one.",
    colors={
        # In the light flavor the ramp runs the other way: crust is the
        # darkest *ground* (title bars), surfaces darken for hover/selection.
        "crust": "#E2D3B6", "mantle": "#EBDEC6", "base": "#F4E9D4",
        "surface0": "#D9C8A7", "surface1": "#CAB48E", "surface2": "#BAA07A",
        "overlay0": "#A58C6A", "overlay1": "#8C7254", "overlay2": "#735C44",
        "subtext0": "#654F3B", "subtext1": "#54402F", "text": "#3E2C1E", "text_hi": "#2A1D13",
        "yellow": "#936200", "yellow_hi": "#A56E00",
        "orange": "#AD4E00", "orange_hi": "#C4561A",
        "red": "#992418", "red_hi": "#BC4031",
        "green": "#66740F", "green_hi": "#697813",
        "sage": "#3E7157", "sage_hi": "#4C8367",
        "denim": "#3F6480", "denim_hi": "#517791",
        "clay": "#A65633",
    },
    ansi_roles=LIGHT_ANSI,
)

FLAVORS = [WALNUT, TUNNEL, ENAMEL]
DEFAULT = WALNUT

# ── Syntax roles, shared by every editor port ──────────────────────────────
# role → (color role, styles ⊂ {"bold", "italic"})
SYNTAX = {
    "comment": ("overlay1", {"italic"}),
    "keyword": ("orange", set()),
    "storage": ("orange", set()),
    "operator": ("overlay2", set()),
    "punctuation": ("overlay2", set()),
    "function": ("yellow", set()),
    "function.builtin": ("yellow", {"italic"}),
    "string": ("green", set()),
    "string.escape": ("clay", set()),
    "regexp": ("clay", set()),
    "number": ("red_hi", set()),
    "constant": ("red_hi", set()),
    "boolean": ("red_hi", set()),
    "type": ("sage", set()),
    "type.builtin": ("sage", {"italic"}),
    "variable": ("text", set()),
    "variable.builtin": ("red_hi", {"italic"}),
    "parameter": ("subtext1", {"italic"}),
    "property": ("subtext1", set()),
    "namespace": ("subtext0", set()),
    "tag": ("orange", set()),
    "attribute": ("yellow", {"italic"}),
    "decorator": ("clay", {"italic"}),
    "heading": ("yellow", {"bold"}),
    "link": ("denim", set()),
    "code": ("green", set()),
    "emphasis": ("text", {"italic"}),
    "strong": ("text_hi", {"bold"}),
    "quote": ("subtext0", {"italic"}),
    "invalid": ("red", set()),
}


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def blend(fg, bg, alpha):
    """Mix fg over bg at alpha (0..1) — for tints and in-between grounds."""
    if not 0 <= alpha <= 1:
        raise ValueError(f"blend alpha {alpha} is outside 0..1")
    f, b = hex_to_rgb(fg), hex_to_rgb(bg)
    r, g, b_ = (round(fi * alpha + bi * (1 - alpha)) for fi, bi in zip(f, b, strict=True))
    return f"#{r:02X}{g:02X}{b_:02X}"


def alpha(color, a):
    """#RRGGBB + alpha (0..1) → #RRGGBBAA."""
    if len(color) != 7 or not 0 <= a <= 1:
        raise ValueError(f"alpha() wants #RRGGBB and 0..1, got {color!r}, {a}")
    return f"{color}{round(a * 255):02X}"
