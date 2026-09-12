-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(C8DAD1)'
M.crustAlpha = 'C8DAD1'

M.mantle = 'rgb(D5E3DD)'
M.mantleAlpha = 'D5E3DD'

M.base = 'rgb(E2EDE8)'
M.baseAlpha = 'E2EDE8'

M.surface0 = 'rgb(B6D2C5)'
M.surface0Alpha = 'B6D2C5'

M.surface1 = 'rgb(9DC1B1)'
M.surface1Alpha = '9DC1B1'

M.surface2 = 'rgb(88AF9E)'
M.surface2Alpha = '88AF9E'

M.overlay0 = 'rgb(759A8A)'
M.overlay0Alpha = '759A8A'

M.overlay1 = 'rgb(5C8171)'
M.overlay1Alpha = '5C8171'

M.overlay2 = 'rgb(4A695C)'
M.overlay2Alpha = '4A695C'

M.subtext0 = 'rgb(405B4F)'
M.subtext0Alpha = '405B4F'

M.subtext1 = 'rgb(334A41)'
M.subtext1Alpha = '334A41'

M.text = 'rgb(21352D)'
M.textAlpha = '21352D'

M.text_hi = 'rgb(16241E)'
M.text_hiAlpha = '16241E'

M.yellow = 'rgb(856A00)'
M.yellowAlpha = '856A00'

M.yellow_hi = 'rgb(937500)'
M.yellow_hiAlpha = '937500'

M.orange = 'rgb(9B5D00)'
M.orangeAlpha = '9B5D00'

M.orange_hi = 'rgb(AE6800)'
M.orange_hiAlpha = 'AE6800'

M.red = 'rgb(A30013)'
M.redAlpha = 'A30013'

M.red_hi = 'rgb(C82C2C)'
M.red_hiAlpha = 'C82C2C'

M.green = 'rgb(00823B)'
M.greenAlpha = '00823B'

M.green_hi = 'rgb(00863D)'
M.green_hiAlpha = '00863D'

M.sage = 'rgb(007752)'
M.sageAlpha = '007752'

M.sage_hi = 'rgb(2A8862)'
M.sage_hiAlpha = '2A8862'

M.denim = 'rgb(0961A9)'
M.denimAlpha = '0961A9'

M.denim_hi = 'rgb(2E75B9)'
M.denim_hiAlpha = '2E75B9'

M.clay = 'rgb(B43586)'
M.clayAlpha = 'B43586'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(856A00)',
        inactive_border = 'rgb(9DC1B1)',
        nogroup_border = 'rgb(A689A0)',
        nogroup_border_active = 'rgb(B43586)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(856A00)',
        border_inactive = 'rgb(939E6A)',
        border_locked_active = 'rgb(9B5D00)',
        border_locked_inactive = 'rgb(9C996A)',
      },
      groupbar = {
        text_color = 'rgb(16241E)',
        text_color_inactive = 'rgb(405B4F)',
        col = {
          active = 'rgb(856A00)',
          inactive = 'rgb(9DC1B1)',
          locked_active = 'rgb(9B5D00)',
          locked_inactive = 'rgb(9C996A)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(21352D24)',
      },
    },
    misc = {
      background_color = 'rgb(E2EDE8)',
    },
  })
end

return M
