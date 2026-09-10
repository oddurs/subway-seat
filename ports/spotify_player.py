from ports._cli import marked, row
from ports._lib import ANSI_NAMES, HEADER, Out

META = {
    "id": "spotify-player",
    "name": "spotify_player",
    "category": "CLI & TUI",
    "homepage": "https://github.com/aome510/spotify-player",
    "enable": {
        "where": "~/.config/spotify-player/app.toml, after adding the theme to the end of theme.toml",
        "code": 'theme = "{slug}"',
        "lang": "toml",
    },
    "detect": ["spotify_player"],
    "notes": "A full palette plus component styles: gold track titles, orange progress bar, avocado for "
    "what's playing, and a visualizer that climbs the 70s stripe.",
}

def s(fg=None, bg=None, *mods):
    parts = [f'fg = "{fg}"'] if fg else []
    parts += [f'bg = "{bg}"'] if bg else []
    parts += ["modifiers = [" + ", ".join(f'"{m}"' for m in mods) + "]"] if mods else []
    return "{ " + ", ".join(parts) + " }" if parts else "{}"


def entry(f):
    palette = {"background": f.base, "foreground": f.text}
    for i, color in enumerate(f.ansi):
        palette[("bright_" if i >= 8 else "") + ANSI_NAMES[i % 8]] = color
    components = {
        "block_title": s(f.orange, None, "Bold"),
        "border": s(f.surface2),
        "playback_status": s(f.yellow, None, "Bold"),
        "playback_track": s(f.yellow, None, "Bold"),
        "playback_artists": s(f.orange),
        "playback_album": s(f.sage),
        "playback_genres": s(f.overlay1, None, "Italic"),
        "playback_metadata": s(f.subtext0),
        "playback_progress_bar": s(f.orange, f.surface1),
        "playback_progress_bar_unfilled": s(f.surface2, f.surface1),
        "current_playing": s(f.green, None, "Bold"),
        "page_desc": s(f.yellow, None, "Bold"),
        "playlist_desc": s(f.overlay1),
        "table_header": s(f.orange),
        "selection": s(f.text_hi, row(f), "Bold"),
        "secondary_row": s(None, f.mantle),
        "like": s(f.red_hi),
        "lyrics_played": s(f.overlay1),
        "lyrics_playing": s(f.yellow, None, "Bold"),
        "visualization": f'{{ low = "{f.green}", mid = "{f.yellow}", high = "{f.red_hi}" }}',
    }
    pal = "\n".join(f'{k} = "{v}"' for k, v in palette.items())
    comp = "\n".join(f"{k} = {v}" for k, v in components.items())
    return f'[[themes]]\nname = "{f.slug}"\n\n[themes.palette]\n{pal}\n\n[themes.component_style]\n{comp}\n'


def build(flavors):
    outs = [
        Out(f"themes/{f.slug}.toml", marked(f"# {HEADER}\n{entry(f)}"), flavor=f.id,
            dest="~/.config/spotify-player/theme.toml", append=True, lang="toml")
        for f in flavors
    ]
    outs.append(Out("theme.toml", f"# {HEADER}\n" + "\n".join(entry(f) for f in flavors), lang="toml",
                    how="all three flavors: use it as ~/.config/spotify-player/theme.toml if you have no themes of your own"))
    return outs
