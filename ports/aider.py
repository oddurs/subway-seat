"""Aider: color settings for .aider.conf.yml, one snippet per flavor.

Two aider quirks shape the file (aider/io.py, aider/main.py):
- `completion-menu-current-color` paints the highlighted item's *background* and
  `completion-menu-current-bg-color` its *text*, the reverse of their names.
- `dark-mode` / `light-mode` are applied after the config file and overwrite the
  prompt, reply, error, warning and code-theme colors, so the snippet leaves them off.

Code blocks default to rich's `ansi_dark` / `ansi_light`, which draw with the
terminal's own colors. A Pygments style name only works when that style is
installed in aider's environment; otherwise rich quietly falls back to Pygments'
light `default`, grey boxes on a dark terminal. So the Subway Seat style (from
the Pygments port's `package/`) is an opt-in line.
"""

from ports._lib import HEADER, MARK_END, MARK_START, Out, ink
from ports.pygments import PACKAGE_URL

META = {
    "id": "aider",
    "name": "Aider",
    "category": "Agents",
    "homepage": "https://aider.chat",
    "enable": {
        "where": "~/.aider.conf.yml (or .aider.conf.yml in a repo)",
        "code": "cat {slug}.aider.conf.yml >> ~/.aider.conf.yml",
        "lang": "sh",
    },
    "detect": ["aider"],
    "notes": "Prompt, reply, tool and completion-menu colors for aider's config file. Code blocks use rich's "
    "ANSI theme, so they follow your Subway Seat terminal, or the Subway Seat Pygments style if you install it. "
    "Append one flavor; to switch, replace the block between the markers, since YAML won't take the keys twice.",
}


def conf(f):
    menu_bg = f.surface0 if f.dark else f.mantle
    ansi = "ansi_dark" if f.dark else "ansi_light"
    return f"""{MARK_START}
# {HEADER}
# {f.name} for aider. Leave dark-mode and light-mode unset: aider applies them
# after this file and they replace these colors and the code theme with its own.
user-input-color: "{f.yellow}"
assistant-output-color: "{f.text}"
tool-output-color: "{f.subtext0}"
tool-error-color: "{f.red_hi}"
tool-warning-color: "{f.orange}"
completion-menu-color: "{f.text}"
completion-menu-bg-color: "{menu_bg}"
# aider swaps the next two: current-color is the highlighted item's background,
# current-bg-color its text. Burnt orange bar, {'crust' if f.dark else 'base'} letters.
completion-menu-current-color: "{f.orange}"
completion-menu-current-bg-color: "{ink(f)}"
# Code blocks in your terminal's colors. For the Subway Seat Pygments style,
# install it into aider's environment and use `code-theme: {f.slug}` instead:
#   uv tool install aider-chat --with "subway-seat-pygments @ {PACKAGE_URL}"
code-theme: {ansi}
{MARK_END}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.aider.conf.yml", conf(f), flavor=f.id, dest="~/.aider.conf.yml", append=True, lang="yaml")
        for f in flavors
    ]
