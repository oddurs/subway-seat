# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#293040'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#C92B23'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#697794,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#B14A07'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[function]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[command]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#896800,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#896800,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#896800'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#B14A07'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#7660AB'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#007376'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#007376'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#293040'
ZSH_HIGHLIGHT_STYLES[path]='fg=#3C4557,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#556179,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#3C4557,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#556179,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#C92B23'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#0D8131'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#C92B23'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#0D8131'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#C92B23'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#0D8131'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#C92B23'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#7660AB'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#0D8131'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#7660AB'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#C92B23'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#7660AB'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#C92B23,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#896800'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#B14A07'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#0D8131'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#007376'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#977300,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#E8F0FF,bg=#B14A07'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#697794'
