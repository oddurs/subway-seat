-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard for Hyprland 0.55+.
--
--   local colors = require("themes.paris-guimard")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(141A17)'
M.crustAlpha = '141A17'

M.mantle = 'rgb(1A231E)'
M.mantleAlpha = '1A231E'

M.base = 'rgb(212D27)'
M.baseAlpha = '212D27'

M.surface0 = 'rgb(2A3831)'
M.surface0Alpha = '2A3831'

M.surface1 = 'rgb(34453C)'
M.surface1Alpha = '34453C'

M.surface2 = 'rgb(42544B)'
M.surface2Alpha = '42544B'

M.overlay0 = 'rgb(5B6A62)'
M.overlay0Alpha = '5B6A62'

M.overlay1 = 'rgb(77847D)'
M.overlay1Alpha = '77847D'

M.overlay2 = 'rgb(929D97)'
M.overlay2Alpha = '929D97'

M.subtext0 = 'rgb(ABB4AF)'
M.subtext0Alpha = 'ABB4AF'

M.subtext1 = 'rgb(C3CAC6)'
M.subtext1Alpha = 'C3CAC6'

M.text = 'rgb(DAE0DC)'
M.textAlpha = 'DAE0DC'

M.text_hi = 'rgb(EAEEEC)'
M.text_hiAlpha = 'EAEEEC'

M.yellow = 'rgb(EBC168)'
M.yellowAlpha = 'EBC168'

M.yellow_hi = 'rgb(FBD380)'
M.yellow_hiAlpha = 'FBD380'

M.orange = 'rgb(D0914F)'
M.orangeAlpha = 'D0914F'

M.orange_hi = 'rgb(E7AB6D)'
M.orange_hiAlpha = 'E7AB6D'

M.red = 'rgb(CD6B63)'
M.redAlpha = 'CD6B63'

M.red_hi = 'rgb(E1837A)'
M.red_hiAlpha = 'E1837A'

M.green = 'rgb(80C28E)'
M.greenAlpha = '80C28E'

M.green_hi = 'rgb(8FD59E)'
M.green_hiAlpha = '8FD59E'

M.sage = 'rgb(7BB096)'
M.sageAlpha = '7BB096'

M.sage_hi = 'rgb(98CCB2)'
M.sage_hiAlpha = '98CCB2'

M.denim = 'rgb(709BC8)'
M.denimAlpha = '709BC8'

M.denim_hi = 'rgb(8DB6E2)'
M.denim_hiAlpha = '8DB6E2'

M.clay = 'rgb(CE96B4)'
M.clayAlpha = 'CE96B4'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(EBC168)',
        inactive_border = 'rgb(34453C)',
        nogroup_border = 'rgb(72656C)',
        nogroup_border_active = 'rgb(CE96B4)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(EBC168)',
        border_inactive = 'rgb(7D774E)',
        border_locked_active = 'rgb(D0914F)',
        border_locked_inactive = 'rgb(726344)',
      },
      groupbar = {
        text_color = 'rgb(EAEEEC)',
        text_color_inactive = 'rgb(ABB4AF)',
        col = {
          active = 'rgb(EBC168)',
          inactive = 'rgb(42544B)',
          locked_active = 'rgb(D0914F)',
          locked_inactive = 'rgb(726344)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(0A0D0C99)',
      },
    },
    misc = {
      background_color = 'rgb(212D27)',
    },
  })
end

return M
