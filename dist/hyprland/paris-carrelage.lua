-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(CAD9D1)'
M.crustAlpha = 'CAD9D1'

M.mantle = 'rgb(D8E3DC)'
M.mantleAlpha = 'D8E3DC'

M.base = 'rgb(E4EDE8)'
M.baseAlpha = 'E4EDE8'

M.surface0 = 'rgb(BAD0C4)'
M.surface0Alpha = 'BAD0C4'

M.surface1 = 'rgb(A3BFB0)'
M.surface1Alpha = 'A3BFB0'

M.surface2 = 'rgb(8EAD9D)'
M.surface2Alpha = '8EAD9D'

M.overlay0 = 'rgb(7B9989)'
M.overlay0Alpha = '7B9989'

M.overlay1 = 'rgb(627F70)'
M.overlay1Alpha = '627F70'

M.overlay2 = 'rgb(4F675B)'
M.overlay2Alpha = '4F675B'

M.subtext0 = 'rgb(45594F)'
M.subtext0Alpha = '45594F'

M.subtext1 = 'rgb(374940)'
M.subtext1Alpha = '374940'

M.text = 'rgb(25352C)'
M.textAlpha = '25352C'

M.text_hi = 'rgb(18231D)'
M.text_hiAlpha = '18231D'

M.yellow = 'rgb(8A6700)'
M.yellowAlpha = '8A6700'

M.yellow_hi = 'rgb(997300)'
M.yellow_hiAlpha = '997300'

M.orange = 'rgb(9B5D00)'
M.orangeAlpha = '9B5D00'

M.orange_hi = 'rgb(AE6800)'
M.orange_hiAlpha = 'AE6800'

M.red = 'rgb(9E171B)'
M.redAlpha = '9E171B'

M.red_hi = 'rgb(BB403B)'
M.red_hiAlpha = 'BB403B'

M.green = 'rgb(18803F)'
M.greenAlpha = '18803F'

M.green_hi = 'rgb(168540)'
M.green_hiAlpha = '168540'

M.sage = 'rgb(277555)'
M.sageAlpha = '277555'

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
        inactive_border = 'rgb(A3BFB0)',
        nogroup_border = 'rgb(9F959C)',
        nogroup_border_active = 'rgb(9A557D)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(8A6700)',
        border_inactive = 'rgb(999C6A)',
        border_locked_active = 'rgb(9B5D00)',
        border_locked_inactive = 'rgb(A0986A)',
      },
      groupbar = {
        text_color = 'rgb(18231D)',
        text_color_inactive = 'rgb(45594F)',
        col = {
          active = 'rgb(8A6700)',
          inactive = 'rgb(A3BFB0)',
          locked_active = 'rgb(9B5D00)',
          locked_inactive = 'rgb(A0986A)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(25352C24)',
      },
    },
    misc = {
      background_color = 'rgb(E4EDE8)',
    },
  })
end

return M
