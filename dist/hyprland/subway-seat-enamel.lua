-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Enamel for Hyprland 0.55+.
--
--   local colors = require("themes.subway-seat-enamel")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(E4D8C0)'
M.crustAlpha = 'E4D8C0'

M.mantle = 'rgb(EEE4D0)'
M.mantleAlpha = 'EEE4D0'

M.base = 'rgb(F8EFDF)'
M.baseAlpha = 'F8EFDF'

M.surface0 = 'rgb(DBCDB3)'
M.surface0Alpha = 'DBCDB3'

M.surface1 = 'rgb(CBB898)'
M.surface1Alpha = 'CBB898'

M.surface2 = 'rgb(BAA380)'
M.surface2Alpha = 'BAA380'

M.overlay0 = 'rgb(A58D6D)'
M.overlay0Alpha = 'A58D6D'

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

M.yellow = 'rgb(976608)'
M.yellowAlpha = '976608'

M.yellow_hi = 'rgb(A9720A)'
M.yellow_hiAlpha = 'A9720A'

M.orange = 'rgb(A04800)'
M.orangeAlpha = 'A04800'

M.orange_hi = 'rgb(BA4D0A)'
M.orange_hiAlpha = 'BA4D0A'

M.red = 'rgb(992418)'
M.redAlpha = '992418'

M.red_hi = 'rgb(BF4233)'
M.red_hiAlpha = 'BF4233'

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

M.clay = 'rgb(843811)'
M.clayAlpha = '843811'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(976608)',
        inactive_border = 'rgb(CBB898)',
        nogroup_border = 'rgb(AF8562)',
        nogroup_border_active = 'rgb(843811)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(976608)',
        border_inactive = 'rgb(B6975E)',
        border_locked_active = 'rgb(A04800)',
        border_locked_inactive = 'rgb(BA8B5B)',
      },
      groupbar = {
        text_color = 'rgb(2A1D13)',
        text_color_inactive = 'rgb(654F3B)',
        col = {
          active = 'rgb(976608)',
          inactive = 'rgb(CBB898)',
          locked_active = 'rgb(A04800)',
          locked_inactive = 'rgb(BA8B5B)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(3E2C1E24)',
      },
    },
    misc = {
      background_color = 'rgb(F8EFDF)',
    },
  })
end

return M
