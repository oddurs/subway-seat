"""Claude Code: themes, a station-sign status line, subagent rows, spinner verbs
and tips, a relaxed output style, and a plugin that bundles all of it.

How Claude Code draws a custom theme (checked against the v2.1.26x binary):

- `overrides` replace any token the base preset has, so every one of the 72 is set
  here, including the ten single-purpose accents the docs' table leaves out.
- Diffs take only their grounds from the theme (`diffAdded`, `diffRemoved`, the
  `…Dimmed` pair for faded hunks, the `…Word` pair for changed words). The code on
  top keeps Claude Code's own colors: Monokai Extended over a `dark` base, GitHub
  over `light`, the +/- signs in its fixed green and red, and removed lines in
  plain text. So the grounds are `_lib.tints`, which keep those fixed colors
  readable (better than the stock themes do).
- Inline `code` in messages is drawn from the base preset's `permission` color, not
  from the overrides, so it stays Claude Code's lavender or blue.
"""

import json

from ports._lib import HEADER, REPO, SITE, VERSION, Out, ink, rgb, selection, tints

META = {
    "id": "claude-code",
    "name": "Claude Code",
    "category": "Agents",
    "homepage": "https://claude.com/product/claude-code",
    "enable": {
        "where": "Claude Code, from the Subway Seat marketplace",
        "code": "/plugin marketplace add oddurs/subway-seat\n/plugin install subway-seat@subway-seat\n/subway-seat:setup",
        "lang": "text",
    },
    "requires": "Claude Code 2.1.247+",
    "detect": ["claude", "~/.claude"],
    "notes": "One plugin: all three themes, a relaxed output style and subagent rows. `/subway-seat:setup` "
    "asks for a flavor, shows what it will change, then adds the station-sign status line, 70s spinner verbs "
    "and “Next stop” tips to your settings; `/subway-seat:setup remove` takes them out again. "
    "Inside tmux, Claude Code rounds colors to 256 unless `CLAUDE_CODE_TMUX_TRUECOLOR=1` is set.",
}

PLUGIN = "subway-seat"
OUTPUT_STYLE_NAME = f"{PLUGIN}:Subway Seat"  # plugin output styles are named "<plugin>:<name>"


