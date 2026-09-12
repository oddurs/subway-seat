-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Catacombes — Under the quarries: the same green with the lights turned down.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#062017" }
style.background2              = { common.color "#061811" }
style.background3              = { common.color "#0A2B20" }
style.text                     = { common.color "#B8CAC2" }
style.caret                    = { common.color "#EBC342" }
style.accent                   = { common.color "#EBC342" }
style.dim                      = { common.color "#648576" }
style.divider                  = { common.color "#05120C" }
style.selection                = { common.color "#1E4738" }
style.line_number              = { common.color "#456A5B" }
style.line_number2             = { common.color "#EBC342" }
style.line_highlight           = { common.color "#0A2B20" }
style.scrollbar                = { common.color "#1E4738" }
style.scrollbar2               = { common.color "#456A5B" }
style.scrollbar_track          = { common.color "#061811" }
style.nagbar                   = { common.color "#DA6058" }
style.nagbar_text              = { common.color "#05120C" }
style.nagbar_dim               = { common.color "rgba(2, 9, 6, 0.45)" }
style.drag_overlay             = { common.color "rgba(207, 222, 215, 0.1)" }
style.drag_overlay_tab         = { common.color "#EBC342" }
style.good                     = { common.color "#73C686" }
style.warn                     = { common.color "#EBC342" }
style.error                    = { common.color "#EF796F" }
style.modified                 = { common.color "#EBC342" }
style.guide                    = { common.color "#0A2B20" }
style.guide_highlight          = { common.color "#1E4738" }
style.bracketmatch_color       = { common.color "#FBD664" }
style.bracketmatch_char_color  = { common.color "#FBD664" }
style.bracketmatch_block_color = { common.color "#13382A" }
style.bracketmatch_frame_color = { common.color "#1E4738" }

style.syntax["normal"]   = { common.color "#CFDED7" }
style.syntax["symbol"]   = { common.color "#CFDED7" }
style.syntax["comment"]  = { common.color "#648576" }
style.syntax["keyword"]  = { common.color "#D78E3C" }
style.syntax["keyword2"] = { common.color "#6FB393" }
style.syntax["number"]   = { common.color "#EF796F" }
style.syntax["literal"]  = { common.color "#EF796F" }
style.syntax["string"]   = { common.color "#73C686" }
style.syntax["operator"] = { common.color "#829D91" }
style.syntax["function"] = { common.color "#EBC342" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
