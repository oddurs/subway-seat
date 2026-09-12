# Subway Seat for Gemini CLI

A custom theme file per flavor, the same theme as a `ui.customThemes` settings block, and an extension with all three (`gemini extensions install <folder>`; they show up in /theme as “Subway Seat (subway-seat)”). Gemini ties string color to its warning color, so strings are harvest gold here instead of avocado.

[Gemini CLI](https://github.com/google-gemini/gemini-cli) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/gemini-cli/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only gemini-cli
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.json`](subway-seat.json) | `~/.gemini/themes/subway-seat.json` |
| Subway Seat | [`settings/subway-seat.json`](settings/subway-seat.json) | merge into ~/.gemini/settings.json |
| Subway Seat Tunnel | [`subway-seat-tunnel.json`](subway-seat-tunnel.json) | `~/.gemini/themes/subway-seat-tunnel.json` |
| Subway Seat Tunnel | [`settings/subway-seat-tunnel.json`](settings/subway-seat-tunnel.json) | merge into ~/.gemini/settings.json |
| Subway Seat Enamel | [`subway-seat-enamel.json`](subway-seat-enamel.json) | `~/.gemini/themes/subway-seat-enamel.json` |
| Subway Seat Enamel | [`settings/subway-seat-enamel.json`](settings/subway-seat-enamel.json) | merge into ~/.gemini/settings.json |
| London Moquette | [`london-moquette.json`](london-moquette.json) | `~/.gemini/themes/london-moquette.json` |
| London Moquette | [`settings/london-moquette.json`](settings/london-moquette.json) | merge into ~/.gemini/settings.json |
| London Deep Level | [`london-deep-level.json`](london-deep-level.json) | `~/.gemini/themes/london-deep-level.json` |
| London Deep Level | [`settings/london-deep-level.json`](settings/london-deep-level.json) | merge into ~/.gemini/settings.json |
| London Portland | [`london-portland.json`](london-portland.json) | `~/.gemini/themes/london-portland.json` |
| London Portland | [`settings/london-portland.json`](settings/london-portland.json) | merge into ~/.gemini/settings.json |
| Paris Guimard | [`paris-guimard.json`](paris-guimard.json) | `~/.gemini/themes/paris-guimard.json` |
| Paris Guimard | [`settings/paris-guimard.json`](settings/paris-guimard.json) | merge into ~/.gemini/settings.json |
| Paris Catacombes | [`paris-catacombes.json`](paris-catacombes.json) | `~/.gemini/themes/paris-catacombes.json` |
| Paris Catacombes | [`settings/paris-catacombes.json`](settings/paris-catacombes.json) | merge into ~/.gemini/settings.json |
| Paris Carrelage | [`paris-carrelage.json`](paris-carrelage.json) | `~/.gemini/themes/paris-carrelage.json` |
| Paris Carrelage | [`settings/paris-carrelage.json`](settings/paris-carrelage.json) | merge into ~/.gemini/settings.json |
| All three | [`extension/gemini-extension.json`](extension/gemini-extension.json) | gemini extensions install ./extension (from this folder), then pick a flavor with /theme |

## Turn it on

**Subway Seat**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/subway-seat.json" }
}
```

**Subway Seat Tunnel**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/subway-seat-tunnel.json" }
}
```

**Subway Seat Enamel**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/subway-seat-enamel.json" }
}
```

**London Moquette**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/london-moquette.json" }
}
```

**London Deep Level**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/london-deep-level.json" }
}
```

**London Portland**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/london-portland.json" }
}
```

**Paris Guimard**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/paris-guimard.json" }
}
```

**Paris Catacombes**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/paris-catacombes.json" }
}
```

**Paris Carrelage**, in ~/.gemini/settings.json, after copying the theme to ~/.gemini/themes/ (it must live under your home directory):

```json
{
  "ui": { "theme": "$HOME/.gemini/themes/paris-carrelage.json" }
}
```

## Uninstall

- Delete `~/.gemini/themes/subway-seat.json`.
- Delete `~/.gemini/themes/subway-seat-tunnel.json`.
- Delete `~/.gemini/themes/subway-seat-enamel.json`.
- Delete `~/.gemini/themes/london-moquette.json`.
- Delete `~/.gemini/themes/london-deep-level.json`.
- Delete `~/.gemini/themes/london-portland.json`.
- Delete `~/.gemini/themes/paris-guimard.json`.
- Delete `~/.gemini/themes/paris-catacombes.json`.
- Delete `~/.gemini/themes/paris-carrelage.json`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
