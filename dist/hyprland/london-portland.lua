-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland for Hyprland 0.55+.
--
--   local colors = require("themes.london-portland")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(C5D5F3)'
M.crustAlpha = 'C5D5F3'

M.mantle = 'rgb(D4E0F6)'
M.mantleAlpha = 'D4E0F6'

M.base = 'rgb(E0EAFE)'
M.baseAlpha = 'E0EAFE'

M.surface0 = 'rgb(B6CAF3)'
M.surface0Alpha = 'B6CAF3'

M.surface1 = 'rgb(A1B7E5)'
M.surface1Alpha = 'A1B7E5'

M.surface2 = 'rgb(8FA5D0)'
M.surface2Alpha = '8FA5D0'

M.overlay0 = 'rgb(7F91B4)'
M.overlay0Alpha = '7F91B4'

M.overlay1 = 'rgb(697794)'
M.overlay1Alpha = '697794'

M.overlay2 = 'rgb(556179)'
M.overlay2Alpha = '556179'

M.subtext0 = 'rgb(4A5469)'
M.subtext0Alpha = '4A5469'

M.subtext1 = 'rgb(3C4557)'
M.subtext1Alpha = '3C4557'

M.text = 'rgb(293040)'
M.textAlpha = '293040'

M.text_hi = 'rgb(1B202B)'
M.text_hiAlpha = '1B202B'

M.yellow = 'rgb(896800)'
M.yellowAlpha = '896800'

M.yellow_hi = 'rgb(977300)'
M.yellow_hiAlpha = '977300'

M.orange = 'rgb(B14A07)'
M.orangeAlpha = 'B14A07'

M.orange_hi = 'rgb(B86100)'
M.orange_hiAlpha = 'B86100'

M.red = 'rgb(9B211A)'
M.redAlpha = '9B211A'

M.red_hi = 'rgb(C92B23)'
M.red_hiAlpha = 'C92B23'

M.green = 'rgb(0D8131)'
M.greenAlpha = '0D8131'

M.green_hi = 'rgb(008730)'
M.green_hiAlpha = '008730'

M.sage = 'rgb(007376)'
M.sageAlpha = '007376'

M.sage_hi = 'rgb(008688)'
M.sage_hiAlpha = '008688'

M.denim = 'rgb(0019A8)'
M.denimAlpha = '0019A8'

M.denim_hi = 'rgb(4A6EBD)'
M.denim_hiAlpha = '4A6EBD'

M.clay = 'rgb(7660AB)'
M.clayAlpha = '7660AB'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(896800)',
        inactive_border = 'rgb(A1B7E5)',
        nogroup_border = 'rgb(9094CE)',
        nogroup_border_active = 'rgb(7660AB)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(896800)',
        border_inactive = 'rgb(979789)',
        border_locked_active = 'rgb(B14A07)',
        border_locked_inactive = 'rgb(A78B8C)',
      },
      groupbar = {
        text_color = 'rgb(1B202B)',
        text_color_inactive = 'rgb(4A5469)',
        col = {
          active = 'rgb(896800)',
          inactive = 'rgb(A1B7E5)',
          locked_active = 'rgb(B14A07)',
          locked_inactive = 'rgb(A78B8C)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(29304024)',
      },
    },
    misc = {
      background_color = 'rgb(E0EAFE)',
    },
  })
end

return M
