-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage — Bevelled white tile under a vaulted platform. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E7F5ED" }
style.background2              = { common.color "#D8EADF" }
style.background3              = { common.color "#F3FAF6" }
style.text                     = { common.color "#374940" }
style.caret                    = { common.color "#754500" }
style.accent                   = { common.color "#754500" }
style.dim                      = { common.color "#627F70" }
style.divider                  = { common.color "#C8E0D3" }
style.selection                = { common.color "#9FC6B1" }
style.line_number              = { common.color "#789C88" }
style.line_number2             = { common.color "#754500" }
style.line_highlight           = { common.color "#D8EADF" }
style.scrollbar                = { common.color "#89B19D" }
style.scrollbar2               = { common.color "#789C88" }
style.scrollbar_track          = { common.color "#D8EADF" }
style.nagbar                   = { common.color "#932D29" }
style.nagbar_text              = { common.color "#E7F5ED" }
style.nagbar_dim               = { common.color "rgba(37, 53, 44, 0.45)" }
style.drag_overlay             = { common.color "rgba(37, 53, 44, 0.1)" }
style.drag_overlay_tab         = { common.color "#754500" }
style.good                     = { common.color "#207F41" }
style.warn                     = { common.color "#8A6700" }
style.error                    = { common.color "#BB403B" }
style.modified                 = { common.color "#8A6700" }
style.guide                    = { common.color "#B7D8C6" }
style.guide_highlight          = { common.color "#89B19D" }
style.bracketmatch_color       = { common.color "#754500" }
style.bracketmatch_char_color  = { common.color "#754500" }
style.bracketmatch_block_color = { common.color "#D9E7DF" }
style.bracketmatch_frame_color = { common.color "#89B19D" }

style.syntax["normal"]   = { common.color "#25352C" }
style.syntax["symbol"]   = { common.color "#25352C" }
style.syntax["comment"]  = { common.color "#627F70" }
style.syntax["keyword"]  = { common.color "#754500" }
style.syntax["keyword2"] = { common.color "#086142" }
style.syntax["number"]   = { common.color "#BB403B" }
style.syntax["literal"]  = { common.color "#BB403B" }
style.syntax["string"]   = { common.color "#207F41" }
style.syntax["operator"] = { common.color "#4F675B" }
style.syntax["function"] = { common.color "#8A6700" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