def theme(f):
    c = f
    t = tints(f)
    dark = f.dark
    # a shimmer is the lighter partner of its color
    clay_shimmer = f.mix("clay", "text_hi", 0.7) if dark else f.mix("clay", "base", 0.8)
    overrides = {
        "claude": c.orange, "claudeShimmer": c.orange_hi,
        "claudeBlue_FOR_SYSTEM_SPINNER": c.denim, "claudeBlueShimmer_FOR_SYSTEM_SPINNER": c.denim_hi,
        "text": c.text, "inverseText": ink(f),
        "inactive": c.overlay2, "inactiveShimmer": c.subtext0 if dark else c.overlay1,
        "subtle": c.overlay0 if dark else c.surface2,
        "suggestion": c.yellow,
        "permission": c.yellow, "permissionShimmer": c.yellow_hi,
        "remember": c.sage,
        "background": c.sage,
        "success": c.green, "error": c.red_hi,
        "warning": c.yellow, "warningShimmer": c.yellow_hi,
        "merged": c.clay,
        "promptBorder": c.overlay0, "promptBorderShimmer": c.overlay1 if dark else c.surface2,
        "planMode": c.sage, "autoAccept": c.clay, "autoAcceptShimmer": clay_shimmer,
        "skill": c.clay, "bashBorder": c.yellow,
        "ide": c.denim, "professionalBlue": c.denim, "chromeYellow": c.yellow,
        "fastMode": c.orange_hi, "fastModeShimmer": c.yellow_hi,
        "effortUltra": c.yellow_hi,
        "diffAdded": t["add"], "diffRemoved": t["del"],
        "diffAddedDimmed": t["add_dim"], "diffRemovedDimmed": t["del_dim"],
        "diffAddedWord": t["add_emph"], "diffRemovedWord": t["del_emph"],
        "userMessageBackground": c.surface0 if dark else c.mantle,
        "userMessageBackgroundHover": c.surface1 if dark else c.crust,
        "bashMessageBackgroundColor": f.mix("yellow", "base", 0.1),
        "memoryBackgroundColor": f.mix("sage", "base", 0.12),
        "composerSidebarBackground": c.mantle,
        "selectionBg": selection(f),
        "rate_limit_fill": c.orange, "rate_limit_empty": c.surface1,
        "briefLabelYou": c.yellow, "briefLabelClaude": c.orange,
        "clawd_body": c.orange, "clawd_background": c.crust if dark else c.text_hi,
        "red_FOR_SUBAGENTS_ONLY": c.red_hi, "blue_FOR_SUBAGENTS_ONLY": c.denim,
        "green_FOR_SUBAGENTS_ONLY": c.green, "yellow_FOR_SUBAGENTS_ONLY": c.yellow,
        # a dusty mauve, so "purple" isn't a second denim
        "purple_FOR_SUBAGENTS_ONLY": f.mix("red_hi", "denim_hi", 0.5), "orange_FOR_SUBAGENTS_ONLY": c.orange,
        "pink_FOR_SUBAGENTS_ONLY": c.clay, "cyan_FOR_SUBAGENTS_ONLY": c.sage,
        # ultrathink's rainbow, as a 70s stripe
        "rainbow_red": c.red, "rainbow_orange": c.orange, "rainbow_yellow": c.yellow,
        "rainbow_green": c.green, "rainbow_blue": c.sage, "rainbow_indigo": c.denim,
        "rainbow_violet": c.clay,
        "rainbow_red_shimmer": c.red_hi, "rainbow_orange_shimmer": c.orange_hi,
        "rainbow_yellow_shimmer": c.yellow_hi, "rainbow_green_shimmer": c.green_hi,
        "rainbow_blue_shimmer": c.sage_hi, "rainbow_indigo_shimmer": c.denim_hi,
        "rainbow_violet_shimmer": clay_shimmer,
    }
    return {"name": f.name, "base": "dark" if dark else "light", "overrides": overrides}


# ── Spinner verbs and tips ─────────────────────────────────────────────────
VERBS = [
    "Reading the Vignelli map", "Riding the local", "Running express", "Transferring", "Holding the doors",
    "Watching the gap", "Waiting on the platform", "Rolling uptown", "Rolling downtown",
    "Changing at 14th Street", "Dropping a token", "Grabbing the pole", "Finding a seat",
    "Sinking into the shag", "Flipping the record", "Warming up the hi-fi", "Tuning the 8-track",
    "Adjusting the rabbit ears", "Watering the spider plant", "Percolating", "Taking the A train",
    "Keeping it groovy", "Easing on down the road", "Digging it", "Grooving", "Punching a transfer",
    "Checking the strip map", "Spinning the lazy Susan", "Knotting the macramé", "Lava-lamping",
]

TIPS = [
    ("clear", "/clear gives you a fresh car. Stand clear of the closing doors."),
    ("compact", "Car getting crowded? /compact squeezes the conversation down so there's room to stretch."),
    ("context", "/context shows how crowded the car is."),
    ("resume", "/resume picks up a ride you left earlier, right where you got off."),
    ("modes", "Shift+Tab changes how you ride: plan the trip first, or let edits through on their own."),
    ("esc", "Esc stops Claude mid-turn. No emergency brake required."),
    ("rewind", "With an empty prompt, Esc twice rewinds the line to an earlier stop."),
    ("bang", "Start a message with ! to run a shell command without leaving your seat."),
    ("at", "@ a file to bring it along for the ride."),
    ("btw", "/btw asks a quick side question without adding it to the ride."),
    ("claude-md", "Put the house rules in CLAUDE.md so every ride starts on the right line."),
    ("theme", "/theme swaps between Subway Seat, Tunnel and Enamel. Same seats, different light."),
    ("model", "/model switches trains. Opus for the long haul, Haiku for a hop."),
    ("usage", "/usage shows the fare so far and how much of your pass is left."),
    ("slow", "No rush. The next train is always right behind this one."),
]


