# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#856A00"
    shape_external_resolved: "#856A00"
    shape_external: "#C82C2C"
    shape_keyword: "#9B5D00"
    shape_flag: "#007752"
    shape_externalarg: "#334A41"
    shape_signature: "#007752"
    shape_string: "#00823B"
    shape_raw_string: "#00823B"
    shape_string_interpolation: "#B43586"
    shape_int: "#C82C2C"
    shape_float: "#C82C2C"
    shape_bool: "#C82C2C"
    shape_binary: "#C82C2C"
    shape_datetime: "#C82C2C"
    shape_nothing: "#C82C2C"
    shape_literal: "#C82C2C"
    shape_range: "#B43586"
    shape_custom: "#B43586"
    shape_variable: "#B43586"
    shape_vardecl: "#B43586"
    shape_filepath: "#334A41"
    shape_directory: "#334A41"
    shape_globpattern: "#B43586"
    shape_glob_interpolation: "#B43586"
    shape_pipe: "#9B5D00"
    shape_redirection: "#B43586"
    shape_operator: "#B43586"
    shape_block: "#4A695C"
    shape_closure: "#4A695C"
    shape_list: "#4A695C"
    shape_record: "#4A695C"
    shape_table: "#4A695C"
    shape_match_pattern: "#00823B"
    shape_matching_brackets: { fg: "#937500" attr: "b" }
    shape_garbage: { fg: "#C82C2C" attr: "u" }

    background: "#E2EDE8"
    foreground: "#21352D"
    cursor: "#9B5D00"
    separator: "#88AF9E"
    leading_trailing_space_bg: { bg: "#9DC1B1" }
    header: { fg: "#9B5D00" attr: "b" }
    row_index: "#5C8171"
    empty: "#759A8A"
    hints: "#759A8A"
    search_result: { fg: "#16241E" bg: "#C6C6A2" }
    selection: { fg: "#16241E" bg: "#9DC1B1" }
    selection_cursor: { attr: "n" }
    bool: "#C82C2C"
    int: "#C82C2C"
    float: "#C82C2C"
    string: "#21352D"
    glob: "#B43586"
    binary: "#C82C2C"
    binary_null_char: "#759A8A"
    binary_printable: "#00823B"
    binary_whitespace: "#007752"
    binary_ascii_other: "#B43586"
    binary_non_ascii: "#9B5D00"
    custom: "#B43586"
    nothing: "#759A8A"
    list: "#21352D"
    record: "#21352D"
    range: "#B43586"
    cell-path: "#4A695C"
    block: "#4A695C"
    closure: "#4A695C"
    semver: "#007752"
    semver-range: "#007752"
    banner_foreground: "#21352D"
    banner_highlight1: "#9B5D00"
    banner_highlight2: "#856A00"
    filesize: {||
      if $in < 1kb { "#405B4F"
      } else if $in < 1mb { "#00823B"
      } else if $in < 100mb { "#856A00"
      } else if $in < 1gb { "#9B5D00"
      } else { "#C82C2C" }
    }
    duration: {||
      if $in < 1sec { "#00823B"
      } else if $in < 1min { "#856A00"
      } else if $in < 1hr { "#9B5D00"
      } else { "#C82C2C" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#00863D"
      } else if $in < 1day { "#00823B"
      } else if $in < 1wk { "#856A00"
      } else if $in < 4wk { "#9B5D00"
      } else if $in < 52wk { "#405B4F"
      } else { "#5C8171" }
    }
}

$env.config.explore.selected_cell = { fg: "#E2EDE8" bg: "#9B5D00" }
$env.config.explore.highlight = { fg: "#16241E" bg: "#C6C6A2" }
$env.config.explore.status_bar_text = { fg: "#334A41" }
$env.config.explore.status_bar_background = { fg: "#21352D" bg: "#C8DAD1" }
$env.config.explore.command_bar_text = { fg: "#21352D" }
$env.config.explore.command_bar_background = { bg: "#C8DAD1" }
$env.config.explore.title_bar_text = { fg: "#16241E" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#B6D2C5" }
$env.config.explore.status = {
    info: { fg: "#0961A9" }
    success: { fg: "#E2EDE8" bg: "#00823B" }
    warn: { fg: "#E2EDE8" bg: "#856A00" }
    error: { fg: "#E2EDE8" bg: "#C82C2C" }
}
