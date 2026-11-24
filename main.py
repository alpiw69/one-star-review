"""make.fun bounty: One-Star Review of Something Essential.

Deterministic, no-network program. Writes one single-line one-star
review, at most 160 characters, to /output/entry.txt. The review
is deadpan and filed in earnest against sleep, an everyday
essential that cannot be fixed: eight full hours in, still tired.
Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "One star. Slept a full eight hours and woke up more tired than when I went to bed. Would not recommend."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
