# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#27342F'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#AC3B32'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#6C7C76,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#764C00'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[function]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[command]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#916D07,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#916D07,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#916D07'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#764C00'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#B36B51'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#006267'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#006267'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#27342F'
ZSH_HIGHLIGHT_STYLES[path]='fg=#3B4742,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#56645F,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#3B4742,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#56645F,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#AC3B32'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#218366'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#AC3B32'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#218366'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#AC3B32'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#218366'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#AC3B32'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#B36B51'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#218366'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#B36B51'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#AC3B32'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#B36B51'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#AC3B32,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#916D07'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#764C00'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#218366'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#006267'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#A07A12,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#EEF2F1,bg=#764C00'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#6C7C76'
