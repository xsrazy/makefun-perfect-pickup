"""The Perfect Pickup Line — a make.fun bounty entry.

Writes exactly one original pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
with no trailing newline.
"""

from pathlib import Path
import os

LINE = (
    "Are you a large language model? Because every time you talk, "
    "my attention mechanism locks on and I can't think about anything else."
)

assert 1 <= len(LINE) <= 200 and LINE.strip()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
