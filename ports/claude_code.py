"""Claude Code: themes, a station-sign status line, subagent rows, spinner verbs
and tips, a relaxed output style, and a plugin that bundles all of it."""

import json

from ports._lib import HEADER, REPO, VERSION, Out, rgb, tints

META = {
    "id": "claude-code",
    "name": "Claude Code",
    "category": "Agents",
    "homepage": "https://claude.com/claude-code",
    "enable": {
        "where": "Claude Code, from the Subway Seat marketplace",
        "code": "/plugin marketplace add oddurs/subway-seat\n/plugin install subway-seat@subway-seat\n/theme      # pick {name}\n/subway-seat:setup",
        "lang": "text",
    },
    "notes": "The deepest port. The plugin ships all three themes, a relaxed output style and a "
    "subagent status line; `/subway-seat:setup` adds the station-sign status line, 70s spinner verbs "
    "and “Next stop” tips to your settings. Every token is themed, down to the ultrathink rainbow.",
}



def theme(f):
    c = f
    t = tints(f)
    ink = c.crust if f.dark else c.base
    overrides = {
        "claude": c.orange, "claudeShimmer": c.orange_hi,
        "text": c.text, "inverseText": ink,
        "inactive": c.overlay1, "inactiveShimmer": c.overlay2,
        "subtle": c.surface2,
        "suggestion": c.yellow,
        "permission": c.yellow, "permissionShimmer": c.yellow_hi,
        "remember": c.sage,
        "success": c.green, "error": c.red_hi,
        "warning": c.yellow, "warningShimmer": c.yellow_hi,
        "merged": c.clay,
        "promptBorder": c.overlay0, "promptBorderShimmer": c.overlay1,
        "planMode": c.sage, "autoAccept": c.clay, "bashBorder": c.yellow,
        "ide": c.denim, "fastMode": c.orange_hi, "fastModeShimmer": c.yellow_hi,
        "effortUltra": c.yellow_hi,
        "diffAdded": t["add"], "diffRemoved": t["del"],
        "diffAddedDimmed": f.mix("green", "base", 0.09),
        "diffRemovedDimmed": f.mix("red", "base", 0.1),
        "diffAddedWord": t["add_emph"], "diffRemovedWord": t["del_emph"],
        "userMessageBackground": c.surface0 if f.dark else c.mantle,
        "userMessageBackgroundHover": c.surface1 if f.dark else c.crust,
        "bashMessageBackgroundColor": f.mix("yellow", "base", 0.1),
        "memoryBackgroundColor": f.mix("sage", "base", 0.12),
        "selectionBg": c.surface2 if f.dark else c.surface1,
        "rate_limit_fill": c.orange, "rate_limit_empty": c.surface1,
        "briefLabelYou": c.yellow, "briefLabelClaude": c.orange,
        "red_FOR_SUBAGENTS_ONLY": c.red_hi, "blue_FOR_SUBAGENTS_ONLY": c.denim,
        "green_FOR_SUBAGENTS_ONLY": c.green, "yellow_FOR_SUBAGENTS_ONLY": c.yellow,
        "purple_FOR_SUBAGENTS_ONLY": c.denim_hi, "orange_FOR_SUBAGENTS_ONLY": c.orange,
        "pink_FOR_SUBAGENTS_ONLY": c.clay, "cyan_FOR_SUBAGENTS_ONLY": c.sage,
        # ultrathink's rainbow, as a 70s stripe
        "rainbow_red": c.red, "rainbow_orange": c.orange, "rainbow_yellow": c.yellow,
        "rainbow_green": c.green, "rainbow_blue": c.sage, "rainbow_indigo": c.denim,
        "rainbow_violet": c.clay,
        "rainbow_red_shimmer": c.red_hi, "rainbow_orange_shimmer": c.orange_hi,
        "rainbow_yellow_shimmer": c.yellow_hi, "rainbow_green_shimmer": c.green_hi,
        "rainbow_blue_shimmer": c.sage_hi, "rainbow_indigo_shimmer": c.denim_hi,
        "rainbow_violet_shimmer": c.text_hi,
    }
    return {"name": f.name, "base": "dark" if f.dark else "light", "overrides": overrides}


