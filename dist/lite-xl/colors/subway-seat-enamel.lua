-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Enamel — Cream enamel panels in the morning sun. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#F4E9D4" }
style.background2              = { common.color "#EBDEC6" }
style.background3              = { common.color "#FAF4EA" }
style.text                     = { common.color "#54402F" }
style.caret                    = { common.color "#AD4E00" }
style.accent                   = { common.color "#AD4E00" }
style.dim                      = { common.color "#8C7254" }
style.divider                  = { common.color "#E2D3B6" }
style.selection                = { common.color "#CAB48E" }
style.line_number              = { common.color "#A58C6A" }
style.line_number2             = { common.color "#AD4E00" }
style.line_highlight           = { common.color "#EBDEC6" }
style.scrollbar                = { common.color "#BAA07A" }
style.scrollbar2               = { common.color "#A58C6A" }
style.scrollbar_track          = { common.color "#EBDEC6" }
style.nagbar                   = { common.color "#992418" }
style.nagbar_text              = { common.color "#F4E9D4" }
style.nagbar_dim               = { common.color "rgba(62, 44, 30, 0.45)" }
style.drag_overlay             = { common.color "rgba(62, 44, 30, 0.1)" }
style.drag_overlay_tab         = { common.color "#AD4E00" }
style.good                     = { common.color "#66740F" }
style.warn                     = { common.color "#936200" }
style.error                    = { common.color "#BC4031" }
style.modified                 = { common.color "#936200" }
style.guide                    = { common.color "#D9C8A7" }
style.guide_highlight          = { common.color "#BAA07A" }
style.bracketmatch_color       = { common.color "#AD4E00" }
style.bracketmatch_char_color  = { common.color "#AD4E00" }
style.bracketmatch_block_color = { common.color "#E7DCC7" }
style.bracketmatch_frame_color = { common.color "#BAA07A" }

style.syntax["normal"]   = { common.color "#3E2C1E" }
style.syntax["symbol"]   = { common.color "#3E2C1E" }
style.syntax["comment"]  = { common.color "#8C7254" }
style.syntax["keyword"]  = { common.color "#AD4E00" }
style.syntax["keyword2"] = { common.color "#3E7157" }
style.syntax["number"]   = { common.color "#BC4031" }
style.syntax["literal"]  = { common.color "#BC4031" }
style.syntax["string"]   = { common.color "#66740F" }
style.syntax["operator"] = { common.color "#735C44" }
style.syntax["function"] = { common.color "#936200" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
