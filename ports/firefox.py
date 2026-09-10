"""Firefox: a static theme per flavor (manifest + unsigned .xpi), plus a
Firefox Color share link that opens the same colors in color.firefox.com."""

import base64
import json
import lzma
import struct

import palette as p
from ports._apps import AUTHOR, DESCRIPTION
from ports._lib import HEADER, REPO, VERSION, Out, selection, solid, ui_colors, zip_bytes

META = {
    "id": "firefox",
    "name": "Firefox",
    "category": "Apps",
    "homepage": "https://www.firefox.com",
    "enable": {
        "where": "Firefox: the Firefox Color link, or about:addons for the .xpi",
        "code": "Release Firefox: open the link in {slug}.firefox-color.txt with the Firefox Color add-on installed.\n"
        "Developer Edition, Nightly or ESR, with xpinstall.signatures.required set to false in about:config:\n"
        "about:addons › ⚙ › Install Add-on From File… › {slug}.xpi\n"
        "To try it on release Firefox until the next restart: about:debugging › This Firefox › "
        "Load Temporary Add-on… › {slug}.xpi",
        "lang": "text",
    },
    "auto": {
        "where": "about:addons (Developer Edition, Nightly or ESR, as above)",
        "code": "about:addons › ⚙ › Install Add-on From File… › subway-seat-auto.xpi\n"
        "# Enamel while the system is light, Subway Seat (Walnut) while it's dark",
        "lang": "text",
    },
    "requires": "Firefox 106+",
    "detect": [
        "/Applications/Firefox.app", "/Applications/Firefox Developer Edition.app", "/Applications/Firefox Nightly.app",
        "firefox",
    ],
    "notes": "A static theme for tabs, toolbar, address bar, menus, sidebar and the new-tab page. The .xpi files "
    "are unsigned, so release Firefox only takes them until a restart; the Firefox Color link installs "
    "for good. subway-seat-auto.xpi follows the system: Enamel when it's light, Walnut when it's dark.",
}


def colors(f):
    """Firefox/Thunderbird theme.colors, shared by both ports."""
    dark = f.dark
    line = f.surface0 if dark else f.surface1  # quiet separators
    paper = ui_colors(f)["paper"]  # popovers are raised onto paper
    return {
        "frame": f.crust,
        "frame_inactive": f.crust if dark else f.mantle,
        "tab_background_text": f.overlay2,
        "tab_background_separator": line,
        "tab_selected": f.base,
        "tab_text": f.text,
        "tab_line": f.orange,
        "tab_loading": f.orange,
        "toolbar": f.base,
        "toolbar_text": f.text,
        "toolbar_top_separator": f.crust,
        "toolbar_bottom_separator": line,
        "toolbar_vertical_separator": line,
        "icons": f.subtext1,
        "icons_attention": f.orange,
        "button_background_hover": f.surface0,
        "button_background_active": f.surface1,
        "toolbar_field": f.mantle,
        "toolbar_field_text": f.text,
        "toolbar_field_border": line,
        "toolbar_field_focus": f.mantle if dark else f.base,
        "toolbar_field_text_focus": f.text_hi,
        "toolbar_field_border_focus": f.orange,
        "toolbar_field_highlight": selection(f),
        "toolbar_field_highlight_text": f.text_hi,
        "toolbar_field_separator": line,
        "popup": paper,
        "popup_text": f.text,
        "popup_border": solid("text@EDGE", f, "paper"),
        "popup_highlight": selection(f),
        "popup_highlight_text": f.text_hi,
        "sidebar": f.mantle,
        "sidebar_text": f.text,
        "sidebar_border": line,
        "sidebar_highlight": selection(f),
        "sidebar_highlight_text": f.text_hi,
        "ntp_background": f.base,
        "ntp_card_background": f.surface0 if dark else f.mantle,
        "ntp_text": f.text,
    }


MIN_VERSION = "106.0"  # the color_scheme / content_color_scheme properties


def theme(f, colors_of=None):
    """One `theme` (or `dark_theme`) object: colors plus the color-scheme hint."""
    scheme = "dark" if f.dark else "light"
    return {
        "colors": (colors_of or colors)(f),
        "properties": {"color_scheme": scheme, "content_color_scheme": scheme},
    }


def manifest(f, name=None, slug=None, description=None, dark=None, colors_of=None):
    """A static theme for flavor f; with `dark`, f is the light theme and `dark` follows the system's dark mode."""
    m = {
        "manifest_version": 2,
        "name": name or f.name,
        "version": VERSION,
        "description": description or f"{DESCRIPTION} {f.blurb}",
        "author": AUTHOR,
        "homepage_url": REPO,
        "browser_specific_settings": {
            "gecko": {"id": f"{slug or f.slug}@oddurs.github.io", "strict_min_version": MIN_VERSION},
        },
        "theme": theme(f, colors_of),
    }
    if dark is not None:
        m["dark_theme"] = theme(dark, colors_of)
    return m


