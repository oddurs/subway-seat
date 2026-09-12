-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Tunnel for Hyprland 0.55+.
--
--   local colors = require("themes.subway-seat-tunnel")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(140D07)'
M.crustAlpha = '140D07'

M.mantle = 'rgb(1B120A)'
M.mantleAlpha = '1B120A'

M.base = 'rgb(24180E)'
M.baseAlpha = '24180E'

M.surface0 = 'rgb(302115)'
M.surface0Alpha = '302115'

M.surface1 = 'rgb(3D2C1D)'
M.surface1Alpha = '3D2C1D'

M.surface2 = 'rgb(4F3927)'
M.surface2Alpha = '4F3927'

M.overlay0 = 'rgb(745B45)'
M.overlay0Alpha = '745B45'

M.overlay1 = 'rgb(917759)'
M.overlay1Alpha = '917759'

M.overlay2 = 'rgb(AA9171)'
M.overlay2Alpha = 'AA9171'

M.subtext0 = 'rgb(C0AA88)'
M.subtext0Alpha = 'C0AA88'

M.subtext1 = 'rgb(D6C3A0)'
M.subtext1Alpha = 'D6C3A0'

M.text = 'rgb(E9D8B6)'
M.textAlpha = 'E9D8B6'

M.text_hi = 'rgb(F6EAD1)'
M.text_hiAlpha = 'F6EAD1'

M.yellow = 'rgb(F3BF45)'
M.yellowAlpha = 'F3BF45'

M.yellow_hi = 'rgb(FFD36B)'
M.yellow_hiAlpha = 'FFD36B'

M.orange = 'rgb(EC7F31)'
M.orangeAlpha = 'EC7F31'

M.orange_hi = 'rgb(FF9D55)'
M.orange_hiAlpha = 'FF9D55'

M.red = 'rgb(E05C45)'
M.redAlpha = 'E05C45'

M.red_hi = 'rgb(F97160)'
M.red_hiAlpha = 'F97160'

M.green = 'rgb(ADB956)'
M.greenAlpha = 'ADB956'

M.green_hi = 'rgb(BFCB63)'
M.green_hiAlpha = 'BFCB63'

M.sage = 'rgb(86AD95)'
M.sageAlpha = '86AD95'

M.sage_hi = 'rgb(A5C9B0)'
M.sage_hiAlpha = 'A5C9B0'

M.denim = 'rgb(7F9BAE)'
M.denimAlpha = '7F9BAE'

M.denim_hi = 'rgb(9DB6C6)'
M.denim_hiAlpha = '9DB6C6'

M.clay = 'rgb(F4A87E)'
M.clayAlpha = 'F4A87E'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(F3BF45)',
        inactive_border = 'rgb(3D2C1D)',
        nogroup_border = 'rgb(865E44)',
        nogroup_border_active = 'rgb(F4A87E)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F3BF45)',
        border_inactive = 'rgb(86672D)',
        border_locked_active = 'rgb(EC7F31)',
        border_locked_inactive = 'rgb(834D25)',
      },
      groupbar = {
        text_color = 'rgb(F6EAD1)',
        text_color_inactive = 'rgb(C0AA88)',
        col = {
          active = 'rgb(F3BF45)',
          inactive = 'rgb(4F3927)',
          locked_active = 'rgb(EC7F31)',
          locked_inactive = 'rgb(834D25)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(0A060499)',
      },
    },
    misc = {
      background_color = 'rgb(24180E)',
    },
  })
end

return M
