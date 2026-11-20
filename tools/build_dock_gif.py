"""Build the README animation from the current edition capture manifest.

After refreshing the Dock captures, run python3 tools/build_dock_gif.py
with Pillow 10.1 or newer. Use --repo ../macos-tahoe-liquid-kde for Tahoe. The script updates the English README image link.
"""

import argparse
import hashlib
import io
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
STYLES = ("red", "orange", "yellow", "green", "blue", "purple", "pink")
WIDTH = 1040
FRAME_MS = 50
SEQUENCE = (("regular", "light"), ("regular", "dark"), *((style, "light") for style in STYLES))


def dock_frames(captures):
    images = []
    for key in SEQUENCE:
        path, digest = captures[key]
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f"Capture checksum mismatch for {path}")
        with Image.open(io.BytesIO(data)) as source:
            height = round(source.height * WIDTH / source.width)
            images.append(source.convert("RGB").resize((WIDTH, height), Image.Resampling.LANCZOS))
    if len({image.size for image in images}) != 1:
        raise ValueError("Dock capture dimensions differ")

    frames = []
    durations = []
    for index, (style, mode) in enumerate(SEQUENCE):
        current = images[index]
        following = images[(index + 1) % len(images)]
        # Hold the two original icon sets, then move steadily through the tints.
        hold_ms = 0
        transition_ms = 2700
        if style == "regular":
            hold_ms = 700
            transition_ms = 300
        elif style == STYLES[-1]:
            transition_ms = 600
        steps = transition_ms // FRAME_MS
        for step in range(steps):
            frames.append(Image.blend(current, following, step / steps))
            durations.append(FRAME_MS + (hold_ms if step == 0 else 0))

    # Sample fine icon details at full output scale, without averaging their colors.
    sample_size = (WIDTH // 3, images[0].height // 3)
    samples = Image.new("RGB", (sample_size[0], sample_size[1] * len(frames)))
    for index, frame in enumerate(frames):
        samples.paste(frame.resize(sample_size, Image.Resampling.NEAREST), (0, index * sample_size[1]))
    palette = samples.quantize(colors=256)
    encoded = []
    for frame, duration in zip(frames, durations):
        if duration > FRAME_MS:
            # Give each held multicolor view its own full palette.
            encoded.append(frame.quantize(colors=256))
        else:
            encoded.append(frame.quantize(palette=palette, dither=Image.Dither.NONE))
    return encoded, durations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT, help="Edition checkout to update")
    root = parser.parse_args().repo.resolve()
    screenshots = root / "src/screenshots"
    manifest = json.loads((screenshots / "readme-capture.json").read_text())
    edition = manifest["edition"]
    if edition not in ("golden-gate", "tahoe"):
        raise ValueError(f"Unknown edition: {edition}")
    captures = {}
    for name, record in manifest["images"].items():
        style = record.get("style")
        key = style, record.get("mode")
        if record.get("edition") != edition or key not in SEQUENCE:
            continue
        if record.get("case") == f"dock-{style}":
            if record.get("macOSDockIcons") is not False:
                raise ValueError(f"Expected standard theme icons for {key}")
            if key in captures:
                raise ValueError(f"Ambiguous Dock capture for {key}")
            captures[key] = screenshots / name, record["sha256"]

    frames, durations = dock_frames(captures)
    buffer = io.BytesIO()
    frames[0].save(buffer, format="GIF", save_all=True, append_images=frames[1:],
                   duration=durations, loop=0, optimize=False, disposal=1)
    data = buffer.getvalue()
    digest = hashlib.sha256(data).hexdigest()[:12]
    target = screenshots / "previews" / f"{edition}-dock-{digest}.gif"
    readme = root / "README.md"
    original = readme.read_text()
    pattern = rf'(?<=src=")src/screenshots/previews/{edition}-dock-[0-9a-f]{{12}}\.gif(?=")'
    updated, count = re.subn(pattern, target.relative_to(root).as_posix(), original)
    if count != 1:
        raise ValueError("Expected one Dock animation in README.md")
    target.write_bytes(data)
    if updated != original:
        readme.write_text(updated)
    print(target.relative_to(root))


if __name__ == "__main__":
    main()
