import json

from ports._lib import HEADER, REPO, Out

META = {
    "id": "gogh",
    "name": "Gogh",
    "category": "Palettes",
    "homepage": "https://github.com/Gogh-Co/Gogh",
    "enable": {
        "where": "a Gogh checkout: the YAML is its theme source (the file name must match the name)",
        "code": 'cp "{name}.yml" Gogh/themes/\ncd Gogh && task validate',
        "lang": "sh",
    },
    "notes": "Gogh themes: the 16 ANSI colors, background, foreground and cursor. "
    "The YAML is what Gogh's themes/ folder takes; the JSON matches its generated data/json files.",
}

AUTHOR_NAME = "oddurs"
# Gogh's own labels for the 16 slots.
LABELS = [
    "Black (Host)", "Red (Syntax string)", "Green (Command)", "Yellow (Command second)",
    "Blue (Path)", "Magenta (Syntax var)", "Cyan (Prompt)", "White",
    "Bright Black", "Bright Red (Command error)", "Bright Green (Exec)", "Bright Yellow",
    "Bright Blue (Folder)", "Bright Magenta", "Bright Cyan", "Bright White",
]


def theme(f):
    return {
        "name": f.name,
        "author": f"{AUTHOR_NAME} ({REPO})",
        "author_name": AUTHOR_NAME,
        "author_url": REPO,
        "variant": "dark" if f.dark else "light",
        **{f"color_{i + 1:02d}": c for i, c in enumerate(f.ansi)},
        "background": f.base,
        "foreground": f.text,
        "cursor": f.yellow if f.dark else f.orange,
    }


def yml(f):
    t = theme(f)
    lines = [f"color_{i + 1:02d}: '{c}'    # {label}" for i, (c, label) in enumerate(zip(f.ansi, LABELS))]
    colors = "\n".join(lines[:8]) + "\n\n" + "\n".join(lines[8:])
    return (
        f"---\n# {HEADER}\nname: '{t['name']}'\nauthor: '{t['author']}'\nauthor_name: '{AUTHOR_NAME}'\n"
        f"author_url: '{REPO}'\nvariant: '{t['variant']}'\n\n{colors}\n\n"
        f"background: '{t['background']}'  # Background\nforeground: '{t['foreground']}'  # Foreground (Text)\n\n"
        f"cursor: '{t['cursor']}'      # Cursor\n"
    )


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(Out(f"{f.name}.yml", yml(f), flavor=f.id, dest=f"Gogh/themes/{f.name}.yml", lang="yaml"))
        outs.append(Out(f"{f.slug}.json", json.dumps(theme(f), indent=2) + "\n", flavor=f.id,
                        dest=f"Gogh/data/json/{f.slug}.json", lang="json"))
    return outs
