"""WezTerm: a TOML color scheme per flavor for `~/.config/wezterm/colors`."""

from ports._lib import HEADER, REPO, Out, selection
from ports._terminals import lit, search, search_cur, split

LOAD = "wezterm.color.load_scheme(wezterm.home_dir .. '/.config/wezterm/colors/"

META = {
    "id": "wezterm",
    "name": "WezTerm",
    "category": "Terminals",
    "homepage": "https://wezterm.org",
    "detect": ["wezterm", "/Applications/WezTerm.app"],
    "enable": {
        "where": "~/.config/wezterm/wezterm.lua",
        "code": "config.color_scheme = '{name}'\n"
        "-- the fancy tab bar's strip comes from window_frame, which a scheme file can't set\n"
        f"local colors = {LOAD}{{slug}}.toml')\n"
        "config.window_frame = {{ active_titlebar_bg = colors.tab_bar.background, "
        "inactive_titlebar_bg = colors.tab_bar.background }}",
        "lang": "lua",
    },
    "auto": {
        "where": "~/.config/wezterm/wezterm.lua (WezTerm reloads it when the appearance changes)",
        "code": "local dark = not wezterm.gui or wezterm.gui.get_appearance():find('Dark')\n"
        "local slug = dark and 'subway-seat' or 'subway-seat-enamel'\n"
        f"local colors, meta = {LOAD}' .. slug .. '.toml')\n"
        "config.color_scheme = meta.name\n"
        "config.window_frame = { active_titlebar_bg = colors.tab_bar.background, "
        "inactive_titlebar_bg = colors.tab_bar.background }",
        "lang": "lua",
    },
    "notes": "Colors, cursor, selection, splits, copy mode, quick select and the tab bar. On Windows the "
    "folder is `%USERPROFILE%\\.config\\wezterm\\colors`.",
}


def q(v):
    return f'"{v}"'


def arr(colors):
    return "[\n" + "".join(f'  "{c}",\n' for c in colors) + "]"


def tab(bg, fg, bold=False):
    return (
        f"bg_color = {q(bg)}\nfg_color = {q(fg)}\nintensity = {q('Bold' if bold else 'Normal')}\n"
        'italic = false\nstrikethrough = false\nunderline = "None"'
    )


def theme(f):
    colors = {
        "foreground": q(f.text),
        "background": q(f.base),
        "cursor_bg": q(lit(f)),
        "cursor_border": q(lit(f)),
        "cursor_fg": q(f.base),
        "compose_cursor": q(f.clay),
        "selection_bg": q(selection(f)),
        "selection_fg": q(f.text_hi),
        "scrollbar_thumb": q(f.surface2),
        "split": q(split(f)),
        "visual_bell": q(f.surface0),
        "ansi": arr(f.ansi[:8]),
        "brights": arr(f.ansi[8:]),
        "copy_mode_active_highlight_bg": f"{{ Color = {q(search_cur(f))} }}",
        "copy_mode_active_highlight_fg": f"{{ Color = {q(f.text_hi)} }}",
        "copy_mode_inactive_highlight_bg": f"{{ Color = {q(search(f))} }}",
        "copy_mode_inactive_highlight_fg": f"{{ Color = {q(f.text)} }}",
        "quick_select_label_bg": f"{{ Color = {q(f.orange)} }}",
        "quick_select_label_fg": f"{{ Color = {q(f.base)} }}",
        "quick_select_match_bg": f"{{ Color = {q(search(f))} }}",
        "quick_select_match_fg": f"{{ Color = {q(f.text)} }}",
    }
    return (
        f"# {HEADER}\n\n[colors]\n"
        + "\n".join(f"{k} = {v}" for k, v in colors.items())
        + f"\n\n[colors.tab_bar]\nbackground = {q(f.crust)}\ninactive_tab_edge = {q(f.surface0)}\n"
        + f"\n[colors.tab_bar.active_tab]\n{tab(f.base, lit(f), bold=True)}\n"
        + f"\n[colors.tab_bar.inactive_tab]\n{tab(f.mantle, f.overlay1)}\n"
        + f"\n[colors.tab_bar.inactive_tab_hover]\n{tab(f.surface0, f.text)}\n"
        + f"\n[colors.tab_bar.new_tab]\n{tab(f.crust, f.overlay1)}\n"
        + f"\n[colors.tab_bar.new_tab_hover]\n{tab(f.surface0, lit(f))}\n"
        + f'\n[metadata]\nname = {q(f.name)}\nauthor = "oddurs"\norigin_url = {q(REPO)}\naliases = []\n'
    )


def build(flavors):
    return [
        Out(
            f"{f.slug}.toml",
            theme(f),
            flavor=f.id,
            dest=f"~/.config/wezterm/colors/{f.slug}.toml",
            lang="toml",
        )
        for f in flavors
    ]
