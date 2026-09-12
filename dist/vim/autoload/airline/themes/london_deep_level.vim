" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'london_deep_level'

if &background ==# 'light'
  let g:airline#themes#london_deep_level#palette = {}
  let g:airline#themes#london_deep_level#palette.normal = airline#themes#generate_color_map(['#E8F0FF', '#A54300', 255, 130, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.normal.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.normal.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.insert = airline#themes#generate_color_map(['#E8F0FF', '#0D8131', 255, 28, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.insert.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.insert.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.visual = airline#themes#generate_color_map(['#E8F0FF', '#8D6C08', 255, 94, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.visual.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.visual.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.replace = airline#themes#generate_color_map(['#E8F0FF', '#CC2E25', 255, 160, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.replace.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.replace.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.commandline = airline#themes#generate_color_map(['#E8F0FF', '#007376', 255, 30, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.commandline.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.commandline.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.terminal = airline#themes#generate_color_map(['#E8F0FF', '#755FA9', 255, 97, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_deep_level#palette.terminal.airline_warning = ['#E8F0FF', '#8D6C08', 255, 94]
  let g:airline#themes#london_deep_level#palette.terminal.airline_error = ['#E8F0FF', '#CC2E25', 255, 160]
  let g:airline#themes#london_deep_level#palette.inactive = airline#themes#generate_color_map(['#697794', '#CCDAF2', 67, 189], ['#697794', '#CCDAF2', 67, 189], ['#8192B4', '#CCDAF2', 103, 189])
  let g:airline#themes#london_deep_level#palette.accents = {'red': ['#CC2E25', '', 160, '']}
else
  let g:airline#themes#london_deep_level#palette = {}
  let g:airline#themes#london_deep_level#palette.normal = airline#themes#generate_color_map(['#0A0E18', '#DE8946', 233, 173, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.normal.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.normal.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.insert = airline#themes#generate_color_map(['#0A0E18', '#77C581', 233, 114, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.insert.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.insert.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.visual = airline#themes#generate_color_map(['#0A0E18', '#F2C03F', 233, 214, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.visual.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.visual.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.replace = airline#themes#generate_color_map(['#0A0E18', '#FE8474', 233, 210, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.replace.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.replace.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.commandline = airline#themes#generate_color_map(['#0A0E18', '#54B4B5', 233, 73, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.commandline.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.commandline.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.terminal = airline#themes#generate_color_map(['#0A0E18', '#AE9EDC', 233, 146, 'bold'], ['#BEC6D5', '#232F49', 251, 236], ['#A5AEC0', '#0D1421', 145, 233])
  let g:airline#themes#london_deep_level#palette.terminal.airline_warning = ['#0A0E18', '#F2C03F', 233, 214]
  let g:airline#themes#london_deep_level#palette.terminal.airline_error = ['#0A0E18', '#FE8474', 233, 210]
  let g:airline#themes#london_deep_level#palette.inactive = airline#themes#generate_color_map(['#6F7C97', '#0A0E18', 67, 233], ['#6F7C97', '#0A0E18', 67, 233], ['#53617D', '#0A0E18', 60, 233])
  let g:airline#themes#london_deep_level#palette.accents = {'red': ['#FE8474', '', 210, '']}
endif