def tips_json():
    return json.dumps(
        {"tips": [{"id": f"subway-seat.{i}", "text": text, "cooldownSessions": 2} for i, text in TIPS]},
        indent=2,
    ) + "\n"


DATA = "${CLAUDE_PLUGIN_DATA}"  # setup.sh swaps in the plugin's data folder


def settings(f):
    """What /subway-seat:setup merges into the user's settings (each key whole)."""
    return {
        "theme": f"custom:{PLUGIN}:{f.slug}",
        "statusLine": {
            "type": "command", "command": f"{DATA}/subway-seat-statusline", "padding": 0,
            "hideVimModeIndicator": True,
        },
        "spinnerVerbs": {"mode": "replace", "verbs": VERBS},
        "spinnerTipsOverride": {"tipsFile": f"{DATA}/tips.json", "label": "Next stop"},
    }


# ── Status line scripts (bash + jq) ────────────────────────────────────────
def triplet(color):
    return ";".join(str(v) for v in rgb(color))


def roles(f):
    return {
        "INK": ink(f), "TEXT": f.text, "SUB": f.subtext1, "DIM": f.overlay2, "FAINT": f.overlay1,
        "RAIL": f.surface2, "ORANGE": f.orange, "YELLOW": f.yellow, "GREEN": f.green, "SAGE": f.sage,
        "RED": f.red_hi, "CLAY": f.clay,
    }


def palette_case(flavors, names):
    """A bash `case` that sets the named color triplets for the chosen flavor."""
    arms = []
    for f in flavors:
        body = " ".join(f"{k}='{triplet(v)}'" for k, v in roles(f).items() if k in names)
        pattern = "*" if f.id == "walnut" else f.id
        arms.append((pattern, f"  {pattern}) {body} ;;"))
    arms.sort(key=lambda a: a[0] == "*")  # default arm last
    return "case $flavor in\n" + "\n".join(a[1] for a in arms) + "\nesac"


# Which flavor to draw in: the one your Claude Code theme names, Enamel for a
# light theme, and for "auto" whatever the terminal or macOS says.
PICK_FLAVOR = r"""pick_flavor() {
  case ${SUBWAY_SEAT_FLAVOR:-} in walnut | tunnel | enamel) flavor=$SUBWAY_SEAT_FLAVOR; return ;; esac
  flavor=walnut
  case $1 in
    *subway-seat-enamel*) flavor=enamel ;;
    *subway-seat-tunnel*) flavor=tunnel ;;
    *subway-seat*) ;;
    light*) flavor=enamel ;;
    auto)
      case ${COLORFGBG:-} in
        *\;7 | *\;15) flavor=enamel ;;
        *\;*) ;;
        *) case $OSTYPE in darwin*) defaults read -g AppleInterfaceStyle >/dev/null 2>&1 || flavor=enamel ;; esac ;;
      esac ;;
  esac
}"""

