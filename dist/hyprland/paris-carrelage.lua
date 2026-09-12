-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(C8E0D3)'
M.crustAlpha = 'C8E0D3'

M.mantle = 'rgb(D8EADF)'
M.mantleAlpha = 'D8EADF'

M.base = 'rgb(E7F5ED)'
M.baseAlpha = 'E7F5ED'

M.surface0 = 'rgb(B7D8C6)'
M.surface0Alpha = 'B7D8C6'

M.surface1 = 'rgb(9FC6B1)'
M.surface1Alpha = '9FC6B1'

M.surface2 = 'rgb(89B19D)'
M.surface2Alpha = '89B19D'

M.overlay0 = 'rgb(789C88)'
M.overlay0Alpha = '789C88'

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
        inactive_border = 'rgb(9FC6B1)',
        nogroup_border = 'rgb(9D999C)',
        nogroup_border_active = 'rgb(9A557D)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(8A6700)',
        border_inactive = 'rgb(97A06A)',
        border_locked_active = 'rgb(754500)',
        border_locked_inactive = 'rgb(8E926A)',
      },
      groupbar = {
        text_color = 'rgb(18231D)',
        text_color_inactive = 'rgb(45594F)',
        col = {
          active = 'rgb(8A6700)',
          inactive = 'rgb(9FC6B1)',
          locked_active = 'rgb(754500)',
          locked_inactive = 'rgb(8E926A)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(25352C24)',
      },
    },
    misc = {
      background_color = 'rgb(E7F5ED)',
    },
  })
end

return M
