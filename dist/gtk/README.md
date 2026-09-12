# Subway Seat for GTK and libadwaita

Window, view, header bar, sidebar, card, dialog, popover and accent colors for libadwaita apps, as named colors and CSS variables. The GTK 3 file needs the adw-gtk3 theme. Flatpak apps only see these files after `flatpak override --user --filesystem=xdg-config/gtk-4.0:ro` (and `gtk-3.0`).

[GTK and libadwaita](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/css-variables.html) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/gtk/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only gtk
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`gtk-4.0/subway-seat.css`](gtk-4.0/subway-seat.css) | `~/.config/gtk-4.0/subway-seat.css` |
| Subway Seat | [`gtk-3.0/subway-seat.css`](gtk-3.0/subway-seat.css) | `~/.config/gtk-3.0/subway-seat.css`; with the adw-gtk3 theme, add `@import url("subway-seat.css");` to ~/.config/gtk-3.0/gtk.css |
| Subway Seat Tunnel | [`gtk-4.0/subway-seat-tunnel.css`](gtk-4.0/subway-seat-tunnel.css) | `~/.config/gtk-4.0/subway-seat-tunnel.css` |
| Subway Seat Tunnel | [`gtk-3.0/subway-seat-tunnel.css`](gtk-3.0/subway-seat-tunnel.css) | `~/.config/gtk-3.0/subway-seat-tunnel.css`; with the adw-gtk3 theme, add `@import url("subway-seat-tunnel.css");` to ~/.config/gtk-3.0/gtk.css |
| Subway Seat Enamel | [`gtk-4.0/subway-seat-enamel.css`](gtk-4.0/subway-seat-enamel.css) | `~/.config/gtk-4.0/subway-seat-enamel.css` |
| Subway Seat Enamel | [`gtk-3.0/subway-seat-enamel.css`](gtk-3.0/subway-seat-enamel.css) | `~/.config/gtk-3.0/subway-seat-enamel.css`; with the adw-gtk3 theme, add `@import url("subway-seat-enamel.css");` to ~/.config/gtk-3.0/gtk.css |
| London Moquette | [`gtk-4.0/london-moquette.css`](gtk-4.0/london-moquette.css) | `~/.config/gtk-4.0/london-moquette.css` |
| London Moquette | [`gtk-3.0/london-moquette.css`](gtk-3.0/london-moquette.css) | `~/.config/gtk-3.0/london-moquette.css`; with the adw-gtk3 theme, add `@import url("london-moquette.css");` to ~/.config/gtk-3.0/gtk.css |
| London Deep Level | [`gtk-4.0/london-deep-level.css`](gtk-4.0/london-deep-level.css) | `~/.config/gtk-4.0/london-deep-level.css` |
| London Deep Level | [`gtk-3.0/london-deep-level.css`](gtk-3.0/london-deep-level.css) | `~/.config/gtk-3.0/london-deep-level.css`; with the adw-gtk3 theme, add `@import url("london-deep-level.css");` to ~/.config/gtk-3.0/gtk.css |
| London Portland | [`gtk-4.0/london-portland.css`](gtk-4.0/london-portland.css) | `~/.config/gtk-4.0/london-portland.css` |
| London Portland | [`gtk-3.0/london-portland.css`](gtk-3.0/london-portland.css) | `~/.config/gtk-3.0/london-portland.css`; with the adw-gtk3 theme, add `@import url("london-portland.css");` to ~/.config/gtk-3.0/gtk.css |
| Paris Guimard | [`gtk-4.0/paris-guimard.css`](gtk-4.0/paris-guimard.css) | `~/.config/gtk-4.0/paris-guimard.css` |
| Paris Guimard | [`gtk-3.0/paris-guimard.css`](gtk-3.0/paris-guimard.css) | `~/.config/gtk-3.0/paris-guimard.css`; with the adw-gtk3 theme, add `@import url("paris-guimard.css");` to ~/.config/gtk-3.0/gtk.css |
| Paris Catacombes | [`gtk-4.0/paris-catacombes.css`](gtk-4.0/paris-catacombes.css) | `~/.config/gtk-4.0/paris-catacombes.css` |
| Paris Catacombes | [`gtk-3.0/paris-catacombes.css`](gtk-3.0/paris-catacombes.css) | `~/.config/gtk-3.0/paris-catacombes.css`; with the adw-gtk3 theme, add `@import url("paris-catacombes.css");` to ~/.config/gtk-3.0/gtk.css |
| Paris Carrelage | [`gtk-4.0/paris-carrelage.css`](gtk-4.0/paris-carrelage.css) | `~/.config/gtk-4.0/paris-carrelage.css` |
| Paris Carrelage | [`gtk-3.0/paris-carrelage.css`](gtk-3.0/paris-carrelage.css) | `~/.config/gtk-3.0/paris-carrelage.css`; with the adw-gtk3 theme, add `@import url("paris-carrelage.css");` to ~/.config/gtk-3.0/gtk.css |

## Turn it on

**Subway Seat**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("subway-seat.css");
```

**Subway Seat Tunnel**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("subway-seat-tunnel.css");
```

**Subway Seat Enamel**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("subway-seat-enamel.css");
```

**London Moquette**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("london-moquette.css");
```

**London Deep Level**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("london-deep-level.css");
```

**London Portland**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("london-portland.css");
```

**Paris Guimard**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("paris-guimard.css");
```

**Paris Catacombes**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("paris-catacombes.css");
```

**Paris Carrelage**, in ~/.config/gtk-4.0/gtk.css, then restart the apps:

```css
@import url("paris-carrelage.css");
```

## Follow light and dark

In ~/.config/gtk-4.0/gtk.css (GTK 4.20+, GNOME 49+):

```css
@import url("subway-seat-enamel.css");
@media (prefers-color-scheme: dark) {
  @import url("subway-seat.css");
}
```

## Uninstall

- Delete `~/.config/gtk-4.0/subway-seat.css`.
- Delete `~/.config/gtk-3.0/subway-seat.css`.
- Delete `~/.config/gtk-4.0/subway-seat-tunnel.css`.
- Delete `~/.config/gtk-3.0/subway-seat-tunnel.css`.
- Delete `~/.config/gtk-4.0/subway-seat-enamel.css`.
- Delete `~/.config/gtk-3.0/subway-seat-enamel.css`.
- Delete `~/.config/gtk-4.0/london-moquette.css`.
- Delete `~/.config/gtk-3.0/london-moquette.css`.
- Delete `~/.config/gtk-4.0/london-deep-level.css`.
- Delete `~/.config/gtk-3.0/london-deep-level.css`.
- Delete `~/.config/gtk-4.0/london-portland.css`.
- Delete `~/.config/gtk-3.0/london-portland.css`.
- Delete `~/.config/gtk-4.0/paris-guimard.css`.
- Delete `~/.config/gtk-3.0/paris-guimard.css`.
- Delete `~/.config/gtk-4.0/paris-catacombes.css`.
- Delete `~/.config/gtk-3.0/paris-catacombes.css`.
- Delete `~/.config/gtk-4.0/paris-carrelage.css`.
- Delete `~/.config/gtk-3.0/paris-carrelage.css`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
