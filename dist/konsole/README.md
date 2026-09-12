# Subway Seat for Konsole

Background, foreground and the eight colors, each with intense (bright) and faint variants; the profile adds the cursor, focus border and tab activity colors. To keep your own profile instead, set `ColorScheme=subway-seat` (or `-tunnel`, `-enamel`) under its `[Appearance]`. Konsole doesn't follow the system light/dark setting, so pick one flavor.

[Konsole](https://apps.kde.org/konsole/) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/konsole/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only konsole
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.colorscheme`](subway-seat.colorscheme) | `~/.local/share/konsole/subway-seat.colorscheme` |
| Subway Seat | [`Subway Seat.profile`](Subway%20Seat.profile) | `~/.local/share/konsole/Subway Seat.profile` |
| Subway Seat Tunnel | [`subway-seat-tunnel.colorscheme`](subway-seat-tunnel.colorscheme) | `~/.local/share/konsole/subway-seat-tunnel.colorscheme` |
| Subway Seat Tunnel | [`Subway Seat Tunnel.profile`](Subway%20Seat%20Tunnel.profile) | `~/.local/share/konsole/Subway Seat Tunnel.profile` |
| Subway Seat Enamel | [`subway-seat-enamel.colorscheme`](subway-seat-enamel.colorscheme) | `~/.local/share/konsole/subway-seat-enamel.colorscheme` |
| Subway Seat Enamel | [`Subway Seat Enamel.profile`](Subway%20Seat%20Enamel.profile) | `~/.local/share/konsole/Subway Seat Enamel.profile` |
| London Moquette | [`london-moquette.colorscheme`](london-moquette.colorscheme) | `~/.local/share/konsole/london-moquette.colorscheme` |
| London Moquette | [`London Moquette.profile`](London%20Moquette.profile) | `~/.local/share/konsole/London Moquette.profile` |
| London Deep Level | [`london-deep-level.colorscheme`](london-deep-level.colorscheme) | `~/.local/share/konsole/london-deep-level.colorscheme` |
| London Deep Level | [`London Deep Level.profile`](London%20Deep%20Level.profile) | `~/.local/share/konsole/London Deep Level.profile` |
| London Portland | [`london-portland.colorscheme`](london-portland.colorscheme) | `~/.local/share/konsole/london-portland.colorscheme` |
| London Portland | [`London Portland.profile`](London%20Portland.profile) | `~/.local/share/konsole/London Portland.profile` |
| Paris Guimard | [`paris-guimard.colorscheme`](paris-guimard.colorscheme) | `~/.local/share/konsole/paris-guimard.colorscheme` |
| Paris Guimard | [`Paris Guimard.profile`](Paris%20Guimard.profile) | `~/.local/share/konsole/Paris Guimard.profile` |
| Paris Catacombes | [`paris-catacombes.colorscheme`](paris-catacombes.colorscheme) | `~/.local/share/konsole/paris-catacombes.colorscheme` |
| Paris Catacombes | [`Paris Catacombes.profile`](Paris%20Catacombes.profile) | `~/.local/share/konsole/Paris Catacombes.profile` |
| Paris Carrelage | [`paris-carrelage.colorscheme`](paris-carrelage.colorscheme) | `~/.local/share/konsole/paris-carrelage.colorscheme` |
| Paris Carrelage | [`Paris Carrelage.profile`](Paris%20Carrelage.profile) | `~/.local/share/konsole/Paris Carrelage.profile` |

## Turn it on

**Subway Seat**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Subway Seat.profile
```

**Subway Seat Tunnel**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Subway Seat Tunnel.profile
```

**Subway Seat Enamel**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Subway Seat Enamel.profile
```

**London Moquette**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=London Moquette.profile
```

**London Deep Level**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=London Deep Level.profile
```

**London Portland**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=London Portland.profile
```

**Paris Guimard**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Paris Guimard.profile
```

**Paris Catacombes**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Paris Catacombes.profile
```

**Paris Carrelage**, in ~/.config/konsolerc, or Settings › Configure Konsole › Profiles › Set as Default:

```ini
[Desktop Entry]
DefaultProfile=Paris Carrelage.profile
```

## Uninstall

- Delete `~/.local/share/konsole/subway-seat.colorscheme`.
- Delete `~/.local/share/konsole/Subway Seat.profile`.
- Delete `~/.local/share/konsole/subway-seat-tunnel.colorscheme`.
- Delete `~/.local/share/konsole/Subway Seat Tunnel.profile`.
- Delete `~/.local/share/konsole/subway-seat-enamel.colorscheme`.
- Delete `~/.local/share/konsole/Subway Seat Enamel.profile`.
- Delete `~/.local/share/konsole/london-moquette.colorscheme`.
- Delete `~/.local/share/konsole/London Moquette.profile`.
- Delete `~/.local/share/konsole/london-deep-level.colorscheme`.
- Delete `~/.local/share/konsole/London Deep Level.profile`.
- Delete `~/.local/share/konsole/london-portland.colorscheme`.
- Delete `~/.local/share/konsole/London Portland.profile`.
- Delete `~/.local/share/konsole/paris-guimard.colorscheme`.
- Delete `~/.local/share/konsole/Paris Guimard.profile`.
- Delete `~/.local/share/konsole/paris-catacombes.colorscheme`.
- Delete `~/.local/share/konsole/Paris Catacombes.profile`.
- Delete `~/.local/share/konsole/paris-carrelage.colorscheme`.
- Delete `~/.local/share/konsole/Paris Carrelage.profile`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
