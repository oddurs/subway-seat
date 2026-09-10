-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- lualine's theme = "auto" loads the theme named like g:colors_name; this one
-- shows whichever flavor `colorscheme subway-seat` put on screen.
local ok, ss = pcall(require, "subway-seat")
local flavor = ok and ss.current or (vim.o.background == "light" and "enamel" or "walnut")
return require("lualine.themes.subway-seat-" .. flavor)
