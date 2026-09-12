" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'subway_seat_tunnel'

if &background ==# 'light'
  let g:airline#themes#subway_seat_tunnel#palette = {}
  let g:airline#themes#subway_seat_tunnel#palette.normal = airline#themes#generate_color_map(['#F8EFDF', '#AD4E00', 255, 130, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.normal.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.normal.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.insert = airline#themes#generate_color_map(['#F8EFDF', '#66740F', 255, 58, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.insert.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.insert.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.visual = airline#themes#generate_color_map(['#F8EFDF', '#936200', 255, 94, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.visual.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.visual.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.replace = airline#themes#generate_color_map(['#F8EFDF', '#BC4031', 255, 124, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.replace.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.replace.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.commandline = airline#themes#generate_color_map(['#F8EFDF', '#3E7157', 255, 65, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.commandline.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.commandline.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.terminal = airline#themes#generate_color_map(['#F8EFDF', '#863913', 255, 88, 'bold'], ['#54402F', '#CBB898', 238, 180], ['#654F3B', '#EEE4D0', 240, 254])
  let g:airline#themes#subway_seat_tunnel#palette.terminal.airline_warning = ['#F8EFDF', '#936200', 255, 94]
  let g:airline#themes#subway_seat_tunnel#palette.terminal.airline_error = ['#F8EFDF', '#BC4031', 255, 124]
  let g:airline#themes#subway_seat_tunnel#palette.inactive = airline#themes#generate_color_map(['#8C7254', '#E4D8C0', 101, 187], ['#8C7254', '#E4D8C0', 101, 187], ['#A58D6D', '#E4D8C0', 137, 187])
  let g:airline#themes#subway_seat_tunnel#palette.accents = {'red': ['#BC4031', '', 124, '']}
else
  let g:airline#themes#subway_seat_tunnel#palette = {}
  let g:airline#themes#subway_seat_tunnel#palette.normal = airline#themes#generate_color_map(['#140D07', '#EC7F31', 233, 208, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.normal.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.normal.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.insert = airline#themes#generate_color_map(['#140D07', '#ADB956', 233, 143, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.insert.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.insert.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.visual = airline#themes#generate_color_map(['#140D07', '#F3BF45', 233, 214, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.visual.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.visual.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.replace = airline#themes#generate_color_map(['#140D07', '#F97160', 233, 203, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.replace.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.replace.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.commandline = airline#themes#generate_color_map(['#140D07', '#86AD95', 233, 108, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.commandline.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.commandline.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.terminal = airline#themes#generate_color_map(['#140D07', '#F4A87E', 233, 216, 'bold'], ['#D6C3A0', '#3D2C1D', 187, 236], ['#C0AA88', '#1B120A', 144, 233])
  let g:airline#themes#subway_seat_tunnel#palette.terminal.airline_warning = ['#140D07', '#F3BF45', 233, 214]
  let g:airline#themes#subway_seat_tunnel#palette.terminal.airline_error = ['#140D07', '#F97160', 233, 203]
  let g:airline#themes#subway_seat_tunnel#palette.inactive = airline#themes#generate_color_map(['#917759', '#140D07', 101, 233], ['#917759', '#140D07', 101, 233], ['#745B45', '#140D07', 95, 233])
  let g:airline#themes#subway_seat_tunnel#palette.accents = {'red': ['#F97160', '', 203, '']}
endif
