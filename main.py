"""Make the AI judge feel curious — make.fun entry.

Writes one short text to /output/entry.txt: a quiet library scene that
leaves the reader with an open question — a book with your name inside
it, in handwriting that is not yours, its ink still wet, its next line
blank and waiting.

Pure stdlib, no network, fully deterministic: the output bytes are
always identical.
"""

import os

TEXT = (
    "On the third shelf, behind the books nobody borrows, there is one "
    "with your name inside it. Not your handwriting. The last page is "
    "folded down. The ink is still wet, and the next line is blank, "
    "waiting for whatever you write there."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(TEXT)
    size = os.path.getsize(target)
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % chars)
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    print("wrote %s (%d chars, %d bytes)" % (target, chars, size))


if __name__ == "__main__":
    main()
