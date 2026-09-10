"""Obsidian: a community theme (manifest.json + theme.css). Walnut in dark mode, Enamel in
light mode, Tunnel as a Style Settings toggle (or a CSS snippet). Written against the
Obsidian 1.13 variable set, where callout and canvas colors are plain colors."""

import colorsys
import json

import palette as p
from ports._apps import AUTHOR, AUTHOR_URL, rgba
from ports._lib import HEADER, VERSION, Out, ink, tints, ui_colors

META = {
    "id": "obsidian",
    "name": "Obsidian",
    "category": "Apps",
    "homepage": "https://obsidian.md",
    "enable": {
        "where": "Obsidian › Settings › Appearance",
        "code": "Themes › Subway Seat\n"
        "Base color scheme › Dark for Walnut and Tunnel, Light for Enamel\n"
        "Tunnel: Style Settings › Subway Seat › Tunnel (deeper dark), or CSS snippets › subway-seat-tunnel",
        "lang": "text",
    },
    "auto": {
        "where": "Obsidian › Settings › Appearance",
        "code": "Base color scheme › Adapt to system\n"
        "# Enamel while the system is light, Walnut (or Tunnel, if it's on) while it's dark",
        "lang": "text",
    },
    "requires": "Obsidian 1.13+",
    "detect": ["/Applications/Obsidian.app", "obsidian"],
    "notes": "A full community theme: Walnut in dark mode, Enamel in light mode, and Tunnel as a "
    "Style Settings toggle or a CSS snippet. Headings run the 70s stripe from burnt orange to "
    "terracotta, and callouts, code, diffs, graph and canvas stay in the same warm room.",
}

NAME = "Subway Seat"
MIN_APP = "1.13.0"  # 1.13 moved callout/canvas colors from "r, g, b" triplets to plain colors
TUNNEL_CLASS = "subway-seat-tunnel"


def triplet(color):
    return ", ".join(str(v) for v in p.hex_to_rgb(color))


def hsl(color):
    r, g, b = (v / 255 for v in p.hex_to_rgb(color))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    return f"{hue * 360:.1f}", f"{sat * 100:.1f}%", f"{light * 100:.1f}%"


def extended(f):
    """Obsidian's eight named colors, mapped into the palette (cyan→sage, blue→denim,
    purple→Sixth Avenue orange, pink→terracotta): denim stays the only cool color.
    Red takes the bright step on dark grounds."""
    return {
        "red": f.red_hi if f.dark else f.red,
        "orange": f.orange,
        "yellow": f.yellow,
        "green": f.green,
        "cyan": f.sage,
        "blue": f.denim,
        "purple": f.orange_hi,
        "pink": f.clay,
    }


