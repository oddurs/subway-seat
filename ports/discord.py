"""Discord (Vencord, Vesktop, BetterDiscord): a variable-level theme per flavor.

Each file themes both of Discord's modes, so switching Discord between dark and
light keeps you in the room: Walnut and Tunnel pair with Enamel, Enamel pairs
with Walnut. Only CSS custom properties are overridden (plus highlight.js token
classes, which come from the library, not Discord's hashed class names).
"""

import palette as p
from ports._apps import AUTHOR, rgba
from ports._lib import HEADER, REPO, VERSION, Out, ink, pair, tints, ui_colors

RAW = "https://raw.githubusercontent.com/oddurs/subway-seat/main/dist/discord"

META = {
    "id": "discord",
    "name": "Discord",
    "category": "Apps",
    "homepage": "https://discord.com",
    "enable": {
        "where": "Vencord or Vesktop: Settings › Themes › Open Themes Folder · BetterDiscord: Settings › Themes",
        "code": "Copy {slug}.theme.css into the themes folder, then turn it on under Settings › Themes.\n"
        "Discord's dark mode shows the dark flavor and its light mode shows Enamel.\n"
        "Vencord can also load it by URL (Settings › Themes › Online Themes):\n"
        f"{RAW}/{{slug}}.theme.css",
        "lang": "text",
    },
    "auto": {
        "where": "Discord › User Settings › Appearance",
        "code": "Theme: Sync with computer\n"
        "(each file covers both of Discord's modes: dark shows Walnut or Tunnel, light shows Enamel)",
        "lang": "text",
    },
    "requires": "Vencord, Vesktop or BetterDiscord",
    "detect": ["~/Library/Application Support/Vencord"],
    "notes": "Overrides Discord's color variables only, not its generated class names, which change between "
    "client updates. Each file covers both of Discord's modes and pairs a dark flavor with Enamel.",
}

# Where each client keeps themes. The file's dest is Vencord on macOS; the rest go in `how`.
FOLDERS = (
    "that's Vencord on macOS; on Linux it's ~/.config/Vencord/themes, on Windows %APPDATA%\\Vencord\\themes. "
    "Vesktop and BetterDiscord use the same folders with vesktop or BetterDiscord in place of Vencord."
)

DARK_SEL = ".visual-refresh.theme-dark,\n.visual-refresh .theme-dark"
LIGHT_SEL = ".visual-refresh.theme-light,\n.visual-refresh .theme-light"


def ramp(color):
    """Discord's --brand-100…900 ladder around one color (500 = the color)."""
    steps = [100, 130, 160, 200, 230, 260, 300, 330, 360, 400, 430, 460, 500,
             530, 560, 600, 630, 660, 700, 730, 760, 800, 830, 860, 900]
    out = {}
    for s in steps:
        if s < 500:
            out[s] = p.blend("#FFFFFF", color, (500 - s) / 400 * 0.8)
        elif s > 500:
            out[s] = p.blend("#000000", color, (s - 500) / 400 * 0.8)
        else:
            out[s] = color
    return out


