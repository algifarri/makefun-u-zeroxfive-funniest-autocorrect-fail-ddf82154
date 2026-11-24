#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Funniest Autocorrect Fail entry.

Writes one line (117 characters, under the 200-character cap) that reads
as a hilarious autocorrect fail to /output/entry.txt.
"""

import os

ENTRY = (
    "Hi Mrs. Johnson, just confirming Timmy's dominatrix appointment "
    "is tomorrow at 3 \u2014 DENTIST! I meant dentist, I swear!"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