def groups(f):
    """[(section comment, {variable: value})] for one flavor."""
    d = f.dark
    x = extended(f)
    ah, as_, al = hsl(f.orange)
    hover = rgba(f.overlay1, 0.14 if d else 0.16)
    accent = "var(--color-accent)"
    paper = ui_colors(f)["paper"]  # menus, prompts and suggestions are raised onto paper
    t = tints(f)

    ramp = (
        {
            "00": f.base, "05": f.mix("surface0", "base", 0.5), "10": f.surface0,
            "20": f.mix("surface1", "surface0", 0.5), "25": f.surface1,
            "30": f.mix("surface2", "surface1", 0.4), "35": f.surface2, "40": f.overlay0,
            "50": f.overlay1, "60": f.overlay2, "70": f.subtext0, "100": f.text,
        }
        if d
        else {
            "00": f.base, "05": f.mix("mantle", "base", 0.5), "10": f.mantle, "20": f.crust,
            "25": f.surface0, "30": f.mix("surface1", "surface0", 0.5), "35": f.surface1,
            "40": f.surface2, "50": f.overlay0, "60": f.overlay1, "70": f.subtext0, "100": f.text,
        }
    )
    l1, l2 = ("1.1", "1.2") if d else ("1.08", "1.16")

    out = []
    out.append(("Palette: the base ramp runs from the editor ground to parchment text", {
        **{f"--color-base-{k}": v for k, v in ramp.items()},
        **{f"--color-{k}": v for k, v in x.items()},
        **{f"--color-{k}-rgb": triplet(v) for k, v in x.items()},
    }))
    out.append(("Accent: burnt orange, still overridable under Settings › Appearance", {
        "--accent-h": ah,
        "--accent-s": as_,
        "--accent-l": al,
        "--color-accent": "hsl(var(--accent-h), var(--accent-s), var(--accent-l))",
        "--color-accent-hsl": "var(--accent-h), var(--accent-s), var(--accent-l)",
        "--color-accent-1": f"hsl(calc(var(--accent-h) + 1), calc(var(--accent-s) * 1.1), calc(var(--accent-l) * {l1}))",
        "--color-accent-2": f"hsl(calc(var(--accent-h) + 2), calc(var(--accent-s) * 1.15), calc(var(--accent-l) * {l2}))",
    }))
    out.append(("Grounds: editor walnut, sidebars espresso, title bar and ribbon tunnel", {
        "--background-primary": f.base,
        "--background-primary-alt": f.mix("mantle", "base", 0.5),
        "--background-secondary": f.mantle,
        "--background-secondary-alt": f.base,
        "--background-modifier-hover": hover,
        "--background-modifier-active-hover": f"color-mix(in srgb, {accent} 14%, transparent)",
        "--background-modifier-border": f.surface0,
        "--background-modifier-border-hover": f.surface1,
        "--background-modifier-border-focus": f.orange,
        "--background-modifier-error": x["red"],
        "--background-modifier-error-hover": f.red if d else f.red_hi,
        "--background-modifier-warning": f.yellow,
        "--background-modifier-warning-hover": f.yellow_hi,
        "--background-modifier-success": f.green,
        "--background-modifier-form-field": f.surface0 if d else f.base,
        "--background-modifier-form-field-hover": f.surface0 if d else f.base,
        "--background-modifier-cover": rgba(f.crust, 0.6 if d else 0.5),
        "--background-modifier-box-shadow": rgba(f.crust, 0.5) if d else rgba(f.overlay2, 0.14),
        "--background-modifier-message": rgba(f.crust if d else f.text_hi, 0.92),
        "--workspace-background-translucent": rgba(f.crust if d else f.base, 0.6),
    }))
    out.append(("Text", {
        "--text-normal": f.text,
        "--text-muted": f.subtext0,
        "--text-faint": f.overlay1,
        "--text-on-accent": ink(f),
        "--text-on-accent-inverted": f.crust if d else f.text_hi,
        "--text-accent": accent,
        "--text-accent-hover": "var(--color-accent-1)",
        "--text-error": x["red"],
        "--text-warning": f.yellow,
        "--text-success": f.green,
        "--text-selection": f"color-mix(in srgb, {accent} {30 if d else 22}%, transparent)",
        "--text-highlight-bg": rgba(f.yellow if d else f.yellow_hi, 0.3 if d else 0.32),
        "--text-highlight-bg-rgb": triplet(f.yellow if d else f.yellow_hi),
        "--caret-color": f.yellow if d else f.orange,
        "--bold-color": f.text_hi,
        "--italic-color": "inherit",
    }))
    out.append(("Interactive", {
        "--interactive-normal": f.surface0 if d else f.base,
        "--interactive-hover": f.surface1 if d else f.surface0,
        "--interactive-accent": accent,
        "--interactive-accent-hsl": "var(--color-accent-hsl)",
        "--interactive-accent-hover": "var(--color-accent-1)",
        "--dropdown-background": "var(--interactive-normal)",
        "--dropdown-background-hover": "var(--interactive-hover)",
        "--toggle-thumb-color": f.text_hi if d else f.base,
        "--slider-thumb-background": f.text_hi if d else f.base,
        "--slider-thumb-background-hover": f.text_hi if d else f.base,
        "--slider-track-background": f.surface1,
        "--input-placeholder-color": f.overlay1,
        "--flair-background": f.surface0,
        "--flair-color": f.subtext1,
        "--pill-color": f.subtext0,
        "--pill-color-hover": f.text,
        "--pill-color-remove": f.overlay1,
        "--pill-color-remove-hover": f.orange,
        "--pill-border-color": f.surface1,
        "--pill-border-color-hover": f.surface2,
        "--search-icon-color": f.subtext0,
        "--search-clear-button-color": f.subtext0,
    }))
    out.append(("Headings: the 70s stripe, burnt orange down to terracotta", {
        "--h1-color": f.orange,
        "--h2-color": f.yellow,
        "--h3-color": f.green,
        "--h4-color": f.sage,
        "--h5-color": x["red"],
        "--h6-color": f.clay,
        "--heading-formatting": f.overlay0,
        "--inline-title-color": f.text_hi,
    }))
    out.append(("Links and tags: denim is the only cool color, tags wear orange", {
        "--link-color": f.denim,
        "--link-color-hover": f.denim_hi,
        "--link-external-color": f.denim,
        "--link-external-color-hover": f.denim_hi,
        "--link-unresolved-color": f.denim,
        "--link-unresolved-opacity": "0.65",
        "--link-unresolved-decoration-style": "dotted",
        "--link-unresolved-decoration-color": rgba(f.denim, 0.5),
        "--tag-color": f.orange,
        "--tag-color-hover": f.orange_hi if d else f.orange,
        "--tag-background": rgba(f.orange, 0.12),
        "--tag-background-hover": rgba(f.orange, 0.2),
        "--tag-border-color": rgba(f.orange, 0.18),
        "--tag-border-color-hover": rgba(f.orange, 0.3),
    }))
    out.append(("Code: the same syntax roles as every editor port", {
        "--code-background": f.mantle,
        "--code-border-color": f.surface0,
        "--code-bracket-background": hover,
        "--code-normal": f.syntax("variable")[0],
        "--code-comment": f.syntax("comment")[0],
        "--code-function": f.syntax("function")[0],
        "--code-important": f.syntax("regexp")[0],
        "--code-keyword": f.syntax("keyword")[0],
        "--code-operator": f.syntax("operator")[0],
        "--code-property": f.syntax("property")[0],
        "--code-punctuation": f.syntax("punctuation")[0],
        "--code-string": f.syntax("string")[0],
        "--code-tag": f.syntax("tag")[0],
        "--code-value": f.syntax("number")[0],
    }))
    out.append(("Diffs in code blocks: line tints, green and red signs, denim hunk headers", {
        "--ss-diff-add": t["add"],
        "--ss-diff-del": t["del"],
        "--ss-diff-chg": t["chg"],
        "--ss-diff-add-fg": f.green,
        "--ss-diff-del-fg": f.red_hi,
        "--ss-diff-chg-fg": f.yellow,
        "--ss-diff-header": f.denim,
    }))
    out.append(("Callouts, by type", {
        "--callout-default": f.denim,
        "--callout-info": f.denim,
        "--callout-todo": f.denim,
        "--callout-summary": f.sage,
        "--callout-tip": f.sage,
        "--callout-important": f.orange,
        "--callout-success": f.green,
        "--callout-question": f.clay,
        "--callout-warning": f.yellow,
        "--callout-fail": x["red"],
        "--callout-error": x["red"],
        "--callout-bug": x["red"],
        "--callout-example": x["purple"],
        "--callout-quote": f.overlay1,
    }))
    out.append(("Blocks: quotes, checklists, lists, rules, tables, properties", {
        "--blockquote-border-color": f.clay,
        "--blockquote-color": f.subtext1,
        "--blockquote-background-color": "transparent",
        "--checkbox-color": accent,
        "--checkbox-color-hover": "var(--color-accent-1)",
        "--checkbox-border-color": f.overlay0,
        "--checkbox-border-color-hover": f.overlay1,
        "--checkbox-marker-color": ink(f),
        "--checklist-done-color": f.overlay1,
        "--list-marker-color": f.overlay1,
        "--list-marker-color-hover": f.subtext0,
        "--list-marker-color-collapsed": f.orange,
        "--collapse-icon-color": f.overlay1,
        "--collapse-icon-color-collapsed": f.orange,
        "--hr-color": f.surface1,
        "--table-border-color": f.surface1 if d else f.surface0,
        "--table-header-background": f.mantle,
        "--table-header-background-hover": f.surface0,
        "--table-header-border-color": f.surface1 if d else f.surface0,
        "--table-header-color": f.text_hi,
        "--table-row-alt-background": f.mix("mantle", "base", 0.4),
        "--table-row-alt-background-hover": hover,
        "--table-row-background-hover": hover,
        "--table-selection": f"color-mix(in srgb, {accent} 12%, transparent)",
        "--table-selection-border-color": accent,
        "--table-drag-handle-color": f.overlay1,
        "--table-add-button-border-color": f.surface1,
        "--metadata-border-color": f.surface0,
        "--metadata-divider-color": f.surface0,
        "--metadata-label-text-color": f.subtext0,
        "--metadata-input-text-color": f.text,
        "--embed-border-start": f"2px solid {f.surface2 if d else f.surface1}",
    }))
    out.append(("Graph and canvas", {
        "--graph-text": f.text,
        "--graph-line": f.surface2 if d else f.surface1,
        "--graph-node": f.subtext0,
        "--graph-node-unresolved": f.overlay0,
        "--graph-node-focused": f.orange,
        "--graph-node-tag": f.green,
        "--graph-node-attachment": f.yellow,
        "--canvas-background": f.base,
        "--canvas-dot-pattern": f.surface1 if d else f.surface0,
        "--canvas-card-label-color": f.overlay1,
        "--canvas-color": f.overlay1 if d else f.surface2,  # cards and edges with no color picked
        "--canvas-color-1": x["red"],
        "--canvas-color-2": f.orange,
        "--canvas-color-3": f.yellow,
        "--canvas-color-4": f.green,
        "--canvas-color-5": f.sage,
        "--canvas-color-6": f.denim,
    }))
    out.append(("Window: title bar, ribbon, tabs, status bar, dividers", {
        "--titlebar-background": f.crust,
        "--titlebar-background-focused": f.crust,
        "--titlebar-border-color": f.crust,
        "--titlebar-text-color": f.subtext0,
        "--titlebar-text-color-focused": f.text,
        "--ribbon-background": f.crust,
        "--ribbon-background-collapsed": f.crust,
        "--tab-container-background": f.crust,
        "--tab-background-active": f.base,
        "--tab-text-color": f.overlay1,
        "--tab-text-color-active": f.subtext0,
        "--tab-text-color-focused": f.subtext0,
        "--tab-text-color-focused-active": f.subtext1,
        "--tab-text-color-focused-active-current": f.text,
        "--tab-text-color-focused-highlighted": f.orange,
        "--tab-divider-color": f.surface0 if d else f.surface1,
        "--tab-outline-color": f.crust,
        "--status-bar-background": f.mantle,
        "--status-bar-border-color": f.crust,
        "--status-bar-text-color": f.subtext0,
        "--divider-color": f.crust,
        "--divider-color-hover": accent,
        "--vault-profile-color": f.text,
        "--vault-profile-color-hover": f.text_hi,
    }))
    out.append(("Navigation, icons, scrollbars", {
        "--nav-item-color": f.subtext0,
        "--nav-item-color-hover": f.text,
        "--nav-item-color-active": f.text,
        "--nav-item-color-selected": f.text,
        "--nav-item-color-highlighted": f.orange,
        "--nav-item-background-hover": hover,
        "--nav-item-background-active": f.surface0,
        "--nav-item-background-selected": f"color-mix(in srgb, {accent} 16%, transparent)",
        "--nav-heading-color": f.text,
        "--nav-heading-color-hover": f.text_hi,
        "--nav-heading-color-collapsed": f.overlay1,
        "--nav-heading-color-collapsed-hover": f.subtext0,
        "--nav-tag-color": f.overlay1,
        "--nav-tag-color-hover": f.subtext0,
        "--nav-tag-color-active": f.subtext0,
        "--icon-color": f.subtext0,
        "--icon-color-hover": f.text,
        "--icon-color-active": f.orange,
        "--icon-color-focused": f.text,
        "--indentation-guide-color": f.surface1 if d else f.surface0,
        "--indentation-guide-color-active": f.overlay0,
        "--scrollbar-bg": "transparent",
        "--scrollbar-thumb-bg": rgba(f.overlay1, 0.28),
        "--scrollbar-active-thumb-bg": rgba(f.overlay1, 0.5),
    }))
    out.append(("Menus, modals, prompts, popovers, PDFs", {
        "--menu-background": paper,
        "--menu-border-color": f.surface1,
        "--modal-background": f.base,
        "--modal-border-color": f.surface1,
        "--prompt-background": paper,
        "--prompt-border-color": f.surface1,
        "--suggestion-background": paper,
        "--setting-items-background": f.mix("mantle", "base", 0.5),
        "--setting-items-border-color": f.surface0,
        "--drag-ghost-background": rgba(f.crust if d else f.text_hi, 0.9),
        "--drag-ghost-text-color": f.text if d else f.base,
        "--pdf-background": f.mantle,
        "--pdf-sidebar-background": f.mantle,
        "--pdf-page-background": f.base,
    }))
    return out


