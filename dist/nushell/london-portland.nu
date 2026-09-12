# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#896800"
    shape_external_resolved: "#896800"
    shape_external: "#C92B23"
    shape_keyword: "#B14A07"
    shape_flag: "#007376"
    shape_externalarg: "#3C4557"
    shape_signature: "#007376"
    shape_string: "#0D8131"
    shape_raw_string: "#0D8131"
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
    shape_pipe: "#B14A07"
    shape_redirection: "#7660AB"
    shape_operator: "#7660AB"
    shape_block: "#556179"
    shape_closure: "#556179"
    shape_list: "#556179"
    shape_record: "#556179"
    shape_table: "#556179"
    shape_match_pattern: "#0D8131"
    shape_matching_brackets: { fg: "#977300" attr: "b" }
    shape_garbage: { fg: "#C92B23" attr: "u" }

    background: "#E8F0FF"
    foreground: "#293040"
    cursor: "#B14A07"
    separator: "#93A7CF"
    leading_trailing_space_bg: { bg: "#A8BBE2" }
    header: { fg: "#B14A07" attr: "b" }
    row_index: "#697794"
    empty: "#8192B4"
    hints: "#8192B4"
    search_result: { fg: "#1B202B" bg: "#CBC7B2" }
    selection: { fg: "#1B202B" bg: "#A8BBE2" }
    selection_cursor: { attr: "n" }
    bool: "#C92B23"
    int: "#C92B23"
    float: "#C92B23"
    string: "#293040"
    glob: "#7660AB"
    binary: "#C92B23"
    binary_null_char: "#8192B4"
    binary_printable: "#0D8131"
    binary_whitespace: "#007376"
    binary_ascii_other: "#7660AB"
    binary_non_ascii: "#B14A07"
    custom: "#7660AB"
    nothing: "#8192B4"
    list: "#293040"
    record: "#293040"
    range: "#7660AB"
    cell-path: "#556179"
    block: "#556179"
    closure: "#556179"
    semver: "#007376"
    semver-range: "#007376"
    banner_foreground: "#293040"
    banner_highlight1: "#B14A07"
    banner_highlight2: "#896800"
    filesize: {||
      if $in < 1kb { "#4A5469"
      } else if $in < 1mb { "#0D8131"
      } else if $in < 100mb { "#896800"
      } else if $in < 1gb { "#B14A07"
      } else { "#C92B23" }
    }
    duration: {||
      if $in < 1sec { "#0D8131"
      } else if $in < 1min { "#896800"
      } else if $in < 1hr { "#B14A07"
      } else { "#C92B23" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#008730"
      } else if $in < 1day { "#0D8131"
      } else if $in < 1wk { "#896800"
      } else if $in < 4wk { "#B14A07"
      } else if $in < 52wk { "#4A5469"
      } else { "#697794" }
    }
}

$env.config.explore.selected_cell = { fg: "#E8F0FF" bg: "#B14A07" }
$env.config.explore.highlight = { fg: "#1B202B" bg: "#CBC7B2" }
$env.config.explore.status_bar_text = { fg: "#3C4557" }
$env.config.explore.status_bar_background = { fg: "#293040" bg: "#CCDAF2" }
$env.config.explore.command_bar_text = { fg: "#293040" }
$env.config.explore.command_bar_background = { bg: "#CCDAF2" }
$env.config.explore.title_bar_text = { fg: "#1B202B" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#BFCFF1" }
$env.config.explore.status = {
    info: { fg: "#0019A8" }
    success: { fg: "#E8F0FF" bg: "#0D8131" }
    warn: { fg: "#E8F0FF" bg: "#896800" }
    error: { fg: "#E8F0FF" bg: "#C92B23" }
}
