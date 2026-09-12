#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="London Portland"

export COLOR_01="#3C4557"           # Black (Host)
export COLOR_02="#9B211A"           # Red (Syntax string)
export COLOR_03="#0D8131"           # Green (Command)
export COLOR_04="#896800"           # Yellow (Command second)
export COLOR_05="#0019A8"           # Blue (Path)
export COLOR_06="#B14A07"           # Magenta (Syntax var)
export COLOR_07="#007376"           # Cyan (Prompt)
export COLOR_08="#95A5C4"           # White

export COLOR_09="#697794"           # Bright Black
export COLOR_10="#C92B23"           # Bright Red (Command error)
export COLOR_11="#008730"           # Bright Green (Exec)
export COLOR_12="#977300"           # Bright Yellow
export COLOR_13="#4A6EBD"           # Bright Blue (Folder)
export COLOR_14="#B86100"           # Bright Magenta
export COLOR_15="#008688"           # Bright Cyan
export COLOR_16="#A9B7D4"           # Bright White

export BACKGROUND_COLOR="#E5EAF4"   # Background
export FOREGROUND_COLOR="#293040"   # Foreground (Text)

export CURSOR_COLOR="#B14A07" # Cursor

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
