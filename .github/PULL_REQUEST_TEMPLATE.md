## What this does

<!-- One or two sentences. For a new port: the app and the format. -->

## How I checked it

<!-- Loaded it in the app? Ran a validator? Screenshots of each flavor are very welcome. -->

- [ ] `uv run ./build.py` runs clean (no ⚠ warnings) and `dist/` is committed
- [ ] `uv run --with pytest --with pyyaml pytest -q` passes
- [ ] Written against palette roles, not hex
- [ ] All three flavors look right (Enamel isn't just an inversion)
- [ ] If the app shows diffs: code keeps its syntax colors on the diff tints (see CONTRIBUTING.md)
