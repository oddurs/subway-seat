-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Enamel — Cream enamel panels in the morning sun. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#F8EFDF" }
style.background2              = { common.color "#EEE4D0" }
style.background3              = { common.color "#FCF7EF" }
style.text                     = { common.color "#54402F" }
style.caret                    = { common.color "#A04800" }
style.accent                   = { common.color "#A04800" }
style.dim                      = { common.color "#8C7254" }
style.divider                  = { common.color "#E4D8C0" }
style.selection                = { common.color "#CBB898" }
style.line_number              = { common.color "#A58D6D" }
style.line_number2             = { common.color "#A04800" }
style.line_highlight           = { common.color "#EEE4D0" }
style.scrollbar                = { common.color "#BAA380" }
style.scrollbar2               = { common.color "#A58D6D" }
style.scrollbar_track          = { common.color "#EEE4D0" }
style.nagbar                   = { common.color "#992418" }
style.nagbar_text              = { common.color "#F8EFDF" }
style.nagbar_dim               = { common.color "rgba(62, 44, 30, 0.45)" }
style.drag_overlay             = { common.color "rgba(62, 44, 30, 0.1)" }
style.drag_overlay_tab         = { common.color "#A04800" }
style.good                     = { common.color "#66740F" }
style.warn                     = { common.color "#976608" }
style.error                    = { common.color "#BF4233" }
style.modified                 = { common.color "#976608" }
style.guide                    = { common.color "#DBCDB3" }
style.guide_highlight          = { common.color "#BAA380" }
style.bracketmatch_color       = { common.color "#A04800" }
style.bracketmatch_char_color  = { common.color "#A04800" }
style.bracketmatch_block_color = { common.color "#EBE1D1" }
style.bracketmatch_frame_color = { common.color "#BAA380" }

style.syntax["normal"]   = { common.color "#3E2C1E" }
style.syntax["symbol"]   = { common.color "#3E2C1E" }
style.syntax["comment"]  = { common.color "#8C7254" }
style.syntax["keyword"]  = { common.color "#A04800" }
style.syntax["keyword2"] = { common.color "#3E7157" }
style.syntax["number"]   = { common.color "#BF4233" }
style.syntax["literal"]  = { common.color "#BF4233" }
style.syntax["string"]   = { common.color "#66740F" }
style.syntax["operator"] = { common.color "#735C44" }
style.syntax["function"] = { common.color "#976608" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
