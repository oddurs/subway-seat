# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#EBC168"
    shape_external_resolved: "#EBC168"
    shape_external: "#E1837A"
    shape_keyword: "#D0914F"
    shape_flag: "#7BB096"
    shape_externalarg: "#C0C7C3"
    shape_signature: "#7BB096"
    shape_string: "#80C28E"
    shape_raw_string: "#80C28E"
    shape_string_interpolation: "#CE96B4"
    shape_int: "#E1837A"
    shape_float: "#E1837A"
    shape_bool: "#E1837A"
    shape_binary: "#E1837A"
    shape_datetime: "#E1837A"
    shape_nothing: "#E1837A"
    shape_literal: "#E1837A"
    shape_range: "#CE96B4"
    shape_custom: "#CE96B4"
    shape_variable: "#CE96B4"
    shape_vardecl: "#CE96B4"
    shape_filepath: "#C0C7C3"
    shape_directory: "#C0C7C3"
    shape_globpattern: "#CE96B4"
    shape_glob_interpolation: "#CE96B4"
    shape_pipe: "#D0914F"
    shape_redirection: "#CE96B4"
    shape_operator: "#CE96B4"
    shape_block: "#8E9993"
    shape_closure: "#8E9993"
    shape_list: "#8E9993"
    shape_record: "#8E9993"
    shape_table: "#8E9993"
    shape_match_pattern: "#80C28E"
    shape_matching_brackets: { fg: "#FBD380" attr: "b" }
    shape_garbage: { fg: "#E1837A" attr: "u" }

    background: "#141D19"
    foreground: "#D5DCD8"
    cursor: "#EBC168"
    separator: "#34423B"
    leading_trailing_space_bg: { bg: "#27332D" }
    header: { fg: "#D0914F" attr: "b" }
    row_index: "#738079"
    empty: "#57645D"
    hints: "#57645D"
    search_result: { fg: "#E8ECEA" bg: "#544E31" }
    selection: { fg: "#E8ECEA" bg: "#34423B" }
    selection_cursor: { attr: "n" }
    bool: "#E1837A"
    int: "#E1837A"
    float: "#E1837A"
    string: "#D5DCD8"
    glob: "#CE96B4"
    binary: "#E1837A"
    binary_null_char: "#57645D"
    binary_printable: "#80C28E"
    binary_whitespace: "#7BB096"
    binary_ascii_other: "#CE96B4"
    binary_non_ascii: "#D0914F"
    custom: "#CE96B4"
    nothing: "#57645D"
    list: "#D5DCD8"
    record: "#D5DCD8"
    range: "#CE96B4"
    cell-path: "#8E9993"
    block: "#8E9993"
    closure: "#8E9993"
    semver: "#7BB096"
    semver-range: "#7BB096"
    banner_foreground: "#D5DCD8"
    banner_highlight1: "#D0914F"
    banner_highlight2: "#EBC168"
    filesize: {||
      if $in < 1kb { "#A7B0AB"
      } else if $in < 1mb { "#80C28E"
      } else if $in < 100mb { "#EBC168"
      } else if $in < 1gb { "#D0914F"
      } else { "#E1837A" }
    }
    duration: {||
      if $in < 1sec { "#80C28E"
      } else if $in < 1min { "#EBC168"
      } else if $in < 1hr { "#D0914F"
      } else { "#E1837A" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#8FD59E"
      } else if $in < 1day { "#80C28E"
      } else if $in < 1wk { "#EBC168"
      } else if $in < 4wk { "#D0914F"
      } else if $in < 52wk { "#A7B0AB"
      } else { "#738079" }
    }
}

$env.config.explore.selected_cell = { fg: "#0B100D" bg: "#D0914F" }
$env.config.explore.highlight = { fg: "#E8ECEA" bg: "#544E31" }
$env.config.explore.status_bar_text = { fg: "#C0C7C3" }
$env.config.explore.status_bar_background = { fg: "#D5DCD8" bg: "#0F1612" }
$env.config.explore.command_bar_text = { fg: "#D5DCD8" }
$env.config.explore.command_bar_background = { bg: "#0F1612" }
$env.config.explore.title_bar_text = { fg: "#E8ECEA" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#27332D" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#0B100D" bg: "#80C28E" }
    warn: { fg: "#0B100D" bg: "#EBC168" }
    error: { fg: "#0B100D" bg: "#E1837A" }
}
