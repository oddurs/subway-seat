from ports._lib import HEADER, Out, h

META = {
    "id": "fish",
    "name": "fish",
    "category": "Shell & prompt",
    "homepage": "https://fishshell.com",
    "enable": {"where": "config.fish (fish 4.3+)", "code": "fish_config theme choose {slug}", "lang": "fish"},
    "notes": "Command-line syntax colours and the completion pager. `subway-seat-auto` carries both "
    "Walnut and Enamel and follows your terminal's background.",
}


def colors(f):
    return {
        "fish_color_normal": h(f.text),
        "fish_color_command": h(f.yellow),
        "fish_color_keyword": h(f.orange),
        "fish_color_param": h(f.subtext1),
        "fish_color_option": h(f.sage),
        "fish_color_quote": h(f.green),
        "fish_color_redirection": h(f.clay),
        "fish_color_end": h(f.orange),
        "fish_color_operator": h(f.clay),
        "fish_color_escape": h(f.clay),
        "fish_color_comment": f"{h(f.overlay1)} --italics",
        "fish_color_error": h(f.red_hi),
        "fish_color_cancel": h(f.red),
        "fish_color_autosuggestion": h(f.overlay0),
        "fish_color_gray": h(f.overlay0),
        "fish_color_valid_path": "--underline",
        "fish_color_selection": f"{h(f.text_hi)} --bold --background={h(f.surface2)}",
        "fish_color_search_match": f"--bold --background={h(f.surface1)}",
        "fish_color_history_current": "--bold",
        "fish_color_cwd": h(f.yellow),
        "fish_color_cwd_root": h(f.red_hi),
        "fish_color_user": h(f.orange),
        "fish_color_host": h(f.subtext1),
        "fish_color_host_remote": h(f.green),
        "fish_color_status": h(f.red_hi),
        "fish_pager_color_progress": f"{h(f.crust if f.dark else f.base)} --background={h(f.orange)}",
        "fish_pager_color_prefix": f"{h(f.yellow)} --bold",
        "fish_pager_color_completion": h(f.text),
        "fish_pager_color_description": f"{h(f.overlay1)} --italics",
        "fish_pager_color_selected_background": f"--background={h(f.surface1)}",
    }


def body(f):
    return "\n".join(f"{k} {v}" for k, v in colors(f).items())


def build(flavors):
    by_id = {f.id: f for f in flavors}
    outs = [
        Out(
            f"themes/{f.slug}.theme",
            f"# name: '{f.name}'\n# {HEADER}\n# preferred_background: {h(f.base)}\n\n{body(f)}\n",
            flavor=f.id,
            dest=f"~/.config/fish/themes/{f.slug}.theme",
            lang="conf",
        )
        for f in flavors
    ]
    dark, light = by_id["walnut"], by_id["enamel"]
    outs.append(
        Out(
            "themes/subway-seat-auto.theme",
            f"# name: 'Subway Seat (auto)'\n# {HEADER}\n\n"
            f"[light]\n# preferred_background: {h(light.base)}\n{body(light)}\n\n"
            f"[dark]\n# preferred_background: {h(dark.base)}\n{body(dark)}\n",
            dest="~/.config/fish/themes/subway-seat-auto.theme",
            lang="conf",
        )
    )
    return outs