def variables(f):
    dark = f.dark
    accent = f.orange
    danger = f.red_hi if dark else f.red
    muted = f.overlay2
    # Grounds, darkest → lightest in dark flavors; light flavors step the other way.
    frame, side, chat = f.crust, f.mantle, f.base
    raised = f.surface0 if dark else f.base
    floating = ui_colors(f)["paper"]  # popovers, menus and tooltips sit on paper
    input_bg = f.mix("surface0", "base", 0.6) if dark else f.mantle
    hover_a = 0.10 if dark else 0.14
    v = {}

    for step, c in ramp(accent).items():
        v[f"--brand-{step}"] = c
    for pct in range(5, 100, 5):
        v[f"--brand-{pct:02d}a"] = rgba(accent, pct / 100)
    v |= {
        "--brand-experiment": accent,
        "--brand-experiment-560": ramp(accent)[560],
        "--blurple-50": accent,
        "--blurple-60": ramp(accent)[560],
        "--opacity-blurple-8": rgba(accent, 0.08),
        "--opacity-blurple-16": rgba(accent, 0.16),
        "--opacity-blurple-24": rgba(accent, 0.24),
        "--opacity-blurple-32": rgba(accent, 0.32),
        "--opacity-blurple-60": rgba(accent, 0.6),
        "--text-brand": accent,
        "--control-brand-foreground": accent,
        "--control-brand-foreground-new": accent,
        "--__adaptive-focus-ring-color": accent,
        "--focus-primary": accent,

        # Grounds — the visual-refresh names first, then the classic ones.
        "--app-frame-background": frame,
        "--background-base-lowest": frame,
        "--background-base-lower": side,
        "--background-base-low": chat,
        "--background-surface-high": chat,
        "--background-surface-higher": f.mix("surface0", "base", 0.5) if dark else f.base,
        "--background-surface-highest": raised,
        "--background-gradient-highest": chat,
        "--bg-surface-raised": floating,
        "--bg-surface-overlay": floating,
        "--bg-base-primary": chat,
        "--bg-base-secondary": side,
        "--bg-base-tertiary": frame,
        "--home-background": chat,
        "--chat-background": chat,
        "--chat-background-default": chat,
        "--chat-border": frame,
        "--chat-text-muted": muted,
        "--background-primary": chat,
        "--background-secondary": side,
        "--background-secondary-alt": f.mix("mantle", "crust", 0.5),
        "--background-tertiary": frame,
        "--background-floating": floating,
        "--background-nested-floating": floating,
        "--background-accent": f.surface1,
        "--background-message-hover": rgba(f.crust if dark else f.surface0, 0.3 if dark else 0.45),
        "--message-background-hover": rgba(f.crust if dark else f.surface0, 0.3 if dark else 0.45),
        "--background-modifier-hover": rgba(f.overlay0, hover_a),
        "--background-modifier-active": rgba(f.overlay0, hover_a + 0.06),
        "--background-modifier-selected": rgba(f.overlay0, hover_a + 0.1),
        "--background-modifier-accent": rgba(f.overlay0, 0.24),
        "--background-mod-muted": rgba(f.overlay0, 0.06),
        "--background-mod-subtle": rgba(f.overlay0, hover_a),
        "--background-mod-normal": rgba(f.overlay0, hover_a + 0.06),
        "--background-mod-strong": rgba(f.overlay0, hover_a + 0.14),
        "--interactive-background-hover": rgba(f.overlay0, hover_a),
        "--interactive-background-active": rgba(f.overlay0, hover_a + 0.06),
        "--interactive-background-selected": rgba(f.overlay0, hover_a + 0.1),
        "--modal-background": chat,
        "--modal-footer-background": side,
        "--card-background-default": raised,
        "--custom-channel-members-bg": side,
        "--user-profile-overlay-background": side,
        "--user-profile-overlay-background-hover": f.surface0,
        "--__header-bar-background": side,
        "--deprecated-card-bg": raised,
        "--deprecated-store-bg": chat,
        "--deprecated-quickswitcher-input-background": input_bg,
        "--deprecated-text-input-bg": input_bg,
        "--deprecated-text-input-border": f.surface1 if dark else f.surface0,

        # Borders stay quiet.
        "--border-subtle": f.surface0 if dark else f.crust,
        "--border-muted": f.surface0 if dark else f.crust,
        "--border-normal": f.surface1 if dark else f.surface0,
        "--border-strong": f.surface2 if dark else f.surface1,
        "--border-faint": rgba(f.overlay0, 0.12),

        # Text
        "--text-default": f.text,
        "--text-normal": f.text,
        "--text-strong": f.text_hi,
        "--text-subtle": f.subtext1,
        "--text-muted": muted,
        "--text-link": f.denim,
        "--text-positive": f.green,
        "--text-warning": f.yellow,
        "--text-danger": danger,
        "--text-feedback-positive": f.green,
        "--text-feedback-warning": f.yellow,
        "--text-feedback-critical": danger,
        "--text-feedback-info": f.denim,
        "--header-primary": f.text_hi,
        "--header-secondary": f.subtext0,
        "--channels-default": muted,
        "--channel-icon": muted,
        "--channel-text-area-placeholder": f.overlay1,
        "--textbox-markdown-syntax": f.overlay0,
        "--white": f.text if dark else f.base,
        "--white-500": f.text if dark else f.base,
        "--logo-primary": f.text,

        # Icons and interactive text
        "--icon-default": f.subtext1,
        "--icon-strong": f.text,
        "--icon-subtle": muted,
        "--icon-muted": f.overlay1,
        "--icon-voice-muted": danger,
        "--interactive-normal": f.subtext1,
        "--interactive-hover": f.text,
        "--interactive-active": f.text_hi,
        "--interactive-muted": f.overlay0,
        "--interactive-icon-default": f.subtext1,
        "--interactive-icon-hover": f.text,
        "--interactive-icon-active": f.text_hi,
        "--interactive-text-default": f.subtext1,
        "--interactive-text-hover": f.text,
        "--interactive-text-active": f.text_hi,

        # Composer and inputs
        "--channeltextarea-background": input_bg,
        "--input-background": input_bg,
        "--input-background-default": input_bg,
        "--input-text-default": f.text,
        "--input-placeholder-text-default": f.overlay1,
        "--input-border-default": f.surface1 if dark else f.surface0,
        "--input-border-hover": f.surface2 if dark else f.surface1,
        "--input-border-active": accent,

        # Buttons
        "--control-primary-background-default": accent,
        "--control-primary-background-hover": ramp(accent)[560],
        "--control-primary-background-active": ramp(accent)[600],
        "--control-primary-text-default": ink(f),
        "--control-primary-text-hover": ink(f),
        "--control-secondary-background-default": f.surface1 if dark else f.surface0,
        "--control-secondary-background-hover": f.surface2 if dark else f.surface1,
        "--control-secondary-background-active": f.surface2 if dark else f.surface1,
        "--control-secondary-border-default": f.surface0,
        "--control-secondary-text-default": f.text,
        "--control-secondary-text-hover": f.text_hi,
        "--control-critical-primary-background-default": danger,
        "--control-critical-primary-background-hover": f.red,
        "--control-critical-primary-background-active": f.red,
        "--control-critical-primary-text-default": ink(f),
        "--control-critical-primary-text-hover": ink(f),
        "--control-connected-background-default": f.green,
        "--control-connected-background-hover": f.mix("green", "crust", 0.85),
        "--control-connected-background-active": f.mix("green", "crust", 0.75),
        "--control-connected-border-default": f.green,
        "--control-connected-border-hover": f.mix("green", "crust", 0.85),
        "--control-connected-border-active": f.mix("green", "crust", 0.75),
        "--control-critical-secondary-background-default": "transparent",
        "--control-critical-secondary-background-hover": danger,
        "--control-critical-secondary-background-active": f.red,
        "--control-critical-secondary-border-default": danger,
        "--control-critical-secondary-border-hover": danger,
        "--control-critical-secondary-border-active": f.red,
        "--control-critical-secondary-text-default": danger,
        "--control-critical-secondary-text-hover": ink(f),
        "--control-critical-secondary-text-active": ink(f),
        "--control-critical-secondary-icon-default": danger,
        "--control-critical-secondary-icon-hover": ink(f),
        "--control-critical-secondary-icon-active": ink(f),
        "--button-secondary-background": f.surface1 if dark else f.surface0,
        "--button-secondary-background-hover": f.surface2 if dark else f.surface1,
        "--button-outline-primary-text": f.text,
        "--button-outline-brand-text": f.text,
        "--button-outline-brand-background-hover": ramp(accent)[560],
        "--button-outline-brand-border-active": ramp(accent)[560],
        "--button-danger-background": danger,
        "--button-positive-background": f.green,

        # Mentions, replies, highlights
        "--mention-foreground": accent,
        "--mention-background": rgba(accent, 0.22),
        "--message-reacted-background-default": rgba(accent, 0.18),
        "--message-reacted-text-default": accent,
        "--message-mentioned-background-default": rgba(f.yellow, 0.1),
        "--message-mentioned-background-hover": rgba(f.yellow, 0.14),
        "--background-mentioned": rgba(f.yellow, 0.1),
        "--background-mentioned-hover": rgba(f.yellow, 0.14),
        "--info-warning-foreground": f.yellow,
        "--message-highlight-background-default": rgba(accent, 0.08),
        "--message-highlight-background-hover": rgba(accent, 0.12),
        "--message-automod-background-default": rgba(f.clay, 0.06),
        "--message-automod-background-hover": rgba(f.clay, 0.1),
        "--background-code": f.mantle if dark else f.crust,
        "--spoiler-hidden-background": f.surface2,
        "--spoiler-hidden-background-hover": f.overlay0,
        "--spoiler-revealed-background": f.surface0,

        # Threads: the spines that join a thread to its channel
        "--spine-default": f.surface2 if dark else f.surface1,
        "--thread-channel-spine": f.surface2 if dark else f.surface1,

        # Feedback and status
        "--status-positive": f.green,
        "--status-positive-background": f.green,
        "--status-positive-text": ink(f),
        "--status-warning": f.yellow,
        "--status-warning-background": f.yellow,
        "--status-warning-text": ink(f),
        "--status-danger": danger,
        "--status-danger-background": danger,
        "--status-danger-text": ink(f),
        "--background-feedback-positive": rgba(f.green, 0.14),
        "--background-feedback-warning": rgba(f.yellow, 0.14),
        "--background-feedback-critical": rgba(danger, 0.14),
        "--background-feedback-info": rgba(f.denim, 0.14),
        "--background-feedback-notification": danger,
        "--icon-feedback-notification": danger,
        "--badge-notification-background": danger,
        "--badge-text-brand": ink(f),
        "--icon-feedback-positive": f.green,
        "--icon-feedback-warning": f.yellow,
        "--icon-feedback-critical": danger,
        "--icon-feedback-info": f.denim,
        "--notice-background-positive": f.green,
        "--notice-background-warning": f.yellow,
        "--notice-background-critical": danger,
        "--notice-background-info": f.denim,
        "--notice-text-positive": ink(f),
        "--notice-text-warning": ink(f),
        "--notice-text-critical": ink(f),
        "--notice-text-info": ink(f),
        "--text-status-online": f.green,
        "--text-status-idle": f.yellow,
        "--text-status-dnd": danger,
        "--text-status-offline": f.overlay1,
        "--icon-status-online": f.green,
        "--icon-status-idle": f.yellow,
        "--icon-status-dnd": danger,
        "--icon-status-offline": f.overlay1,
        "--status-green-600": f.green,
        "--status-yellow-500": f.yellow,
        "--status-red-500": danger,
        "--green-360": f.green,
        "--yellow-300": f.yellow,
        "--red-400": danger,

        # Checkboxes, radios, scrollbars
        "--checkbox-background-active": accent,
        "--checkbox-icon-active": ink(f),
        "--checkbox-border-default": f.overlay0,
        "--radio-thumb-background-active": ink(f),
        "--scrollbar-thin-thumb": f.surface2 if dark else f.surface1,
        "--scrollbar-thin-track": "transparent",
        "--scrollbar-auto-thumb": f.surface2 if dark else f.surface1,
        "--scrollbar-auto-track": "transparent",
        "--scrollbar-auto-scrollbar-color-thumb": f.surface2 if dark else f.surface1,
        "--scrollbar-auto-scrollbar-color-track": "transparent",

        # Nitro and partner colors, pulled into the palette
        "--premium-perk-yellow": f.yellow,
        "--premium-perk-orange": f.orange,
        "--premium-perk-green": f.green,
        "--premium-perk-blue": f.denim,
        "--premium-perk-light-blue": f.denim_hi,
        "--premium-perk-dark-blue": f.denim,
        "--premium-perk-purple": f.clay,
        "--premium-perk-pink": f.clay,
        "--guild-boosting-pink": f.clay,
        "--guild-boosting-purple": f.clay,
        "--guild-boosting-blue": f.denim,
        "--premium-tier-0-blue": f.denim,
        "--premium-tier-0-blue-for-gradients": f.denim,
        "--premium-tier-0-blue-for-gradients-2": f.denim_hi,
        "--premium-tier-0-purple": f.clay,
        "--premium-tier-0-purple-for-gradients": f.clay,
        "--premium-tier-1-blue": f.denim,
        "--premium-tier-1-blue-for-gradients": f.denim,
        "--premium-tier-1-dark-blue-for-gradients": f.denim,
        "--premium-tier-1-purple": f.clay,
        "--premium-tier-2-pink": f.orange_hi,
        "--premium-tier-2-pink-for-gradients": f.orange_hi,
        "--premium-tier-2-pink-for-gradients-2": f.orange,
        "--premium-tier-2-purple": f.clay,
        "--premium-tier-2-purple-for-gradients": f.clay,
        "--premium-tier-2-purple-for-gradients-2": f.orange,
        "--spotify": f.green,
    }
    v |= code_variables(f)
    return v


