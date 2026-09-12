-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Guimard — Cast iron off a Metro entrance, which is nearly black. Brass leads.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#212D27" }
style.background2              = { common.color "#1A231E" }
style.background3              = { common.color "#2A3831" }
style.text                     = { common.color "#C3CAC6" }
style.caret                    = { common.color "#EBC168" }
style.accent                   = { common.color "#EBC168" }
style.dim                      = { common.color "#77847D" }
style.divider                  = { common.color "#141A17" }
style.selection                = { common.color "#42544B" }
style.line_number              = { common.color "#5B6A62" }
style.line_number2             = { common.color "#EBC168" }
style.line_highlight           = { common.color "#2A3831" }
style.scrollbar                = { common.color "#42544B" }
style.scrollbar2               = { common.color "#5B6A62" }
style.scrollbar_track          = { common.color "#1A231E" }
style.nagbar                   = { common.color "#CD6B63" }
style.nagbar_text              = { common.color "#141A17" }
style.nagbar_dim               = { common.color "rgba(10, 13, 12, 0.45)" }
style.drag_overlay             = { common.color "rgba(218, 224, 220, 0.1)" }
style.drag_overlay_tab         = { common.color "#EBC168" }
style.good                     = { common.color "#80C28E" }
style.warn                     = { common.color "#EBC168" }
style.error                    = { common.color "#E1837A" }
style.modified                 = { common.color "#EBC168" }
style.guide                    = { common.color "#2A3831" }
style.guide_highlight          = { common.color "#42544B" }
style.bracketmatch_color       = { common.color "#FBD380" }
style.bracketmatch_char_color  = { common.color "#FBD380" }
style.bracketmatch_block_color = { common.color "#34453C" }
style.bracketmatch_frame_color = { common.color "#42544B" }

style.syntax["normal"]   = { common.color "#DAE0DC" }
style.syntax["symbol"]   = { common.color "#DAE0DC" }
style.syntax["comment"]  = { common.color "#77847D" }
style.syntax["keyword"]  = { common.color "#D0914F" }
style.syntax["keyword2"] = { common.color "#7BB096" }
style.syntax["number"]   = { common.color "#E1837A" }
style.syntax["literal"]  = { common.color "#E1837A" }
style.syntax["string"]   = { common.color "#80C28E" }
style.syntax["operator"] = { common.color "#929D97" }
style.syntax["function"] = { common.color "#EBC168" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
