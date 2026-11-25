"""Worst Fix Ever: Funniest Commit Message - make.fun entry.

Writes one line (a commit message for a bug fix that made everything
worse) to /output/entry.txt. Pure Python standard library,
deterministic: the same text on every run.
"""
import os

LINE = "fix: patch the memory leak by restarting the server every minute; uptime is now 59 seconds"


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