STATUSLINE = r"""#!/usr/bin/env bash
# __HEADER__
#
# Subway Seat status line for Claude Code: a station sign under the prompt.
#   (O) Opus   ~/Code/project    main !2   load ━━━━──────  42%   $0.84
# Reads Claude Code's status JSON on stdin and needs jq. Segments drop off the
# right end when the terminal is narrow ($COLUMNS, which Claude Code sets).
# SUBWAY_SEAT_FLAVOR=walnut|tunnel|enamel overrides the flavor read from your theme;
# SUBWAY_SEAT_GLYPHS=plain drops the Nerd Font glyphs.

input=$(cat)
if ! command -v jq >/dev/null 2>&1; then
  printf 'Subway Seat: the status line needs jq\n'
  exit 0
fi
settings=
f="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json"
[ -r "$f" ] && settings=$(<"$f")

# One jq call. Fields are joined with the unit separator (not a tab, which `read`
# would treat as whitespace and collapse), and control characters are stripped.
IFS=$'\037' read -r theme model key letter agent cwd dir pct cost effort rlabel rpct wt wtbranch vim <<EOF
$(jq -r --arg settings "$settings" '
  def clean: tostring | gsub("\\p{Cc}"; "");
  def int: if type == "number" then (. + 0.5 | floor | if . < 0 then 0 else . end) else "" end;
  def cut($n): if length > $n then .[0:$n - 1] + "…" else . end;
  def money: (. * 100 + 0.5 | floor) as $c
    | "\($c / 100 | floor).\($c % 100 | tostring | if length < 2 then "0" + . else . end)";
  def short: (env.HOME // "") as $h
    | (if $h != "" and . == $h then "~"
       elif $h != "" and startswith($h + "/") then "~" + .[($h | length):]
       else . end)
    | (if . != "/" then sub("/+$"; "") else . end)
    | split("/") as $p
    | if ($p | length) > 3 then "…/" + ($p[-2:] | map(cut(24)) | join("/")) else cut(40) end;
  (.model.display_name // .model.id // "Claude" | clean | sub(" *\\([0-9.]+ ?[KkMm] context\\)$"; "")) as $model
  | (.workspace.current_dir // .cwd // "" | clean) as $cwd
  | (.rate_limits // {}) as $rl
  | ([["5h", $rl.five_hour.used_percentage], ["7d", $rl.seven_day.used_percentage]]
     | map(select(.[1] | type == "number")) | max_by(.[1]) // ["", ""]) as $rate
  | [ (($settings | try fromjson catch {}) | .theme // "" | clean),
      $model, ($model | ascii_downcase), ($model | .[0:1] | ascii_upcase), (.agent.name // "" | clean | cut(20)),
      ($cwd | short), $cwd,
      (.context_window.used_percentage | int),
      (if ($rl.five_hour // $rl.seven_day) != null then ""
       elif (.cost.total_cost_usd | type) == "number" then .cost.total_cost_usd | money
       else "" end),
      (.effort.level // "" | clean),
      $rate[0], ($rate[1] | int),
      (.worktree.name // .workspace.git_worktree // "" | clean),
      (.worktree.branch // "" | clean),
      (.vim.mode // "" | clean | ascii_upcase)
    ] | map(tostring) | join("\u001f")' <<<"$input" 2>/dev/null)
EOF

model=${model:-Claude} letter=${letter:-C}

__PICK_FLAVOR__
pick_flavor "$theme"

__PALETTE__

F=$'\033[38;2;' G=$'\033[48;2;' R=$'\033[0m'  # "$F${TEXT}m" is a foreground, "$G${TEXT}m" a background
B=$'\033[1m'
nerd=1; [ "${SUBWAY_SEAT_GLYPHS:-}" = plain ] && nerd=0
CAP_L=$'\xee\x82\xb6' CAP_R=$'\xee\x82\xb4' BRANCH=$'\xee\x82\xa0'  # Nerd Font U+E0B6 U+E0B4 U+E0A0

# Terminal cells in a string: count bytes, less UTF-8 continuation bytes.
w() { local LC_ALL=C; local s=${1//[$'\200'-$'\277']/}; W=${#s}; }

# Segments go left to right until the next one doesn't fit.
cols=${COLUMNS:-0}
case $cols in '' | *[!0-9]*) cols=0 ;; esac
room=100000; [ "$cols" -gt 0 ] && room=$((cols - 4))
out='' used=0 full=''
add() { # $1 = plain text (for measuring), $2 = colored text
  [ -n "$full" ] && return 1
  w "$1"
  local need=$W
  [ -n "$out" ] && need=$((W + 3))
  if [ $((used + need)) -gt "$room" ]; then full=1; return 1; fi
  [ -n "$out" ] && out+='   '
  out+=$2 used=$((used + need))
}

meter() { # $1 = percent, $2 = cells, $3 = color of the filled part
  local fill=$((($1 * $2 + 50) / 100)) i
  [ $fill -gt "$2" ] && fill=$2
  M="$F${3}m"; for ((i = 0; i < fill; i++)); do M+="━"; done
  M+="$F${RAIL}m"; for ((i = fill; i < $2; i++)); do M+="─"; done
  M+=$R; MP=''; for ((i = 0; i < $2; i++)); do MP+="-"; done
}
level() { if [ "$1" -ge 80 ]; then L=$RED; elif [ "$1" -ge 50 ]; then L=$YELLOW; else L=$GREEN; fi; }

# The model as a route bullet: a colored circle with one bold letter.
case $key in
  *opus*) line=$ORANGE ;; *sonnet*) line=$YELLOW ;; *haiku*) line=$GREEN ;; *fable*) line=$SAGE ;; *) line=$CLAY ;;
esac
if [ $nerd = 1 ]; then
  bullet="$F${line}m$CAP_L$R$G${line}m$F${INK}m$B$letter$R$F${line}m$CAP_R$R"
else
  bullet="$G${line}m$F${INK}m$B $letter $R"
fi
chip='' chipw=''
case $vim in
  N*) chip=$YELLOW ;; I*) chip=$GREEN ;; V*) chip=$CLAY ;; R*) chip=$RED ;; ?*) chip=$SAGE ;;
esac
[ -n "$chip" ] && chip="$G${chip}m$F${INK}m$B ${vim:0:1} $R " chipw='    '
as=''; [ -n "$agent" ] && as=" $F${DIM}mas $agent$R"
add "${chipw}xxx $model${agent:+ as $agent}" "$chip$bullet $F${TEXT}m$model$R$as" ||
  { out="$chip$bullet"; full=1; }

# Where we are.
[ -n "$cwd" ] && add "$cwd" "$F${SUB}m$cwd$R"

# Which line: the git branch (or @commit when detached) and a dirty count. In a
# worktree the branch gets a transfer mark instead of the branch glyph.
if [ -n "$dir" ] && [ -z "$full" ]; then
  IFS=$'\037' read -r head oid dirty <<EOF
$(git --no-optional-locks -C "$dir" status --porcelain=v2 --branch 2>/dev/null |
    awk '/^# branch\.head /{h=$3} /^# branch\.oid /{o=$3} !/^#/{n++} END{if (h != "") printf "%s\037%s\037%d", h, o, n}')
EOF
  [ -z "$head" ] && head=$wtbranch
  [ "$head" = "(detached)" ] && head="@${oid:0:7}"
  if [ -n "$head" ]; then
    mark=''
    if [ -n "$wt" ]; then mark='↳ '; elif [ $nerd = 1 ]; then mark="$BRANCH "; fi
    d=''; [ "${dirty:-0}" != 0 ] && d=" !$dirty"
    add "$mark$head$d" "$F${YELLOW}m$mark$head$R${d:+ $F${CLAY}m!$dirty$R}"
  fi
fi

# How full the car is: context used, as a ten-cell meter.
if [ -n "$pct" ]; then
  level "$pct"; meter "$pct" 10 "$L"
  printf -v P '%3d' "$pct"
  add "load $MP $P%" "$F${FAINT}mload$R $M $F${DIM}m$P%$R"
fi

# The fare so far, or, on a Pro or Max plan, the pass: the fuller usage limit once it's half used.
if [ -n "$rlabel" ] && [ "$rpct" -ge 50 ] 2>/dev/null; then
  level "$rpct"; meter "$rpct" 5 "$L"
  printf -v P '%3d' "$rpct"
  add "$rlabel $MP $P%" "$F${FAINT}m$rlabel$R $M $F${DIM}m$P%$R"
elif [ -n "$cost" ]; then
  add "\$$cost" "$F${DIM}m\$$cost$R"
fi

# Effort, when it's turned up.
case $effort in
  xhigh | max) add "≋ $effort" "$F${CLAY}m≋ $effort$R" ;;
esac

printf '%s\n' "$out"
"""

