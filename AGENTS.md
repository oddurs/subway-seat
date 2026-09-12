# AGENTS.md

Guide for coding agents working on Subway Seat: transit color schemes generated for 117 apps from one palette. Three families — New York, London, Paris — of three flavors each, all filling the same 26 roles. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md), which has the same rules in more depth.

## Layout

```
palette.py        the only source of colors: roles, families, flavors, SYNTAX, blend/alpha
ports/_lib.py     the port contract (read its docstring first) and shared helpers
ports/<id>.py     one module per app: META + build(flavors) -> list[Out]
build.py          runs every port → dist/<id>/, dist/manifest.json, dist/install.tsv,
                  site/src/theme/{tokens.stylex.ts,flavors.ts,palette.json}, README tables
dist/             generated, committed (every file has a stable URL)
tests/            pytest suite; builds everything in memory
site/             Next.js 16 + StyleX website (bun); reads dist/manifest.json
install.sh        the installer (POSIX sh; reads dist/install.tsv); install.fish wraps it
```

Families and flavors:

| Family | Dark | Deeper dark | Light | Lead accent |
|---|---|---|---|---|
| **New York** | Walnut | Tunnel | Enamel | burnt orange |
| **London** | Moquette | Deep Level | Portland | Corporate red |
| **Paris** | Guimard | Catacombes | Carrelage | line 4 magenta |

## The split

One spine, three cities. Know which half you're touching before you touch it.

**The spine** — change it and every family changes at once:

- the 26 roles, the `SYNTAX` map, `ROLE_USES`, `ACCENT_ROLES`
- the derivations in `_lib`: `tints`, `ink`, `selection`, `pair`, the `INK` layering levels
- the port contract, and the installer
- the contrast floors in `tests/test_palette.py`
- **the perceived lightness ladder** — the 26 OKLab L values every flavor sits on
- the site's spacing scale and page frame

**A family** — its own, and nobody else's: the hex behind each role, its role names,
its three flavors, its lead accent, its signage colors, its corner radii, its filename
prefix, and its furniture on the site.

**A port may never branch on a family, or name a flavor id.** If you need the dark
and light of a flavor's own family, that's `pair(f)`; for the family itself,
`family_of(f)`; for filenames, `f.prefix`; for the name of a role, `f.role_names`.
Three ports got this wrong and it only showed when a second family arrived.

## Commands

```sh
uv run ./build.py                          # full build (Python 3.12+; uv brings it and PyYAML)
uv run ./build.py --only ghostty,bat       # some ports; keeps the rest of the manifest
uv run ./build.py --only ghostty --no-manifest   # port files only; safe to run in parallel
uv run ./build.py --check                  # fail if anything on disk differs from a fresh build
uv run --with pytest --with pyyaml pytest -q
uvx ruff check .   # no ruff format: the ports keep their hand-aligned color tables
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
- **Solve a new flavor, don't eyeball it.** Work in OKLab. Take the sibling flavor's
  L for all 26 roles unchanged — that's what keeps the families at one visual weight
  and makes every contrast floor transfer — and vary only hue and chroma. Then run the
  floors before you write the values down. Hand-tuning in HSL is what produced three
  rounds of failures: its lightness isn't perceptual, so equal steps aren't equal.
- **The chroma curve flips with polarity.** A dark flavor pulls chroma out toward
  `text`, so pale type stays white. A light flavor must do the opposite: there `text`
  is the inked end and the paper is the pale one, and tapering it leaves the greys
  dead neutral.
- **Accents come in two bands, not one.** The four used as large fills — `red`,
  `orange`, `yellow`, `green`, which is what a powerline prompt and the diff grounds
  paint with — hold a tight even chroma band, or the stripe wobbles. The rest
  (`sage`, `denim`, `clay`) are only ever text, and stay quiet.
- **Diffs:** use `tints(f)` grounds, keep syntax colors on top of them, `+`/`-` in `green`/`red_hi`. The full standard is in CONTRIBUTING.md, "Diffs".
- **Dark and light:** Enamel's ramp runs the other way; don't just invert. Denim (blue) only for links and info.
- **US spelling** ("color") in notes, generated files and docs, except names an app defines (tmux `*-color`, eza `colorful`, bottom `*_colors`, Notepad++ style names).
- **Never hand-edit `dist/` or `site/src/theme/*`** (except `type.stylex.ts`); change the port or palette and rebuild. Don't commit a stale `dist/`: CI runs `./build.py --check`.
- **Version:** only in `pyproject.toml`; bumping it is in docs/RELEASE.md, "Cutting a release".
- **Shell:** `install.fish` and `enable["code"]` with `lang: "fish"` are fish syntax; give a POSIX `enable["sh"]` alongside.
- **Tone:** notes are calm, plain and specific. Menu paths use `›`.
- **Commits:** short imperative subject. No `Co-Authored-By` trailers, "Generated with" lines or any other AI attribution in commits or PRs.
- Verify formats against the real tool or upstream source where you can, and say how in the PR.

## The site

- **Generated, not hand-written:** `site/src/theme/*` and the block between the
  `flavors:start` / `flavors:end` markers in `globals.css`. Hand-written CSS can't match
  a flavor id generically, so every rule that names one is emitted by `build.py` and a
  new family costs nothing. `type.stylex.ts` is the one theme file you may edit.
- **`data-only` / `data-unless`** show and hide content by flavor or family. Prefer them
  to JavaScript state for anything visible: a control that draws both of its states and
  lets CSS pick is correct in the first painted frame, where `useSyncExternalStore` is
  only correct after hydration.
- **Three token sets, three jobs.** `color` is the theme. `art` is decorative color for
  site graphics — a light flavor's accents are solved to carry small text on paper, so
  they come out too dark for a supergraphic, and `art` lifts them part of the way toward
  the family's dark default. `ink` is site text: `ink.fill` is the family's lead accent,
  so a primary button is always the one color that family spends on identity.
- **Type and spacing are tokens.** Faces, scale, leading, tracking and the variable-font
  axes live in `type.stylex.ts`, overridden per family in `faces.ts`, so a headline is
  one element in the markup rather than one per city. Two faces belong to no city: code
  is JetBrains Mono, and app-mockup chrome is Inter. Spacing is deliberately shared —
  color and type are where a family is itself, but a page that changed its measure
  between cities would read as three sites.
- **A light flavor needs the opposite type correction to a dark one.** Light type on a
  dark ground haloes and reads heavy; dark type on pale ground reads thin and loose. The
  dark flavors open their tracking, the light ones close it up.
- **Adding a new `.stylex.ts` file needs a dev-server restart.** StyleX will otherwise
  emit the class names with no declarations, and the rule silently does nothing.
- **Look at it.** `bun run dev`, then screenshot with headless Chrome. Every real bug
  this design went through — a roundel drawn as a disc, a weave where every accent came
  out the same color, a workbench still painted in another city, a control showing no
  city selected — was invisible in the diff and obvious in a picture.
