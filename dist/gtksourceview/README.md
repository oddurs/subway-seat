# Subway Seat for GtkSourceView

One style scheme for everything built on GtkSourceView: GNOME Text Editor, Builder, gedit and Meld. Walnut and Enamel are paired, so GNOME Text Editor switches between them with the system style.

[GtkSourceView](https://gitlab.gnome.org/GNOME/gtksourceview) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/gtksourceview/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only gtksourceview
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.xml`](subway-seat.xml) | `~/.local/share/gtksourceview-5/styles/subway-seat.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| Subway Seat Tunnel | [`subway-seat-tunnel.xml`](subway-seat-tunnel.xml) | `~/.local/share/gtksourceview-5/styles/subway-seat-tunnel.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| Subway Seat Enamel | [`subway-seat-enamel.xml`](subway-seat-enamel.xml) | `~/.local/share/gtksourceview-5/styles/subway-seat-enamel.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| London Moquette | [`london-moquette.xml`](london-moquette.xml) | `~/.local/share/gtksourceview-5/styles/london-moquette.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| London Deep Level | [`london-deep-level.xml`](london-deep-level.xml) | `~/.local/share/gtksourceview-5/styles/london-deep-level.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| London Portland | [`london-portland.xml`](london-portland.xml) | `~/.local/share/gtksourceview-5/styles/london-portland.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| Paris Guimard | [`paris-guimard.xml`](paris-guimard.xml) | `~/.local/share/gtksourceview-5/styles/paris-guimard.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| Paris Catacombes | [`paris-catacombes.xml`](paris-catacombes.xml) | `~/.local/share/gtksourceview-5/styles/paris-catacombes.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |
| Paris Carrelage | [`paris-carrelage.xml`](paris-carrelage.xml) | `~/.local/share/gtksourceview-5/styles/paris-carrelage.xml`; gedit reads ~/.local/share/gtksourceview-4/styles (libgedit-gtksourceview-300/styles from gedit 45) |

## Turn it on

**Subway Seat**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'subway-seat'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'subway-seat'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'subway-seat'  # Builder
```

**Subway Seat Tunnel**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'subway-seat-tunnel'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'subway-seat-tunnel'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'subway-seat-tunnel'  # Builder
```

**Subway Seat Enamel**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'subway-seat-enamel'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'subway-seat-enamel'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'subway-seat-enamel'  # Builder
```

**London Moquette**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'london-moquette'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'london-moquette'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'london-moquette'  # Builder
```

**London Deep Level**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'london-deep-level'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'london-deep-level'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'london-deep-level'  # Builder
```

**London Portland**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'london-portland'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'london-portland'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'london-portland'  # Builder
```

**Paris Guimard**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'paris-guimard'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'paris-guimard'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'paris-guimard'  # Builder
```

**Paris Catacombes**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'paris-catacombes'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'paris-catacombes'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'paris-catacombes'  # Builder
```

**Paris Carrelage**, in a shell (one line per app), or the app's Preferences › Appearance (Font & Colors in gedit):

```sh
gsettings set org.gnome.TextEditor style-scheme 'paris-carrelage'  # GNOME Text Editor
gsettings set org.gnome.gedit.preferences.editor scheme 'paris-carrelage'  # gedit
gsettings set org.gnome.builder.editor style-scheme-name 'paris-carrelage'  # Builder
```

## Follow light and dark

In a shell (GNOME Text Editor; pick Subway Seat or Enamel first):

```sh
gsettings set org.gnome.TextEditor style-variant 'follow'
```

## Uninstall

- Delete `~/.local/share/gtksourceview-5/styles/subway-seat.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/subway-seat-tunnel.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/subway-seat-enamel.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/london-moquette.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/london-deep-level.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/london-portland.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/paris-guimard.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/paris-catacombes.xml`.
- Delete `~/.local/share/gtksourceview-5/styles/paris-carrelage.xml`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
