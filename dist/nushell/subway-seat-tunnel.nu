# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Subway Seat Tunnel for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F3BF45"
    shape_external_resolved: "#F3BF45"
    shape_external: "#F97160"
    shape_keyword: "#EC7F31"
    shape_flag: "#86AD95"
    shape_externalarg: "#D6C3A0"
    shape_signature: "#86AD95"
    shape_string: "#ADB956"
    shape_raw_string: "#ADB956"
    shape_string_interpolation: "#F4A87E"
    shape_int: "#F97160"
    shape_float: "#F97160"
    shape_bool: "#F97160"
    shape_binary: "#F97160"
    shape_datetime: "#F97160"
    shape_nothing: "#F97160"
    shape_literal: "#F97160"
    shape_range: "#F4A87E"
    shape_custom: "#F4A87E"
    shape_variable: "#F4A87E"
    shape_vardecl: "#F4A87E"
    shape_filepath: "#D6C3A0"
    shape_directory: "#D6C3A0"
    shape_globpattern: "#F4A87E"
    shape_glob_interpolation: "#F4A87E"
    shape_pipe: "#EC7F31"
    shape_redirection: "#F4A87E"
    shape_operator: "#F4A87E"
    shape_block: "#AA9171"
    shape_closure: "#AA9171"
    shape_list: "#AA9171"
    shape_record: "#AA9171"
    shape_table: "#AA9171"
    shape_match_pattern: "#ADB956"
    shape_matching_brackets: { fg: "#FFD36B" attr: "b" }
    shape_garbage: { fg: "#F97160" attr: "u" }

    background: "#24180E"
    foreground: "#E9D8B6"
    cursor: "#F3BF45"
    separator: "#4F3927"
    leading_trailing_space_bg: { bg: "#3D2C1D" }
    header: { fg: "#EC7F31" attr: "b" }
    row_index: "#917759"
    empty: "#745B45"
    hints: "#745B45"
    search_result: { fg: "#F6EAD1" bg: "#624A1E" }
    selection: { fg: "#F6EAD1" bg: "#4F3927" }
    selection_cursor: { attr: "n" }
    bool: "#F97160"
    int: "#F97160"
    float: "#F97160"
    string: "#E9D8B6"
    glob: "#F4A87E"
    binary: "#F97160"
    binary_null_char: "#745B45"
    binary_printable: "#ADB956"
    binary_whitespace: "#86AD95"
    binary_ascii_other: "#F4A87E"
    binary_non_ascii: "#EC7F31"
    custom: "#F4A87E"
    nothing: "#745B45"
    list: "#E9D8B6"
    record: "#E9D8B6"
    range: "#F4A87E"
    cell-path: "#AA9171"
    block: "#AA9171"
    closure: "#AA9171"
    semver: "#86AD95"
    semver-range: "#86AD95"
    banner_foreground: "#E9D8B6"
    banner_highlight1: "#EC7F31"
    banner_highlight2: "#F3BF45"
    filesize: {||
      if $in < 1kb { "#C0AA88"
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
      } else if $in < 52wk { "#C0AA88"
      } else { "#917759" }
    }
}

$env.config.explore.selected_cell = { fg: "#140D07" bg: "#EC7F31" }
$env.config.explore.highlight = { fg: "#F6EAD1" bg: "#624A1E" }
$env.config.explore.status_bar_text = { fg: "#D6C3A0" }
$env.config.explore.status_bar_background = { fg: "#E9D8B6" bg: "#1B120A" }
$env.config.explore.command_bar_text = { fg: "#E9D8B6" }
$env.config.explore.command_bar_background = { bg: "#1B120A" }
$env.config.explore.title_bar_text = { fg: "#F6EAD1" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#3D2C1D" }
$env.config.explore.status = {
    info: { fg: "#7F9BAE" }
    success: { fg: "#140D07" bg: "#ADB956" }
    warn: { fg: "#140D07" bg: "#F3BF45" }
    error: { fg: "#140D07" bg: "#F97160" }
}
