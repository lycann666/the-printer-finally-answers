"""The Printer Finally Answers — make.fun entry.

Writes the office printer's one-line comeback to /output/entry.txt.
Deterministic: a single constant string, same output on every run.
No network, no files read, no secrets.
"""

import os
import sys

LINE = "Error 0x00BEEF: user attempted percussive maintenance, so I am now printing your apology."

MAX_LEN = 240


def validate_line(line: str) -> None:
    """Gate the comeback line before it is written.

    The line must be a single non-empty line of 1-240 characters and not
    just whitespace. On failure, report to stderr and exit non-zero so a
    bad line can never be silently written as the entry.
    """
    if not line:
        print("error: LINE is empty", file=sys.stderr)
        sys.exit(1)
    if line.strip() == "":
        print("error: LINE is only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: LINE must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_LEN:
        print(
            f"error: LINE is {len(line)} chars, over the {MAX_LEN}-char limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
