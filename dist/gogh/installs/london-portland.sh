#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="London Portland"

export COLOR_01="#434548"           # Black (Host)
export COLOR_02="#A40005"           # Red (Syntax string)
export COLOR_03="#357D41"           # Green (Command)
export COLOR_04="#896800"           # Yellow (Command second)
export COLOR_05="#0019A8"           # Blue (Path)
export COLOR_06="#9F591B"           # Magenta (Syntax var)
export COLOR_07="#007376"           # Cyan (Prompt)
export COLOR_08="#9BA5B8"           # White

export COLOR_09="#727781"           # Bright Black
export COLOR_10="#CA2822"           # Bright Red (Command error)
export COLOR_11="#398145"           # Bright Green (Exec)
export COLOR_12="#977300"           # Bright Yellow
export COLOR_13="#406BD0"           # Bright Blue (Folder)
export COLOR_14="#AE672B"           # Bright Magenta
export COLOR_15="#008689"           # Bright Cyan
export COLOR_16="#ADB7CB"           # Bright White

export BACKGROUND_COLOR="#E5EAF6"   # Background
export FOREGROUND_COLOR="#2F3033"   # Foreground (Text)

export CURSOR_COLOR="#9F591B" # Cursor

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
