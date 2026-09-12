-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard — Cast iron off a Metro entrance, which is nearly black. Brass leads.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#1E2E26" }
style.background2              = { common.color "#18241D" }
style.background3              = { common.color "#263930" }
style.text                     = { common.color "#C2CBC5" }
style.caret                    = { common.color "#F2BF4B" }
style.accent                   = { common.color "#F2BF4B" }
style.dim                      = { common.color "#74857C" }
style.divider                  = { common.color "#131A17" }
style.selection                = { common.color "#3E554A" }
style.line_number              = { common.color "#586B61" }
style.line_number2             = { common.color "#F2BF4B" }
style.line_highlight           = { common.color "#263930" }
style.scrollbar                = { common.color "#3E554A" }
style.scrollbar2               = { common.color "#586B61" }
style.scrollbar_track          = { common.color "#18241D" }
style.nagbar                   = { common.color "#CD6B63" }
style.nagbar_text              = { common.color "#131A17" }
style.nagbar_dim               = { common.color "rgba(10, 13, 12, 0.45)" }
style.drag_overlay             = { common.color "rgba(217, 225, 219, 0.1)" }
style.drag_overlay_tab         = { common.color "#F2BF4B" }
style.good                     = { common.color "#80C28E" }
style.warn                     = { common.color "#F2BF4B" }
style.error                    = { common.color "#EE8F85" }
style.modified                 = { common.color "#F2BF4B" }
style.guide                    = { common.color "#263930" }
style.guide_highlight          = { common.color "#3E554A" }
style.bracketmatch_color       = { common.color "#FFD273" }
style.bracketmatch_char_color  = { common.color "#FFD273" }
style.bracketmatch_block_color = { common.color "#30463B" }
style.bracketmatch_frame_color = { common.color "#3E554A" }

style.syntax["normal"]   = { common.color "#D9E1DB" }
style.syntax["symbol"]   = { common.color "#D9E1DB" }
style.syntax["comment"]  = { common.color "#74857C" }
style.syntax["keyword"]  = { common.color "#D0914F" }
style.syntax["keyword2"] = { common.color "#5FA09D" }
style.syntax["number"]   = { common.color "#EE8F85" }
style.syntax["literal"]  = { common.color "#EE8F85" }
style.syntax["string"]   = { common.color "#80C28E" }
style.syntax["operator"] = { common.color "#909E96" }
style.syntax["function"] = { common.color "#F2BF4B" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
