# Subway Seat for Sublime Text

A color scheme with gutter diff marks, inline diff, bracket and find highlights, and hover popups raised on the same paper as the other editors' menus. Copy it to Packages/User; Preferences › Browse Packages… opens the Packages folder.

[Sublime Text](https://www.sublimetext.com) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/sublime-text/) · Needs Sublime Text 4

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only sublime-text
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`Subway Seat.sublime-color-scheme`](Subway%20Seat.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| Subway Seat Tunnel | [`Subway Seat Tunnel.sublime-color-scheme`](Subway%20Seat%20Tunnel.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat Tunnel.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| Subway Seat Enamel | [`Subway Seat Enamel.sublime-color-scheme`](Subway%20Seat%20Enamel.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat Enamel.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| London Moquette | [`London Moquette.sublime-color-scheme`](London%20Moquette.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/London Moquette.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| London Deep Level | [`London Deep Level.sublime-color-scheme`](London%20Deep%20Level.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/London Deep Level.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| London Portland | [`London Portland.sublime-color-scheme`](London%20Portland.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/London Portland.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| Paris Guimard | [`Paris Guimard.sublime-color-scheme`](Paris%20Guimard.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Paris Guimard.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| Paris Catacombes | [`Paris Catacombes.sublime-color-scheme`](Paris%20Catacombes.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Paris Catacombes.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |
| Paris Carrelage | [`Paris Carrelage.sublime-color-scheme`](Paris%20Carrelage.sublime-color-scheme) | `~/Library/Application Support/Sublime Text/Packages/User/Paris Carrelage.sublime-color-scheme`; Linux: ~/.config/sublime-text/Packages/User · Windows: %APPDATA%\Sublime Text\Packages\User |

## Turn it on

**Subway Seat**, in Preferences › Settings:

```json
"color_scheme": "Subway Seat.sublime-color-scheme"
```

**Subway Seat Tunnel**, in Preferences › Settings:

```json
"color_scheme": "Subway Seat Tunnel.sublime-color-scheme"
```

**Subway Seat Enamel**, in Preferences › Settings:

```json
"color_scheme": "Subway Seat Enamel.sublime-color-scheme"
```

**London Moquette**, in Preferences › Settings:

```json
"color_scheme": "London Moquette.sublime-color-scheme"
```

**London Deep Level**, in Preferences › Settings:

```json
"color_scheme": "London Deep Level.sublime-color-scheme"
```

**London Portland**, in Preferences › Settings:

```json
"color_scheme": "London Portland.sublime-color-scheme"
```

**Paris Guimard**, in Preferences › Settings:

```json
"color_scheme": "Paris Guimard.sublime-color-scheme"
```

**Paris Catacombes**, in Preferences › Settings:

```json
"color_scheme": "Paris Catacombes.sublime-color-scheme"
```

**Paris Carrelage**, in Preferences › Settings:

```json
"color_scheme": "Paris Carrelage.sublime-color-scheme"
```

## Follow light and dark

In Preferences › Settings:

```json
"color_scheme": "auto",
"dark_color_scheme": "Subway Seat.sublime-color-scheme",
"light_color_scheme": "Subway Seat Enamel.sublime-color-scheme",
"theme": "auto"
```

## Uninstall

- Delete `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat Tunnel.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/Subway Seat Enamel.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/London Moquette.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/London Deep Level.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/London Portland.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/Paris Guimard.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/Paris Catacombes.sublime-color-scheme`.
- Delete `~/Library/Application Support/Sublime Text/Packages/User/Paris Carrelage.sublime-color-scheme`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
