#!/usr/bin/env python3
"""Print the tired Dark Lord's monologue.

Reads the entry text from entry.txt, located next to this script,
and prints it to standard output. Standard library only.
"""

from pathlib import Path


def load_entry() -> str:
    """Return the monologue text stored in entry.txt."""
    # Resolve against this script's own directory so the entry is found
    # no matter which working directory the script is run from.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    return entry_path.read_text(encoding="utf-8").strip()


def main() -> int:
    print(load_entry())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
