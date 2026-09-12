# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F3BF45"
    shape_external_resolved: "#F3BF45"
    shape_external: "#FF8373"
    shape_keyword: "#EC7F31"
    shape_flag: "#86AD95"
    shape_externalarg: "#D9C6A3"
    shape_signature: "#86AD95"
    shape_string: "#ADB956"
    shape_raw_string: "#ADB956"
    shape_string_interpolation: "#F4A87E"
    shape_int: "#FF8373"
    shape_float: "#FF8373"
    shape_bool: "#FF8373"
    shape_binary: "#FF8373"
    shape_datetime: "#FF8373"
    shape_nothing: "#FF8373"
    shape_literal: "#FF8373"
    shape_range: "#F4A87E"
    shape_custom: "#F4A87E"
    shape_variable: "#F4A87E"
    shape_vardecl: "#F4A87E"
    shape_filepath: "#D9C6A3"
    shape_directory: "#D9C6A3"
    shape_globpattern: "#F4A87E"
    shape_glob_interpolation: "#F4A87E"
    shape_pipe: "#EC7F31"
    shape_redirection: "#F4A87E"
    shape_operator: "#F4A87E"
    shape_block: "#AE9575"
    shape_closure: "#AE9575"
    shape_list: "#AE9575"
    shape_record: "#AE9575"
    shape_table: "#AE9575"
    shape_match_pattern: "#ADB956"
    shape_matching_brackets: { fg: "#FFD36B" attr: "b" }
    shape_garbage: { fg: "#FF8373" attr: "u" }

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
    bool: "#FF8373"
    int: "#FF8373"
    float: "#FF8373"
    string: "#EDDCBC"
    glob: "#F4A87E"
    binary: "#FF8373"
    binary_null_char: "#7B6047"
    binary_printable: "#ADB956"
    binary_whitespace: "#86AD95"
    binary_ascii_other: "#F4A87E"
    binary_non_ascii: "#EC7F31"
    custom: "#F4A87E"
    nothing: "#7B6047"
    list: "#EDDCBC"
    record: "#EDDCBC"
    range: "#F4A87E"
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
      } else { "#FF8373" }
    }
    duration: {||
      if $in < 1sec { "#ADB956"
      } else if $in < 1min { "#F3BF45"
      } else if $in < 1hr { "#EC7F31"
      } else { "#FF8373" }
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
    error: { fg: "#20160E" bg: "#FF8373" }
}
