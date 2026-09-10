#!/bin/sh
# Render the wallpaper SVGs in dist/wallpapers to the PNGs in assets/wallpapers.
#
#   scripts/render-wallpapers.sh            # every flavor, design and size
#   scripts/render-wallpapers.sh stripes    # only names containing "stripes"
#
# Uses resvg or rsvg-convert when one is installed, otherwise headless Chrome or
# Chromium, and oxipng afterwards when it's there. The build itself never needs
# any of this: it only writes the SVGs.
set -eu

root=$(cd "$(dirname "$0")/.." && pwd)
src=$root/dist/wallpapers
out=$root/assets/wallpapers
filter=${1:-}

[ -d "$src" ] || { echo "No $src: run ./build.py --only wallpapers first." >&2; exit 1; }
mkdir -p "$out"

chrome=""
for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
         "/Applications/Chromium.app/Contents/MacOS/Chromium" \
         google-chrome google-chrome-stable chromium chromium-browser; do
  if [ -x "$c" ] || command -v "$c" >/dev/null 2>&1; then chrome=$c; break; fi
done

# Chrome writes the screenshot but doesn't always exit afterwards, so wait for
# the file to stop growing, then stop it.
with_chrome() { # svg png width height
  tmp=$(mktemp -d)
  cat >"$tmp/page.html" <<EOF
<!doctype html><style>html,body{margin:0;overflow:hidden}img{display:block;width:${3}px;height:${4}px}</style><img src="file://$1">
EOF
  rm -f "$2"
  "$chrome" --headless=new --disable-gpu --hide-scrollbars --no-first-run --no-default-browser-check \
    --disable-extensions --use-mock-keychain --user-data-dir="$tmp/profile" --force-device-scale-factor=1 \
    --allow-file-access-from-files --window-size="$3,$4" --screenshot="$2" "file://$tmp/page.html" >/dev/null 2>&1 &
  pid=$! last=-1 i=0 bytes=0
  while [ $i -lt 240 ]; do
    sleep 0.5; i=$((i + 1))
    kill -0 $pid 2>/dev/null || break
    if [ -s "$2" ]; then
      bytes=$(wc -c <"$2")
      [ "$bytes" = "$last" ] && break
      last=$bytes
    fi
  done
  kill $pid 2>/dev/null || true
  wait $pid 2>/dev/null || true
  rm -rf "$tmp"
  [ -s "$2" ]
}

render() { # svg png width height
  if command -v resvg >/dev/null 2>&1; then resvg -w "$3" -h "$4" "$1" "$2"
  elif command -v rsvg-convert >/dev/null 2>&1; then rsvg-convert -w "$3" -h "$4" -o "$2" "$1"
  elif [ -n "$chrome" ]; then with_chrome "$1" "$2" "$3" "$4"
  else echo "Install resvg or rsvg-convert, or Chrome/Chromium." >&2; exit 1
  fi
}

# PNG suffix : SVG suffix : width : height
for spec in "5k:16x9:5120:2880" "4k:16x9:3840:2160" "2560x1600:16x10:2560:1600" "phone:phone:1290:2796"; do
  label=${spec%%:*} rest=${spec#*:}
  aspect=${rest%%:*} rest=${rest#*:}
  w=${rest%%:*} h=${rest#*:}
  for svg in "$src"/*-"$aspect".svg; do
    base=$(basename "$svg" "-$aspect.svg")
    png=$out/$base-$label.png
    case $png in *"$filter"*) ;; *) continue ;; esac
    render "$svg" "$png" "$w" "$h"
    command -v oxipng >/dev/null 2>&1 && oxipng -q -o 4 --strip safe "$png"
    printf '  %s  %s\n' "$(du -h "$png" | cut -f1)" "${png#"$root"/}"
  done
done
