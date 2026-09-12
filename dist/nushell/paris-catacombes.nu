# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F2BF4B"
    shape_external_resolved: "#F2BF4B"
    shape_external: "#EE8F85"
    shape_keyword: "#D0914F"
    shape_flag: "#5FA09D"
    shape_externalarg: "#BFC8C2"
    shape_signature: "#5FA09D"
    shape_string: "#80C28E"
    shape_raw_string: "#80C28E"
    shape_string_interpolation: "#CE96B4"
    shape_int: "#EE8F85"
    shape_float: "#EE8F85"
    shape_bool: "#EE8F85"
    shape_binary: "#EE8F85"
    shape_datetime: "#EE8F85"
    shape_nothing: "#EE8F85"
    shape_literal: "#EE8F85"
    shape_range: "#CE96B4"
    shape_custom: "#CE96B4"
    shape_variable: "#CE96B4"
    shape_vardecl: "#CE96B4"
    shape_filepath: "#BFC8C2"
    shape_directory: "#BFC8C2"
    shape_globpattern: "#CE96B4"
    shape_glob_interpolation: "#CE96B4"
    shape_pipe: "#D0914F"
    shape_redirection: "#CE96B4"
    shape_operator: "#CE96B4"
    shape_block: "#8C9A92"
    shape_closure: "#8C9A92"
    shape_list: "#8C9A92"
    shape_record: "#8C9A92"
    shape_table: "#8C9A92"
    shape_match_pattern: "#80C28E"
    shape_matching_brackets: { fg: "#FFD273" attr: "b" }
    shape_garbage: { fg: "#EE8F85" attr: "u" }

    background: "#121E19"
    foreground: "#D4DDD7"
    cursor: "#F2BF4B"
    separator: "#31433A"
    leading_trailing_space_bg: { bg: "#24342C" }
    header: { fg: "#D0914F" attr: "b" }
    row_index: "#708178"
    empty: "#54655C"
    hints: "#54655C"
    search_result: { fg: "#E7ECEA" bg: "#554E28" }
    selection: { fg: "#E7ECEA" bg: "#31433A" }
    selection_cursor: { attr: "n" }
    bool: "#EE8F85"
    int: "#EE8F85"
    float: "#EE8F85"
    string: "#D4DDD7"
    glob: "#CE96B4"
    binary: "#EE8F85"
    binary_null_char: "#54655C"
    binary_printable: "#80C28E"
    binary_whitespace: "#5FA09D"
    binary_ascii_other: "#CE96B4"
    binary_non_ascii: "#D0914F"
    custom: "#CE96B4"
    nothing: "#54655C"
    list: "#D4DDD7"
    record: "#D4DDD7"
    range: "#CE96B4"
    cell-path: "#8C9A92"
    block: "#8C9A92"
    closure: "#8C9A92"
    semver: "#5FA09D"
    semver-range: "#5FA09D"
    banner_foreground: "#D4DDD7"
    banner_highlight1: "#D0914F"
    banner_highlight2: "#F2BF4B"
    filesize: {||
      if $in < 1kb { "#A5B1AA"
      } else if $in < 1mb { "#80C28E"
      } else if $in < 100mb { "#F2BF4B"
      } else if $in < 1gb { "#D0914F"
      } else { "#EE8F85" }
    }
    duration: {||
      if $in < 1sec { "#80C28E"
      } else if $in < 1min { "#F2BF4B"
      } else if $in < 1hr { "#D0914F"
      } else { "#EE8F85" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#8FD59E"
      } else if $in < 1day { "#80C28E"
      } else if $in < 1wk { "#F2BF4B"
      } else if $in < 4wk { "#D0914F"
      } else if $in < 52wk { "#A5B1AA"
      } else { "#708178" }
    }
}

$env.config.explore.selected_cell = { fg: "#0A100D" bg: "#D0914F" }
$env.config.explore.highlight = { fg: "#E7ECEA" bg: "#554E28" }
$env.config.explore.status_bar_text = { fg: "#BFC8C2" }
$env.config.explore.status_bar_background = { fg: "#D4DDD7" bg: "#0D1711" }
$env.config.explore.command_bar_text = { fg: "#D4DDD7" }
$env.config.explore.command_bar_background = { bg: "#0D1711" }
$env.config.explore.title_bar_text = { fg: "#E7ECEA" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#24342C" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#0A100D" bg: "#80C28E" }
    warn: { fg: "#0A100D" bg: "#F2BF4B" }
    error: { fg: "#0A100D" bg: "#EE8F85" }
}
