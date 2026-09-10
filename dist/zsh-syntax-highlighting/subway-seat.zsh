# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#EDDCBC'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#EC6A50'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#967B5C,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#EC7F31'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[function]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[command]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#F3BF45,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#F3BF45,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#F3BF45'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#EC7F31'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#E0956C'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#86AD95'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#86AD95'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#EDDCBC'
ZSH_HIGHLIGHT_STYLES[path]='fg=#D9C6A3,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#AE9575,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#D9C6A3,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#AE9575,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#EC6A50'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#A3AE4B'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#EC6A50'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#A3AE4B'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#EC6A50'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#A3AE4B'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#EC6A50'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#E0956C'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#A3AE4B'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#E0956C'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#EC6A50'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#E0956C'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#EC6A50,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#F3BF45'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#EC7F31'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#A3AE4B'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#86AD95'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#FFD36B,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#20160E,bg=#F3BF45'
