"""qutebrowser: a config.py color snippet per flavor (every c.colors.* setting)."""

from ports._apps import ink, select
from ports._lib import HEADER, Out

META = {
    "id": "qutebrowser",
    "name": "qutebrowser",
    "category": "Apps",
    "homepage": "https://qutebrowser.org",
    "enable": {
        "where": "~/.config/qutebrowser/config.py (macOS: ~/.qutebrowser/config.py)",
        "code": "config.load_autoconfig()\nconfig.source(\"{snake}.py\")",
        "lang": "python",
    },
    "notes": "Sets every `c.colors.*` option: tabs, status bar modes, completion, hints, prompts, messages "
    "and downloads, plus the page background and preferred color scheme so new tabs don't flash white.",
}


def settings(f):
    d = f.dark
    danger = f.red_hi if d else f.red
    sel = select(f)
    line = f.surface0 if d else f.surface1
    on = ink(f)
    return {
        # Completion (the : command menu)
        "completion.fg": f.text,
        "completion.odd.bg": f.mantle,
        "completion.even.bg": f.mantle,
        "completion.category.fg": f.orange,
        "completion.category.bg": f.crust,
        "completion.category.border.top": f.crust,
        "completion.category.border.bottom": line,
        "completion.item.selected.fg": f.text_hi,
        "completion.item.selected.bg": sel,
        "completion.item.selected.border.top": sel,
        "completion.item.selected.border.bottom": sel,
        "completion.item.selected.match.fg": f.orange_hi if d else f.orange,
        "completion.match.fg": f.yellow,
        "completion.scrollbar.fg": f.surface2 if d else f.surface1,
        "completion.scrollbar.bg": f.mantle,
        # Context menus
        "contextmenu.menu.bg": f.mantle,
        "contextmenu.menu.fg": f.text,
        "contextmenu.disabled.bg": f.mantle,
        "contextmenu.disabled.fg": f.overlay0,
        "contextmenu.selected.bg": sel,
        "contextmenu.selected.fg": f.text_hi,
        # Downloads
        "downloads.bar.bg": f.crust,
        "downloads.start.fg": on,
        "downloads.start.bg": f.denim,
        "downloads.stop.fg": on,
        "downloads.stop.bg": f.green,
        "downloads.error.fg": on,
        "downloads.error.bg": danger,
        "downloads.system.fg": "none",
        "downloads.system.bg": "none",
        # Hints
        "hints.fg": on,
        "hints.bg": f.yellow,
        "hints.match.fg": f.mix("yellow", "crust" if d else "text_hi", 0.5),
        # Key hints
        "keyhint.fg": f.text,
        "keyhint.suffix.fg": f.orange,
        "keyhint.bg": f.mantle,
        # Messages
        "messages.error.fg": on,
        "messages.error.bg": danger,
        "messages.error.border": danger,
        "messages.warning.fg": on,
        "messages.warning.bg": f.yellow,
        "messages.warning.border": f.yellow,
        "messages.info.fg": f.text,
        "messages.info.bg": f.mantle,
        "messages.info.border": line,
        # Prompts
        "prompts.fg": f.text,
        "prompts.border": f"1px solid {line}",
        "prompts.bg": f.mantle,
        "prompts.selected.fg": f.text_hi,
        "prompts.selected.bg": sel,
        # Status bar: quiet in normal mode, a solid chip of color for the others
        "statusbar.normal.fg": f.subtext1,
        "statusbar.normal.bg": f.crust,
        "statusbar.insert.fg": on,
        "statusbar.insert.bg": f.green,
        "statusbar.passthrough.fg": on,
        "statusbar.passthrough.bg": f.denim,
        "statusbar.private.fg": f.text,
        "statusbar.private.bg": f.mix("clay", "crust", 0.22),
        "statusbar.command.fg": f.text,
        "statusbar.command.bg": f.mantle,
        "statusbar.command.private.fg": f.text,
        "statusbar.command.private.bg": f.mix("clay", "mantle", 0.22),
        "statusbar.caret.fg": on,
        "statusbar.caret.bg": f.sage,
        "statusbar.caret.selection.fg": on,
        "statusbar.caret.selection.bg": f.sage_hi,
        "statusbar.progress.bg": f.orange,
        "statusbar.url.fg": f.text,
        "statusbar.url.error.fg": danger,
        "statusbar.url.hover.fg": f.denim,
        "statusbar.url.success.http.fg": f.clay,
        "statusbar.url.success.https.fg": f.green,
        "statusbar.url.warn.fg": f.yellow,
        # Tabs
        "tabs.bar.bg": f.crust,
        "tabs.indicator.start": f.yellow,
        "tabs.indicator.stop": f.green,
        "tabs.indicator.error": danger,
        "tabs.indicator.system": "none",
        "tabs.odd.fg": f.overlay2,
        "tabs.odd.bg": f.crust,
        "tabs.even.fg": f.overlay2,
        "tabs.even.bg": f.crust,
        "tabs.pinned.odd.fg": f.subtext0,
        "tabs.pinned.odd.bg": f.mantle,
        "tabs.pinned.even.fg": f.subtext0,
        "tabs.pinned.even.bg": f.mantle,
        "tabs.pinned.selected.odd.fg": f.text_hi,
        "tabs.pinned.selected.odd.bg": f.base,
        "tabs.pinned.selected.even.fg": f.text_hi,
        "tabs.pinned.selected.even.bg": f.base,
        "tabs.selected.odd.fg": f.text_hi,
        "tabs.selected.odd.bg": f.base,
        "tabs.selected.even.fg": f.text_hi,
        "tabs.selected.even.bg": f.base,
        # Tooltips and pages
        "tooltip.fg": f.text,
        "tooltip.bg": f.surface0 if d else f.mantle,
        "webpage.bg": f.base,
        "webpage.preferred_color_scheme": "dark" if d else "light",
    }


def snippet(f):
    d = f.dark
    hint_border = f.mix("yellow", "crust", 0.55) if d else f.mix("yellow", "text_hi", 0.7)
    lines = [
        f"# {HEADER}",
        f"# {f.name} for qutebrowser. In config.py: config.source(\"{f.snake}.py\")",
        "# pylint: disable=undefined-variable  (c and config are provided by qutebrowser)",
        "",
    ]
    lines += [f"c.colors.{k} = {v!r}".replace("'", '"') for k, v in settings(f).items()]
    lines += ["", f'c.hints.border = "1px solid {hint_border}"', ""]
    return "\n".join(lines)


def build(flavors):
    return [Out(f"{f.snake}.py", snippet(f), flavor=f.id, dest=f"~/.config/qutebrowser/{f.snake}.py", lang="python")
            for f in flavors]
