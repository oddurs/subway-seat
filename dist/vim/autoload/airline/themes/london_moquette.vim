" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'london_moquette'

if &background ==# 'light'
  let g:airline#themes#london_moquette#palette = {}
  let g:airline#themes#london_moquette#palette.normal = airline#themes#generate_color_map(['#E5EAF6', '#9F591B', 255, 130, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.normal.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.normal.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.insert = airline#themes#generate_color_map(['#E5EAF6', '#357D41', 255, 29, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.insert.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.insert.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.visual = airline#themes#generate_color_map(['#E5EAF6', '#896800', 255, 94, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.visual.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.visual.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.replace = airline#themes#generate_color_map(['#E5EAF6', '#CA2822', 255, 160, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.replace.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.replace.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.commandline = airline#themes#generate_color_map(['#E5EAF6', '#007376', 255, 30, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.commandline.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.commandline.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.terminal = airline#themes#generate_color_map(['#E5EAF6', '#7660AB', 255, 97, 'bold'], ['#434548', '#ADB7CB', 238, 146], ['#515459', '#D9E0EC', 240, 254])
  let g:airline#themes#london_moquette#palette.terminal.airline_warning = ['#E5EAF6', '#896800', 255, 94]
  let g:airline#themes#london_moquette#palette.terminal.airline_error = ['#E5EAF6', '#CA2822', 255, 160]
  let g:airline#themes#london_moquette#palette.inactive = airline#themes#generate_color_map(['#727781', '#CED5E3', 243, 188], ['#727781', '#CED5E3', 243, 188], ['#8A919F', '#CED5E3', 246, 188])
  let g:airline#themes#london_moquette#palette.accents = {'red': ['#CA2822', '', 160, '']}
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
