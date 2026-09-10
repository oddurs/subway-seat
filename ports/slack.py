"""Slack: sidebar theme strings, in the current four-color format and the legacy ten."""

from ports._lib import HEADER, Out, ink

META = {
    "id": "slack",
    "name": "Slack",
    "category": "Apps",
    "homepage": "https://slack.com",
    "enable": {
        "where": "Slack › Preferences › Themes",
        "code": "Paste a string from {slug}.txt into Import theme, or into any message\n"
        "and click “Switch sidebar theme”. The four colors also go one by one under Custom theme.",
        "lang": "text",
    },
    "detect": ["/Applications/Slack.app", "slack"],
    "notes": "Slack only lets themes color the sidebar and a few highlights; the message pane follows "
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
            f"# {f.name}: set Slack's color mode to {mode}.",
            "#",
            "# Current Slack: system navigation, selected items, presence, notifications",
            ",".join(modern(f)),
            "",
            "# Legacy ten-color string (older clients and theme sites)",
            ",".join(legacy(f)),
        ]) + "\n"
        outs.append(Out(f"{f.slug}.txt", body, flavor=f.id, lang="text",
                        how="paste a string into Slack › Preferences › Themes › Import theme"))
    return outs
