-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
local M = {}

M.flavors = { "walnut", "tunnel", "enamel" }

M.config = {
  -- "auto" follows vim.o.background: light → enamel, dark → walnut.
  flavor = "auto",
  -- Leave Normal/NormalNC/SignColumn backgrounds unset so the terminal shows through.
  transparent = false,
  -- Set false to drop every italic (comments, parameters, builtins …).
  italics = true,
  -- function(colors, flavor) return { GroupName = { fg = colors.orange } } end
  overrides = nil,
}

function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", M.config, opts or {})
end

local function resolve(flavor)
  flavor = flavor or M.config.flavor
  if flavor == "auto" then
    return vim.o.background == "light" and "enamel" or "walnut"
  end
  return flavor
end

--- The palette for a flavor, as role → "#RRGGBB".
function M.colors(flavor)
  return require("subway-seat.palette")[resolve(flavor)]
end

function M.load(flavor)
  flavor = resolve(flavor)
  local colors = M.colors(flavor)
  local groups = vim.deepcopy(require("subway-seat.groups." .. flavor))

  if M.config.transparent then
    for _, name in ipairs({ "Normal", "NormalNC", "SignColumn", "FoldColumn", "EndOfBuffer", "StatusLine" }) do
      if groups[name] then groups[name].bg = nil end
    end
  end
  if not M.config.italics then
    for _, spec in pairs(groups) do spec.italic = nil end
  end
  if type(M.config.overrides) == "function" then
    for name, spec in pairs(M.config.overrides(colors, flavor) or {}) do
      groups[name] = spec
    end
  end

  if vim.g.colors_name then vim.cmd("highlight clear") end
  if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
  -- Changing 'background' re-sources the active colorscheme; drop the name first.
  vim.g.colors_name = nil
  local bg = flavor == "enamel" and "light" or "dark"
  if vim.o.background ~= bg then vim.o.background = bg end
  vim.o.termguicolors = true
  vim.g.colors_name = flavor == "walnut" and "subway-seat" or ("subway-seat-" .. flavor)

  for name, spec in pairs(groups) do
    vim.api.nvim_set_hl(0, name, spec)
  end
  for i, c in ipairs(require("subway-seat.palette").ansi[flavor]) do
    vim.g["terminal_color_" .. (i - 1)] = c
  end
end

return M