# Discord's code colors: highlight.js in chat, and its newer code renderer, both read these.
CODE = {
    "--text-code": "variable",
    "--text-code-comment": "comment",
    "--text-code-keyword": "keyword",
    "--text-code-operator": "operator",
    "--text-code-title": "function",
    "--text-code-builtin": "function.builtin",
    "--text-code-string": "string",
    "--text-code-escape": "string.escape",
    "--text-code-regexp": "regexp",
    "--text-code-number": "number",
    "--text-code-type": "type",
    "--text-code-variable": "variable",
    "--text-code-property": "property",
    "--text-code-attribute": "attribute",
    "--text-code-namespace": "namespace",
    "--text-code-tag": "tag",
    "--text-code-decorator": "decorator",
    "--text-code-section": "heading",
    "--text-code-bullet": "keyword",
    "--text-code-link": "link",
    "--text-code-error": "invalid",
}


def code_variables(f):
    t = tints(f)
    v = {var: f.syntax(role)[0] for var, role in CODE.items()}
    # Diff blocks: the whole line is one token, so signs and text take green / red_hi on the line tint.
    v |= {
        "--text-code-addition": f.green,
        "--text-code-deletion": f.red_hi,
        "--background-code-addition": t["add"],
        "--background-code-deletion": t["del"],
    }
    return v


