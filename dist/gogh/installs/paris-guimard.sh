#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Guimard"

export COLOR_01="#34453C"           # Black (Host)
export COLOR_02="#CD6B63"           # Red (Syntax string)
export COLOR_03="#80C28E"           # Green (Command)
export COLOR_04="#EBC168"           # Yellow (Command second)
export COLOR_05="#709BC8"           # Blue (Path)
export COLOR_06="#D0914F"           # Magenta (Syntax var)
export COLOR_07="#7BB096"           # Cyan (Prompt)
export COLOR_08="#C3CAC6"           # White

export COLOR_09="#77847D"           # Bright Black
export COLOR_10="#E1837A"           # Bright Red (Command error)
export COLOR_11="#8FD59E"           # Bright Green (Exec)
export COLOR_12="#FBD380"           # Bright Yellow
export COLOR_13="#8DB6E2"           # Bright Blue (Folder)
export COLOR_14="#E7AB6D"           # Bright Magenta
export COLOR_15="#98CCB2"           # Bright Cyan
export COLOR_16="#EAEEEC"           # Bright White

export BACKGROUND_COLOR="#212D27"   # Background
export FOREGROUND_COLOR="#DAE0DC"   # Foreground (Text)

export CURSOR_COLOR="#EBC168" # Cursor

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