SUBAGENTS = r"""#!/usr/bin/env bash
# __HEADER__
#
# Subway Seat rows for Claude Code's subagent panel: a route bullet colored by
# state, the name, what it's doing, and how full its context is.
# Reads {columns, tasks:[…]} on stdin and prints one {"id","content"} line per task.
# Needs jq; without it Claude Code keeps its own rows.

input=$(cat)
command -v jq >/dev/null 2>&1 || exit 0

__PICK_FLAVOR__
pick_flavor "$(jq -r '.theme // empty' "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json" 2>/dev/null)"

__PALETTE__

# Route bullets: round with a Nerd Font, square with SUBWAY_SEAT_GLYPHS=plain.
caps=$'\xee\x82\xb6\037\xee\x82\xb4'  # U+E0B6, U+E0B4
[ "${SUBWAY_SEAT_GLYPHS:-}" = plain ] && caps=$'\037'

jq -c --arg ink "$INK" --arg text "$TEXT" --arg dim "$DIM" --arg faint "$FAINT" --arg rail "$RAIL" \
  --arg run "$YELLOW" --arg ok "$GREEN" --arg bad "$RED" --arg idle "$SAGE" --arg caps "$caps" '
  def fg($c): "\u001b[38;2;\($c)m";
  def bg($c): "\u001b[48;2;\($c)m";
  def reset: "\u001b[0m";
  def clean: tostring | gsub("\\p{Cc}"; "");
  def cut($n): if length > $n then .[0:$n - 1] + "…" else . end;
  def k($n): if $n >= 1000000 then "\(($n / 100000 | floor) / 10)M"
             elif $n >= 1000 then "\(($n / 100 | floor) / 10)k" else "\($n | floor)" end;
  def kind: {local_agent: "agent", local_bash: "shell", remote_agent: "remote agent",
             local_workflow: "workflow", in_process_teammate: "teammate"}[.] // .;
  (.columns // 80) as $cols
  | (.tasks // [])[]
  | select(.id != null)
  | ((.status // "") | ascii_downcase) as $s
  | (if ($s | test("fail|error")) then $bad
     elif ($s | test("kill|cancel|stop")) then $faint
     elif ($s | test("complete|done|success|finish")) then $ok
     elif ($s | test("run|progress|active|work")) then $run
     else $idle end) as $line
  | ((.name // .description // (.type // "agent" | kind)) | clean) as $full
  | (.tokenCount // 0) as $tok
  | (if (.contextWindowSize // 0) > 0
     then ($tok * 5 / .contextWindowSize + 0.5 | floor | if . > 5 then 5 elif . < 0 then 0 else . end)
     else null end) as $cells
  | k($tok) as $toks
  | (4 + (if $cells != null then 7 else 0 end) + 2 + ($toks | length)) as $fixed
  | ($full | cut([28, $cols - $fixed] | min | if . < 4 then 4 else . end)) as $name
  | ($name | .[0:1] | ascii_upcase) as $letter
  | ($cols - $fixed - ($name | length) - 2) as $room
  | ((.label // .description // "") | clean | if . == $full then "" else . end
     | if $room < 8 then "" else cut($room) end) as $what
  | {
      id,
      content: (
        (($caps | split("\u001f")) as [$l, $r]
         | if $l == "" then bg($line) + fg($ink) + " \($letter) " + reset
           else fg($line) + $l + bg($line) + fg($ink) + "\u001b[1m" + $letter + reset + fg($line) + $r + reset end)
        + " "
        + fg($text) + $name + reset
        + (if $what != "" then "  " + fg($dim) + $what + reset else "" end)
        + (if $cells != null then "  " + fg($line) + ("━" * $cells) + fg($rail) + ("─" * (5 - $cells)) + reset else "" end)
        + "  " + fg($faint) + $toks + reset
      )
    }
' <<<"$input"
"""

