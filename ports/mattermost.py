"""Mattermost: a custom theme JSON per flavor, pasted into the theme editor."""

import json

from ports._lib import Out, ink, solid

META = {
    "id": "mattermost",
    "name": "Mattermost",
    "category": "Apps",
    "homepage": "https://mattermost.com",
    "detect": ["/Applications/Mattermost.app"],
    "enable": {
        "where": "Mattermost › Settings › Display › Theme › Edit › Custom Theme",
        "code": "Paste the contents of {slug}.json into “Copy and paste to share theme colors”.",
        "lang": "text",
    },
    "notes": "An espresso sidebar with a blackout team bar, orange buttons, mention badges and "
    "active-channel marks, denim links and a harvest-gold wash on messages that mention you. "
    "Code blocks use Mattermost's Monokai (Walnut, Tunnel) or Solarized Light (Enamel), the "
    "closest of its four code themes. Mattermost has no light/dark pairing for custom themes.",
}


def theme(f):
    return {
        # Sidebar. Mattermost dims sidebarText to 64% for read channels (so it starts
        # from text_hi) and paints the active channel with an 8% sidebarText wash plus
        # a sidebarTextActiveBorder mark.
        "sidebarBg": f.mantle,
        "sidebarText": f.text_hi,
        "sidebarUnreadText": f.text_hi,
        "sidebarTextHoverBg": solid("text@L2", f, over="mantle"),
        "sidebarTextActiveBorder": f.orange,
        "sidebarTextActiveColor": ink(f),  # text on sidebarTextActiveBorder badges
        "sidebarHeaderBg": f.crust,  # the global header across the top
        "sidebarHeaderTextColor": f.text,
        "sidebarTeamBarBg": f.crust,
        # Presence
        "onlineIndicator": f.green,
        "awayIndicator": f.yellow,
        "dndIndicator": f.red_hi,
        # Mention badges
        "mentionBg": f.orange,
        "mentionBj": f.orange,  # legacy spelling Mattermost still ships in its presets
        "mentionColor": ink(f),
        # Center channel
        "centerChannelBg": f.base,
        "centerChannelColor": f.text,
        "newMessageSeparator": f.red_hi,
        "linkColor": f.denim,
        "buttonBg": f.orange,
        "buttonColor": ink(f),
        "errorTextColor": f.red_hi,
        # Used as-is behind @mentions of you, and mixed 50/50 with the channel
        # ground behind whole posts that mention you.
        "mentionHighlightBg": f.mix("yellow", "base", 0.45),
        "mentionHighlightLink": f.text_hi,
        "codeTheme": "monokai" if f.dark else "solarized-light",
    }


def build(flavors):
    how = "Mattermost › Settings › Display › Theme › Edit › Custom Theme: paste into “Copy and paste to share theme colors”"
    return [
        Out(f"{f.slug}.json", json.dumps(theme(f), indent=2) + "\n", flavor=f.id, lang="json", how=how) for f in flavors
    ]
