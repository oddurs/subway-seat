" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'london_moquette'

if &background ==# 'light'
  let g:airline#themes#london_moquette#palette = {}
  let g:airline#themes#london_moquette#palette.normal = airline#themes#generate_color_map(['#E8F0FF', '#B14A07', 255, 130, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.normal.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.normal.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.insert = airline#themes#generate_color_map(['#E8F0FF', '#0D8131', 255, 28, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.insert.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.insert.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.visual = airline#themes#generate_color_map(['#E8F0FF', '#896800', 255, 94, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.visual.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.visual.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.replace = airline#themes#generate_color_map(['#E8F0FF', '#C92B23', 255, 160, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.replace.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.replace.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.commandline = airline#themes#generate_color_map(['#E8F0FF', '#007376', 255, 30, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.commandline.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.commandline.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.terminal = airline#themes#generate_color_map(['#E8F0FF', '#7660AB', 255, 97, 'bold'], ['#3C4557', '#A8BBE2', 238, 146], ['#4A5469', '#DCE5F7', 240, 254])
  let g:airline#themes#london_moquette#palette.terminal.airline_warning = ['#E8F0FF', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.terminal.airline_error = ['#E8F0FF', '#C92B23', 255, 160]
  let g:airline#themes#london_moquette#palette.inactive = airline#themes#generate_color_map(['#697794', '#CCDAF2', 67, 189], ['#697794', '#CCDAF2', 67, 189], ['#8192B4', '#CCDAF2', 103, 189])
  let g:airline#themes#london_moquette#palette.accents = {'red': ['#C92B23', '', 160, '']}
else
  let g:airline#themes#london_moquette#palette = {}
  let g:airline#themes#london_moquette#palette.normal = airline#themes#generate_color_map(['#121826', '#DE8946', 234, 173, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.normal.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.normal.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.insert = airline#themes#generate_color_map(['#121826', '#77C581', 234, 114, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.insert.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.insert.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.visual = airline#themes#generate_color_map(['#121826', '#F2C03F', 234, 214, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.visual.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.visual.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.replace = airline#themes#generate_color_map(['#121826', '#F17869', 234, 210, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.replace.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.replace.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.commandline = airline#themes#generate_color_map(['#121826', '#54B4B5', 234, 73, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.commandline.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.commandline.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.terminal = airline#themes#generate_color_map(['#121826', '#AE9EDC', 234, 146, 'bold'], ['#C1C9D8', '#303F61', 251, 238], ['#A9B2C4', '#172032', 249, 234])
  let g:airline#themes#london_moquette#palette.terminal.airline_warning = ['#121826', '#F2C03F', 234, 214]
  let g:airline#themes#london_moquette#palette.terminal.airline_error = ['#121826', '#F17869', 234, 210]
  let g:airline#themes#london_moquette#palette.inactive = airline#themes#generate_color_map(['#73819C', '#121826', 67, 234], ['#73819C', '#121826', 67, 234], ['#576685', '#121826', 60, 234])
  let g:airline#themes#london_moquette#palette.accents = {'red': ['#F17869', '', 210, '']}
endif
