# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Guimard for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#EBC342"
    shape_external_resolved: "#EBC342"
    shape_external: "#EF796F"
    shape_keyword: "#D78E3C"
    shape_flag: "#6FB393"
    shape_externalarg: "#BBCDC5"
    shape_signature: "#6FB393"
    shape_string: "#73C686"
    shape_raw_string: "#73C686"
    shape_string_interpolation: "#E783BD"
    shape_int: "#EF796F"
    shape_float: "#EF796F"
    shape_bool: "#EF796F"
    shape_binary: "#EF796F"
    shape_datetime: "#EF796F"
    shape_nothing: "#EF796F"
    shape_literal: "#EF796F"
    shape_range: "#E783BD"
    shape_custom: "#E783BD"
    shape_variable: "#E783BD"
    shape_vardecl: "#E783BD"
    shape_filepath: "#BBCDC5"
    shape_directory: "#BBCDC5"
    shape_globpattern: "#E783BD"
    shape_glob_interpolation: "#E783BD"
    shape_pipe: "#D78E3C"
    shape_redirection: "#E783BD"
    shape_operator: "#E783BD"
    shape_block: "#86A195"
    shape_closure: "#86A195"
    shape_list: "#86A195"
    shape_record: "#86A195"
    shape_table: "#86A195"
    shape_match_pattern: "#73C686"
    shape_matching_brackets: { fg: "#FBD664" attr: "b" }
    shape_garbage: { fg: "#EF796F" attr: "u" }

    background: "#0E3125"
    foreground: "#D3E2DB"
    cursor: "#EBC342"
    separator: "#285A47"
    leading_trailing_space_bg: { bg: "#194A39" }
    header: { fg: "#D78E3C" attr: "b" }
    row_index: "#67897A"
    empty: "#47705F"
    hints: "#47705F"
    search_result: { fg: "#E6F0EB" bg: "#505D2E" }
    selection: { fg: "#E6F0EB" bg: "#285A47" }
    selection_cursor: { attr: "n" }
    bool: "#EF796F"
    int: "#EF796F"
    float: "#EF796F"
    string: "#D3E2DB"
    glob: "#E783BD"
    binary: "#EF796F"
    binary_null_char: "#47705F"
    binary_printable: "#73C686"
    binary_whitespace: "#6FB393"
    binary_ascii_other: "#E783BD"
    binary_non_ascii: "#D78E3C"
    custom: "#E783BD"
    nothing: "#47705F"
    list: "#D3E2DB"
    record: "#D3E2DB"
    range: "#E783BD"
    cell-path: "#86A195"
    block: "#86A195"
    closure: "#86A195"
    semver: "#6FB393"
    semver-range: "#6FB393"
    banner_foreground: "#D3E2DB"
    banner_highlight1: "#D78E3C"
    banner_highlight2: "#EBC342"
    filesize: {||
      if $in < 1kb { "#A2B7AE"
      } else if $in < 1mb { "#73C686"
      } else if $in < 100mb { "#EBC342"
      } else if $in < 1gb { "#D78E3C"
      } else { "#EF796F" }
    }
    duration: {||
      if $in < 1sec { "#73C686"
      } else if $in < 1min { "#EBC342"
      } else if $in < 1hr { "#D78E3C"
      } else { "#EF796F" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#82D896"
      } else if $in < 1day { "#73C686"
      } else if $in < 1wk { "#EBC342"
      } else if $in < 4wk { "#D78E3C"
      } else if $in < 52wk { "#A2B7AE"
      } else { "#67897A" }
    }
}

$env.config.explore.selected_cell = { fg: "#0A1D15" bg: "#D78E3C" }
$env.config.explore.highlight = { fg: "#E6F0EB" bg: "#505D2E" }
$env.config.explore.status_bar_text = { fg: "#BBCDC5" }
$env.config.explore.status_bar_background = { fg: "#D3E2DB" bg: "#0C261C" }
$env.config.explore.command_bar_text = { fg: "#D3E2DB" }
$env.config.explore.command_bar_background = { bg: "#0C261C" }
$env.config.explore.title_bar_text = { fg: "#E6F0EB" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#194A39" }
$env.config.explore.status = {
    info: { fg: "#639BD5" }
    success: { fg: "#0A1D15" bg: "#73C686" }
    warn: { fg: "#0A1D15" bg: "#EBC342" }
    error: { fg: "#0A1D15" bg: "#EF796F" }
}
