"""Shared fixtures: every port built once, in memory (nothing is written to dist/)."""

import pytest

import build
import palette as p

# Port ids, known at collection time so tests can be parametrized per port.
PORT_IDS = list(build.discover())


def luminance(color: str) -> float:
    """WCAG relative luminance of #RRGGBB."""

    def channel(v: int) -> float:
        c = v / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(v) for v in p.hex_to_rgb(color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    """WCAG contrast ratio between two #RRGGBB colors."""
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


@pytest.fixture(scope="session")
def mods():
    return build.discover()


@pytest.fixture(scope="session")
def outs(mods):
    """{id: [Out, …]} straight from each port's build()."""
    return {pid: mod.build(p.FLAVORS) for pid, mod in mods.items()}


@pytest.fixture(scope="session")
def rendered(mods):
    """{id: (files, manifest entry)} after build.py's own validation, plus the warnings it raised."""
    build.WARNINGS.clear()
    result = {pid: build.render_port(mod) for pid, mod in mods.items()}
    warnings = list(build.WARNINGS)
    build.WARNINGS.clear()
    return result, warnings


@pytest.fixture(scope="session")
def files(rendered):
    """Every generated file, keyed by its path under dist/."""
    return {path: body for port_files, _ in rendered[0].values() for path, body in port_files.items()}


@pytest.fixture(scope="session")
def entries(rendered):
    return {pid: entry for pid, (_, entry) in rendered[0].items()}
