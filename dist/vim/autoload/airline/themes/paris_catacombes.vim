" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_catacombes'

if &background ==# 'light'
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#E2EDE8', '#9B5D00', 255, 130, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#E2EDE8', '#00823B', 255, 29, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#E2EDE8', '#856A00', 255, 94, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#E2EDE8', '#C82C2C', 255, 160, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#E2EDE8', '#007752', 255, 29, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#E2EDE8', '#B43586', 255, 126, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#5C8171', '#C8DAD1', 66, 188], ['#5C8171', '#C8DAD1', 66, 188], ['#759A8A', '#C8DAD1', 246, 188])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#C82C2C', '', 160, '']}
else
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#05120C', '#D78E3C', 233, 172, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#05120C', '#73C686', 233, 114, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#05120C', '#EBC342', 233, 221, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#05120C', '#EF796F', 233, 210, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#05120C', '#6FB393', 233, 72, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#05120C', '#E783BD', 233, 175, 'bold'], ['#B8CAC2', '#13382A', 251, 236], ['#9EB3AA', '#061811', 145, 233])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#05120C', '#EBC342', 233, 221]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#05120C', '#EF796F', 233, 210]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#648576', '#05120C', 66, 233], ['#648576', '#05120C', 66, 233], ['#456A5B', '#05120C', 241, 233])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#EF796F', '', 210, '']}
endif
