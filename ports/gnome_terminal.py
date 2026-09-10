"""GNOME Terminal: a POSIX sh script per flavor that adds (or updates) a profile via gsettings."""

import uuid

from ports._lib import HEADER, REPO, Out, selection
from ports._terminals import lit

META = {
    "id": "gnome-terminal",
    "name": "GNOME Terminal",
    "category": "Terminals",
    "homepage": "https://help.gnome.org/gnome-terminal/",
    "detect": ["gnome-terminal"],
    "enable": {
        "where": "any shell in your GNOME session",
        "code": "sh {slug}.sh   # adds the “{name}” profile; pick it in Preferences",
        "lang": "sh",
    },
    "notes": "Adds a profile with the palette, cursor, selection and bold colors. Re-running the script "
    "updates the same profile in place, and `sh <script> --uninstall` removes it. Profiles don't switch with "
    "the system style, so pick one flavor. Ptyxis, GNOME's newer terminal, is not covered.",
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
# `sh {f.slug}.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || {{ echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }}

UUID={uid}
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${{1-}}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\\[, /[/; s/, \\]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the '{f.name}' profile."
  exit 0
fi

{sets}

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${{list%]}}, '$UUID']" ;;
esac

echo "Added the '{f.name}' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh {f.slug}.sh --uninstall"
"""


def build(flavors):
    return [
        Out(
            f"{f.slug}.sh",
            script(f),
            flavor=f.id,
            lang="sh",
            how=f"Run once with `sh {f.slug}.sh`; it adds the profile through gsettings",
        )
        for f in flavors
    ]
