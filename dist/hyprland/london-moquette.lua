-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Moquette for Hyprland 0.55+.
--
--   local colors = require("themes.london-moquette")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(121826)'
M.crustAlpha = '121826'

M.mantle = 'rgb(172032)'
M.mantleAlpha = '172032'

M.base = 'rgb(1E2941)'
M.baseAlpha = '1E2941'

M.surface0 = 'rgb(263451)'
M.surface0Alpha = '263451'

M.surface1 = 'rgb(303F61)'
M.surface1Alpha = '303F61'

M.surface2 = 'rgb(3D4F72)'
M.surface2Alpha = '3D4F72'

M.overlay0 = 'rgb(576685)'
M.overlay0Alpha = '576685'

M.overlay1 = 'rgb(73819C)'
M.overlay1Alpha = '73819C'

M.overlay2 = 'rgb(8F9AB0)'
M.overlay2Alpha = '8F9AB0'

M.subtext0 = 'rgb(A9B2C4)'
M.subtext0Alpha = 'A9B2C4'

M.subtext1 = 'rgb(C1C9D8)'
M.subtext1Alpha = 'C1C9D8'

M.text = 'rgb(D8DEEA)'
M.textAlpha = 'D8DEEA'

M.text_hi = 'rgb(E9EDF5)'
M.text_hiAlpha = 'E9EDF5'

M.yellow = 'rgb(F2C03F)'
M.yellowAlpha = 'F2C03F'

M.yellow_hi = 'rgb(FFD36C)'
M.yellow_hiAlpha = 'FFD36C'

M.orange = 'rgb(DE8946)'
M.orangeAlpha = 'DE8946'

M.orange_hi = 'rgb(E5AA7F)'
M.orange_hiAlpha = 'E5AA7F'

M.red = 'rgb(DB6052)'
M.redAlpha = 'DB6052'

M.red_hi = 'rgb(FE8474)'
M.red_hiAlpha = 'FE8474'

M.green = 'rgb(77C581)'
M.greenAlpha = '77C581'

M.green_hi = 'rgb(9AD2A0)'
M.green_hiAlpha = '9AD2A0'

M.sage = 'rgb(54B4B5)'
M.sageAlpha = '54B4B5'

M.sage_hi = 'rgb(72D1D3)'
M.sage_hiAlpha = '72D1D3'

M.denim = 'rgb(7595DA)'
M.denimAlpha = '7595DA'

M.denim_hi = 'rgb(8BB0FF)'
M.denim_hiAlpha = '8BB0FF'

M.clay = 'rgb(AE9EDC)'
M.clayAlpha = 'AE9EDC'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(F2C03F)',
        inactive_border = 'rgb(303F61)',
        nogroup_border = 'rgb(626592)',
        nogroup_border_active = 'rgb(AE9EDC)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F2C03F)',
        border_inactive = 'rgb(7E7353)',
        border_locked_active = 'rgb(DE8946)',
        border_locked_inactive = 'rgb(765D56)',
      },
      groupbar = {
        text_color = 'rgb(E9EDF5)',
        text_color_inactive = 'rgb(A9B2C4)',
        col = {
          active = 'rgb(F2C03F)',
          inactive = 'rgb(3D4F72)',
          locked_active = 'rgb(DE8946)',
          locked_inactive = 'rgb(765D56)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(090C1399)',
      },
    },
    misc = {
      background_color = 'rgb(1E2941)',
    },
  })
end

return M
