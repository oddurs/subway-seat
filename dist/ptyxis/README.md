# Subway Seat for Ptyxis

The 16 colors, cursor, header bar, bell flash, and the header tints for root and SSH sessions, in a light and a dark face. Ptyxis switches faces with its style; from Ptyxis 49 that style is dark until you choose Follow System Style. The Flatpak reads palettes from `~/.var/app/app.devsuite.Ptyxis/data/app.devsuite.Ptyxis/palettes/`. The cursor text color needs Ptyxis 50.

[Ptyxis](https://gitlab.gnome.org/GNOME/ptyxis) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/ptyxis/) · Needs Ptyxis 46+

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.palette`](subway-seat.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat.palette` |
| Subway Seat Tunnel | [`subway-seat-tunnel.palette`](subway-seat-tunnel.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat-tunnel.palette` |
| Subway Seat Enamel | [`subway-seat-enamel.palette`](subway-seat-enamel.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat-enamel.palette` |
| London Moquette | [`london-moquette.palette`](london-moquette.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/london-moquette.palette` |
| London Deep Level | [`london-deep-level.palette`](london-deep-level.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/london-deep-level.palette` |
| London Portland | [`london-portland.palette`](london-portland.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/london-portland.palette` |
| Paris Guimard | [`paris-guimard.palette`](paris-guimard.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/paris-guimard.palette` |
| Paris Catacombes | [`paris-catacombes.palette`](paris-catacombes.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/paris-catacombes.palette` |
| Paris Carrelage | [`paris-carrelage.palette`](paris-carrelage.palette) | `~/.local/share/org.gnome.Ptyxis/palettes/paris-carrelage.palette` |

## Turn it on

**Subway Seat**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'subway-seat'
```

**Subway Seat Tunnel**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'subway-seat-tunnel'
```

**Subway Seat Enamel**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'subway-seat-enamel'
```

**London Moquette**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'london-moquette'
```

**London Deep Level**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'london-deep-level'
```

**London Portland**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'london-portland'
```

**Paris Guimard**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'paris-guimard'
```

**Paris Catacombes**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'paris-catacombes'
```

**Paris Carrelage**, in Preferences › Profiles › your profile › Color Palette (under Show All), or a shell:

```sh
uuid=$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$uuid/" palette 'paris-carrelage'
```

## Follow light and dark

In the main menu's style buttons (Follow System Style), or a shell:

```sh
gsettings set org.gnome.Ptyxis interface-style 'system'
```

## Uninstall

- Delete `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat-tunnel.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/subway-seat-enamel.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/london-moquette.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/london-deep-level.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/london-portland.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/paris-guimard.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/paris-catacombes.palette`.
- Delete `~/.local/share/org.gnome.Ptyxis/palettes/paris-carrelage.palette`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
