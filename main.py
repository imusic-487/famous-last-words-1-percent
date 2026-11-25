"""Famous Last Words at 1 Percent.

Writes one line -- the funniest last words a phone could say as its
battery hits 1 percent -- to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "At 1%, one last confession: I never lost your photos — "
    "I hid them. Your camera roll is a crime scene."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
