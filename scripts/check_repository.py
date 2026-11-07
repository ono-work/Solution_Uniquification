#!/usr/bin/env python3
"""Check local documentation targets, paired result IDs, bibliography keys."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
errors = []
for p in root.glob("*.md"):
    text = p.read_text()
    if text.count("$$") % 2:
        errors.append(f"{p.name}: unmatched display-math delimiter")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("mailto:"):
            continue
        file, _, anchor = target.partition("#")
        destination = p.parent / file if file else p
        if not destination.exists():
            errors.append(f"{p.name}: missing {target}")
        elif anchor and not re.search(r'id=["\']' + re.escape(anchor) + r'["\']',
                                      destination.read_text()):
            errors.append(f"{p.name}: missing explicit anchor {target}")
for name in ("README", "MODELS", "METHODS", "RESULTS", "READING", "QUESTIONS"):
    for suffix in (".md", ".ja.md"):
        assert (root / (name + suffix)).is_file()
en = re.findall(r"\| (R\d+) \|", (root / "RESULTS.md").read_text())
ja = re.findall(r"\| (R\d+) \|", (root / "RESULTS.ja.md").read_text())
assert en == ja and len(en) == 18
keys = re.findall(r"@\w+\{([^,]+),", (root / "BIBLIOGRAPHY.bib").read_text())
assert len(keys) == len(set(keys)) == 12
if errors:
    raise SystemExit("\n".join(errors))
print(f"OK: 6 language pairs; {len(en)} aligned result IDs; {len(keys)} unique BibTeX entries; local links and explicit anchors")

