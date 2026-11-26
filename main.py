"""One Star, Five Stars for the Food.

Writes a single-sentence, one-star review of planet Earth by an alien
tourist -- with a genuine compliment about the food -- to /output/entry.txt.
Standard library only, deterministic, no network, no clock, no randomness.
"""

import os
import sys

SENTENCE = (
    "One star: the gravity bruised all four of my knees, the weather changed "
    "its mind hourly, and the locals kept asking where I parked my ship, but "
    "the tacos were worth every light-year of the trip."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path=DEFAULT_OUTPUT):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    write_entry(target)
    print("Wrote %d characters to %s" % (len(SENTENCE), target))
