# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#25352C'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#BB403B'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#627F70,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#754500'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[function]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[command]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#8A6700,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#8A6700,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#8A6700'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#754500'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#9A557D'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#086142'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#086142'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#25352C'
ZSH_HIGHLIGHT_STYLES[path]='fg=#374940,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#4F675B,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#374940,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#4F675B,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#BB403B'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#BB403B'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#BB403B'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#BB403B'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#9A557D'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#9A557D'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#BB403B'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#9A557D'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#BB403B,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#8A6700'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#754500'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#207F41'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#086142'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#997300,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#DEF0E6,bg=#754500'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#627F70'
