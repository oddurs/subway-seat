import palette as p
from ports._cli import ink
from ports._lib import HEADER, Out, h

META = {
    "id": "vivid",
    "name": "vivid",
    "category": "CLI & TUI",
    "homepage": "https://github.com/sharkdp/vivid",
    "enable": {
        "where": "config.fish, after copying the theme to ~/.config/vivid/themes/",
        "code": "set -gx LS_COLORS (vivid generate {slug})",
        "lang": "fish",
    },
    "notes": "LS_COLORS for ls, fd, eza and friends: gold directories instead of blue, avocado "
    "executables, sage symlinks, terracotta media and red archives.",
}


def theme(f):
    colors = "\n".join(f"  {r}: '{h(f.colors[r])}'" for r in p.ROLES)
    colors += f"\n  ink: '{h(ink(f))}'"
    return f"""# {HEADER}
# {f.name} for vivid.
colors:
{colors}

core:
  normal_text: {{}}
  regular_file: {{}}
  reset_to_normal: {{}}

  directory:
    foreground: yellow
    font-style: bold

  symlink:
    foreground: sage

  multi_hard_link: {{}}

  fifo:
    foreground: clay

  socket:
    foreground: clay
    font-style: bold

  door:
    foreground: clay

  block_device:
    foreground: orange_hi
    background: surface0

  character_device:
    foreground: orange
    background: surface0

  broken_symlink:
    foreground: ink
    background: red

  missing_symlink_target:
    foreground: ink
    background: red

  setuid:
    foreground: ink
    background: red

  setgid:
    foreground: ink
    background: yellow

  file_with_capability:
    foreground: clay
    font-style: underline

  sticky_other_writable:
    foreground: yellow
    background: surface1

  other_writable:
    foreground: yellow
    background: surface1

  sticky:
    foreground: yellow
    background: surface0

  executable_file:
    foreground: green
    font-style: bold

text:
  special:
    foreground: yellow_hi
    font-style: bold

  todo:
    font-style: bold

  licenses:
    foreground: overlay1

  configuration:
    foreground: subtext0

  other:
    foreground: subtext1

markup:
  foreground: orange

programming:
  source:
    foreground: sage

  tooling:
    foreground: yellow

    continuous-integration:
      foreground: yellow

media:
  foreground: clay

  audio:
    foreground: orange_hi

  video:
    foreground: orange

  fonts:
    foreground: subtext0

office:
  foreground: denim

archives:
  foreground: red_hi

executable:
  foreground: green
  font-style: bold

unimportant:
  foreground: overlay0
"""


def build(flavors):
    return [
        Out(f"{f.slug}.yml", theme(f), flavor=f.id, dest=f"~/.config/vivid/themes/{f.slug}.yml", lang="yaml")
        for f in flavors
    ]
