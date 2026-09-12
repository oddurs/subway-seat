# Subway Seat for Vim

True-color and 256-color definitions in one file, with groups for ALE, coc, vim-lsp, GitGutter, Signify, fugitive, NERDTree, fern and more, plus lightline and airline themes (`let g:lightline = { 'colorscheme': 'subway_seat' }`, `let g:airline_theme = 'subway_seat'`). `colorscheme subway-seat` follows `background`. Install with vim-plug: `Plug 'oddurs/subway-seat', { 'rtp': 'dist/vim' }`, or copy the folders into `~/.vim`.

[Vim](https://www.vim.org) · [Previews and copy buttons](https://oddurs.github.io/subway-seat/ports/vim/)

## Files

| Flavor | File | Where it goes |
|---|---|---|
| All three | [`colors/subway-seat.vim`](colors/subway-seat.vim) | `~/.vim/colors/subway-seat.vim` |
| Subway Seat | [`colors/subway-seat-walnut.vim`](colors/subway-seat-walnut.vim) | `~/.vim/colors/subway-seat-walnut.vim` |
| Subway Seat Tunnel | [`colors/subway-seat-tunnel.vim`](colors/subway-seat-tunnel.vim) | `~/.vim/colors/subway-seat-tunnel.vim` |
| Subway Seat Enamel | [`colors/subway-seat-enamel.vim`](colors/subway-seat-enamel.vim) | `~/.vim/colors/subway-seat-enamel.vim` |
| London Moquette | [`colors/subway-seat-moquette.vim`](colors/subway-seat-moquette.vim) | `~/.vim/colors/subway-seat-moquette.vim` |
| London Deep Level | [`colors/subway-seat-deep.vim`](colors/subway-seat-deep.vim) | `~/.vim/colors/subway-seat-deep.vim` |
| London Portland | [`colors/subway-seat-portland.vim`](colors/subway-seat-portland.vim) | `~/.vim/colors/subway-seat-portland.vim` |
| All three | [`autoload/lightline/colorscheme/subway_seat.vim`](autoload/lightline/colorscheme/subway_seat.vim) | `~/.vim/autoload/lightline/colorscheme/subway_seat.vim` |
| All three | [`autoload/airline/themes/subway_seat.vim`](autoload/airline/themes/subway_seat.vim) | `~/.vim/autoload/airline/themes/subway_seat.vim` |
| Subway Seat Tunnel | [`autoload/lightline/colorscheme/subway_seat_tunnel.vim`](autoload/lightline/colorscheme/subway_seat_tunnel.vim) | `~/.vim/autoload/lightline/colorscheme/subway_seat_tunnel.vim` |
| Subway Seat Tunnel | [`autoload/airline/themes/subway_seat_tunnel.vim`](autoload/airline/themes/subway_seat_tunnel.vim) | `~/.vim/autoload/airline/themes/subway_seat_tunnel.vim` |
| Subway Seat Enamel | [`autoload/lightline/colorscheme/subway_seat_enamel.vim`](autoload/lightline/colorscheme/subway_seat_enamel.vim) | `~/.vim/autoload/lightline/colorscheme/subway_seat_enamel.vim` |
| Subway Seat Enamel | [`autoload/airline/themes/subway_seat_enamel.vim`](autoload/airline/themes/subway_seat_enamel.vim) | `~/.vim/autoload/airline/themes/subway_seat_enamel.vim` |
| London Moquette | [`autoload/lightline/colorscheme/london_moquette.vim`](autoload/lightline/colorscheme/london_moquette.vim) | `~/.vim/autoload/lightline/colorscheme/london_moquette.vim` |
| London Moquette | [`autoload/airline/themes/london_moquette.vim`](autoload/airline/themes/london_moquette.vim) | `~/.vim/autoload/airline/themes/london_moquette.vim` |
| London Deep Level | [`autoload/lightline/colorscheme/london_deep_level.vim`](autoload/lightline/colorscheme/london_deep_level.vim) | `~/.vim/autoload/lightline/colorscheme/london_deep_level.vim` |
| London Deep Level | [`autoload/airline/themes/london_deep_level.vim`](autoload/airline/themes/london_deep_level.vim) | `~/.vim/autoload/airline/themes/london_deep_level.vim` |
| London Portland | [`autoload/lightline/colorscheme/london_portland.vim`](autoload/lightline/colorscheme/london_portland.vim) | `~/.vim/autoload/lightline/colorscheme/london_portland.vim` |
| London Portland | [`autoload/airline/themes/london_portland.vim`](autoload/airline/themes/london_portland.vim) | `~/.vim/autoload/airline/themes/london_portland.vim` |

## Turn it on

**Subway Seat**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-walnut
```

**Subway Seat Tunnel**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-tunnel
```

**Subway Seat Enamel**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-enamel
```

**London Moquette**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-moquette
```

**London Deep Level**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-deep
```

**London Portland**, in ~/.vimrc (or ~/.vim/vimrc; Windows ~/_vimrc):

```vim
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat-portland
```

## Follow light and dark

In ~/.vimrc:

```vim
" subway-seat follows 'background': Walnut when dark, Enamel when light.
" Vim sets 'background' from the terminal's colors when the terminal reports them.
if has('termguicolors') | set termguicolors | endif
colorscheme subway-seat
```

## Uninstall

- Delete `~/.vim/colors/subway-seat.vim`.
- Delete `~/.vim/colors/subway-seat-walnut.vim`.
- Delete `~/.vim/colors/subway-seat-tunnel.vim`.
- Delete `~/.vim/colors/subway-seat-enamel.vim`.
- Delete `~/.vim/colors/subway-seat-moquette.vim`.
- Delete `~/.vim/colors/subway-seat-deep.vim`.
- Delete `~/.vim/colors/subway-seat-portland.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/subway_seat.vim`.
- Delete `~/.vim/autoload/airline/themes/subway_seat.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/subway_seat_tunnel.vim`.
- Delete `~/.vim/autoload/airline/themes/subway_seat_tunnel.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/subway_seat_enamel.vim`.
- Delete `~/.vim/autoload/airline/themes/subway_seat_enamel.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/london_moquette.vim`.
- Delete `~/.vim/autoload/airline/themes/london_moquette.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/london_deep_level.vim`.
- Delete `~/.vim/autoload/airline/themes/london_deep_level.vim`.
- Delete `~/.vim/autoload/lightline/colorscheme/london_portland.vim`.
- Delete `~/.vim/autoload/airline/themes/london_portland.vim`.
- Remove the line you added to turn it on.

Generated by `build.py` from `palette.py` (v0.3.0). Edit the port in `ports/`, not these files.
