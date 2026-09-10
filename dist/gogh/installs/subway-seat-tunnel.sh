#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Subway Seat Tunnel"

export COLOR_01="#3D2C1D"           # Black (Host)
export COLOR_02="#E05C45"           # Red (Syntax string)
export COLOR_03="#ADB956"           # Green (Command)
export COLOR_04="#F3BF45"           # Yellow (Command second)
export COLOR_05="#7F9BAE"           # Blue (Path)
export COLOR_06="#EC7F31"           # Magenta (Syntax var)
export COLOR_07="#86AD95"           # Cyan (Prompt)
export COLOR_08="#D6C3A0"           # White

export COLOR_09="#917759"           # Bright Black
export COLOR_10="#F97160"           # Bright Red (Command error)
export COLOR_11="#BFCB63"           # Bright Green (Exec)
export COLOR_12="#FFD36B"           # Bright Yellow
export COLOR_13="#9DB6C6"           # Bright Blue (Folder)
export COLOR_14="#FF9D55"           # Bright Magenta
export COLOR_15="#A5C9B0"           # Bright Cyan
export COLOR_16="#F6EAD1"           # Bright White

export BACKGROUND_COLOR="#24180E"   # Background
export FOREGROUND_COLOR="#E9D8B6"   # Foreground (Text)

export CURSOR_COLOR="#F3BF45" # Cursor

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
