#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "London Moquette" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh london-moquette.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=81c89bbe-7f9d-5629-ac27-a79bdadf3e17
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'London Moquette' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'London Moquette'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#1E2941'"
gsettings set "$PROFILE" foreground-color "'#D8DEEA'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#E9EDF5'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#F2C03F'"
gsettings set "$PROFILE" cursor-foreground-color "'#1E2941'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#3D4F72'"
gsettings set "$PROFILE" highlight-foreground-color "'#E9EDF5'"
gsettings set "$PROFILE" palette "['#303F61', '#DB6052', '#77C581', '#F2C03F', '#7595DA', '#DE8946', '#54B4B5', '#C1C9D8', '#73819C', '#F17869', '#9AD2A0', '#FFD36C', '#8BB0FF', '#E5AA7F', '#72D1D3', '#E9EDF5']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'London Moquette' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh london-moquette.sh --uninstall"
