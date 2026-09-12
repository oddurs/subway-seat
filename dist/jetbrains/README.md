# Subway Seat for JetBrains IDEs

One plugin for IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider and the rest: a UI theme and a matching editor color scheme for each flavor, plus an Islands version of each theme for the Islands look (2025.2.3 and later). The .icls files import on their own if you only want the editor colors.

[JetBrains IDEs](https://www.jetbrains.com) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/jetbrains/) · Needs IntelliJ-based IDEs 2023.2+

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`schemes/subway-seat.icls`](schemes/subway-seat.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| Subway Seat | [`themes/subway-seat.theme.json`](themes/subway-seat.theme.json) | packaged in subway-seat-jetbrains.jar |
| Subway Seat | [`themes/subway-seat-islands.theme.json`](themes/subway-seat-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| Subway Seat Tunnel | [`schemes/subway-seat-tunnel.icls`](schemes/subway-seat-tunnel.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| Subway Seat Tunnel | [`themes/subway-seat-tunnel.theme.json`](themes/subway-seat-tunnel.theme.json) | packaged in subway-seat-jetbrains.jar |
| Subway Seat Tunnel | [`themes/subway-seat-tunnel-islands.theme.json`](themes/subway-seat-tunnel-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| Subway Seat Enamel | [`schemes/subway-seat-enamel.icls`](schemes/subway-seat-enamel.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| Subway Seat Enamel | [`themes/subway-seat-enamel.theme.json`](themes/subway-seat-enamel.theme.json) | packaged in subway-seat-jetbrains.jar |
| Subway Seat Enamel | [`themes/subway-seat-enamel-islands.theme.json`](themes/subway-seat-enamel-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Moquette | [`schemes/london-moquette.icls`](schemes/london-moquette.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| London Moquette | [`themes/london-moquette.theme.json`](themes/london-moquette.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Moquette | [`themes/london-moquette-islands.theme.json`](themes/london-moquette-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Deep Level | [`schemes/london-deep-level.icls`](schemes/london-deep-level.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| London Deep Level | [`themes/london-deep-level.theme.json`](themes/london-deep-level.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Deep Level | [`themes/london-deep-level-islands.theme.json`](themes/london-deep-level-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Portland | [`schemes/london-portland.icls`](schemes/london-portland.icls) | Settings › Editor › Color Scheme › ⚙ › Import Scheme… (editor colors only) |
| London Portland | [`themes/london-portland.theme.json`](themes/london-portland.theme.json) | packaged in subway-seat-jetbrains.jar |
| London Portland | [`themes/london-portland-islands.theme.json`](themes/london-portland-islands.theme.json) | packaged in subway-seat-jetbrains.jar |
| All three | [`META-INF/plugin.xml`](META-INF/plugin.xml) | packaged in subway-seat-jetbrains.jar |
| All three | [`META-INF/pluginIcon.svg`](META-INF/pluginIcon.svg) | packaged in subway-seat-jetbrains.jar |
| All three | [`subway-seat-jetbrains.jar`](subway-seat-jetbrains.jar) | Settings › Plugins › ⚙ › Install Plugin from Disk… |

## Turn it on

**Subway Seat**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: Subway Seat (or Subway Seat Islands)
Editor › Color Scheme: Subway Seat
```

**Subway Seat Tunnel**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: Subway Seat Tunnel (or Subway Seat Tunnel Islands)
Editor › Color Scheme: Subway Seat Tunnel
```

**Subway Seat Enamel**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: Subway Seat Enamel (or Subway Seat Enamel Islands)
Editor › Color Scheme: Subway Seat Enamel
```

**London Moquette**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: London Moquette (or London Moquette Islands)
Editor › Color Scheme: London Moquette
```

**London Deep Level**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: London Deep Level (or London Deep Level Islands)
Editor › Color Scheme: London Deep Level
```

**London Portland**, in Settings › Plugins › ⚙ › Install Plugin from Disk… (subway-seat-jetbrains.jar), then Settings › Appearance & Behavior › Appearance:

```text
Theme: London Portland (or London Portland Islands)
Editor › Color Scheme: London Portland
```

## Follow light and dark

In Settings › Appearance & Behavior › Appearance:

```text
☑ Sync with OS, then ⚙ beside it:
Dark: Subway Seat (or Subway Seat Islands)
Light: Subway Seat Enamel (or Subway Seat Enamel Islands)
```

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
