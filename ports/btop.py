from ports._cli import stripe
from ports._lib import HEADER, Out, ink

META = {
    "id": "btop",
    "name": "btop",
    "category": "CLI & TUI",
    "homepage": "https://github.com/aristocratos/btop",
    "enable": {"where": "~/.config/btop/btop.conf, or Options › Color theme", "code": 'color_theme = "{slug}"', "lang": "conf"},
    "detect": ["btop"],
    "notes": "Every graph runs the 70s stripe, avocado to gold to orange to red, and the four boxes "
    "are outlined in orange, gold, avocado and terracotta.",
}


def theme(f):
    hot = stripe(f, 3)  # avocado → gold/orange → redbird

    def fade(role):  # the quiet end of a meter
        return f.mix(role, "base", 0.55)

    sections = [
        ("Main background, empty for terminal default", {"main_bg": f.base}),
        ("Main text color", {"main_fg": f.text}),
        ("Title color for boxes", {"title": f.text_hi}),
        ("Highlight color for keyboard shortcuts", {"hi_fg": f.orange}),
        ("Background of the selected item in the processes box", {"selected_bg": f.surface1}),
        ("Foreground of the selected item in the processes box", {"selected_fg": f.yellow_hi if f.dark else f.text_hi}),
        ("Inactive or disabled text", {"inactive_fg": f.overlay0}),
        ("Text drawn over graphs: uptime, network graph scale", {"graph_text": f.subtext0}),
        ("Background of the percentage meters", {"meter_bg": f.surface1}),
        ("Mini cpu graphs, detailed memory graph and status text in the processes box", {"proc_misc": f.sage}),
        ("Box outlines", {"cpu_box": f.orange, "mem_box": f.yellow, "net_box": f.green, "proc_box": f.clay}),
        ("Box dividers and small box outlines", {"div_line": f.surface2}),
        ("Temperature graph", {"temp_start": hot[0], "temp_mid": hot[1], "temp_end": hot[2]}),
        ("CPU graph", {"cpu_start": hot[0], "cpu_mid": hot[1], "cpu_end": hot[2]}),
        ("Mem/disk free meter", {"free_start": fade("green"), "free_mid": f.green, "free_end": f.green_hi}),
        ("Mem/disk cached meter", {"cached_start": fade("denim"), "cached_mid": f.denim, "cached_end": f.denim_hi}),
        ("Mem/disk available meter", {"available_start": fade("yellow"), "available_mid": f.yellow, "available_end": f.yellow_hi}),
        ("Mem/disk used meter", {"used_start": f.orange, "used_mid": f.red, "used_end": f.red_hi}),
        ("Download graph", {"download_start": fade("green"), "download_mid": f.green, "download_end": f.yellow}),
        ("Upload graph", {"upload_start": fade("orange"), "upload_mid": f.orange, "upload_end": f.red_hi}),
        ("Process box gradient for threads, memory and cpu usage", {"process_start": hot[0], "process_mid": hot[1], "process_end": hot[2]}),
        ("Banners over the process list while it is paused or following a process",
         {"proc_pause_bg": f.red, "proc_follow_bg": f.sage, "proc_banner_bg": f.orange, "proc_banner_fg": ink(f)}),
        ("The process being followed", {"followed_bg": f.sage, "followed_fg": ink(f)}),
    ]
    out = [f"# {HEADER}", f"# {f.name} for btop.", ""]
    for comment, keys in sections:
        out.append(f"# {comment}")
        out += [f'theme[{k}]="{v}"' for k, v in keys.items()]
        out.append("")
    return "\n".join(out)


def build(flavors):
    return [
        Out(f"{f.slug}.theme", theme(f), flavor=f.id, dest=f"~/.config/btop/themes/{f.slug}.theme", lang="conf")
        for f in flavors
    ]
