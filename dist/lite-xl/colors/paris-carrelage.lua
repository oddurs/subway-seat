-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Paris Carrelage — Bevelled white tile under a vaulted platform. The light one.

local style = require "core.style"
local common = require "core.common"

style.background               = { common.color "#EEF2F1" }
style.background2              = { common.color "#E1E6E5" }
style.background3              = { common.color "#F6F8F8" }
style.text                     = { common.color "#3B4742" }
style.caret                    = { common.color "#764C00" }
style.accent                   = { common.color "#764C00" }
style.dim                      = { common.color "#6C7C76" }
style.divider                  = { common.color "#D5DBDA" }
style.selection                = { common.color "#B0BFBB" }
style.line_number              = { common.color "#859792" }
style.line_number2             = { common.color "#764C00" }
style.line_highlight           = { common.color "#E1E6E5" }
style.scrollbar                = { common.color "#99ABA6" }
style.scrollbar2               = { common.color "#859792" }
style.scrollbar_track          = { common.color "#E1E6E5" }
style.nagbar                   = { common.color "#88251E" }
style.nagbar_text              = { common.color "#EEF2F1" }
style.nagbar_dim               = { common.color "rgba(39, 52, 47, 0.45)" }
style.drag_overlay             = { common.color "rgba(39, 52, 47, 0.1)" }
style.drag_overlay_tab         = { common.color "#764C00" }
style.good                     = { common.color "#218366" }
style.warn                     = { common.color "#916D07" }
style.error                    = { common.color "#AC3B32" }
style.modified                 = { common.color "#916D07" }
style.guide                    = { common.color "#C6D2CF" }
style.guide_highlight          = { common.color "#99ABA6" }
style.bracketmatch_color       = { common.color "#764C00" }
style.bracketmatch_char_color  = { common.color "#764C00" }
style.bracketmatch_block_color = { common.color "#E0E5E3" }
style.bracketmatch_frame_color = { common.color "#99ABA6" }

style.syntax["normal"]   = { common.color "#27342F" }
style.syntax["symbol"]   = { common.color "#27342F" }
style.syntax["comment"]  = { common.color "#6C7C76" }
style.syntax["keyword"]  = { common.color "#764C00" }
style.syntax["keyword2"] = { common.color "#006267" }
style.syntax["number"]   = { common.color "#AC3B32" }
style.syntax["literal"]  = { common.color "#AC3B32" }
style.syntax["string"]   = { common.color "#218366" }
style.syntax["operator"] = { common.color "#56645F" }
style.syntax["function"] = { common.color "#916D07" }

style.log["INFO"]  = { icon = "i", color = style.text }
style.log["WARN"]  = { icon = "!", color = style.warn }
style.log["ERROR"] = { icon = "!", color = style.error }

return style
