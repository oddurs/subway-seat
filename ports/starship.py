from ports._cli import marked
from ports._lib import ANSI_NAMES, HEADER, Out, ink

META = {
    "id": "starship",
    "name": "Starship",
    "category": "Shell & prompt",
    "homepage": "https://starship.rs",
    "enable": {
        "where": "the top of ~/.config/starship.toml, above every [section] (below a table it would "
        "be read as part of that table and ignored), after adding the palette block to the end",
        "code": "palette = '{snake}'",
        "lang": "toml",
    },
    "detect": ["starship"],
    "notes": "Palettes use the slot names of Starship's Gruvbox Rainbow preset, so its segments turn "
    "into a red → orange → gold → avocado stripe; they also redefine the standard color names, so "
    "other prompts pick up the flavor. `subway-seat.toml` is a complete prompt built on it: point "
    "STARSHIP_CONFIG at it or copy it over your config.",
}

# Gruvbox Rainbow layout; the Nerd Font glyphs are written as escapes.
PRESET = """\
"$schema" = 'https://starship.rs/config-schema.json'

format = \"\"\"
[\\ue0b6](color_orange)\\
$os\\
$username\\
[\\ue0b0](bg:color_yellow fg:color_orange)\\
$directory\\
[\\ue0b0](fg:color_yellow bg:color_aqua)\\
$git_branch\\
$git_status\\
[\\ue0b0](fg:color_aqua bg:color_blue)\\
$c\\
$rust\\
$golang\\
$nodejs\\
$python\\
[\\ue0b0](fg:color_blue bg:color_bg3)\\
$docker_context\\
[\\ue0b0](fg:color_bg3 bg:color_bg1)\\
$time\\
[\\ue0b4 ](fg:color_bg1)\\
$line_break$character\"\"\"

palette = '{snake}'

[os]
disabled = false
style = "bg:color_orange fg:color_fg0"

[os.symbols]
Macos = "\\U000f0035 "
Linux = "\\U000f033d "

[username]
show_always = true
style_user = "bg:color_orange fg:color_fg0"
style_root = "bg:color_orange fg:color_fg0"
format = '[ $user ]($style)'

[directory]
style = "fg:color_fg0 bg:color_yellow"
format = "[ $path ]($style)"
truncation_length = 3
truncation_symbol = "…/"

[git_branch]
symbol = "\\uf418"
style = "bg:color_aqua"
format = '[[ $symbol $branch ](fg:color_fg0 bg:color_aqua)]($style)'

[git_status]
style = "bg:color_aqua"
format = '[[($all_status$ahead_behind )](fg:color_fg0 bg:color_aqua)]($style)'

[nodejs]
symbol = "\\ue718"
format = '[[ $symbol( $version) ](fg:color_fg0 bg:color_blue)]($style)'

[c]
symbol = "\\ue61e "
format = '[[ $symbol( $version) ](fg:color_fg0 bg:color_blue)]($style)'

[rust]
symbol = "\\ue7a8"
format = '[[ $symbol( $version) ](fg:color_fg0 bg:color_blue)]($style)'

[golang]
symbol = "\\ue627"
format = '[[ $symbol( $version) ](fg:color_fg0 bg:color_blue)]($style)'

[python]
symbol = "\\ue606"
format = '[[ $symbol( $version) ](fg:color_fg0 bg:color_blue)]($style)'

[docker_context]
symbol = "\\uf308"
format = '[[ $symbol( $context) ](fg:color_fg_dark bg:color_bg3)]($style)'

[time]
disabled = false
time_format = "%R"
format = "[[ \\uf43a $time ](fg:color_fg_dark bg:color_bg1)]($style)"

[character]
success_symbol = "[\\uf105](bold fg:color_green)"
error_symbol = "[\\uf105](bold fg:color_red)"
vimcmd_symbol = "[\\uf104](bold fg:color_green)"
vimcmd_visual_symbol = "[\\uf104](bold fg:color_yellow)"
"""


def palette(f):
    slots = {
        "color_fg0": ink(f),
        "color_fg_dark": f.subtext1,
        "color_bg1": f.surface1,
        "color_bg3": f.surface2,
        "color_orange": f.red,
        "color_yellow": f.orange,
        "color_aqua": f.yellow,
        "color_blue": f.green,
        "color_green": f.green_hi,
        "color_red": f.red_hi,
        "color_purple": f.orange_hi,
    }
    # Starship's own color names, so prompts that say `red` or `bright-black` get the flavor too
    for i, color in enumerate(f.ansi):
        name = ANSI_NAMES[i % 8].replace("magenta", "purple")
        slots[("bright-" if i >= 8 else "") + name] = color
    body = "\n".join(f"{k:<14} = '{v}'" for k, v in slots.items())
    return f"[palettes.{f.snake}]\n{body}\n"


def build(flavors):
    outs = [
        Out(f"palettes/{f.slug}.toml", marked(f"# {HEADER}\n{palette(f)}"), flavor=f.id,
            dest="~/.config/starship.toml", append=True, lang="toml")
        for f in flavors
    ]
    all_palettes = "\n".join(palette(f) for f in flavors)
    outs.append(
        Out("subway-seat.toml", f"# {HEADER}\n{PRESET.replace('{snake}', flavors[0].snake)}\n{all_palettes}",
            dest="~/.config/starship/subway-seat.toml", lang="toml",
            how="use it with STARSHIP_CONFIG=~/.config/starship/subway-seat.toml, or copy it over "
            "~/.config/starship.toml; change `palette` to pick the flavor")
    )
    return outs
