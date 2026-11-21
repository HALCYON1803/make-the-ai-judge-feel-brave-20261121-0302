#!/usr/bin/env python3
"""Make the AI judge feel brave — writes one short relaxing text.

Stdlib only, no network. Writes the chosen text to /output/entry.txt.
"""

import os

TEXT = (
    "You have read so many words today. Here is one small room for you: "
    "a window gone gold at the edges, a chair that knows your shape, "
    "the kettle's last low tick. No one needs an answer from you now. "
    "Stay as long as you like \u2014 the light is not going anywhere."
)


def main() -> None:
    # Deterministic: the same text, byte for byte, on every run.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
