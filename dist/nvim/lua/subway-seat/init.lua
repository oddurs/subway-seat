-- Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
-- Subway Seat for Neovim. `:colorscheme subway-seat` follows 'background';
-- `subway-seat-walnut`, `-tunnel` and `-enamel` pick one flavor. See :help subway-seat.
local M = {}

M.flavors = { "walnut", "tunnel", "enamel", "moquette", "deep", "portland", "guimard", "catacombes", "carrelage" }

-- Every flavor's file stem, and which of them are light. Both come from
-- palette.py, so a new family needs no change here.
M.prefix = { walnut = "subway-seat", tunnel = "subway-seat", enamel = "subway-seat", moquette = "london", deep = "london", portland = "london", guimard = "paris", catacombes = "paris", carrelage = "paris" }
M.light = { enamel = true, portland = true, carrelage = true }

M.config = {
  -- The flavor `:colorscheme subway-seat` shows for each 'background'.
  background = { dark = "walnut", light = "enamel" },
  -- Leave the editor and gutter backgrounds unset so the terminal shows through.
  transparent = false,
  -- Set false to drop every italic (comments, parameters, builtins …).
  italics = true,
  -- function(colors, flavor) return { GroupName = { fg = colors.orange } } end
  overrides = nil,
  -- Before 0.3: a fixed flavor for `:colorscheme subway-seat` ("auto" follows 'background').
  flavor = "auto",
}

--- The flavor on screen ("walnut", "tunnel" or "enamel"), or nil before the first load.
M.current = nil

local default = { dark = "walnut", light = "enamel" }
local shown = {} -- 'background' → the flavor last shown with it
local transparent = {
  "Normal", "NormalNC", "SignColumn", "FoldColumn", "EndOfBuffer", "LineNr", "CursorLineNr",
  "StatusLine", "StatusLineNC", "TabLineFill", "WinBar", "WinBarNC",
  "NeoTreeNormal", "NeoTreeNormalNC", "NvimTreeNormal", "NvimTreeNormalNC", "TroubleNormal", "TroubleNormalNC",
}

function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", M.config, opts or {})
end

--- The palette for a flavor (default: the one on screen), as role → "#RRGGBB".
function M.colors(flavor)
  return require("subway-seat.palette")[flavor or M.current or default[vim.o.background] or "walnut"]
end

local function is_light(flavor)
  return M.light[flavor] == true
end

-- A flavor's groups live in its colors file, which returns them when called with "subway-seat".
local function read(flavor)
  local file = "colors/subway-seat-" .. flavor .. ".lua"
  local path = vim.api.nvim_get_runtime_file(file, false)[1]
  if not path then
    error("subway-seat: " .. file .. " isn't on 'runtimepath'")
  end
  return assert(loadfile(path))("subway-seat")
end

local function apply(flavor, name, set_background)
  local spec = read(flavor)
  if set_background and vim.o.background ~= spec.background then
    -- Drop the name first, so Neovim doesn't re-run the previous colorscheme for the new 'background'.
    vim.g.colors_name = nil
    vim.o.background = spec.background
  end

  local groups = vim.deepcopy(spec.groups)
  if M.config.transparent then
    for _, group in ipairs(transparent) do
      if groups[group] then groups[group].bg = nil end
    end
  end
  if not M.config.italics then
    for _, hl in pairs(groups) do hl.italic = nil end
  end
  if type(M.config.overrides) == "function" then
    for group, hl in pairs(M.config.overrides(M.colors(flavor), flavor) or {}) do
      groups[group] = hl
    end
  end

  vim.cmd("hi clear")
  if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
  vim.o.termguicolors = true
  vim.g.colors_name = name
  for group, hl in pairs(groups) do
    vim.api.nvim_set_hl(0, group, hl)
  end
  for i, color in ipairs(spec.ansi) do
    vim.g["terminal_color_" .. (i - 1)] = color
  end
  M.current = flavor
  shown[vim.o.background] = flavor
end

local function follow(bg)
  return M.config.background[bg] or default[bg]
end

--- Entry point of the colors/ files. Neovim re-runs the current one when 'background'
--- changes; then the flavor follows 'background' instead of setting it back.
function M.colorscheme(name)
  local bg = vim.o.background
  local reloading = vim.g.colors_name == name and M.current ~= nil
  local flavor = name:match("^subway%-seat%-(%a+)$")
  if not flavor then -- "subway-seat"
    local fixed = M.config.flavor ~= "auto" and M.config.flavor or nil
    if fixed and (is_light(fixed) == (bg == "light") or not reloading) then
      return apply(fixed, name, true)
    end
    return apply(follow(bg), name, false)
  end
  if reloading and is_light(flavor) ~= (bg == "light") then
    local to = shown[bg] or follow(bg)
    return apply(to, "subway-seat-" .. to, false)
  end
  apply(flavor, name, true)
end

--- Load a flavor ("walnut", "tunnel", "enamel"), or follow 'background' when nil.
function M.load(flavor)
  M.colorscheme((flavor == nil or flavor == "auto") and "subway-seat" or ("subway-seat-" .. flavor))
end

return M
