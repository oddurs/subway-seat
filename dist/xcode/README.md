# Subway Seat for Xcode

Source editor, console and rendered documentation colors in SF Mono, with comments in italic. Change the font size in Xcode's Themes settings; the colors stay. Xcode remembers the theme you pick separately for light and dark mode, so it can follow the system.

[Xcode](https://developer.apple.com/xcode/) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/xcode/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only xcode
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`Subway Seat.xccolortheme`](Subway%20Seat.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat.xccolortheme` |
| Subway Seat Tunnel | [`Subway Seat Tunnel.xccolortheme`](Subway%20Seat%20Tunnel.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat Tunnel.xccolortheme` |
| Subway Seat Enamel | [`Subway Seat Enamel.xccolortheme`](Subway%20Seat%20Enamel.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat Enamel.xccolortheme` |
| London Moquette | [`London Moquette.xccolortheme`](London%20Moquette.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Moquette.xccolortheme` |
| London Deep Level | [`London Deep Level.xccolortheme`](London%20Deep%20Level.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Deep Level.xccolortheme` |
| London Portland | [`London Portland.xccolortheme`](London%20Portland.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Portland.xccolortheme` |
| Paris Guimard | [`Paris Guimard.xccolortheme`](Paris%20Guimard.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Guimard.xccolortheme` |
| Paris Catacombes | [`Paris Catacombes.xccolortheme`](Paris%20Catacombes.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Catacombes.xccolortheme` |
| Paris Carrelage | [`Paris Carrelage.xccolortheme`](Paris%20Carrelage.xccolortheme) | `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Carrelage.xccolortheme` |

## Turn it on

**Subway Seat**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Subway Seat.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Subway Seat under Settings › Themes
```

**Subway Seat Tunnel**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Subway Seat Tunnel.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Subway Seat Tunnel under Settings › Themes
```

**Subway Seat Enamel**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Subway Seat Enamel.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Subway Seat Enamel under Settings › Themes
```

**London Moquette**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "London Moquette.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick London Moquette under Settings › Themes
```

**London Deep Level**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "London Deep Level.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick London Deep Level under Settings › Themes
```

**London Portland**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "London Portland.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick London Portland under Settings › Themes
```

**Paris Guimard**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Paris Guimard.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Paris Guimard under Settings › Themes
```

**Paris Catacombes**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Paris Catacombes.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Paris Catacombes under Settings › Themes
```

**Paris Carrelage**, in Terminal, then Xcode › Settings… › Themes:

```sh
mkdir -p ~/Library/Developer/Xcode/UserData/FontAndColorThemes
cp "Paris Carrelage.xccolortheme" ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
# restart Xcode, then pick Paris Carrelage under Settings › Themes
```

## Follow light and dark

In Terminal, with Xcode closed (Xcode keeps one theme for light mode and one for dark):

```sh
defaults write com.apple.dt.Xcode XCFontAndColorCurrentTheme -string 'Subway Seat Enamel.xccolortheme'
defaults write com.apple.dt.Xcode XCFontAndColorCurrentDarkTheme -string 'Subway Seat.xccolortheme'
```

## Uninstall

- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat Tunnel.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Subway Seat Enamel.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Moquette.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Deep Level.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/London Portland.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Guimard.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Catacombes.xccolortheme`.
- Delete `~/Library/Developer/Xcode/UserData/FontAndColorThemes/Paris Carrelage.xccolortheme`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
