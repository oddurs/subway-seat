#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "Subway Seat Enamel" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh subway-seat-enamel.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=1c4ed141-59b8-52e3-83d2-6ca516e24de0
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'Subway Seat Enamel' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'Subway Seat Enamel'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#F4E9D4'"
gsettings set "$PROFILE" foreground-color "'#3E2C1E'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#2A1D13'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#AD4E00'"
gsettings set "$PROFILE" cursor-foreground-color "'#F4E9D4'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#CAB48E'"
gsettings set "$PROFILE" highlight-foreground-color "'#2A1D13'"
gsettings set "$PROFILE" palette "['#54402F', '#992418', '#66740F', '#936200', '#3F6480', '#AD4E00', '#3E7157', '#BAA07A', '#8C7254', '#BC4031', '#697813', '#A56E00', '#517791', '#C4561A', '#4C8367', '#CAB48E']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Subway Seat Enamel' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh subway-seat-enamel.sh --uninstall"
