#!/usr/bin/env fish
# Link Subway Seat into the apps you have installed, then print the one line
# each app needs to switch over. Your config files are never edited.
#
#   ./install.fish            # Walnut (the original dark)
#   ./install.fish tunnel     # deeper dark
#   ./install.fish enamel     # light
#
# Files are symlinked from dist/, so after a `git pull` (or ./build.py) the
# installed themes update in place. Re-running is safe.

set -l root (realpath (dirname (status --current-filename)))
set -l dist $root/dist

set -l flavor walnut
set -q argv[1]; and set flavor (string lower -- $argv[1])
switch $flavor
    case walnut
        set -g name "Subway Seat"
        set -g slug subway-seat
    case tunnel
        set -g name "Subway Seat Tunnel"
        set -g slug subway-seat-tunnel
    case enamel
        set -g name "Subway Seat Enamel"
        set -g slug subway-seat-enamel
    case '*'
        echo "Unknown flavor '$flavor'. Pick walnut, tunnel or enamel."
        exit 1
end
set -g snake (string replace -a - _ $slug)
set -g todo

function link -a src dst
    test -e $src; or return 1
    mkdir -p (dirname $dst)
    ln -sfn $src $dst
    echo "  linked  "(string replace $HOME '~' -- $dst)
end

function note -a app where line
    set -a todo "$app — in $where:" "    $line" ""
end

function has
    for tool in $argv
        type -q $tool; and return 0
        test -d "/Applications/$tool.app"; and return 0
    end
    return 1
end

echo "Subway Seat → $name"
echo

# ── Tidy links from the old single-flavor layout ───────────────────────────
for old in ~/.local/share/nvim/site/colors/subway-seat.lua ~/.config/fish/conf.d/subway-seat.fish
    if test -L $old; and string match -q "$dist/*" (readlink $old)
        rm $old
        echo "  removed old link "(string replace $HOME '~' -- $old)
    end
end

# ── Terminals ──────────────────────────────────────────────────────────────
if has ghostty Ghostty
    for f in $dist/ghostty/*
        link $f ~/.config/ghostty/themes/(basename $f)
    end
    note Ghostty "~/.config/ghostty/config" "theme = $name"
end
if has kitty
    for f in $dist/kitty/*.conf
        link $f ~/.config/kitty/themes/(basename $f)
    end
    note kitty "a shell" "kitten themes --reload-in=all $name"
end
if has alacritty Alacritty
    for f in $dist/alacritty/*.toml
        link $f ~/.config/alacritty/themes/(basename $f)
    end
    note Alacritty "~/.config/alacritty/alacritty.toml" "[general] import = [\"~/.config/alacritty/themes/$slug.toml\"]"
end
if has wezterm WezTerm
    for f in $dist/wezterm/*.toml
        link $f ~/.config/wezterm/colors/(basename $f)
    end
    note WezTerm "wezterm.lua" "config.color_scheme = \"$name\""
end
if test -d /Applications/iTerm.app
    note iTerm2 "Settings › Profiles › Colors › Color Presets › Import" (string replace $HOME '~' -- "$dist/iterm2/$name.itermcolors")
end

# ── Shell & prompt ─────────────────────────────────────────────────────────
if has fish
    for f in $dist/fish/themes/*.theme
        link $f ~/.config/fish/themes/(basename $f)
    end
    # A small real file (not a link) so it survives rebuilds.
    mkdir -p ~/.config/fish/conf.d
    printf '%s\n' "# Subway Seat — written by install.fish ($flavor)" \
        'if status is-interactive' \
        "    fish_config theme choose $slug" \
        'end' \
        "test -f $dist/fzf/$slug.fish; and source $dist/fzf/$slug.fish" >~/.config/fish/conf.d/subway-seat.fish
    echo "  wrote   ~/.config/fish/conf.d/subway-seat.fish (fish theme + fzf colours)"
end
if has starship
    note Starship "~/.config/starship.toml (paste the palette block first)" "palette = '$snake'   # palette: $dist/starship/palettes/$slug.toml"
end

# ── CLI & TUI ──────────────────────────────────────────────────────────────
if has bat
    for f in $dist/bat/*.tmTheme
        link $f (bat --config-dir)/themes/(basename $f)
    end
    bat cache --build >/dev/null; and echo "  rebuilt bat cache"
    note bat "your shell config" "set -gx BAT_THEME \"$name\""
end
if has delta
    link $dist/delta/themes.gitconfig ~/.config/delta/subway-seat.gitconfig
    note delta "~/.gitconfig" "[include] path = ~/.config/delta/subway-seat.gitconfig   then   [delta] features = $slug"
end
if has lazygit
    note lazygit "~/.config/lazygit/config.yml" "merge $dist/lazygit/$slug.yml"
end
if has btop
    for f in $dist/btop/*.theme
        link $f ~/.config/btop/themes/(basename $f)
    end
    note btop "~/.config/btop/btop.conf" "color_theme = \"$slug\""
end
if has yazi
    for d in $dist/yazi/*.yazi
        link $d ~/.config/yazi/flavors/(basename $d)
    end
    note yazi "~/.config/yazi/theme.toml" "[flavor] dark = \"$slug\""
end
if has herdr
    note herdr "~/.config/herdr/config.toml, then herdr server reload-config" "append $dist/herdr/$slug.toml and set [theme] name = \"catppuccin\""
end

# ── Editors ────────────────────────────────────────────────────────────────
if has nvim; or test -d ~/.config/nvim
    link $dist/nvim ~/.local/share/nvim/site/pack/subway-seat/start/subway-seat
    note Neovim "init.lua" "vim.cmd.colorscheme(\"$slug\")"
end
if has vim
    for f in $dist/vim/colors/*.vim
        link $f ~/.vim/colors/(basename $f)
    end
    note Vim "~/.vimrc" "colorscheme $slug"
end
if has hx
    for f in $dist/helix/*.toml
        link $f ~/.config/helix/themes/(basename $f)
    end
    note Helix "~/.config/helix/config.toml" "theme = \"$snake\""
end
if has zed Zed
    link $dist/zed/themes/subway-seat.json ~/.config/zed/themes/subway-seat.json
    note Zed "settings.json" "\"theme\": \"$name\""
end
set -l code_cli (command -s code; or echo "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code")
if test -x "$code_cli"
    set -l vsix $dist/vscode/*.vsix
    "$code_cli" --install-extension $vsix[1] --force >/dev/null 2>&1; and echo "  installed the VS Code extension"
    note "VS Code" "settings.json" "\"workbench.colorTheme\": \"$name\""
end

# ── Agents ─────────────────────────────────────────────────────────────────
if has claude
    for f in $dist/claude-code/themes/*.json
        link $f ~/.claude/themes/(basename $f)
    end
    note "Claude Code" "Claude Code (the plugin adds the status line, verbs and tips)" "/theme → $name     or: /plugin marketplace add oddurs/subway-seat"
end
if has opencode
    for f in $dist/opencode/*.json
        link $f ~/.config/opencode/themes/(basename $f)
    end
    note opencode "tui.json" "\"theme\": \"$slug\""
end
if has codex
    for f in $dist/codex/*.tmTheme
        link $f ~/.codex/themes/(basename $f)
    end
    note Codex "~/.codex/config.toml" "[tui] theme = \"$slug\""
end

echo
if test (count $todo) -gt 0
    echo "One line each to switch over:"
    echo
    printf '  %s\n' $todo
end
echo "Everything else (Obsidian, JetBrains, Firefox, Slack, …) has install steps on the site."
