# Subway Seat for lazygit

Orange borders on the focused panel, gold while searching, warm grounds for the selected line, and copied and rebase-base commits marked in sage and gold. The diff pane shows git's own colors, so install the git port; or add the `-delta.yml` file to run diffs through delta with the delta port's feature (it uses `git.diffRenderers`, the key in lazygit 0.65; older releases call it `git.paging`).

[lazygit](https://github.com/jesseduffield/lazygit) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/lazygit/)

## The quick way

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --only lazygit
```

The [installer](../../docs/INSTALL.md) shows its plan and asks once. Add `--flavor tunnel`, `--flavor enamel` or `--flavor auto` for another flavor. To do it yourself, use the files below.

## Files

| Flavor | File | Where it goes |
|---|---|---|
| Subway Seat | [`subway-seat.yml`](subway-seat.yml) | `~/.config/lazygit/subway-seat.yml` |
| Subway Seat | [`subway-seat-delta.yml`](subway-seat-delta.yml) | `~/.config/lazygit/subway-seat-delta.yml` |
| Subway Seat Tunnel | [`subway-seat-tunnel.yml`](subway-seat-tunnel.yml) | `~/.config/lazygit/subway-seat-tunnel.yml` |
| Subway Seat Tunnel | [`subway-seat-tunnel-delta.yml`](subway-seat-tunnel-delta.yml) | `~/.config/lazygit/subway-seat-tunnel-delta.yml` |
| Subway Seat Enamel | [`subway-seat-enamel.yml`](subway-seat-enamel.yml) | `~/.config/lazygit/subway-seat-enamel.yml` |
| Subway Seat Enamel | [`subway-seat-enamel-delta.yml`](subway-seat-enamel-delta.yml) | `~/.config/lazygit/subway-seat-enamel-delta.yml` |
| London Moquette | [`london-moquette.yml`](london-moquette.yml) | `~/.config/lazygit/london-moquette.yml` |
| London Moquette | [`london-moquette-delta.yml`](london-moquette-delta.yml) | `~/.config/lazygit/london-moquette-delta.yml` |
| London Deep Level | [`london-deep-level.yml`](london-deep-level.yml) | `~/.config/lazygit/london-deep-level.yml` |
| London Deep Level | [`london-deep-level-delta.yml`](london-deep-level-delta.yml) | `~/.config/lazygit/london-deep-level-delta.yml` |
| London Portland | [`london-portland.yml`](london-portland.yml) | `~/.config/lazygit/london-portland.yml` |
| London Portland | [`london-portland-delta.yml`](london-portland-delta.yml) | `~/.config/lazygit/london-portland-delta.yml` |
| Paris Guimard | [`paris-guimard.yml`](paris-guimard.yml) | `~/.config/lazygit/paris-guimard.yml` |
| Paris Guimard | [`paris-guimard-delta.yml`](paris-guimard-delta.yml) | `~/.config/lazygit/paris-guimard-delta.yml` |
| Paris Catacombes | [`paris-catacombes.yml`](paris-catacombes.yml) | `~/.config/lazygit/paris-catacombes.yml` |
| Paris Catacombes | [`paris-catacombes-delta.yml`](paris-catacombes-delta.yml) | `~/.config/lazygit/paris-catacombes-delta.yml` |
| Paris Carrelage | [`paris-carrelage.yml`](paris-carrelage.yml) | `~/.config/lazygit/paris-carrelage.yml` |
| Paris Carrelage | [`paris-carrelage-delta.yml`](paris-carrelage-delta.yml) | `~/.config/lazygit/paris-carrelage-delta.yml` |

## Turn it on

**Subway Seat**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/subway-seat.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/subway-seat.yml"
```

**Subway Seat Tunnel**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/subway-seat-tunnel.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/subway-seat-tunnel.yml"
```

**Subway Seat Enamel**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/subway-seat-enamel.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/subway-seat-enamel.yml"
```

**London Moquette**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/london-moquette.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/london-moquette.yml"
```

**London Deep Level**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/london-deep-level.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/london-deep-level.yml"
```

**London Portland**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/london-portland.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/london-portland.yml"
```

**Paris Guimard**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/paris-guimard.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/paris-guimard.yml"
```

**Paris Catacombes**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/paris-catacombes.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/paris-catacombes.yml"
```

**Paris Carrelage**, in fish, once (`set -U` keeps it). lazygit merges every file in LG_CONFIG_FILE and stops if one is missing, hence the `touch`. For delta diffs, add the flavor's `-delta.yml` file to the list:

```fish
set -l dir (lazygit --print-config-dir); mkdir -p $dir; touch $dir/config.yml
set -Ux LG_CONFIG_FILE "$dir/config.yml,$HOME/.config/lazygit/paris-carrelage.yml"
```

In bash or zsh:

```sh
dir="$(lazygit --print-config-dir)"; mkdir -p "$dir"; touch "$dir/config.yml"
# then in ~/.zshrc or ~/.bashrc:
export LG_CONFIG_FILE="$(lazygit --print-config-dir)/config.yml,$HOME/.config/lazygit/paris-carrelage.yml"
```

## Uninstall

- Delete `~/.config/lazygit/subway-seat.yml`.
- Delete `~/.config/lazygit/subway-seat-delta.yml`.
- Delete `~/.config/lazygit/subway-seat-tunnel.yml`.
- Delete `~/.config/lazygit/subway-seat-tunnel-delta.yml`.
- Delete `~/.config/lazygit/subway-seat-enamel.yml`.
- Delete `~/.config/lazygit/subway-seat-enamel-delta.yml`.
- Delete `~/.config/lazygit/london-moquette.yml`.
- Delete `~/.config/lazygit/london-moquette-delta.yml`.
- Delete `~/.config/lazygit/london-deep-level.yml`.
- Delete `~/.config/lazygit/london-deep-level-delta.yml`.
- Delete `~/.config/lazygit/london-portland.yml`.
- Delete `~/.config/lazygit/london-portland-delta.yml`.
- Delete `~/.config/lazygit/paris-guimard.yml`.
- Delete `~/.config/lazygit/paris-guimard-delta.yml`.
- Delete `~/.config/lazygit/paris-catacombes.yml`.
- Delete `~/.config/lazygit/paris-catacombes-delta.yml`.
- Delete `~/.config/lazygit/paris-carrelage.yml`.
- Delete `~/.config/lazygit/paris-carrelage-delta.yml`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
