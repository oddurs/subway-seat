from ports._cli import bar, ink, selection
from ports._lib import HEADER, Out, tints

META = {
    "id": "tmux",
    "name": "tmux",
    "category": "CLI & TUI",
    "homepage": "https://github.com/tmux/tmux",
    "enable": {
        "where": "~/.tmux.conf or ~/.config/tmux/tmux.conf (after TPM's `run` line, if you use TPM)",
        "code": "source-file ~/.config/tmux/{slug}.conf",
        "lang": "conf",
    },
    "notes": "A status bar like a station sign: the session as an orange route bullet (gold while the "
    "prefix is held), the active window lit in gold, a clock and a four-color stripe. The rounded "
    "bullet ends need a Nerd Font; no plugins required.",
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

# ── Messages, prompts, copy mode ───────────────────────────────────────────
set -g message-style "fg={c['text_hi']},bg={c['surface1']}"
set -g message-command-style "fg={c['yellow']},bg={c['surface1']}"
set -g mode-style "fg={c['text_hi']},bg={sel}"
set -gq copy-mode-match-style "fg={c['text_hi']},bg={t['search']}"
set -gq copy-mode-current-match-style "fg={c['text_hi']},bg={t['search_cur']},bold"
set -gq copy-mode-mark-style "fg={on},bg={c['clay']}"
set -g clock-mode-colour "{c['yellow']}"

# ── Popups and menus (tmux 3.3+ / 3.4+) ────────────────────────────────────
set -gq popup-style "fg={c['text']},bg={c['base']}"
set -gq popup-border-style "fg={c['orange']}"
set -gq menu-style "fg={c['text']},bg={bg}"
set -gq menu-selected-style "fg={on},bg={c['orange']}"
set -gq menu-border-style "fg={c['surface2']}"
"""


def build(flavors):
    return [
        Out(f"{f.slug}.conf", conf(f), flavor=f.id, dest=f"~/.config/tmux/{f.slug}.conf", lang="conf")
        for f in flavors
    ]
