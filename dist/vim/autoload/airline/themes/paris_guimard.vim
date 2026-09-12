" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#E7F5ED', '#754500', 255, 94, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#E7F5ED', '#207F41', 255, 29, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#E7F5ED', '#8A6700', 255, 94, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#E7F5ED', '#BB403B', 255, 131, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#E7F5ED', '#086142', 255, 23, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#E7F5ED', '#9A557D', 255, 132, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#627F70', '#C8E0D3', 66, 253], ['#627F70', '#C8E0D3', 66, 253], ['#789C88', '#C8E0D3', 108, 253])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#BB403B', '', 131, '']}
else
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#131A17', '#D0914F', 234, 173, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#131A17', '#80C28E', 234, 108, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#131A17', '#F2BF4B', 234, 214, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#131A17', '#E1837A', 234, 174, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#131A17', '#6CA087', 234, 72, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#131A17', '#CE96B4', 234, 175, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#131A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#74857C', '#131A17', 244, 234], ['#74857C', '#131A17', 244, 234], ['#586B61', '#131A17', 241, 234])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#E1837A', '', 174, '']}
endif