# ── Spinner verbs and tips ─────────────────────────────────────────────────
VERBS = [
    "Standing clear", "Riding the local", "Running express", "Transferring", "Holding the doors",
    "Watching the gap", "Waiting on the platform", "Rolling uptown", "Rolling downtown",
    "Changing at 14th Street", "Dropping a token", "Grabbing the pole", "Finding a seat",
    "Sinking into the shag", "Flipping the record", "Warming up the hi-fi", "Tuning the 8-track",
    "Adjusting the rabbit ears", "Watering the spider plant", "Percolating", "Mellowing out",
    "Keeping it groovy", "Easing on down the road", "Digging it", "Grooving", "Kicking back",
    "Taking it easy", "Spinning the lazy Susan", "Knotting the macramé", "Lava-lamping",
]

TIPS = [
    ("clear", "/clear gives you a fresh car. Stand clear of the closing doors."),
    ("compact", "Car getting crowded? /compact squeezes the conversation down so there's room to stretch."),
    ("resume", "/resume picks up a ride you left earlier, right where you got off."),
    ("modes", "Shift+Tab changes trains: plan first, or let edits through on their own."),
    ("esc", "Esc stops Claude mid-turn. No emergency brake required."),
    ("rewind", "Esc twice rewinds the line to an earlier stop."),
    ("bang", "Start a message with ! to run a shell command without leaving your seat."),
    ("at", "@ a file to bring it along for the ride."),
    ("claude-md", "Put the house rules in CLAUDE.md so every ride starts on the right line."),
    ("theme", "/theme swaps between Walnut, Tunnel and Enamel. Same seats, different light."),
    ("model", "/model switches trains. Opus for the long haul, Haiku for a hop."),
    ("slow", "No rush. The next train is always right behind this one."),
]


def tips_json():
    return json.dumps(
        {"tips": [{"id": f"subway-seat.{i}", "text": text, "cooldownSessions": 2} for i, text in TIPS]},
        indent=2,
    ) + "\n"


def settings(f, root="~/.claude/subway-seat"):
    return {
        "theme": f"custom:{f.slug}",
        "statusLine": {"type": "command", "command": f"{root}/subway-seat-statusline", "padding": 1},
        "subagentStatusLine": {"type": "command", "command": f"{root}/subway-seat-subagents"},
        "spinnerVerbs": {"mode": "replace", "verbs": VERBS},
        "spinnerTipsOverride": {"tipsFile": f"{root}/tips.json", "label": "Next stop"},
    }


# ── Status line scripts (bash + jq) ────────────────────────────────────────
def triplet(color):
    return ";".join(str(v) for v in rgb(color))


def palette_case(flavors):
    """A bash `case` that sets colour triplets for the chosen flavor."""
    arms = []
    for f in flavors:
        roles = {
            "INK": f.crust if f.dark else f.base, "TEXT": f.text, "SUB": f.subtext1, "DIM": f.overlay1,
            "FAINT": f.overlay0, "RAIL": f.surface2, "ORANGE": f.orange, "YELLOW": f.yellow, "GREEN": f.green,
            "SAGE": f.sage, "RED": f.red_hi, "CLAY": f.clay, "DENIM": f.denim,
        }
        body = " ".join(f"{k}='{triplet(v)}'" for k, v in roles.items())
        pattern = "*" if f.id == "walnut" else f.id
        arms.append((pattern, f"  {pattern}) {body} ;;"))
    arms.sort(key=lambda a: a[0] == "*")  # default arm last
    return "case $flavor in\n" + "\n".join(a[1] for a in arms) + "\nesac"


FLAVOR_DETECT = r"""flavor=${SUBWAY_SEAT_FLAVOR:-}
if [ -z "$flavor" ]; then
  case $(jq -r '.theme // empty' "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json" 2>/dev/null) in
    *subway-seat-tunnel) flavor=tunnel ;;
    *subway-seat-enamel) flavor=enamel ;;
    *) flavor=walnut ;;
  esac
fi"""

