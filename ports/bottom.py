from ports._cli import ink
from ports._lib import HEADER, Out

META = {
    "id": "bottom",
    "name": "bottom",
    "category": "CLI & TUI",
    "homepage": "https://github.com/ClementTsang/bottom",
    "enable": {
        "where": "bottom.toml (~/.config/bottom/ on Linux, ~/Library/Application Support/bottom/ on macOS)",
        "code": "cat {slug}.toml >> bottom.toml",
        "lang": "fish",
    },
    "notes": "A `[styles]` block for bottom 0.10+: cores and sensors in stripe colors, avocado "
    "download, orange upload, orange table headers and borders.",
}


def q(c):
    return f'"{c}"'


def arr(cs):
    return "[" + ", ".join(q(c) for c in cs) + "]"


def styles(f):
    many = [f.green, f.yellow, f.orange, f.red_hi, f.sage, f.clay, f.green_hi, f.yellow_hi]
    return f"""# {HEADER}
# {f.name} for bottom. Key names use the 0.10 spelling, which later releases accept too.

[styles.cpu]
all_entry_color = {q(f.text)}
avg_entry_color = {q(f.orange)}
cpu_core_colors = {arr(many)}

[styles.memory]
ram_color = {q(f.green)}
cache_color = {q(f.sage)}
swap_color = {q(f.orange)}
arc_color = {q(f.clay)}
gpu_colors = {arr([f.yellow, f.orange, f.red_hi, f.sage, f.clay, f.green_hi])}

[styles.network]
rx_color = {q(f.green)}
tx_color = {q(f.orange)}
rx_total_color = {q(f.green_hi)}
tx_total_color = {q(f.orange_hi)}

[styles.battery]
high_battery_color = {q(f.green)}
medium_battery_color = {q(f.yellow)}
low_battery_color = {q(f.red_hi)}

[styles.tables]
headers = {{ color = {q(f.orange)}, bold = true }}

[styles.graphs]
graph_color = {q(f.overlay0)}
legend_text = {{ color = {q(f.subtext0)} }}

[styles.widgets]
border_color = {q(f.surface2)}
selected_border_color = {q(f.orange)}
widget_title = {{ color = {q(f.yellow)} }}
text = {{ color = {q(f.text)} }}
selected_text = {{ color = {q(ink(f))}, bg_color = {q(f.orange)} }}
disabled_text = {{ color = {q(f.overlay0)} }}
thread_text = {{ color = {q(f.sage)} }}  # 0.11+

# Newer sections (bottom 0.13+); older releases ignore them.
[styles.temp_graph]
temp_graph_color_styles = {arr(many)}

[styles.disk_io_graph]
read_colours = {arr([f.green, f.sage, f.green_hi, f.sage_hi])}
write_colours = {arr([f.orange, f.clay, f.orange_hi, f.red_hi])}
"""


def build(flavors):
    return [
        Out(f"{f.slug}.toml", styles(f), flavor=f.id, dest="~/.config/bottom/bottom.toml", append=True, lang="toml")
        for f in flavors
    ]
