" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#E2EDE8', '#9B5D00', 255, 130, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#E2EDE8', '#00823B', 255, 29, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#E2EDE8', '#856A00', 255, 94, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#E2EDE8', '#C82C2C', 255, 160, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#E2EDE8', '#007752', 255, 29, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#E2EDE8', '#B43586', 255, 126, 'bold'], ['#334A41', '#9DC1B1', 238, 109], ['#405B4F', '#D5E3DD', 240, 253])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#E2EDE8', '#856A00', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#E2EDE8', '#C82C2C', 255, 160]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#5C8171', '#C8DAD1', 66, 188], ['#5C8171', '#C8DAD1', 66, 188], ['#759A8A', '#C8DAD1', 246, 188])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#C82C2C', '', 160, '']}
else
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#0A1D15', '#D78E3C', 234, 172, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#0A1D15', '#73C686', 234, 114, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#0A1D15', '#EBC342', 234, 221, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#0A1D15', '#EF796F', 234, 210, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#0A1D15', '#6FB393', 234, 72, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#0A1D15', '#E783BD', 234, 175, 'bold'], ['#BBCDC5', '#194A39', 251, 23], ['#A2B7AE', '#0C261C', 249, 234])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#0A1D15', '#EBC342', 234, 221]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#0A1D15', '#EF796F', 234, 210]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#67897A', '#0A1D15', 66, 234], ['#67897A', '#0A1D15', 66, 234], ['#47705F', '#0A1D15', 241, 234])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#EF796F', '', 210, '']}
endif
