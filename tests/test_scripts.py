"""The Claude Code plugin's shell scripts, run for real on crafted status JSON."""

import json
import os
import shutil
import stat
import subprocess
from pathlib import Path

import pytest

pytestmark = pytest.mark.skipif(not (shutil.which("bash") and shutil.which("jq")), reason="needs bash and jq")

STATUS = {
    "model": {"display_name": "Opus"},
    "context_window": {"used_percentage": 42},
    "cost": {"total_cost_usd": 0.84},
}


@pytest.fixture(scope="module")
def scripts(files, tmp_path_factory):
    """The generated scripts, written to a temporary directory (wherever the port puts them)."""
    out = tmp_path_factory.mktemp("scripts")
    found = {}
    for path, body in files.items():
        name = Path(path).name
        is_script = isinstance(body, str) and body.startswith("#!")
        if path.startswith("claude-code/") and name.startswith("subway-seat-") and is_script:
            target = out / name
            target.write_text(body, encoding="utf-8")
            target.chmod(target.stat().st_mode | stat.S_IEXEC)
            found[name] = target
    return found


def run(script: Path, payload: dict, tmp_path: Path, **env: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", str(script)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=False,
        env={
            **os.environ,
            "CLAUDE_CONFIG_DIR": str(tmp_path),  # never read the real ~/.claude
            "SUBWAY_SEAT_FLAVOR": "walnut",
            **env,
        },
    )


def has_locale(name: str) -> bool:
    listed = subprocess.run(["locale", "-a"], capture_output=True, text=True, check=False).stdout.lower()
    return name.lower().replace("utf-8", "utf8") in listed.replace("utf-8", "utf8")


def test_statusline_renders(scripts, tmp_path):
    result = run(scripts["subway-seat-statusline"], STATUS, tmp_path, LC_ALL="C")
    assert result.returncode == 0, result.stderr
    assert not result.stderr
    for text in ("Opus", "42%", "$0.84"):
        assert text in result.stdout


@pytest.mark.skipif(not has_locale("de_DE.UTF-8"), reason="the de_DE.UTF-8 locale isn't installed")
@pytest.mark.xfail(strict=False, reason="printf reads the locale's decimal comma; fix pending in ports/claude_code.py")
def test_statusline_ignores_comma_decimal_locale(scripts, tmp_path):
    result = run(scripts["subway-seat-statusline"], STATUS, tmp_path, LC_ALL="de_DE.UTF-8")
    assert result.returncode == 0, result.stderr
    assert not result.stderr, result.stderr
    assert "$0.84" in result.stdout


def test_subagents_emits_json_lines(scripts, tmp_path):
    payload = {"columns": 80, "tasks": [{"id": "a", "name": "explore", "status": "running"}]}
    result = run(scripts["subway-seat-subagents"], payload, tmp_path)
    assert result.returncode == 0, result.stderr
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    assert lines, "no rows"
    for line in lines:
        row = json.loads(line)
        assert row["id"] == "a"
        assert "content" in row
