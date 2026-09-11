# Subway Seat for Claude Code

One plugin: every flavor's themes, a relaxed output style and subagent rows. `/subway-seat:setup` asks for a flavor, shows what it will change, then adds the station-sign status line, 70s spinner verbs and “Next stop” tips to your settings; `/subway-seat:setup remove` takes them out again. Claude Code colors code in diffs and file views itself (Monokai on dark, GitHub on light). Each flavor's “terminal colors” theme hands that to your terminal's 16 colors instead, so in a Subway Seat terminal the code matches the rest; diff lines then get plainer 256-color grounds, gray for added lines on the dark flavors. Inside tmux, Claude Code rounds colors to 256 unless `CLAUDE_CODE_TMUX_TRUECOLOR=1` is set.

[Claude Code](https://claude.com/product/claude-code) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/claude-code/) · Needs Claude Code 2.1.247+

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only claude-code
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`themes/subway-seat.json`](themes/subway-seat.json) | `~/.claude/themes/subway-seat.json` |
| Subway Seat | [`plugin/themes/subway-seat.json`](plugin/themes/subway-seat.json) |  |
| Subway Seat | [`themes/subway-seat-terminal.json`](themes/subway-seat-terminal.json) | `~/.claude/themes/subway-seat-terminal.json` |
| Subway Seat | [`plugin/themes/subway-seat-terminal.json`](plugin/themes/subway-seat-terminal.json) |  |
| Subway Seat | [`plugin/settings/subway-seat.json`](plugin/settings/subway-seat.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| Subway Seat Tunnel | [`themes/subway-seat-tunnel.json`](themes/subway-seat-tunnel.json) | `~/.claude/themes/subway-seat-tunnel.json` |
| Subway Seat Tunnel | [`plugin/themes/subway-seat-tunnel.json`](plugin/themes/subway-seat-tunnel.json) |  |
| Subway Seat Tunnel | [`themes/subway-seat-tunnel-terminal.json`](themes/subway-seat-tunnel-terminal.json) | `~/.claude/themes/subway-seat-tunnel-terminal.json` |
| Subway Seat Tunnel | [`plugin/themes/subway-seat-tunnel-terminal.json`](plugin/themes/subway-seat-tunnel-terminal.json) |  |
| Subway Seat Tunnel | [`plugin/settings/subway-seat-tunnel.json`](plugin/settings/subway-seat-tunnel.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| Subway Seat Enamel | [`themes/subway-seat-enamel.json`](themes/subway-seat-enamel.json) | `~/.claude/themes/subway-seat-enamel.json` |
| Subway Seat Enamel | [`plugin/themes/subway-seat-enamel.json`](plugin/themes/subway-seat-enamel.json) |  |
| Subway Seat Enamel | [`themes/subway-seat-enamel-terminal.json`](themes/subway-seat-enamel-terminal.json) | `~/.claude/themes/subway-seat-enamel-terminal.json` |
| Subway Seat Enamel | [`plugin/themes/subway-seat-enamel-terminal.json`](plugin/themes/subway-seat-enamel-terminal.json) |  |
| Subway Seat Enamel | [`plugin/settings/subway-seat-enamel.json`](plugin/settings/subway-seat-enamel.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| All three | [`plugin/.claude-plugin/plugin.json`](plugin/.claude-plugin/plugin.json) |  |
| All three | [`plugin/settings.json`](plugin/settings.json) |  |
| All three | [`plugin/hooks/hooks.json`](plugin/hooks/hooks.json) |  |
| All three | [`plugin/scripts/subway-seat-statusline`](plugin/scripts/subway-seat-statusline) | `~/.claude/subway-seat/subway-seat-statusline` |
| All three | [`plugin/scripts/subway-seat-subagents`](plugin/scripts/subway-seat-subagents) | `~/.claude/subway-seat/subway-seat-subagents` |
| All three | [`plugin/scripts/sync.sh`](plugin/scripts/sync.sh) |  |
| All three | [`plugin/scripts/setup.sh`](plugin/scripts/setup.sh) |  |
| All three | [`plugin/tips.json`](plugin/tips.json) | `~/.claude/subway-seat/tips.json` |
| All three | [`plugin/output-styles/subway-seat.md`](plugin/output-styles/subway-seat.md) | `~/.claude/output-styles/subway-seat.md` |
| All three | [`plugin/skills/setup/SKILL.md`](plugin/skills/setup/SKILL.md) |  |

## Turn it on

**Subway Seat**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Subway Seat
```

**Subway Seat Tunnel**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Subway Seat Tunnel
```

**Subway Seat Enamel**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Subway Seat Enamel
```

## Uninstall

- Delete `~/.claude/themes/subway-seat.json`.
- Delete `~/.claude/themes/subway-seat-terminal.json`.
- Delete `~/.claude/themes/subway-seat-tunnel.json`.
- Delete `~/.claude/themes/subway-seat-tunnel-terminal.json`.
- Delete `~/.claude/themes/subway-seat-enamel.json`.
- Delete `~/.claude/themes/subway-seat-enamel-terminal.json`.
- Delete `~/.claude/subway-seat/subway-seat-statusline`.
- Delete `~/.claude/subway-seat/subway-seat-subagents`.
- Delete `~/.claude/subway-seat/tips.json`.
- Delete `~/.claude/output-styles/subway-seat.md`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
