#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Carrelage"

export COLOR_01="#334A41"           # Black (Host)
export COLOR_02="#A30013"           # Red (Syntax string)
export COLOR_03="#00823B"           # Green (Command)
export COLOR_04="#856A00"           # Yellow (Command second)
export COLOR_05="#0961A9"           # Blue (Path)
export COLOR_06="#9B5D00"           # Magenta (Syntax var)
export COLOR_07="#007752"           # Cyan (Prompt)
export COLOR_08="#88AF9E"           # White

export COLOR_09="#5C8171"           # Bright Black
export COLOR_10="#C82C2C"           # Bright Red (Command error)
export COLOR_11="#00863D"           # Bright Green (Exec)
export COLOR_12="#937500"           # Bright Yellow
export COLOR_13="#2E75B9"           # Bright Blue (Folder)
export COLOR_14="#AE6800"           # Bright Magenta
export COLOR_15="#2A8862"           # Bright Cyan
export COLOR_16="#9DC1B1"           # Bright White

export BACKGROUND_COLOR="#E2EDE8"   # Background
export FOREGROUND_COLOR="#21352D"   # Foreground (Text)

export CURSOR_COLOR="#9B5D00" # Cursor

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
