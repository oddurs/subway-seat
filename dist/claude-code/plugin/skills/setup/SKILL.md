---
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
