-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat for Hyprland 0.55+.
--
--   local colors = require("themes.subway-seat")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(20160E)'
M.crustAlpha = '20160E'

M.mantle = 'rgb(2A1D13)'
M.mantleAlpha = '2A1D13'

M.base = 'rgb(362619)'
M.baseAlpha = '362619'

M.surface0 = 'rgb(43301F)'
M.surface0Alpha = '43301F'

M.surface1 = 'rgb(513B27)'
M.surface1Alpha = '513B27'

M.surface2 = 'rgb(634932)'
M.surface2Alpha = '634932'

M.overlay0 = 'rgb(7B6047)'
M.overlay0Alpha = '7B6047'

M.overlay1 = 'rgb(967B5C)'
M.overlay1Alpha = '967B5C'

M.overlay2 = 'rgb(AE9575)'
M.overlay2Alpha = 'AE9575'

M.subtext0 = 'rgb(C4AE8C)'
M.subtext0Alpha = 'C4AE8C'

M.subtext1 = 'rgb(D9C6A3)'
M.subtext1Alpha = 'D9C6A3'

M.text = 'rgb(EDDCBC)'
M.textAlpha = 'EDDCBC'

M.text_hi = 'rgb(F8ECD4)'
M.text_hiAlpha = 'F8ECD4'

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

M.red_hi = 'rgb(FF8373)'
M.red_hiAlpha = 'FF8373'

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
        inactive_border = 'rgb(513B27)',
        nogroup_border = 'rgb(92674A)',
        nogroup_border_active = 'rgb(F4A87E)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F3BF45)',
        border_inactive = 'rgb(927033)',
        border_locked_active = 'rgb(EC7F31)',
        border_locked_inactive = 'rgb(8F562B)',
      },
      groupbar = {
        text_color = 'rgb(F8ECD4)',
        text_color_inactive = 'rgb(C4AE8C)',
        col = {
          active = 'rgb(F3BF45)',
          inactive = 'rgb(634932)',
          locked_active = 'rgb(EC7F31)',
          locked_inactive = 'rgb(8F562B)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(100B0799)',
      },
    },
    misc = {
      background_color = 'rgb(362619)',
    },
  })
end

return M