def flat(f):
    return {k: v for _, vars_ in groups(f) for k, v in vars_.items()}


# Obsidian sets these on `body.theme-dark` / `body` rather than `.theme-dark`, so ours need
# `body` in the selector to win.
ON_BODY = {"--canvas-color"}


def block(selector, grouped):
    lines = [f"{selector} {{"]
    on_body = {}
    for i, (comment, vars_) in enumerate(grouped):
        vars_ = {k: v for k, v in vars_.items() if k not in ON_BODY or on_body.update({k: v})}
        if not vars_:
            continue
        if i:
            lines.append("")
        lines.append(f"  /* {comment} */")
        lines += [f"  {k}: {v};" for k, v in vars_.items()]
    lines.append("}")
    if on_body:
        lines += ["", f"body{selector} {{", *(f"  {k}: {v};" for k, v in on_body.items()), "}"]
    return "\n".join(lines)


# Prism draws code blocks in reading view: tint diff lines, keep their text in the normal code
# color with a green or red sign, and make hunk headers denim. The editor's diff tokens just
# take the sign colors.
DIFF_RULES = """/* Diffs in code blocks */
.markdown-rendered .language-diff .token.inserted:not(.prefix),
.markdown-rendered .language-diff .token.deleted:not(.prefix),
.markdown-rendered .language-diff .token.diff:not(.prefix) {
  display: block;
  color: var(--code-normal);
}
.markdown-rendered .language-diff .token.inserted:not(.prefix) { background-color: var(--ss-diff-add); }
.markdown-rendered .language-diff .token.deleted:not(.prefix) { background-color: var(--ss-diff-del); }
.markdown-rendered .language-diff .token.diff:not(.prefix) { background-color: var(--ss-diff-chg); font-weight: inherit; }
.markdown-rendered .language-diff .token.prefix.inserted { color: var(--ss-diff-add-fg); }
.markdown-rendered .language-diff .token.prefix.deleted { color: var(--ss-diff-del-fg); }
.markdown-rendered .language-diff .token.prefix.diff { color: var(--ss-diff-chg-fg); }
.markdown-rendered .language-diff .token.coord { color: var(--ss-diff-header); }
.cm-positive { color: var(--ss-diff-add-fg); }
.cm-negative { color: var(--ss-diff-del-fg); }"""


