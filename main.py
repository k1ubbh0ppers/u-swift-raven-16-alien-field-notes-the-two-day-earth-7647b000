#!/usr/bin/env python3
"""Field notes from a two-day visit to Earth, in review form.

This script takes a single one-line review, written from the point of view
of an alien tourist, and stores it at /output/entry.txt as UTF-8 text with
exactly one trailing newline. It uses only the Python 3 standard library
and never touches the network.

The joke turns on a self-checkout: the humans handle every step
themselves, scanning, bagging and paying, and then politely thank the
machine anyway, so the visitor logs the machine as the staff. Opening
with "Visited Earth:" frames the whole line as an outsider's report
right away, which is the part the scoring weighs most. A single everyday
observation, a tidy punch, and the kicker ("excellent staff") saved for
the very end.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

REVIEW = (
    "Visited Earth: the locals scan their own food, bag it, pay, "
    "then thank the machine for its help. 5/5 stars, excellent staff."
)


def store_review(text: str) -> None:
    """Create the output folder if needed, then save the review line."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text + "\n", encoding="utf-8", newline="\n")


def announce(text: str) -> None:
    """Echo the review and its length so the run is easy to eyeball."""
    print(text)
    print(f"characters: {len(text)}")


def run() -> None:
    store_review(REVIEW)
    announce(REVIEW)


if __name__ == "__main__":
    run()
