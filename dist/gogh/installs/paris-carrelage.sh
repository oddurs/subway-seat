#!/usr/bin/env bash
# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.

export PROFILE_NAME="Paris Carrelage"

export COLOR_01="#374940"           # Black (Host)
export COLOR_02="#9E171B"           # Red (Syntax string)
export COLOR_03="#18803F"           # Green (Command)
export COLOR_04="#8A6700"           # Yellow (Command second)
export COLOR_05="#27629C"           # Blue (Path)
export COLOR_06="#9B5D00"           # Magenta (Syntax var)
export COLOR_07="#277555"           # Cyan (Prompt)
export COLOR_08="#8EAD9D"           # White

export COLOR_09="#627F70"           # Bright Black
export COLOR_10="#BB403B"           # Bright Red (Command error)
export COLOR_11="#168540"           # Bright Green (Exec)
export COLOR_12="#997300"           # Bright Yellow
export COLOR_13="#3E75AD"           # Bright Blue (Folder)
export COLOR_14="#AE6800"           # Bright Magenta
export COLOR_15="#3D8666"           # Bright Cyan
export COLOR_16="#A3BFB0"           # Bright White

export BACKGROUND_COLOR="#E4EDE8"   # Background
export FOREGROUND_COLOR="#25352C"   # Foreground (Text)

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
