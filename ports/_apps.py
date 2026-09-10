"""Shared bits for the desktop-app and browser ports (category "Apps")."""

import uuid

import palette as p

AUTHOR = "Oddur Sigurdsson"
AUTHOR_URL = "https://github.com/oddurs"
DESCRIPTION = "A walnut-brown 1970s NYC subway theme: harvest gold, burnt orange and avocado on warm wood."
_NS = uuid.UUID("5b0b3a52-7d1e-4c55-9a7e-5ea7ee5ea700")  # fixed, so ids are stable across builds


def rgb_list(color):
    return list(p.hex_to_rgb(color))


def rgba(color, a):
    r, g, b = p.hex_to_rgb(color)
    return f"rgba({r}, {g}, {b}, {a:g})"


def stable_uuid(name):
    return str(uuid.uuid5(_NS, name))