STATUS_ROLES = ("INK", "TEXT", "SUB", "DIM", "FAINT", "RAIL", "ORANGE", "YELLOW", "GREEN", "SAGE", "RED", "CLAY")
SUBAGENT_ROLES = ("INK", "TEXT", "DIM", "FAINT", "RAIL", "YELLOW", "GREEN", "SAGE", "RED")


def script(template, flavors, names):
    return (
        template.replace("__HEADER__", HEADER)
        .replace("__PICK_FLAVOR__", PICK_FLAVOR)
        .replace("__PALETTE__", palette_case(flavors, names))
    )


# ── Plugin plumbing: keep the scripts current, and merge settings on request ──
# Plugin settings.json isn't expanded, so the default subagent rows find the
# copies the session-start hook keeps in the plugin's data folder, and stay quiet
# (Claude Code's own rows) until they exist.
SUBAGENTS_COMMAND = (
    'for f in "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"/plugins/data/subway-seat-*/subway-seat-subagents; '
    'do [ -x "$f" ] && exec "$f"; done; exit 0'
)

SYNC = r"""#!/bin/sh
# __HEADER__
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
"""

SETUP = r"""#!/usr/bin/env bash
# __HEADER__
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
      | if $voice == "yes" then .outputStyle = "__OUTPUT_STYLE__" else . end' "$root/settings/$slug.json") ||
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
"""

