#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "Paris Carrelage" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
# `sh paris-carrelage.sh --uninstall` removes it again (dconf reset on the profile, then drops it from the list).
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=913cbd97-ec50-5946-8e0f-ec3cc0d4a54d
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"
list=$(gsettings get org.gnome.Terminal.ProfilesList list)

if [ "${1-}" = "--uninstall" ]; then
  new=$(printf '%s' "$list" | sed "s/'$UUID'//; s/, ,/,/; s/\[, /[/; s/, \]/]/")
  gsettings set org.gnome.Terminal.ProfilesList list "$new"
  [ "$(gsettings get org.gnome.Terminal.ProfilesList default)" = "'$UUID'" ] && gsettings reset org.gnome.Terminal.ProfilesList default
  dconf reset -f "/org/gnome/terminal/legacy/profiles:/:$UUID/"
  echo "Removed the 'Paris Carrelage' profile."
  exit 0
fi

gsettings set "$PROFILE" visible-name "'Paris Carrelage'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#E7F5ED'"
gsettings set "$PROFILE" foreground-color "'#25352C'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#18231D'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#754500'"
gsettings set "$PROFILE" cursor-foreground-color "'#E7F5ED'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#9FC6B1'"
gsettings set "$PROFILE" highlight-foreground-color "'#18231D'"
gsettings set "$PROFILE" palette "['#374940', '#932D29', '#207F41', '#8A6700', '#27629C', '#754500', '#086142', '#89B19D', '#627F70', '#BB403B', '#168540', '#997300', '#3E75AD', '#AE6800', '#3D8666', '#9FC6B1']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Paris Carrelage' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh paris-carrelage.sh --uninstall"
