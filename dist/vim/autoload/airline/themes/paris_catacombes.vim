" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_catacombes'

if &background ==# 'light'
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#EEF3ED', '#804B00', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#EEF3ED', '#207F41', 255, 29, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#EEF3ED', '#8E6B08', 255, 94, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#EEF3ED', '#BE423D', 255, 167, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#EEF3ED', '#006E6B', 255, 23, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#EEF3ED', '#98547C', 255, 96, 'bold'], ['#3D473E', '#B1C0B0', 238, 250], ['#4C574D', '#E1E7E0', 240, 254])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#EEF3ED', '#8E6B08', 255, 94]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#EEF3ED', '#BE423D', 255, 167]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#6E7C6E', '#D4DCD3', 243, 253], ['#6E7C6E', '#D4DCD3', 243, 253], ['#879887', '#D4DCD3', 246, 253])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#BE423D', '', 167, '']}
else
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#0A100D', '#D0914F', 233, 173, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#0A100D', '#80C28E', 233, 108, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#0A100D', '#F2BF4B', 233, 214, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#0A100D', '#EE8F85', 233, 210, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#0A100D', '#5FA09D', 233, 73, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#0A100D', '#CE96B4', 233, 175, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#0A100D', '#EE8F85', 233, 210]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#708178', '#0A100D', 244, 233], ['#708178', '#0A100D', 244, 233], ['#54655C', '#0A100D', 59, 233])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#EE8F85', '', 210, '']}
endif
