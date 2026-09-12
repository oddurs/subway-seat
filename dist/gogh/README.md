# Subway Seat for Gogh

Gogh themes: the 16 ANSI colors, background, foreground and cursor. installs/ has Gogh's install script for each flavor, which applies it to GNOME Terminal, Tilix, Xfce Terminal, Konsole, Alacritty and the other terminals Gogh supports (set TERMINAL). The YAML is Gogh's theme source and the JSON matches its data/json files.

[Gogh](https://github.com/Gogh-Co/Gogh) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/gogh/)

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`installs/subway-seat.sh`](installs/subway-seat.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Subway Seat | [`Subway Seat.yml`](Subway%20Seat.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Subway Seat | [`subway-seat.json`](subway-seat.json) | the same theme in the form of Gogh's data/json files |
| Subway Seat Tunnel | [`installs/subway-seat-tunnel.sh`](installs/subway-seat-tunnel.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Subway Seat Tunnel | [`Subway Seat Tunnel.yml`](Subway%20Seat%20Tunnel.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Subway Seat Tunnel | [`subway-seat-tunnel.json`](subway-seat-tunnel.json) | the same theme in the form of Gogh's data/json files |
| Subway Seat Enamel | [`installs/subway-seat-enamel.sh`](installs/subway-seat-enamel.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Subway Seat Enamel | [`Subway Seat Enamel.yml`](Subway%20Seat%20Enamel.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Subway Seat Enamel | [`subway-seat-enamel.json`](subway-seat-enamel.json) | the same theme in the form of Gogh's data/json files |
| London Moquette | [`installs/london-moquette.sh`](installs/london-moquette.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| London Moquette | [`London Moquette.yml`](London%20Moquette.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| London Moquette | [`london-moquette.json`](london-moquette.json) | the same theme in the form of Gogh's data/json files |
| London Deep Level | [`installs/london-deep-level.sh`](installs/london-deep-level.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| London Deep Level | [`London Deep Level.yml`](London%20Deep%20Level.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| London Deep Level | [`london-deep-level.json`](london-deep-level.json) | the same theme in the form of Gogh's data/json files |
| London Portland | [`installs/london-portland.sh`](installs/london-portland.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| London Portland | [`London Portland.yml`](London%20Portland.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| London Portland | [`london-portland.json`](london-portland.json) | the same theme in the form of Gogh's data/json files |
| Paris Guimard | [`installs/paris-guimard.sh`](installs/paris-guimard.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Paris Guimard | [`Paris Guimard.yml`](Paris%20Guimard.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Paris Guimard | [`paris-guimard.json`](paris-guimard.json) | the same theme in the form of Gogh's data/json files |
| Paris Catacombes | [`installs/paris-catacombes.sh`](installs/paris-catacombes.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Paris Catacombes | [`Paris Catacombes.yml`](Paris%20Catacombes.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Paris Catacombes | [`paris-catacombes.json`](paris-catacombes.json) | the same theme in the form of Gogh's data/json files |
| Paris Carrelage | [`installs/paris-carrelage.sh`](installs/paris-carrelage.sh) | run it with Gogh's apply-colors.sh in the folder above it (or beside it); TERMINAL=… picks the terminal |
| Paris Carrelage | [`Paris Carrelage.yml`](Paris%20Carrelage.yml) | Gogh's theme source: themes/ in a Gogh checkout (the file name must match the name) |
| Paris Carrelage | [`paris-carrelage.json`](paris-carrelage.json) | the same theme in the form of Gogh's data/json files |

## Turn it on

**Subway Seat**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/subway-seat.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**Subway Seat Tunnel**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/subway-seat-tunnel.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**Subway Seat Enamel**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/subway-seat-enamel.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**London Moquette**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/london-moquette.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**London Deep Level**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/london-deep-level.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**London Portland**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/london-portland.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**Paris Guimard**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/paris-guimard.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**Paris Catacombes**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/paris-catacombes.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

**Paris Carrelage**, in a terminal, in the folder that holds installs/:

```sh
curl -fsSLO https://github.com/Gogh-Co/Gogh/raw/master/apply-colors.sh
bash installs/paris-carrelage.sh
# Gogh works out which terminal you're in; TERMINAL=gnome-terminal (or another) picks one
```

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
