# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#916D07"
    shape_external_resolved: "#916D07"
    shape_external: "#AC3B32"
    shape_keyword: "#764C00"
    shape_flag: "#006267"
    shape_externalarg: "#3B4742"
    shape_signature: "#006267"
    shape_string: "#218366"
    shape_raw_string: "#218366"
    shape_string_interpolation: "#B36B51"
    shape_int: "#AC3B32"
    shape_float: "#AC3B32"
    shape_bool: "#AC3B32"
    shape_binary: "#AC3B32"
    shape_datetime: "#AC3B32"
    shape_nothing: "#AC3B32"
    shape_literal: "#AC3B32"
    shape_range: "#B36B51"
    shape_custom: "#B36B51"
    shape_variable: "#B36B51"
    shape_vardecl: "#B36B51"
    shape_filepath: "#3B4742"
    shape_directory: "#3B4742"
    shape_globpattern: "#B36B51"
    shape_glob_interpolation: "#B36B51"
    shape_pipe: "#764C00"
    shape_redirection: "#B36B51"
    shape_operator: "#B36B51"
    shape_block: "#56645F"
    shape_closure: "#56645F"
    shape_list: "#56645F"
    shape_record: "#56645F"
    shape_table: "#56645F"
    shape_match_pattern: "#218366"
    shape_matching_brackets: { fg: "#A07A12" attr: "b" }
    shape_garbage: { fg: "#AC3B32" attr: "u" }

    background: "#EEF2F1"
    foreground: "#27342F"
    cursor: "#764C00"
    separator: "#99ABA6"
    leading_trailing_space_bg: { bg: "#B0BFBB" }
    header: { fg: "#764C00" attr: "b" }
    row_index: "#6C7C76"
    empty: "#859792"
    hints: "#859792"
    search_result: { fg: "#19221E" bg: "#D2CAAB" }
    selection: { fg: "#19221E" bg: "#B0BFBB" }
    selection_cursor: { attr: "n" }
    bool: "#AC3B32"
    int: "#AC3B32"
    float: "#AC3B32"
    string: "#27342F"
    glob: "#B36B51"
    binary: "#AC3B32"
    binary_null_char: "#859792"
    binary_printable: "#218366"
    binary_whitespace: "#006267"
    binary_ascii_other: "#B36B51"
    binary_non_ascii: "#764C00"
    custom: "#B36B51"
    nothing: "#859792"
    list: "#27342F"
    record: "#27342F"
    range: "#B36B51"
    cell-path: "#56645F"
    block: "#56645F"
    closure: "#56645F"
    semver: "#006267"
    semver-range: "#006267"
    banner_foreground: "#27342F"
    banner_highlight1: "#764C00"
    banner_highlight2: "#916D07"
    filesize: {||
      if $in < 1kb { "#4A5752"
      } else if $in < 1mb { "#218366"
      } else if $in < 100mb { "#916D07"
      } else if $in < 1gb { "#764C00"
      } else { "#AC3B32" }
    }
    duration: {||
      if $in < 1sec { "#218366"
      } else if $in < 1min { "#916D07"
      } else if $in < 1hr { "#764C00"
      } else { "#AC3B32" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#278D6E"
      } else if $in < 1day { "#218366"
      } else if $in < 1wk { "#916D07"
      } else if $in < 4wk { "#764C00"
      } else if $in < 52wk { "#4A5752"
      } else { "#6C7C76" }
    }
}

$env.config.explore.selected_cell = { fg: "#EEF2F1" bg: "#764C00" }
$env.config.explore.highlight = { fg: "#19221E" bg: "#D2CAAB" }
$env.config.explore.status_bar_text = { fg: "#3B4742" }
$env.config.explore.status_bar_background = { fg: "#27342F" bg: "#D5DBDA" }
$env.config.explore.command_bar_text = { fg: "#27342F" }
$env.config.explore.command_bar_background = { bg: "#D5DBDA" }
$env.config.explore.title_bar_text = { fg: "#19221E" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#C6D2CF" }
$env.config.explore.status = {
    info: { fg: "#25629B" }
    success: { fg: "#EEF2F1" bg: "#218366" }
    warn: { fg: "#EEF2F1" bg: "#916D07" }
    error: { fg: "#EEF2F1" bg: "#AC3B32" }
}
