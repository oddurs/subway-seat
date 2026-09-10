# Releasing Subway Seat

How Subway Seat gets from this repo onto people's screens: where it's listed, in what order, and what to say when it goes out. Researched 2026-09-10 against each channel's own README, CONTRIBUTING file and recent merged PRs; anything unverified is marked.

The short version: **one YAML file in iTerm2-Color-Schemes** reaches Ghostty, Windows Terminal themes and ~40 generated terminal formats. Everything else is either a registry with a lead time (start those first) or a place to say hello on launch day.

---

## 1. What we're launching

- **Name:** Subway Seat. Flavors: **Subway Seat** (Walnut, dark), **Subway Seat Tunnel** (deeper dark), **Subway Seat Enamel** (light).
- **One line:** A warm, walnut-brown color scheme from a 1970s subway car: parchment text, harvest gold, burnt orange, avocado. Sit back.
- **Proof points:** ~90 ports from one `palette.py`; a real layered VS Code/Zed workbench; the deepest Claude Code theme there is (themes, status line, subagent rows, spinner verbs, tips, output style, all in one plugin); ports for opencode, Codex, Gemini CLI, Aider and herdr.
- **Voice:** relaxed and plain. No hype words, no "blazing", no emoji walls. Let the screenshots do the work.

## 2. Repo shape

- **Hub monorepo:** `oddurs/subway-seat` holds the generator, `dist/` (committed, so every file has a stable URL), the site and docs. Most ports are just files people copy, so they live here, like Flexoki and Tokyo Night's extras.
- **Satellite repos (planned), only where a registry needs the package at the repo root.** None of these repos exist yet, and nothing syncs them. The plan: a `satellites` job in `release.yml` (`needs: release`) that runs `git subtree split --prefix=<src>` for each row and pushes the result and the tag with a per-repo deploy key, so they never drift:

  | Satellite | Why | Source | Status |
  |---|---|---|---|
  | `subway-seat.nvim` | lazy.nvim/packer install by `owner/repo`; awesome-neovim and vimcolorschemes index repos | `dist/nvim` + `dist/vim/colors` (two folders, so staged through a copy, not one subtree split) | planned |
  | `subway-seat-theme.el` | MELPA recipe points at a dedicated repo | `dist/emacs` | planned |
  | `subway-seat-sublime` | Package Control: one package per repo, semver tags | `dist/sublime-text` | planned |
  | `subway-seat-obsidian` | Obsidian needs `manifest.json` + `theme.css` at the root and a release per version (so the job also needs a token that can create releases there) | `dist/obsidian` | planned |

- VS Code (vsce/ovsx, planned), Zed (`path = "dist/zed"` in `extensions.toml`), JetBrains (upload) and the Claude Code plugin (marketplace in this repo, live) all publish straight from the monorepo.
- **An org later, maybe.** A `subway-seat` GitHub org (Catppuccin/Rosé Pine model) is worth it once other people maintain ports. Orgs are created in the web UI; transfer the repos then and GitHub keeps redirects.

## 3. Start now: things with lead times

