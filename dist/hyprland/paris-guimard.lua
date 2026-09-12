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

M.yellow = 'rgb(F1BF4B)'
M.yellowAlpha = 'F1BF4B'

M.yellow_hi = 'rgb(FFD57A)'
M.yellow_hiAlpha = 'FFD57A'

M.orange = 'rgb(CA9245)'
M.orangeAlpha = 'CA9245'

M.orange_hi = 'rgb(DFAA61)'
M.orange_hiAlpha = 'DFAA61'

M.red = 'rgb(C7665B)'
M.redAlpha = 'C7665B'

M.red_hi = 'rgb(E7877B)'
M.red_hiAlpha = 'E7877B'

M.green = 'rgb(70CAA9)'
M.greenAlpha = '70CAA9'

M.green_hi = 'rgb(89DEBE)'
M.green_hiAlpha = '89DEBE'

M.sage = 'rgb(549B9F)'
M.sageAlpha = '549B9F'

M.sage_hi = 'rgb(70B5B9)'
M.sage_hiAlpha = '70B5B9'

M.denim = 'rgb(709BC8)'
M.denimAlpha = '709BC8'

M.denim_hi = 'rgb(8DB6E2)'
M.denim_hiAlpha = '8DB6E2'

M.clay = 'rgb(FAB49C)'
M.clayAlpha = 'FAB49C'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(F1BF4B)',
        inactive_border = 'rgb(30463B)',
        nogroup_border = 'rgb(817262)',
        nogroup_border_active = 'rgb(FAB49C)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F1BF4B)',
        border_inactive = 'rgb(7D7641)',
        border_locked_active = 'rgb(CA9245)',
        border_locked_inactive = 'rgb(6E643F)',
      },
      groupbar = {
        text_color = 'rgb(E9EEEC)',
        text_color_inactive = 'rgb(A9B5AE)',
        col = {
          active = 'rgb(F1BF4B)',
          inactive = 'rgb(3E554A)',
          locked_active = 'rgb(CA9245)',
          locked_inactive = 'rgb(6E643F)',
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
