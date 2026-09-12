-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard for Hyprland 0.55+.
--
--   local colors = require("themes.paris-guimard")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(131A17)'
M.crustAlpha = '131A17'

M.mantle = 'rgb(18241D)'
M.mantleAlpha = '18241D'

M.base = 'rgb(1E2E26)'
M.baseAlpha = '1E2E26'

M.surface0 = 'rgb(263930)'
M.surface0Alpha = '263930'

M.surface1 = 'rgb(30463B)'
M.surface1Alpha = '30463B'

M.surface2 = 'rgb(3E554A)'
M.surface2Alpha = '3E554A'

M.overlay0 = 'rgb(586B61)'
M.overlay0Alpha = '586B61'

M.overlay1 = 'rgb(74857C)'
M.overlay1Alpha = '74857C'

M.overlay2 = 'rgb(909E96)'
M.overlay2Alpha = '909E96'

M.subtext0 = 'rgb(A9B5AE)'
M.subtext0Alpha = 'A9B5AE'

M.subtext1 = 'rgb(C2CBC5)'
M.subtext1Alpha = 'C2CBC5'

M.text = 'rgb(D9E1DB)'
M.textAlpha = 'D9E1DB'

M.text_hi = 'rgb(E9EEEC)'
M.text_hiAlpha = 'E9EEEC'

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
        active_border = 'rgb(EBC168)',
        inactive_border = 'rgb(30463B)',
        nogroup_border = 'rgb(6F666B)',
        nogroup_border_active = 'rgb(CE96B4)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(EBC168)',
        border_inactive = 'rgb(7B774D)',
        border_locked_active = 'rgb(D0914F)',
        border_locked_inactive = 'rgb(706443)',
      },
      groupbar = {
        text_color = 'rgb(E9EEEC)',
        text_color_inactive = 'rgb(A9B5AE)',
        col = {
          active = 'rgb(EBC168)',
          inactive = 'rgb(3E554A)',
          locked_active = 'rgb(D0914F)',
          locked_inactive = 'rgb(706443)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(0A0D0C99)',
      },
    },
    misc = {
      background_color = 'rgb(1E2E26)',
    },
  })
end

return M
