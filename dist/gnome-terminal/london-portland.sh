#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "London Portland" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh london-portland.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=15baa349-e295-5b3d-af0b-14d8196d293c
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'London Portland' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'London Portland'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#E5EAF6'"
gsettings set "$PROFILE" foreground-color "'#2F3033'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#1F2022'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#9F591B'"
gsettings set "$PROFILE" cursor-foreground-color "'#E5EAF6'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#ADB7CB'"
gsettings set "$PROFILE" highlight-foreground-color "'#1F2022'"
gsettings set "$PROFILE" palette "['#434548', '#A40005', '#357D41', '#896800', '#0019A8', '#9F591B', '#007376', '#9BA5B8', '#727781', '#CA2822', '#398145', '#977300', '#406BD0', '#AE672B', '#008689', '#ADB7CB']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'London Portland' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh london-portland.sh --uninstall"
