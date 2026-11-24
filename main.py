#!/usr/bin/env python3
"""Write the entry for make.fun's "Weirdest Job Title: Blind Judge Showdown".

The program writes one weird job title (1-60 characters) to
/output/entry.txt. The title was picked by drafting a slate of
candidates and duelling them pairwise on the bounty judge's criteria,
in the judge's order: a weird job title first, then stranger than
ordinary work, a funny twist that lands on first read, a title that
still sounds like a real job you can picture someone doing, and short
enough to take in at a glance. The slate and the duels are recorded in
candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (44 characters) — see candidates.md for the full slate.
TITLE = "Professional Mourner for Strangers' Funerals"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(TITLE)


if __name__ == "__main__":
    main()