# highlight.js token classes (code blocks) — the palette's shared syntax roles.
HLJS = [
    ("comment, .hljs-quote", "comment"),
    ("keyword, .hljs-selector-tag, .hljs-meta .hljs-keyword", "keyword"),
    ("built_in", "function.builtin"),
    ("title, .hljs-title.function_, .hljs-section", "function"),
    ("string, .hljs-meta .hljs-string", "string"),
    ("regexp, .hljs-char.escape_", "regexp"),
    ("number, .hljs-literal, .hljs-symbol", "number"),
    ("type, .hljs-title.class_, .hljs-class .hljs-title", "type"),
    ("attr, .hljs-attribute, .hljs-property", "property"),
    ("variable, .hljs-template-variable, .hljs-params", "parameter"),
    ("tag, .hljs-name", "tag"),
    ("selector-class, .hljs-selector-id, .hljs-selector-attr", "attribute"),
    ("meta, .hljs-doctag", "decorator"),
    ("link", "link"),
]


# Discord re-declares these on more specific selectors (darker/midnight/gradient
# themes, the header bar); catppuccin/discord found they need !important to hold.
IMPORTANT = {
    "--text-muted", "--text-link", "--text-strong", "--background-secondary-alt", "--background-accent",
    "--background-surface-high", "--background-surface-higher", "--background-surface-highest",
    "--background-base-lowest", "--background-base-lower", "--background-base-low",
    "--border-subtle", "--background-mod-subtle", "--background-mod-strong", "--card-background-default",
    "--control-secondary-background-default", "--control-secondary-text-default", "--modal-background",
    "--channels-default", "--channel-icon", "--icon-muted", "--interactive-icon-default",
    "--interactive-text-default", "--message-background-hover", "--__header-bar-background", "--brand-500",
}


