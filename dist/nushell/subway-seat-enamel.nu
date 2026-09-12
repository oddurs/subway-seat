# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Enamel for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#936200"
    shape_external_resolved: "#936200"
    shape_external: "#BC4031"
    shape_keyword: "#AD4E00"
    shape_flag: "#3E7157"
    shape_externalarg: "#54402F"
    shape_signature: "#3E7157"
    shape_string: "#66740F"
    shape_raw_string: "#66740F"
    shape_string_interpolation: "#863913"
    shape_int: "#BC4031"
    shape_float: "#BC4031"
    shape_bool: "#BC4031"
    shape_binary: "#BC4031"
    shape_datetime: "#BC4031"
    shape_nothing: "#BC4031"
    shape_literal: "#BC4031"
    shape_range: "#863913"
    shape_custom: "#863913"
    shape_variable: "#863913"
    shape_vardecl: "#863913"
    shape_filepath: "#54402F"
    shape_directory: "#54402F"
    shape_globpattern: "#863913"
    shape_glob_interpolation: "#863913"
    shape_pipe: "#AD4E00"
    shape_redirection: "#863913"
    shape_operator: "#863913"
    shape_block: "#735C44"
    shape_closure: "#735C44"
    shape_list: "#735C44"
    shape_record: "#735C44"
    shape_table: "#735C44"
    shape_match_pattern: "#66740F"
    shape_matching_brackets: { fg: "#A56E00" attr: "b" }
    shape_garbage: { fg: "#BC4031" attr: "u" }

    background: "#F4E9D4"
    foreground: "#3E2C1E"
    cursor: "#AD4E00"
    separator: "#BAA07A"
    leading_trailing_space_bg: { bg: "#CAB48E" }
    header: { fg: "#AD4E00" attr: "b" }
    row_index: "#8C7254"
    empty: "#A58C6A"
    hints: "#A58C6A"
    search_result: { fg: "#2A1D13" bg: "#D7C094" }
    selection: { fg: "#2A1D13" bg: "#CAB48E" }
    selection_cursor: { attr: "n" }
    bool: "#BC4031"
    int: "#BC4031"
    float: "#BC4031"
    string: "#3E2C1E"
    glob: "#863913"
    binary: "#BC4031"
    binary_null_char: "#A58C6A"
    binary_printable: "#66740F"
    binary_whitespace: "#3E7157"
    binary_ascii_other: "#863913"
    binary_non_ascii: "#AD4E00"
    custom: "#863913"
    nothing: "#A58C6A"
    list: "#3E2C1E"
    record: "#3E2C1E"
    range: "#863913"
    cell-path: "#735C44"
    block: "#735C44"
    closure: "#735C44"
    semver: "#3E7157"
    semver-range: "#3E7157"
    banner_foreground: "#3E2C1E"
    banner_highlight1: "#AD4E00"
    banner_highlight2: "#936200"
    filesize: {||
      if $in < 1kb { "#654F3B"
      } else if $in < 1mb { "#66740F"
      } else if $in < 100mb { "#936200"
      } else if $in < 1gb { "#AD4E00"
      } else { "#BC4031" }
    }
    duration: {||
      if $in < 1sec { "#66740F"
      } else if $in < 1min { "#936200"
      } else if $in < 1hr { "#AD4E00"
      } else { "#BC4031" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#697813"
      } else if $in < 1day { "#66740F"
      } else if $in < 1wk { "#936200"
      } else if $in < 4wk { "#AD4E00"
      } else if $in < 52wk { "#654F3B"
      } else { "#8C7254" }
    }
}

$env.config.explore.selected_cell = { fg: "#F4E9D4" bg: "#AD4E00" }
$env.config.explore.highlight = { fg: "#2A1D13" bg: "#D7C094" }
$env.config.explore.status_bar_text = { fg: "#54402F" }
$env.config.explore.status_bar_background = { fg: "#3E2C1E" bg: "#E2D3B6" }
$env.config.explore.command_bar_text = { fg: "#3E2C1E" }
$env.config.explore.command_bar_background = { bg: "#E2D3B6" }
$env.config.explore.title_bar_text = { fg: "#2A1D13" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#D9C8A7" }
$env.config.explore.status = {
    info: { fg: "#3F6480" }
    success: { fg: "#F4E9D4" bg: "#66740F" }
    warn: { fg: "#F4E9D4" bg: "#936200" }
    error: { fg: "#F4E9D4" bg: "#BC4031" }
}
