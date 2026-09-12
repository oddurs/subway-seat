# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#896800"
    shape_external_resolved: "#896800"
    shape_external: "#C92B23"
    shape_keyword: "#A45600"
    shape_flag: "#007376"
    shape_externalarg: "#3C4557"
    shape_signature: "#007376"
    shape_string: "#00822E"
    shape_raw_string: "#00822E"
    shape_string_interpolation: "#7660AB"
    shape_int: "#C92B23"
    shape_float: "#C92B23"
    shape_bool: "#C92B23"
    shape_binary: "#C92B23"
    shape_datetime: "#C92B23"
    shape_nothing: "#C92B23"
    shape_literal: "#C92B23"
    shape_range: "#7660AB"
    shape_custom: "#7660AB"
    shape_variable: "#7660AB"
    shape_vardecl: "#7660AB"
    shape_filepath: "#3C4557"
    shape_directory: "#3C4557"
    shape_globpattern: "#7660AB"
    shape_glob_interpolation: "#7660AB"
    shape_pipe: "#A45600"
    shape_redirection: "#7660AB"
    shape_operator: "#7660AB"
    shape_block: "#556179"
    shape_closure: "#556179"
    shape_list: "#556179"
    shape_record: "#556179"
    shape_table: "#556179"
    shape_match_pattern: "#00822E"
    shape_matching_brackets: { fg: "#977300" attr: "b" }
    shape_garbage: { fg: "#C92B23" attr: "u" }

    background: "#E5EAF4"
    foreground: "#293040"
    cursor: "#A45600"
    separator: "#95A5C4"
    leading_trailing_space_bg: { bg: "#A9B7D4" }
    header: { fg: "#A45600" attr: "b" }
    row_index: "#697794"
    empty: "#8291AE"
    hints: "#8291AE"
    search_result: { fg: "#1B202B" bg: "#C9C3AB" }
    selection: { fg: "#1B202B" bg: "#A9B7D4" }
    selection_cursor: { attr: "n" }
    bool: "#C92B23"
    int: "#C92B23"
    float: "#C92B23"
    string: "#293040"
    glob: "#7660AB"
    binary: "#C92B23"
    binary_null_char: "#8291AE"
    binary_printable: "#00822E"
    binary_whitespace: "#007376"
    binary_ascii_other: "#7660AB"
    binary_non_ascii: "#A45600"
    custom: "#7660AB"
    nothing: "#8291AE"
    list: "#293040"
    record: "#293040"
    range: "#7660AB"
    cell-path: "#556179"
    block: "#556179"
    closure: "#556179"
    semver: "#007376"
    semver-range: "#007376"
    banner_foreground: "#293040"
    banner_highlight1: "#A45600"
    banner_highlight2: "#896800"
    filesize: {||
      if $in < 1kb { "#4A5469"
      } else if $in < 1mb { "#00822E"
      } else if $in < 100mb { "#896800"
      } else if $in < 1gb { "#A45600"
      } else { "#C92B23" }
    }
    duration: {||
      if $in < 1sec { "#00822E"
      } else if $in < 1min { "#896800"
      } else if $in < 1hr { "#A45600"
      } else { "#C92B23" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#008730"
      } else if $in < 1day { "#00822E"
      } else if $in < 1wk { "#896800"
      } else if $in < 4wk { "#A45600"
      } else if $in < 52wk { "#4A5469"
      } else { "#697794" }
    }
}

$env.config.explore.selected_cell = { fg: "#E5EAF4" bg: "#A45600" }
$env.config.explore.highlight = { fg: "#1B202B" bg: "#C9C3AB" }
$env.config.explore.status_bar_text = { fg: "#3C4557" }
$env.config.explore.status_bar_background = { fg: "#293040" bg: "#CDD5E4" }
$env.config.explore.command_bar_text = { fg: "#293040" }
$env.config.explore.command_bar_background = { bg: "#CDD5E4" }
$env.config.explore.title_bar_text = { fg: "#1B202B" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#BFCAE1" }
$env.config.explore.status = {
    info: { fg: "#0019A8" }
    success: { fg: "#E5EAF4" bg: "#00822E" }
    warn: { fg: "#E5EAF4" bg: "#896800" }
    error: { fg: "#E5EAF4" bg: "#C92B23" }
}
