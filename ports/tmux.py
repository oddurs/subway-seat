from ports._cli import bar
from ports._lib import HEADER, Out, ink, selection, tints, ui_colors

META = {
    "id": "tmux",
    "name": "tmux",
    "category": "CLI & TUI",
    "homepage": "https://github.com/tmux/tmux",
    "enable": {
        "where": "~/.tmux.conf or ~/.config/tmux/tmux.conf, above TPM's `run` line if you use TPM "
        "(plugins such as tmux-continuum add to the status bar when TPM runs, and this file would "
        "replace their additions)",
        "code": "source-file ~/.config/tmux/{slug}.conf",
        "lang": "conf",
    },
    "auto": {
        "where": "~/.tmux.conf, in place of the line above (tmux 3.6+, in a terminal that reports "
        "light and dark changes)",
        "code": "source-file ~/.config/tmux/subway-seat.conf\n"
        "set-hook -g client-dark-theme 'source-file ~/.config/tmux/subway-seat.conf'\n"
        "set-hook -g client-light-theme 'source-file ~/.config/tmux/subway-seat-enamel.conf'",
        "lang": "conf",
    },
    "requires": "tmux 3.2+",
    "detect": ["tmux"],
    "notes": "A status bar like a station sign: the session as an orange route bullet (gold while the "
    "prefix is held), the active window lit in gold, a clock and a four-color stripe. The rounded "
    "bullet ends need a Nerd Font; no plugins required. With TPM, `set -g @plugin 'oddurs/subway-seat'` "
    "works too: set `@subway_seat_flavor` to walnut, tunnel, enamel or auto first, and list it before "
    "tmux-continuum.",
}

# Rounded caps (Nerd Font / Powerline Extra) around the session "route bullet".
LEFT_CAP, RIGHT_CAP = "\ue0b6", "\ue0b4"


def conf(f):
    # tmux expands #D and #F inside formats (pane id, window flags), so every
    # color is written in lowercase to keep hex digits from being read as aliases.
    c = {k: v.lower() for k, v in f.colors.items()}
    t = {k: v.lower() for k, v in tints(f).items()}
    bg, on = bar(f).lower(), ink(f).lower()
    sel = selection(f).lower()
    paper = ui_colors(f)["paper"].lower()
    cursor = c["yellow"] if f.dark else c["orange"]
    border = c["surface1"] if f.dark else c["surface2"]
    bullet = f"#{{?client_prefix,{c['yellow']},{c['orange']}}}"
    zoom = f"#{{?window_zoomed_flag,#[fg={c['yellow']}] Z,}}"

    status_left = (
        f"#[fg={bullet},bg={bg}]{LEFT_CAP}"
        f"#[fg={on},bg={bullet},bold] #S "
        f"#[fg={bullet},bg={bg},nobold]{RIGHT_CAP} "
    )
    window = f"#[fg={c['overlay1']},bg={bg}] #I #[fg={c['subtext0']}]#W{zoom} "
    window_current = (
        f"#[fg={on},bg={c['yellow']},bold] #I "
        f"#[fg={c['text_hi']},bg={c['surface1']},nobold] #W{zoom} "
        f"#[bg={bg}]"
    )
    stripe = "".join(f"#[fg={c[k]}]█" for k in ("red", "orange", "yellow", "green"))
    status_right = (
        f"#[fg={c['subtext0']},bg={bg}] %a %d %b "
        f"#[fg={c['text_hi']},bg={c['surface1']}] %H:%M "
        f"#[bg={bg}] {stripe}"
    )

    return f"""# {HEADER}
# {f.name} for tmux 3.2+. Options from newer releases are set with -q, so older tmux skips them.

# ── Status bar ─────────────────────────────────────────────────────────────
set -g status on
set -g status-justify left
set -g status-style "fg={c['subtext0']},bg={bg}"
set -g status-left-style NONE
set -g status-right-style NONE
set -g status-left-length 40
set -g status-right-length 80
set -g status-left "{status_left}"
set -g status-right "{status_right}"

# ── Windows ────────────────────────────────────────────────────────────────
set -g window-status-separator ""
set -g window-status-style "fg={c['subtext0']},bg={bg}"
set -g window-status-current-style "fg={c['text_hi']},bg={c['surface1']}"
set -g window-status-last-style "fg={c['subtext1']},bg={bg}"
set -g window-status-activity-style "fg={c['orange']},bg={bg}"
set -g window-status-bell-style "fg={c['red_hi']},bg={bg},bold"
set -g window-status-format "{window}"
set -g window-status-current-format "{window_current}"

# ── Panes ──────────────────────────────────────────────────────────────────
set -g pane-border-style "fg={border}"
set -g pane-active-border-style "fg={c['orange']}"
set -g display-panes-colour "{c['overlay0']}"
set -g display-panes-active-colour "{c['orange']}"
set -gq display-panes-border-style "fg={border}"
set -gq pane-scrollbars-style "fg={c['overlay0']},bg={c['mantle'] if f.dark else c['crust']},width=1,pad=0"
set -gq pane-status-style "fg={c['subtext0']},bg={bg}"
set -gq pane-status-current-style "fg={c['text_hi']},bg={bg},underscore"
set -gq session-status-style "fg={c['subtext0']},bg={bg}"
set -gq session-status-current-style "fg={c['text_hi']},bg={bg},underscore"
set -gq cursor-colour "{cursor}"

# ── Messages, prompts, copy mode ───────────────────────────────────────────
set -g message-style "fg={c['text_hi']},bg={c['surface1']}"
set -g message-command-style "fg={c['yellow']},bg={c['surface1']}"
set -g mode-style "fg={c['text_hi']},bg={sel}"
set -gq copy-mode-match-style "fg={c['text_hi']},bg={t['search']}"
set -gq copy-mode-current-match-style "fg={c['text_hi']},bg={t['search_cur']},bold"
set -gq copy-mode-mark-style "fg={on},bg={c['clay']}"
set -gq copy-mode-selection-style "fg={c['text_hi']},bg={sel}"
set -gq copy-mode-position-style "fg={on},bg={c['orange']}"
set -gq copy-mode-line-number-style "fg={c['overlay0']}"
set -gq copy-mode-current-line-number-style "fg={cursor}"
set -gq copy-mode-current-line-style "bg={c['surface0'] if f.dark else c['mantle']}"
set -gq prompt-cursor-colour "{cursor}"
set -gq prompt-command-cursor-colour "{c['orange'] if f.dark else c['yellow']}"
set -g clock-mode-colour "{c['yellow']}"

# ── Choose-tree and switch modes (tmux 3.6+) ───────────────────────────────
set -gq tree-mode-border-style "fg={border}"
set -gq tree-mode-selection-style "fg={c['text_hi']},bg={sel}"
set -gq switch-mode-match-style "fg={c['text_hi']},bg={t['search']},bold"

# ── Popups and menus (tmux 3.3+ / 3.4+) ────────────────────────────────────
set -gq popup-style "fg={c['text']},bg={paper}"
set -gq popup-border-style "fg={c['orange']},bg={paper}"
set -gq menu-style "fg={c['text']},bg={paper}"
set -gq menu-selected-style "fg={on},bg={c['orange']}"
set -gq menu-border-style "fg={c['surface2']},bg={paper}"
"""


def build(flavors):
    return [
        Out(f"{f.slug}.conf", conf(f), flavor=f.id, dest=f"~/.config/tmux/{f.slug}.conf", lang="conf")
        for f in flavors
    ]
