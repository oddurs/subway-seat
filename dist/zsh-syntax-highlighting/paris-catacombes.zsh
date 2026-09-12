# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#D5DCD8'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#E1837A'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#738079,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#D0914F'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[function]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[command]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#EBC168,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#EBC168,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#EBC168'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#D0914F'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#CE96B4'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#7BB096'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#7BB096'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#D5DCD8'
ZSH_HIGHLIGHT_STYLES[path]='fg=#C0C7C3,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#8E9993,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#C0C7C3,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#8E9993,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#E1837A'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#80C28E'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#E1837A'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#80C28E'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#E1837A'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#80C28E'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#E1837A'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#CE96B4'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#80C28E'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#CE96B4'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#E1837A'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#CE96B4'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#E1837A,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#EBC168'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#D0914F'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#80C28E'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#7BB096'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#FBD380,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#0B100D,bg=#EBC168'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#738079'
