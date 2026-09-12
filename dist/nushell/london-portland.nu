# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#8D6C08"
    shape_external_resolved: "#8D6C08"
    shape_external: "#CC2E25"
    shape_keyword: "#A54300"
    shape_flag: "#007376"
    shape_externalarg: "#3C4557"
    shape_signature: "#007376"
    shape_string: "#0D8131"
    shape_raw_string: "#0D8131"
    shape_string_interpolation: "#755FA9"
    shape_int: "#CC2E25"
    shape_float: "#CC2E25"
    shape_bool: "#CC2E25"
    shape_binary: "#CC2E25"
    shape_datetime: "#CC2E25"
    shape_nothing: "#CC2E25"
    shape_literal: "#CC2E25"
    shape_range: "#755FA9"
    shape_custom: "#755FA9"
    shape_variable: "#755FA9"
    shape_vardecl: "#755FA9"
    shape_filepath: "#3C4557"
    shape_directory: "#3C4557"
    shape_globpattern: "#755FA9"
    shape_glob_interpolation: "#755FA9"
    shape_pipe: "#A54300"
    shape_redirection: "#755FA9"
    shape_operator: "#755FA9"
    shape_block: "#556179"
    shape_closure: "#556179"
    shape_list: "#556179"
    shape_record: "#556179"
    shape_table: "#556179"
    shape_match_pattern: "#0D8131"
    shape_matching_brackets: { fg: "#9B770A" attr: "b" }
    shape_garbage: { fg: "#CC2E25" attr: "u" }

    background: "#E8F0FF"
    foreground: "#293040"
    cursor: "#A54300"
    separator: "#93A7CF"
    leading_trailing_space_bg: { bg: "#A8BBE2" }
    header: { fg: "#A54300" attr: "b" }
    row_index: "#697794"
    empty: "#8192B4"
    hints: "#8192B4"
    search_result: { fg: "#1B202B" bg: "#CDC8B5" }
    selection: { fg: "#1B202B" bg: "#A8BBE2" }
    selection_cursor: { attr: "n" }
    bool: "#CC2E25"
    int: "#CC2E25"
    float: "#CC2E25"
    string: "#293040"
    glob: "#755FA9"
    binary: "#CC2E25"
    binary_null_char: "#8192B4"
    binary_printable: "#0D8131"
    binary_whitespace: "#007376"
    binary_ascii_other: "#755FA9"
    binary_non_ascii: "#A54300"
    custom: "#755FA9"
    nothing: "#8192B4"
    list: "#293040"
    record: "#293040"
    range: "#755FA9"
    cell-path: "#556179"
    block: "#556179"
    closure: "#556179"
    semver: "#007376"
    semver-range: "#007376"
    banner_foreground: "#293040"
    banner_highlight1: "#A54300"
    banner_highlight2: "#8D6C08"
    filesize: {||
      if $in < 1kb { "#4A5469"
      } else if $in < 1mb { "#0D8131"
      } else if $in < 100mb { "#8D6C08"
      } else if $in < 1gb { "#A54300"
      } else { "#CC2E25" }
    }
    duration: {||
      if $in < 1sec { "#0D8131"
      } else if $in < 1min { "#8D6C08"
      } else if $in < 1hr { "#A54300"
      } else { "#CC2E25" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#008730"
      } else if $in < 1day { "#0D8131"
      } else if $in < 1wk { "#8D6C08"
      } else if $in < 4wk { "#A54300"
      } else if $in < 52wk { "#4A5469"
      } else { "#697794" }
    }
}

$env.config.explore.selected_cell = { fg: "#E8F0FF" bg: "#A54300" }
$env.config.explore.highlight = { fg: "#1B202B" bg: "#CDC8B5" }
$env.config.explore.status_bar_text = { fg: "#3C4557" }
$env.config.explore.status_bar_background = { fg: "#293040" bg: "#CCDAF2" }
$env.config.explore.command_bar_text = { fg: "#293040" }
$env.config.explore.command_bar_background = { bg: "#CCDAF2" }
$env.config.explore.title_bar_text = { fg: "#1B202B" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#BFCFF1" }
$env.config.explore.status = {
    info: { fg: "#0019A8" }
    success: { fg: "#E8F0FF" bg: "#0D8131" }
    warn: { fg: "#E8F0FF" bg: "#8D6C08" }
    error: { fg: "#E8F0FF" bg: "#CC2E25" }
}