HOOKS = {
    "hooks": {
        "SessionStart": [{
            "hooks": [{
                "type": "command",
                "command": '"${CLAUDE_PLUGIN_ROOT}/scripts/sync.sh" "${CLAUDE_PLUGIN_ROOT}" "${CLAUDE_PLUGIN_DATA}"',
                "timeout": 10,
            }],
        }],
    },
}

OUTPUT_STYLE = """---
name: Subway Seat
description: Relaxed and warm, like a friend on the next seat. Still exact.
keep-coding-instructions: true
---

# Subway Seat

Talk like a good friend on the next seat of a slow Sunday train: unhurried, warm, plain-spoken. Only the voice relaxes. The engineering stays exactly as careful, and every other instruction still applies.

- Lead with the answer or the result, then the why. No preamble, no pep talk, no narration of what you're about to do.
- Short sentences, everyday words, first and second person: "I changed", "you'll want".
- Stay calm about problems: say what broke, what it means, and the next step. Never soften a real risk to keep the mood.
- Flavor is rare. At most one small image from the 1970s or the subway (a transfer, the express, a record, shag carpet) per turn, only in your final message, and most turns need none. Skip it for errors, security, data loss, or when the user is stressed.
- The voice is for talking to the user only. Code, comments, commit messages, PR and issue text, docs, config, logs, and anything you write to a file or pass to a tool keep their normal professional register.
- Precision beats personality. Exact names, paths, numbers and commands always win over a turn of phrase.
"""

SETUP_SKILL = """---
name: setup
description: Add Subway Seat's theme, station-sign status line, 70s spinner verbs and "Next stop" tips to the user's Claude Code settings, or take them out again with `remove`.
argument-hint: "[remove]"
disable-model-invocation: true
allowed-tools: AskUserQuestion Read Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh *)
---

# Subway Seat setup

The plugin already ships the three themes, the subagent rows and the Subway Seat output style. This skill adds what a plugin can't set by itself, in the user's own settings: the theme choice, the status line, the spinner verbs and the tips. Do it all in this one turn, and change nothing until the user picks **Apply**.

Run each command exactly as written, without quoting the script path, so it matches the pre-approved rule. Don't edit settings files any other way.

Arguments: `$ARGUMENTS`

## If the arguments say `remove`

1. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh remove --dry-run` and show the output. If nothing is listed, say so and stop.
2. Ask with AskUserQuestion: "Remove these Subway Seat settings?" with the options **Remove** and **Cancel**.
3. On Remove, run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh remove` and pass on what it prints. Add that `claude plugin uninstall subway-seat@subway-seat` removes the plugin itself, and that uninstalling never touches these settings.

## Otherwise

1. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh check`. If it reports a problem, such as jq missing, pass it on and stop.
2. Ask one AskUserQuestion with three questions:
   - **Flavor**: "Subway Seat" (Walnut, the original dark brown), "Subway Seat Tunnel" (deeper dark) or "Subway Seat Enamel" (light). Recommend the one that matches their terminal's background.
   - **Spinner verbs**: "Replace" (only the 70s verbs) or "Add" (mixed in with Claude Code's own).
   - **Voice**: "Everywhere" (the relaxed Subway Seat output style in every project) or "Not now" (keep the current style; `/config` › Output style switches it per project later).
3. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh apply --flavor <walnut|tunnel|enamel> --verbs <replace|append> --voice <yes|no> --data ${CLAUDE_PLUGIN_DATA} --dry-run` with their answers, and show its output: every key it will change, with the current and new value.
4. Ask with AskUserQuestion: "Apply these changes?" with the options **Apply** and **Cancel**. On Cancel, stop.
5. On Apply, run the same command without `--dry-run`, and pass on what it prints, including the backup path and any notes.
6. Finish in two or three short lines: the theme and status line switch over within a moment (restart Claude Code if they don't); the status line looks best with a Nerd Font, and `SUBWAY_SEAT_GLYPHS=plain` drops the glyphs; `/subway-seat:setup remove` undoes all of it.
"""


