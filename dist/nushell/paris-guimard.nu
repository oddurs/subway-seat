# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Guimard for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F1BF4B"
    shape_external_resolved: "#F1BF4B"
    shape_external: "#E7877B"
    shape_keyword: "#CA9245"
    shape_flag: "#549B9F"
    shape_externalarg: "#C2CBC5"
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
    shape_filepath: "#C2CBC5"
    shape_directory: "#C2CBC5"
    shape_globpattern: "#FAB49C"
    shape_glob_interpolation: "#FAB49C"
    shape_pipe: "#CA9245"
    shape_redirection: "#FAB49C"
    shape_operator: "#FAB49C"
    shape_block: "#909E96"
    shape_closure: "#909E96"
    shape_list: "#909E96"
    shape_record: "#909E96"
    shape_table: "#909E96"
    shape_match_pattern: "#70CAA9"
    shape_matching_brackets: { fg: "#FFD57A" attr: "b" }
    shape_garbage: { fg: "#E7877B" attr: "u" }

    background: "#1E2E26"
    foreground: "#D9E1DB"
    cursor: "#F1BF4B"
    separator: "#3E554A"
    leading_trailing_space_bg: { bg: "#30463B" }
    header: { fg: "#CA9245" attr: "b" }
    row_index: "#74857C"
    empty: "#586B61"
    hints: "#586B61"
    search_result: { fg: "#E9EEEC" bg: "#5D5A31" }
    selection: { fg: "#E9EEEC" bg: "#3E554A" }
    selection_cursor: { attr: "n" }
    bool: "#E7877B"
    int: "#E7877B"
    float: "#E7877B"
    string: "#D9E1DB"
    glob: "#FAB49C"
    binary: "#E7877B"
    binary_null_char: "#586B61"
    binary_printable: "#70CAA9"
    binary_whitespace: "#549B9F"
    binary_ascii_other: "#FAB49C"
    binary_non_ascii: "#CA9245"
    custom: "#FAB49C"
    nothing: "#586B61"
    list: "#D9E1DB"
    record: "#D9E1DB"
    range: "#FAB49C"
    cell-path: "#909E96"
    block: "#909E96"
    closure: "#909E96"
    semver: "#549B9F"
    semver-range: "#549B9F"
    banner_foreground: "#D9E1DB"
    banner_highlight1: "#CA9245"
    banner_highlight2: "#F1BF4B"
    filesize: {||
      if $in < 1kb { "#A9B5AE"
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
      } else if $in < 52wk { "#A9B5AE"
      } else { "#74857C" }
    }
}

$env.config.explore.selected_cell = { fg: "#131A17" bg: "#CA9245" }
$env.config.explore.highlight = { fg: "#E9EEEC" bg: "#5D5A31" }
$env.config.explore.status_bar_text = { fg: "#C2CBC5" }
$env.config.explore.status_bar_background = { fg: "#D9E1DB" bg: "#18241D" }
$env.config.explore.command_bar_text = { fg: "#D9E1DB" }
$env.config.explore.command_bar_background = { bg: "#18241D" }
$env.config.explore.title_bar_text = { fg: "#E9EEEC" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#30463B" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#131A17" bg: "#70CAA9" }
    warn: { fg: "#131A17" bg: "#F1BF4B" }
    error: { fg: "#131A17" bg: "#E7877B" }
}
