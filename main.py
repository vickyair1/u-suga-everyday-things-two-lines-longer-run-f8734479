#!/usr/bin/env python3
"""Everyday Things, Two Lines: a traffic jam, explained to a 10-year-old.

Writes exactly two lines to /output/entry.txt, no trailing newline.
Line 1 explains a traffic jam through one analogy; line 2 says why the
analogy works: what it maps and what it leaves out.
"""

import os

# Final wording: "getting impatient" is plainer kid language than
# "growing impatient"; everything else holds from the rework.

LINE_1 = "A traffic jam is a parking lot that forgot it was a road, where every car is parked bumper to bumper and going nowhere."
LINE_2 = "It maps the cars standing still and squeezed tight, but it leaves out the honking, the drivers getting impatient, and that nobody actually chose to park there."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-400 chars, UTF-8, not only
    # whitespace, exactly two lines. Fail loudly here rather than ship
    # an invalid entry.
    text = LINE_1 + "\n" + LINE_2
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert text.count("\n") == 1, "entry must be exactly two lines"
    for line in (LINE_1, LINE_2):
        assert line.strip() == line and "\n" not in line, "each line must be one clean line"
        assert line.endswith(".") and line.count(".") == 1, "each line must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
