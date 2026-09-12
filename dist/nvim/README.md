# Subway Seat for Neovim

A plugin: `setup({ background, transparent, italics, overrides })`, flavors that follow `background` (flip it and Walnut becomes Enamel and back), lualine themes, and groups for Tree-sitter, LSP and about 70 plugins (mini, snacks, blink.cmp, telescope, gitsigns, diffview, neogit and more). Install with lazy.nvim: `{ "oddurs/subway-seat", lazy = false, priority = 1000, config = function(p) vim.opt.rtp:append(p.dir .. "/dist/nvim"); vim.cmd.colorscheme("subway-seat") end }`, or vim-plug: `Plug 'oddurs/subway-seat', { 'rtp': 'dist/nvim' }`. Or copy `dist/nvim` into `~/.config/nvim`; the colors files also work on their own.

[Neovim](https://neovim.io) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/nvim/) · Needs Neovim 0.9+

## Files

| Flavor | File | Where it goes |
|---|---|---|
| All three | [`colors/subway-seat.lua`](colors/subway-seat.lua) | `~/.config/nvim/colors/subway-seat.lua` |
| Subway Seat | [`colors/subway-seat-walnut.lua`](colors/subway-seat-walnut.lua) | `~/.config/nvim/colors/subway-seat-walnut.lua` |
| Subway Seat Tunnel | [`colors/subway-seat-tunnel.lua`](colors/subway-seat-tunnel.lua) | `~/.config/nvim/colors/subway-seat-tunnel.lua` |
| Subway Seat Enamel | [`colors/subway-seat-enamel.lua`](colors/subway-seat-enamel.lua) | `~/.config/nvim/colors/subway-seat-enamel.lua` |
| London Moquette | [`colors/london-moquette.lua`](colors/london-moquette.lua) | `~/.config/nvim/colors/london-moquette.lua` |
| London Deep Level | [`colors/london-deep.lua`](colors/london-deep.lua) | `~/.config/nvim/colors/london-deep.lua` |
| London Portland | [`colors/london-portland.lua`](colors/london-portland.lua) | `~/.config/nvim/colors/london-portland.lua` |
| Paris Guimard | [`colors/paris-guimard.lua`](colors/paris-guimard.lua) | `~/.config/nvim/colors/paris-guimard.lua` |
| Paris Catacombes | [`colors/paris-catacombes.lua`](colors/paris-catacombes.lua) | `~/.config/nvim/colors/paris-catacombes.lua` |
| Paris Carrelage | [`colors/paris-carrelage.lua`](colors/paris-carrelage.lua) | `~/.config/nvim/colors/paris-carrelage.lua` |
| All three | [`lua/subway-seat/init.lua`](lua/subway-seat/init.lua) | `~/.config/nvim/lua/subway-seat/init.lua` |
| All three | [`lua/subway-seat/palette.lua`](lua/subway-seat/palette.lua) | `~/.config/nvim/lua/subway-seat/palette.lua` |
| All three | [`lua/lualine/themes/subway-seat.lua`](lua/lualine/themes/subway-seat.lua) | `~/.config/nvim/lua/lualine/themes/subway-seat.lua` |
| Subway Seat | [`lua/lualine/themes/subway-seat-walnut.lua`](lua/lualine/themes/subway-seat-walnut.lua) | `~/.config/nvim/lua/lualine/themes/subway-seat-walnut.lua` |
| Subway Seat | [`lua/lualine/themes/subway_seat.lua`](lua/lualine/themes/subway_seat.lua) | `~/.config/nvim/lua/lualine/themes/subway_seat.lua` |
| Subway Seat Tunnel | [`lua/lualine/themes/subway-seat-tunnel.lua`](lua/lualine/themes/subway-seat-tunnel.lua) | `~/.config/nvim/lua/lualine/themes/subway-seat-tunnel.lua` |
| Subway Seat Tunnel | [`lua/lualine/themes/subway_seat_tunnel.lua`](lua/lualine/themes/subway_seat_tunnel.lua) | `~/.config/nvim/lua/lualine/themes/subway_seat_tunnel.lua` |
| Subway Seat Enamel | [`lua/lualine/themes/subway-seat-enamel.lua`](lua/lualine/themes/subway-seat-enamel.lua) | `~/.config/nvim/lua/lualine/themes/subway-seat-enamel.lua` |
| Subway Seat Enamel | [`lua/lualine/themes/subway_seat_enamel.lua`](lua/lualine/themes/subway_seat_enamel.lua) | `~/.config/nvim/lua/lualine/themes/subway_seat_enamel.lua` |
| London Moquette | [`lua/lualine/themes/london-moquette.lua`](lua/lualine/themes/london-moquette.lua) | `~/.config/nvim/lua/lualine/themes/london-moquette.lua` |
| London Moquette | [`lua/lualine/themes/london_moquette.lua`](lua/lualine/themes/london_moquette.lua) | `~/.config/nvim/lua/lualine/themes/london_moquette.lua` |
| London Deep Level | [`lua/lualine/themes/london-deep.lua`](lua/lualine/themes/london-deep.lua) | `~/.config/nvim/lua/lualine/themes/london-deep.lua` |
| London Deep Level | [`lua/lualine/themes/london_deep_level.lua`](lua/lualine/themes/london_deep_level.lua) | `~/.config/nvim/lua/lualine/themes/london_deep_level.lua` |
| London Portland | [`lua/lualine/themes/london-portland.lua`](lua/lualine/themes/london-portland.lua) | `~/.config/nvim/lua/lualine/themes/london-portland.lua` |
| London Portland | [`lua/lualine/themes/london_portland.lua`](lua/lualine/themes/london_portland.lua) | `~/.config/nvim/lua/lualine/themes/london_portland.lua` |
| Paris Guimard | [`lua/lualine/themes/paris-guimard.lua`](lua/lualine/themes/paris-guimard.lua) | `~/.config/nvim/lua/lualine/themes/paris-guimard.lua` |
| Paris Guimard | [`lua/lualine/themes/paris_guimard.lua`](lua/lualine/themes/paris_guimard.lua) | `~/.config/nvim/lua/lualine/themes/paris_guimard.lua` |
| Paris Catacombes | [`lua/lualine/themes/paris-catacombes.lua`](lua/lualine/themes/paris-catacombes.lua) | `~/.config/nvim/lua/lualine/themes/paris-catacombes.lua` |
| Paris Catacombes | [`lua/lualine/themes/paris_catacombes.lua`](lua/lualine/themes/paris_catacombes.lua) | `~/.config/nvim/lua/lualine/themes/paris_catacombes.lua` |
| Paris Carrelage | [`lua/lualine/themes/paris-carrelage.lua`](lua/lualine/themes/paris-carrelage.lua) | `~/.config/nvim/lua/lualine/themes/paris-carrelage.lua` |
| Paris Carrelage | [`lua/lualine/themes/paris_carrelage.lua`](lua/lualine/themes/paris_carrelage.lua) | `~/.config/nvim/lua/lualine/themes/paris_carrelage.lua` |
| All three | [`doc/subway-seat.txt`](doc/subway-seat.txt) | `~/.config/nvim/doc/subway-seat.txt` |

## Turn it on

**Subway Seat**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("subway-seat-walnut")
```

**Subway Seat Tunnel**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("subway-seat-tunnel")
```

**Subway Seat Enamel**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("subway-seat-enamel")
```

**London Moquette**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("london-moquette")
```

**London Deep Level**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("london-deep")
```

**London Portland**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("london-portland")
```

**Paris Guimard**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("paris-guimard")
```

**Paris Catacombes**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("paris-catacombes")
```

**Paris Carrelage**, in init.lua (~/.config/nvim/init.lua; Windows ~/AppData/Local/nvim/init.lua):

```lua
vim.cmd.colorscheme("paris-carrelage")
```

## Follow light and dark

In init.lua:

```lua
-- `subway-seat` follows 'background': Walnut when dark, Enamel when light.
-- Neovim sets 'background' from the terminal; auto-dark-mode.nvim sets it from the OS.
require("subway-seat").setup({ background = { dark = "walnut", light = "enamel" } }) -- or dark = "tunnel"
vim.cmd.colorscheme("subway-seat")

-- lazy.nvim, to follow the OS light/dark setting:
-- { "f-person/auto-dark-mode.nvim", opts = {} }
```

## Uninstall

- Delete `~/.config/nvim/colors/subway-seat.lua`.
- Delete `~/.config/nvim/colors/subway-seat-walnut.lua`.
- Delete `~/.config/nvim/colors/subway-seat-tunnel.lua`.
- Delete `~/.config/nvim/colors/subway-seat-enamel.lua`.
- Delete `~/.config/nvim/colors/london-moquette.lua`.
- Delete `~/.config/nvim/colors/london-deep.lua`.
- Delete `~/.config/nvim/colors/london-portland.lua`.
- Delete `~/.config/nvim/colors/paris-guimard.lua`.
- Delete `~/.config/nvim/colors/paris-catacombes.lua`.
- Delete `~/.config/nvim/colors/paris-carrelage.lua`.
- Delete `~/.config/nvim/lua/subway-seat/init.lua`.
- Delete `~/.config/nvim/lua/subway-seat/palette.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway-seat.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway-seat-walnut.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway_seat.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway-seat-tunnel.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway_seat_tunnel.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway-seat-enamel.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/subway_seat_enamel.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london-moquette.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london_moquette.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london-deep.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london_deep_level.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london-portland.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/london_portland.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris-guimard.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris_guimard.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris-catacombes.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris_catacombes.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris-carrelage.lua`.
- Delete `~/.config/nvim/lua/lualine/themes/paris_carrelage.lua`.
- Delete `~/.config/nvim/doc/subway-seat.txt`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
