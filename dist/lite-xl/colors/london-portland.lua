-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland — Holden's Portland stone. Links are the exact Corporate Blue.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E5EAF4" }
style.background2              = { common.color "#DAE0EB" }
style.background3              = { common.color "#F2F4FA" }
style.text                     = { common.color "#3C4557" }
style.caret                    = { common.color "#A45600" }
style.accent                   = { common.color "#A45600" }
style.dim                      = { common.color "#697794" }
style.divider                  = { common.color "#CDD5E4" }
style.selection                = { common.color "#A9B7D4" }
style.line_number              = { common.color "#8291AE" }
style.line_number2             = { common.color "#A45600" }
style.line_highlight           = { common.color "#DAE0EB" }
style.scrollbar                = { common.color "#95A5C4" }
style.scrollbar2               = { common.color "#8291AE" }
style.scrollbar_track          = { common.color "#DAE0EB" }
style.nagbar                   = { common.color "#A40005" }
style.nagbar_text              = { common.color "#E5EAF4" }
style.nagbar_dim               = { common.color "rgba(41, 48, 64, 0.45)" }
style.drag_overlay             = { common.color "rgba(41, 48, 64, 0.1)" }
style.drag_overlay_tab         = { common.color "#A45600" }
style.good                     = { common.color "#00822E" }
style.warn                     = { common.color "#896800" }
style.error                    = { common.color "#C92B23" }
style.modified                 = { common.color "#896800" }
style.guide                    = { common.color "#BFCAE1" }
style.guide_highlight          = { common.color "#95A5C4" }
style.bracketmatch_color       = { common.color "#A45600" }
style.bracketmatch_char_color  = { common.color "#A45600" }
style.bracketmatch_block_color = { common.color "#D8DDE7" }
style.bracketmatch_frame_color = { common.color "#95A5C4" }

style.syntax["normal"]   = { common.color "#293040" }
style.syntax["symbol"]   = { common.color "#293040" }
style.syntax["comment"]  = { common.color "#697794" }
style.syntax["keyword"]  = { common.color "#A45600" }
style.syntax["keyword2"] = { common.color "#007376" }
style.syntax["number"]   = { common.color "#C92B23" }
style.syntax["literal"]  = { common.color "#C92B23" }
style.syntax["string"]   = { common.color "#00822E" }
style.syntax["operator"] = { common.color "#556179" }
style.syntax["function"] = { common.color "#896800" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
