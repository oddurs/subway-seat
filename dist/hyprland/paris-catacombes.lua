-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes for Hyprland 0.55+.
--
--   local colors = require("themes.paris-catacombes")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(05120C)'
M.crustAlpha = '05120C'

M.mantle = 'rgb(061811)'
M.mantleAlpha = '061811'

M.base = 'rgb(062017)'
M.baseAlpha = '062017'

M.surface0 = 'rgb(0A2B20)'
M.surface0Alpha = '0A2B20'

M.surface1 = 'rgb(13382A)'
M.surface1Alpha = '13382A'

M.surface2 = 'rgb(1E4738)'
M.surface2Alpha = '1E4738'

M.overlay0 = 'rgb(456A5B)'
M.overlay0Alpha = '456A5B'

M.overlay1 = 'rgb(648576)'
M.overlay1Alpha = '648576'

M.overlay2 = 'rgb(829D91)'
M.overlay2Alpha = '829D91'

M.subtext0 = 'rgb(9EB3AA)'
M.subtext0Alpha = '9EB3AA'

M.subtext1 = 'rgb(B8CAC2)'
M.subtext1Alpha = 'B8CAC2'

M.text = 'rgb(CFDED7)'
M.textAlpha = 'CFDED7'

M.text_hi = 'rgb(E4EEE9)'
M.text_hiAlpha = 'E4EEE9'

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
        inactive_border = 'rgb(13382A)',
        nogroup_border = 'rgb(685665)',
        nogroup_border_active = 'rgb(E783BD)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(EBC342)',
        border_inactive = 'rgb(697034)',
        border_locked_active = 'rgb(D78E3C)',
        border_locked_inactive = 'rgb(615A31)',
      },
      groupbar = {
        text_color = 'rgb(E4EEE9)',
        text_color_inactive = 'rgb(9EB3AA)',
        col = {
          active = 'rgb(EBC342)',
          inactive = 'rgb(1E4738)',
          locked_active = 'rgb(D78E3C)',
          locked_inactive = 'rgb(615A31)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(02090699)',
      },
    },
    misc = {
      background_color = 'rgb(062017)',
    },
  })
end

return M
