"""The Excuse That Almost Works — make.fun entry.

Reads the one-line excuse from entry.txt and prints it.
The bounty asks for a single line of plain text, at most 20 words,
that a gamer would text the boss to skip work during GTA 6 launch week.
"""

import os

MAX_WORDS = 20


def load_excuse(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read().strip()
    if not text:
        raise ValueError("excuse must not be empty")
    if "\n" in text:
        raise ValueError("excuse must be a single line")
    if len(text.split()) > MAX_WORDS:
        raise ValueError("excuse must be at most 20 words")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print(load_excuse(os.path.join(here, "entry.txt")))


if __name__ == "__main__":
    main()
