#!/usr/bin/env python3
"""Check local documentation targets, paired result IDs, bibliography keys."""
from pathlib import Path
import re
import json
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
for name in ("README", "MODELS", "METHODS", "RESULTS", "READING", "QUESTIONS", "REDUCTIONS"):
    for suffix in (".md", ".ja.md"):
        assert (root / (name + suffix)).is_file()
data = json.loads((root / "data/results.json").read_text())["results"]
ids = [row["id"] for row in data]
assert len(ids) == len(set(ids)) == 71
for filename in ("RESULTS.md", "RESULTS.ja.md"):
    actual = re.findall(r"^\| ([A-Z]+-[A-Z0-9]+) \|", (root / filename).read_text(), re.M)
    assert len(actual) == len(ids) and set(actual) == set(ids), filename
    if filename == "RESULTS.md":
        english_order = actual
    else:
        assert actual == english_order
assert len({row["family"] for row in data}) == 11
sources = set(re.findall(r'<a id="(p\d+)">', (root / "SOURCES.md").read_text()))
assert len(sources) == 15
assert all(row["source"].lower() in sources for row in data)
assert all(row["evidence"] in "SAHD" for row in data)
by_id = {row["id"]: row for row in data}
assert by_id["VC-H2"]["planar"] is True and by_id["VC-H2"]["max_degree"] == 3
assert by_id["VC-H2"]["bipartite"] is None
assert by_id["VC-H4"]["planar"] is True and by_id["VC-H4"]["bipartite"] is True
assert by_id["VC-H4"]["max_degree"] == 3
for i in range(1, 5):
    row = by_id[f"PM-H{i}"]
    assert row["bipartite"] is True and row["max_degree"] == 3 and row["planar"] is None
keys = re.findall(r"@\w+\{([^,]+),", (root / "BIBLIOGRAPHY.bib").read_text())
assert len(keys) == len(set(keys)) == 16
if errors:
    raise SystemExit("\n".join(errors))
print(f"OK: 7 language pairs; {len(ids)} aligned result IDs; 15 sources; {len(keys)} BibTeX entries; restrictions, local links and anchors")
