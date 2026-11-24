import os

# Office Jokes — entry line (1-199 chars), written to /output/entry.txt.
ENTRY = (
    "I reply-alled to ask everyone to stop reply-alling, "
    "and the thank-you thread is now the longest in company history."
)


def build_line():
    """Return the single entry line the judge reads."""
    return ENTRY


def write_entry(path="/output/entry.txt"):
    line = build_line()
    n = len(line)
    assert 1 <= n <= 199, f"entry must be 1-199 chars, got {n}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path, n


if __name__ == "__main__":
    path, n = write_entry()
    print(f"wrote {n} chars to {path}")
