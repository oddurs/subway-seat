# Subway Seat for eza

Gold directories, avocado executables, sage symlinks, and file sizes that warm up from avocado to red as they grow. LS_COLORS and EZA_COLORS override it; the vivid port sets LS_COLORS to match.

[eza](https://eza.rocks) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/eza/) · Needs eza 0.20+

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only eza
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.yml`](subway-seat.yml) | `~/.config/eza/subway-seat/theme.yml` |
| Subway Seat Tunnel | [`subway-seat-tunnel.yml`](subway-seat-tunnel.yml) | `~/.config/eza/subway-seat-tunnel/theme.yml` |
| Subway Seat Enamel | [`subway-seat-enamel.yml`](subway-seat-enamel.yml) | `~/.config/eza/subway-seat-enamel/theme.yml` |
| London Moquette | [`london-moquette.yml`](london-moquette.yml) | `~/.config/eza/london-moquette/theme.yml` |
| London Deep Level | [`london-deep-level.yml`](london-deep-level.yml) | `~/.config/eza/london-deep-level/theme.yml` |
| London Portland | [`london-portland.yml`](london-portland.yml) | `~/.config/eza/london-portland/theme.yml` |
| Paris Guimard | [`paris-guimard.yml`](paris-guimard.yml) | `~/.config/eza/paris-guimard/theme.yml` |
| Paris Catacombes | [`paris-catacombes.yml`](paris-catacombes.yml) | `~/.config/eza/paris-catacombes/theme.yml` |
| Paris Carrelage | [`paris-carrelage.yml`](paris-carrelage.yml) | `~/.config/eza/paris-carrelage/theme.yml` |

## Turn it on

**Subway Seat**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/subway-seat
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/subway-seat"
```

**Subway Seat Tunnel**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/subway-seat-tunnel
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/subway-seat-tunnel"
```

**Subway Seat Enamel**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/subway-seat-enamel
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/subway-seat-enamel"
```

**London Moquette**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/london-moquette
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/london-moquette"
```

**London Deep Level**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/london-deep-level
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/london-deep-level"
```

**London Portland**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/london-portland
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/london-portland"
```

**Paris Guimard**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/paris-guimard
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/paris-guimard"
```

**Paris Catacombes**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/paris-catacombes
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/paris-catacombes"
```

**Paris Carrelage**, in config.fish (bash and zsh: export it from ~/.bashrc or ~/.zshrc). Each flavor is a theme.yml in its own folder, so switching is changing this one line:

```fish
set -gx EZA_CONFIG_DIR ~/.config/eza/paris-carrelage
```

In bash or zsh:

```sh
export EZA_CONFIG_DIR="$HOME/.config/eza/paris-carrelage"
```

## Uninstall

- Delete `~/.config/eza/subway-seat/theme.yml`.
- Delete `~/.config/eza/subway-seat-tunnel/theme.yml`.
- Delete `~/.config/eza/subway-seat-enamel/theme.yml`.
- Delete `~/.config/eza/london-moquette/theme.yml`.
- Delete `~/.config/eza/london-deep-level/theme.yml`.
- Delete `~/.config/eza/london-portland/theme.yml`.
- Delete `~/.config/eza/paris-guimard/theme.yml`.
- Delete `~/.config/eza/paris-catacombes/theme.yml`.
- Delete `~/.config/eza/paris-carrelage/theme.yml`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
