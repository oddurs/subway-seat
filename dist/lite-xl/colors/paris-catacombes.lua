-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes — Under the quarries: the same green with the lights turned down.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#121E19" }
style.background2              = { common.color "#0D1711" }
style.background3              = { common.color "#1A2921" }
style.text                     = { common.color "#BFC8C2" }
style.caret                    = { common.color "#F2BF4B" }
style.accent                   = { common.color "#F2BF4B" }
style.dim                      = { common.color "#708178" }
style.divider                  = { common.color "#0A100D" }
style.selection                = { common.color "#31433A" }
style.line_number              = { common.color "#54655C" }
style.line_number2             = { common.color "#F2BF4B" }
style.line_highlight           = { common.color "#1A2921" }
style.scrollbar                = { common.color "#31433A" }
style.scrollbar2               = { common.color "#54655C" }
style.scrollbar_track          = { common.color "#0D1711" }
style.nagbar                   = { common.color "#CD6B63" }
style.nagbar_text              = { common.color "#0A100D" }
style.nagbar_dim               = { common.color "rgba(5, 8, 6, 0.45)" }
style.drag_overlay             = { common.color "rgba(212, 221, 215, 0.1)" }
style.drag_overlay_tab         = { common.color "#F2BF4B" }
style.good                     = { common.color "#80C28E" }
style.warn                     = { common.color "#F2BF4B" }
style.error                    = { common.color "#E1837A" }
style.modified                 = { common.color "#F2BF4B" }
style.guide                    = { common.color "#1A2921" }
style.guide_highlight          = { common.color "#31433A" }
style.bracketmatch_color       = { common.color "#FFD273" }
style.bracketmatch_char_color  = { common.color "#FFD273" }
style.bracketmatch_block_color = { common.color "#24342C" }
style.bracketmatch_frame_color = { common.color "#31433A" }

style.syntax["normal"]   = { common.color "#D4DDD7" }
style.syntax["symbol"]   = { common.color "#D4DDD7" }
style.syntax["comment"]  = { common.color "#708178" }
style.syntax["keyword"]  = { common.color "#D0914F" }
style.syntax["keyword2"] = { common.color "#6CA087" }
style.syntax["number"]   = { common.color "#E1837A" }
style.syntax["literal"]  = { common.color "#E1837A" }
style.syntax["string"]   = { common.color "#80C28E" }
style.syntax["operator"] = { common.color "#8C9A92" }
style.syntax["function"] = { common.color "#F2BF4B" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
