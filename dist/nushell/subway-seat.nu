# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F3BF45"
    shape_external_resolved: "#F3BF45"
    shape_external: "#F97160"
    shape_keyword: "#EC7F31"
    shape_flag: "#86AD95"
    shape_externalarg: "#D9C6A3"
    shape_signature: "#86AD95"
    shape_string: "#ADB956"
    shape_raw_string: "#ADB956"
    shape_string_interpolation: "#E0956C"
    shape_int: "#F97160"
    shape_float: "#F97160"
    shape_bool: "#F97160"
    shape_binary: "#F97160"
    shape_datetime: "#F97160"
    shape_nothing: "#F97160"
    shape_literal: "#F97160"
    shape_range: "#E0956C"
    shape_custom: "#E0956C"
    shape_variable: "#E0956C"
    shape_vardecl: "#E0956C"
    shape_filepath: "#D9C6A3"
    shape_directory: "#D9C6A3"
    shape_globpattern: "#E0956C"
    shape_glob_interpolation: "#E0956C"
    shape_pipe: "#EC7F31"
    shape_redirection: "#E0956C"
    shape_operator: "#E0956C"
    shape_block: "#AE9575"
    shape_closure: "#AE9575"
    shape_list: "#AE9575"
    shape_record: "#AE9575"
    shape_table: "#AE9575"
    shape_match_pattern: "#ADB956"
    shape_matching_brackets: { fg: "#FFD36B" attr: "b" }
    shape_garbage: { fg: "#F97160" attr: "u" }

    background: "#362619"
    foreground: "#EDDCBC"
    cursor: "#F3BF45"
    separator: "#634932"
    leading_trailing_space_bg: { bg: "#513B27" }
    header: { fg: "#EC7F31" attr: "b" }
    row_index: "#967B5C"
    empty: "#7B6047"
    hints: "#7B6047"
    search_result: { fg: "#F8ECD4" bg: "#6F5426" }
    selection: { fg: "#F8ECD4" bg: "#634932" }
    selection_cursor: { attr: "n" }
    bool: "#F97160"
    int: "#F97160"
    float: "#F97160"
    string: "#EDDCBC"
    glob: "#E0956C"
    binary: "#F97160"
    binary_null_char: "#7B6047"
    binary_printable: "#ADB956"
    binary_whitespace: "#86AD95"
    binary_ascii_other: "#E0956C"
    binary_non_ascii: "#EC7F31"
    custom: "#E0956C"
    nothing: "#7B6047"
    list: "#EDDCBC"
    record: "#EDDCBC"
    range: "#E0956C"
    cell-path: "#AE9575"
    block: "#AE9575"
    closure: "#AE9575"
    semver: "#86AD95"
    semver-range: "#86AD95"
    banner_foreground: "#EDDCBC"
    banner_highlight1: "#EC7F31"
    banner_highlight2: "#F3BF45"
    filesize: {||
      if $in < 1kb { "#C4AE8C"
      } else if $in < 1mb { "#ADB956"
      } else if $in < 100mb { "#F3BF45"
      } else if $in < 1gb { "#EC7F31"
      } else { "#F97160" }
    }
    duration: {||
      if $in < 1sec { "#ADB956"
      } else if $in < 1min { "#F3BF45"
      } else if $in < 1hr { "#EC7F31"
      } else { "#F97160" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#BFCB63"
      } else if $in < 1day { "#ADB956"
      } else if $in < 1wk { "#F3BF45"
      } else if $in < 4wk { "#EC7F31"
      } else if $in < 52wk { "#C4AE8C"
      } else { "#967B5C" }
    }
}

$env.config.explore.selected_cell = { fg: "#20160E" bg: "#EC7F31" }
$env.config.explore.highlight = { fg: "#F8ECD4" bg: "#6F5426" }
$env.config.explore.status_bar_text = { fg: "#D9C6A3" }
$env.config.explore.status_bar_background = { fg: "#EDDCBC" bg: "#2A1D13" }
$env.config.explore.command_bar_text = { fg: "#EDDCBC" }
$env.config.explore.command_bar_background = { bg: "#2A1D13" }
$env.config.explore.title_bar_text = { fg: "#F8ECD4" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#513B27" }
$env.config.explore.status = {
    info: { fg: "#7F9BAE" }
    success: { fg: "#20160E" bg: "#ADB956" }
    warn: { fg: "#20160E" bg: "#F3BF45" }
    error: { fg: "#20160E" bg: "#F97160" }
}
