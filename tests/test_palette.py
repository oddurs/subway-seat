"""palette.py: the roles, the flavors, contrast, and the color math every port relies on."""

import itertools
import re

import pytest
from conftest import contrast, luminance

import palette as p
from ports import claude_code
from ports._lib import tints

HEX = re.compile(r"^#[0-9A-F]{6}$")


def test_every_flavor_defines_exactly_the_roles():
    for f in p.FLAVORS:
        assert set(f.colors) == set(p.ROLES), f.id


def test_role_tables_consistent():
    assert len(p.ROLES) == len(set(p.ROLES)), "a role is listed twice"
    assert set(p.ROLE_NAMES) == set(p.ROLES), "ROLE_NAMES should name every role"
    assert set(p.ROLE_USES) == set(p.ROLES), "ROLE_USES should describe every role"
    assert len(set(p.ROLE_NAMES.values())) == len(p.ROLE_NAMES), "two roles share a name"
    assert set(p.ACCENT_ROLES) <= set(p.ACCENTS), "ACCENT_ROLES should only list accents"
    assert all(p.ROLE_USES[r] for r in p.ROLES)


def test_hex_values_are_uppercase_rrggbb():
    for f in p.FLAVORS:
        bad = {role: value for role, value in f.colors.items() if not HEX.match(value)}
        assert not bad, f"{f.id}: {bad}"


def test_flavor_identity():
    ids = [f.id for f in p.FLAVORS]
    slugs = [f.slug for f in p.FLAVORS]
    assert len(set(ids)) == len(ids)
    assert len(set(slugs)) == len(slugs)
    for f in p.FLAVORS:
        assert f.slug in ("subway-seat", f"subway-seat-{f.id}"), f.slug
        assert f.snake == f.slug.replace("-", "_")
        # Names are interpolated unescaped into XML, TOML and INI templates.
        assert re.fullmatch(r"[A-Za-z ]+", f.name), f.name
        assert f.blurb.strip()
    assert sum(not f.dark for f in p.FLAVORS) == 1, "exactly one light flavor"
    assert p.DEFAULT in p.FLAVORS


def test_ansi_is_16_known_roles():
    for f in p.FLAVORS:
        assert len(f.ansi_roles) == 16, f.id
        assert set(f.ansi_roles) <= set(p.ROLES), f.id
        assert all(HEX.match(c) for c in f.ansi)


def test_syntax_table_valid():
    for role, (color_role, styles) in p.SYNTAX.items():
        assert color_role in p.ROLES, role
        assert styles <= {"bold", "italic"}, role


def test_ground_ramp_order():
    ramp = p.GROUND + p.TEXT
    for f in p.FLAVORS:
        if f.dark:
            # crust → text_hi gets lighter at every step.
            lums = [luminance(f.colors[r]) for r in ramp]
            assert lums == sorted(lums) and len(set(lums)) == len(lums), f.id
        else:
            # Enamel runs the other way from base, with crust and mantle darker than base.
            order = ramp[ramp.index("base") :]
            lums = [luminance(f.colors[r]) for r in order]
            assert lums == sorted(lums, reverse=True) and len(set(lums)) == len(lums), f.id
            assert luminance(f.crust) < luminance(f.mantle) < luminance(f.base), f.id


def test_contrast_floor():
    """Text on base. Minimums when this was written: text 10.75, subtext 6.38, syntax 3.65."""
    for f in p.FLAVORS:
        for role in ("text", "text_hi"):
            assert contrast(f.colors[role], f.base) >= 7, (f.id, role)
        for role in ("subtext0", "subtext1"):
            assert contrast(f.colors[role], f.base) >= 6, (f.id, role)
        for role, (color_role, _) in p.SYNTAX.items():
            assert contrast(f.colors[color_role], f.base) >= 3.4, (f.id, role)


# ── Diff tints: syntax colors stay readable on added and removed lines ─────
# Minimums when this was written (all on `comment`): line tints 2.879 (Walnut add),
# word emphasis 2.174 (Walnut add_emph). The floors sit just under those, so a
# retune that makes code on a diff harder to read fails here.
@pytest.mark.parametrize("flavor", p.FLAVORS, ids=lambda f: f.id)
@pytest.mark.parametrize(("ground", "floor"), [("add", 2.8), ("del", 2.8), ("add_emph", 2.0), ("del_emph", 2.0)])
def test_syntax_readable_on_diff_tints(flavor, ground, floor):
    tint = tints(flavor)[ground]
    low = {role: round(contrast(flavor.colors[c], tint), 2) for role, (c, _) in p.SYNTAX.items()}
    low = {role: ratio for role, ratio in low.items() if ratio < floor}
    assert not low, f"{flavor.id} on {ground} {tint}: {low}"


