# Changelog

All notable changes to Subway Seat. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [SemVer](https://semver.org/): a color change that alters how existing code looks is a minor bump; a fixed key or a new port is a patch.

## [0.3.0] - 2026-09-11

### Changed

- Palette: Enamel's accents are darker, so they reach WCAG AA on cream and comments recede below them again. The dark flavors' red, bright red and green are lifted so errors and numbers read; Tunnel's overlays are raised to match Walnut; ANSI 8 (bright black) is now the comment color.
- Diff grounds shift hue instead of lightness: every syntax color keeps about 3:1 or more on added and removed lines, and word emphasis stays clearly stronger than the line.
- Every role has a name and a documented use; crust is "Blackout" and base is "Paneling".
- US spelling ("color") in every note, generated file and doc, except names an app defines.
- The version lives in one place, `pyproject.toml`, and every generated manifest reads it.
- The README's flavor and accent tables are generated from `palette.py`.

### Added

- **One-command setup.** `install.sh` (POSIX sh, also `curl … | sh`) detects your apps, shows a plan, asks once, links the files and adds the enable lines inside removable blocks. `switch <flavor>` re-points everything at once; `status`, `uninstall` and `list` round it out. Choices live in `~/.config/subway-seat/config`. `install.fish` is now a thin wrapper, and the site has a configurator at `/install`.
- **25 new ports (117 in all):** wallpapers (stripes and bucket seats, three flavors, desktop and phone), Ptyxis, KDE Plasma, GTK 4/libadwaita, Hyprland, waybar, rofi, fuzzel, dunst, mako, PowerShell, lsd, Midnight Commander, Sublime Merge, Godot, Mattermost, Element, television, broot, zathura, newsboat, fastfetch, matplotlib, a macOS color list, and git's own colors.
- **Diffs everywhere:** delta, git, lazygit (with a delta pager config), kitty's diff kitten, VS Code, Neovim, Vim, Zed, JetBrains, Helix, Emacs (magit, ediff, smerge), Sublime Text and Merge, Claude Code, Pygments, highlight.js, Prism, Chroma, Obsidian and Discord all use the same diff grounds; web formats export them as tokens.
- **Follow light and dark** wherever the app can: kitty, iTerm2, WezTerm, VS Code, Zed, JetBrains, Sublime, Neovim, Emacs, fish, bat, tmux, yazi, Firefox/Thunderbird (an auto add-on), highlight.js, Prism, Tailwind, GTK and more.
- **Claude Code:** the setup skill asks once and dry-runs before writing (a bundled `setup.sh`); a SessionStart hook makes the subagent rows work from the plugin; ten more theme tokens; status line v2 (width-aware, detached HEAD, worktrees, vim mode, rate-limit meter, comma-decimal locales) and new tips.
- **Neovim:** flavors follow `background`, `setup{ background = { dark, light } }`, standalone colors files and ~2,000 groups across ~70 plugins. VS Code covers the full 1.133 color registry, GitLens and Error Lens; JetBrains gains Islands variants.
- **The site:** port search, palette formats and downloads, a flavor comparison, share images for every port, per-port "report a problem" links, "Download all", a styled 404, and a rebuilt Claude Code mock taken line for line from a real session.
- A Desktop category.
- The port contract gains `how` (install steps that aren't a path), `auto` (follow the OS light/dark setting), `requires`, `detect`, `enable.sh` and `enable.file`. Appended blocks are wrapped in `# >>> subway-seat >>>` markers so removing them is one step.
- A generated README in every `dist/<id>/`: the files, where they go, how to turn it on and how to uninstall.
- `dist/install.tsv`, the table the one-command installer reads.
- `./build.py --check`, a pytest suite (palette contrast, diff-tint contrast, the port contract, determinism), and CI checks that load the themes in fish, Starship, bat, tmux, Zellij and Ghostty, lint the workflows and shell scripts, and check links weekly.

### Fixed

- Install steps that pointed at unpublished channels (Marketplace, Zed extensions, MELPA, a `.nvim` repo) now use the files in this repo.
- Pasting an enable snippet no longer breaks the app: Windows Terminal's duplicate `profiles`, Starship's `palette` placement, fzf replacing `FZF_DEFAULT_OPTS`, tmux above TPM's `run`, lazygit without a config file, fish's auto theme without `[unknown]`.
- Enamel's bracket match, current parameter hint and several popovers were nearly invisible.
- Claude Code setup wrote a theme name that doesn't exist, and pointed at the removed `/output-style`.
- The site's share image 404'd, narrow screens scrolled sideways, and the editor mock lost its highlights in Tunnel and Enamel; port pages are a fraction of their old weight.
- `./build.py --only <id>` no longer cuts `dist/manifest.json` down to one port.
- CI's "dist/ is current" check missed files that were never committed and Telegram's text themes.
- The build writes UTF-8 with LF line endings on every OS.

## [0.2.0] - 2026-09-10

### Added

- Three flavors: **Subway Seat** (Walnut), **Subway Seat Tunnel** (deeper dark) and **Subway Seat Enamel** (light).
- A port system: one module per app in `ports/`, built for every flavor into `dist/` with parse checks and a manifest.
- ~90 ports across terminals, editors, agent harnesses, shell and prompt, CLI and TUI tools, desktop apps and palette formats.
- A layered VS Code workbench (one chrome ground, translucent hovers and selections, raised popovers) that also themes the AI panels in Cursor, Windsurf and Kiro, packaged as a VSIX by the build.
- A Neovim plugin with `setup()`, flavor auto-selection from `background`, lualine themes and plugin highlight groups.
- A Claude Code plugin: themes, a station-sign status line, subagent rows, spinner verbs, tips and a relaxed output style.
- Ports for opencode, Codex, Gemini CLI, Aider and herdr, and notes for the agents that follow your terminal colors.
- The website: flavor switcher, a VS Code mock painted with the real theme, and a page for every port.

## 0.1.0 - 2026-09-10

### Added

- The original Walnut palette with Ghostty, fish, Starship, bat/delta, herdr, Neovim, VS Code and Claude Code ports.

[0.3.0]: https://github.com/oddurs/subway-seat/compare/744219f...v0.3.0
[0.2.0]: https://github.com/oddurs/subway-seat/commit/744219f
