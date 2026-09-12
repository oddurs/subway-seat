# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Moquette for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F2C03F"
    shape_external_resolved: "#F2C03F"
    shape_external: "#FE8474"
    shape_keyword: "#DE8946"
    shape_flag: "#54B4B5"
    shape_externalarg: "#C1C9D8"
    shape_signature: "#54B4B5"
    shape_string: "#77C581"
    shape_raw_string: "#77C581"
    shape_string_interpolation: "#AE9EDC"
    shape_int: "#FE8474"
    shape_float: "#FE8474"
    shape_bool: "#FE8474"
    shape_binary: "#FE8474"
    shape_datetime: "#FE8474"
    shape_nothing: "#FE8474"
    shape_literal: "#FE8474"
    shape_range: "#AE9EDC"
    shape_custom: "#AE9EDC"
    shape_variable: "#AE9EDC"
    shape_vardecl: "#AE9EDC"
    shape_filepath: "#C1C9D8"
    shape_directory: "#C1C9D8"
    shape_globpattern: "#AE9EDC"
    shape_glob_interpolation: "#AE9EDC"
    shape_pipe: "#DE8946"
    shape_redirection: "#AE9EDC"
    shape_operator: "#AE9EDC"
    shape_block: "#8F9AB0"
    shape_closure: "#8F9AB0"
    shape_list: "#8F9AB0"
    shape_record: "#8F9AB0"
    shape_table: "#8F9AB0"
    shape_match_pattern: "#77C581"
    shape_matching_brackets: { fg: "#FFD36C" attr: "b" }
    shape_garbage: { fg: "#FE8474" attr: "u" }

    background: "#1E2941"
    foreground: "#D8DEEA"
    cursor: "#F2C03F"
    separator: "#3D4F72"
    leading_trailing_space_bg: { bg: "#303F61" }
    header: { fg: "#DE8946" attr: "b" }
    row_index: "#73819C"
    empty: "#576685"
    hints: "#576685"
    search_result: { fg: "#E9EDF5" bg: "#5E5640" }
    selection: { fg: "#E9EDF5" bg: "#3D4F72" }
    selection_cursor: { attr: "n" }
    bool: "#FE8474"
    int: "#FE8474"
    float: "#FE8474"
    string: "#D8DEEA"
    glob: "#AE9EDC"
    binary: "#FE8474"
    binary_null_char: "#576685"
    binary_printable: "#77C581"
    binary_whitespace: "#54B4B5"
    binary_ascii_other: "#AE9EDC"
    binary_non_ascii: "#DE8946"
    custom: "#AE9EDC"
    nothing: "#576685"
    list: "#D8DEEA"
    record: "#D8DEEA"
    range: "#AE9EDC"
    cell-path: "#8F9AB0"
    block: "#8F9AB0"
    closure: "#8F9AB0"
    semver: "#54B4B5"
    semver-range: "#54B4B5"
    banner_foreground: "#D8DEEA"
    banner_highlight1: "#DE8946"
    banner_highlight2: "#F2C03F"
    filesize: {||
      if $in < 1kb { "#A9B2C4"
      } else if $in < 1mb { "#77C581"
      } else if $in < 100mb { "#F2C03F"
      } else if $in < 1gb { "#DE8946"
      } else { "#FE8474" }
    }
    duration: {||
      if $in < 1sec { "#77C581"
      } else if $in < 1min { "#F2C03F"
      } else if $in < 1hr { "#DE8946"
      } else { "#FE8474" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#9AD2A0"
      } else if $in < 1day { "#77C581"
      } else if $in < 1wk { "#F2C03F"
      } else if $in < 4wk { "#DE8946"
      } else if $in < 52wk { "#A9B2C4"
      } else { "#73819C" }
    }
}

$env.config.explore.selected_cell = { fg: "#121826" bg: "#DE8946" }
$env.config.explore.highlight = { fg: "#E9EDF5" bg: "#5E5640" }
$env.config.explore.status_bar_text = { fg: "#C1C9D8" }
$env.config.explore.status_bar_background = { fg: "#D8DEEA" bg: "#172032" }
$env.config.explore.command_bar_text = { fg: "#D8DEEA" }
$env.config.explore.command_bar_background = { bg: "#172032" }
$env.config.explore.title_bar_text = { fg: "#E9EDF5" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#303F61" }
$env.config.explore.status = {
    info: { fg: "#7595DA" }
    success: { fg: "#121826" bg: "#77C581" }
    warn: { fg: "#121826" bg: "#F2C03F" }
    error: { fg: "#121826" bg: "#FE8474" }
}
