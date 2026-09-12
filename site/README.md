# Subway Seat — site

Next.js 16 (App Router, Turbopack) styled with StyleX. Serves on port **8502**.

```fish
bun install
bun run dev          # http://localhost:8502 — regenerates the theme first
bun run build        # production build; `bun run start` serves it on the same port
bun run check        # eslint (incl. @stylexjs rules) + tsc + biome format check

# the GitHub Pages site, as CI deploys it, into out/
STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/subway-seat bun run build
bun run check:links  # every internal href/src/og:image in out/ resolves under the base path
```

## How it fits together

- `../palette.py` is the only place colors live. `../build.py` writes every app theme into
  `../dist/` (plus `dist/manifest.json`, which the site reads) **and** this site's
  `src/theme/tokens.stylex.ts`, `src/theme/flavors.ts` and `src/theme/palette.json`. Don't edit
  those three (`type.stylex.ts` is hand-written); `predev` / `prebuild` run the build for you with
  `python3`, which must be 3.12 or newer.
- The editor preview and every config block are highlighted by Shiki with the generated VS Code
  themes from `../dist/`, so the site shows exactly what gets installed. The terminal and herdr
  mocks read their colors from the generated eza and Claude Code themes the same way.
- `src/theme/ink.stylex.ts` holds the few site-only text colors: the accents on the dark flavors,
  and mixes toward text on Enamel so small text clears 4.5:1.
- Routes that turn `dist/` into downloads, all prerendered at build time:
  - `/files/[...path]` — each generated file.
  - `/zip/<id>-<flavor>.zip` — "Download all" for ports with more than one file.
  - `/code/[...path]` — the whole of a long file, highlighted, for a port page's "Show all" (pages
    carry the first 150 lines).
  - `/og/<name>.png` — share images (`src/og/card.tsx`, fonts in `src/og/`).
  - `/install.sh` — the repo's `../install.sh` (a stub that says so when it's missing).
- `/install` is the setup configurator: it writes the `install.sh` one-liner, the
  `~/.config/subway-seat/config` file and the clone command from a flavor and a set of apps.
  Whether a port is set up automatically, with one step or by hand comes from the manifest's
  `installs` (checked against `install.sh` by the tests), and port pages use the same answer.
- `/shot/[name]` renders one demo on a plain ground for README and store screenshots
  (`?flavor=tunnel|enamel`).

## StyleX setup

- `babel.config.js` — `@stylexjs/babel-plugin`; Next 16 applies it under Turbopack and webpack.
- `postcss.config.js` — `@stylexjs/postcss-plugin` swaps the `@stylex;` directive in
  `src/app/globals.css` for the compiled atomic CSS (in `@layer`s, above `@layer resets`).
- `eslint.config.mjs` — Next's config plus `@stylexjs/eslint-plugin`.
- `biome.json` — formatter only.
