-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Moquette — The seat you're sitting on. Corporate Blue, turned right down.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#1E2941" }
style.background2              = { common.color "#172032" }
style.background3              = { common.color "#263451" }
style.text                     = { common.color "#C1C9D8" }
style.caret                    = { common.color "#F2C03F" }
style.accent                   = { common.color "#F2C03F" }
style.dim                      = { common.color "#73819C" }
style.divider                  = { common.color "#121826" }
style.selection                = { common.color "#3D4F72" }
style.line_number              = { common.color "#576685" }
style.line_number2             = { common.color "#F2C03F" }
style.line_highlight           = { common.color "#263451" }
style.scrollbar                = { common.color "#3D4F72" }
style.scrollbar2               = { common.color "#576685" }
style.scrollbar_track          = { common.color "#172032" }
style.nagbar                   = { common.color "#DB6052" }
style.nagbar_text              = { common.color "#121826" }
style.nagbar_dim               = { common.color "rgba(9, 12, 19, 0.45)" }
style.drag_overlay             = { common.color "rgba(216, 222, 234, 0.1)" }
style.drag_overlay_tab         = { common.color "#F2C03F" }
style.good                     = { common.color "#77C581" }
style.warn                     = { common.color "#F2C03F" }
style.error                    = { common.color "#F17869" }
style.modified                 = { common.color "#F2C03F" }
style.guide                    = { common.color "#263451" }
style.guide_highlight          = { common.color "#3D4F72" }
style.bracketmatch_color       = { common.color "#FFD36C" }
style.bracketmatch_char_color  = { common.color "#FFD36C" }
style.bracketmatch_block_color = { common.color "#303F61" }
style.bracketmatch_frame_color = { common.color "#3D4F72" }

style.syntax["normal"]   = { common.color "#D8DEEA" }
style.syntax["symbol"]   = { common.color "#D8DEEA" }
style.syntax["comment"]  = { common.color "#73819C" }
style.syntax["keyword"]  = { common.color "#DE8946" }
style.syntax["keyword2"] = { common.color "#54B4B5" }
style.syntax["number"]   = { common.color "#F17869" }
style.syntax["literal"]  = { common.color "#F17869" }
style.syntax["string"]   = { common.color "#77C581" }
style.syntax["operator"] = { common.color "#8F9AB0" }
style.syntax["function"] = { common.color "#F2C03F" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
