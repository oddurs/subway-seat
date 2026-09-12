" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#EEF3ED', '#804B00', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#EEF3ED', '#207F41', 255, 29, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#EEF3ED', '#8E6B08', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#EEF3ED', '#BE423D', 255, 167, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#EEF3ED', '#006E6B', 255, 23, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#EEF3ED', '#98547C', 255, 96, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#6E7C6E', '#D4DCD3', 243, 253], ['#6E7C6E', '#D4DCD3', 243, 253], ['#879887', '#D4DCD3', 246, 253])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#BE423D', '', 167, '']}
else
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#131A17', '#D0914F', 234, 173, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#131A17', '#80C28E', 234, 108, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#131A17', '#F2BF4B', 234, 214, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#131A17', '#EE8F85', 234, 210, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#131A17', '#5FA09D', 234, 73, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#131A17', '#CE96B4', 234, 175, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#131A17', '#F2BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#131A17', '#EE8F85', 234, 210]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#74857C', '#131A17', 244, 234], ['#74857C', '#131A17', 244, 234], ['#586B61', '#131A17', 241, 234])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#EE8F85', '', 210, '']}
endif
