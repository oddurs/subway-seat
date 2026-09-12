" Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
" airline: let g:airline_theme = 'paris_catacombes'

if &background ==# 'light'
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#E7F5ED', '#754500', 255, 94, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#E7F5ED', '#207F41', 255, 29, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#E7F5ED', '#8A6700', 255, 94, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#E7F5ED', '#BB403B', 255, 131, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#E7F5ED', '#086142', 255, 23, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#E7F5ED', '#9A557D', 255, 132, 'bold'], ['#374940', '#9FC6B1', 238, 151], ['#45594F', '#D8EADF', 240, 254])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#E7F5ED', '#8A6700', 255, 94]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#E7F5ED', '#BB403B', 255, 131]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#627F70', '#C8E0D3', 66, 253], ['#627F70', '#C8E0D3', 66, 253], ['#789C88', '#C8E0D3', 108, 253])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#BB403B', '', 131, '']}
else
  let g:airline#themes#paris_catacombes#palette = {}
  let g:airline#themes#paris_catacombes#palette.normal = airline#themes#generate_color_map(['#0A100D', '#D0914F', 233, 173, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.normal.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.normal.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.insert = airline#themes#generate_color_map(['#0A100D', '#80C28E', 233, 108, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.insert.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.insert.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.visual = airline#themes#generate_color_map(['#0A100D', '#F2BF4B', 233, 214, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.visual.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.visual.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.replace = airline#themes#generate_color_map(['#0A100D', '#E1837A', 233, 174, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.replace.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.replace.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.commandline = airline#themes#generate_color_map(['#0A100D', '#6CA087', 233, 72, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.commandline.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.commandline.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.terminal = airline#themes#generate_color_map(['#0A100D', '#CE96B4', 233, 175, 'bold'], ['#BFC8C2', '#24342C', 251, 236], ['#A5B1AA', '#0D1711', 145, 233])
  let g:airline#themes#paris_catacombes#palette.terminal.airline_warning = ['#0A100D', '#F2BF4B', 233, 214]
  let g:airline#themes#paris_catacombes#palette.terminal.airline_error = ['#0A100D', '#E1837A', 233, 174]
  let g:airline#themes#paris_catacombes#palette.inactive = airline#themes#generate_color_map(['#708178', '#0A100D', 244, 233], ['#708178', '#0A100D', 244, 233], ['#54655C', '#0A100D', 59, 233])
  let g:airline#themes#paris_catacombes#palette.accents = {'red': ['#E1837A', '', 174, '']}
endif
