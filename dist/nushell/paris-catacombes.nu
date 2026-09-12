# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Catacombes for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#EBC342"
    shape_external_resolved: "#EBC342"
    shape_external: "#EF796F"
    shape_keyword: "#D78E3C"
    shape_flag: "#6FB393"
    shape_externalarg: "#B8CAC2"
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
    shape_filepath: "#B8CAC2"
    shape_directory: "#B8CAC2"
    shape_globpattern: "#E783BD"
    shape_glob_interpolation: "#E783BD"
    shape_pipe: "#D78E3C"
    shape_redirection: "#E783BD"
    shape_operator: "#E783BD"
    shape_block: "#829D91"
    shape_closure: "#829D91"
    shape_list: "#829D91"
    shape_record: "#829D91"
    shape_table: "#829D91"
    shape_match_pattern: "#73C686"
    shape_matching_brackets: { fg: "#FBD664" attr: "b" }
    shape_garbage: { fg: "#EF796F" attr: "u" }

    background: "#062017"
    foreground: "#CFDED7"
    cursor: "#EBC342"
    separator: "#1E4738"
    leading_trailing_space_bg: { bg: "#13382A" }
    header: { fg: "#D78E3C" attr: "b" }
    row_index: "#648576"
    empty: "#456A5B"
    hints: "#456A5B"
    search_result: { fg: "#E4EEE9" bg: "#4B5124" }
    selection: { fg: "#E4EEE9" bg: "#1E4738" }
    selection_cursor: { attr: "n" }
    bool: "#EF796F"
    int: "#EF796F"
    float: "#EF796F"
    string: "#CFDED7"
    glob: "#E783BD"
    binary: "#EF796F"
    binary_null_char: "#456A5B"
    binary_printable: "#73C686"
    binary_whitespace: "#6FB393"
    binary_ascii_other: "#E783BD"
    binary_non_ascii: "#D78E3C"
    custom: "#E783BD"
    nothing: "#456A5B"
    list: "#CFDED7"
    record: "#CFDED7"
    range: "#E783BD"
    cell-path: "#829D91"
    block: "#829D91"
    closure: "#829D91"
    semver: "#6FB393"
    semver-range: "#6FB393"
    banner_foreground: "#CFDED7"
    banner_highlight1: "#D78E3C"
    banner_highlight2: "#EBC342"
    filesize: {||
      if $in < 1kb { "#9EB3AA"
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
      } else if $in < 52wk { "#9EB3AA"
      } else { "#648576" }
    }
}

$env.config.explore.selected_cell = { fg: "#05120C" bg: "#D78E3C" }
$env.config.explore.highlight = { fg: "#E4EEE9" bg: "#4B5124" }
$env.config.explore.status_bar_text = { fg: "#B8CAC2" }
$env.config.explore.status_bar_background = { fg: "#CFDED7" bg: "#061811" }
$env.config.explore.command_bar_text = { fg: "#CFDED7" }
$env.config.explore.command_bar_background = { bg: "#061811" }
$env.config.explore.title_bar_text = { fg: "#E4EEE9" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#13382A" }
$env.config.explore.status = {
    info: { fg: "#639BD5" }
    success: { fg: "#05120C" bg: "#73C686" }
    warn: { fg: "#05120C" bg: "#EBC342" }
    error: { fg: "#05120C" bg: "#EF796F" }
}
