# Contributing

Thanks for wanting to add to the car. The most common contribution is a new port, and a port is one Python file.

## What you need

- **Python 3.12 or newer.** The stock `python3` on macOS is too old. [uv](https://docs.astral.sh/uv/) is the easy way: `uv run ./build.py` fetches a suitable Python and PyYAML (used to check YAML output) on first use.
- Nothing else for ports. The website needs [bun](https://bun.sh).

## Add a port

1. Open an issue with the **Port request** template first if you'd like a second opinion on the format.
2. Create `ports/<id>.py`. The id is the app's kebab-case name; the file uses underscores, e.g. `ports/windows_terminal.py` for `windows-terminal`. Copy a nearby port that uses the same kind of format.
3. Build and check just yours:

   ```sh
   uv run ./build.py --only <id>
   ```

   `--only` writes `dist/<id>/` and updates your entry in `dist/manifest.json`, keeping every other port. `build.py` parses JSON, TOML, YAML, XML, plist and Python output and fails loudly if a file doesn't parse; it prints a `⚠` for anything that breaks the contract below. If the app has a validator (a `--check` flag, a linter, loading it for real), use it too and say so in the PR.
4. Run the full build and commit `dist/` along with your port: `uv run ./build.py`. The full build also regenerates the README tables and the site's theme files. CI fails if anything differs from a fresh build.

Every file in `dist/<id>/` comes from the port: the build replaces the folder each time, so files placed there by hand disappear. Ship an asset (a screenshot, an icon) as an `Out` with `bytes` content.

### The contract

A port module defines `META` and `build(flavors)`. The docstring at the top of [`ports/_lib.py`](ports/_lib.py) is the reference for every field, including the optional ones (`auto`, `requires`, `detect`, `enable["sh"]`, `enable["file"]`). In short:

```python
from ports._lib import HEADER, Out

META = {
    "id": "ghostty",
    "name": "Ghostty",
    "category": "Terminals",  # one of CATEGORIES in ports/_lib.py
    "homepage": "https://ghostty.org",
    "enable": {"where": "~/.config/ghostty/config", "code": "theme = {name}", "lang": "conf"},
    "requires": "Ghostty 1.3+",
    "detect": ["ghostty", "/Applications/Ghostty.app"],
    "notes": "One or two plain sentences for the website.",
}


def build(flavors):
    return [
        Out(
            f.name,
            f"# {HEADER}\nbackground = {f.base}\n...",
            flavor=f.id,
            dest=f"~/.config/ghostty/themes/{f.name}",
            lang="conf",
        )
        for f in flavors
    ]
```

- `dest` is a path (`~/…`, `/…`, `%APPDATA%\…`, `$XDG_CONFIG_HOME/…`, or a project path like `styles/subway-seat.css`) or `None`. Directions ("double-click to import", "Settings › Theme › Import") go in `how`.
- `append=True` means the text is added to the end of the file at `dest`. Wrap it in `MARK_START`/`MARK_END` from `_lib`, in the comment syntax the target file uses, so uninstalling is deleting one block.
- `enable["code"]` is formatted per flavor with `{name}`, `{slug}`, `{snake}` and `{id}`. When it's fish-only, add a POSIX-shell `enable["sh"]`.
- Menu paths use `›` (`Settings › Appearance › Theme`); `→` means "then".

### File names

- **Default:** the flavor's slug and the app's extension: `subway-seat.toml`, `subway-seat-tunnel.toml`, `subway-seat-enamel.toml`.
- **The display name** (`Subway Seat Tunnel`) where the file name becomes the theme's name in the app: Ghostty, bat, iTerm2, Terminal.app, Sublime Text, Xcode, Notepad++, Alfred, Adobe Swatch Exchange, GIMP, Procreate, Gogh, the Obsidian theme folder.
- **snake_case** (`subway_seat_tunnel`) where the ecosystem needs an identifier: Helix, qutebrowser, Pygments modules, Starship palettes, vim-airline and lightline.
- Where an app looks a file up by the colorscheme's name (lualine's `theme = "auto"` loads `lualine/themes/<colors_name>.lua`), use exactly that name.

### Color rules

Write against **roles**, never hex. A test fails on any hex literal in `ports/` other than pure black, white and black overlays. The flavor object gives you every role as an attribute (`f.base`, `f.orange`, `f.text_hi`), plus `f.ansi` (the 16 terminal colors), `f.syntax("keyword")` and `f.mix(a, b, t)`. `_lib` has the shared derivations: `ink(f)` for text on an accent fill, `selection(f)` for apps without alpha, `tints(f)` for diff, search and diagnostic grounds, and `resolve("text@L3", f)` / `solid(…)` / `ui_colors(f)` for the layering system. Use them instead of local copies.

- **Grounds:** one chrome ground (`mantle`) for sidebars, panels, tab strips, title and status bars; the editor/content on `base`; `crust` only as 1px grooves and inactive title bars. Popovers go on `paper` (`resolve("paper", f)`), lifted with a hairline edge.
- **Hover and selection** are translucent text (`text@L1` … `text@L4`), so they sit right on any ground.
- **Syntax:** keywords orange, functions gold, strings avocado, types seafoam, numbers redbird, comments cardboard italic. `palette.SYNTAX` is the source of truth.
- **Light flavor:** `f.dark` is False for Enamel. Its ramp runs the other way (`crust` is the darkest ground; surfaces darken). Don't just invert: in light, raised things get brighter, not darker, and lines need a little more contrast.
- **Blue stays rare.** Denim is for links and info. Magenta is burnt orange.

### Diffs

Diffs are where themes usually look worst: syntax-highlighted code on green and red grounds, in lazygit, Claude Code, delta, VS Code and so on. `tints(f)` is tuned so every syntax color keeps about 3:1 or more on a line tint (the tests hold it there):

- Grounds: `add`/`del` for whole lines, `add_emph`/`del_emph` for changed words, `add_dim`/`del_dim` for faded diffs, `chg`/`chg_emph` for modified lines and words.
- `search`/`search_cur` for matches; `info`/`hint` for diagnostics.

For every port that shows diffs:

- Use these tints, never ad-hoc mixes.
- Keep syntax foregrounds on top of diff grounds. Don't flatten added lines to green text when the app can do backgrounds.
- `+`/`-` signs and gutter markers: `green` / `red_hi` (Enamel uses the same roles).
- Word emphasis must be clearly stronger than the line tint.
- Tint the line numbers in the diff gutter to match when the app supports it.
- Apps with only foreground colors: added text `green`, removed `red_hi`, hunk headers `denim`, file headers `text_hi` bold, context `text`/`subtext`.
- Check that "modified", "added" and "removed" gutter bars are distinct in all three flavors.
- Where you can render a real diff in the real tool (delta, git, lazygit, nvim `:diffthis`, VS Code), do it and look at it.

### Style

- Put `HEADER` in a comment at the top of any file whose format allows comments, in that format's syntax (`#`, `//`, `--`, `<!-- -->`, `;;`). That includes JSON-with-comments formats such as `.sublime-color-scheme`.
- **Strict JSON can't carry a header.** Files ending in `.json` are parsed as strict JSON by the build, so they get no comment. If the format has a free-text field of its own (a `description`) or a key the app ignores, the port may put `HEADER` there; don't invent keys the app might reject. The generated `dist/<id>/README.md` says where every file comes from. The exempt files are `.json`, `.md`, `.txt`, `.alfredappearance`, `.svg`, `LICENSE` and packaging dotfiles such as `.vscodeignore`; a test checks everything else.
- US spelling ("color", "gray", "center") everywhere, except names an app defines: tmux's `*-colour` options, eza's `colourful`, bottom's `*_colours`, Notepad++'s style names.
- Keep `notes` calm and plain: what it covers, anything a user needs to know. No marketing words. Version floors go in `requires`, not in `notes`.
- Match the key coverage of the best existing theme for that app (Catppuccin's port is usually the bar).

## Test

```sh
uv run --with pytest --with pyyaml pytest -q        # everything, in a few seconds
uv run --with pytest --with pyyaml pytest -q -k ghostty   # the tests for one port
uvx ruff check . && uvx ruff format --check .
uv run ./build.py --check                           # dist/, site tokens and README are current
```

The suite builds every port in memory (nothing is written to `dist/`) and checks the palette's roles and contrast, syntax contrast on the diff tints, each port's META and files, spelling, hex literals, the version, `install.tsv`, and that the build is deterministic. It also runs the Claude Code status line scripts when `bash` and `jq` are installed. CI runs the same suite on Python 3.12 and 3.14, loads the themes in Neovim, Vim, Emacs, fish, Starship, bat, tmux, Zellij and Ghostty, and lints the workflows and shell scripts.

## Everything else

- **Palette changes** go in `palette.py` and affect every port; open an issue with the **Palette change** template, with screenshots, before sending one.
- **The website** lives in `site/` (Next.js + StyleX). `cd site && bun install && bun run dev` serves it on port 8502; `bun run check` runs ESLint (with the StyleX rules), TypeScript and Biome.
- **Commits:** short imperative subject, a body if the why isn't obvious. Commit the rebuilt `dist/` in the same commit as the change that caused it.

Be kind in issues and reviews; see the [code of conduct](CODE_OF_CONDUCT.md).
