#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
#
# Merges Subway Seat into Claude Code's user settings, or takes it out again.
#   setup.sh check
#   setup.sh apply --flavor walnut|tunnel|enamel --verbs replace|append --voice yes|no --data DIR [--dry-run]
#   setup.sh remove [--dry-run]
# Each key it writes is replaced whole, and every other key is kept. The first
# real write keeps a backup next to settings.json.
set -u

root=$(cd "$(dirname "$0")/.." && pwd)
dir=${CLAUDE_CONFIG_DIR:-$HOME/.claude}
s="$dir/settings.json"
FLOOR=2.1.247
# The keys Subway Seat may own, and how to tell a value is ours.
KEYS='["theme","statusLine","subagentStatusLine","spinnerVerbs","spinnerTipsOverride","outputStyle"]'
OURS='def ours: (tostring | test("subway-seat|Subway Seat")) or ((.verbs? // []) | index("Changing at 14th Street") != null);'

die() { printf 'Subway Seat: %s\nNothing was changed.\n' "$1"; exit 1; }

command -v jq >/dev/null 2>&1 ||
  die "setup needs jq (brew install jq, apt install jq, or winget install jqlang.jq)."
if [ -f "$s" ] && ! jq -e 'type == "object"' "$s" >/dev/null 2>&1; then
  die "$s isn't a JSON object. Fix it first."
fi

action=${1:-}
[ $# -gt 0 ] && shift
flavor='' verbs=replace voice=no data='' dry=''
while [ $# -gt 0 ]; do
  case $1 in
    --flavor) flavor=${2:-} && shift 2 ;;
    --verbs) verbs=${2:-} && shift 2 ;;
    --voice) voice=${2:-} && shift 2 ;;
    --data) data=${2:-} && shift 2 ;;
    --dry-run) dry=1 && shift ;;
    *) die "unknown option $1" ;;
  esac
done

current() { if [ -f "$s" ]; then cat "$s"; else printf '{}\n'; fi; }

