from ports._cli import row
from ports._lib import HEADER, Out, ink

META = {
    "id": "gh-dash",
    "name": "gh-dash",
    "category": "CLI & TUI",
    "homepage": "https://github.com/dlvhdr/gh-dash",
    "enable": {
        "where": "~/.config/gh-dash/config.yml (on releases before 4.25, paste the theme block in instead)",
        "code": "include:\n  - ~/.config/gh-dash/{slug}.yml",
        "lang": "yaml",
    },
    "requires": "gh-dash 4.25+ for `include`",
    "detect": ["gh-dash", "~/.local/share/gh/extensions/gh-dash"],
    "notes": "Parchment text, orange borders on the active section and a warm selected row, with "
    "author-role icons in the palette's accents. gh-dash shows PR diffs through its pager, so set "
    "`pager: {diff: delta}` in the same config to see them with the delta port.",
}


def theme(f):
    return f"""# {HEADER}
# {f.name} for gh-dash.
theme:
  colors:
    text:
      primary: "{f.text}"
      secondary: "{f.orange}"
      inverted: "{ink(f)}"
      faint: "{f.overlay1}"
      warning: "{f.yellow}"
      success: "{f.green}"
      error: "{f.red_hi}"
      actor: "{f.subtext1}"
    background:
      selected: "{row(f)}"
    border:
      primary: "{f.orange}"
      secondary: "{f.surface2}"
      faint: "{f.surface0}"
    icon:
      newcontributor: "{f.green}"
      contributor: "{f.sage}"
      collaborator: "{f.yellow}"
      member: "{f.yellow}"
      owner: "{f.orange}"
      unknownrole: "{f.overlay1}"
"""


def build(flavors):
    return [
        Out(f"{f.slug}.yml", theme(f), flavor=f.id, dest=f"~/.config/gh-dash/{f.slug}.yml", lang="yaml")
        for f in flavors
    ]
