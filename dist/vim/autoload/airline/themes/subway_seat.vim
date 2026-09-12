" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'subway_seat'

if &background ==# 'light'
  let g:airline#themes#subway_seat#palette = {}
  let g:airline#themes#subway_seat#palette.normal = airline#themes#generate_color_map(['#F8EFDF', '#A04800', 255, 130, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.normal.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.normal.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.insert = airline#themes#generate_color_map(['#F8EFDF', '#66740F', 255, 58, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.insert.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.insert.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.visual = airline#themes#generate_color_map(['#F8EFDF', '#976608', 255, 94, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.visual.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.visual.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.replace = airline#themes#generate_color_map(['#F8EFDF', '#BF4233', 255, 167, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.replace.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.replace.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.commandline = airline#themes#generate_color_map(['#F8EFDF', '#3E7157', 255, 65, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.commandline.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.commandline.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.terminal = airline#themes#generate_color_map(['#F8EFDF', '#843811', 255, 88, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat#palette.terminal.airline_warning = ['#F8EFDF', '#976608', 255, 94]
  let g:airline#themes#subway_seat#palette.terminal.airline_error = ['#F8EFDF', '#BF4233', 255, 167]
  let g:airline#themes#subway_seat#palette.inactive = airline#themes#generate_color_map(['#8C7254', '#E4D8C0', 101, 187], ['#8C7254', '#E4D8C0', 101, 187], ['#A58D6D', '#E4D8C0', 137, 187])
  let g:airline#themes#subway_seat#palette.accents = {'red': ['#BF4233', '', 167, '']}
else
  let g:airline#themes#subway_seat#palette = {}
  let g:airline#themes#subway_seat#palette.normal = airline#themes#generate_color_map(['#20160E', '#EC7F31', 234, 208, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.normal.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.normal.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.insert = airline#themes#generate_color_map(['#20160E', '#ADB956', 234, 143, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.insert.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.insert.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.visual = airline#themes#generate_color_map(['#20160E', '#F3BF45', 234, 214, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.visual.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.visual.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.replace = airline#themes#generate_color_map(['#20160E', '#FF8373', 234, 210, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.replace.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.replace.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.commandline = airline#themes#generate_color_map(['#20160E', '#86AD95', 234, 108, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.commandline.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.commandline.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.terminal = airline#themes#generate_color_map(['#20160E', '#F4A87E', 234, 216, 'bold'], ['#D9C6A3', '#513B27', 187, 238], ['#C4AE8C', '#2A1D13', 180, 234])
  let g:airline#themes#subway_seat#palette.terminal.airline_warning = ['#20160E', '#F3BF45', 234, 214]
  let g:airline#themes#subway_seat#palette.terminal.airline_error = ['#20160E', '#FF8373', 234, 210]
  let g:airline#themes#subway_seat#palette.inactive = airline#themes#generate_color_map(['#967B5C', '#20160E', 101, 234], ['#967B5C', '#20160E', 101, 234], ['#7B6047', '#20160E', 95, 234])
  let g:airline#themes#subway_seat#palette.accents = {'red': ['#FF8373', '', 210, '']}
endif
