<p align="center">
  <img src="assets/icon.png" width="96" alt="" />
</p>

<h1 align="center">Subway Seat</h1>

<p align="center">
  A walnut-brown color scheme from a 1970s subway car.<br />
  Parchment text, harvest gold, burnt orange, avocado. Sit back.
</p>

<p align="center">
  <a href="https://oddurs.github.io/subway-seat">Website</a> ·
  <a href="https://oddurs.github.io/subway-seat/palette">Palette</a> ·
  <a href="#ports">Ports</a> ·
  <a href="CONTRIBUTING.md">Add a port</a>
</p>

<p align="center">
  <img src="assets/screenshots/hero.png" alt="The Subway Seat website: a walnut-brown page with a large cream headline, 70s orange, gold and avocado stripes, and a band of shag carpet." />
</p>

## Three flavors

<!-- flavors:start -->
**New York** — A 1970s subway car: walnut paneling, orange bucket seats, cream enamel.

| | | |
|---|---|---|
| **Subway Seat** | `walnut` · dark | Walnut paneling and orange bucket seats. The original. |
| **Subway Seat Tunnel** | `tunnel` · dark | The late local after midnight: espresso-deep, same warm lights. |
| **Subway Seat Enamel** | `enamel` · light | Cream enamel panels in the morning sun. The light one. |

**London** — The Tube: Corporate Blue turned down, brick and hazard yellow, the standard red.

| | | |
|---|---|---|
| **London Moquette** | `moquette` · dark | The seat you're sitting on. Corporate Blue, turned right down. |
| **London Deep Level** | `deep` · dark | Below the cut-and-cover lines. The ground drops; the signals don't. |
| **London Portland** | `portland` · light | Holden's Portland stone. Links are the exact Corporate Blue. |

**Paris** — The Metro in its materials: cast iron and brass, white tile, verdigris and terracotta.

| | | |
|---|---|---|
| **Paris Guimard** | `guimard` · dark | Cast iron off a Metro entrance, which is nearly black. Brass leads. |
| **Paris Catacombes** | `catacombes` · dark | Under the quarries: the same green with the lights turned down. |
| **Paris Carrelage** | `carrelage` · light | Bevelled white tile under a vaulted platform. The light one. |
<!-- flavors:end -->

<p align="center">
  <img src="assets/screenshots/vscode.png" alt="VS Code in Subway Seat: a walnut editor, darker sidebar and tabs, a raised suggestion popover, and a terminal panel." />
</p>

<p align="center">
  <img src="assets/screenshots/vscode-tunnel.png" width="49%" alt="The same VS Code window in Subway Seat Tunnel, an espresso-dark flavor." />
  <img src="assets/screenshots/vscode-enamel.png" width="49%" alt="The same VS Code window in Subway Seat Enamel, a cream light flavor." />
</p>

The whole spectrum isn't invited. Blue is faded denim and only marks links; magenta got reassigned to burnt orange; cyan is seafoam tile. Everything stays in the same warm room.

<!-- accents:start -->
| Accent | Leads |
|---|---|
| Burnt orange | keywords, tags, the Claude spinner |
| Harvest gold | functions, commands, the cursor |
| Avocado | strings, additions |
| Seafoam tile | types, classes, options |
| Redbird bright | numbers, constants, deletions |
| Terracotta | escapes, regex, decorators |
| Faded denim | links and info, the only cool color |
<!-- accents:end -->

## Ports

