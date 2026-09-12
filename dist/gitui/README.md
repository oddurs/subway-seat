# Subway Seat for gitui

Orange titles on the focused panel, avocado added and redbird removed lines that keep their color when selected, gold commit hashes. The file viewer's syntax colors come from the tmTheme next to it.

[gitui](https://github.com/gitui-org/gitui) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/gitui/) · Needs gitui 0.28+

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only gitui
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.ron`](subway-seat.ron) | `~/.config/gitui/subway-seat.ron` |
| Subway Seat | [`subway-seat.tmTheme`](subway-seat.tmTheme) | `~/.config/gitui/subway-seat.tmTheme` |
| Subway Seat Tunnel | [`subway-seat-tunnel.ron`](subway-seat-tunnel.ron) | `~/.config/gitui/subway-seat-tunnel.ron` |
| Subway Seat Tunnel | [`subway-seat-tunnel.tmTheme`](subway-seat-tunnel.tmTheme) | `~/.config/gitui/subway-seat-tunnel.tmTheme` |
| Subway Seat Enamel | [`subway-seat-enamel.ron`](subway-seat-enamel.ron) | `~/.config/gitui/subway-seat-enamel.ron` |
| Subway Seat Enamel | [`subway-seat-enamel.tmTheme`](subway-seat-enamel.tmTheme) | `~/.config/gitui/subway-seat-enamel.tmTheme` |
| London Moquette | [`london-moquette.ron`](london-moquette.ron) | `~/.config/gitui/london-moquette.ron` |
| London Moquette | [`london-moquette.tmTheme`](london-moquette.tmTheme) | `~/.config/gitui/london-moquette.tmTheme` |
| London Deep Level | [`london-deep-level.ron`](london-deep-level.ron) | `~/.config/gitui/london-deep-level.ron` |
| London Deep Level | [`london-deep-level.tmTheme`](london-deep-level.tmTheme) | `~/.config/gitui/london-deep-level.tmTheme` |
| London Portland | [`london-portland.ron`](london-portland.ron) | `~/.config/gitui/london-portland.ron` |
| London Portland | [`london-portland.tmTheme`](london-portland.tmTheme) | `~/.config/gitui/london-portland.tmTheme` |
| Paris Guimard | [`paris-guimard.ron`](paris-guimard.ron) | `~/.config/gitui/paris-guimard.ron` |
| Paris Guimard | [`paris-guimard.tmTheme`](paris-guimard.tmTheme) | `~/.config/gitui/paris-guimard.tmTheme` |
| Paris Catacombes | [`paris-catacombes.ron`](paris-catacombes.ron) | `~/.config/gitui/paris-catacombes.ron` |
| Paris Catacombes | [`paris-catacombes.tmTheme`](paris-catacombes.tmTheme) | `~/.config/gitui/paris-catacombes.tmTheme` |
| Paris Carrelage | [`paris-carrelage.ron`](paris-carrelage.ron) | `~/.config/gitui/paris-carrelage.ron` |
| Paris Carrelage | [`paris-carrelage.tmTheme`](paris-carrelage.tmTheme) | `~/.config/gitui/paris-carrelage.tmTheme` |

## Turn it on

**Subway Seat**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t subway-seat.ron
```

**Subway Seat Tunnel**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t subway-seat-tunnel.ron
```

**Subway Seat Enamel**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t subway-seat-enamel.ron
```

**London Moquette**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t london-moquette.ron
```

**London Deep Level**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t london-deep-level.ron
```

**London Portland**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t london-portland.ron
```

**Paris Guimard**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t paris-guimard.ron
```

**Paris Catacombes**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t paris-catacombes.ron
```

**Paris Carrelage**, in the command line, with both files in ~/.config/gitui/ (or save the .ron as theme.ron):

```sh
gitui -t paris-carrelage.ron
```

## Uninstall

- Delete `~/.config/gitui/subway-seat.ron`.
- Delete `~/.config/gitui/subway-seat.tmTheme`.
- Delete `~/.config/gitui/subway-seat-tunnel.ron`.
- Delete `~/.config/gitui/subway-seat-tunnel.tmTheme`.
- Delete `~/.config/gitui/subway-seat-enamel.ron`.
- Delete `~/.config/gitui/subway-seat-enamel.tmTheme`.
- Delete `~/.config/gitui/london-moquette.ron`.
- Delete `~/.config/gitui/london-moquette.tmTheme`.
- Delete `~/.config/gitui/london-deep-level.ron`.
- Delete `~/.config/gitui/london-deep-level.tmTheme`.
- Delete `~/.config/gitui/london-portland.ron`.
- Delete `~/.config/gitui/london-portland.tmTheme`.
- Delete `~/.config/gitui/paris-guimard.ron`.
- Delete `~/.config/gitui/paris-guimard.tmTheme`.
- Delete `~/.config/gitui/paris-catacombes.ron`.
- Delete `~/.config/gitui/paris-catacombes.tmTheme`.
- Delete `~/.config/gitui/paris-carrelage.ron`.
- Delete `~/.config/gitui/paris-carrelage.tmTheme`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
