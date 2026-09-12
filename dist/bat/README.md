# Subway Seat for bat

TextMate themes for bat. delta (through the delta port), aichat and anything else built on syntect can use them too.

[bat](https://github.com/sharkdp/bat) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/bat/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only bat
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`Subway Seat.tmTheme`](Subway%20Seat.tmTheme) | `~/.config/bat/themes/Subway Seat.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| Subway Seat Tunnel | [`Subway Seat Tunnel.tmTheme`](Subway%20Seat%20Tunnel.tmTheme) | `~/.config/bat/themes/Subway Seat Tunnel.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| Subway Seat Enamel | [`Subway Seat Enamel.tmTheme`](Subway%20Seat%20Enamel.tmTheme) | `~/.config/bat/themes/Subway Seat Enamel.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| London Moquette | [`London Moquette.tmTheme`](London%20Moquette.tmTheme) | `~/.config/bat/themes/London Moquette.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| London Deep Level | [`London Deep Level.tmTheme`](London%20Deep%20Level.tmTheme) | `~/.config/bat/themes/London Deep Level.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| London Portland | [`London Portland.tmTheme`](London%20Portland.tmTheme) | `~/.config/bat/themes/London Portland.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| Paris Guimard | [`Paris Guimard.tmTheme`](Paris%20Guimard.tmTheme) | `~/.config/bat/themes/Paris Guimard.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| Paris Catacombes | [`Paris Catacombes.tmTheme`](Paris%20Catacombes.tmTheme) | `~/.config/bat/themes/Paris Catacombes.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |
| Paris Carrelage | [`Paris Carrelage.tmTheme`](Paris%20Carrelage.tmTheme) | `~/.config/bat/themes/Paris Carrelage.tmTheme`; then run `bat cache --build` (on Windows the folder is %APPDATA%\bat\themes) |

## Turn it on

**Subway Seat**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Subway Seat"
```

In bash or zsh:

```sh
export BAT_THEME="Subway Seat"
```

**Subway Seat Tunnel**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Subway Seat Tunnel"
```

In bash or zsh:

```sh
export BAT_THEME="Subway Seat Tunnel"
```

**Subway Seat Enamel**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Subway Seat Enamel"
```

In bash or zsh:

```sh
export BAT_THEME="Subway Seat Enamel"
```

**London Moquette**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "London Moquette"
```

In bash or zsh:

```sh
export BAT_THEME="London Moquette"
```

**London Deep Level**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "London Deep Level"
```

In bash or zsh:

```sh
export BAT_THEME="London Deep Level"
```

**London Portland**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "London Portland"
```

In bash or zsh:

```sh
export BAT_THEME="London Portland"
```

**Paris Guimard**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Paris Guimard"
```

In bash or zsh:

```sh
export BAT_THEME="Paris Guimard"
```

**Paris Catacombes**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Paris Catacombes"
```

In bash or zsh:

```sh
export BAT_THEME="Paris Catacombes"
```

**Paris Carrelage**, in config.fish (bash and zsh: ~/.bashrc or ~/.zshrc), after copying the themes to `$(bat --config-dir)/themes` and running `bat cache --build`:

```fish
set -gx BAT_THEME "Paris Carrelage"
```

In bash or zsh:

```sh
export BAT_THEME="Paris Carrelage"
```

## Follow light and dark

In config.fish, with BAT_THEME left unset (bat 0.25+ asks the terminal which to use):

```fish
set -gx BAT_THEME_DARK "Subway Seat"
set -gx BAT_THEME_LIGHT "Subway Seat Enamel"
```

## Uninstall

- Delete `~/.config/bat/themes/Subway Seat.tmTheme`.
- Delete `~/.config/bat/themes/Subway Seat Tunnel.tmTheme`.
- Delete `~/.config/bat/themes/Subway Seat Enamel.tmTheme`.
- Delete `~/.config/bat/themes/London Moquette.tmTheme`.
- Delete `~/.config/bat/themes/London Deep Level.tmTheme`.
- Delete `~/.config/bat/themes/London Portland.tmTheme`.
- Delete `~/.config/bat/themes/Paris Guimard.tmTheme`.
- Delete `~/.config/bat/themes/Paris Catacombes.tmTheme`.
- Delete `~/.config/bat/themes/Paris Carrelage.tmTheme`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
