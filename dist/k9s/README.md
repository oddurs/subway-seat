# Subway Seat for k9s

Gold breadcrumbs with the current view in orange, like a line of station signs, and resource states in avocado, gold, orange and red.

[k9s](https://k9scli.io) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/k9s/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only k9s
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.yaml`](subway-seat.yaml) | `~/Library/Application Support/k9s/skins/subway-seat.yaml`; on Linux the folder is ~/.config/k9s/skins |
| Subway Seat Tunnel | [`subway-seat-tunnel.yaml`](subway-seat-tunnel.yaml) | `~/Library/Application Support/k9s/skins/subway-seat-tunnel.yaml`; on Linux the folder is ~/.config/k9s/skins |
| Subway Seat Enamel | [`subway-seat-enamel.yaml`](subway-seat-enamel.yaml) | `~/Library/Application Support/k9s/skins/subway-seat-enamel.yaml`; on Linux the folder is ~/.config/k9s/skins |
| London Moquette | [`london-moquette.yaml`](london-moquette.yaml) | `~/Library/Application Support/k9s/skins/london-moquette.yaml`; on Linux the folder is ~/.config/k9s/skins |
| London Deep Level | [`london-deep-level.yaml`](london-deep-level.yaml) | `~/Library/Application Support/k9s/skins/london-deep-level.yaml`; on Linux the folder is ~/.config/k9s/skins |
| London Portland | [`london-portland.yaml`](london-portland.yaml) | `~/Library/Application Support/k9s/skins/london-portland.yaml`; on Linux the folder is ~/.config/k9s/skins |
| Paris Guimard | [`paris-guimard.yaml`](paris-guimard.yaml) | `~/Library/Application Support/k9s/skins/paris-guimard.yaml`; on Linux the folder is ~/.config/k9s/skins |
| Paris Catacombes | [`paris-catacombes.yaml`](paris-catacombes.yaml) | `~/Library/Application Support/k9s/skins/paris-catacombes.yaml`; on Linux the folder is ~/.config/k9s/skins |
| Paris Carrelage | [`paris-carrelage.yaml`](paris-carrelage.yaml) | `~/Library/Application Support/k9s/skins/paris-carrelage.yaml`; on Linux the folder is ~/.config/k9s/skins |

## Turn it on

**Subway Seat**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: subway-seat
```

**Subway Seat Tunnel**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: subway-seat-tunnel
```

**Subway Seat Enamel**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: subway-seat-enamel
```

**London Moquette**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: london-moquette
```

**London Deep Level**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: london-deep-level
```

**London Portland**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: london-portland
```

**Paris Guimard**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: paris-guimard
```

**Paris Catacombes**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: paris-catacombes
```

**Paris Carrelage**, in k9s config.yaml, with the skin in the skins/ folder beside it (`k9s info` shows both: ~/Library/Application Support/k9s on macOS, ~/.config/k9s on Linux or with XDG_CONFIG_HOME set):

```yaml
k9s:
  ui:
    skin: paris-carrelage
```

## Uninstall

- Delete `~/Library/Application Support/k9s/skins/subway-seat.yaml`.
- Delete `~/Library/Application Support/k9s/skins/subway-seat-tunnel.yaml`.
- Delete `~/Library/Application Support/k9s/skins/subway-seat-enamel.yaml`.
- Delete `~/Library/Application Support/k9s/skins/london-moquette.yaml`.
- Delete `~/Library/Application Support/k9s/skins/london-deep-level.yaml`.
- Delete `~/Library/Application Support/k9s/skins/london-portland.yaml`.
- Delete `~/Library/Application Support/k9s/skins/paris-guimard.yaml`.
- Delete `~/Library/Application Support/k9s/skins/paris-catacombes.yaml`.
- Delete `~/Library/Application Support/k9s/skins/paris-carrelage.yaml`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