def tunnel_diff(base_f, tunnel_f):
    """Only the variables where Tunnel differs from Walnut (the grounds)."""
    a = flat(base_f)
    return {k: v for k, v in flat(tunnel_f).items() if a.get(k) != v}


SETTINGS = f"""/* @settings

name: {NAME}
id: subway-seat
settings:
    -
        id: {TUNNEL_CLASS}
        title: Tunnel (deeper dark)
        description: Swap the walnut grounds for Tunnel's espresso-deep ones in dark mode. Accents stay the same.
        type: class-toggle
        default: false
        addCommand: true

*/"""


def theme_css(walnut, tunnel, enamel):
    diff = tunnel_diff(walnut, tunnel)
    parts = [
        (
            f"/* {HEADER}\n\n"
            f"   {NAME} for Obsidian {MIN_APP}+\n"
            "   Dark mode is Walnut, light mode is Enamel. Tunnel, the deeper dark, is opt-in: turn it on\n"
            f"   with the Style Settings plugin, or add the `{TUNNEL_CLASS}` class to <body> any other way.\n"
            "   Without Style Settings, the subway-seat-tunnel.css snippet does the same job. */"
        ),
        SETTINGS,
        block(".theme-dark", groups(walnut)),
        block(f".theme-dark.{TUNNEL_CLASS}", [("Tunnel: deeper grounds, same warm lights", diff)]),
        block(".theme-light", groups(enamel)),
        DIFF_RULES,
    ]
    return "\n\n".join(parts) + "\n"


