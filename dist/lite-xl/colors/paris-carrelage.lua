-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage — Bevelled white tile under a vaulted platform. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E2EDE8" }
style.background2              = { common.color "#D5E3DD" }
style.background3              = { common.color "#F0F6F4" }
style.text                     = { common.color "#334A41" }
style.caret                    = { common.color "#9B5D00" }
style.accent                   = { common.color "#9B5D00" }
style.dim                      = { common.color "#5C8171" }
style.divider                  = { common.color "#C8DAD1" }
style.selection                = { common.color "#9DC1B1" }
style.line_number              = { common.color "#759A8A" }
style.line_number2             = { common.color "#9B5D00" }
style.line_highlight           = { common.color "#D5E3DD" }
style.scrollbar                = { common.color "#88AF9E" }
style.scrollbar2               = { common.color "#759A8A" }
style.scrollbar_track          = { common.color "#D5E3DD" }
style.nagbar                   = { common.color "#A30013" }
style.nagbar_text              = { common.color "#E2EDE8" }
style.nagbar_dim               = { common.color "rgba(33, 53, 45, 0.45)" }
style.drag_overlay             = { common.color "rgba(33, 53, 45, 0.1)" }
style.drag_overlay_tab         = { common.color "#9B5D00" }
style.good                     = { common.color "#00823B" }
style.warn                     = { common.color "#856A00" }
style.error                    = { common.color "#C82C2C" }
style.modified                 = { common.color "#856A00" }
style.guide                    = { common.color "#B6D2C5" }
style.guide_highlight          = { common.color "#88AF9E" }
style.bracketmatch_color       = { common.color "#9B5D00" }
style.bracketmatch_char_color  = { common.color "#9B5D00" }
style.bracketmatch_block_color = { common.color "#D4E0DB" }
style.bracketmatch_frame_color = { common.color "#88AF9E" }

style.syntax["normal"]   = { common.color "#21352D" }
style.syntax["symbol"]   = { common.color "#21352D" }
style.syntax["comment"]  = { common.color "#5C8171" }
style.syntax["keyword"]  = { common.color "#9B5D00" }
style.syntax["keyword2"] = { common.color "#007752" }
style.syntax["number"]   = { common.color "#C82C2C" }
style.syntax["literal"]  = { common.color "#C82C2C" }
style.syntax["string"]   = { common.color "#00823B" }
style.syntax["operator"] = { common.color "#4A695C" }
style.syntax["function"] = { common.color "#856A00" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
