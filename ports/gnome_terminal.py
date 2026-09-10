"""GNOME Terminal: a POSIX sh script per flavor that adds (or updates) a profile via gsettings."""

import uuid

from ports._lib import HEADER, REPO, Out
from ports._terminals import lit, selection

META = {
    "id": "gnome-terminal",
    "name": "GNOME Terminal",
    "category": "Terminals",
    "homepage": "https://help.gnome.org/users/gnome-terminal/stable/",
    "enable": {
        "where": "any shell in your GNOME session",
        "code": "sh {slug}.sh   # adds the “{name}” profile; pick it in Preferences",
        "lang": "sh",
    },
    "notes": "Adds a profile with the palette, cursor, selection and bold colors. Re-running the script "
    "updates the same profile in place. Ptyxis, GNOME's newer terminal, is not covered.",
}


def profile_id(f):
    # Stable per flavor, so re-running updates the profile instead of adding another.
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{REPO}#gnome-terminal/{f.slug}"))


def script(f):
    uid = profile_id(f)
    palette = "[" + ", ".join(f"'{c}'" for c in f.ansi) + "]"
    keys = [
        ("visible-name", f"'{f.name}'"),
        ("use-theme-colors", "false"),
        ("background-color", f"'{f.base}'"),
        ("foreground-color", f"'{f.text}'"),
        ("bold-color-same-as-fg", "false"),
        ("bold-color", f"'{f.text_hi}'"),
        ("cursor-colors-set", "true"),
        ("cursor-background-color", f"'{lit(f)}'"),
        ("cursor-foreground-color", f"'{f.base}'"),
        ("highlight-colors-set", "true"),
        ("highlight-background-color", f"'{selection(f)}'"),
        ("highlight-foreground-color", f"'{f.text_hi}'"),
        ("palette", palette),
    ]
    sets = "\n".join(f'gsettings set "$PROFILE" {k} "{v}"' for k, v in keys)
    return f"""#!/bin/sh
# {HEADER}
# Adds the "{f.name}" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
set -eu

command -v gsettings >/dev/null 2>&1 || {{ echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }}

UUID={uid}
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"

{sets}

list=$(gsettings get org.gnome.Terminal.ProfilesList list)
case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${{list%]}}, '$UUID']" ;;
esac

echo "Added the '{f.name}' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
"""


def build(flavors):
    return [
        Out(f"{f.slug}.sh", script(f), flavor=f.id, dest=f"anywhere; run once with `sh {f.slug}.sh`", lang="sh")
        for f in flavors
    ]
