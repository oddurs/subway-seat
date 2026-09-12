#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="London Deep Level"

export COLOR_01="#232F49"           # Black (Host)
export COLOR_02="#DB6052"           # Red (Syntax string)
export COLOR_03="#77C581"           # Green (Command)
export COLOR_04="#F2C03F"           # Yellow (Command second)
export COLOR_05="#7595DA"           # Blue (Path)
export COLOR_06="#DE8946"           # Magenta (Syntax var)
export COLOR_07="#54B4B5"           # Cyan (Prompt)
export COLOR_08="#BEC6D5"           # White

export COLOR_09="#6F7C97"           # Bright Black
export COLOR_10="#F17869"           # Bright Red (Command error)
export COLOR_11="#9AD2A0"           # Bright Green (Exec)
export COLOR_12="#FFD36C"           # Bright Yellow
export COLOR_13="#8BB0FF"           # Bright Blue (Folder)
export COLOR_14="#E5AA7F"           # Bright Magenta
export COLOR_15="#72D1D3"           # Bright Cyan
export COLOR_16="#E7EBF3"           # Bright White

export BACKGROUND_COLOR="#121A2D"   # Background
export FOREGROUND_COLOR="#D4DAE7"   # Foreground (Text)

export CURSOR_COLOR="#F2C03F" # Cursor

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
