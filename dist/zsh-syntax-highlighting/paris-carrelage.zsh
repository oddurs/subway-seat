# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#2A342B'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#BE423D'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#6E7C6E,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#804B00'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[function]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[command]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#8E6B08,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#8E6B08,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#8E6B08'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#804B00'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#98547C'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#006E6B'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#006E6B'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#2A342B'
ZSH_HIGHLIGHT_STYLES[path]='fg=#3D473E,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#586459,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#3D473E,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#586459,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#BE423D'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#BE423D'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#BE423D'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#BE423D'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#98547C'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#98547C'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#BE423D'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#98547C'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#BE423D,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#8E6B08'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#804B00'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#006E6B'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#9D770A,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#EEF3ED,bg=#804B00'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#6E7C6E'
