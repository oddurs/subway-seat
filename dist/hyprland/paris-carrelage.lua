-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(BFDDCD)'
M.crustAlpha = 'BFDDCD'

M.mantle = 'rgb(D0E6D8)'
M.mantleAlpha = 'D0E6D8'

M.base = 'rgb(DEF0E6)'
M.baseAlpha = 'DEF0E6'

M.surface0 = 'rgb(ACD5BF)'
M.surface0Alpha = 'ACD5BF'

M.surface1 = 'rgb(96C4AC)'
M.surface1Alpha = '96C4AC'

M.surface2 = 'rgb(84B09A)'
M.surface2Alpha = '84B09A'

M.overlay0 = 'rgb(769B87)'
M.overlay0Alpha = '769B87'

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

M.orange = 'rgb(754500)'
M.orangeAlpha = '754500'

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

M.sage = 'rgb(086142)'
M.sageAlpha = '086142'

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
        inactive_border = 'rgb(96C4AC)',
        nogroup_border = 'rgb(989899)',
        nogroup_border_active = 'rgb(9A557D)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(8A6700)',
        border_inactive = 'rgb(919F67)',
        border_locked_active = 'rgb(754500)',
        border_locked_inactive = 'rgb(899167)',
      },
      groupbar = {
        text_color = 'rgb(18231D)',
        text_color_inactive = 'rgb(45594F)',
        col = {
          active = 'rgb(8A6700)',
          inactive = 'rgb(96C4AC)',
          locked_active = 'rgb(754500)',
          locked_inactive = 'rgb(899167)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(25352C24)',
      },
    },
    misc = {
      background_color = 'rgb(DEF0E6)',
    },
  })
end

return M
