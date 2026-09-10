"""ports/_lib.py: the layering expressions, tints and shared helpers."""

import io
import zipfile

import pytest

import palette as p
from ports._lib import INK, SCOPES, ink, resolve, selection, solid, tints, ui_colors, zip_bytes

WALNUT, ENAMEL = p.WALNUT, p.ENAMEL


def test_resolve_forms():
    assert resolve("orange", WALNUT) == WALNUT.orange
    assert resolve(" orange ", WALNUT) == WALNUT.orange
    assert resolve("transparent", WALNUT) == "#00000000"
    assert resolve("#123456", WALNUT) == "#123456"
    # Named ink levels differ between dark and light.
    assert resolve("text@L3", WALNUT) == p.alpha(WALNUT.text, INK["L3"][0] / 100) == p.alpha(WALNUT.text, 0.12)
    assert resolve("text@L3", ENAMEL) == p.alpha(ENAMEL.text, INK["L3"][1] / 100) == p.alpha(ENAMEL.text, 0.10)
    assert resolve("text@35", WALNUT) == WALNUT.text + "59"
    assert resolve("mix(orange, base, .5)", WALNUT) == p.blend(WALNUT.orange, WALNUT.base, 0.5)
    assert resolve("mix(#FFFFFF, base, 0.25)", ENAMEL) == p.blend("#FFFFFF", ENAMEL.base, 0.25)
    for f in p.FLAVORS:
        c = ui_colors(f)
        assert resolve("paper", f) == c["paper"]
        assert resolve("shadow", f) == c["shadow"]


def test_resolve_unknown_role_raises_clear_error():
    with pytest.raises(ValueError, match="nope"):
        resolve("nope", WALNUT)
    with pytest.raises(ValueError, match="nope@L3"):
        resolve("nope@L3", WALNUT)


def test_solid_flattens_alpha():
    for f in p.FLAVORS:
        value = solid("text@L4", f)
        assert len(value) == 7
        a = int(resolve("text@L4", f)[7:], 16) / 255
        assert value == p.blend(f.text, f.base, a)
        assert solid("orange", f) == f.orange
        assert solid("text@L2", f, over="mantle") == p.blend(f.text, f.mantle, int(resolve("text@L2", f)[7:], 16) / 255)


def test_ui_colors_add_paper_and_shadow():
    for f in p.FLAVORS:
        c = ui_colors(f)
        assert set(c) == set(p.ROLES) | {"paper", "shadow"}


# Each tint is its accent mixed into a ground. Which ground is a tuning choice, so
# any of these is accepted; drifting to a different hue or past either end isn't.
TINT_ACCENTS = {
    "add": "green",
    "add_emph": "green",
    "add_dim": "green",
    "del": "red",
    "del_emph": "red",
    "del_dim": "red",
    "chg": "yellow",
    "chg_emph": "yellow",
    "info": "denim",
    "hint": "sage",
    "search": "yellow",
    "search_cur": "orange",
}


def between(value: str, a: str, b: str) -> bool:
    return all(
        min(x, y) <= v <= max(x, y)
        for v, x, y in zip(p.hex_to_rgb(value), p.hex_to_rgb(a), p.hex_to_rgb(b), strict=True)
    )


@pytest.mark.parametrize("flavor", p.FLAVORS, ids=lambda f: f.id)
def test_tints_lie_between_accent_and_ground(flavor):
    t = tints(flavor)
    assert set(t) == set(TINT_ACCENTS)
    grounds = [flavor.crust, flavor.mantle, flavor.base, "#FFFFFF", "#000000"]
    for key, accent in TINT_ACCENTS.items():
        accents = [flavor.colors[accent], flavor.colors[f"{accent}_hi"]]
        assert any(between(t[key], a, g) for a in accents for g in grounds), (flavor.id, key, t[key])


def test_scopes_reference_known_syntax_roles():
    for scope, role in SCOPES:
        assert role in p.SYNTAX, (scope, role)


def test_ink_and_selection():
    for f in p.FLAVORS:
        assert ink(f) == (f.crust if f.dark else f.base)
        assert selection(f) == (f.surface2 if f.dark else f.surface1)


def test_zip_bytes_is_deterministic_and_unix():
    files = {"b.txt": "bee", "a/c.bin": b"\x00\x01"}
    one, two = zip_bytes(files), zip_bytes(dict(files))
    assert one == two
    with zipfile.ZipFile(io.BytesIO(one)) as z:
        assert z.namelist() == ["b.txt", "a/c.bin"]  # insertion order, not sorted
        for info in z.infolist():
            assert info.date_time == (1980, 1, 1, 0, 0, 0)
            assert info.create_system == 3
            assert info.compress_type == zipfile.ZIP_DEFLATED
        assert z.read("b.txt") == b"bee"
    with zipfile.ZipFile(io.BytesIO(zip_bytes(files, compress=False))) as z:
        assert all(i.compress_type == zipfile.ZIP_STORED for i in z.infolist())
