# Subway Seat for Hyprland

Window borders, group borders, the groupbar, the shadow and the no-wallpaper background. Hyprland 0.55 moved to Lua: `require` the module for the palette and call `.apply()` for the borders. The `.conf` is the same palette for hyprland.conf on 0.54 and older.

[Hyprland](https://hypr.land) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/hyprland/)

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.lua`](subway-seat.lua) | `~/.config/hypr/themes/subway-seat.lua` |
| Subway Seat | [`subway-seat.conf`](subway-seat.conf) | `~/.config/hypr/subway-seat.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/subway-seat.conf` near the top of hyprland.conf |
| Subway Seat Tunnel | [`subway-seat-tunnel.lua`](subway-seat-tunnel.lua) | `~/.config/hypr/themes/subway-seat-tunnel.lua` |
| Subway Seat Tunnel | [`subway-seat-tunnel.conf`](subway-seat-tunnel.conf) | `~/.config/hypr/subway-seat-tunnel.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/subway-seat-tunnel.conf` near the top of hyprland.conf |
| Subway Seat Enamel | [`subway-seat-enamel.lua`](subway-seat-enamel.lua) | `~/.config/hypr/themes/subway-seat-enamel.lua` |
| Subway Seat Enamel | [`subway-seat-enamel.conf`](subway-seat-enamel.conf) | `~/.config/hypr/subway-seat-enamel.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/subway-seat-enamel.conf` near the top of hyprland.conf |
| London Moquette | [`london-moquette.lua`](london-moquette.lua) | `~/.config/hypr/themes/london-moquette.lua` |
| London Moquette | [`london-moquette.conf`](london-moquette.conf) | `~/.config/hypr/london-moquette.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/london-moquette.conf` near the top of hyprland.conf |
| London Deep Level | [`london-deep-level.lua`](london-deep-level.lua) | `~/.config/hypr/themes/london-deep-level.lua` |
| London Deep Level | [`london-deep-level.conf`](london-deep-level.conf) | `~/.config/hypr/london-deep-level.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/london-deep-level.conf` near the top of hyprland.conf |
| London Portland | [`london-portland.lua`](london-portland.lua) | `~/.config/hypr/themes/london-portland.lua` |
| London Portland | [`london-portland.conf`](london-portland.conf) | `~/.config/hypr/london-portland.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/london-portland.conf` near the top of hyprland.conf |
| Paris Guimard | [`paris-guimard.lua`](paris-guimard.lua) | `~/.config/hypr/themes/paris-guimard.lua` |
| Paris Guimard | [`paris-guimard.conf`](paris-guimard.conf) | `~/.config/hypr/paris-guimard.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/paris-guimard.conf` near the top of hyprland.conf |
| Paris Catacombes | [`paris-catacombes.lua`](paris-catacombes.lua) | `~/.config/hypr/themes/paris-catacombes.lua` |
| Paris Catacombes | [`paris-catacombes.conf`](paris-catacombes.conf) | `~/.config/hypr/paris-catacombes.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/paris-catacombes.conf` near the top of hyprland.conf |
| Paris Carrelage | [`paris-carrelage.lua`](paris-carrelage.lua) | `~/.config/hypr/themes/paris-carrelage.lua` |
| Paris Carrelage | [`paris-carrelage.conf`](paris-carrelage.conf) | `~/.config/hypr/paris-carrelage.conf`; Hyprland 0.54 or older: add `source = ~/.config/hypr/paris-carrelage.conf` near the top of hyprland.conf |

## Turn it on

**Subway Seat**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.subway-seat").apply()
```

**Subway Seat Tunnel**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.subway-seat-tunnel").apply()
```

**Subway Seat Enamel**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.subway-seat-enamel").apply()
```

**London Moquette**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.london-moquette").apply()
```

**London Deep Level**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.london-deep-level").apply()
```

**London Portland**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.london-portland").apply()
```

**Paris Guimard**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.paris-guimard").apply()
```

**Paris Catacombes**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.paris-catacombes").apply()
```

**Paris Carrelage**, in ~/.config/hypr/hyprland.lua (Hyprland 0.55+):

```lua
require("themes.paris-carrelage").apply()
```

## Uninstall

- Delete `~/.config/hypr/themes/subway-seat.lua`.
- Delete `~/.config/hypr/subway-seat.conf`.
- Delete `~/.config/hypr/themes/subway-seat-tunnel.lua`.
- Delete `~/.config/hypr/subway-seat-tunnel.conf`.
- Delete `~/.config/hypr/themes/subway-seat-enamel.lua`.
- Delete `~/.config/hypr/subway-seat-enamel.conf`.
- Delete `~/.config/hypr/themes/london-moquette.lua`.
- Delete `~/.config/hypr/london-moquette.conf`.
- Delete `~/.config/hypr/themes/london-deep-level.lua`.
- Delete `~/.config/hypr/london-deep-level.conf`.
- Delete `~/.config/hypr/themes/london-portland.lua`.
- Delete `~/.config/hypr/london-portland.conf`.
- Delete `~/.config/hypr/themes/paris-guimard.lua`.
- Delete `~/.config/hypr/paris-guimard.conf`.
- Delete `~/.config/hypr/themes/paris-catacombes.lua`.
- Delete `~/.config/hypr/paris-catacombes.conf`.
- Delete `~/.config/hypr/themes/paris-carrelage.lua`.
- Delete `~/.config/hypr/paris-carrelage.conf`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
