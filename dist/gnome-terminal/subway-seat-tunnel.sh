#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Adds the "Subway Seat Tunnel" profile to GNOME Terminal. Safe to re-run: it updates the same profile.
set -eu

command -v gsettings >/dev/null 2>&1 || { echo "gsettings not found; run this inside a GNOME session." >&2; exit 1; }

UUID=29f02fbc-7589-5028-9f48-3b9c9901ee50
PROFILE="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$UUID/"

gsettings set "$PROFILE" visible-name "'Subway Seat Tunnel'"
gsettings set "$PROFILE" use-theme-colors "false"
gsettings set "$PROFILE" background-color "'#24180E'"
gsettings set "$PROFILE" foreground-color "'#E9D8B6'"
gsettings set "$PROFILE" bold-color-same-as-fg "false"
gsettings set "$PROFILE" bold-color "'#F6EAD1'"
gsettings set "$PROFILE" cursor-colors-set "true"
gsettings set "$PROFILE" cursor-background-color "'#F3BF45'"
gsettings set "$PROFILE" cursor-foreground-color "'#24180E'"
gsettings set "$PROFILE" highlight-colors-set "true"
gsettings set "$PROFILE" highlight-background-color "'#4F3927'"
gsettings set "$PROFILE" highlight-foreground-color "'#F6EAD1'"
gsettings set "$PROFILE" palette "['#3D2C1D', '#D2503A', '#A3AE4B', '#F3BF45', '#7F9BAE', '#EC7F31', '#86AD95', '#D6C3A0', '#6A523C', '#EC6A50', '#BFCB63', '#FFD36B', '#9DB6C6', '#FF9D55', '#A5C9B0', '#F6EAD1']"

list=$(gsettings get org.gnome.Terminal.ProfilesList list)
case "$list" in
  *"$UUID"*) ;;
  "@as []" | "[]") gsettings set org.gnome.Terminal.ProfilesList list "['$UUID']" ;;
  *) gsettings set org.gnome.Terminal.ProfilesList list "${list%]}, '$UUID']" ;;
esac

echo "Added the 'Subway Seat Tunnel' profile. To make it the default:"
echo "  gsettings set org.gnome.Terminal.ProfilesList default '$UUID'"
