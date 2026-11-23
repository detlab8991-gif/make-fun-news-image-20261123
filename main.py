"""Copy the entry image to the path the grader reads.

The repository holds the image as entry.jpg next to this program. This
program copies it byte for byte to /output/entry.png, creating the output
directory when it is missing. It reads nothing else, reaches no network,
and writes the same bytes on every run.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.jpg"
DESTINATION = Path("/output/entry.png")


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing: {SOURCE}")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    written = DESTINATION.stat().st_size
    if written != SOURCE.stat().st_size:
        raise SystemExit(f"copy incomplete: wrote {written} bytes")
    print(f"wrote {DESTINATION} ({written} bytes)")


if __name__ == "__main__":
    main()
