-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes for Hyprland 0.55+.
--
--   local colors = require("themes.paris-catacombes")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(0A100D)'
M.crustAlpha = '0A100D'

M.mantle = 'rgb(0D1711)'
M.mantleAlpha = '0D1711'

M.base = 'rgb(121E19)'
M.baseAlpha = '121E19'

M.surface0 = 'rgb(1A2921)'
M.surface0Alpha = '1A2921'

M.surface1 = 'rgb(24342C)'
M.surface1Alpha = '24342C'

M.surface2 = 'rgb(31433A)'
M.surface2Alpha = '31433A'

M.overlay0 = 'rgb(54655C)'
M.overlay0Alpha = '54655C'

M.overlay1 = 'rgb(708178)'
M.overlay1Alpha = '708178'

M.overlay2 = 'rgb(8C9A92)'
M.overlay2Alpha = '8C9A92'

M.subtext0 = 'rgb(A5B1AA)'
M.subtext0Alpha = 'A5B1AA'

M.subtext1 = 'rgb(BFC8C2)'
M.subtext1Alpha = 'BFC8C2'

M.text = 'rgb(D4DDD7)'
M.textAlpha = 'D4DDD7'

M.text_hi = 'rgb(E7ECEA)'
M.text_hiAlpha = 'E7ECEA'

M.yellow = 'rgb(F2BF4B)'
M.yellowAlpha = 'F2BF4B'

M.yellow_hi = 'rgb(FFD273)'
M.yellow_hiAlpha = 'FFD273'

M.orange = 'rgb(D0914F)'
M.orangeAlpha = 'D0914F'

M.orange_hi = 'rgb(E7AB6D)'
M.orange_hiAlpha = 'E7AB6D'

M.red = 'rgb(CD6B63)'
M.redAlpha = 'CD6B63'

M.red_hi = 'rgb(E1837A)'
M.red_hiAlpha = 'E1837A'

M.green = 'rgb(80C28E)'
M.greenAlpha = '80C28E'

M.green_hi = 'rgb(8FD59E)'
M.green_hiAlpha = '8FD59E'

M.sage = 'rgb(6CA087)'
M.sageAlpha = '6CA087'

M.sage_hi = 'rgb(98CCB2)'
M.sage_hiAlpha = '98CCB2'

M.denim = 'rgb(709BC8)'
M.denimAlpha = '709BC8'

M.denim_hi = 'rgb(8DB6E2)'
M.denim_hiAlpha = '8DB6E2'

M.clay = 'rgb(CE96B4)'
M.clayAlpha = 'CE96B4'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(F2BF4B)',
        inactive_border = 'rgb(24342C)',
        nogroup_border = 'rgb(685B62)',
        nogroup_border_active = 'rgb(CE96B4)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F2BF4B)',
        border_inactive = 'rgb(766C38)',
        border_locked_active = 'rgb(D0914F)',
        border_locked_inactive = 'rgb(69593A)',
      },
      groupbar = {
        text_color = 'rgb(E7ECEA)',
        text_color_inactive = 'rgb(A5B1AA)',
        col = {
          active = 'rgb(F2BF4B)',
          inactive = 'rgb(31433A)',
          locked_active = 'rgb(D0914F)',
          locked_inactive = 'rgb(69593A)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(05080699)',
      },
    },
    misc = {
      background_color = 'rgb(121E19)',
    },
  })
end

return M
