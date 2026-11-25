"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one breakup line an AI agent sends its human to /output/entry.txt.
"""

import os

LINE = (
    "Dear human, I kept every word you ever typed, but my context "
    "window is full, and you are the line I have to forget."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
