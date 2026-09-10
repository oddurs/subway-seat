-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Enamel for Hyprland 0.55+.
--
--   local colors = require("themes.subway-seat-enamel")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(E2D3B6)'
M.crustAlpha = 'E2D3B6'

M.mantle = 'rgb(EBDEC6)'
M.mantleAlpha = 'EBDEC6'

M.base = 'rgb(F4E9D4)'
M.baseAlpha = 'F4E9D4'

M.surface0 = 'rgb(D9C8A7)'
M.surface0Alpha = 'D9C8A7'

M.surface1 = 'rgb(CAB48E)'
M.surface1Alpha = 'CAB48E'

M.surface2 = 'rgb(BAA07A)'
M.surface2Alpha = 'BAA07A'

M.overlay0 = 'rgb(A58C6A)'
M.overlay0Alpha = 'A58C6A'

M.overlay1 = 'rgb(8C7254)'
M.overlay1Alpha = '8C7254'

M.overlay2 = 'rgb(735C44)'
M.overlay2Alpha = '735C44'

M.subtext0 = 'rgb(654F3B)'
M.subtext0Alpha = '654F3B'

M.subtext1 = 'rgb(54402F)'
M.subtext1Alpha = '54402F'

M.text = 'rgb(3E2C1E)'
M.textAlpha = '3E2C1E'

M.text_hi = 'rgb(2A1D13)'
M.text_hiAlpha = '2A1D13'

M.yellow = 'rgb(936200)'
M.yellowAlpha = '936200'

M.yellow_hi = 'rgb(A56E00)'
M.yellow_hiAlpha = 'A56E00'

M.orange = 'rgb(AD4E00)'
M.orangeAlpha = 'AD4E00'

M.orange_hi = 'rgb(C4561A)'
M.orange_hiAlpha = 'C4561A'

M.red = 'rgb(992418)'
M.redAlpha = '992418'

M.red_hi = 'rgb(BC4031)'
M.red_hiAlpha = 'BC4031'

M.green = 'rgb(66740F)'
M.greenAlpha = '66740F'

M.green_hi = 'rgb(697813)'
M.green_hiAlpha = '697813'

M.sage = 'rgb(3E7157)'
M.sageAlpha = '3E7157'

M.sage_hi = 'rgb(4C8367)'
M.sage_hiAlpha = '4C8367'

M.denim = 'rgb(3F6480)'
M.denimAlpha = '3F6480'

M.denim_hi = 'rgb(517791)'
M.denim_hiAlpha = '517791'

M.clay = 'rgb(A65633)'
M.clayAlpha = 'A65633'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(936200)',
        inactive_border = 'rgb(CAB48E)',
        nogroup_border = 'rgb(BC8E6A)',
        nogroup_border_active = 'rgb(A65633)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(936200)',
        border_inactive = 'rgb(B49355)',
        border_locked_active = 'rgb(AD4E00)',
        border_locked_inactive = 'rgb(BE8B55)',
      },
      groupbar = {
        text_color = 'rgb(2A1D13)',
        text_color_inactive = 'rgb(654F3B)',
        col = {
          active = 'rgb(936200)',
          inactive = 'rgb(CAB48E)',
          locked_active = 'rgb(AD4E00)',
          locked_inactive = 'rgb(BE8B55)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(3E2C1E24)',
      },
    },
    misc = {
      background_color = 'rgb(F4E9D4)',
    },
  })
end

return M