Every port is generated from [`palette.py`](palette.py) in all three flavors. Each folder in [`dist/`](dist) has the files and a README with install steps; the [website](https://oddurs.github.io/subway-seat) has previews and the full file for every one. The easiest way in is the one-command `install.sh` described below.

<!-- ports:start -->
| | |
|---|---|
| **Terminals** (20) | [Alacritty](dist/alacritty), [foot](dist/foot), [Ghostty](dist/ghostty), [GNOME Terminal](dist/gnome-terminal), [Hyper](dist/hyper), [iTerm2](dist/iterm2), [kitty](dist/kitty), [Konsole](dist/konsole), [Ptyxis](dist/ptyxis), [Rio](dist/rio), [Tabby](dist/tabby), [Terminal.app](dist/terminal-app), [Terminator](dist/terminator), [Termux](dist/termux), [Tilix](dist/tilix), [Warp](dist/warp), [WezTerm](dist/wezterm), [Windows Terminal](dist/windows-terminal), [Xfce Terminal](dist/xfce-terminal), [Xresources](dist/xresources) |
| **Editors** (16) | [Emacs](dist/emacs), [Godot](dist/godot), [GtkSourceView](dist/gtksourceview), [Helix](dist/helix), [JetBrains IDEs](dist/jetbrains), [Kakoune](dist/kakoune), [Lite XL](dist/lite-xl), [micro](dist/micro), [Neovim](dist/nvim), [Notepad++](dist/notepad-plus-plus), [Sublime Merge](dist/sublime-merge), [Sublime Text](dist/sublime-text), [Vim](dist/vim), [VS Code](dist/vscode), [Xcode](dist/xcode), [Zed](dist/zed) |
| **Agents** (7) | [Aider](dist/aider), [Claude Code](dist/claude-code), [Codex CLI](dist/codex), [Copilot CLI, Amp & goose](dist/terminal-agents), [Gemini CLI](dist/gemini-cli), [herdr](dist/herdr), [opencode](dist/opencode) |
| **Shell & prompt** (5) | [fish](dist/fish), [Nushell](dist/nushell), [PowerShell](dist/powershell), [Starship](dist/starship), [zsh-syntax-highlighting](dist/zsh-syntax-highlighting) |
| **CLI & TUI** (26) | [AIChat](dist/aichat), [Atuin](dist/atuin), [bat](dist/bat), [bottom](dist/bottom), [broot](dist/broot), [btop](dist/btop), [cava](dist/cava), [delta](dist/delta), [eza](dist/eza), [fastfetch](dist/fastfetch), [fzf](dist/fzf), [gh-dash](dist/gh-dash), [Git](dist/git), [gitui](dist/gitui), [Glow](dist/glow), [k9s](dist/k9s), [lazygit](dist/lazygit), [lsd](dist/lsd), [Midnight Commander](dist/midnight-commander), [Newsboat](dist/newsboat), [spotify_player](dist/spotify-player), [television](dist/television), [tmux](dist/tmux), [vivid](dist/vivid), [Yazi](dist/yazi), [Zellij](dist/zellij) |
| **Apps** (17) | [Alfred](dist/alfred), [Chrome](dist/chrome), [Dark Reader](dist/dark-reader), [Discord](dist/discord), [Element](dist/element), [Firefox](dist/firefox), [Mattermost](dist/mattermost), [Obsidian](dist/obsidian), [qutebrowser](dist/qutebrowser), [Raycast](dist/raycast), [Slack](dist/slack), [Spotify (Spicetify)](dist/spicetify), [Telegram](dist/telegram), [Thunderbird](dist/thunderbird), [Vimium](dist/vimium), [Vivaldi](dist/vivaldi), [zathura](dist/zathura) |
| **Desktop** (9) | [dunst](dist/dunst), [fuzzel](dist/fuzzel), [GTK and libadwaita](dist/gtk), [Hyprland](dist/hyprland), [KDE Plasma](dist/kde), [mako](dist/mako), [rofi](dist/rofi), [Wallpapers](dist/wallpapers), [waybar](dist/waybar) |
| **Palettes** (17) | [Adobe Swatch Exchange](dist/ase), [Base16 / Base24 / Tinted8](dist/base16), [Chroma](dist/chroma), [CSS variables](dist/css), [GIMP, Inkscape, Krita](dist/gimp), [Gogh](dist/gogh), [Hex list](dist/txt), [highlight.js](dist/highlightjs), [macOS color list](dist/clr), [matplotlib](dist/matplotlib), [Palette JSON](dist/json), [Prism](dist/prism), [Procreate](dist/procreate), [Pygments](dist/pygments), [Sass](dist/scss), [Shiki](dist/shiki), [Tailwind CSS](dist/tailwind) |
<!-- ports:end -->

### The deep ones

- **VS Code** (and Cursor, Windsurf, VSCodium): a layered workbench with about 1,000 color keys, including the AI panels of each fork. One chrome ground, grooves instead of lines, popovers on paper, translucent hovers and selections.
- **Claude Code**: themes for all three flavors, a station-sign status line, subagent rows, 70s spinner verbs, "Next stop" tips and a relaxed output style, bundled as a plugin. Claude Code colors the code in diffs itself; each flavor's "terminal colors" theme hands that to your terminal's palette, so in a Subway Seat terminal it matches too. `/subway-seat:setup` asks which you want.

  ```
  /plugin marketplace add oddurs/subway-seat
  /plugin install subway-seat@subway-seat
  /subway-seat:setup
  ```

  <img src="assets/screenshots/claude.png" alt="A Claude Code session in Subway Seat with an orange route-bullet status line, subagent rows and a rotating spinner verb." />

- **Neovim**: a plugin with `setup({ background = { dark = …, light = … }, transparent, italics, overrides })`, `colorscheme subway-seat` following `background` (flip it and Walnut becomes Enamel and back), lualine themes, and about 2,000 highlight groups covering Tree-sitter, LSP and about 70 plugins.
- **Zed**: a full theme family covering every style key, including the agent panel.

## Install

One command finds the apps on your Mac or Linux machine, links in their themes, and turns Subway Seat on:

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh
```

It shows the plan and asks once before changing anything. Theme files go where each app looks for them. The line that switches an app over is added to its config between `# >>> subway-seat >>>` markers, and only where appending is a safe, complete way to do it. Anything that needs a person (a settings screen, an import dialog) is listed at the end as a short step. Claude Code gets the plugin, and VS Code and its forks get the extension.

```sh
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --flavor tunnel  # or enamel, or auto
curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh -s -- --dry-run         # the plan only

sh ~/.local/share/subway-seat/install.sh switch enamel   # re-point every app at once
sh ~/.local/share/subway-seat/install.sh status          # what's installed, and what drifted
sh ~/.local/share/subway-seat/install.sh uninstall       # remove everything it did, and nothing else
```

`auto` follows the system's light or dark setting in the apps that can, and uses Walnut elsewhere.

From a clone, run `./install.sh` (or `./install.fish`) instead. The files are then linked rather than copied, so a `git pull` updates them in place. It needs only `sh` and the tools every Mac and Linux system has, plus `curl` or `wget` for the one-line install. [docs/INSTALL.md](docs/INSTALL.md) covers `--only`, `--skip`, `--copy`, `--no-enable`, the settings file and how to uninstall by hand.

## How it's built

```
palette.py      flavors and roles: the only place colors live
ports/*.py      one small module per app, written against roles
build.py        runs every port for every flavor → dist/, checks the files parse
site/           the website (Next.js + StyleX), colored by the same palette
```

The build needs Python 3.12 or newer. [uv](https://docs.astral.sh/uv/) brings the right Python and PyYAML (used to check YAML output) for you:

```sh
uv run ./build.py                 # everything
uv run ./build.py --only vscode   # one port; the manifest keeps the rest
uv run ./build.py --check         # fail if anything differs from a fresh build
uv run ./build.py --list          # what's there
```

[CONTRIBUTING.md](CONTRIBUTING.md) covers adding a port and running the tests.

## License

MIT. Take it, tweak it, ship it.