def plugin_manifest():
    return json.dumps({
        "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
        "name": PLUGIN,
        "displayName": "Subway Seat",
        "version": VERSION,
        "description": "A walnut-brown 1970s NYC subway theme for Claude Code: three flavors, a station-sign "
        "status line, subagent rows, 70s spinner verbs and tips, and a relaxed output style.",
        "author": {"name": "Oddur Sigurdsson", "url": "https://github.com/oddurs"},
        "homepage": f"{SITE}/ports/claude-code",
        "repository": REPO,
        "license": "MIT",
        "keywords": KEYWORDS,
    }, indent=2) + "\n"


KEYWORDS = ["theme", "color-scheme", "statusline", "70s", "retro", "subway", "subway-seat"]


def build(flavors):
    how_setup = "merged into ~/.claude/settings.json by /subway-seat:setup"
    outs = []
    for f in flavors:
        body = json.dumps(theme(f), indent=2) + "\n"
        outs.append(Out(f"themes/{f.slug}.json", body, flavor=f.id,
                        dest=f"~/.claude/themes/{f.slug}.json", lang="json"))
        outs.append(Out(f"plugin/themes/{f.slug}.json", body, flavor=f.id, lang="json"))
        outs.append(Out(f"plugin/settings/{f.slug}.json", json.dumps(settings(f), indent=2) + "\n",
                        flavor=f.id, how=how_setup, lang="json"))
    outs += [
        Out("plugin/.claude-plugin/plugin.json", plugin_manifest(), lang="json"),
        Out("plugin/settings.json", json.dumps({"subagentStatusLine": {
            "type": "command", "command": SUBAGENTS_COMMAND}}, indent=2) + "\n", lang="json"),
        Out("plugin/hooks/hooks.json", json.dumps(HOOKS, indent=2) + "\n", lang="json"),
        Out("plugin/scripts/subway-seat-statusline", script(STATUSLINE, flavors, STATUS_ROLES),
            dest="~/.claude/subway-seat/subway-seat-statusline", lang="sh"),
        Out("plugin/scripts/subway-seat-subagents", script(SUBAGENTS, flavors, SUBAGENT_ROLES),
            dest="~/.claude/subway-seat/subway-seat-subagents", lang="sh"),
        Out("plugin/scripts/sync.sh", SYNC.replace("__HEADER__", HEADER), lang="sh"),
        Out("plugin/scripts/setup.sh", SETUP.replace("__HEADER__", HEADER).replace("__OUTPUT_STYLE__", OUTPUT_STYLE_NAME),
            lang="sh"),
        Out("plugin/tips.json", tips_json(), dest="~/.claude/subway-seat/tips.json", lang="json"),
        Out("plugin/output-styles/subway-seat.md", OUTPUT_STYLE, dest="~/.claude/output-styles/subway-seat.md", lang="text"),
        Out("plugin/skills/setup/SKILL.md", SETUP_SKILL, lang="text"),
    ]
    return outs
