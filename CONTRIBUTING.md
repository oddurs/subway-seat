# Contributing

Thanks for wanting to add to the car. The most common contribution is a new port, and a port is one Python file.

## Add a port

1. Open an issue with the **Port request** template first if you'd like a second opinion on the format.
2. Create `ports/<id>.py` (the id is the app's kebab-case name; the file uses underscores, e.g. `ports/windows_terminal.py` for `windows-terminal`). Copy a nearby port that uses the same kind of format.
3. Build and check just yours:

   ```sh
   uv run --with pyyaml ./build.py --only <id>
   ```

   `build.py` parses JSON, TOML, YAML, XML and plist output and fails loudly if a file doesn't parse. If the app has a validator (a `--check` flag, a linter, loading it for real), use it too and say so in the PR.
4. Run the full build and commit `dist/` along with your port: `./build.py`. CI fails if `dist/` is out of date.

### The contract

A port module defines `META` and `build(flavors)`. See the docstring at the top of [`ports/_lib.py`](ports/_lib.py) for every field; in short:

```python
from ports._lib import HEADER, Out

META = {
    "id": "ghostty",
    "name": "Ghostty",
    "category": "Terminals",  # Terminals, Editors, Agents, Shell & prompt, CLI & TUI, Apps, Palettes
    "homepage": "https://ghostty.org",
    "enable": {"where": "~/.config/ghostty/config", "code": "theme = {name}", "lang": "conf"},
    "notes": "One or two plain sentences for the website.",
}

def build(flavors):
    return [
        Out(f.name, f"background = {f.base}\n...", flavor=f.id,
            dest=f"~/.config/ghostty/themes/{f.name}", lang="conf")
        for f in flavors
    ]
```

### Colour rules

Write against **roles**, never hex. The flavor object gives you every role as an attribute (`f.base`, `f.orange`, `f.text_hi`), plus `f.ansi` (the 16 terminal colours), `f.syntax("keyword")`, `f.mix(a, b, t)`, and in `_lib`: `tints(f)` for diff/search backgrounds and `resolve("text@L3", f)` for the layering system.

- **Grounds:** one chrome ground (`mantle`) for sidebars, panels, tab strips, title and status bars; the editor/content on `base`; `crust` only as 1px grooves and inactive title bars. Popovers go on `paper` (`resolve("paper", f)`), lifted with a hairline edge.
- **Hover and selection** are translucent text (`text@L1` … `text@L4`), so they sit right on any ground.
- **Syntax:** keywords orange, functions gold, strings avocado, types seafoam, numbers redbird, comments cardboard italic. `palette.SYNTAX` is the source of truth.
- **Light flavor:** `f.dark` is False for Enamel. Its ramp runs the other way (`crust` is the darkest ground; surfaces darken). Text on an accent fill is `f.crust if f.dark else f.base`. Don't just invert: in light, raised things get brighter, not darker, and lines need a little more contrast.
- **Blue stays rare.** Denim is for links and info. Magenta is burnt orange.

### Style

- Put `HEADER` in a comment at the top of any file whose format allows comments.
- Keep `notes` calm and plain: what it covers, anything a user needs to know. No marketing words.
- Match the key coverage of the best existing theme for that app (Catppuccin's port is usually the bar).

## Everything else

- **Palette changes** go in `palette.py` and affect every port; open an issue with a screenshot before sending one.
- **The website** lives in `site/` (Next.js + StyleX). `cd site && bun install && bun run dev` serves it on port 8502; `bun run check` runs ESLint (with the StyleX rules), TypeScript and Biome.
- **Commits:** short imperative subject, a body if the why isn't obvious.

Be kind in issues and reviews; see the [code of conduct](CODE_OF_CONDUCT.md).
