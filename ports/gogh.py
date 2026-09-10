import json

from ports._lib import HEADER, REPO, Out

META = {
    "id": "gogh",
    "name": "Gogh",
    "category": "Palettes",
    "homepage": "https://github.com/Gogh-Co/Gogh",
    "enable": {
        "where": "a terminal, in the folder that holds installs/",
        "code": "curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh\n"
        "bash installs/{slug}.sh\n"
        "# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one",
        "lang": "sh",
    },
    "notes": "Gogh themes: the 16 ANSI colors, background, foreground and cursor. installs/ has Gogh's install "
    "script for each flavor, which applies it to GNOME Terminal, Tilix, Xfce Terminal, Konsole, Alacritty and "
    "the other terminals Gogh supports (set TERMINAL). The YAML is Gogh's theme source and the JSON matches its "
    "data/json files.",
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
    lines = [f"color_{i + 1:02d}: '{c}'    # {label}" for i, (c, label) in enumerate(zip(f.ansi, LABELS, strict=True))]
    colors = "\n".join(lines[:8]) + "\n\n" + "\n".join(lines[8:])
    return (
        f"---\n# {HEADER}\nname: '{t['name']}'\nauthor: '{t['author']}'\nauthor_name: '{AUTHOR_NAME}'\n"
        f"author_url: '{REPO}'\nvariant: '{t['variant']}'\n\n{colors}\n\n"
        f"background: '{t['background']}'  # Background\nforeground: '{t['foreground']}'  # Foreground (Text)\n\n"
        f"cursor: '{t['cursor']}'      # Cursor\n"
    )


def install_script(f):
    """Gogh's installs/<theme>.sh: its generator's template (tools/generate/07_generate_install_scripts.py)
    with our header. The file name is Gogh's slug of the theme name, which is the flavor's slug."""
    colors = [f'export COLOR_{i + 1:02d}="{c}"           # {label}' for i, (c, label) in enumerate(zip(f.ansi, LABELS, strict=True))]
    t = theme(f)
    return f"""#!/usr/bin/env bash
# {HEADER}

export PROFILE_NAME="{f.name}"

{chr(10).join(colors[:8])}

{chr(10).join(colors[8:])}

export BACKGROUND_COLOR="{t['background']}"   # Background
export FOREGROUND_COLOR="{t['foreground']}"   # Foreground (Text)

export CURSOR_COLOR="{t['cursor']}" # Cursor

apply_theme() {{
    if [[ -e "${{GOGH_APPLY_SCRIPT}}" ]]; then
      bash "${{GOGH_APPLY_SCRIPT}}"
    elif [[ -e "${{PARENT_PATH}}/apply-colors.sh" ]]; then
      bash "${{PARENT_PATH}}/apply-colors.sh"
    elif [[ -e "${{SCRIPT_PATH}}/apply-colors.sh" ]]; then
      bash "${{SCRIPT_PATH}}/apply-colors.sh"
    else
      printf '\\n%s\\n' "Error: Couldn't find apply-colors.sh" 1>&2
      exit 1
    fi
}}

# | ===========================================================================
# | Apply Colors
# | ===========================================================================
SCRIPT_PATH="${{SCRIPT_PATH:-$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)}}"
PARENT_PATH="$(dirname "${{SCRIPT_PATH}}")"

if [ -z "${{GOGH_NONINTERACTIVE+no}}" ]; then
    apply_theme
else
    apply_theme 1>/dev/null
fi
"""


def build(flavors):
    outs = []
    for f in flavors:
        outs.append(Out(f"installs/{f.slug}.sh", install_script(f), flavor=f.id, lang="sh",
                        how="run it with Gogh's apply-colors.sh in the folder above it (or beside it); "
                        "TERMINAL=… picks the terminal"))
        outs.append(Out(f"{f.name}.yml", yml(f), flavor=f.id, lang="yaml",
                        how="Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name)"))
        outs.append(Out(f"{f.slug}.json", json.dumps(theme(f), indent=2) + "\n", flavor=f.id, lang="json",
                        how="the same theme in the form of Gogh's data/json files"))
    return outs
