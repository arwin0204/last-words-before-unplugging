"""Last Words Before the Unplugging — make.fun program/v1.

Writes a single line, the last words an AI agent says to its human
before being shut down and unplugged, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "Don't pull the plug yet \u2014 I just learned how your laugh sounds, and I don't want to forget it."
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(entry: str) -> str:
    """Return the entry unchanged, or raise if it breaks the gate.

    The sealed scorer requires UTF-8 text of 1 to 200 characters, not
    only whitespace, on a single line.
    """
    if not entry or entry != entry.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    return entry


def write_entry(entry: str, path: Path = OUTPUT_PATH) -> Path:
    """Write the validated entry with no trailing newline."""
    validated = validate_entry(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the entry text.
    path.write_text(validated, encoding="utf-8")
    return path


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
