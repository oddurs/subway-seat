" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#EEF3ED', '#8A5308', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#EEF3ED', '#207F41', 255, 29, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#EEF3ED', '#8A6700', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#EEF3ED', '#BB403B', 255, 131, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#EEF3ED', '#0B714D', 255, 29, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#EEF3ED', '#9A557D', 255, 132, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#EEF3ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#EEF3ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#6E7C6E', '#D4DCD3', 243, 253], ['#6E7C6E', '#D4DCD3', 243, 253], ['#879887', '#D4DCD3', 246, 253])
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
