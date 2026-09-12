# Subway Seat for Emacs

Three themes in one package, covering the tree-sitter font-lock faces, org, magit, diff and ediff, vertico, corfu, company, helm, treemacs, lsp-ui, doom-modeline and more. To install straight from GitHub instead of copying files, use `(use-package subway-seat-theme :vc (:url "https://github.com/oddurs/subway-seat" :lisp-dir "dist/emacs" :rev :newest))` on Emacs 30+, or `(package-vc-install '(subway-seat-theme :url "https://github.com/oddurs/subway-seat" :lisp-dir "dist/emacs"))` on Emacs 29, then `(load-theme 'subway-seat t)`.

[Emacs](https://www.gnu.org/software/emacs/) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/emacs/) · Needs Emacs 27.1+

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only emacs
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat-theme.el`](subway-seat-theme.el) | `~/.config/emacs/themes/subway-seat-theme.el` |
| Subway Seat Tunnel | [`subway-seat-tunnel-theme.el`](subway-seat-tunnel-theme.el) | `~/.config/emacs/themes/subway-seat-tunnel-theme.el`; needs subway-seat-theme.el in the same folder |
| Subway Seat Enamel | [`subway-seat-enamel-theme.el`](subway-seat-enamel-theme.el) | `~/.config/emacs/themes/subway-seat-enamel-theme.el`; needs subway-seat-theme.el in the same folder |
| London Moquette | [`london-moquette-theme.el`](london-moquette-theme.el) | `~/.config/emacs/themes/london-moquette-theme.el`; needs subway-seat-theme.el in the same folder |
| London Deep Level | [`london-deep-level-theme.el`](london-deep-level-theme.el) | `~/.config/emacs/themes/london-deep-level-theme.el`; needs subway-seat-theme.el in the same folder |
| London Portland | [`london-portland-theme.el`](london-portland-theme.el) | `~/.config/emacs/themes/london-portland-theme.el`; needs subway-seat-theme.el in the same folder |
| Paris Guimard | [`paris-guimard-theme.el`](paris-guimard-theme.el) | `~/.config/emacs/themes/paris-guimard-theme.el`; needs subway-seat-theme.el in the same folder |
| Paris Catacombes | [`paris-catacombes-theme.el`](paris-catacombes-theme.el) | `~/.config/emacs/themes/paris-catacombes-theme.el`; needs subway-seat-theme.el in the same folder |
| Paris Carrelage | [`paris-carrelage-theme.el`](paris-carrelage-theme.el) | `~/.config/emacs/themes/paris-carrelage-theme.el`; needs subway-seat-theme.el in the same folder |

## Turn it on

**Subway Seat**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'subway-seat t)
```

**Subway Seat Tunnel**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'subway-seat-tunnel t)
```

**Subway Seat Enamel**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'subway-seat-enamel t)
```

**London Moquette**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'london-moquette t)
```

**London Deep Level**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'london-deep-level t)
```

**London Portland**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'london-portland t)
```

**Paris Guimard**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'paris-guimard t)
```

**Paris Catacombes**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'paris-catacombes t)
```

**Paris Carrelage**, in init.el, with the three files in ~/.config/emacs/themes/:

```elisp
(add-to-list 'load-path "~/.config/emacs/themes/")
(add-to-list 'custom-theme-load-path "~/.config/emacs/themes/")
(load-theme 'paris-carrelage t)
```

## Follow light and dark

In init.el, with the auto-dark package from MELPA (it swaps the theme when the OS appearance changes):

```elisp
(use-package auto-dark
  :ensure t
  :custom (auto-dark-themes '((subway-seat) (subway-seat-enamel)))
  :init (auto-dark-mode))
```

## Uninstall

- Delete `~/.config/emacs/themes/subway-seat-theme.el`.
- Delete `~/.config/emacs/themes/subway-seat-tunnel-theme.el`.
- Delete `~/.config/emacs/themes/subway-seat-enamel-theme.el`.
- Delete `~/.config/emacs/themes/london-moquette-theme.el`.
- Delete `~/.config/emacs/themes/london-deep-level-theme.el`.
- Delete `~/.config/emacs/themes/london-portland-theme.el`.
- Delete `~/.config/emacs/themes/paris-guimard-theme.el`.
- Delete `~/.config/emacs/themes/paris-catacombes-theme.el`.
- Delete `~/.config/emacs/themes/paris-carrelage-theme.el`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
