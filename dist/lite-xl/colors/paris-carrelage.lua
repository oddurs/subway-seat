-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage — Bevelled white tile under a vaulted platform. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#EEF3ED" }
style.background2              = { common.color "#E1E7E0" }
style.background3              = { common.color "#F6F9F6" }
style.text                     = { common.color "#3D473E" }
style.caret                    = { common.color "#804B00" }
style.accent                   = { common.color "#804B00" }
style.dim                      = { common.color "#6E7C6E" }
style.divider                  = { common.color "#D4DCD3" }
style.selection                = { common.color "#B1C0B0" }
style.line_number              = { common.color "#879887" }
style.line_number2             = { common.color "#804B00" }
style.line_highlight           = { common.color "#E1E7E0" }
style.scrollbar                = { common.color "#9BAC9A" }
style.scrollbar2               = { common.color "#879887" }
style.scrollbar_track          = { common.color "#E1E7E0" }
style.nagbar                   = { common.color "#932D29" }
style.nagbar_text              = { common.color "#EEF3ED" }
style.nagbar_dim               = { common.color "rgba(42, 52, 43, 0.45)" }
style.drag_overlay             = { common.color "rgba(42, 52, 43, 0.1)" }
style.drag_overlay_tab         = { common.color "#804B00" }
style.good                     = { common.color "#207F41" }
style.warn                     = { common.color "#8E6B08" }
style.error                    = { common.color "#BE423D" }
style.modified                 = { common.color "#8E6B08" }
style.guide                    = { common.color "#C7D3C5" }
style.guide_highlight          = { common.color "#9BAC9A" }
style.bracketmatch_color       = { common.color "#804B00" }
style.bracketmatch_char_color  = { common.color "#804B00" }
style.bracketmatch_block_color = { common.color "#E0E6DF" }
style.bracketmatch_frame_color = { common.color "#9BAC9A" }

style.syntax["normal"]   = { common.color "#2A342B" }
style.syntax["symbol"]   = { common.color "#2A342B" }
style.syntax["comment"]  = { common.color "#6E7C6E" }
style.syntax["keyword"]  = { common.color "#804B00" }
style.syntax["keyword2"] = { common.color "#006E6B" }
style.syntax["number"]   = { common.color "#BE423D" }
style.syntax["literal"]  = { common.color "#BE423D" }
style.syntax["string"]   = { common.color "#207F41" }
style.syntax["operator"] = { common.color "#586459" }
style.syntax["function"] = { common.color "#8E6B08" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
