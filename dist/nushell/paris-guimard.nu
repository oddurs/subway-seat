# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Guimard for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#EBC168"
    shape_external_resolved: "#EBC168"
    shape_external: "#E1837A"
    shape_keyword: "#D0914F"
    shape_flag: "#7BB096"
    shape_externalarg: "#C3CAC6"
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
    shape_filepath: "#C3CAC6"
    shape_directory: "#C3CAC6"
    shape_globpattern: "#CE96B4"
    shape_glob_interpolation: "#CE96B4"
    shape_pipe: "#D0914F"
    shape_redirection: "#CE96B4"
    shape_operator: "#CE96B4"
    shape_block: "#929D97"
    shape_closure: "#929D97"
    shape_list: "#929D97"
    shape_record: "#929D97"
    shape_table: "#929D97"
    shape_match_pattern: "#80C28E"
    shape_matching_brackets: { fg: "#FBD380" attr: "b" }
    shape_garbage: { fg: "#E1837A" attr: "u" }

    background: "#212D27"
    foreground: "#DAE0DC"
    cursor: "#EBC168"
    separator: "#42544B"
    leading_trailing_space_bg: { bg: "#34453C" }
    header: { fg: "#D0914F" attr: "b" }
    row_index: "#77847D"
    empty: "#5B6A62"
    hints: "#5B6A62"
    search_result: { fg: "#EAEEEC" bg: "#5E593A" }
    selection: { fg: "#EAEEEC" bg: "#42544B" }
    selection_cursor: { attr: "n" }
    bool: "#E1837A"
    int: "#E1837A"
    float: "#E1837A"
    string: "#DAE0DC"
    glob: "#CE96B4"
    binary: "#E1837A"
    binary_null_char: "#5B6A62"
    binary_printable: "#80C28E"
    binary_whitespace: "#7BB096"
    binary_ascii_other: "#CE96B4"
    binary_non_ascii: "#D0914F"
    custom: "#CE96B4"
    nothing: "#5B6A62"
    list: "#DAE0DC"
    record: "#DAE0DC"
    range: "#CE96B4"
    cell-path: "#929D97"
    block: "#929D97"
    closure: "#929D97"
    semver: "#7BB096"
    semver-range: "#7BB096"
    banner_foreground: "#DAE0DC"
    banner_highlight1: "#D0914F"
    banner_highlight2: "#EBC168"
    filesize: {||
      if $in < 1kb { "#ABB4AF"
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
      } else if $in < 52wk { "#ABB4AF"
      } else { "#77847D" }
    }
}

$env.config.explore.selected_cell = { fg: "#141A17" bg: "#D0914F" }
$env.config.explore.highlight = { fg: "#EAEEEC" bg: "#5E593A" }
$env.config.explore.status_bar_text = { fg: "#C3CAC6" }
$env.config.explore.status_bar_background = { fg: "#DAE0DC" bg: "#1A231E" }
$env.config.explore.command_bar_text = { fg: "#DAE0DC" }
$env.config.explore.command_bar_background = { bg: "#1A231E" }
$env.config.explore.title_bar_text = { fg: "#EAEEEC" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#34453C" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#141A17" bg: "#80C28E" }
    warn: { fg: "#141A17" bg: "#EBC168" }
    error: { fg: "#141A17" bg: "#E1837A" }
}
