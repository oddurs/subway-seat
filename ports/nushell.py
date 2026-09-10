from ports._cli import bar, ink, selection
from ports._lib import HEADER, Out

META = {
    "id": "nushell",
    "name": "Nushell",
    "category": "Shell & prompt",
    "homepage": "https://www.nushell.sh",
    "enable": {
        "where": "config.nu (`$nu.config-path`)",
        "code": "source ~/.config/nushell/themes/{slug}.nu",
        "lang": "text",
    },
    "notes": "The fish port's command-line colours as a `color_config`, plus table output where file "
    "sizes and ages run down the 70s stripe. It turns on `highlight_resolved_externals`, so unknown "
    "commands show red as they do in fish.",
}


def q(color):
    return f'"{color}"'


def rec(fg=None, bg=None, attr=None):
    parts = [f'fg: "{fg}"'] if fg else []
    parts += [f'bg: "{bg}"'] if bg else []
    parts += [f'attr: "{attr}"'] if attr else []
    return "{ " + " ".join(parts) + " }"


def ramp(steps, last):
    """A closure that picks a colour by threshold, e.g. file size or age."""
    body = []
    for i, (limit, color) in enumerate(steps):
        body.append(f"{'if' if i == 0 else '} else if'} $in < {limit} {{ \"{color}\"")
    body.append(f'}} else {{ "{last}" }}')
    return "\n".join(body)


def theme(f):
    on = ink(f)
    shapes = {
        # Commands, keywords and flags, as in the fish port.
        "shape_internalcall": q(f.yellow),
        "shape_external_resolved": q(f.yellow),
        "shape_external": q(f.red_hi),
        "shape_keyword": q(f.orange),
        "shape_flag": q(f.sage),
        "shape_externalarg": q(f.subtext1),
        "shape_signature": q(f.sage),
        # Strings and literals
        "shape_string": q(f.green),
        "shape_raw_string": q(f.green),
        "shape_string_interpolation": q(f.clay),
        "shape_int": q(f.red_hi),
        "shape_float": q(f.red_hi),
        "shape_bool": q(f.red_hi),
        "shape_binary": q(f.red_hi),
        "shape_datetime": q(f.red_hi),
        "shape_nothing": q(f.red_hi),
        "shape_literal": q(f.red_hi),
        "shape_range": q(f.clay),
        "shape_custom": q(f.clay),
        # Variables and paths
        "shape_variable": q(f.clay),
        "shape_vardecl": q(f.clay),
        "shape_filepath": q(f.subtext1),
        "shape_directory": q(f.subtext1),
        "shape_globpattern": q(f.clay),
        "shape_glob_interpolation": q(f.clay),
        # Operators and punctuation
        "shape_pipe": q(f.orange),
        "shape_redirection": q(f.clay),
        "shape_operator": q(f.clay),
        "shape_block": q(f.overlay2),
        "shape_closure": q(f.overlay2),
        "shape_list": q(f.overlay2),
        "shape_record": q(f.overlay2),
        "shape_table": q(f.overlay2),
        "shape_match_pattern": q(f.green),
        "shape_matching_brackets": rec(f.yellow_hi, attr="b"),
        "shape_garbage": rec(f.red_hi, attr="u"),
    }
    size = ramp([("1kb", f.subtext0), ("1mb", f.green), ("100mb", f.yellow), ("1gb", f.orange)], f.red_hi)
    duration = ramp([("1sec", f.green), ("1min", f.yellow), ("1hr", f.orange)], f.red_hi)
    age = ramp([("1hr", f.green_hi), ("1day", f.green), ("1wk", f.yellow), ("4wk", f.orange), ("52wk", f.subtext0)],
               f.overlay1)
    values = {
        # Terminal colours, read by theme-switching commands rather than drawn by Nushell.
        "background": q(f.base),
        "foreground": q(f.text),
        "cursor": q(f.yellow if f.dark else f.orange),
        "separator": q(f.surface2),
        "leading_trailing_space_bg": rec(bg=f.surface1),
        "header": rec(f.orange, attr="b"),
        "row_index": q(f.overlay1),
        "empty": q(f.overlay0),
        "hints": q(f.overlay0),
        "search_result": rec(on, f.yellow),
        "selection": rec(f.text_hi, selection(f)),
        "selection_cursor": rec(attr="n"),
        "bool": q(f.red_hi),
        "int": q(f.red_hi),
        "float": q(f.red_hi),
        "string": q(f.text),
        "glob": q(f.clay),
        "binary": q(f.red_hi),
        "binary_null_char": q(f.overlay0),
        "binary_printable": q(f.green),
        "binary_whitespace": q(f.sage),
        "binary_ascii_other": q(f.clay),
        "binary_non_ascii": q(f.orange),
        "custom": q(f.clay),
        "nothing": q(f.overlay0),
        "list": q(f.text),
        "record": q(f.text),
        "range": q(f.clay),
        "cell-path": q(f.overlay2),
        "block": q(f.overlay2),
        "closure": q(f.overlay2),
        "semver": q(f.sage),
        "semver-range": q(f.sage),
        "banner_foreground": q(f.text),
        "banner_highlight1": q(f.orange),
        "banner_highlight2": q(f.yellow),
        "filesize": "{||\n" + size + "\n}",
        "duration": "{||\n" + duration + "\n}",
        "datetime": "{|| (date now) - $in |\n" + age + "\n}",
    }

    def block(d):
        lines = []
        for k, v in d.items():
            head, *rest = v.split("\n")
            lines.append(f"    {k}: {head}")
            lines += ["    }" if line == "}" else f"      {line}" for line in rest]
        return "\n".join(lines)

    explore = {
        "status_bar_background": rec(f.text, bar(f)),
        "command_bar_text": rec(f.text),
        "highlight": rec(on, f.yellow),
        "selected_cell": rec(on, f.orange),
    }
    return f"""# {HEADER}
# {f.name} for Nushell. Source it from config.nu.

$env.config.highlight_resolved_externals = true

$env.config.color_config = {{
{block(shapes)}

{block(values)}
}}

$env.config.explore = {{
{block(explore)}
    status: {{
        info: "{f.denim}"
        success: "{f.green}"
        warn: "{f.yellow}"
        error: "{f.red_hi}"
    }}
}}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.nu", theme(f), flavor=f.id, dest=f"~/.config/nushell/themes/{f.slug}.nu", lang="text")
        for f in flavors
    ]
