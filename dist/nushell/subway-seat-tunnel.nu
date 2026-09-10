# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Tunnel for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F3BF45"
    shape_external_resolved: "#F3BF45"
    shape_external: "#EC6A50"
    shape_keyword: "#EC7F31"
    shape_flag: "#86AD95"
    shape_externalarg: "#D6C3A0"
    shape_signature: "#86AD95"
    shape_string: "#A3AE4B"
    shape_raw_string: "#A3AE4B"
    shape_string_interpolation: "#E0956C"
    shape_int: "#EC6A50"
    shape_float: "#EC6A50"
    shape_bool: "#EC6A50"
    shape_binary: "#EC6A50"
    shape_datetime: "#EC6A50"
    shape_nothing: "#EC6A50"
    shape_literal: "#EC6A50"
    shape_range: "#E0956C"
    shape_custom: "#E0956C"
    shape_variable: "#E0956C"
    shape_vardecl: "#E0956C"
    shape_filepath: "#D6C3A0"
    shape_directory: "#D6C3A0"
    shape_globpattern: "#E0956C"
    shape_glob_interpolation: "#E0956C"
    shape_pipe: "#EC7F31"
    shape_redirection: "#E0956C"
    shape_operator: "#E0956C"
    shape_block: "#A48B6C"
    shape_closure: "#A48B6C"
    shape_list: "#A48B6C"
    shape_record: "#A48B6C"
    shape_table: "#A48B6C"
    shape_match_pattern: "#A3AE4B"
    shape_matching_brackets: { fg: "#FFD36B" attr: "b" }
    shape_garbage: { fg: "#EC6A50" attr: "u" }

    background: "#24180E"
    foreground: "#E9D8B6"
    cursor: "#F3BF45"
    separator: "#4F3927"
    leading_trailing_space_bg: { bg: "#3D2C1D" }
    header: { fg: "#EC7F31" attr: "b" }
    row_index: "#8A7053"
    empty: "#6A523C"
    hints: "#6A523C"
    search_result: { fg: "#140D07" bg: "#F3BF45" }
    selection: { fg: "#F6EAD1" bg: "#4F3927" }
    selection_cursor: { attr: "n" }
    bool: "#EC6A50"
    int: "#EC6A50"
    float: "#EC6A50"
    string: "#E9D8B6"
    glob: "#E0956C"
    binary: "#EC6A50"
    binary_null_char: "#6A523C"
    binary_printable: "#A3AE4B"
    binary_whitespace: "#86AD95"
    binary_ascii_other: "#E0956C"
    binary_non_ascii: "#EC7F31"
    custom: "#E0956C"
    nothing: "#6A523C"
    list: "#E9D8B6"
    record: "#E9D8B6"
    range: "#E0956C"
    cell-path: "#A48B6C"
    block: "#A48B6C"
    closure: "#A48B6C"
    semver: "#86AD95"
    semver-range: "#86AD95"
    banner_foreground: "#E9D8B6"
    banner_highlight1: "#EC7F31"
    banner_highlight2: "#F3BF45"
    filesize: {||
      if $in < 1kb { "#C0AA88"
      } else if $in < 1mb { "#A3AE4B"
      } else if $in < 100mb { "#F3BF45"
      } else if $in < 1gb { "#EC7F31"
      } else { "#EC6A50" }
    }
    duration: {||
      if $in < 1sec { "#A3AE4B"
      } else if $in < 1min { "#F3BF45"
      } else if $in < 1hr { "#EC7F31"
      } else { "#EC6A50" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#BFCB63"
      } else if $in < 1day { "#A3AE4B"
      } else if $in < 1wk { "#F3BF45"
      } else if $in < 4wk { "#EC7F31"
      } else if $in < 52wk { "#C0AA88"
      } else { "#8A7053" }
    }
}

$env.config.explore = {
    status_bar_background: { fg: "#E9D8B6" bg: "#1B120A" }
    command_bar_text: { fg: "#E9D8B6" }
    highlight: { fg: "#140D07" bg: "#F3BF45" }
    selected_cell: { fg: "#140D07" bg: "#EC7F31" }
    status: {
        info: "#7F9BAE"
        success: "#A3AE4B"
        warn: "#F3BF45"
        error: "#EC6A50"
    }
}
