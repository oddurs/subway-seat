"""Slack: sidebar theme strings, in the current four-colour format and the legacy ten."""

from ports._apps import ink
from ports._lib import HEADER, Out

META = {
    "id": "slack",
    "name": "Slack",
    "category": "Apps",
    "homepage": "https://slack.com",
    "enable": {
        "where": "Slack → Preferences → Appearance → Custom theme",
        "code": "Paste the {name} string from {slug}.txt into any message and click\n"
        "“Switch sidebar theme”, or enter the four colours under Custom theme.",
        "lang": "text",
    },
    "notes": "Slack only lets themes colour the sidebar and a few highlights; the message pane follows "
    "Slack's own light or dark mode, so pick dark for Walnut and Tunnel and light for Enamel.",
}


def modern(f):
    # System navigation, Selected items, Presence indication, Notifications
    return [f.mantle, f.orange, f.green, f.red_hi if f.dark else f.red]


def legacy(f):
    # Column BG, Menu BG Hover, Active Item, Active Item Text, Hover Item,
    # Text Color, Active Presence, Mention Badge, Top Nav BG, Top Nav Text
    return [
        f.mantle, f.surface0, f.orange, ink(f), f.surface0,
        f.text, f.green, f.red_hi if f.dark else f.red, f.crust, f.text,
    ]


def build(flavors):
    outs = []
    for f in flavors:
        mode = "dark" if f.dark else "light"
        body = "\n".join([
            f"# {HEADER}",
            f"# {f.name}: set Slack's colour mode to {mode}.",
            "#",
            "# Current Slack: system navigation, selected items, presence, notifications",
            ",".join(modern(f)),
            "",
            "# Legacy ten-colour string (older clients and theme sites)",
            ",".join(legacy(f)),
        ]) + "\n"
        outs.append(Out(f"{f.slug}.txt", body, flavor=f.id,
                        dest="Slack → Preferences → Appearance → Custom theme", lang="text"))
    return outs