changes() { # $1 = new keys; prints the old and new value of each key that changes
  current | jq -r --argjson new "$1" "$OURS"'
    def v: if . == null then "(not set)"
      elif type == "object" and has("verbs") then "\(.mode), \(.verbs | length) verbs"
      else tojson | split(env.HOME // "\u0000") | join("~") | if length > 160 then .[0:157] + "..." else . end end;
    . as $cur
    | ($new | to_entries[] | select($cur[.key] != .value)
       | "\(.key)\n  now: \($cur[.key] | v)\n  new: \(.value | v)"),
      (select($cur.subagentStatusLine != null and ($cur.subagentStatusLine | ours))
       | "subagentStatusLine\n  now: \($cur.subagentStatusLine | v)\n  new: (not set; the plugin supplies it)")'
}

write() { # $1 = jq filter, then its jq options. Writes through a symlink, keeps the mode.
  local fresh='' tmp
  mkdir -p "$dir" || die "can't create $dir."
  if [ ! -f "$s" ]; then printf '{}\n' >"$s" || die "can't create $s."; fresh=1; fi
  if [ -z "$fresh" ] && [ ! -e "$s.subway-seat.bak" ]; then cp "$s" "$s.subway-seat.bak" || die "can't back up $s."; fi
  tmp=$(mktemp "$s.XXXXXX") || die "can't write next to $s."
  if jq "${@:2}" "$OURS $1" "$s" >"$tmp" && cat "$tmp" >"$s"; then
    rm -f "$tmp"
  else
    rm -f "$tmp"
    die "couldn't update $s."
  fi
}

notes() {
  local v f copies=''
  v=$(claude --version 2>/dev/null | awk '{print $1}')
  if [ -n "$v" ] && [ "$(printf '%s\n%s\n' "$FLOOR" "$v" | sort -t. -k1,1n -k2,2n -k3,3n | head -n 1)" != "$FLOOR" ]; then
    printf 'Note: the tips label and file need Claude Code %s or later, and this is %s. Run claude update.\n' "$FLOOR" "$v"
  fi
  for f in "$dir"/themes/subway-seat*.json; do [ -f "$f" ] && copies="$copies  $f\n"; done
  if [ -n "$copies" ]; then
    printf 'Note: %s has its own Subway Seat theme files too, so /theme lists each flavor twice.\n' "$dir/themes"
    printf 'Delete these to keep only the plugin'"'"'s:\n%b' "$copies"
  fi
  if [ -d "$dir/subway-seat" ]; then
    printf 'Note: nothing uses %s any more (it held copies from an older setup); you can delete it.\n' "$dir/subway-seat"
  fi
}

case $action in
  check)
    printf 'Settings: %s%s\n' "$s" "$([ -f "$s" ] || printf ' (not created yet)')"
    current | jq -r --argjson keys "$KEYS" '. as $c | $keys[] | "  \(.): \($c[.] // "(not set)" | tostring | .[0:100])"'
    notes
    exit 0
    ;;
  apply)
    case $flavor in
      walnut) slug=subway-seat ;; tunnel) slug=subway-seat-tunnel ;; enamel) slug=subway-seat-enamel ;;
      *) die "--flavor must be walnut, tunnel or enamel." ;;
    esac
    case $verbs in replace | append) ;; *) die "--verbs must be replace or append." ;; esac
    case $voice in yes | no) ;; *) die "--voice must be yes or no." ;; esac
    [ -n "$data" ] || data="$dir/plugins/data/subway-seat-subway-seat"
    new=$(jq --arg cmd "$(printf '%q' "$data/subway-seat-statusline")" --arg data "$data" \
      --arg verbs "$verbs" --arg voice "$voice" '
      .statusLine.command = $cmd
      | .spinnerTipsOverride.tipsFile = ($data + "/tips.json")
      | .spinnerVerbs.mode = $verbs
      | if $voice == "yes" then .outputStyle = "subway-seat:Subway Seat" else . end' "$root/settings/$slug.json") ||
      die "can't read $root/settings/$slug.json."
    list=$(changes "$new")
    if [ -z "$list" ]; then
      printf 'Already set up (%s). Nothing to change.\n' "$slug"
      exit 0
    fi
    printf 'In %s:\n%s\n' "$s" "$list"
    if [ -n "$dry" ]; then notes; exit 0; fi
    "$root/scripts/sync.sh" "$root" "$data"
    # an older setup's subagentStatusLine would hide the plugin's own
    # shellcheck disable=SC2016 # a jq filter
    write '(if (.subagentStatusLine // null) != null and (.subagentStatusLine | ours) then del(.subagentStatusLine) else . end) + $new' \
      --argjson new "$new"
    ;;
  remove)
    gone=$(current | jq -r --argjson keys "$KEYS" "$OURS"' . as $c | $keys[] | select($c[.] != null and ($c[.] | ours))')
    if [ -z "$gone" ]; then
      printf 'No Subway Seat settings in %s. Nothing to remove.\n' "$s"
      exit 0
    fi
    printf 'From %s, remove:\n' "$s"
    printf '%s\n' "$gone" | sed 's/^/  /'
    [ -n "$dry" ] && exit 0
    # shellcheck disable=SC2016 # a jq filter
    write 'reduce $keys[] as $k (.; if .[$k] != null and (.[$k] | ours) then del(.[$k]) else . end)' --argjson keys "$KEYS"
    ;;
  *)
    die "usage: setup.sh check | apply --flavor F --verbs replace|append --voice yes|no --data DIR [--dry-run] | remove [--dry-run]"
    ;;
esac

printf 'Done.'
[ -e "$s.subway-seat.bak" ] && printf ' Your settings from before the first run are in %s.' "$s.subway-seat.bak"
printf '\n'
[ "$action" = apply ] && notes
exit 0
