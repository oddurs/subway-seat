# Subway Seat

A walnut-brown color theme from a 1970s subway car: parchment text, harvest gold, burnt orange and avocado, with orange bucket seats and wood paneling in mind.

![Subway Seat in VS Code](https://raw.githubusercontent.com/oddurs/subway-seat/main/assets/screenshots/vscode.png)

- **Subway Seat**: Walnut, the original dark flavor
- **Subway Seat Tunnel**: the late local after midnight, a deeper dark
- **Subway Seat Enamel**: cream enamel panels in the morning sun, the light one

The workbench is layered on purpose: one chrome ground, grooves instead of lines, popovers lifted onto paper, and every hover and row a thin wash of text color, so they sit right on any surface. Selections, search matches and diffs use the same colors as the Neovim, JetBrains, Zed and other ports. It also themes the AI panels in VS Code, Cursor, Windsurf and Kiro, and the colors GitLens, Error Lens and GitHub Pull Requests contribute.

## Install

Pick **Preferences: Color Theme › Subway Seat** (or Tunnel, or Enamel). If you have the `.vsix` file:

```sh
code --install-extension subway-seat.vsix
```

Cursor (`cursor`), Windsurf (`windsurf`) and VSCodium (`codium`) take the same flag, or use **Extensions › ⋯ › Install from VSIX…**.

## Follow the system's light and dark mode

```json
"window.autoDetectColorScheme": true,
"workbench.preferredDarkColorTheme": "Subway Seat",
"workbench.preferredLightColorTheme": "Subway Seat Enamel"
```

![Subway Seat Tunnel](https://raw.githubusercontent.com/oddurs/subway-seat/main/assets/screenshots/vscode-tunnel.png)

![Subway Seat Enamel](https://raw.githubusercontent.com/oddurs/subway-seat/main/assets/screenshots/vscode-enamel.png)

Subway Seat is available for over 100 apps, from Ghostty and Neovim to Claude Code: [github.com/oddurs/subway-seat](https://github.com/oddurs/subway-seat).
