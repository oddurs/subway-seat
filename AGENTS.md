# AGENTS.md

Guide for coding agents working on Subway Seat: a 1970s walnut-brown color scheme generated for ~90 apps from one palette. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md), which has the same rules in more depth.

## Layout

```
palette.py        the only source of colors: roles, three flavors, SYNTAX, blend/alpha
ports/_lib.py     the port contract (read its docstring first) and shared helpers
ports/<id>.py     one module per app: META + build(flavors) -> list[Out]
build.py          runs every port → dist/<id>/, dist/manifest.json, dist/install.tsv,
                  site/src/theme/{tokens.stylex.ts,flavors.ts,palette.json}, README tables
dist/             generated, committed (every file has a stable URL)
tests/            pytest suite; builds everything in memory
site/             Next.js 16 + StyleX website (bun); reads dist/manifest.json
install.fish      installer (fish syntax); install.sh is the POSIX one
```

Flavors: Walnut (`subway-seat`, dark), Tunnel (`subway-seat-tunnel`, deeper dark), Enamel (`subway-seat-enamel`, light).

## Commands

```sh
uv run ./build.py                          # full build (Python 3.12+; uv brings it and PyYAML)
uv run ./build.py --only ghostty,bat       # some ports; keeps the rest of the manifest
uv run ./build.py --only ghostty --no-manifest   # port files only; safe to run in parallel
uv run ./build.py --check                  # fail if anything on disk differs from a fresh build
uv run --with pytest --with pyyaml pytest -q
uvx ruff check . && uvx ruff format --check .
cd site && bun install && bun run check    # the website: lint, types, format
```

`--only` doesn't regenerate the README tables or the site's theme files; run a full build before committing.

## The port contract

- `META`: `id` (kebab-case; the module is the id in snake_case), `name`, `category` (one of `CATEGORIES`), `homepage` (https), `notes`; optional `enable`, `auto`, `requires`, `detect`. Details in `ports/_lib.py`.
- `Out(path, content, flavor=None, dest=None, lang="text", append=False, how=None)`. `dest` is a real path or None; prose steps go in `how`. `append=True` content is wrapped in `MARK_START`/`MARK_END`.
- The build must print no `⚠` warnings for the ports you touch.
- Every file in `dist/<id>/` comes from the port; the build replaces the folder.

## Rules

- **Never hand-pick hex.** Use palette roles (`f.base`, `f.orange`) and `_lib` derivations (`ink`, `selection`, `tints`, `resolve`, `solid`, `ui_colors`). A test fails on hex literals in `ports/`.
- **Diffs:** use `tints(f)` grounds, keep syntax colors on top of them, `+`/`-` in `green`/`red_hi`. The full standard is in CONTRIBUTING.md, "Diffs".
- **Dark and light:** Enamel's ramp runs the other way; don't just invert. Denim (blue) only for links and info.
- **US spelling** ("color") in notes, generated files and docs, except names an app defines (tmux `*-colour`, eza `colourful`, bottom `*_colours`, Notepad++ style names).
- **Never hand-edit `dist/` or `site/src/theme/*`** (except `type.stylex.ts`); change the port or palette and rebuild. Don't commit a stale `dist/`: CI runs `./build.py --check`.
- **Version:** only in `pyproject.toml`; bumping it is in docs/RELEASE.md, "Cutting a release".
- **Shell:** `install.fish` and `enable["code"]` with `lang: "fish"` are fish syntax; give a POSIX `enable["sh"]` alongside.
- **Tone:** notes are calm, plain and specific. Menu paths use `›`.
- **Commits:** short imperative subject. No `Co-Authored-By` trailers, "Generated with" lines or any other AI attribution in commits or PRs.
- Verify formats against the real tool or upstream source where you can, and say how in the PR.
