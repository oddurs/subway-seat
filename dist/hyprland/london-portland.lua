-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland for Hyprland 0.55+.
--
--   local colors = require("themes.london-portland")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(CCDAF2)'
M.crustAlpha = 'CCDAF2'

M.mantle = 'rgb(DCE5F7)'
M.mantleAlpha = 'DCE5F7'

M.base = 'rgb(E8F0FF)'
M.baseAlpha = 'E8F0FF'

M.surface0 = 'rgb(BFCFF1)'
M.surface0Alpha = 'BFCFF1'

M.surface1 = 'rgb(A8BBE2)'
M.surface1Alpha = 'A8BBE2'

M.surface2 = 'rgb(93A7CF)'
M.surface2Alpha = '93A7CF'

M.overlay0 = 'rgb(8192B4)'
M.overlay0Alpha = '8192B4'

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

M.yellow = 'rgb(8D6C08)'
M.yellowAlpha = '8D6C08'

M.yellow_hi = 'rgb(9B770A)'
M.yellow_hiAlpha = '9B770A'

M.orange = 'rgb(A54300)'
M.orangeAlpha = 'A54300'

M.orange_hi = 'rgb(AC5A00)'
M.orange_hiAlpha = 'AC5A00'

M.red = 'rgb(9B211A)'
M.redAlpha = '9B211A'

M.red_hi = 'rgb(CC2E25)'
M.red_hiAlpha = 'CC2E25'

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

M.clay = 'rgb(755FA9)'
M.clayAlpha = '755FA9'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(8D6C08)',
        inactive_border = 'rgb(A8BBE2)',
        nogroup_border = 'rgb(9496CB)',
        nogroup_border_active = 'rgb(755FA9)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(8D6C08)',
        border_inactive = 'rgb(9D9B8B)',
        border_locked_active = 'rgb(A54300)',
        border_locked_inactive = 'rgb(A78B88)',
      },
      groupbar = {
        text_color = 'rgb(1B202B)',
        text_color_inactive = 'rgb(4A5469)',
        col = {
          active = 'rgb(8D6C08)',
          inactive = 'rgb(A8BBE2)',
          locked_active = 'rgb(A54300)',
          locked_inactive = 'rgb(A78B88)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(29304024)',
      },
    },
    misc = {
      background_color = 'rgb(E8F0FF)',
    },
  })
end

return M
