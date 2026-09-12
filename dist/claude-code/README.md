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
| London Moquette | [`themes/london-moquette.json`](themes/london-moquette.json) | `~/.claude/themes/london-moquette.json` |
| London Moquette | [`plugin/themes/london-moquette.json`](plugin/themes/london-moquette.json) |  |
| London Moquette | [`themes/london-moquette-terminal.json`](themes/london-moquette-terminal.json) | `~/.claude/themes/london-moquette-terminal.json` |
| London Moquette | [`plugin/themes/london-moquette-terminal.json`](plugin/themes/london-moquette-terminal.json) |  |
| London Moquette | [`plugin/settings/london-moquette.json`](plugin/settings/london-moquette.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| London Deep Level | [`themes/london-deep-level.json`](themes/london-deep-level.json) | `~/.claude/themes/london-deep-level.json` |
| London Deep Level | [`plugin/themes/london-deep-level.json`](plugin/themes/london-deep-level.json) |  |
| London Deep Level | [`themes/london-deep-level-terminal.json`](themes/london-deep-level-terminal.json) | `~/.claude/themes/london-deep-level-terminal.json` |
| London Deep Level | [`plugin/themes/london-deep-level-terminal.json`](plugin/themes/london-deep-level-terminal.json) |  |
| London Deep Level | [`plugin/settings/london-deep-level.json`](plugin/settings/london-deep-level.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| London Portland | [`themes/london-portland.json`](themes/london-portland.json) | `~/.claude/themes/london-portland.json` |
| London Portland | [`plugin/themes/london-portland.json`](plugin/themes/london-portland.json) |  |
| London Portland | [`themes/london-portland-terminal.json`](themes/london-portland-terminal.json) | `~/.claude/themes/london-portland-terminal.json` |
| London Portland | [`plugin/themes/london-portland-terminal.json`](plugin/themes/london-portland-terminal.json) |  |
| London Portland | [`plugin/settings/london-portland.json`](plugin/settings/london-portland.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| Paris Guimard | [`themes/paris-guimard.json`](themes/paris-guimard.json) | `~/.claude/themes/paris-guimard.json` |
| Paris Guimard | [`plugin/themes/paris-guimard.json`](plugin/themes/paris-guimard.json) |  |
| Paris Guimard | [`themes/paris-guimard-terminal.json`](themes/paris-guimard-terminal.json) | `~/.claude/themes/paris-guimard-terminal.json` |
| Paris Guimard | [`plugin/themes/paris-guimard-terminal.json`](plugin/themes/paris-guimard-terminal.json) |  |
| Paris Guimard | [`plugin/settings/paris-guimard.json`](plugin/settings/paris-guimard.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| Paris Catacombes | [`themes/paris-catacombes.json`](themes/paris-catacombes.json) | `~/.claude/themes/paris-catacombes.json` |
| Paris Catacombes | [`plugin/themes/paris-catacombes.json`](plugin/themes/paris-catacombes.json) |  |
| Paris Catacombes | [`themes/paris-catacombes-terminal.json`](themes/paris-catacombes-terminal.json) | `~/.claude/themes/paris-catacombes-terminal.json` |
| Paris Catacombes | [`plugin/themes/paris-catacombes-terminal.json`](plugin/themes/paris-catacombes-terminal.json) |  |
| Paris Catacombes | [`plugin/settings/paris-catacombes.json`](plugin/settings/paris-catacombes.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
| Paris Carrelage | [`themes/paris-carrelage.json`](themes/paris-carrelage.json) | `~/.claude/themes/paris-carrelage.json` |
| Paris Carrelage | [`plugin/themes/paris-carrelage.json`](plugin/themes/paris-carrelage.json) |  |
| Paris Carrelage | [`themes/paris-carrelage-terminal.json`](themes/paris-carrelage-terminal.json) | `~/.claude/themes/paris-carrelage-terminal.json` |
| Paris Carrelage | [`plugin/themes/paris-carrelage-terminal.json`](plugin/themes/paris-carrelage-terminal.json) |  |
| Paris Carrelage | [`plugin/settings/paris-carrelage.json`](plugin/settings/paris-carrelage.json) | merged into ~/.claude/settings.json by /subway-seat:setup |
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

**London Moquette**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick London Moquette
```

**London Deep Level**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick London Deep Level
```

**London Portland**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick London Portland
```

**Paris Guimard**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Paris Guimard
```

**Paris Catacombes**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Paris Catacombes
```

**Paris Carrelage**, in Claude Code, from the Subway Seat marketplace:

```text
/plugin marketplace add oddurs/subway-seat
/plugin install subway-seat@subway-seat
/subway-seat:setup   # and pick Paris Carrelage
```

## Uninstall

- Delete `~/.claude/themes/subway-seat.json`.
- Delete `~/.claude/themes/subway-seat-terminal.json`.
- Delete `~/.claude/themes/subway-seat-tunnel.json`.
- Delete `~/.claude/themes/subway-seat-tunnel-terminal.json`.
- Delete `~/.claude/themes/subway-seat-enamel.json`.
- Delete `~/.claude/themes/subway-seat-enamel-terminal.json`.
- Delete `~/.claude/themes/london-moquette.json`.
- Delete `~/.claude/themes/london-moquette-terminal.json`.
- Delete `~/.claude/themes/london-deep-level.json`.
- Delete `~/.claude/themes/london-deep-level-terminal.json`.
- Delete `~/.claude/themes/london-portland.json`.
- Delete `~/.claude/themes/london-portland-terminal.json`.
- Delete `~/.claude/themes/paris-guimard.json`.
- Delete `~/.claude/themes/paris-guimard-terminal.json`.
- Delete `~/.claude/themes/paris-catacombes.json`.
- Delete `~/.claude/themes/paris-catacombes-terminal.json`.
- Delete `~/.claude/themes/paris-carrelage.json`.
- Delete `~/.claude/themes/paris-carrelage-terminal.json`.
- Delete `~/.claude/subway-seat/subway-seat-statusline`.
- Delete `~/.claude/subway-seat/subway-seat-subagents`.
- Delete `~/.claude/subway-seat/tips.json`.
- Delete `~/.claude/output-styles/subway-seat.md`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
