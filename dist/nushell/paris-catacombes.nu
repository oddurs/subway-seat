# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F1BF4B"
    shape_external_resolved: "#F1BF4B"
    shape_external: "#E7877B"
    shape_keyword: "#CA9245"
    shape_flag: "#549B9F"
    shape_externalarg: "#BFC8C2"
    shape_signature: "#549B9F"
    shape_string: "#70CAA9"
    shape_raw_string: "#70CAA9"
    shape_string_interpolation: "#FAB49C"
    shape_int: "#E7877B"
    shape_float: "#E7877B"
    shape_bool: "#E7877B"
    shape_binary: "#E7877B"
    shape_datetime: "#E7877B"
    shape_nothing: "#E7877B"
    shape_literal: "#E7877B"
    shape_range: "#FAB49C"
    shape_custom: "#FAB49C"
    shape_variable: "#FAB49C"
    shape_vardecl: "#FAB49C"
    shape_filepath: "#BFC8C2"
    shape_directory: "#BFC8C2"
    shape_globpattern: "#FAB49C"
    shape_glob_interpolation: "#FAB49C"
    shape_pipe: "#CA9245"
    shape_redirection: "#FAB49C"
    shape_operator: "#FAB49C"
    shape_block: "#8C9A92"
    shape_closure: "#8C9A92"
    shape_list: "#8C9A92"
    shape_record: "#8C9A92"
    shape_table: "#8C9A92"
    shape_match_pattern: "#70CAA9"
    shape_matching_brackets: { fg: "#FFD57A" attr: "b" }
    shape_garbage: { fg: "#E7877B" attr: "u" }

    background: "#121E19"
    foreground: "#D4DDD7"
    cursor: "#F1BF4B"
    separator: "#31433A"
    leading_trailing_space_bg: { bg: "#24342C" }
    header: { fg: "#CA9245" attr: "b" }
    row_index: "#708178"
    empty: "#54655C"
    hints: "#54655C"
    search_result: { fg: "#E7ECEA" bg: "#554E28" }
    selection: { fg: "#E7ECEA" bg: "#31433A" }
    selection_cursor: { attr: "n" }
    bool: "#E7877B"
    int: "#E7877B"
    float: "#E7877B"
    string: "#D4DDD7"
    glob: "#FAB49C"
    binary: "#E7877B"
    binary_null_char: "#54655C"
    binary_printable: "#70CAA9"
    binary_whitespace: "#549B9F"
    binary_ascii_other: "#FAB49C"
    binary_non_ascii: "#CA9245"
    custom: "#FAB49C"
    nothing: "#54655C"
    list: "#D4DDD7"
    record: "#D4DDD7"
    range: "#FAB49C"
    cell-path: "#8C9A92"
    block: "#8C9A92"
    closure: "#8C9A92"
    semver: "#549B9F"
    semver-range: "#549B9F"
    banner_foreground: "#D4DDD7"
    banner_highlight1: "#CA9245"
    banner_highlight2: "#F1BF4B"
    filesize: {||
      if $in < 1kb { "#A5B1AA"
      } else if $in < 1mb { "#70CAA9"
      } else if $in < 100mb { "#F1BF4B"
      } else if $in < 1gb { "#CA9245"
      } else { "#E7877B" }
    }
    duration: {||
      if $in < 1sec { "#70CAA9"
      } else if $in < 1min { "#F1BF4B"
      } else if $in < 1hr { "#CA9245"
      } else { "#E7877B" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#89DEBE"
      } else if $in < 1day { "#70CAA9"
      } else if $in < 1wk { "#F1BF4B"
      } else if $in < 4wk { "#CA9245"
      } else if $in < 52wk { "#A5B1AA"
      } else { "#708178" }
    }
}

$env.config.explore.selected_cell = { fg: "#0A100D" bg: "#CA9245" }
$env.config.explore.highlight = { fg: "#E7ECEA" bg: "#554E28" }
$env.config.explore.status_bar_text = { fg: "#BFC8C2" }
$env.config.explore.status_bar_background = { fg: "#D4DDD7" bg: "#0D1711" }
$env.config.explore.command_bar_text = { fg: "#D4DDD7" }
$env.config.explore.command_bar_background = { bg: "#0D1711" }
$env.config.explore.title_bar_text = { fg: "#E7ECEA" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#24342C" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#0A100D" bg: "#70CAA9" }
    warn: { fg: "#0A100D" bg: "#F1BF4B" }
    error: { fg: "#0A100D" bg: "#E7877B" }
}
