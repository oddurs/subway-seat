#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Subway Seat Enamel"

export COLOR_01="#54402F"           # Black (Host)
export COLOR_02="#992418"           # Red (Syntax string)
export COLOR_03="#66740F"           # Green (Command)
export COLOR_04="#976608"           # Yellow (Command second)
export COLOR_05="#3F6480"           # Blue (Path)
export COLOR_06="#A04800"           # Magenta (Syntax var)
export COLOR_07="#3E7157"           # Cyan (Prompt)
export COLOR_08="#BAA380"           # White

export COLOR_09="#8C7254"           # Bright Black
export COLOR_10="#BF4233"           # Bright Red (Command error)
export COLOR_11="#697813"           # Bright Green (Exec)
export COLOR_12="#A9720A"           # Bright Yellow
export COLOR_13="#517791"           # Bright Blue (Folder)
export COLOR_14="#BA4D0A"           # Bright Magenta
export COLOR_15="#4C8367"           # Bright Cyan
export COLOR_16="#CBB898"           # Bright White

export BACKGROUND_COLOR="#F8EFDF"   # Background
export FOREGROUND_COLOR="#3E2C1E"   # Foreground (Text)

export CURSOR_COLOR="#A04800" # Cursor

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