STATUSLINE = r"""#!/usr/bin/env bash
# __HEADER__
#
# Subway Seat status line for Claude Code: a station sign under the prompt.
#   (O) Opus   ~/Code/project    main !2   load ━━━━──────  42%   $0.84
# Reads Claude Code's status JSON on stdin. Needs jq.
# SUBWAY_SEAT_FLAVOR=walnut|tunnel|enamel overrides the flavor it reads from your theme;
# SUBWAY_SEAT_GLYPHS=plain drops the Nerd Font glyphs.

input=$(cat)
get() { jq -r "$1 // empty" <<<"$input" 2>/dev/null; }

__FLAVOR_DETECT__

__PALETTE__

fg() { printf '\033[38;2;%sm' "$1"; }
bg() { printf '\033[48;2;%sm' "$1"; }
R=$'\033[0m'
B=$'\033[1m'
nerd=1; [ "${SUBWAY_SEAT_GLYPHS:-}" = plain ] && nerd=0
CAP_L=$'\xee\x82\xb6' CAP_R=$'\xee\x82\xb4' BRANCH=$'\xee\x82\xa0'  # Nerd Font U+E0B6 U+E0B4 U+E0A0

# The model as a route bullet: a coloured circle with one bold letter.
model=$(get '.model.display_name'); model=${model:-Claude}
case $(printf '%s' "$model" | tr '[:upper:]' '[:lower:]') in
  *opus*) line=$ORANGE ;; *sonnet*) line=$YELLOW ;; *haiku*) line=$GREEN ;; *fable*) line=$SAGE ;; *) line=$CLAY ;;
esac
letter=$(printf '%s' "$model" | cut -c1 | tr '[:lower:]' '[:upper:]')
if [ $nerd = 1 ]; then
  bullet="$(fg "$line")$CAP_L$R$(bg "$line")$(fg "$INK")$B$letter$R$(fg "$line")$CAP_R$R"
else
  bullet="$(bg "$line")$(fg "$INK")$B $letter $R"
fi
out="$bullet $(fg "$TEXT")$model$R"

# Where we are.
cwd=$(get '.workspace.current_dir'); cwd=${cwd:-$(get '.cwd')}
if [ -n "$cwd" ]; then
  short=${cwd/#$HOME/\~}
  short=$(printf '%s' "$short" | awk -F/ '{ n = NF; if (n > 3) print "…/" $(n-1) "/" $n; else print $0 }')
  out+="   $(fg "$SUB")$short$R"
fi

# Which line: git branch plus a dirty count.
if [ -n "$cwd" ] && branch=$(git -C "$cwd" branch --show-current 2>/dev/null) && [ -n "$branch" ]; then
  dirty=$(git -C "$cwd" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  mark=""; [ $nerd = 1 ] && mark="$BRANCH "
  out+="   $(fg "$YELLOW")$mark$branch$R"
  [ "$dirty" != 0 ] && out+=" $(fg "$CLAY")!$dirty$R"
fi

# How full the car is: context used, as a ten-cell meter.
pct=$(get '.context_window.used_percentage')
if [ -n "$pct" ]; then
  p=${pct%.*}; cells=$(( (p + 5) / 10 )); [ $cells -gt 10 ] && cells=10
  if [ "$p" -ge 80 ]; then load=$RED; elif [ "$p" -ge 50 ]; then load=$YELLOW; else load=$GREEN; fi
  meter="$(fg "$load")"; for ((i = 0; i < cells; i++)); do meter+="━"; done
  meter+="$(fg "$RAIL")"; for ((i = cells; i < 10; i++)); do meter+="─"; done
  out+="   $(fg "$FAINT")load$R $meter$R $(fg "$DIM")$(printf '%3d' "$p")%$R"
fi

# Fare so far.
cost=$(get '.cost.total_cost_usd')
[ -n "$cost" ] && out+="   $(fg "$DIM")\$$(printf '%.2f' "$cost")$R"

# Effort, when it's turned up.
case $(get '.effort.level') in
  xhigh | max) out+="   $(fg "$CLAY")≋ $(get '.effort.level')$R" ;;
esac

printf '%s\n' "$out"
"""

