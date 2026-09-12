# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#CFDED7'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#EF796F'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#648576,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#D78E3C'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[function]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[command]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#EBC342,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#EBC342,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#EBC342'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#D78E3C'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#E783BD'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#6FB393'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#6FB393'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#CFDED7'
ZSH_HIGHLIGHT_STYLES[path]='fg=#B8CAC2,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#829D91,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#B8CAC2,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#829D91,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#EF796F'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#73C686'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#EF796F'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#73C686'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#EF796F'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#73C686'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#EF796F'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#E783BD'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#73C686'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#E783BD'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#EF796F'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#E783BD'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#EF796F,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#EBC342'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#D78E3C'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#73C686'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#6FB393'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#FBD664,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#05120C,bg=#EBC342'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#648576'
