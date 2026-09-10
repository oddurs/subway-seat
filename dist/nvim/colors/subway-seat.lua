-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat, following 'background': Walnut when it's dark, Enamel when it's light
-- (with the plugin, whatever `setup({ background = { dark = …, light = … } })` names).
-- Neovim re-runs this file when 'background' changes, so flipping it flips the flavor.

if vim.api.nvim_get_runtime_file("lua/subway-seat/init.lua", false)[1] then
  return require("subway-seat").colorscheme("subway-seat")
end

-- On its own: read the flavor from its colors file next to this one.
local flavor = vim.o.background == "light" and "enamel" or "walnut"
local path = vim.api.nvim_get_runtime_file("colors/subway-seat-" .. flavor .. ".lua", false)[1]
if not path then
  error("subway-seat: colors/subway-seat-" .. flavor .. ".lua is missing; copy the whole colors/ folder")
end
local spec = assert(loadfile(path))("subway-seat")
vim.cmd("hi clear")
if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
vim.o.termguicolors = true
vim.g.colors_name = "subway-seat"
for group, hl in pairs(spec.groups) do vim.api.nvim_set_hl(0, group, hl) end
for i, color in ipairs(spec.ansi) do vim.g["terminal_color_" .. (i - 1)] = color end
