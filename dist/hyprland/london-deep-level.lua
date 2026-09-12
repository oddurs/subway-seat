-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Deep Level for Hyprland 0.55+.
--
--   local colors = require("themes.london-deep-level")   -- the palette
--   colors.apply()                                   -- borders, groups, groupbar
--
local M = {}

M.crust = 'rgb(0A0E18)'
M.crustAlpha = '0A0E18'

M.mantle = 'rgb(0D1421)'
M.mantleAlpha = '0D1421'

M.base = 'rgb(121A2D)'
M.baseAlpha = '121A2D'

M.surface0 = 'rgb(1A243A)'
M.surface0Alpha = '1A243A'

M.surface1 = 'rgb(232F49)'
M.surface1Alpha = '232F49'

M.surface2 = 'rgb(303E5B)'
M.surface2Alpha = '303E5B'

M.overlay0 = 'rgb(53617D)'
M.overlay0Alpha = '53617D'

M.overlay1 = 'rgb(6F7C97)'
M.overlay1Alpha = '6F7C97'

M.overlay2 = 'rgb(8B96AC)'
M.overlay2Alpha = '8B96AC'

M.subtext0 = 'rgb(A5AEC0)'
M.subtext0Alpha = 'A5AEC0'

M.subtext1 = 'rgb(BEC6D5)'
M.subtext1Alpha = 'BEC6D5'

M.text = 'rgb(D4DAE7)'
M.textAlpha = 'D4DAE7'

M.text_hi = 'rgb(E7EBF3)'
M.text_hiAlpha = 'E7EBF3'

M.yellow = 'rgb(F2C03F)'
M.yellowAlpha = 'F2C03F'

M.yellow_hi = 'rgb(FFD36C)'
M.yellow_hiAlpha = 'FFD36C'

M.orange = 'rgb(DE8946)'
M.orangeAlpha = 'DE8946'

M.orange_hi = 'rgb(E5AA7F)'
M.orange_hiAlpha = 'E5AA7F'

M.red = 'rgb(DB6052)'
M.redAlpha = 'DB6052'

M.red_hi = 'rgb(FE8474)'
M.red_hiAlpha = 'FE8474'

M.green = 'rgb(77C581)'
M.greenAlpha = '77C581'

M.green_hi = 'rgb(9AD2A0)'
M.green_hiAlpha = '9AD2A0'

M.sage = 'rgb(54B4B5)'
M.sageAlpha = '54B4B5'

M.sage_hi = 'rgb(72D1D3)'
M.sage_hiAlpha = '72D1D3'

M.denim = 'rgb(7595DA)'
M.denimAlpha = '7595DA'

M.denim_hi = 'rgb(8BB0FF)'
M.denim_hiAlpha = '8BB0FF'

M.clay = 'rgb(AE9EDC)'
M.clayAlpha = 'AE9EDC'

function M.apply()
  hl.config({
    general = {
      col = {
        active_border = 'rgb(F2C03F)',
        inactive_border = 'rgb(232F49)',
        nogroup_border = 'rgb(5B5B84)',
        nogroup_border_active = 'rgb(AE9EDC)',
      },
    },
    group = {
      col = {
        border_active = 'rgb(F2C03F)',
        border_inactive = 'rgb(766945)',
        border_locked_active = 'rgb(DE8946)',
        border_locked_inactive = 'rgb(6E5348)',
      },
      groupbar = {
        text_color = 'rgb(E7EBF3)',
        text_color_inactive = 'rgb(A5AEC0)',
        col = {
          active = 'rgb(F2C03F)',
          inactive = 'rgb(303E5B)',
          locked_active = 'rgb(DE8946)',
          locked_inactive = 'rgb(6E5348)',
        },
      },
    },
    decoration = {
      shadow = {
        color = 'rgba(05070C99)',
      },
    },
    misc = {
      background_color = 'rgb(121A2D)',
    },
  })
end

return M
