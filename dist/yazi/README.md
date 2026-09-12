# Subway Seat for Yazi

Yazi flavors with gold directories, an orange mode badge and a gold bar on the hovered file; previews use the bundled tmTheme, and Yazi's file icons are recolored in the palette.

[Yazi](https://yazi-rs.github.io) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/yazi/) · Needs Yazi 25.2+

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only yazi
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.yazi/flavor.toml`](subway-seat.yazi/flavor.toml) | `~/.config/yazi/flavors/subway-seat.yazi/flavor.toml` |
| Subway Seat | [`subway-seat.yazi/tmtheme.xml`](subway-seat.yazi/tmtheme.xml) | `~/.config/yazi/flavors/subway-seat.yazi/tmtheme.xml` |
| Subway Seat Tunnel | [`subway-seat-tunnel.yazi/flavor.toml`](subway-seat-tunnel.yazi/flavor.toml) | `~/.config/yazi/flavors/subway-seat-tunnel.yazi/flavor.toml` |
| Subway Seat Tunnel | [`subway-seat-tunnel.yazi/tmtheme.xml`](subway-seat-tunnel.yazi/tmtheme.xml) | `~/.config/yazi/flavors/subway-seat-tunnel.yazi/tmtheme.xml` |
| Subway Seat Enamel | [`subway-seat-enamel.yazi/flavor.toml`](subway-seat-enamel.yazi/flavor.toml) | `~/.config/yazi/flavors/subway-seat-enamel.yazi/flavor.toml` |
| Subway Seat Enamel | [`subway-seat-enamel.yazi/tmtheme.xml`](subway-seat-enamel.yazi/tmtheme.xml) | `~/.config/yazi/flavors/subway-seat-enamel.yazi/tmtheme.xml` |
| London Moquette | [`london-moquette.yazi/flavor.toml`](london-moquette.yazi/flavor.toml) | `~/.config/yazi/flavors/london-moquette.yazi/flavor.toml` |
| London Moquette | [`london-moquette.yazi/tmtheme.xml`](london-moquette.yazi/tmtheme.xml) | `~/.config/yazi/flavors/london-moquette.yazi/tmtheme.xml` |
| London Deep Level | [`london-deep-level.yazi/flavor.toml`](london-deep-level.yazi/flavor.toml) | `~/.config/yazi/flavors/london-deep-level.yazi/flavor.toml` |
| London Deep Level | [`london-deep-level.yazi/tmtheme.xml`](london-deep-level.yazi/tmtheme.xml) | `~/.config/yazi/flavors/london-deep-level.yazi/tmtheme.xml` |
| London Portland | [`london-portland.yazi/flavor.toml`](london-portland.yazi/flavor.toml) | `~/.config/yazi/flavors/london-portland.yazi/flavor.toml` |
| London Portland | [`london-portland.yazi/tmtheme.xml`](london-portland.yazi/tmtheme.xml) | `~/.config/yazi/flavors/london-portland.yazi/tmtheme.xml` |
| Paris Guimard | [`paris-guimard.yazi/flavor.toml`](paris-guimard.yazi/flavor.toml) | `~/.config/yazi/flavors/paris-guimard.yazi/flavor.toml` |
| Paris Guimard | [`paris-guimard.yazi/tmtheme.xml`](paris-guimard.yazi/tmtheme.xml) | `~/.config/yazi/flavors/paris-guimard.yazi/tmtheme.xml` |
| Paris Catacombes | [`paris-catacombes.yazi/flavor.toml`](paris-catacombes.yazi/flavor.toml) | `~/.config/yazi/flavors/paris-catacombes.yazi/flavor.toml` |
| Paris Catacombes | [`paris-catacombes.yazi/tmtheme.xml`](paris-catacombes.yazi/tmtheme.xml) | `~/.config/yazi/flavors/paris-catacombes.yazi/tmtheme.xml` |
| Paris Carrelage | [`paris-carrelage.yazi/flavor.toml`](paris-carrelage.yazi/flavor.toml) | `~/.config/yazi/flavors/paris-carrelage.yazi/flavor.toml` |
| Paris Carrelage | [`paris-carrelage.yazi/tmtheme.xml`](paris-carrelage.yazi/tmtheme.xml) | `~/.config/yazi/flavors/paris-carrelage.yazi/tmtheme.xml` |

## Turn it on

**Subway Seat**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "subway-seat"
light = "subway-seat"
```

**Subway Seat Tunnel**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "subway-seat-tunnel"
light = "subway-seat-tunnel"
```

**Subway Seat Enamel**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "subway-seat-enamel"
light = "subway-seat-enamel"
```

**London Moquette**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "london-moquette"
light = "london-moquette"
```

**London Deep Level**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "london-deep-level"
light = "london-deep-level"
```

**London Portland**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "london-portland"
light = "london-portland"
```

**Paris Guimard**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "paris-guimard"
light = "paris-guimard"
```

**Paris Catacombes**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "paris-catacombes"
light = "paris-catacombes"
```

**Paris Carrelage**, in ~/.config/yazi/theme.toml:

```toml
[flavor]
dark  = "paris-carrelage"
light = "paris-carrelage"
```

## Follow light and dark

In ~/.config/yazi/theme.toml (Yazi picks by the terminal's background):

```toml
[flavor]
dark  = "subway-seat"
light = "subway-seat-enamel"
```

## Uninstall

- Delete `~/.config/yazi/flavors/subway-seat.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/subway-seat.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/subway-seat-tunnel.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/subway-seat-tunnel.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/subway-seat-enamel.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/subway-seat-enamel.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/london-moquette.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/london-moquette.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/london-deep-level.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/london-deep-level.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/london-portland.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/london-portland.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/paris-guimard.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/paris-guimard.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/paris-catacombes.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/paris-catacombes.yazi/tmtheme.xml`.
- Delete `~/.config/yazi/flavors/paris-carrelage.yazi/flavor.toml`.
- Delete `~/.config/yazi/flavors/paris-carrelage.yazi/tmtheme.xml`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
