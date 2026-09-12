# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# Paris Carrelage for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#8A6700"
    shape_external_resolved: "#8A6700"
    shape_external: "#BB403B"
    shape_keyword: "#754500"
    shape_flag: "#086142"
    shape_externalarg: "#374940"
    shape_signature: "#086142"
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
    shape_filepath: "#374940"
    shape_directory: "#374940"
    shape_globpattern: "#9A557D"
    shape_glob_interpolation: "#9A557D"
    shape_pipe: "#754500"
    shape_redirection: "#9A557D"
    shape_operator: "#9A557D"
    shape_block: "#4F675B"
    shape_closure: "#4F675B"
    shape_list: "#4F675B"
    shape_record: "#4F675B"
    shape_table: "#4F675B"
    shape_match_pattern: "#207F41"
    shape_matching_brackets: { fg: "#997300" attr: "b" }
    shape_garbage: { fg: "#BB403B" attr: "u" }

    background: "#E7F5ED"
    foreground: "#25352C"
    cursor: "#754500"
    separator: "#89B19D"
    leading_trailing_space_bg: { bg: "#9FC6B1" }
    header: { fg: "#754500" attr: "b" }
    row_index: "#627F70"
    empty: "#789C88"
    hints: "#789C88"
    search_result: { fg: "#18231D" bg: "#CBCAA6" }
    selection: { fg: "#18231D" bg: "#9FC6B1" }
    selection_cursor: { attr: "n" }
    bool: "#BB403B"
    int: "#BB403B"
    float: "#BB403B"
    string: "#25352C"
    glob: "#9A557D"
    binary: "#BB403B"
    binary_null_char: "#789C88"
    binary_printable: "#207F41"
    binary_whitespace: "#086142"
    binary_ascii_other: "#9A557D"
    binary_non_ascii: "#754500"
    custom: "#9A557D"
    nothing: "#789C88"
    list: "#25352C"
    record: "#25352C"
    range: "#9A557D"
    cell-path: "#4F675B"
    block: "#4F675B"
    closure: "#4F675B"
    semver: "#086142"
    semver-range: "#086142"
    banner_foreground: "#25352C"
    banner_highlight1: "#754500"
    banner_highlight2: "#8A6700"
    filesize: {||
      if $in < 1kb { "#45594F"
      } else if $in < 1mb { "#207F41"
      } else if $in < 100mb { "#8A6700"
      } else if $in < 1gb { "#754500"
      } else { "#BB403B" }
    }
    duration: {||
      if $in < 1sec { "#207F41"
      } else if $in < 1min { "#8A6700"
      } else if $in < 1hr { "#754500"
      } else { "#BB403B" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#168540"
      } else if $in < 1day { "#207F41"
      } else if $in < 1wk { "#8A6700"
      } else if $in < 4wk { "#754500"
      } else if $in < 52wk { "#45594F"
      } else { "#627F70" }
    }
}

$env.config.explore.selected_cell = { fg: "#E7F5ED" bg: "#754500" }
$env.config.explore.highlight = { fg: "#18231D" bg: "#CBCAA6" }
$env.config.explore.status_bar_text = { fg: "#374940" }
$env.config.explore.status_bar_background = { fg: "#25352C" bg: "#C8E0D3" }
$env.config.explore.command_bar_text = { fg: "#25352C" }
$env.config.explore.command_bar_background = { bg: "#C8E0D3" }
$env.config.explore.title_bar_text = { fg: "#18231D" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#B7D8C6" }
$env.config.explore.status = {
    info: { fg: "#27629C" }
    success: { fg: "#E7F5ED" bg: "#207F41" }
    warn: { fg: "#E7F5ED" bg: "#8A6700" }
    error: { fg: "#E7F5ED" bg: "#BB403B" }
}
