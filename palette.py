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

# What each role is called on the site and in docs, per family (the dark reading).
NEW_YORK_NAMES = {
    "crust": "Blackout", "mantle": "Espresso", "base": "Paneling", "surface0": "Coppertone",
    "surface1": "Saddle", "surface2": "Corduroy", "overlay0": "Pecan", "overlay1": "Cardboard",
    "overlay2": "Burlap", "subtext0": "Khaki", "subtext1": "Almond", "text": "Parchment",
    "text_hi": "Ivory", "yellow": "Harvest gold", "yellow_hi": "Broadway yellow",
    "orange": "Burnt orange", "orange_hi": "Sixth Avenue", "red": "Redbird", "red_hi": "Redbird bright",
    "green": "Avocado", "green_hi": "Avocado bright", "sage": "Seafoam tile", "sage_hi": "Seafoam bright",
    "denim": "Faded denim", "denim_hi": "Denim bright", "clay": "Terracotta",
}

LONDON_NAMES = {
    "crust": "Running tunnel", "mantle": "Concourse", "base": "Moquette", "surface0": "Armrest",
    "surface1": "Grab rail", "surface2": "Ironwork", "overlay0": "Hoarding", "overlay1": "Etched glass",
    "overlay2": "Frosted", "subtext0": "Chalk", "subtext1": "Vitreous", "text": "Johnston white",
    "text_hi": "Tile white", "yellow": "Hazard line", "yellow_hi": "Hazard bright",
    "orange": "London brick", "orange_hi": "Brick bright", "red": "Corporate red",
    "red_hi": "Corporate bright", "green": "District green", "green_hi": "District bright",
    "sage": "Dockland teal", "sage_hi": "Dockland bright", "denim": "Corporate blue",
    "denim_hi": "Cornflower", "clay": "Elizabeth violet",
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
    id: str        # "walnut" | "tunnel" | "moquette" | …
    name: str      # "Subway Seat", "Subway Seat Tunnel", "London Moquette", …
    slug: str      # "subway-seat", "subway-seat-tunnel", "london-moquette", …
    dark: bool
    family: str    # a Family id: "new-york" | "london"
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

    @property
    def prefix(self):
        """The filename stem of this flavor's family."""
        return FAMILY[self.family].prefix

    @property
    def role_names(self):
        """What this family calls each role."""
        return FAMILY[self.family].role_names

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
    family="new-york",
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
    family="new-york",
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
    family="new-york",
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


# London's accents in two bands, mirroring Walnut's own structure: the four used
# as large fills (prompt segments, diff grounds, git status) hold a tight even
# chroma band so a powerline stripe reads as one ribbon; the rest stay quiet.
LONDON_ACCENTS = {
    "yellow": "#F2C03F", "yellow_hi": "#FFD36C",   # platform-edge hazard line
    "orange": "#DE8946", "orange_hi": "#E5AA7F",   # London brick
    "red": "#DB6052", "red_hi": "#F17869",         # Corporate Red
    "green": "#77C581", "green_hi": "#9AD2A0",     # District green
    "sage": "#54B4B5", "sage_hi": "#72D1D3",       # DLR teal
    "denim": "#7595DA", "denim_hi": "#8BB0FF",     # Corporate Blue
    "clay": "#AE9EDC",                             # Elizabeth violet
}

MOQUETTE = Flavor(
    id="moquette",
    family="london",
    name="London Moquette",
    slug="london-moquette",
    dark=True,
    blurb="The seat you're sitting on. Corporate Blue, turned right down.",
    colors={
        "crust": "#121826", "mantle": "#172032", "base": "#1E2941",
        "surface0": "#263451", "surface1": "#303F61", "surface2": "#3D4F72",
        "overlay0": "#576685", "overlay1": "#73819C", "overlay2": "#8F9AB0",
        "subtext0": "#A9B2C4", "subtext1": "#C1C9D8", "text": "#D8DEEA", "text_hi": "#E9EDF5",
        **LONDON_ACCENTS,
    },
    ansi_roles=DARK_ANSI,
)

DEEP_LEVEL = Flavor(
    id="deep",
    family="london",
    name="London Deep Level",
    slug="london-deep-level",
    dark=True,
    blurb="Below the cut-and-cover lines. The ground drops; the signals don't.",
    colors={
        "crust": "#0A0E18", "mantle": "#0D1421", "base": "#121A2D",
        "surface0": "#1A243A", "surface1": "#232F49", "surface2": "#303E5B",
        "overlay0": "#53617D", "overlay1": "#6F7C97", "overlay2": "#8B96AC",
        "subtext0": "#A5AEC0", "subtext1": "#BEC6D5", "text": "#D4DAE7", "text_hi": "#E7EBF3",
        **LONDON_ACCENTS,
    },
    ansi_roles=DARK_ANSI,
)

PORTLAND = Flavor(
    id="portland",
    family="london",
    name="London Portland",
    slug="london-portland",
    dark=False,
    blurb="Holden's Portland stone. Links are the exact Corporate Blue.",
    colors={
        # As in Enamel, the ramp runs the other way from base.
        "crust": "#CED5E3", "mantle": "#D9E0EC", "base": "#E5EAF6",
        "surface0": "#C1CADC", "surface1": "#ADB7CB", "surface2": "#9BA5B8",
        "overlay0": "#8A919F", "overlay1": "#727781", "overlay2": "#5D6168",
        "subtext0": "#515459", "subtext1": "#434548", "text": "#2F3033", "text_hi": "#1F2022",
        "yellow": "#896800", "yellow_hi": "#977300",
        "orange": "#9F591B", "orange_hi": "#AE672B",
        "red": "#A40005", "red_hi": "#CA2822",
        "green": "#357D41", "green_hi": "#398145",
        "sage": "#007376", "sage_hi": "#008689",
        "denim": "#0019A8", "denim_hi": "#406BD0",   # Corporate Blue, exact
        "clay": "#7660AB",
    },
    ansi_roles=LIGHT_ANSI,
)


@dataclass(frozen=True)
class Family:
    """One city. Same 26 roles, same lightness ladder, different values."""

    id: str          # "new-york" | "london"
    name: str        # "New York"
    blurb: str
    # The signage band the site's nav is built from: New York's black enamel
    # station sign, London's Corporate Blue roundel bar. Same in every flavor.
    sign: dict = field(repr=False)
    # Corner radii the site's furniture is built on. New York rounds everything
    # the way 70s signage did; the Underground sets its signs in rectangles.
    shape: dict = field(repr=False)
    # The stem every one of this family's filenames is built on. Ports that
    # ship one file per flavor plus an auto file name them `<prefix>-<id>` and
    # `<prefix>`, so a port never has to know which city it is writing for.
    prefix: str
    role_names: dict = field(repr=False)
    flavors: tuple = field(repr=False, default=())

    @property
    def default(self):
        return self.flavors[0]

    @property
    def light(self):
        return next(f for f in self.flavors if not f.dark)


NEW_YORK = Family(
    id="new-york",
    name="New York",
    blurb="A 1970s subway car: walnut paneling, orange bucket seats, cream enamel.",
    sign={"bg": "#0C0805", "text": "#F8ECD4", "ring": "#EC7F31"},
    shape={"pill": "999px", "card": "6px", "chip": "50%"},
    prefix="subway-seat",
    role_names=NEW_YORK_NAMES,
    flavors=(WALNUT, TUNNEL, ENAMEL),
)

LONDON = Family(
    id="london",
    name="London",
    blurb="The Tube: Corporate Blue turned down, brick and hazard yellow, the standard red.",
    sign={"bg": "#0019A8", "text": "#FFFFFF", "ring": "#F2C03F"},
    shape={"pill": "2px", "card": "0px", "chip": "2px"},
    prefix="london",
    role_names=LONDON_NAMES,
    flavors=(MOQUETTE, DEEP_LEVEL, PORTLAND),
)

FAMILIES = [NEW_YORK, LONDON]
FAMILY = {fam.id: fam for fam in FAMILIES}
FLAVORS = [f for fam in FAMILIES for f in fam.flavors]
DEFAULT = WALNUT

# The New York names stay importable; ports that name roles should prefer
# `flavor.role_names`, which follows the flavor's family.
ROLE_NAMES = NEW_YORK_NAMES

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
