#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Carrelage"

export COLOR_01="#3B4742"           # Black (Host)
export COLOR_02="#88251E"           # Red (Syntax string)
export COLOR_03="#218366"           # Green (Command)
export COLOR_04="#916D07"           # Yellow (Command second)
export COLOR_05="#25629B"           # Blue (Path)
export COLOR_06="#764C00"           # Magenta (Syntax var)
export COLOR_07="#006267"           # Cyan (Prompt)
export COLOR_08="#99ABA6"           # White

export COLOR_09="#6C7C76"           # Bright Black
export COLOR_10="#AC3B32"           # Bright Red (Command error)
export COLOR_11="#278D6E"           # Bright Green (Exec)
export COLOR_12="#A07A12"           # Bright Yellow
export COLOR_13="#3D75AD"           # Bright Blue (Folder)
export COLOR_14="#885A00"           # Bright Magenta
export COLOR_15="#027479"           # Bright Cyan
export COLOR_16="#B0BFBB"           # Bright White

export BACKGROUND_COLOR="#EEF2F1"   # Background
export FOREGROUND_COLOR="#27342F"   # Foreground (Text)

export CURSOR_COLOR="#764C00" # Cursor

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
