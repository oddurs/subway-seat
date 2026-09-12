-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- London Portland — Holden's Portland stone. Links are the exact Corporate Blue.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#E5EAF6" }
style.background2              = { common.color "#D9E0EC" }
style.background3              = { common.color "#F2F4FA" }
style.text                     = { common.color "#434548" }
style.caret                    = { common.color "#9F591B" }
style.accent                   = { common.color "#9F591B" }
style.dim                      = { common.color "#727781" }
style.divider                  = { common.color "#CED5E3" }
style.selection                = { common.color "#ADB7CB" }
style.line_number              = { common.color "#8A919F" }
style.line_number2             = { common.color "#9F591B" }
style.line_highlight           = { common.color "#D9E0EC" }
style.scrollbar                = { common.color "#9BA5B8" }
style.scrollbar2               = { common.color "#8A919F" }
style.scrollbar_track          = { common.color "#D9E0EC" }
style.nagbar                   = { common.color "#A40005" }
style.nagbar_text              = { common.color "#E5EAF6" }
style.nagbar_dim               = { common.color "rgba(47, 48, 51, 0.45)" }
style.drag_overlay             = { common.color "rgba(47, 48, 51, 0.1)" }
style.drag_overlay_tab         = { common.color "#9F591B" }
style.good                     = { common.color "#357D41" }
style.warn                     = { common.color "#896800" }
style.error                    = { common.color "#CA2822" }
style.modified                 = { common.color "#896800" }
style.guide                    = { common.color "#C1CADC" }
style.guide_highlight          = { common.color "#9BA5B8" }
style.bracketmatch_color       = { common.color "#9F591B" }
style.bracketmatch_char_color  = { common.color "#9F591B" }
style.bracketmatch_block_color = { common.color "#D8DDE8" }
style.bracketmatch_frame_color = { common.color "#9BA5B8" }

style.syntax["normal"]   = { common.color "#2F3033" }
style.syntax["symbol"]   = { common.color "#2F3033" }
style.syntax["comment"]  = { common.color "#727781" }
style.syntax["keyword"]  = { common.color "#9F591B" }
style.syntax["keyword2"] = { common.color "#007376" }
style.syntax["number"]   = { common.color "#CA2822" }
style.syntax["literal"]  = { common.color "#CA2822" }
style.syntax["string"]   = { common.color "#357D41" }
style.syntax["operator"] = { common.color "#5D6168" }
style.syntax["function"] = { common.color "#896800" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
