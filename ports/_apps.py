"""Shared bits for the desktop-app and browser ports (category "Apps")."""

import io
import uuid
import zipfile

import palette as p

VERSION = "0.2.0"
AUTHOR = "Oddur Sigurdsson"
AUTHOR_URL = "https://github.com/oddurs"
DESCRIPTION = "A walnut-brown 1970s NYC subway theme: harvest gold, burnt orange and avocado on warm wood."
_NS = uuid.UUID("5b0b3a52-7d1e-4c55-9a7e-5ea7ee5ea700")  # fixed, so ids are stable across builds


def ink(f):
    """Text on an accent fill: the darkest ground in dark flavors, the lightest in light."""
    return f.crust if f.dark else f.base


def select(f):
    """Selected/highlighted row ground (matches the terminal selection)."""
    return f.surface2 if f.dark else f.surface1


def rgb_list(color):
    return list(p.hex_to_rgb(color))


def rgba(color, a):
    r, g, b = p.hex_to_rgb(color)
    return f"rgba({r}, {g}, {b}, {a:g})"


def stable_uuid(name):
    return str(uuid.uuid5(_NS, name))


def zip_bytes(files):
    """{arcname: str | bytes} → deterministic zip bytes (fixed timestamps, given order)."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data.encode() if isinstance(data, str) else data)
    return buf.getvalue()
