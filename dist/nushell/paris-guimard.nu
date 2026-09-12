# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Guimard for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#EBC168"
    shape_external_resolved: "#EBC168"
    shape_external: "#E1837A"
    shape_keyword: "#D0914F"
    shape_flag: "#6CA087"
    shape_externalarg: "#C2CBC5"
    shape_signature: "#6CA087"
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
    shape_filepath: "#C2CBC5"
    shape_directory: "#C2CBC5"
    shape_globpattern: "#CE96B4"
    shape_glob_interpolation: "#CE96B4"
    shape_pipe: "#D0914F"
    shape_redirection: "#CE96B4"
    shape_operator: "#CE96B4"
    shape_block: "#909E96"
    shape_closure: "#909E96"
    shape_list: "#909E96"
    shape_record: "#909E96"
    shape_table: "#909E96"
    shape_match_pattern: "#80C28E"
    shape_matching_brackets: { fg: "#FBD380" attr: "b" }
    shape_garbage: { fg: "#E1837A" attr: "u" }

    background: "#1E2E26"
    foreground: "#D9E1DB"
    cursor: "#EBC168"
    separator: "#3E554A"
    leading_trailing_space_bg: { bg: "#30463B" }
    header: { fg: "#D0914F" attr: "b" }
    row_index: "#74857C"
    empty: "#586B61"
    hints: "#586B61"
    search_result: { fg: "#E9EEEC" bg: "#5C5A3A" }
    selection: { fg: "#E9EEEC" bg: "#3E554A" }
    selection_cursor: { attr: "n" }
    bool: "#E1837A"
    int: "#E1837A"
    float: "#E1837A"
    string: "#D9E1DB"
    glob: "#CE96B4"
    binary: "#E1837A"
    binary_null_char: "#586B61"
    binary_printable: "#80C28E"
    binary_whitespace: "#6CA087"
    binary_ascii_other: "#CE96B4"
    binary_non_ascii: "#D0914F"
    custom: "#CE96B4"
    nothing: "#586B61"
    list: "#D9E1DB"
    record: "#D9E1DB"
    range: "#CE96B4"
    cell-path: "#909E96"
    block: "#909E96"
    closure: "#909E96"
    semver: "#6CA087"
    semver-range: "#6CA087"
    banner_foreground: "#D9E1DB"
    banner_highlight1: "#D0914F"
    banner_highlight2: "#EBC168"
    filesize: {||
      if $in < 1kb { "#A9B5AE"
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
      } else if $in < 52wk { "#A9B5AE"
      } else { "#74857C" }
    }
}

$env.config.explore.selected_cell = { fg: "#131A17" bg: "#D0914F" }
$env.config.explore.highlight = { fg: "#E9EEEC" bg: "#5C5A3A" }
$env.config.explore.status_bar_text = { fg: "#C2CBC5" }
$env.config.explore.status_bar_background = { fg: "#D9E1DB" bg: "#18241D" }
$env.config.explore.command_bar_text = { fg: "#D9E1DB" }
$env.config.explore.command_bar_background = { bg: "#18241D" }
$env.config.explore.title_bar_text = { fg: "#E9EEEC" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#30463B" }
$env.config.explore.status = {
    info: { fg: "#709BC8" }
    success: { fg: "#131A17" bg: "#80C28E" }
    warn: { fg: "#131A17" bg: "#EBC168" }
    error: { fg: "#131A17" bg: "#E1837A" }
}