| When | What | Why it can't wait | Status |
|---|---|---|---|
| Today | Register a domain (e.g. `subwayseat.dev`) and point the site at it | The VS Code **verified publisher** badge needs a domain ≥ 6 months old plus 6 months of Marketplace history | not started |
| Today | Create the VS Code publisher (`oddurs`) and an Open VSX namespace; file the Open VSX [namespace ownership claim](https://github.com/eclipse-openvsx/openvsx/wiki/Namespace-Access) | Unclaimed namespaces show an "unverified" warning | not started |
| Today | Set up **Microsoft Entra ID** publishing for `vsce` in CI (vsce ≥ 2.26.1); see §7 | Azure DevOps global PATs retire **December 1, 2026**; the classic `vsce login` PAT flow stops working | planned |
| Today | JetBrains vendor profile; Obsidian community account linked to GitHub | Account review takes days | not started |
| Today | Create `subway-seat.nvim` and `subway-seat-theme.el` (public), add topics `neovim-colorscheme`, `vim-colorscheme`, `nvim-theme`, `colorscheme` | MELPA wants the repo public ≥ 1 month; awesome-neovim wants ≥ 1 week; vimcolorschemes.com indexes by topic + ≥ 1 star | not started |
| Today | Turn on private vulnerability reporting, Dependabot alerts, and rulesets for `main` and `v*` tags | SECURITY.md and CODE_OF_CONDUCT.md point at the private reporting form | not started |
| T−2 weeks | Open the slow PRs (Zed, Package Control, Helix) so they land near launch | Reviews take weeks; Helix also has a release lag | not started |

## 4. Upstream submissions

In priority order. "AI disclosure" marks channels whose rules ask you to say an agent helped.

| # | Channel | What to submit | Notes |
|---|---|---|---|
| 1 | **[iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)** (27k★) | `yaml/Subway Seat.yml`, `yaml/Subway Seat Tunnel.yml`, `yaml/Subway Seat Enamel.yml` (Gogh YAML + `cursor_text`, `selection`, `selection_text`, `bold`, `link`, `tab`, `author`, `variant`). Filename = display name. Run `tools/gen.py -s "Subway Seat"` and the screenshot generator. | **Feeds Ghostty's built-in list** (weekly bump), windowsterminalthemes.dev and ~40 generated formats. `gen.py` may nudge colors to 1.75:1 contrast — check the output. **AI disclosure** (AGENTS.md). Merges in 1–9 days. |
| 2 | **[Gogh](https://github.com/Gogh-Co/Gogh)** (10k★) | `themes/Subway Seat.yml` ×3 — no underscores, uppercase hex, `variant`. PR title `theme: Add Subway Seat`. `task validate`. | Same YAML as #1 with uppercase hex. |
| 3 | **[tinted-theming/schemes](https://github.com/tinted-theming/schemes)** | `base16/subway-seat*.yaml` and `base24/…` from `dist/base16` | Upstream of nixpkgs `base16-schemes` → Stylix users. Merges in days. |
| 4 | **[kitty-themes](https://github.com/kovidgoyal/kitty-themes)** | `themes/Subway_Seat.conf` ×3 with `## name/author/license/upstream/blurb` header, screenshot in PR | Reaches every `kitten themes` user. |
| 5 | **[alacritty-theme](https://github.com/alacritty/alacritty-theme)** | `themes/subway_seat*.toml`, screenshot via `print_colors.sh`, README row | Merge time varies. |
| 6 | **[btop](https://github.com/aristocratos/btop/tree/main/themes)** | `themes/subway-seat*.theme` incl. newer `proc_*`/`followed_*` keys | Actively taking themes. |
| 7 | **[Zed extensions](https://github.com/zed-industries/extensions)** | Submodule + `extensions.toml` entry, id `subway-seat-theme`, `path = "dist/zed"`, MIT LICENSE at that path | Fork to a *personal* account. First feedback can take weeks. |
| 8 | **VS Code Marketplace + Open VSX** (planned) | `vsce publish` / `ovsx publish` from CI on tag, once the publisher, namespace and credentials exist | Cursor, Windsurf and VSCodium pull from Open VSX. vscodethemes.com indexes automatically. Until then, install `dist/vscode/subway-seat.vsix` by hand. |
| 9 | **JetBrains Marketplace** | Upload `dist/jetbrains/subway-seat-jetbrains.jar`; 40×40 SVG logo; 1280×800 screenshots | Name ≤ 30 chars, no "Theme/Plugin/JetBrains". 3–4 working days. |
| 10 | **Obsidian** | Submit on community.obsidian.md from `subway-seat-obsidian` (release tag = version, `manifest.json` + `theme.css` attached, 512×288 screenshot) | Theme name can't contain "Theme" and **can't change after submission**. |
| 11 | **[Helix](https://github.com/helix-editor/helix/blob/master/runtime/themes/README.md)** | `runtime/themes/subway_seat*.toml` + author/license header | Weeks to review, then a release lag; the TOML ships here meanwhile. |
| 12 | **Package Control** | Channel PR `Add Subway Seat` pointing at `subway-seat-sublime` (semver tags) | "A few weeks". Ship `.sublime-color-scheme` and `.tmTheme`. |
| 13 | **MELPA** (planned) | `recipes/subway-seat-theme` after `subway-seat-theme.el` has been public for 1 month; `package-lint` clean | **AI disclosure** (`Assisted-by:`). |
| 14 | **Claude Code plugins** | This repo already is a marketplace (`/plugin marketplace add oddurs/subway-seat`); also submit to the community directory via [claude.ai/admin-settings/directory/submissions/plugins/new](https://claude.ai/admin-settings/directory/submissions/plugins/new) | `claude plugin validate --strict` runs in CI. |
| 15 | **yazi flavors** | `subway-seat.yazi` folder (flavor.toml, tmtheme.xml, preview.png, LICENSE) + link PR to [yazi-rs/flavors](https://github.com/yazi-rs/flavors) | Flavors are beta. |
| 16 | **[ray.so themes](https://github.com/raycast/ray-so)** | `app/(navigation)/themes/themes/<user>/subway-seat.json` | |
| 17 | **Spicetify Marketplace** | Topic `spicetify-themes` + root `manifest.json` | spicetify-themes itself no longer takes themes. |
| 18 | **fzf wiki, userstyles.world, Dotfyle** | Wiki entry, userstyle mirror, Dotfyle form | Minutes each. |

**Closed or not worth a PR (ship the files here instead):** bat (not accepting new default themes), spicetify-themes (closed to new themes), Starship presets (PRs sit for years), WezTerm's bundled list (last sync 2024-07), fish bundling (curated — revisit if it gets popular), delta's `themes.gitconfig` (themes must be named after a wild organism — "Avocado" would qualify if we want it), Alfred Gallery (workflows only).

## 5. Launch day

Order matters less than being around to answer questions. Post from a real desktop, not a mockup.

1. Tag `v1.0.0` (see "Cutting a release" below). CI drafts the GitHub release with the dist zip, the VSIX, the JetBrains JAR and the Firefox add-ons, and publishes VS Code + Open VSX; the satellite sync joins once it exists. Publish the draft.
2. Site live on the domain, with the flavor switcher and every port page.
3. **Show HN** — link the site, stay in the thread for the day. Don't ask anyone to upvote.
4. **r/unixporn** — read the sidebar and flair list first; a `[OC]`/WM-tagged title and a details comment have been required. One real screenshot: Ghostty + Neovim + herdr + Claude Code on Walnut.
5. **r/neovim, r/vscode, r/commandline** — check each sub's self-promotion rule (unverified).
6. **Bluesky + Mastodon thread** — four images (editor, terminal, Enamel, the palette card), alt text on every one, #ColorScheme #Neovim #Ghostty #VSCode.
7. **Obsidian forum** "Share & showcase" + Discord #updates after the theme is approved.

### Drafts

**Show HN**

> Show HN: Subway Seat – a 70s subway-car color scheme, generated for 90 apps
>
> I wanted my terminal to feel like the orange-and-brown subway cars and wood-paneled living rooms of the 1970s, so I made a palette: walnut ground, parchment text, harvest gold, burnt orange, avocado. It has three flavors (dark, deeper dark, light).
>
> Everything is generated from one Python file with no dependencies — Ghostty, VS Code, Neovim, Zed, JetBrains, Helix, tmux, lazygit, Obsidian and ~80 more. The VS Code and Zed themes use a layering system (one chrome ground, translucent hovers and selections) that I borrowed from studying GitHub Dimmed, Catppuccin and Rosé Pine.
>
> The Claude Code port goes further than colors: a station-sign status line, subagent rows, 70s spinner verbs ("Sinking into the shag"), tips and a relaxed output style, bundled as a plugin.
>
> Site with previews and every config: <url>. Happy to answer anything about the generator or the color choices.

**Bluesky / Mastodon (thread of 3)**

> 1/ Subway Seat: a color scheme from a 1970s subway car. Walnut paneling, orange bucket seats, cream enamel, avocado. Three flavors, ~90 apps, one palette file. <url>
>
> 2/ The whole spectrum isn't invited. Blue is faded denim and only marks links; magenta got reassigned to burnt orange. Everything stays in the same warm room.
>
> 3/ It goes deep in Claude Code: a station-sign status line, subagent rows, spinner verbs like "Flipping the record", and a relaxed output style. /plugin marketplace add oddurs/subway-seat

**r/unixporn title**

> [Ghostty] Subway Seat — sinking into a 70s subway car

**dev.to / blog outline — "90 ports from one palette"**

1. Why brown (and why the whole spectrum doesn't belong).
2. Roles, not hex: one flavor table, every port written against roles.
3. The layering system: what GitHub Dimmed, Catppuccin, Rosé Pine and Everforest taught me about grounds, seams and translucent ink.
4. Agent harnesses are the new editors: theming Claude Code, opencode, Codex and Gemini CLI.
5. Shipping: iTerm2-Color-Schemes is the secret front door to Ghostty.

## 6. Assets

- **Screenshots** at 2560×1600 per flavor: Ghostty (fish + starship + eza + rg), Neovim, VS Code, Zed, herdr + Claude Code, Obsidian. A catwalk-style composite of all three flavors for the README and OG image.
- **Palette card** (the site's swatch section, exported) and **wallpapers** in each flavor.
- **Store assets:** VS Code 256px PNG icon + `galleryBanner` #362619; JetBrains 40×40 SVG + 1280×800 screenshots; Obsidian 512×288; Product Hunt is a weak fit for a free theme — skip.

## 7. Versions and releases

- **Semver across the board.** `0.x` until launch; `1.0.0` on launch day. A color change that alters how existing code looks is a minor bump; a fixed key or new port is a patch.
- **One tag releases everything.** Pushing `vX.Y.Z` runs `release.yml`: the full CI workflow first, then a check that the tag matches `version` in `pyproject.toml` and that CHANGELOG.md has a dated `## [X.Y.Z]` section, then `./build.py --check`. It drafts a GitHub release with that CHANGELOG section as notes and attaches `subway-seat-X.Y.Z-dist.zip`, `subway-seat-X.Y.Z.vsix`, the JetBrains JAR and the Firefox `.xpi` files. It publishes to the VS Code Marketplace and Open VSX only when `VSCE_PAT` / `OVSX_PAT` are set (neither is yet). The satellite sync is planned (§2). You review the draft and publish it.
- **No tags exist yet.** The first tag is `v0.3.0`, cut after the current round of fixes lands. 0.1.0 and 0.2.0 were never tagged.
- **Stable file URLs.** `dist/` is committed and file names don't carry the version (`dist/vscode/subway-seat.vsix`), so links from READMEs and upstream PRs keep working; only the release assets are versioned.
- VS Code allows only `major.minor.patch`; if pre-releases are ever needed, use odd minor versions.
- **CHANGELOG.md** in Keep a Changelog format; each release note leads with a screenshot when colors change.

### Cutting a release

1. Bump `version` in `pyproject.toml` (the only place it lives), then run `uv lock` so `uv.lock` matches.
2. In CHANGELOG.md, turn `## [X.Y.Z] - Unreleased` into `## [X.Y.Z] - YYYY-MM-DD` and point its link at `compare/<previous tag>...vX.Y.Z` (the first release compares from `744219f`).
3. Run `uv run ./build.py` and `uv run --with pytest --with pyyaml pytest -q`, then commit, with `dist/`, on `main`.
4. `git tag -s vX.Y.Z -m "Subway Seat X.Y.Z"`, then `git push origin main vX.Y.Z`.
5. Watch the Release workflow, read the draft release, and publish it.

Protect `v*` tags with a ruleset (no deletion, no force-push, no update) so a published tag can't move.

### VS Code publishing with Entra ID

`release.yml` still publishes with a `VSCE_PAT` secret, and those PATs stop working when Azure DevOps retires global PATs on **December 1, 2026**. The replacement, following the [VS Code publishing docs](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) (vsce ≥ 2.26.1):

1. In Azure, create a user-assigned managed identity. Add a federated credential for GitHub Actions: issuer `https://token.actions.githubusercontent.com`, subject `repo:oddurs/subway-seat:environment:marketplace`.
2. In the Visual Studio Marketplace, add that identity as a member of the `oddurs` publisher with the Contributor role.
3. In the repo, create a `marketplace` environment (limited to `v*` tags) holding the identity's client ID and tenant ID as variables. No secret is stored.
4. In `release.yml`, give the publishing job `environment: marketplace` and `id-token: write`, add a pinned `azure/login` step (`client-id`, `tenant-id`, `allow-no-subscriptions: true`), and run `npx --yes @vscode/vsce@<pinned> publish --azure-credential --packagePath dist/vscode/subway-seat.vsix`.
5. Delete the `VSCE_PAT` secret and step. Open VSX is separate and keeps its `OVSX_PAT`.

## 8. After launch

- **Port requests** via the issue template; a port is one Python file (`ports/<id>.py`), so contributors can add one without touching anything else. `CONTRIBUTING.md` walks through it.
- **Watch:** Marketplace installs, Open VSX downloads, plugin installs, stars, and which port pages the site's visitors open (plain server logs, no tracking).
- **Later channels:** fish bundling, delta (as "Avocado"), the Cursor Agents Window theme format once it ships, Crush when it gets themes (PR #3608).
