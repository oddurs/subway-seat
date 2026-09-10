"""lsd: colors.yaml with every key lsd 1.2 reads, matching the eza port."""

from ports._lib import HEADER, Out

META = {
    "id": "lsd",
    "name": "lsd",
    "category": "CLI & TUI",
    "homepage": "https://github.com/lsd-rs/lsd",
    "detect": ["lsd"],
    "requires": "lsd 1.1+",
    "enable": {
        "where": "~/.config/lsd/config.yaml",
        "code": "color:\n  theme: custom",
        "lang": "yaml",
    },
    "notes": "The long-view columns in the eza port's colors: gold, orange and avocado permissions, sizes "
    "that warm from avocado to orange as they grow, sage links and git marks in the diff colors. lsd colors "
    "file names from LS_COLORS, so pair it with the vivid port for gold directories. lsd drops the whole "
    "file if it meets a key it doesn't know, so the file sticks to the keys lsd 1.1 and 1.2 read.",
}


def theme(f):
    doc = {
        "user": f.yellow,
        "group": f.subtext1,
        "permission": {
            "read": f.yellow,
            "write": f.orange,
            "exec": f.green,
            "exec-sticky": f.clay,
            "no-access": f.overlay0,
            "octal": f.clay,
            "acl": f.overlay1,
            "context": f.overlay1,
        },
        # Windows file attributes (lsd on Windows shows these instead of permissions)
        "attributes": {
            "archive": f.subtext0,
            "read": f.yellow,
            "hidden": f.overlay1,
            "system": f.clay,
        },
        "date": {
            "hour-old": f.green,
            "day-old": f.subtext1,
            "older": f.subtext0,
        },
        "size": {
            "none": f.overlay1,
            "small": f.green,
            "medium": f.yellow,
            "large": f.orange,
        },
        "inode": {"valid": f.overlay1, "invalid": f.overlay0},
        "links": {"valid": f.sage, "invalid": f.overlay0},
        "tree-edge": f.overlay0,
        "git-status": {
            "default": f.subtext0,
            "unmodified": f.overlay1,
            "ignored": f.overlay0,
            "new-in-index": f.green,
            "new-in-workdir": f.green,
            "typechange": f.clay,
            "deleted": f.red_hi,
            "renamed": f.sage,
            "modified": f.yellow,
            "conflicted": f.red,
        },
    }
    lines = [f"# {HEADER}", f"# {f.name} for lsd. File names follow LS_COLORS (see the vivid port)."]
    for key, value in doc.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            lines += [f'  {k}: "{v}"' for k, v in value.items()]
        else:
            lines.append(f'{key}: "{value}"')
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.slug}/colors.yaml", theme(f), flavor=f.id, dest="~/.config/lsd/colors.yaml", lang="yaml")
        for f in flavors
    ]