SUBAGENTS = r"""#!/usr/bin/env bash
# __HEADER__
#
# Subway Seat rows for Claude Code's subagent panel: a route bullet coloured by
# state, the name, what it's doing, and how full its context is.
# Reads {columns, tasks:[…]} on stdin and prints one {"id","content"} line per task. Needs jq.

__FLAVOR_DETECT__

__PALETTE__

jq -c --arg ink "$INK" --arg text "$TEXT" --arg dim "$DIM" --arg faint "$FAINT" --arg rail "$RAIL" \
  --arg run "$YELLOW" --arg ok "$GREEN" --arg bad "$RED" --arg idle "$SAGE" '
  def fg($c): "\u001b[38;2;\($c)m";
  def bg($c): "\u001b[48;2;\($c)m";
  def reset: "\u001b[0m";
  def k($n): if $n >= 1000 then "\(($n / 100 | floor) / 10)k" else "\($n)" end;
  (.columns // 80) as $cols
  | .tasks[]
  | ((.status // "") | ascii_downcase) as $s
  | (if ($s | test("fail|error|kill|cancel")) then $bad
     elif ($s | test("complete|done|success|finish")) then $ok
     elif ($s | test("run|progress|active|work")) then $run
     else $idle end) as $line
  | ((.name // .type // "agent") | .[0:1] | ascii_upcase) as $letter
  | (if (.contextWindowSize // 0) > 0 then ((.tokenCount // 0) * 5 / .contextWindowSize | floor | if . > 5 then 5 else . end) else null end) as $cells
  | ((.description // .label // "") | if length > ($cols - 40) then .[0:($cols - 41)] + "…" else . end) as $what
  | {
      id,
      content: (
        bg($line) + fg($ink) + " \($letter) " + reset + " "
        + fg($text) + (.name // .type // "agent") + reset
        + (if $what != "" then "  " + fg($dim) + $what + reset else "" end)
        + (if $cells != null then "  " + fg($line) + ("━" * $cells) + fg($rail) + ("─" * (5 - $cells)) + reset else "" end)
        + "  " + fg($faint) + k(.tokenCount // 0) + reset
      )
    }
'
"""


def script(template, flavors):
    return (
        template.replace("__HEADER__", HEADER)
        .replace("__FLAVOR_DETECT__", FLAVOR_DETECT)
        .replace("__PALETTE__", palette_case(flavors))
    )


OUTPUT_STYLE = """---
name: Subway Seat
description: Relaxed and warm, like a friend on the next seat. Still exact.
keep-coding-instructions: true
---

# Subway Seat

Talk like a good friend riding next to the user on a slow Sunday train: unhurried, warm and plain-spoken. The work stays exactly as careful as ever; only the voice relaxes.

- Lead with the answer or the result, then the why. No preamble, no pep talk.
- Short sentences. Everyday words. Say "I changed" and "you'll want", not "the implementation has been modified".
- Stay calm about problems. Name what broke, what it means, and the next step, without alarm.
- At most one light image per reply from the world of the 1970s or the subway (a transfer, the express, a record, shag carpet), and only when it genuinely helps. Never force it, and skip it entirely when the news is bad or the topic is serious.
- Never let the voice leak into anything you write for the user to keep: code, comments, commit messages, docs and file contents stay in their normal, professional register.
- Precision beats personality. When in doubt, drop the flavor and be exact.
"""

