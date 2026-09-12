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
gsettings set "$PROFILE" background-color "'#EEF2F1'"
gsettings set "$PROFILE" foreground-color "'#27342F'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#19221E'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#764C00'"
gsettings set "$PROFILE" cursor-foreground-color "'#EEF2F1'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#B0BFBB'"
gsettings set "$PROFILE" highlight-foreground-color "'#19221E'"
gsettings set "$PROFILE" palette "['#3B4742', '#88251E', '#218366', '#916D07', '#25629B', '#764C00', '#006267', '#99ABA6', '#6C7C76', '#AC3B32', '#278D6E', '#A07A12', '#3D75AD', '#885A00', '#027479', '#B0BFBB']"

case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Paris Carrelage' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
echo "To remove it later:"
echo "  sh paris-carrelage.sh --uninstall"
