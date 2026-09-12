-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard — Cast-iron green off a Metro entrance. The original green.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#0E3125" }
style.background2              = { common.color "#0C261C" }
style.background3              = { common.color "#113E2E" }
style.text                     = { common.color "#BBCDC5" }
style.caret                    = { common.color "#EBC342" }
style.accent                   = { common.color "#EBC342" }
style.dim                      = { common.color "#67897A" }
style.divider                  = { common.color "#0A1D15" }
style.selection                = { common.color "#285A47" }
style.line_number              = { common.color "#47705F" }
style.line_number2             = { common.color "#EBC342" }
style.line_highlight           = { common.color "#113E2E" }
style.scrollbar                = { common.color "#285A47" }
style.scrollbar2               = { common.color "#47705F" }
style.scrollbar_track          = { common.color "#0C261C" }
style.nagbar                   = { common.color "#DA6058" }
style.nagbar_text              = { common.color "#0A1D15" }
style.nagbar_dim               = { common.color "rgba(5, 14, 10, 0.45)" }
style.drag_overlay             = { common.color "rgba(211, 226, 219, 0.1)" }
style.drag_overlay_tab         = { common.color "#EBC342" }
style.good                     = { common.color "#73C686" }
style.warn                     = { common.color "#EBC342" }
style.error                    = { common.color "#EF796F" }
style.modified                 = { common.color "#EBC342" }
style.guide                    = { common.color "#113E2E" }
style.guide_highlight          = { common.color "#285A47" }
style.bracketmatch_color       = { common.color "#FBD664" }
style.bracketmatch_char_color  = { common.color "#FBD664" }
style.bracketmatch_block_color = { common.color "#194A39" }
style.bracketmatch_frame_color = { common.color "#285A47" }

style.syntax["normal"]   = { common.color "#D3E2DB" }
style.syntax["symbol"]   = { common.color "#D3E2DB" }
style.syntax["comment"]  = { common.color "#67897A" }
style.syntax["keyword"]  = { common.color "#D78E3C" }
style.syntax["keyword2"] = { common.color "#6FB393" }
style.syntax["number"]   = { common.color "#EF796F" }
style.syntax["literal"]  = { common.color "#EF796F" }
style.syntax["string"]   = { common.color "#73C686" }
style.syntax["operator"] = { common.color "#86A195" }
style.syntax["function"] = { common.color "#EBC342" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
