"""The 3 AM Excuse — make.fun entry.

Writes a single excuse line to /output/entry.txt.
The line is the whole entry: the wallet speaks, no narrator explains it.
Standard library only, no network, deterministic.
"""

import os

LINE = "3 AM? I only sign when the sun is up and the gas is down. Come back when your life choices do."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
