# Changelog

All notable changes to Subway Seat. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [SemVer](https://semver.org/): a color change that alters how existing code looks is a minor bump; a fixed key or a new port is a patch.

## [0.3.0] - Unreleased

### Changed

- Palette: Enamel's accents are darker, so they reach WCAG AA on cream and comments recede below them again. The dark flavors' red, bright red and green are lifted so errors and numbers read; Tunnel's overlays are raised to match Walnut; ANSI 8 (bright black) is now the comment color.
- Diff grounds shift hue instead of lightness: every syntax color keeps about 3:1 or more on added and removed lines, and word emphasis stays clearly stronger than the line.
- Every role has a name and a documented use; crust is "Blackout" and base is "Paneling".
- US spelling ("color") in every note, generated file and doc, except names an app defines.
- The version lives in one place, `pyproject.toml`, and every generated manifest reads it.
- The README's flavor and accent tables are generated from `palette.py`.

### Added

- A Desktop category.
- The port contract gains `how` (install steps that aren't a path), `auto` (follow the OS light/dark setting), `requires`, `detect`, `enable.sh` and `enable.file`. Appended blocks are wrapped in `# >>> subway-seat >>>` markers so removing them is one step.
- A generated README in every `dist/<id>/`: the files, where they go, how to turn it on and how to uninstall.
- `dist/install.tsv`, the table the one-command installer reads.
- `./build.py --check`, a pytest suite (palette contrast, diff-tint contrast, the port contract, determinism), and CI checks that load the themes in fish, Starship, bat, tmux, Zellij and Ghostty, lint the workflows and shell scripts, and check links weekly.

### Fixed

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

<!-- No tags exist before v0.3.0. When it's tagged, point [0.3.0] at compare/744219f...v0.3.0. -->
[0.3.0]: https://github.com/oddurs/subway-seat/compare/744219f...main
[0.2.0]: https://github.com/oddurs/subway-seat/commit/744219f
