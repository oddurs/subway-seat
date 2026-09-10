"""Element: a custom theme per flavor (legacy colors plus Compound design tokens)."""

import json

import palette as p
from ports._lib import Out, selection

META = {
    "id": "element",
    "name": "Element",
    "category": "Apps",
    "homepage": "https://element.io",
    "detect": ["/Applications/Element.app"],
    "enable": {
        "where": "Element › Settings › Appearance (turn off “Match system theme” first)",
        "code": 'Theme: {name}\n// or, in config.json: "default_theme": "custom-{name}"',
        "lang": "text",
    },
    "notes": "A custom theme that sets Element's Compound color scales from the palette, so every "
    "surface follows: a paneling timeline, espresso room list and blackout space bar, orange where "
    "Element uses its green accent (success stays avocado), and usernames in the warm accents. "
    "Element Desktop and self-hosted Element take all three from config.json; app.element.io adds "
    "one at a time from a theme URL. Element's “Match system theme” only switches between its own "
    "light and dark themes, so custom themes don't follow the OS.",
}

STEPS = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400)
# How much of the hue each step keeps: toward the canvas below 900, toward text_hi above it.
TOWARD_BASE = {100: 0.10, 200: 0.15, 300: 0.22, 400: 0.32, 500: 0.44, 600: 0.54, 700: 0.67, 800: 0.83}
TOWARD_TEXT = {1000: 0.85, 1100: 0.70, 1200: 0.50, 1300: 0.30, 1400: 0.15}
# Compound hue scale → palette role. The cool hues fold into the warm ones.
HUES = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "lime": "green_hi",
    "green": "green",
    "cyan": "sage",
    "blue": "denim",
    "purple": "clay",
    "fuchsia": "orange_hi",
    "pink": "red_hi",
}


def grays(f):
    """The Compound gray scale from the ground roles: 100 sits just off the canvas, 1400 is text_hi."""
    c = f.colors
    if f.dark:
        low = [
            f.mix("surface0", "base", 1 / 3),
            f.mix("surface0", "base", 2 / 3),
            c["surface0"],
            c["surface1"],
            c["surface2"],
            c["overlay0"],
            f.mix("overlay1", "overlay0", 0.5),
        ]
    else:
        low = [
            f.mix("mantle", "base", 0.5),
            c["mantle"],
            c["crust"],
            c["surface0"],
            c["surface1"],
            c["surface2"],
            c["overlay0"],
        ]
    high = [
        c["overlay1"],
        c["overlay2"],
        c["subtext0"],
        c["subtext1"],
        f.mix("text", "subtext1", 0.5),
        c["text"],
        c["text_hi"],
    ]
    return dict(zip(STEPS, low + high, strict=True))


def ramp(f, role):
    out = {step: f.mix(role, "base", t) for step, t in TOWARD_BASE.items()}
    out[900] = f.colors[role]
    out.update({step: f.mix(role, "text_hi", t) for step, t in TOWARD_TEXT.items()})
    return out


def alpha_over_base(f, color, ink):
    """#RRGGBBAA of `ink` whose alpha best reproduces `color` over the canvas (least squares)."""
    base, fg, target = (p.hex_to_rgb(x) for x in (f.base, ink, color))
    num = sum((t - b) * (i - b) for t, b, i in zip(target, base, fg, strict=True))
    den = sum((i - b) ** 2 for b, i in zip(base, fg, strict=True))
    return p.alpha(ink, min(1.0, max(0.0, num / den)))


