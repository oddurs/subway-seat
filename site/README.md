# Subway Seat — site

Next.js 16 (App Router, Turbopack) styled with StyleX. Serves on port **8502**.

```fish
bun install
bun run dev      # http://localhost:8502 — regenerates the theme first
bun run build    # static build; `bun run start` serves it on the same port
bun run check    # eslint (incl. @stylexjs rules) + tsc + biome format check
```

## How it fits together

- `../palette.py` is the only place colours live. `../build.py` writes every app theme into `../dist/`
  **and** this site's `src/theme/tokens.stylex.ts` + `src/theme/palette.ts` (don't edit those two).
  `predev` / `prebuild` run it for you.
- The editor preview and every config block are highlighted by Shiki using the generated VS Code
  theme from `../dist/`, so the site shows exactly what gets installed.
- `/files/[id]` serves the dist files as downloads, prerendered at build time.

## StyleX setup

- `babel.config.js` — `@stylexjs/babel-plugin`; Next 16 applies it under Turbopack and webpack.
- `postcss.config.js` — `@stylexjs/postcss-plugin` swaps the `@stylex;` directive in
  `src/app/globals.css` for the compiled atomic CSS (in `@layer`s, above `@layer resets`).
- `eslint.config.mjs` — Next's config plus `@stylexjs/eslint-plugin`.
- `biome.json` — formatter only.
