#!/bin/sh
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
#
# Copies the status line scripts and tips into the plugin's data folder, which
# keeps its path across plugin updates. Runs at session start; prints nothing,
# since whatever a SessionStart hook prints goes into Claude's context.
root=$1 data=$2
[ -n "$root" ] && [ -n "$data" ] || exit 0
mkdir -p "$data" 2>/dev/null || exit 0
for name in subway-seat-statusline subway-seat-subagents tips.json; do
  src="$root/scripts/$name"
  [ "$name" = tips.json ] && src="$root/tips.json"
  [ -f "$src" ] || continue
  cmp -s "$src" "$data/$name" 2>/dev/null && continue
  rm -f "$data/$name" && cp "$src" "$data/$name" 2>/dev/null
done
chmod +x "$data"/subway-seat-statusline "$data"/subway-seat-subagents 2>/dev/null
exit 0
