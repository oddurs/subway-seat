# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Deep Level for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#F2C03F"
    shape_external_resolved: "#F2C03F"
    shape_external: "#F17869"
    shape_keyword: "#DE8946"
    shape_flag: "#54B4B5"
    shape_externalarg: "#BEC6D5"
    shape_signature: "#54B4B5"
    shape_string: "#77C581"
    shape_raw_string: "#77C581"
    shape_string_interpolation: "#AE9EDC"
    shape_int: "#F17869"
    shape_float: "#F17869"
    shape_bool: "#F17869"
    shape_binary: "#F17869"
    shape_datetime: "#F17869"
    shape_nothing: "#F17869"
    shape_literal: "#F17869"
    shape_range: "#AE9EDC"
    shape_custom: "#AE9EDC"
    shape_variable: "#AE9EDC"
    shape_vardecl: "#AE9EDC"
    shape_filepath: "#BEC6D5"
    shape_directory: "#BEC6D5"
    shape_globpattern: "#AE9EDC"
    shape_glob_interpolation: "#AE9EDC"
    shape_pipe: "#DE8946"
    shape_redirection: "#AE9EDC"
    shape_operator: "#AE9EDC"
    shape_block: "#8B96AC"
    shape_closure: "#8B96AC"
    shape_list: "#8B96AC"
    shape_record: "#8B96AC"
    shape_table: "#8B96AC"
    shape_match_pattern: "#77C581"
    shape_matching_brackets: { fg: "#FFD36C" attr: "b" }
    shape_garbage: { fg: "#F17869" attr: "u" }

    background: "#121A2D"
    foreground: "#D4DAE7"
    cursor: "#F2C03F"
    separator: "#303E5B"
    leading_trailing_space_bg: { bg: "#232F49" }
    header: { fg: "#DE8946" attr: "b" }
    row_index: "#6F7C97"
    empty: "#53617D"
    hints: "#53617D"
    search_result: { fg: "#E7EBF3" bg: "#554C32" }
    selection: { fg: "#E7EBF3" bg: "#303E5B" }
    selection_cursor: { attr: "n" }
    bool: "#F17869"
    int: "#F17869"
    float: "#F17869"
    string: "#D4DAE7"
    glob: "#AE9EDC"
    binary: "#F17869"
    binary_null_char: "#53617D"
    binary_printable: "#77C581"
    binary_whitespace: "#54B4B5"
    binary_ascii_other: "#AE9EDC"
    binary_non_ascii: "#DE8946"
    custom: "#AE9EDC"
    nothing: "#53617D"
    list: "#D4DAE7"
    record: "#D4DAE7"
    range: "#AE9EDC"
    cell-path: "#8B96AC"
    block: "#8B96AC"
    closure: "#8B96AC"
    semver: "#54B4B5"
    semver-range: "#54B4B5"
    banner_foreground: "#D4DAE7"
    banner_highlight1: "#DE8946"
    banner_highlight2: "#F2C03F"
    filesize: {||
      if $in < 1kb { "#A5AEC0"
      } else if $in < 1mb { "#77C581"
      } else if $in < 100mb { "#F2C03F"
      } else if $in < 1gb { "#DE8946"
      } else { "#F17869" }
    }
    duration: {||
      if $in < 1sec { "#77C581"
      } else if $in < 1min { "#F2C03F"
      } else if $in < 1hr { "#DE8946"
      } else { "#F17869" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#9AD2A0"
      } else if $in < 1day { "#77C581"
      } else if $in < 1wk { "#F2C03F"
      } else if $in < 4wk { "#DE8946"
      } else if $in < 52wk { "#A5AEC0"
      } else { "#6F7C97" }
    }
}

$env.config.explore.selected_cell = { fg: "#0A0E18" bg: "#DE8946" }
$env.config.explore.highlight = { fg: "#E7EBF3" bg: "#554C32" }
$env.config.explore.status_bar_text = { fg: "#BEC6D5" }
$env.config.explore.status_bar_background = { fg: "#D4DAE7" bg: "#0D1421" }
$env.config.explore.command_bar_text = { fg: "#D4DAE7" }
$env.config.explore.command_bar_background = { bg: "#0D1421" }
$env.config.explore.title_bar_text = { fg: "#E7EBF3" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#232F49" }
$env.config.explore.status = {
    info: { fg: "#7595DA" }
    success: { fg: "#0A0E18" bg: "#77C581" }
    warn: { fg: "#0A0E18" bg: "#F2C03F" }
    error: { fg: "#0A0E18" bg: "#F17869" }
}
