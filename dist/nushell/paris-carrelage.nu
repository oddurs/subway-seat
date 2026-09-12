# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#8E6B08"
    shape_external_resolved: "#8E6B08"
    shape_external: "#BE423D"
    shape_keyword: "#804B00"
    shape_flag: "#006E6B"
    shape_externalarg: "#3D473E"
    shape_signature: "#006E6B"
    shape_string: "#207F41"
    shape_raw_string: "#207F41"
    shape_string_interpolation: "#98547C"
    shape_int: "#BE423D"
    shape_float: "#BE423D"
    shape_bool: "#BE423D"
    shape_binary: "#BE423D"
    shape_datetime: "#BE423D"
    shape_nothing: "#BE423D"
    shape_literal: "#BE423D"
    shape_range: "#98547C"
    shape_custom: "#98547C"
    shape_variable: "#98547C"
    shape_vardecl: "#98547C"
    shape_filepath: "#3D473E"
    shape_directory: "#3D473E"
    shape_globpattern: "#98547C"
    shape_glob_interpolation: "#98547C"
    shape_pipe: "#804B00"
    shape_redirection: "#98547C"
    shape_operator: "#98547C"
    shape_block: "#586459"
    shape_closure: "#586459"
    shape_list: "#586459"
    shape_record: "#586459"
    shape_table: "#586459"
    shape_match_pattern: "#207F41"
    shape_matching_brackets: { fg: "#9D770A" attr: "b" }
    shape_garbage: { fg: "#BE423D" attr: "u" }

    background: "#EEF3ED"
    foreground: "#2A342B"
    cursor: "#804B00"
    separator: "#9BAC9A"
    leading_trailing_space_bg: { bg: "#B1C0B0" }
    header: { fg: "#804B00" attr: "b" }
    row_index: "#6E7C6E"
    empty: "#879887"
    hints: "#879887"
    search_result: { fg: "#1B221C" bg: "#D1CAA8" }
    selection: { fg: "#1B221C" bg: "#B1C0B0" }
    selection_cursor: { attr: "n" }
    bool: "#BE423D"
    int: "#BE423D"
    float: "#BE423D"
    string: "#2A342B"
    glob: "#98547C"
    binary: "#BE423D"
    binary_null_char: "#879887"
    binary_printable: "#207F41"
    binary_whitespace: "#006E6B"
    binary_ascii_other: "#98547C"
    binary_non_ascii: "#804B00"
    custom: "#98547C"
    nothing: "#879887"
    list: "#2A342B"
    record: "#2A342B"
    range: "#98547C"
    cell-path: "#586459"
    block: "#586459"
    closure: "#586459"
    semver: "#006E6B"
    semver-range: "#006E6B"
    banner_foreground: "#2A342B"
    banner_highlight1: "#804B00"
    banner_highlight2: "#8E6B08"
    filesize: {||
      if $in < 1kb { "#4C574D"
      } else if $in < 1mb { "#207F41"
      } else if $in < 100mb { "#8E6B08"
      } else if $in < 1gb { "#804B00"
      } else { "#BE423D" }
    }
    duration: {||
      if $in < 1sec { "#207F41"
      } else if $in < 1min { "#8E6B08"
      } else if $in < 1hr { "#804B00"
      } else { "#BE423D" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#168540"
      } else if $in < 1day { "#207F41"
      } else if $in < 1wk { "#8E6B08"
      } else if $in < 4wk { "#804B00"
      } else if $in < 52wk { "#4C574D"
      } else { "#6E7C6E" }
    }
}

$env.config.explore.selected_cell = { fg: "#EEF3ED" bg: "#804B00" }
$env.config.explore.highlight = { fg: "#1B221C" bg: "#D1CAA8" }
$env.config.explore.status_bar_text = { fg: "#3D473E" }
$env.config.explore.status_bar_background = { fg: "#2A342B" bg: "#D4DCD3" }
$env.config.explore.command_bar_text = { fg: "#2A342B" }
$env.config.explore.command_bar_background = { bg: "#D4DCD3" }
$env.config.explore.title_bar_text = { fg: "#1B221C" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#C7D3C5" }
$env.config.explore.status = {
    info: { fg: "#27629C" }
    success: { fg: "#EEF3ED" bg: "#207F41" }
    warn: { fg: "#EEF3ED" bg: "#8E6B08" }
    error: { fg: "#EEF3ED" bg: "#BE423D" }
}
