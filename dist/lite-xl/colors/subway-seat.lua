-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat — Walnut paneling and orange bucket seats. The original.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#362619" }
style.background2              = { common.color "#2A1D13" }
style.background3              = { common.color "#43301F" }
style.text                     = { common.color "#D9C6A3" }
style.caret                    = { common.color "#F3BF45" }
style.accent                   = { common.color "#F3BF45" }
style.dim                      = { common.color "#967B5C" }
style.divider                  = { common.color "#20160E" }
style.selection                = { common.color "#634932" }
style.line_number              = { common.color "#7B6047" }
style.line_number2             = { common.color "#F3BF45" }
style.line_highlight           = { common.color "#43301F" }
style.scrollbar                = { common.color "#634932" }
style.scrollbar2               = { common.color "#7B6047" }
style.scrollbar_track          = { common.color "#2A1D13" }
style.nagbar                   = { common.color "#E05C45" }
style.nagbar_text              = { common.color "#20160E" }
style.nagbar_dim               = { common.color "rgba(0, 0, 0, 0.45)" }
style.drag_overlay             = { common.color "rgba(237, 220, 188, 0.1)" }
style.drag_overlay_tab         = { common.color "#F3BF45" }
style.good                     = { common.color "#ADB956" }
style.warn                     = { common.color "#F3BF45" }
style.error                    = { common.color "#F97160" }
style.modified                 = { common.color "#F3BF45" }
style.guide                    = { common.color "#43301F" }
style.guide_highlight          = { common.color "#634932" }
style.bracketmatch_color       = { common.color "#FFD36B" }
style.bracketmatch_char_color  = { common.color "#FFD36B" }
style.bracketmatch_block_color = { common.color "#513B27" }
style.bracketmatch_frame_color = { common.color "#634932" }

style.syntax["normal"]   = { common.color "#EDDCBC" }
style.syntax["symbol"]   = { common.color "#EDDCBC" }
style.syntax["comment"]  = { common.color "#967B5C" }
style.syntax["keyword"]  = { common.color "#EC7F31" }
style.syntax["keyword2"] = { common.color "#86AD95" }
style.syntax["number"]   = { common.color "#F97160" }
style.syntax["literal"]  = { common.color "#F97160" }
style.syntax["string"]   = { common.color "#ADB956" }
style.syntax["operator"] = { common.color "#AE9575" }
style.syntax["function"] = { common.color "#F3BF45" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