@pytest.mark.parametrize("flavor", p.FLAVORS, ids=lambda f: f.id)
def test_word_emphasis_is_stronger_than_the_line(flavor):
    t = tints(flavor)

    def distance(a: str) -> float:
        return sum((x - y) ** 2 for x, y in zip(p.hex_to_rgb(a), p.hex_to_rgb(flavor.base), strict=True)) ** 0.5

    for kind in ("add", "del", "chg"):
        assert distance(t[f"{kind}_emph"]) >= 1.5 * distance(t[kind]), (flavor.id, kind)
    for kind in ("add", "del"):
        assert distance(t[f"{kind}_dim"]) < distance(t[kind]), (flavor.id, kind)


@pytest.mark.parametrize("flavor", p.FLAVORS, ids=lambda f: f.id)
def test_diff_grounds_are_distinct(flavor):
    """Added, removed and changed lines must not read as the same color."""
    t = tints(flavor)
    for a, b in itertools.combinations(("add", "del", "chg"), 2):
        gap = sum((x - y) ** 2 for x, y in zip(p.hex_to_rgb(t[a]), p.hex_to_rgb(t[b]), strict=True)) ** 0.5
        assert gap >= 10, (flavor.id, a, b, round(gap, 1))


# ── Claude Code's terminal-colors themes ───────────────────────────────────
def test_xterm_colors():
    assert [claude_code.xterm(n) for n in (16, 52, 187, 231, 232, 236, 255)] == [
        "#000000", "#5F0000", "#D7D7AF", "#FFFFFF", "#080808", "#303030", "#EEEEEE"]


@pytest.mark.parametrize("flavor", p.FLAVORS, ids=lambda f: f.id)
def test_terminal_theme_diff_grounds(flavor):
    """On an ANSI base Claude Code draws code in the terminal's ANSI slots over
    xterm-256 grounds; the same floors as the tints hold there."""
    t = claude_code.theme(flavor, terminal=True)
    assert t["base"] == ("dark-ansi" if flavor.dark else "light-ansi")
    assert t["overrides"].keys() == claude_code.theme(flavor)["overrides"].keys()
    n = {k: int(re.fullmatch(r"ansi256\((\d+)\)", v)[1]) for k, v in t["overrides"].items() if k.startswith("diff")}
    assert len(n) == 6 and all(16 <= i <= 255 for i in n.values()), n
    a = flavor.ansi
    code = [a[7] if flavor.dark else a[0], a[8], a[10], a[11], a[12], a[13], a[14]]

    def reach(token):
        return sum((x - y) ** 2 for x, y in zip(p.hex_to_rgb(claude_code.xterm(n[token])), p.hex_to_rgb(flavor.base),
                                                strict=True)) ** 0.5

    for token, sign in (("diffAdded", a[10]), ("diffRemoved", a[9])):
        for suffix, floor in (("", 2.8), ("Dimmed", 2.8), ("Word", 2.0)):
            ground = claude_code.xterm(n[token + suffix])
            low = {c: round(contrast(c, ground), 2) for c in [*code, sign] if contrast(c, ground) < floor}
            assert not low, (flavor.id, token + suffix, ground, low)
        assert reach(f"{token}Word") > reach(token) >= reach(f"{token}Dimmed"), (flavor.id, token)
    assert n["diffAdded"] != n["diffRemoved"], flavor.id


# ── Color math ─────────────────────────────────────────────────────────────
def test_blend_endpoints_and_midpoint():
    a, b = "#ADB956", "#362619"
    assert p.blend(a, b, 0) == b
    assert p.blend(a, b, 1) == a
    assert p.blend("#000000", "#FFFFFF", 0.5) == "#808080"


def test_blend_output_is_always_rrggbb():
    for t in (i / 20 for i in range(21)):
        assert HEX.match(p.blend("#F97160", "#20160E", t)), t


def test_blend_rejects_out_of_range_alpha():
    with pytest.raises(ValueError):
        p.blend("#FFFFFF", "#000000", 1.2)
    with pytest.raises(ValueError):
        p.blend("#FFFFFF", "#000000", -0.1)


def test_alpha_suffix():
    assert p.alpha("#112233", 1) == "#112233FF"
    assert p.alpha("#112233", 0) == "#11223300"
    assert p.alpha("#112233", 0.5) == "#11223380"


def test_alpha_rejects_colors_that_already_have_alpha():
    with pytest.raises((ValueError, AssertionError)):
        p.alpha("#11223344", 0.5)


def test_mix_accepts_roles_and_hex():
    f = p.DEFAULT
    assert f.mix("green", "base", 0.3) == p.blend(f.green, f.base, 0.3)
    assert f.mix("green", "#FFFFFF", 0.3) == p.blend(f.green, "#FFFFFF", 0.3)
    assert f.mix("#000000", "base", 0.5) == p.blend("#000000", f.base, 0.5)
