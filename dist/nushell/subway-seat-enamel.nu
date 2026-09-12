# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Enamel for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#976608"
    shape_external_resolved: "#976608"
    shape_external: "#BF4233"
    shape_keyword: "#A04800"
    shape_flag: "#3E7157"
    shape_externalarg: "#54402F"
    shape_signature: "#3E7157"
    shape_string: "#66740F"
    shape_raw_string: "#66740F"
    shape_string_interpolation: "#843811"
    shape_int: "#BF4233"
    shape_float: "#BF4233"
    shape_bool: "#BF4233"
    shape_binary: "#BF4233"
    shape_datetime: "#BF4233"
    shape_nothing: "#BF4233"
    shape_literal: "#BF4233"
    shape_range: "#843811"
    shape_custom: "#843811"
    shape_variable: "#843811"
    shape_vardecl: "#843811"
    shape_filepath: "#54402F"
    shape_directory: "#54402F"
    shape_globpattern: "#843811"
    shape_glob_interpolation: "#843811"
    shape_pipe: "#A04800"
    shape_redirection: "#843811"
    shape_operator: "#843811"
    shape_block: "#735C44"
    shape_closure: "#735C44"
    shape_list: "#735C44"
    shape_record: "#735C44"
    shape_table: "#735C44"
    shape_match_pattern: "#66740F"
    shape_matching_brackets: { fg: "#A9720A" attr: "b" }
    shape_garbage: { fg: "#BF4233" attr: "u" }

    background: "#F8EFDF"
    foreground: "#3E2C1E"
    cursor: "#A04800"
    separator: "#BAA380"
    leading_trailing_space_bg: { bg: "#CBB898" }
    header: { fg: "#A04800" attr: "b" }
    row_index: "#8C7254"
    empty: "#A58D6D"
    hints: "#A58D6D"
    search_result: { fg: "#2A1D13" bg: "#DBC69E" }
    selection: { fg: "#2A1D13" bg: "#CBB898" }
    selection_cursor: { attr: "n" }
    bool: "#BF4233"
    int: "#BF4233"
    float: "#BF4233"
    string: "#3E2C1E"
    glob: "#843811"
    binary: "#BF4233"
    binary_null_char: "#A58D6D"
    binary_printable: "#66740F"
    binary_whitespace: "#3E7157"
    binary_ascii_other: "#843811"
    binary_non_ascii: "#A04800"
    custom: "#843811"
    nothing: "#A58D6D"
    list: "#3E2C1E"
    record: "#3E2C1E"
    range: "#843811"
    cell-path: "#735C44"
    block: "#735C44"
    closure: "#735C44"
    semver: "#3E7157"
    semver-range: "#3E7157"
    banner_foreground: "#3E2C1E"
    banner_highlight1: "#A04800"
    banner_highlight2: "#976608"
    filesize: {||
      if $in < 1kb { "#654F3B"
      } else if $in < 1mb { "#66740F"
      } else if $in < 100mb { "#976608"
      } else if $in < 1gb { "#A04800"
      } else { "#BF4233" }
    }
    duration: {||
      if $in < 1sec { "#66740F"
      } else if $in < 1min { "#976608"
      } else if $in < 1hr { "#A04800"
      } else { "#BF4233" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#697813"
      } else if $in < 1day { "#66740F"
      } else if $in < 1wk { "#976608"
      } else if $in < 4wk { "#A04800"
      } else if $in < 52wk { "#654F3B"
      } else { "#8C7254" }
    }
}

$env.config.explore.selected_cell = { fg: "#F8EFDF" bg: "#A04800" }
$env.config.explore.highlight = { fg: "#2A1D13" bg: "#DBC69E" }
$env.config.explore.status_bar_text = { fg: "#54402F" }
$env.config.explore.status_bar_background = { fg: "#3E2C1E" bg: "#E4D8C0" }
$env.config.explore.command_bar_text = { fg: "#3E2C1E" }
$env.config.explore.command_bar_background = { bg: "#E4D8C0" }
$env.config.explore.title_bar_text = { fg: "#2A1D13" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#DBCDB3" }
$env.config.explore.status = {
    info: { fg: "#3F6480" }
    success: { fg: "#F8EFDF" bg: "#66740F" }
    warn: { fg: "#F8EFDF" bg: "#976608" }
    error: { fg: "#F8EFDF" bg: "#BF4233" }
}
