-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage for Hyprland 0.55+.
--
--   local colors = require("themes.paris-carrelage")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(D5DBDA)'
M.crustAlpha = 'D5DBDA'

M.mantle = 'rgb(E1E6E5)'
M.mantleAlpha = 'E1E6E5'

M.base = 'rgb(EEF2F1)'
M.baseAlpha = 'EEF2F1'

M.surface0 = 'rgb(C6D2CF)'
M.surface0Alpha = 'C6D2CF'

M.surface1 = 'rgb(B0BFBB)'
M.surface1Alpha = 'B0BFBB'

M.surface2 = 'rgb(99ABA6)'
M.surface2Alpha = '99ABA6'

M.overlay0 = 'rgb(859792)'
M.overlay0Alpha = '859792'

M.overlay1 = 'rgb(6C7C76)'
M.overlay1Alpha = '6C7C76'

M.overlay2 = 'rgb(56645F)'
M.overlay2Alpha = '56645F'

M.subtext0 = 'rgb(4A5752)'
M.subtext0Alpha = '4A5752'

M.subtext1 = 'rgb(3B4742)'
M.subtext1Alpha = '3B4742'

M.text = 'rgb(27342F)'
M.textAlpha = '27342F'

M.text_hi = 'rgb(19221E)'
M.text_hiAlpha = '19221E'

M.yellow = 'rgb(916D07)'
M.yellowAlpha = '916D07'

M.yellow_hi = 'rgb(A07A12)'
M.yellow_hiAlpha = 'A07A12'

M.orange = 'rgb(764C00)'
M.orangeAlpha = '764C00'

M.orange_hi = 'rgb(885A00)'
M.orange_hiAlpha = '885A00'

M.red = 'rgb(88251E)'
M.redAlpha = '88251E'

M.red_hi = 'rgb(AC3B32)'
M.red_hiAlpha = 'AC3B32'

M.green = 'rgb(218366)'
M.greenAlpha = '218366'

M.green_hi = 'rgb(278D6E)'
M.green_hiAlpha = '278D6E'

M.sage = 'rgb(006267)'
M.sageAlpha = '006267'

M.sage_hi = 'rgb(027479)'
M.sage_hiAlpha = '027479'

M.denim = 'rgb(25629B)'
M.denimAlpha = '25629B'

M.denim_hi = 'rgb(3D75AD)'
M.denim_hiAlpha = '3D75AD'

M.clay = 'rgb(B36B51)'
M.clayAlpha = 'B36B51'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(916D07)',
        inactive_border = 'rgb(B0BFBB)',
        nogroup_border = 'rgb(B19D91)',
        nogroup_border_active = 'rgb(B36B51)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(916D07)',
        border_inactive = 'rgb(A49E73)',
        border_locked_active = 'rgb(764C00)',
        border_locked_inactive = 'rgb(999170)',
      },
      groupbar = {
        text_color = 'rgb(19221E)',
        text_color_inactive = 'rgb(4A5752)',
        col = {
          active = 'rgb(916D07)',
          inactive = 'rgb(B0BFBB)',
          locked_active = 'rgb(764C00)',
          locked_inactive = 'rgb(999170)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(27342F24)',
      },
    },
    misc = {
      background_color = 'rgb(EEF2F1)',
    },
  })
end

return M
