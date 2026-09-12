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


PARIS_NAMES = {
    # The grounds are the architecture; the accents are the map. That split is
    # how the city itself is colored: cast iron and limestone underfoot, and a
    # line colour for everything you need to find.
    "crust": "Ballast", "mantle": "Fonte", "base": "Guimard", "surface0": "Banquette",
    "surface1": "Rambarde", "surface2": "Ferronnerie", "overlay0": "Ardoise",
    "overlay1": "Zinc", "overlay2": "Brume", "subtext0": "Calcaire", "subtext1": "Craie",
    "text": "Faience", "text_hi": "Porcelaine",
    "yellow": "Ligne 1", "yellow_hi": "Ligne 1 clair",
    "orange": "Ligne 11", "orange_hi": "Ligne 11 clair",
    "red": "Rouge RATP", "red_hi": "Rouge clair",
    "green": "Ligne 6", "green_hi": "Ligne 6 clair",
    "sage": "Ligne 12", "sage_hi": "Ligne 12 clair",
    "denim": "Ligne 2", "denim_hi": "Ligne 2 clair",
    "clay": "Ligne 4",
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
        # As in Enamel, the ramp runs the other way from base — and so does the
        # chroma. A dark flavor pulls color out of its text so pale type reads
        # as white; a light flavor must do the opposite, because here the text
        # is the inked end and the paper is the pale one. Holding chroma through
        # subtext and text is what keeps the greys from going dead neutral.
        "crust": "#CDD5E4", "mantle": "#DAE0EB", "base": "#E5EAF4",
        "surface0": "#BFCAE1", "surface1": "#A9B7D4", "surface2": "#95A5C4",
        "overlay0": "#8291AE", "overlay1": "#697794", "overlay2": "#556179",
        "subtext0": "#4A5469", "subtext1": "#3C4557", "text": "#293040", "text_hi": "#1B202B",
        "yellow": "#896800", "yellow_hi": "#977300",
        "orange": "#A45600", "orange_hi": "#B86100",
        "red": "#A40005", "red_hi": "#C92B23",
        "green": "#00822E", "green_hi": "#008730",
        "sage": "#007376", "sage_hi": "#008688",
        "denim": "#0019A8", "denim_hi": "#4A6EBD",   # Corporate Blue, exact
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
    # The signage band the site's nav is built from. Both cities hang dark
    # signs; each one is only tinted toward its own. The brand color is spent
    # on `mark` — a route bullet, a roundel — rather than on the whole band,
    # which is what keeps one nav working for both families.
    sign: dict = field(repr=False)
    # Corner radii the site's furniture is built on. New York rounds everything
    # the way 70s signage did; the Underground sets its signs in rectangles.
    shape: dict = field(repr=False)
    # The one accent the family spends on identity — chrome, primary buttons,
    # the cursor, the site's links. New York's also leads keywords, so it is
    # everywhere; London's leads nothing else, which is what keeps it rare.
    lead: str
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
    # The mark is the family's own lead accent, taken from its default flavor,
    # so the bullet in the nav is the same orange the theme paints keywords in.
    sign={"bg": "#0C0805", "text": "#F8ECD4", "ring": WALNUT.orange,
          "mark": WALNUT.orange, "mark-alt": WALNUT.crust},
    shape={"pill": "999px", "card": "6px", "chip": "50%"},
    lead="orange",
    prefix="subway-seat",
    role_names=NEW_YORK_NAMES,
    flavors=(WALNUT, TUNNEL, ENAMEL),
)

LONDON = Family(
    id="london",
    name="London",
    blurb="The Tube: Corporate Blue turned down, brick and hazard yellow, the standard red.",
    # The roundel is drawn in the flavor's solved red and blue, not the raw
    # #DC241F and #0019A8: those are three times the chroma of anything else on
    # screen and read as a sticker rather than part of the scheme.
    sign={"bg": "#06090F", "text": "#FFFFFF", "ring": MOQUETTE.red,
          "mark": MOQUETTE.red, "mark-alt": MOQUETTE.denim},
    shape={"pill": "2px", "card": "0px", "chip": "2px"},
    lead="red",
    prefix="london",
    role_names=LONDON_NAMES,
    flavors=(MOQUETTE, DEEP_LEVEL, PORTLAND),
)

