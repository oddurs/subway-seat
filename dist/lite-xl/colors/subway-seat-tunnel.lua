-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat Tunnel — The late local after midnight: espresso-deep, same warm lights.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#24180E" }
style.background2              = { common.color "#1B120A" }
style.background3              = { common.color "#302115" }
style.text                     = { common.color "#D6C3A0" }
style.caret                    = { common.color "#F3BF45" }
style.accent                   = { common.color "#F3BF45" }
style.dim                      = { common.color "#8A7053" }
style.divider                  = { common.color "#140D07" }
style.selection                = { common.color "#4F3927" }
style.line_number              = { common.color "#6A523C" }
style.line_number2             = { common.color "#F3BF45" }
style.line_highlight           = { common.color "#302115" }
style.scrollbar                = { common.color "#4F3927" }
style.scrollbar2               = { common.color "#6A523C" }
style.scrollbar_track          = { common.color "#1B120A" }
style.nagbar                   = { common.color "#D2503A" }
style.nagbar_text              = { common.color "#140D07" }
style.nagbar_dim               = { common.color "rgba(0, 0, 0, 0.45)" }
style.drag_overlay             = { common.color "rgba(233, 216, 182, 0.1)" }
style.drag_overlay_tab         = { common.color "#F3BF45" }
style.good                     = { common.color "#A3AE4B" }
style.warn                     = { common.color "#F3BF45" }
style.error                    = { common.color "#EC6A50" }
style.modified                 = { common.color "#F3BF45" }
style.guide                    = { common.color "#302115" }
style.guide_highlight          = { common.color "#4F3927" }
style.bracketmatch_color       = { common.color "#FFD36B" }
style.bracketmatch_char_color  = { common.color "#FFD36B" }
style.bracketmatch_block_color = { common.color "#3D2C1D" }
style.bracketmatch_frame_color = { common.color "#4F3927" }

style.syntax["normal"]   = { common.color "#E9D8B6" }
style.syntax["symbol"]   = { common.color "#E9D8B6" }
style.syntax["comment"]  = { common.color "#8A7053" }
style.syntax["keyword"]  = { common.color "#EC7F31" }
style.syntax["keyword2"] = { common.color "#86AD95" }
style.syntax["number"]   = { common.color "#EC6A50" }
style.syntax["literal"]  = { common.color "#EC6A50" }
style.syntax["string"]   = { common.color "#A3AE4B" }
style.syntax["operator"] = { common.color "#A48B6C" }
style.syntax["function"] = { common.color "#F3BF45" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
