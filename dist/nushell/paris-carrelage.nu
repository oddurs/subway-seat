# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#8A6700"
    shape_external_resolved: "#8A6700"
    shape_external: "#BB403B"
    shape_keyword: "#8A5308"
    shape_flag: "#0B714D"
    shape_externalarg: "#3D473E"
    shape_signature: "#0B714D"
    shape_string: "#207F41"
    shape_raw_string: "#207F41"
    shape_string_interpolation: "#9A557D"
    shape_int: "#BB403B"
    shape_float: "#BB403B"
    shape_bool: "#BB403B"
    shape_binary: "#BB403B"
    shape_datetime: "#BB403B"
    shape_nothing: "#BB403B"
    shape_literal: "#BB403B"
    shape_range: "#9A557D"
    shape_custom: "#9A557D"
    shape_variable: "#9A557D"
    shape_vardecl: "#9A557D"
    shape_filepath: "#3D473E"
    shape_directory: "#3D473E"
    shape_globpattern: "#9A557D"
    shape_glob_interpolation: "#9A557D"
    shape_pipe: "#8A5308"
    shape_redirection: "#9A557D"
    shape_operator: "#9A557D"
    shape_block: "#586459"
    shape_closure: "#586459"
    shape_list: "#586459"
    shape_record: "#586459"
    shape_table: "#586459"
    shape_match_pattern: "#207F41"
    shape_matching_brackets: { fg: "#997300" attr: "b" }
    shape_garbage: { fg: "#BB403B" attr: "u" }

    background: "#EEF3ED"
    foreground: "#2A342B"
    cursor: "#8A5308"
    separator: "#9BAC9A"
    leading_trailing_space_bg: { bg: "#B1C0B0" }
    header: { fg: "#8A5308" attr: "b" }
    row_index: "#6E7C6E"
    empty: "#879887"
    hints: "#879887"
    search_result: { fg: "#1B221C" bg: "#D0C9A6" }
    selection: { fg: "#1B221C" bg: "#B1C0B0" }
    selection_cursor: { attr: "n" }
    bool: "#BB403B"
    int: "#BB403B"
    float: "#BB403B"
    string: "#2A342B"
    glob: "#9A557D"
    binary: "#BB403B"
    binary_null_char: "#879887"
    binary_printable: "#207F41"
    binary_whitespace: "#0B714D"
    binary_ascii_other: "#9A557D"
    binary_non_ascii: "#8A5308"
    custom: "#9A557D"
    nothing: "#879887"
    list: "#2A342B"
    record: "#2A342B"
    range: "#9A557D"
    cell-path: "#586459"
    block: "#586459"
    closure: "#586459"
    semver: "#0B714D"
    semver-range: "#0B714D"
    banner_foreground: "#2A342B"
    banner_highlight1: "#8A5308"
    banner_highlight2: "#8A6700"
    filesize: {||
      if $in < 1kb { "#4C574D"
      } else if $in < 1mb { "#207F41"
      } else if $in < 100mb { "#8A6700"
      } else if $in < 1gb { "#8A5308"
      } else { "#BB403B" }
    }
    duration: {||
      if $in < 1sec { "#207F41"
      } else if $in < 1min { "#8A6700"
      } else if $in < 1hr { "#8A5308"
      } else { "#BB403B" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#168540"
      } else if $in < 1day { "#207F41"
      } else if $in < 1wk { "#8A6700"
      } else if $in < 4wk { "#8A5308"
      } else if $in < 52wk { "#4C574D"
      } else { "#6E7C6E" }
    }
}

$env.config.explore.selected_cell = { fg: "#EEF3ED" bg: "#8A5308" }
$env.config.explore.highlight = { fg: "#1B221C" bg: "#D0C9A6" }
$env.config.explore.status_bar_text = { fg: "#3D473E" }
$env.config.explore.status_bar_background = { fg: "#2A342B" bg: "#D4DCD3" }
$env.config.explore.command_bar_text = { fg: "#2A342B" }
$env.config.explore.command_bar_background = { bg: "#D4DCD3" }
$env.config.explore.title_bar_text = { fg: "#1B221C" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#C7D3C5" }
$env.config.explore.status = {
    info: { fg: "#27629C" }
    success: { fg: "#EEF3ED" bg: "#207F41" }
    warn: { fg: "#EEF3ED" bg: "#8A6700" }
    error: { fg: "#EEF3ED" bg: "#BB403B" }
}
