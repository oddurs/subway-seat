-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes — Under the quarries: the same green with the lights turned down.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#141D19" }
style.background2              = { common.color "#0F1612" }
style.background3              = { common.color "#1D2822" }
style.text                     = { common.color "#C0C7C3" }
style.caret                    = { common.color "#EBC168" }
style.accent                   = { common.color "#EBC168" }
style.dim                      = { common.color "#738079" }
style.divider                  = { common.color "#0B100D" }
style.selection                = { common.color "#34423B" }
style.line_number              = { common.color "#57645D" }
style.line_number2             = { common.color "#EBC168" }
style.line_highlight           = { common.color "#1D2822" }
style.scrollbar                = { common.color "#34423B" }
style.scrollbar2               = { common.color "#57645D" }
style.scrollbar_track          = { common.color "#0F1612" }
style.nagbar                   = { common.color "#CD6B63" }
style.nagbar_text              = { common.color "#0B100D" }
style.nagbar_dim               = { common.color "rgba(6, 8, 6, 0.45)" }
style.drag_overlay             = { common.color "rgba(213, 220, 216, 0.1)" }
style.drag_overlay_tab         = { common.color "#EBC168" }
style.good                     = { common.color "#80C28E" }
style.warn                     = { common.color "#EBC168" }
style.error                    = { common.color "#E1837A" }
style.modified                 = { common.color "#EBC168" }
style.guide                    = { common.color "#1D2822" }
style.guide_highlight          = { common.color "#34423B" }
style.bracketmatch_color       = { common.color "#FBD380" }
style.bracketmatch_char_color  = { common.color "#FBD380" }
style.bracketmatch_block_color = { common.color "#27332D" }
style.bracketmatch_frame_color = { common.color "#34423B" }

style.syntax["normal"]   = { common.color "#D5DCD8" }
style.syntax["symbol"]   = { common.color "#D5DCD8" }
style.syntax["comment"]  = { common.color "#738079" }
style.syntax["keyword"]  = { common.color "#D0914F" }
style.syntax["keyword2"] = { common.color "#7BB096" }
style.syntax["number"]   = { common.color "#E1837A" }
style.syntax["literal"]  = { common.color "#E1837A" }
style.syntax["string"]   = { common.color "#80C28E" }
style.syntax["operator"] = { common.color "#8E9993" }
style.syntax["function"] = { common.color "#EBC168" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
