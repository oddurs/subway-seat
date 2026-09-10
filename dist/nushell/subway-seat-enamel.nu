# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Enamel for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#A56E00"
    shape_external_resolved: "#A56E00"
    shape_external: "#C44A33"
    shape_keyword: "#C4561A"
    shape_flag: "#3E7157"
    shape_externalarg: "#54402F"
    shape_signature: "#3E7157"
    shape_string: "#697813"
    shape_raw_string: "#697813"
    shape_string_interpolation: "#AE5F3A"
    shape_int: "#C44A33"
    shape_float: "#C44A33"
    shape_bool: "#C44A33"
    shape_binary: "#C44A33"
    shape_datetime: "#C44A33"
    shape_nothing: "#C44A33"
    shape_literal: "#C44A33"
    shape_range: "#AE5F3A"
    shape_custom: "#AE5F3A"
    shape_variable: "#AE5F3A"
    shape_vardecl: "#AE5F3A"
    shape_filepath: "#54402F"
    shape_directory: "#54402F"
    shape_globpattern: "#AE5F3A"
    shape_glob_interpolation: "#AE5F3A"
    shape_pipe: "#C4561A"
    shape_redirection: "#AE5F3A"
    shape_operator: "#AE5F3A"
    shape_block: "#735C44"
    shape_closure: "#735C44"
    shape_list: "#735C44"
    shape_record: "#735C44"
    shape_table: "#735C44"
    shape_match_pattern: "#697813"
    shape_matching_brackets: { fg: "#BA8210" attr: "b" }
    shape_garbage: { fg: "#C44A33" attr: "u" }

    background: "#F4E9D4"
    foreground: "#3E2C1E"
    cursor: "#C4561A"
    separator: "#BAA07A"
    leading_trailing_space_bg: { bg: "#CAB48E" }
    header: { fg: "#C4561A" attr: "b" }
    row_index: "#8C7254"
    empty: "#A58C6A"
    hints: "#A58C6A"
    search_result: { fg: "#F4E9D4" bg: "#A56E00" }
    selection: { fg: "#2A1D13" bg: "#CAB48E" }
    selection_cursor: { attr: "n" }
    bool: "#C44A33"
    int: "#C44A33"
    float: "#C44A33"
    string: "#3E2C1E"
    glob: "#AE5F3A"
    binary: "#C44A33"
    binary_null_char: "#A58C6A"
    binary_printable: "#697813"
    binary_whitespace: "#3E7157"
    binary_ascii_other: "#AE5F3A"
    binary_non_ascii: "#C4561A"
    custom: "#AE5F3A"
    nothing: "#A58C6A"
    list: "#3E2C1E"
    record: "#3E2C1E"
    range: "#AE5F3A"
    cell-path: "#735C44"
    block: "#735C44"
    closure: "#735C44"
    semver: "#3E7157"
    semver-range: "#3E7157"
    banner_foreground: "#3E2C1E"
    banner_highlight1: "#C4561A"
    banner_highlight2: "#A56E00"
    filesize: {||
      if $in < 1kb { "#654F3B"
      } else if $in < 1mb { "#697813"
      } else if $in < 100mb { "#A56E00"
      } else if $in < 1gb { "#C4561A"
      } else { "#C44A33" }
    }
    duration: {||
      if $in < 1sec { "#697813"
      } else if $in < 1min { "#A56E00"
      } else if $in < 1hr { "#C4561A"
      } else { "#C44A33" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#7B8B22"
      } else if $in < 1day { "#697813"
      } else if $in < 1wk { "#A56E00"
      } else if $in < 4wk { "#C4561A"
      } else if $in < 52wk { "#654F3B"
      } else { "#8C7254" }
    }
}

$env.config.explore = {
    status_bar_background: { fg: "#3E2C1E" bg: "#E2D3B6" }
    command_bar_text: { fg: "#3E2C1E" }
    highlight: { fg: "#F4E9D4" bg: "#A56E00" }
    selected_cell: { fg: "#F4E9D4" bg: "#C4561A" }
    status: {
        info: "#3F6480"
        success: "#697813"
        warn: "#A56E00"
        error: "#C44A33"
    }
}
