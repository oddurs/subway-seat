-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland — Holden's Portland stone. Links are the exact Corporate Blue.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E0EAFE" }
style.background2              = { common.color "#D4E0F6" }
style.background3              = { common.color "#F0F4FE" }
style.text                     = { common.color "#3C4557" }
style.caret                    = { common.color "#B14A07" }
style.accent                   = { common.color "#B14A07" }
style.dim                      = { common.color "#697794" }
style.divider                  = { common.color "#C5D5F3" }
style.selection                = { common.color "#A1B7E5" }
style.line_number              = { common.color "#7F91B4" }
style.line_number2             = { common.color "#B14A07" }
style.line_highlight           = { common.color "#D4E0F6" }
style.scrollbar                = { common.color "#8FA5D0" }
style.scrollbar2               = { common.color "#7F91B4" }
style.scrollbar_track          = { common.color "#D4E0F6" }
style.nagbar                   = { common.color "#9B211A" }
style.nagbar_text              = { common.color "#E0EAFE" }
style.nagbar_dim               = { common.color "rgba(41, 48, 64, 0.45)" }
style.drag_overlay             = { common.color "rgba(41, 48, 64, 0.1)" }
style.drag_overlay_tab         = { common.color "#B14A07" }
style.good                     = { common.color "#0D8131" }
style.warn                     = { common.color "#896800" }
style.error                    = { common.color "#C92B23" }
style.modified                 = { common.color "#896800" }
style.guide                    = { common.color "#B6CAF3" }
style.guide_highlight          = { common.color "#8FA5D0" }
style.bracketmatch_color       = { common.color "#B14A07" }
style.bracketmatch_char_color  = { common.color "#B14A07" }
style.bracketmatch_block_color = { common.color "#D3DDF1" }
style.bracketmatch_frame_color = { common.color "#8FA5D0" }

style.syntax["normal"]   = { common.color "#293040" }
style.syntax["symbol"]   = { common.color "#293040" }
style.syntax["comment"]  = { common.color "#697794" }
style.syntax["keyword"]  = { common.color "#B14A07" }
style.syntax["keyword2"] = { common.color "#007376" }
style.syntax["number"]   = { common.color "#C92B23" }
style.syntax["literal"]  = { common.color "#C92B23" }
style.syntax["string"]   = { common.color "#0D8131" }
style.syntax["operator"] = { common.color "#556179" }
style.syntax["function"] = { common.color "#896800" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