def auto_manifest(light, dark, colors_of=None):
    return manifest(
        light, name="Subway Seat Auto", slug="subway-seat-auto", dark=dark, colors_of=colors_of,
        description=f"{DESCRIPTION} Follows the system: {light.name} when it's light, {dark.name} when it's dark.",
    )


# ── Firefox Color share link ───────────────────────────────────────────────
# color.firefox.com/?theme=<json-url "lzma" codec>: msgpack → LZMA ("alone"
# format) → URL-safe base64 without padding. Verified by decoding with json-url.
FIREFOX_COLOR_KEYS = [
    "toolbar", "toolbar_text", "frame", "tab_background_text", "toolbar_field", "toolbar_field_text",
    "tab_line", "popup", "popup_text", "button_background_active", "button_background_hover",
    "frame_inactive", "icons_attention", "icons", "ntp_background", "ntp_text", "popup_border",
    "popup_highlight_text", "popup_highlight", "sidebar_border", "sidebar_highlight_text",
    "sidebar_highlight", "sidebar_text", "sidebar", "tab_background_separator", "tab_loading",
    "tab_selected", "tab_text", "toolbar_bottom_separator", "toolbar_field_border_focus",
    "toolbar_field_border", "toolbar_field_focus", "toolbar_field_highlight_text",
    "toolbar_field_highlight", "toolbar_field_separator", "toolbar_field_text_focus",
    "toolbar_top_separator", "toolbar_vertical_separator",
]


def msgpack(obj):
    """Just enough MessagePack for dicts, lists, short strings and small ints."""
    if isinstance(obj, dict):
        n = len(obj)
        head = bytes([0x80 | n]) if n < 16 else b"\xde" + struct.pack(">H", n)
        return head + b"".join(msgpack(k) + msgpack(v) for k, v in obj.items())
    if isinstance(obj, list):
        n = len(obj)
        head = bytes([0x90 | n]) if n < 16 else b"\xdc" + struct.pack(">H", n)
        return head + b"".join(msgpack(v) for v in obj)
    if isinstance(obj, str):
        b = obj.encode()
        n = len(b)
        if n < 32:
            return bytes([0xA0 | n]) + b
        if n < 256:
            return b"\xd9" + bytes([n]) + b
        return b"\xda" + struct.pack(">H", n) + b
    if isinstance(obj, int) and 0 <= obj < 256:
        return bytes([obj]) if obj < 128 else b"\xcc" + bytes([obj])
    raise TypeError(f"msgpack: unsupported {obj!r}")


def firefox_color_url(f):
    c = colors(f)
    theme = {
        "colors": {k: dict(zip("rgb", p.hex_to_rgb(c[k]), strict=True)) for k in FIREFOX_COLOR_KEYS},
        "images": {"additional_backgrounds": ["./bg-000.svg"], "custom_backgrounds": []},
        "title": f.name,
    }
    raw = lzma.compress(
        msgpack(theme), format=lzma.FORMAT_ALONE,
        filters=[{"id": lzma.FILTER_LZMA1, "preset": 9, "dict_size": 1 << 16}],
    )
    return "https://color.firefox.com/?theme=" + base64.urlsafe_b64encode(raw).decode().rstrip("=")


XPI_HOW = "about:addons › ⚙ › Install Add-on From File… (Developer Edition, Nightly or ESR)"


def build(flavors):
    by = {f.id: f for f in flavors}
    outs = []
    for f in flavors:
        m = json.dumps(manifest(f), indent=2) + "\n"
        outs.append(Out(f"{f.slug}/manifest.json", m, flavor=f.id, lang="json", how=f"inside {f.slug}.xpi"))
        outs.append(Out(f"{f.slug}.xpi", zip_bytes({"manifest.json": m}), flavor=f.id, how=XPI_HOW))
        url = firefox_color_url(f)
        outs.append(Out(f"{f.slug}.firefox-color.txt",
                        f"# {HEADER}\n# {f.name} for Firefox Color (addons.mozilla.org/firefox/addon/firefox-color)\n{url}\n",
                        flavor=f.id, lang="text", how="open the link in Firefox with the Firefox Color add-on installed"))
    auto = json.dumps(auto_manifest(by["enamel"], by["walnut"]), indent=2) + "\n"
    outs.append(Out("subway-seat-auto/manifest.json", auto, lang="json", how="inside subway-seat-auto.xpi"))
    outs.append(Out("subway-seat-auto.xpi", zip_bytes({"manifest.json": auto}), how=XPI_HOW))
    return outs
