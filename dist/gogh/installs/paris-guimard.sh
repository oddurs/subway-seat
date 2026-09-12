#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Guimard"

export COLOR_01="#194A39"           # Black (Host)
export COLOR_02="#DA6058"           # Red (Syntax string)
export COLOR_03="#73C686"           # Green (Command)
export COLOR_04="#EBC342"           # Yellow (Command second)
export COLOR_05="#639BD5"           # Blue (Path)
export COLOR_06="#D78E3C"           # Magenta (Syntax var)
export COLOR_07="#6FB393"           # Cyan (Prompt)
export COLOR_08="#BBCDC5"           # White

export COLOR_09="#67897A"           # Bright Black
export COLOR_10="#EF796F"           # Bright Red (Command error)
export COLOR_11="#82D896"           # Bright Green (Exec)
export COLOR_12="#FBD664"           # Bright Yellow
export COLOR_13="#82B7EE"           # Bright Blue (Folder)
export COLOR_14="#EEA85C"           # Bright Magenta
export COLOR_15="#8ECFAF"           # Bright Cyan
export COLOR_16="#E6F0EB"           # Bright White

export BACKGROUND_COLOR="#0E3125"   # Background
export FOREGROUND_COLOR="#D3E2DB"   # Foreground (Text)

export CURSOR_COLOR="#EBC342" # Cursor

apply_theme() {
    if [[ -e "${GOGH_APPLY_SCRIPT}" ]]; then
      bash "${GOGH_APPLY_SCRIPT}"
    elif [[ -e "${PARENT_PATH}/apply-colors.sh" ]]; then
      bash "${PARENT_PATH}/apply-colors.sh"
    elif [[ -e "${SCRIPT_PATH}/apply-colors.sh" ]]; then
      bash "${SCRIPT_PATH}/apply-colors.sh"
    else
      printf '\n%s\n' "Error: Couldn't find apply-colors.sh" 1>&2
      exit 1
    fi
}

# | ===========================================================================
# | Apply Colors
# | ===========================================================================
SCRIPT_PATH="${SCRIPT_PATH:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
PARENT_PATH="$(dirname "${SCRIPT_PATH}")"

if [ -z "${GOGH_NONINTERACTIVE+no}" ]; then
    apply_theme
else
    apply_theme 1>/dev/null
fi
