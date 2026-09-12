-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland for Hyprland 0.55+.
--
--   local colors = require("themes.london-portland")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(CDD5E4)'
M.crustAlpha = 'CDD5E4'

M.mantle = 'rgb(DAE0EB)'
M.mantleAlpha = 'DAE0EB'

M.base = 'rgb(E5EAF4)'
M.baseAlpha = 'E5EAF4'

M.surface0 = 'rgb(BFCAE1)'
M.surface0Alpha = 'BFCAE1'

M.surface1 = 'rgb(A9B7D4)'
M.surface1Alpha = 'A9B7D4'

M.surface2 = 'rgb(95A5C4)'
M.surface2Alpha = '95A5C4'

M.overlay0 = 'rgb(8291AE)'
M.overlay0Alpha = '8291AE'

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

M.orange = 'rgb(A45600)'
M.orangeAlpha = 'A45600'

M.orange_hi = 'rgb(B86100)'
M.orange_hiAlpha = 'B86100'

M.red = 'rgb(A40005)'
M.redAlpha = 'A40005'

M.red_hi = 'rgb(C92B23)'
M.red_hiAlpha = 'C92B23'

M.green = 'rgb(00822E)'
M.greenAlpha = '00822E'

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
        inactive_border = 'rgb(A9B7D4)',
        nogroup_border = 'rgb(9594C4)',
        nogroup_border_active = 'rgb(7660AB)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(896800)',
        border_inactive = 'rgb(9C977F)',
        border_locked_active = 'rgb(A45600)',
        border_locked_inactive = 'rgb(A7907F)',
      },
      groupbar = {
        text_color = 'rgb(1B202B)',
        text_color_inactive = 'rgb(4A5469)',
        col = {
          active = 'rgb(896800)',
          inactive = 'rgb(A9B7D4)',
          locked_active = 'rgb(A45600)',
          locked_inactive = 'rgb(A7907F)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(29304024)',
      },
    },
    misc = {
      background_color = 'rgb(E5EAF4)',
    },
  })
end

return M