def snippet_css(walnut, tunnel):
    diff = tunnel_diff(walnut, tunnel)
    head = (
        f"/* {HEADER}\n\n"
        "   Subway Seat Tunnel for Obsidian, as a CSS snippet: use it with the Subway Seat theme when\n"
        "   you don't run Style Settings. Settings › Appearance › CSS snippets › subway-seat-tunnel. */"
    )
    return head + "\n\n" + block(".theme-dark", [("Tunnel: deeper grounds, same warm lights", diff)]) + "\n"


def manifest():
    return json.dumps({
        "name": NAME,
        "version": VERSION,
        "minAppVersion": MIN_APP,
        "author": AUTHOR,
        "authorUrl": AUTHOR_URL,
    }, indent=2) + "\n"


def build(flavors):
    by_id = {f.id: f for f in flavors}
    walnut, tunnel, enamel = by_id["walnut"], by_id["tunnel"], by_id["enamel"]
    # Paths are relative to the vault folder.
    dest = f".obsidian/themes/{NAME}"
    how = "inside your vault's folder"
    return [
        Out(f"{NAME}/manifest.json", manifest(), dest=f"{dest}/manifest.json", lang="json", how=how),
        Out(f"{NAME}/theme.css", theme_css(walnut, tunnel, enamel), dest=f"{dest}/theme.css", lang="css", how=how),
        Out("snippets/subway-seat-tunnel.css", snippet_css(walnut, tunnel), flavor="tunnel",
            dest=".obsidian/snippets/subway-seat-tunnel.css", lang="css",
            how="inside your vault's folder; only needed without the Style Settings plugin"),
    ]
