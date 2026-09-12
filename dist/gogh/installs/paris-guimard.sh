#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Guimard"

export COLOR_01="#30463B"           # Black (Host)
export COLOR_02="#C7665B"           # Red (Syntax string)
export COLOR_03="#70CAA9"           # Green (Command)
export COLOR_04="#F1BF4B"           # Yellow (Command second)
export COLOR_05="#709BC8"           # Blue (Path)
export COLOR_06="#CA9245"           # Magenta (Syntax var)
export COLOR_07="#549B9F"           # Cyan (Prompt)
export COLOR_08="#C2CBC5"           # White

export COLOR_09="#74857C"           # Bright Black
export COLOR_10="#E7877B"           # Bright Red (Command error)
export COLOR_11="#89DEBE"           # Bright Green (Exec)
export COLOR_12="#FFD57A"           # Bright Yellow
export COLOR_13="#8DB6E2"           # Bright Blue (Folder)
export COLOR_14="#DFAA61"           # Bright Magenta
export COLOR_15="#70B5B9"           # Bright Cyan
export COLOR_16="#E9EEEC"           # Bright White

export BACKGROUND_COLOR="#1E2E26"   # Background
export FOREGROUND_COLOR="#D9E1DB"   # Foreground (Text)

export CURSOR_COLOR="#F1BF4B" # Cursor

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
