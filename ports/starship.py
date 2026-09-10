from ports._lib import HEADER, Out

META = {
    "id": "starship",
    "name": "Starship",
    "category": "Shell & prompt",
    "homepage": "https://starship.rs",
    "enable": {"where": "~/.config/starship.toml", "code": "palette = '{snake}'", "lang": "toml"},
    "notes": "Palettes use the slot names of Starship's Gruvbox Rainbow preset, so its segments turn "
    "into a red → orange → gold → avocado stripe. `subway-seat.toml` is a complete prompt built on it.",
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
        "color_fg0": f.crust if f.dark else f.base,
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
    body = "\n".join(f"{k:<13} = '{v}'" for k, v in slots.items())
    return f"[palettes.{f.snake}]\n{body}\n"


def build(flavors):
    outs = [
        Out(f"palettes/{f.slug}.toml", f"# {HEADER}\n{palette(f)}", flavor=f.id,
            dest="~/.config/starship.toml", append=True, lang="toml")
        for f in flavors
    ]
    all_palettes = "\n".join(palette(f) for f in flavors)
    outs.append(
        Out("subway-seat.toml", f"# {HEADER}\n{PRESET.replace('{snake}', flavors[0].snake)}\n{all_palettes}",
            dest="~/.config/starship.toml", lang="toml")
    )
    return outs