def compound(f):
    tokens = {"--cpd-color-theme-bg": f.base}
    gray = grays(f)
    tokens.update({f"--cpd-color-gray-{s}": v for s, v in gray.items()})
    tokens.update({f"--cpd-color-alpha-gray-{s}": alpha_over_base(f, v, f.text_hi) for s, v in gray.items()})
    for hue, role in HUES.items():
        scale = ramp(f, role)
        tokens.update({f"--cpd-color-{hue}-{s}": v for s, v in scale.items()})
        # Below 900 the solid step is exactly the hue at that strength over the canvas.
        tokens.update(
            {
                f"--cpd-color-alpha-{hue}-{s}": p.alpha(f.colors[role], TOWARD_BASE[s])
                if s in TOWARD_BASE
                else p.alpha(v, 1)
                for s, v in scale.items()
            }
        )

    def ref(name):
        return f"var(--cpd-color-{name})"

    # Semantic tokens where the palette disagrees with Compound: body text is `text`
    # (not the brightest step) and the accent is burnt orange, not green.
    stops = (1100, 900, 700, 500) if f.dark else (500, 700, 900, 1100)
    tokens.update(
        {
            "--cpd-color-text-primary": ref("gray-1300"),
            # errors read like the editors' red_hi: one step off redbird, toward the text
            "--cpd-color-text-critical-primary": ref("red-1000"),
            "--cpd-color-icon-critical-primary": ref("red-1000"),
            "--cpd-color-text-action-accent": ref("orange-900"),
            "--cpd-color-text-badge-accent": ref("orange-1100"),
            "--cpd-color-bg-accent-rest": ref("orange-900"),
            "--cpd-color-bg-accent-hovered": ref("orange-1000"),
            "--cpd-color-bg-accent-pressed": ref("orange-1100"),
            "--cpd-color-bg-accent-selected": ref("alpha-orange-300"),
            "--cpd-color-bg-accent-subtle": ref("orange-200"),
            "--cpd-color-bg-badge-accent": ref("orange-400"),
            "--cpd-color-border-accent-subtle": ref("orange-700"),
            "--cpd-color-border-accent-primary": ref("orange-900"),
            "--cpd-color-icon-accent-primary": ref("orange-900"),
            "--cpd-color-icon-accent-tertiary": ref("orange-800"),
            **{f"--cpd-color-gradient-action-stop{i}": ref(f"orange-{s}") for i, s in enumerate(stops, 1)},
        }
    )
    return tokens


def colors(f):
    """The legacy variables Element's custom-theme stylesheet (_custom.pcss) still reads. Hex only:
    Element derives -0pct/-15pct/-50pct variants from each."""
    gray = grays(f)
    orange = ramp(f, "orange")
    return {
        "accent-color": f.orange,
        "primary-color": f.orange,
        "warning-color": f.red,
        "alert": f.red_hi,
        "links": f.denim,
        "primary-content": f.text,
        "secondary-content": f.subtext0,
        "tertiary-content": f.overlay2,
        "quaternary-content": f.overlay1,
        "quinary-content": f.overlay0,
        "system": gray[300],
        "system-transparent": p.alpha(gray[300], 0),
        "background": f.base,
        "sidebar-color": f.crust,
        "roomlist-background-color": f.mantle,
        "roomlist-highlights-color": gray[300],
        "roomlist-separator-color": gray[400],
        "secondary-hairline-color": gray[300],
        "timeline-background-color": f.base,
        "timeline-text-color": f.text,
        "timeline-text-secondary-color": f.subtext0,
        "timeline-highlights-color": f.mix("yellow", "base", 0.14),
        "focus-bg-color": selection(f),
        "room-highlight-color": gray[400],
        "menu-selected-color": gray[300],
        "togglesw-off-color": f.overlay0,
        "reaction-row-button-selected-bg-color": orange[300],
        "eventbubble-self-bg": f.mix("orange", "base", 0.14),
        "eventbubble-others-bg": gray[300],
        "eventbubble-bg-hover": gray[200],
        **{f"accent-color-{s}": v for s, v in orange.items()},
    }


def theme(f):
    return {"name": f.name, "is_dark": f.dark, "colors": colors(f), "compound": compound(f)}


def build(flavors):
    raw = "https://raw.githubusercontent.com/oddurs/subway-seat/main/dist/element"
    outs = [
        Out(
            f"{f.slug}.json",
            json.dumps(theme(f), indent=2) + "\n",
            flavor=f.id,
            lang="json",
            how=f"app.element.io: type /devtools in any room › Custom themes, and add {raw}/{f.slug}.json",
        )
        for f in flavors
    ]
    config = {"setting_defaults": {"custom_themes": [theme(f) for f in flavors]}}
    outs.append(
        Out(
            "config.json",
            json.dumps(config, indent=2) + "\n",
            lang="json",
            how="Element Desktop or self-hosted Element: merge `setting_defaults` into Element's config.json "
            "(macOS ~/Library/Application Support/Element/config.json, Linux ~/.config/Element/config.json, "
            "Windows %APPDATA%\\Element\\config.json; create it if it's missing), then restart Element",
        )
    )
    return outs
