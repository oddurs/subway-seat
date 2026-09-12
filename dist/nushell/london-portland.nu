# Subway Seat — generated from palette.py by build.py. Edit the palette, not this file.
# London Portland for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {
    shape_internalcall: "#896800"
    shape_external_resolved: "#896800"
    shape_external: "#CA2822"
    shape_keyword: "#9F591B"
    shape_flag: "#007376"
    shape_externalarg: "#434548"
    shape_signature: "#007376"
    shape_string: "#357D41"
    shape_raw_string: "#357D41"
    shape_string_interpolation: "#7660AB"
    shape_int: "#CA2822"
    shape_float: "#CA2822"
    shape_bool: "#CA2822"
    shape_binary: "#CA2822"
    shape_datetime: "#CA2822"
    shape_nothing: "#CA2822"
    shape_literal: "#CA2822"
    shape_range: "#7660AB"
    shape_custom: "#7660AB"
    shape_variable: "#7660AB"
    shape_vardecl: "#7660AB"
    shape_filepath: "#434548"
    shape_directory: "#434548"
    shape_globpattern: "#7660AB"
    shape_glob_interpolation: "#7660AB"
    shape_pipe: "#9F591B"
    shape_redirection: "#7660AB"
    shape_operator: "#7660AB"
    shape_block: "#5D6168"
    shape_closure: "#5D6168"
    shape_list: "#5D6168"
    shape_record: "#5D6168"
    shape_table: "#5D6168"
    shape_match_pattern: "#357D41"
    shape_matching_brackets: { fg: "#977300" attr: "b" }
    shape_garbage: { fg: "#CA2822" attr: "u" }

    background: "#E5EAF6"
    foreground: "#2F3033"
    cursor: "#9F591B"
    separator: "#9BA5B8"
    leading_trailing_space_bg: { bg: "#ADB7CB" }
    header: { fg: "#9F591B" attr: "b" }
    row_index: "#727781"
    empty: "#8A919F"
    hints: "#8A919F"
    search_result: { fg: "#1F2022" bg: "#C9C3AC" }
    selection: { fg: "#1F2022" bg: "#ADB7CB" }
    selection_cursor: { attr: "n" }
    bool: "#CA2822"
    int: "#CA2822"
    float: "#CA2822"
    string: "#2F3033"
    glob: "#7660AB"
    binary: "#CA2822"
    binary_null_char: "#8A919F"
    binary_printable: "#357D41"
    binary_whitespace: "#007376"
    binary_ascii_other: "#7660AB"
    binary_non_ascii: "#9F591B"
    custom: "#7660AB"
    nothing: "#8A919F"
    list: "#2F3033"
    record: "#2F3033"
    range: "#7660AB"
    cell-path: "#5D6168"
    block: "#5D6168"
    closure: "#5D6168"
    semver: "#007376"
    semver-range: "#007376"
    banner_foreground: "#2F3033"
    banner_highlight1: "#9F591B"
    banner_highlight2: "#896800"
    filesize: {||
      if $in < 1kb { "#515459"
      } else if $in < 1mb { "#357D41"
      } else if $in < 100mb { "#896800"
      } else if $in < 1gb { "#9F591B"
      } else { "#CA2822" }
    }
    duration: {||
      if $in < 1sec { "#357D41"
      } else if $in < 1min { "#896800"
      } else if $in < 1hr { "#9F591B"
      } else { "#CA2822" }
    }
    datetime: {|| (date now) - $in |
      if $in < 1hr { "#398145"
      } else if $in < 1day { "#357D41"
      } else if $in < 1wk { "#896800"
      } else if $in < 4wk { "#9F591B"
      } else if $in < 52wk { "#515459"
      } else { "#727781" }
    }
}

$env.config.explore.selected_cell = { fg: "#E5EAF6" bg: "#9F591B" }
$env.config.explore.highlight = { fg: "#1F2022" bg: "#C9C3AC" }
$env.config.explore.status_bar_text = { fg: "#434548" }
$env.config.explore.status_bar_background = { fg: "#2F3033" bg: "#CED5E3" }
$env.config.explore.command_bar_text = { fg: "#2F3033" }
$env.config.explore.command_bar_background = { bg: "#CED5E3" }
$env.config.explore.title_bar_text = { fg: "#1F2022" attr: "b" }
$env.config.explore.title_bar_background = { bg: "#C1CADC" }
$env.config.explore.status = {
    info: { fg: "#0019A8" }
    success: { fg: "#E5EAF6" bg: "#357D41" }
    warn: { fg: "#E5EAF6" bg: "#896800" }
    error: { fg: "#E5EAF6" bg: "#CA2822" }
}