GUIMARD = Flavor(
    id="guimard",
    family="paris",
    name="Paris Guimard",
    slug="paris-guimard",
    dark=True,
    blurb="Cast-iron green off a Metro entrance. The original green.",
    colors={
        "crust": "#0A1D15", "mantle": "#0C261C", "base": "#0E3125",
        "surface0": "#113E2E", "surface1": "#194A39", "surface2": "#285A47",
        "overlay0": "#47705F", "overlay1": "#67897A", "overlay2": "#86A195",
        "subtext0": "#A2B7AE", "subtext1": "#BBCDC5", "text": "#D3E2DB", "text_hi": "#E6F0EB",
        "yellow": "#EBC342", "yellow_hi": "#FBD664",
        "orange": "#D78E3C", "orange_hi": "#EEA85C",
        "red": "#DA6058", "red_hi": "#EF796F",
        "green": "#73C686", "green_hi": "#82D896",
        "sage": "#6FB393", "sage_hi": "#8ECFAF",
        "denim": "#639BD5", "denim_hi": "#82B7EE",
        "clay": "#E783BD",
    },
    ansi_roles=DARK_ANSI,
)

CATACOMBES = Flavor(
    id="catacombes",
    family="paris",
    name="Paris Catacombes",
    slug="paris-catacombes",
    dark=True,
    blurb="Under the quarries: the same green with the lights turned down.",
    colors={
        "crust": "#05120C", "mantle": "#061811", "base": "#062017",
        "surface0": "#0A2B20", "surface1": "#13382A", "surface2": "#1E4738",
        "overlay0": "#456A5B", "overlay1": "#648576", "overlay2": "#829D91",
        "subtext0": "#9EB3AA", "subtext1": "#B8CAC2", "text": "#CFDED7", "text_hi": "#E4EEE9",
        "yellow": "#EBC342", "yellow_hi": "#FBD664",
        "orange": "#D78E3C", "orange_hi": "#EEA85C",
        "red": "#DA6058", "red_hi": "#EF796F",
        "green": "#73C686", "green_hi": "#82D896",
        "sage": "#6FB393", "sage_hi": "#8ECFAF",
        "denim": "#639BD5", "denim_hi": "#82B7EE",
        "clay": "#E783BD",
    },
    ansi_roles=DARK_ANSI,
)

CARRELAGE = Flavor(
    id="carrelage",
    family="paris",
    name="Paris Carrelage",
    slug="paris-carrelage",
    dark=False,
    blurb="Bevelled white tile under a vaulted platform. The light one.",
    colors={
        # As in Enamel and Portland, the ramp runs the other way from base.
        "crust": "#C8DAD1", "mantle": "#D5E3DD", "base": "#E2EDE8",
        "surface0": "#B6D2C5", "surface1": "#9DC1B1", "surface2": "#88AF9E",
        "overlay0": "#759A8A", "overlay1": "#5C8171", "overlay2": "#4A695C",
        "subtext0": "#405B4F", "subtext1": "#334A41", "text": "#21352D", "text_hi": "#16241E",
        "yellow": "#856A00", "yellow_hi": "#937500",
        "orange": "#9B5D00", "orange_hi": "#AE6800",
        "red": "#A30013", "red_hi": "#C82C2C",
        "green": "#00823B", "green_hi": "#00863D",
        "sage": "#007752", "sage_hi": "#2A8862",
        "denim": "#0961A9", "denim_hi": "#2E75B9",
        "clay": "#B43586",
    },
    ansi_roles=LIGHT_ANSI,
)


PARIS = Family(
    id="paris",
    name="Paris",
    blurb="The Metro: Guimard's cast-iron green, white tile, and the line colors of the map.",
    sign={"bg": "#040B07", "text": "#FFFFFF", "ring": GUIMARD.clay,
          "mark": GUIMARD.clay, "mark-alt": "#FFFFFF"},
    # Art Nouveau bends; nothing Guimard drew was ever square.
    shape={"pill": "999px", "card": "14px", "chip": "50%"},
    # Line 4's magenta. It leads escapes and regex, which are rare, so spending
    # it on chrome keeps it rare there too.
    lead="clay",
    prefix="paris",
    role_names=PARIS_NAMES,
    flavors=(GUIMARD, CATACOMBES, CARRELAGE),
)

FAMILIES = [NEW_YORK, LONDON, PARIS]
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
