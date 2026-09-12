-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland — Holden's Portland stone. Links are the exact Corporate Blue.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E8F0FF" }
style.background2              = { common.color "#DCE5F7" }
style.background3              = { common.color "#F4F8FF" }
style.text                     = { common.color "#3C4557" }
style.caret                    = { common.color "#A54300" }
style.accent                   = { common.color "#A54300" }
style.dim                      = { common.color "#697794" }
style.divider                  = { common.color "#CCDAF2" }
style.selection                = { common.color "#A8BBE2" }
style.line_number              = { common.color "#8192B4" }
style.line_number2             = { common.color "#A54300" }
style.line_highlight           = { common.color "#DCE5F7" }
style.scrollbar                = { common.color "#93A7CF" }
style.scrollbar2               = { common.color "#8192B4" }
style.scrollbar_track          = { common.color "#DCE5F7" }
style.nagbar                   = { common.color "#9B211A" }
style.nagbar_text              = { common.color "#E8F0FF" }
style.nagbar_dim               = { common.color "rgba(41, 48, 64, 0.45)" }
style.drag_overlay             = { common.color "rgba(41, 48, 64, 0.1)" }
style.drag_overlay_tab         = { common.color "#A54300" }
style.good                     = { common.color "#0D8131" }
style.warn                     = { common.color "#8D6C08" }
style.error                    = { common.color "#CC2E25" }
style.modified                 = { common.color "#8D6C08" }
style.guide                    = { common.color "#BFCFF1" }
style.guide_highlight          = { common.color "#93A7CF" }
style.bracketmatch_color       = { common.color "#A54300" }
style.bracketmatch_char_color  = { common.color "#A54300" }
style.bracketmatch_block_color = { common.color "#DBE2F2" }
style.bracketmatch_frame_color = { common.color "#93A7CF" }

style.syntax["normal"]   = { common.color "#293040" }
style.syntax["symbol"]   = { common.color "#293040" }
style.syntax["comment"]  = { common.color "#697794" }
style.syntax["keyword"]  = { common.color "#A54300" }
style.syntax["keyword2"] = { common.color "#007376" }
style.syntax["number"]   = { common.color "#CC2E25" }
style.syntax["literal"]  = { common.color "#CC2E25" }
style.syntax["string"]   = { common.color "#0D8131" }
style.syntax["operator"] = { common.color "#556179" }
style.syntax["function"] = { common.color "#8D6C08" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
