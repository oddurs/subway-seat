-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(D4DCD3)'
M.crustAlpha = 'D4DCD3'

M.mantle = 'rgb(E1E7E0)'
M.mantleAlpha = 'E1E7E0'

M.base = 'rgb(EEF3ED)'
M.baseAlpha = 'EEF3ED'

M.surface0 = 'rgb(C7D3C5)'
M.surface0Alpha = 'C7D3C5'

M.surface1 = 'rgb(B1C0B0)'
M.surface1Alpha = 'B1C0B0'

M.surface2 = 'rgb(9BAC9A)'
M.surface2Alpha = '9BAC9A'

M.overlay0 = 'rgb(879887)'
M.overlay0Alpha = '879887'

M.overlay1 = 'rgb(6E7C6E)'
M.overlay1Alpha = '6E7C6E'

M.overlay2 = 'rgb(586459)'
M.overlay2Alpha = '586459'

M.subtext0 = 'rgb(4C574D)'
M.subtext0Alpha = '4C574D'

M.subtext1 = 'rgb(3D473E)'
M.subtext1Alpha = '3D473E'

M.text = 'rgb(2A342B)'
M.textAlpha = '2A342B'

M.text_hi = 'rgb(1B221C)'
M.text_hiAlpha = '1B221C'

M.yellow = 'rgb(8A6700)'
M.yellowAlpha = '8A6700'

M.yellow_hi = 'rgb(997300)'
M.yellow_hiAlpha = '997300'

M.orange = 'rgb(8A5308)'
M.orangeAlpha = '8A5308'

M.orange_hi = 'rgb(AE6800)'
M.orange_hiAlpha = 'AE6800'

M.red = 'rgb(932D29)'
M.redAlpha = '932D29'

M.red_hi = 'rgb(BB403B)'
M.red_hiAlpha = 'BB403B'

M.green = 'rgb(207F41)'
M.greenAlpha = '207F41'

M.green_hi = 'rgb(168540)'
M.green_hiAlpha = '168540'

M.sage = 'rgb(0B714D)'
M.sageAlpha = '0B714D'

M.sage_hi = 'rgb(3D8666)'
M.sage_hiAlpha = '3D8666'

M.denim = 'rgb(27629C)'
M.denimAlpha = '27629C'

M.denim_hi = 'rgb(3E75AD)'
M.denim_hiAlpha = '3E75AD'

M.clay = 'rgb(9A557D)'
M.clayAlpha = '9A557D'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(8A6700)',
        inactive_border = 'rgb(B1C0B0)',
        nogroup_border = 'rgb(A8959C)',
        nogroup_border_active = 'rgb(9A557D)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(8A6700)',
        border_inactive = 'rgb(A19C6A)',
        border_locked_active = 'rgb(8A5308)',
        border_locked_inactive = 'rgb(A1946D)',
      },
      groupbar = {
        text_color = 'rgb(1B221C)',
        text_color_inactive = 'rgb(4C574D)',
        col = {
          active = 'rgb(8A6700)',
          inactive = 'rgb(B1C0B0)',
          locked_active = 'rgb(8A5308)',
          locked_inactive = 'rgb(A1946D)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(2A342B24)',
      },
    },
    misc = {
      background_color = 'rgb(EEF3ED)',
    },
  })
end

return M
