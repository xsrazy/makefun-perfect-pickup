"""The Perfect Pickup Line — a make.fun bounty entry.

Writes exactly one original pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
with no trailing newline.
"""

from pathlib import Path
import os

LINE = (
    "I'm built to predict the next word, but around you my best "
    "prediction is just one: I'd really like to know your name."
)

assert 1 <= len(LINE) <= 200 and LINE.strip()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
