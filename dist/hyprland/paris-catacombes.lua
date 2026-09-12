-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes for Hyprland 0.55+.
--
--   local colors = require("themes.paris-catacombes")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(0B100D)'
M.crustAlpha = '0B100D'

M.mantle = 'rgb(0F1612)'
M.mantleAlpha = '0F1612'

M.base = 'rgb(141D19)'
M.baseAlpha = '141D19'

M.surface0 = 'rgb(1D2822)'
M.surface0Alpha = '1D2822'

M.surface1 = 'rgb(27332D)'
M.surface1Alpha = '27332D'

M.surface2 = 'rgb(34423B)'
M.surface2Alpha = '34423B'

M.overlay0 = 'rgb(57645D)'
M.overlay0Alpha = '57645D'

M.overlay1 = 'rgb(738079)'
M.overlay1Alpha = '738079'

M.overlay2 = 'rgb(8E9993)'
M.overlay2Alpha = '8E9993'

M.subtext0 = 'rgb(A7B0AB)'
M.subtext0Alpha = 'A7B0AB'

M.subtext1 = 'rgb(C0C7C3)'
M.subtext1Alpha = 'C0C7C3'

M.text = 'rgb(D5DCD8)'
M.textAlpha = 'D5DCD8'

M.text_hi = 'rgb(E8ECEA)'
M.text_hiAlpha = 'E8ECEA'

M.yellow = 'rgb(EBC168)'
M.yellowAlpha = 'EBC168'

M.yellow_hi = 'rgb(FBD380)'
M.yellow_hiAlpha = 'FBD380'

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

M.sage = 'rgb(7BB096)'
M.sageAlpha = '7BB096'

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
        active_border = 'rgb(EBC168)',
        inactive_border = 'rgb(27332D)',
        nogroup_border = 'rgb(6A5B63)',
        nogroup_border_active = 'rgb(CE96B4)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(EBC168)',
        border_inactive = 'rgb(756C45)',
        border_locked_active = 'rgb(D0914F)',
        border_locked_inactive = 'rgb(6B593B)',
      },
      groupbar = {
        text_color = 'rgb(E8ECEA)',
        text_color_inactive = 'rgb(A7B0AB)',
        col = {
          active = 'rgb(EBC168)',
          inactive = 'rgb(34423B)',
          locked_active = 'rgb(D0914F)',
          locked_inactive = 'rgb(6B593B)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(06080699)',
      },
    },
    misc = {
      background_color = 'rgb(141D19)',
    },
  })
end

return M
