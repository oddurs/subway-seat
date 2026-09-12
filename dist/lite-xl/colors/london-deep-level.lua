-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Deep Level — Below the cut-and-cover lines. The ground drops; the signals don't.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#121A2D" }
style.background2              = { common.color "#0D1421" }
style.background3              = { common.color "#1A243A" }
style.text                     = { common.color "#BEC6D5" }
style.caret                    = { common.color "#F2C03F" }
style.accent                   = { common.color "#F2C03F" }
style.dim                      = { common.color "#6F7C97" }
style.divider                  = { common.color "#0A0E18" }
style.selection                = { common.color "#303E5B" }
style.line_number              = { common.color "#53617D" }
style.line_number2             = { common.color "#F2C03F" }
style.line_highlight           = { common.color "#1A243A" }
style.scrollbar                = { common.color "#303E5B" }
style.scrollbar2               = { common.color "#53617D" }
style.scrollbar_track          = { common.color "#0D1421" }
style.nagbar                   = { common.color "#DB6052" }
style.nagbar_text              = { common.color "#0A0E18" }
style.nagbar_dim               = { common.color "rgba(5, 7, 12, 0.45)" }
style.drag_overlay             = { common.color "rgba(212, 218, 231, 0.1)" }
style.drag_overlay_tab         = { common.color "#F2C03F" }
style.good                     = { common.color "#77C581" }
style.warn                     = { common.color "#F2C03F" }
style.error                    = { common.color "#F17869" }
style.modified                 = { common.color "#F2C03F" }
style.guide                    = { common.color "#1A243A" }
style.guide_highlight          = { common.color "#303E5B" }
style.bracketmatch_color       = { common.color "#FFD36C" }
style.bracketmatch_char_color  = { common.color "#FFD36C" }
style.bracketmatch_block_color = { common.color "#232F49" }
style.bracketmatch_frame_color = { common.color "#303E5B" }

style.syntax["normal"]   = { common.color "#D4DAE7" }
style.syntax["symbol"]   = { common.color "#D4DAE7" }
style.syntax["comment"]  = { common.color "#6F7C97" }
style.syntax["keyword"]  = { common.color "#DE8946" }
style.syntax["keyword2"] = { common.color "#54B4B5" }
style.syntax["number"]   = { common.color "#F17869" }
style.syntax["literal"]  = { common.color "#F17869" }
style.syntax["string"]   = { common.color "#77C581" }
style.syntax["operator"] = { common.color "#8B96AC" }
style.syntax["function"] = { common.color "#F2C03F" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
