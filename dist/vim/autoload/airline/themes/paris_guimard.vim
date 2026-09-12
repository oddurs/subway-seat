" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_guimard'

if &background ==# 'light'
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#E4EDE8', '#9B5D00', 255, 130, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#E4EDE8', '#18803F', 255, 29, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#E4EDE8', '#8A6700', 255, 94, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#E4EDE8', '#BB403B', 255, 131, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#E4EDE8', '#277555', 255, 29, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#E4EDE8', '#9A557D', 255, 132, 'bold'], ['#374940', '#A3BFB0', 238, 249], ['#45594F', '#D8E3DC', 240, 254])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#E4EDE8', '#8A6700', 255, 94]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#E4EDE8', '#BB403B', 255, 131]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#627F70', '#CAD9D1', 66, 188], ['#627F70', '#CAD9D1', 66, 188], ['#7B9989', '#CAD9D1', 246, 188])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#BB403B', '', 131, '']}
else
  let g:airline#themes#paris_guimard#palette = {}
  let g:airline#themes#paris_guimard#palette.normal = airline#themes#generate_color_map(['#141A17', '#D0914F', 234, 173, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.normal.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.normal.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.insert = airline#themes#generate_color_map(['#141A17', '#80C28E', 234, 108, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.insert.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.insert.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.visual = airline#themes#generate_color_map(['#141A17', '#EBC168', 234, 179, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.visual.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.visual.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.replace = airline#themes#generate_color_map(['#141A17', '#E1837A', 234, 174, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.replace.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.replace.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.commandline = airline#themes#generate_color_map(['#141A17', '#7BB096', 234, 108, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.commandline.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.commandline.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.terminal = airline#themes#generate_color_map(['#141A17', '#CE96B4', 234, 175, 'bold'], ['#C3CAC6', '#34453C', 251, 238], ['#ABB4AF', '#1A231E', 249, 234])
  let g:airline#themes#paris_guimard#palette.terminal.airline_warning = ['#141A17', '#EBC168', 234, 179]
  let g:airline#themes#paris_guimard#palette.terminal.airline_error = ['#141A17', '#E1837A', 234, 174]
  let g:airline#themes#paris_guimard#palette.inactive = airline#themes#generate_color_map(['#77847D', '#141A17', 244, 234], ['#77847D', '#141A17', 244, 234], ['#5B6A62', '#141A17', 241, 234])
  let g:airline#themes#paris_guimard#palette.accents = {'red': ['#E1837A', '', 174, '']}
endif
