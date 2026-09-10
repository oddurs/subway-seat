from ports._lib import HEADER, Out

META = {
    "id": "fzf",
    "name": "fzf",
    "category": "CLI & TUI",
    "homepage": "https://github.com/junegunn/fzf",
    "enable": {
        "where": "your shell config (fish shown; bash/zsh files use export)",
        "code": "source ~/.config/fzf/{slug}.fish",
        "lang": "fish",
    },
    "notes": "Colors for the finder, preview border, pointer and marker.",
}


def spec(f):
    return ",".join([
        f"fg:{f.subtext1}", "bg:-1", f"hl:{f.yellow}",
        f"fg+:{f.text_hi}", f"bg+:{f.surface0}", f"hl+:{f.yellow_hi}",
        f"info:{f.overlay1}", f"prompt:{f.orange}", f"pointer:{f.orange}",
        f"marker:{f.green}", f"spinner:{f.yellow}", f"header:{f.sage}",
        f"border:{f.surface2}", "gutter:-1", f"query:{f.text}",
        f"selected-bg:{f.surface1}", f"separator:{f.surface1}", f"scrollbar:{f.surface2}",
        f"label:{f.subtext0}", f"preview-border:{f.surface2}",
    ])


def build(flavors):
    outs = []
    for f in flavors:
        s = spec(f)
        outs.append(Out(f"{f.slug}.fish", f'# {HEADER}\nset -gx FZF_DEFAULT_OPTS "--color={s}"\n',
                        flavor=f.id, dest=f"~/.config/fzf/{f.slug}.fish", lang="fish"))
        outs.append(Out(f"{f.slug}.sh", f"# {HEADER}\nexport FZF_DEFAULT_OPTS=\"--color={s}\"\n",
                        flavor=f.id, dest=f"~/.config/fzf/{f.slug}.sh", lang="sh"))
    return outs
