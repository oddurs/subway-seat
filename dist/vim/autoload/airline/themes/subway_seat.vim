" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'subway_seat'

if &background ==# 'light'
  let g:airline#themes#subway_seat#palette = {}
  let g:airline#themes#subway_seat#palette.normal = airline#themes#generate_color_map(['#F4E9D4', '#C4561A', 254, 166, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.normal.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.normal.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.insert = airline#themes#generate_color_map(['#F4E9D4', '#697813', 254, 64, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.insert.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.insert.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.visual = airline#themes#generate_color_map(['#F4E9D4', '#A56E00', 254, 130, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.visual.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.visual.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.replace = airline#themes#generate_color_map(['#F4E9D4', '#C44A33', 254, 167, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.replace.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.replace.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.commandline = airline#themes#generate_color_map(['#F4E9D4', '#3E7157', 254, 59, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.commandline.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.commandline.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.terminal = airline#themes#generate_color_map(['#F4E9D4', '#AE5F3A', 254, 131, 'bold'], ['#54402F', '#CAB48E', 238, 180], ['#654F3B', '#EBDEC6', 239, 253])
  let g:airline#themes#subway_seat#palette.terminal.airline_warning = ['#F4E9D4', '#A56E00', 254, 130]
  let g:airline#themes#subway_seat#palette.terminal.airline_error = ['#F4E9D4', '#C44A33', 254, 167]
  let g:airline#themes#subway_seat#palette.inactive = airline#themes#generate_color_map(['#8C7254', '#E2D3B6', 95, 187], ['#8C7254', '#E2D3B6', 95, 187], ['#A58C6A', '#E2D3B6', 137, 187])
  let g:airline#themes#subway_seat#palette.accents = {'red': ['#C44A33', '', 167, '']}
else
  let g:airline#themes#subway_seat#palette = {}
  let g:airline#themes#subway_seat#palette.normal = airline#themes#generate_color_map(['#20160E', '#EC7F31', 233, 209, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.normal.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.normal.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.insert = airline#themes#generate_color_map(['#20160E', '#A3AE4B', 233, 143, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.insert.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.insert.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.visual = airline#themes#generate_color_map(['#20160E', '#F3BF45', 233, 215, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.visual.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.visual.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.replace = airline#themes#generate_color_map(['#20160E', '#EC6A50', 233, 203, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.replace.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.replace.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.commandline = airline#themes#generate_color_map(['#20160E', '#86AD95', 233, 108, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.commandline.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.commandline.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.terminal = airline#themes#generate_color_map(['#20160E', '#E0956C', 233, 173, 'bold'], ['#D9C6A3', '#513B27', 187, 237], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.terminal.airline_warning = ['#20160E', '#F3BF45', 233, 215]
  let g:airline#themes#subway_seat#palette.terminal.airline_error = ['#20160E', '#EC6A50', 233, 203]
  let g:airline#themes#subway_seat#palette.inactive = airline#themes#generate_color_map(['#967B5C', '#20160E', 101, 233], ['#967B5C', '#20160E', 101, 233], ['#7B6047', '#20160E', 95, 233])
  let g:airline#themes#subway_seat#palette.accents = {'red': ['#EC6A50', '', 203, '']}
endif
