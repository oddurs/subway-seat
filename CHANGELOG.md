# Changelog

All notable changes to Subway Seat. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [SemVer](https://semver.org/): a colour change that alters how existing code looks is a minor bump; a fixed key or a new port is a patch.

## [Unreleased]

## [0.2.0] - 2026-09-10

### Added

- Three flavors: **Subway Seat** (Walnut), **Subway Seat Tunnel** (deeper dark) and **Subway Seat Enamel** (light).
- A port system: one module per app in `ports/`, built for every flavor into `dist/` with parse checks and a manifest.
- ~90 ports across terminals, editors, agent harnesses, shell and prompt, CLI and TUI tools, desktop apps and palette formats.
- A layered VS Code workbench (one chrome ground, translucent hovers and selections, raised popovers) that also themes the AI panels in Cursor, Windsurf and Kiro, packaged as a VSIX by the build.
- A Neovim plugin with `setup()`, flavor auto-selection from `background`, lualine themes and plugin highlight groups.
- A Claude Code plugin: themes, a station-sign status line, subagent rows, spinner verbs, tips and a relaxed output style.
- Ports for opencode, Codex, Gemini CLI, Aider and herdr, and notes for the agents that follow your terminal colours.
- The website: flavor switcher, a VS Code mock painted with the real theme, and a page for every port.

## [0.1.0] - 2026-09-10

### Added

- The original Walnut palette with Ghostty, fish, Starship, bat/delta, herdr, Neovim, VS Code and Claude Code ports.

[Unreleased]: https://github.com/oddurs/subway-seat/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/oddurs/subway-seat/releases/tag/v0.2.0
[0.1.0]: https://github.com/oddurs/subway-seat/releases/tag/v0.1.0
