#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "Paris Guimard" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh paris-guimard.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=57507cdc-085d-58f8-95d0-c5df6583ecaf
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'Paris Guimard' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'Paris Guimard'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#0E3125'"
gsettings set "$PROFILE" foreground-color "'#D3E2DB'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#E6F0EB'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#EBC342'"
gsettings set "$PROFILE" cursor-foreground-color "'#0E3125'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#285A47'"
gsettings set "$PROFILE" highlight-foreground-color "'#E6F0EB'"
gsettings set "$PROFILE" palette "['#194A39', '#DA6058', '#73C686', '#EBC342', '#639BD5', '#D78E3C', '#6FB393', '#BBCDC5', '#67897A', '#EF796F', '#82D896', '#FBD664', '#82B7EE', '#EEA85C', '#8ECFAF', '#E6F0EB']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Paris Guimard' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh paris-guimard.sh --uninstall"
