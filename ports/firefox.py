"""Firefox: a static theme per flavor (manifest + unsigned .xpi), plus a
Firefox Color share link that opens the same colours in color.firefox.com."""

import base64
import json
import lzma
import struct

import palette as p
from ports._apps import AUTHOR, DESCRIPTION, VERSION, select, zip_bytes
from ports._lib import HEADER, REPO, Out

META = {
    "id": "firefox",
    "name": "Firefox",
    "category": "Apps",
    "homepage": "https://www.firefox.com",
    "enable": {
        "where": "Firefox → about:addons (or open the Firefox Color link)",
        "code": "Open {slug}.firefox-color.txt's link with the Firefox Color add-on installed,\n"
        "or load {slug}.xpi from about:debugging → This Firefox → Load Temporary Add-on.",
        "lang": "text",
    },
    "notes": "A static theme for tabs, toolbar, address bar, menus, sidebar and the new-tab page. "
    "The .xpi is unsigned, so the Firefox Color link is the easiest permanent install on release Firefox.",
}


def colors(f):
    """Firefox/Thunderbird theme.colors, shared by both ports."""
    dark = f.dark
    line = f.surface0 if dark else f.surface1  # quiet separators
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
        "toolbar_field_highlight": select(f),
        "toolbar_field_highlight_text": f.text_hi,
        "toolbar_field_separator": line,
        "popup": f.mantle if dark else f.base,
        "popup_text": f.text,
        "popup_border": line,
        "popup_highlight": select(f),
        "popup_highlight_text": f.text_hi,
        "sidebar": f.mantle,
        "sidebar_text": f.text,
        "sidebar_border": line,
        "sidebar_highlight": select(f),
        "sidebar_highlight_text": f.text_hi,
        "ntp_background": f.base,
        "ntp_card_background": f.surface0 if dark else f.mantle,
        "ntp_text": f.text,
    }


def manifest(f):
    return {
        "manifest_version": 2,
        "name": f.name,
        "version": VERSION,
        "description": f"{DESCRIPTION} {f.blurb} ({HEADER})",
        "author": AUTHOR,
        "homepage_url": REPO,
        "browser_specific_settings": {
            "gecko": {"id": f"{f.slug}@oddurs.github.io", "strict_min_version": "106.0"},
        },
        "theme": {
            "colors": colors(f),
            "properties": {
                "color_scheme": "dark" if f.dark else "light",
                "content_color_scheme": "dark" if f.dark else "light",
            },
        },
    }


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
        "colors": {k: dict(zip("rgb", p.hex_to_rgb(c[k]))) for k in FIREFOX_COLOR_KEYS},
        "images": {"additional_backgrounds": ["./bg-000.svg"], "custom_backgrounds": []},
        "title": f.name,
    }
    raw = lzma.compress(
        msgpack(theme), format=lzma.FORMAT_ALONE,
        filters=[{"id": lzma.FILTER_LZMA1, "preset": 9, "dict_size": 1 << 16}],
    )
    return "https://color.firefox.com/?theme=" + base64.urlsafe_b64encode(raw).decode().rstrip("=")


def build(flavors):
    outs = []
    for f in flavors:
        m = json.dumps(manifest(f), indent=2) + "\n"
        outs.append(Out(f"{f.slug}/manifest.json", m, flavor=f.id,
                        dest="inside the .xpi (about:debugging → Load Temporary Add-on)", lang="json"))
        outs.append(Out(f"{f.slug}.xpi", zip_bytes({"manifest.json": m}), flavor=f.id,
                        dest="about:addons → ⚙ → Install Add-on From File (Developer/Nightly/ESR)"))
        url = firefox_color_url(f)
        outs.append(Out(f"{f.slug}.firefox-color.txt",
                        f"# {HEADER}\n# {f.name} for Firefox Color (addons.mozilla.org/firefox/addon/firefox-color)\n{url}\n",
                        flavor=f.id, dest="open in Firefox with Firefox Color installed", lang="text"))
    return outs
