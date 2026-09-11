---
name: setup
description: Add Subway Seat's theme, station-sign status line, 70s spinner verbs and "Next stop" tips to the user's Claude Code settings, or take them out again with `remove`.
argument-hint: "[remove]"
disable-model-invocation: true
allowed-tools: AskUserQuestion Read Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh *)
---

# Subway Seat setup

The plugin already ships the themes, the subagent rows and the Subway Seat output style. This skill adds what a plugin can't set by itself, in the user's own settings: the theme choice, the status line, the spinner verbs and the tips. Do it all in this one turn, and change nothing until the user picks **Apply**.

Run each command exactly as written, without quoting the script path, so it matches the pre-approved rule. Don't edit settings files any other way.

Arguments: `$ARGUMENTS`

## If the arguments say `remove`

1. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh remove --dry-run` and show the output. If nothing is listed, say so and stop.
2. Ask with AskUserQuestion: "Remove these Subway Seat settings?" with the options **Remove** and **Cancel**.
3. On Remove, run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh remove` and pass on what it prints. Add that `claude plugin uninstall subway-seat@subway-seat` removes the plugin itself, and that uninstalling never touches these settings.

## Otherwise

1. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh check`. If it reports a problem, such as jq missing, pass it on and stop.
2. Ask one AskUserQuestion with four questions:
   - **Flavor**: "Subway Seat" (Walnut, the original dark brown), "Subway Seat Tunnel" (deeper dark) or "Subway Seat Enamel" (light). Recommend the one that matches their terminal's background.
   - **Code colors**, for code in diffs and file views: "Claude Code's" (Monokai on dark, GitHub on light; looks the same in any terminal) or "My terminal's" (the terminal's 16 colors, which are Subway Seat's when the terminal uses Subway Seat; diff lines get plainer grounds). Recommend "My terminal's" if their terminal uses a Subway Seat theme, otherwise "Claude Code's".
   - **Spinner verbs**: "Replace" (only the 70s verbs) or "Add" (mixed in with Claude Code's own).
   - **Voice**: "Everywhere" (the relaxed Subway Seat output style in every project) or "Not now" (keep the current style; `/config` › Output style switches it per project later).
3. Run `${CLAUDE_PLUGIN_ROOT}/scripts/setup.sh apply --flavor <walnut|tunnel|enamel> --code <own|terminal> --verbs <replace|append> --voice <yes|no> --data ${CLAUDE_PLUGIN_DATA} --dry-run` with their answers, and show its output: every key it will change, with the current and new value.
4. Ask with AskUserQuestion: "Apply these changes?" with the options **Apply** and **Cancel**. On Cancel, stop.
5. On Apply, run the same command without `--dry-run`, and pass on what it prints, including the backup path and any notes.
6. Finish in two or three short lines: the theme and status line switch over within a moment (restart Claude Code if they don't); the status line looks best with a Nerd Font, and `SUBWAY_SEAT_GLYPHS=plain` drops the glyphs; `/subway-seat:setup remove` undoes all of it.
