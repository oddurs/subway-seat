#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "Paris Catacombes" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh paris-catacombes.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=73f55f90-e703-57b3-9fc1-c70eb9363e8a
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'Paris Catacombes' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'Paris Catacombes'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#121E19'"
gsettings set "$PROFILE" foreground-color "'#D4DDD7'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#E7ECEA'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#F2BF4B'"
gsettings set "$PROFILE" cursor-foreground-color "'#121E19'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#31433A'"
gsettings set "$PROFILE" highlight-foreground-color "'#E7ECEA'"
gsettings set "$PROFILE" palette "['#24342C', '#CD6B63', '#80C28E', '#F2BF4B', '#709BC8', '#D0914F', '#6CA087', '#BFC8C2', '#708178', '#E1837A', '#8FD59E', '#FFD273', '#8DB6E2', '#E7AB6D', '#98CCB2', '#E7ECEA']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Paris Catacombes' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh paris-catacombes.sh --uninstall"