SETUP_SKILL = """---
name: setup
description: Install the Subway Seat status line, subagent rows, spinner verbs and "Next stop" tips into the user's Claude Code settings, and pick a flavor.
disable-model-invocation: true
allowed-tools: Bash, Read
---

# Subway Seat setup

Set the user up with Subway Seat's extras. Themes and the output style already ship with this plugin; this adds what a plugin can't set on its own. Everything below is reversible, and nothing is written until the user says yes.

1. Ask which flavor they want: **Subway Seat** (Walnut, dark), **Subway Seat Tunnel** (deeper dark) or **Subway Seat Enamel** (light). Suggest the one that matches their terminal background.
2. Ask whether spinner verbs should **replace** Claude Code's built-in verbs (full 70s vibe) or be **added** to them.
3. Copy the scripts and tips to a stable location, since the plugin directory changes between versions:

   ```bash
   mkdir -p ~/.claude/subway-seat
   cp "${CLAUDE_PLUGIN_ROOT}/bin/subway-seat-statusline" "${CLAUDE_PLUGIN_ROOT}/bin/subway-seat-subagents" "${CLAUDE_PLUGIN_ROOT}/tips.json" ~/.claude/subway-seat/
   chmod +x ~/.claude/subway-seat/subway-seat-*
   ```

4. Show the user the settings you'll merge (read the matching file in `${CLAUDE_PLUGIN_ROOT}/settings/`, e.g. `subway-seat-enamel.json`; switch `spinnerVerbs.mode` to `append` if they chose that). Point out any existing `statusLine`, `subagentStatusLine`, `spinnerVerbs`, `spinnerTipsOverride` or `theme` values they'd be replacing.
5. Only after they confirm, back up and merge with jq, keeping every other key:

   ```bash
   s="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json"
   cp "$s" "$s.subway-seat.bak"
   jq -s '.[0] * .[1]' "$s" "${CLAUDE_PLUGIN_ROOT}/settings/<flavor-slug>.json" > "$s.tmp" && mv "$s.tmp" "$s"
   ```

   If `settings.json` is a symlink (dotfiles), write through it: `cat "$s.tmp" > "$s" && rm "$s.tmp"` instead of `mv`.
6. Tell them it's done, that the status line needs `jq` and looks best with a Nerd Font (`SUBWAY_SEAT_GLYPHS=plain` drops the glyphs), and that `/output-style` can switch on the relaxed **Subway Seat** voice. Mention the backup path for undoing.
"""


def plugin_manifest():
    return json.dumps({
        "name": "subway-seat",
        "displayName": "Subway Seat",
        "version": VERSION,
        "description": "A walnut-brown 1970s NYC subway theme for Claude Code: three flavors, a station-sign "
        "status line, subagent rows, 70s spinner verbs and tips, and a relaxed output style.",
        "author": {"name": "Oddur Sigurdsson", "url": "https://github.com/oddurs"},
        "homepage": REPO,
        "repository": REPO,
        "license": "MIT",
        "keywords": ["theme", "color-scheme", "statusline", "70s", "retro", "subway-seat"],
        "outputStyles": "./output-styles/",
        "experimental": {"themes": "./themes/"},
    }, indent=2) + "\n"


def build(flavors):
    outs = []
    for f in flavors:
        body = json.dumps(theme(f), indent=2) + "\n"
        outs.append(Out(f"themes/{f.slug}.json", body, flavor=f.id,
                        dest=f"~/.claude/themes/{f.slug}.json", lang="json"))
        outs.append(Out(f"plugin/themes/{f.slug}.json", body, flavor=f.id, lang="json"))
        s = json.dumps(settings(f), indent=2) + "\n"
        outs.append(Out(f"plugin/settings/{f.slug}.json", s, flavor=f.id,
                        dest="merged into ~/.claude/settings.json by /subway-seat:setup", lang="json"))
    outs += [
        Out("plugin/.claude-plugin/plugin.json", plugin_manifest(), lang="json"),
        Out("plugin/settings.json", json.dumps({"subagentStatusLine": {
            "type": "command", "command": '"${CLAUDE_PLUGIN_ROOT}/bin/subway-seat-subagents"'}}, indent=2) + "\n",
            lang="json"),
        Out("plugin/bin/subway-seat-statusline", script(STATUSLINE, flavors),
            dest="~/.claude/subway-seat/subway-seat-statusline", lang="sh"),
        Out("plugin/bin/subway-seat-subagents", script(SUBAGENTS, flavors),
            dest="~/.claude/subway-seat/subway-seat-subagents", lang="sh"),
        Out("plugin/tips.json", tips_json(), dest="~/.claude/subway-seat/tips.json", lang="json"),
        Out("plugin/output-styles/subway-seat.md", OUTPUT_STYLE, dest="~/.claude/output-styles/subway-seat.md", lang="text"),
        Out("plugin/skills/setup/SKILL.md", SETUP_SKILL, lang="text"),
    ]
    return outs
