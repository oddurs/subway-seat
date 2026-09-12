-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland for Hyprland 0.55+.
--
--   local colors = require("themes.london-portland")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(CED5E3)'
M.crustAlpha = 'CED5E3'

M.mantle = 'rgb(D9E0EC)'
M.mantleAlpha = 'D9E0EC'

M.base = 'rgb(E5EAF6)'
M.baseAlpha = 'E5EAF6'

M.surface0 = 'rgb(C1CADC)'
M.surface0Alpha = 'C1CADC'

M.surface1 = 'rgb(ADB7CB)'
M.surface1Alpha = 'ADB7CB'

M.surface2 = 'rgb(9BA5B8)'
M.surface2Alpha = '9BA5B8'

M.overlay0 = 'rgb(8A919F)'
M.overlay0Alpha = '8A919F'

M.overlay1 = 'rgb(727781)'
M.overlay1Alpha = '727781'

M.overlay2 = 'rgb(5D6168)'
M.overlay2Alpha = '5D6168'

M.subtext0 = 'rgb(515459)'
M.subtext0Alpha = '515459'

M.subtext1 = 'rgb(434548)'
M.subtext1Alpha = '434548'

M.text = 'rgb(2F3033)'
M.textAlpha = '2F3033'

M.text_hi = 'rgb(1F2022)'
M.text_hiAlpha = '1F2022'

M.yellow = 'rgb(896800)'
M.yellowAlpha = '896800'

M.yellow_hi = 'rgb(977300)'
M.yellow_hiAlpha = '977300'

M.orange = 'rgb(9F591B)'
M.orangeAlpha = '9F591B'

M.orange_hi = 'rgb(AE672B)'
M.orange_hiAlpha = 'AE672B'

M.red = 'rgb(A40005)'
M.redAlpha = 'A40005'

M.red_hi = 'rgb(CA2822)'
M.red_hiAlpha = 'CA2822'

M.green = 'rgb(357D41)'
M.greenAlpha = '357D41'

M.green_hi = 'rgb(398145)'
M.green_hiAlpha = '398145'

M.sage = 'rgb(007376)'
M.sageAlpha = '007376'

M.sage_hi = 'rgb(008689)'
M.sage_hiAlpha = '008689'

M.denim = 'rgb(0019A8)'
M.denimAlpha = '0019A8'

M.denim_hi = 'rgb(406BD0)'
M.denim_hiAlpha = '406BD0'

M.clay = 'rgb(7660AB)'
M.clayAlpha = '7660AB'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(896800)',
        inactive_border = 'rgb(ADB7CB)',
        nogroup_border = 'rgb(9794BE)',
        nogroup_border_active = 'rgb(7660AB)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(896800)',
        border_inactive = 'rgb(9F977A)',
        border_locked_active = 'rgb(9F591B)',
        border_locked_inactive = 'rgb(A79185)',
      },
      groupbar = {
        text_color = 'rgb(1F2022)',
        text_color_inactive = 'rgb(515459)',
        col = {
          active = 'rgb(896800)',
          inactive = 'rgb(ADB7CB)',
          locked_active = 'rgb(9F591B)',
          locked_inactive = 'rgb(A79185)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(2F303324)',
      },
    },
    misc = {
      background_color = 'rgb(E5EAF6)',
    },
  })
end

return M
