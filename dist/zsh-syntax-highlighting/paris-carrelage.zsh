# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for zsh-syntax-highlighting. Needs a truecolor terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES

# General
ZSH_HIGHLIGHT_STYLES[default]='fg=#21352D'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#C82C2C'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#5C8171,italic'

# Commands
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#9B5D00'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[function]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[command]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#856A00,italic'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#856A00,italic'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#856A00'

# Separators and redirection
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#9B5D00'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#B43586'

# Arguments and options
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#007752'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#007752'
ZSH_HIGHLIGHT_STYLES[assign]='fg=#21352D'
ZSH_HIGHLIGHT_STYLES[path]='fg=#334A41,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#4A695C,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#334A41,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#4A695C,underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#C82C2C'

# Strings
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#00823B'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#C82C2C'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#00823B'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#C82C2C'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#00823B'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#C82C2C'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#B43586'

# Substitutions
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#00823B'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#B43586'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#C82C2C'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#B43586'

# brackets and cursor highlighters (only used if enabled in ZSH_HIGHLIGHT_HIGHLIGHTERS)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#C82C2C,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#856A00'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#9B5D00'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#00823B'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#007752'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#937500,bold'
ZSH_HIGHLIGHT_STYLES[cursor]='fg=#E2EDE8,bg=#9B5D00'

# zsh-autosuggestions (fish's autosuggestion color)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#5C8171'
