-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard for Hyprland 0.55+.
--
--   local colors = require("themes.paris-guimard")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(0A1D15)'
M.crustAlpha = '0A1D15'

M.mantle = 'rgb(0C261C)'
M.mantleAlpha = '0C261C'

M.base = 'rgb(0E3125)'
M.baseAlpha = '0E3125'

M.surface0 = 'rgb(113E2E)'
M.surface0Alpha = '113E2E'

M.surface1 = 'rgb(194A39)'
M.surface1Alpha = '194A39'

M.surface2 = 'rgb(285A47)'
M.surface2Alpha = '285A47'

M.overlay0 = 'rgb(47705F)'
M.overlay0Alpha = '47705F'

M.overlay1 = 'rgb(67897A)'
M.overlay1Alpha = '67897A'

M.overlay2 = 'rgb(86A195)'
M.overlay2Alpha = '86A195'

M.subtext0 = 'rgb(A2B7AE)'
M.subtext0Alpha = 'A2B7AE'

M.subtext1 = 'rgb(BBCDC5)'
M.subtext1Alpha = 'BBCDC5'

M.text = 'rgb(D3E2DB)'
M.textAlpha = 'D3E2DB'

M.text_hi = 'rgb(E6F0EB)'
M.text_hiAlpha = 'E6F0EB'

M.yellow = 'rgb(EBC342)'
M.yellowAlpha = 'EBC342'

M.yellow_hi = 'rgb(FBD664)'
M.yellow_hiAlpha = 'FBD664'

M.orange = 'rgb(D78E3C)'
M.orangeAlpha = 'D78E3C'

M.orange_hi = 'rgb(EEA85C)'
M.orange_hiAlpha = 'EEA85C'

M.red = 'rgb(DA6058)'
M.redAlpha = 'DA6058'

M.red_hi = 'rgb(EF796F)'
M.red_hiAlpha = 'EF796F'

M.green = 'rgb(73C686)'
M.greenAlpha = '73C686'

M.green_hi = 'rgb(82D896)'
M.green_hiAlpha = '82D896'

M.sage = 'rgb(6FB393)'
M.sageAlpha = '6FB393'

M.sage_hi = 'rgb(8ECFAF)'
M.sage_hiAlpha = '8ECFAF'

M.denim = 'rgb(639BD5)'
M.denimAlpha = '639BD5'

M.denim_hi = 'rgb(82B7EE)'
M.denim_hiAlpha = '82B7EE'

M.clay = 'rgb(E783BD)'
M.clayAlpha = 'E783BD'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(EBC342)',
        inactive_border = 'rgb(194A39)',
        nogroup_border = 'rgb(6B616E)',
        nogroup_border_active = 'rgb(E783BD)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(EBC342)',
        border_inactive = 'rgb(6D7A3D)',
        border_locked_active = 'rgb(D78E3C)',
        border_locked_inactive = 'rgb(65653A)',
      },
      groupbar = {
        text_color = 'rgb(E6F0EB)',
        text_color_inactive = 'rgb(A2B7AE)',
        col = {
          active = 'rgb(EBC342)',
          inactive = 'rgb(285A47)',
          locked_active = 'rgb(D78E3C)',
          locked_inactive = 'rgb(65653A)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(050E0A99)',
      },
    },
    misc = {
      background_color = 'rgb(0E3125)',
    },
  })
end

return M
