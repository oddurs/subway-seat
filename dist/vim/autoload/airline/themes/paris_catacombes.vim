" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_catacombes'

if &background ==# 'light'
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#EEF2F1', '#764C00', 255, 94, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#EEF2F1', '#218366', 255, 29, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#EEF2F1', '#916D07', 255, 94, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#EEF2F1', '#AC3B32', 255, 124, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#EEF2F1', '#006267', 255, 23, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#EEF2F1', '#B36B51', 255, 131, 'bold'], ['#3B4742', '#B0BFBB', 238, 250], ['#4A5752', '#E1E6E5', 240, 254])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#EEF2F1', '#916D07', 255, 94]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#EEF2F1', '#AC3B32', 255, 124]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#6C7C76', '#D5DBDA', 243, 253], ['#6C7C76', '#D5DBDA', 243, 253], ['#859792', '#D5DBDA', 246, 253])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#AC3B32', '', 124, '']}
else
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#0A100D', '#CA9245', 233, 172, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#0A100D', '#70CAA9', 233, 79, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#0A100D', '#F1BF4B', 233, 214, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#0A100D', '#E7877B', 233, 174, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#0A100D', '#549B9F', 233, 73, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#0A100D', '#FAB49C', 233, 216, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#0A100D', '#F1BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#0A100D', '#E7877B', 233, 174]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#708178', '#0A100D', 244, 233], ['#708178', '#0A100D', 244, 233], ['#54655C', '#0A100D', 59, 233])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#E7877B', '', 174, '']}
endif
