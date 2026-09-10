"""Aider: colour settings for .aider.conf.yml, one snippet per flavor.

Two aider quirks shape the file (aider/io.py, aider/main.py):
- `completion-menu-current-color` paints the highlighted item's *background* and
  `completion-menu-current-bg-color` its *text*, the reverse of their names.
- `dark-mode` / `light-mode` are applied after the config file and overwrite the
  prompt, reply, error, warning and code-theme colours, so the snippet leaves them off.

Code blocks use the Subway Seat Pygments style by name, which the Pygments
port's `package/` registers once it's installed into aider's environment.
"""

from ports._lib import HEADER, Out
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
    "notes": "Prompt, reply, tool and completion-menu colours for aider's config file. Code blocks use "
    "rich's ANSI theme, so they follow your Subway Seat terminal.",
}


def conf(f):
    ink = f.crust if f.dark else f.base
    menu_bg = f.surface0 if f.dark else f.mantle
    return f"""# {HEADER}
# {f.name} for aider. Leave dark-mode and light-mode unset: aider applies them
# after this file and they replace these colours and the code theme with its own.
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
completion-menu-current-bg-color: "{ink}"
# needs the style in aider's environment:
#   uv tool install aider-chat --with "subway-seat-pygments @ {PACKAGE_URL}"
# (without it, use ansi_dark / ansi_light to take your terminal's colours)
code-theme: {f.slug}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.aider.conf.yml", conf(f), flavor=f.id, dest="~/.aider.conf.yml", append=True, lang="yaml")
        for f in flavors
    ]