def rule(roots, classes, decls):
    """classes: a comma-separated string, or a list when a selector has commas of its own."""
    parts = classes if isinstance(classes, list) else classes.split(",")
    sel = ",\n".join(f"{r} {c.strip()}" for r in roots for c in parts)
    return f"{sel} {{\n" + "\n".join(f"  {d};" for d in decls) + "\n}"


def block(selector, f):
    roots = [r.strip() for r in selector.split(",")]
    lines = [f"{selector} {{"]
    lines += [f"  {k}: {v}{' !important' if k in IMPORTANT else ''};" for k, v in variables(f).items()]
    lines += ["}", "", rule(roots, ".hljs", [f"color: {f.text}"])]
    for cls, role in HLJS:
        color, styles = f.syntax(role)
        decls = [f"color: {color}"]
        if "italic" in styles:
            decls.append("font-style: italic")
        if "bold" in styles:
            decls.append("font-weight: bold")
        lines.append(rule(roots, f".hljs-{cls}", decls))
    t = tints(f)
    lines.append(rule(roots, ".hljs-addition", [f"color: {f.green}", f"background-color: {t['add']}"]))
    lines.append(rule(roots, ".hljs-deletion", [f"color: {f.red_hi}", f"background-color: {t['del']}"]))
    # In a diff block, hunk headers (@@) are denim and file headers (---/+++) bold text.
    diff = ".hljs:has(> .hljs-addition, > .hljs-deletion)"
    lines.append(rule(roots, [f"{diff} > .hljs-meta"], [f"color: {f.denim}", "font-style: normal"]))
    lines.append(rule(roots, [f"{diff} > .hljs-comment"],
                      [f"color: {f.text_hi}", "font-style: normal", "font-weight: bold"]))
    return "\n".join(lines)


