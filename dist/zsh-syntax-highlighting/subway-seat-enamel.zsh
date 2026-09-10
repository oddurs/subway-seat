# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Enamel for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#3E2C1E'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#C44A33'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#8C7254,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#C4561A'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[function]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[command]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#A56E00,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#A56E00,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#A56E00'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#C4561A'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#AE5F3A'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#3E7157'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#3E7157'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#3E2C1E'
ZSH_HIGHLIGHT_STYLES[path]='fg=#54402F,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#735C44,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#54402F,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#735C44,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#C44A33'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#697813'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#C44A33'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#697813'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#C44A33'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#697813'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#C44A33'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#AE5F3A'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#697813'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#AE5F3A'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#C44A33'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#AE5F3A'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#C44A33,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#A56E00'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#C4561A'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#697813'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#3E7157'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#BA8210,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#F4E9D4,bg=#C4561A'
