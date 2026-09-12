" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#EEF2F1', '#764C00', 255, 94, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#EEF2F1', '#218366', 255, 29, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#EEF2F1', '#916D07', 255, 94, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#EEF2F1', '#AC3B32', 255, 124, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#EEF2F1', '#006267', 255, 23, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#EEF2F1', '#B36B51', 255, 131, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#6C7C76', '#D5DBDA', 243, 253], ['#6C7C76', '#D5DBDA', 243, 253], ['#859792', '#D5DBDA', 246, 253])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#AC3B32', '', 124, '']}
else
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#131A17', '#CA9245', 234, 172, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#131A17', '#70CAA9', 234, 79, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#131A17', '#F1BF4B', 234, 214, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#131A17', '#E7877B', 234, 174, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#131A17', '#549B9F', 234, 73, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#131A17', '#FAB49C', 234, 216, 'bold'], ['#C2CBC5', '#30463B', 251, 238], ['#A9B5AE', '#18241D', 249, 234])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#131A17', '#F1BF4B', 234, 214]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#131A17', '#E7877B', 234, 174]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#74857C', '#131A17', 244, 234], ['#74857C', '#131A17', 244, 234], ['#586B61', '#131A17', 241, 234])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#E7877B', '', 174, '']}
endif