def theme(main, dark_f, light_f):
    head = "\n".join([
        "/**",
        f" * @name {main.name}",
        f" * @author {AUTHOR}",
        f" * @version {VERSION}",
        (f" * @description 70s NYC subway seats on walnut paneling: harvest gold, burnt orange and avocado. "
         f"Dark mode: {dark_f.name}; light mode: {light_f.name}."),
        f" * @website {REPO}",
        f" * @source {REPO}",
        " */",
        "",
        f"/* {HEADER} */",
        "",
    ])
    body = [
        f"/* {dark_f.name} — Discord's dark mode */",
        block(DARK_SEL, dark_f),
        "",
        f"/* {light_f.name} — Discord's light mode */",
        block(LIGHT_SEL, light_f),
        "",
        "::selection {",
        f"  background-color: {rgba(main.orange, 0.35)};",
        "}",
    ]
    return head + "\n".join(body) + "\n"


def build(flavors):
    by = {f.id: f for f in flavors}
    pairs = {"walnut": ("walnut", "enamel"), "tunnel": ("tunnel", "enamel"), "enamel": ("walnut", "enamel")}
    outs = []
    for f in flavors:
        dark_f, light_f = pair(f)
        dark_id, light_id = dark_f.id, light_f.id
        outs.append(Out(f"{f.slug}.theme.css", theme(f, by[dark_id], by[light_id]), flavor=f.id, lang="css",
                        dest=f"~/Library/Application Support/Vencord/themes/{f.slug}.theme.css", how=FOLDERS))
    return outs
