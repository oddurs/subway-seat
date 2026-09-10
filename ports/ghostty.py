from ports._lib import HEADER, Out

META = {
    "id": "ghostty",
    "name": "Ghostty",
    "category": "Terminals",
    "homepage": "https://ghostty.org",
    "enable": {"where": "~/.config/ghostty/config", "code": "theme = {name}", "lang": "conf"},
    "notes": "The 16 ANSI colors, cursor, selection and split fill. For light/dark following, use "
    "`theme = light:Subway Seat Enamel,dark:Subway Seat`.",
}


def build(flavors):
    outs = []
    for f in flavors:
        lines = [f"# {HEADER}"]
        lines += [f"palette = {i}={c}" for i, c in enumerate(f.ansi)]
        lines += [
            f"background = {f.base}",
            f"foreground = {f.text}",
            f"cursor-color = {f.yellow if f.dark else f.orange}",
            f"cursor-text = {f.base}",
            f"selection-background = {f.surface2 if f.dark else f.surface1}",
            f"selection-foreground = {f.text_hi}",
            f"split-divider-color = {f.surface0 if f.dark else f.crust}",
            f"unfocused-split-fill = {f.crust}",
        ]
        outs.append(
            Out(
                f.name,
                "\n".join(lines) + "\n",
                flavor=f.id,
                dest=f"~/.config/ghostty/themes/{f.name}",
                lang="conf",
            )
        )
    return outs
