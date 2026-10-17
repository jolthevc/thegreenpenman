#!/usr/bin/env python3
"""Standard-library-only consistency checks for The Green Pen Man."""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "content" / "IDEA_REGISTRY.csv"
REFS = ROOT / "references" / "manifest.csv"
ALLOWED = {"idea", "copy_draft", "copy_approved", "art_draft", "art_approved", "package_ready", "published", "retired"}
REF_ALLOWED = {"pending_import", "approved", "candidate", "rejected", "retired"}
REQUIRED = {"id", "pillar", "subject_type", "on_image_sentence", "art_concept", "caption", "status"}
REF_FIELDS = {"ref_id", "filename", "subject_type", "status"}
errors = []


def read_csv(path: Path):
    if not path.is_file():
        errors.append(f"Missing {path.relative_to(ROOT)}")
        return [], []
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


fields, rows = read_csv(REGISTRY)
if not REQUIRED.issubset(set(fields)):
    errors.append(f"Registry missing columns: {sorted(REQUIRED - set(fields))}")
ids = Counter()
phrases = Counter()
for lineno, row in enumerate(rows, 2):
    code = (row.get("id") or "").strip()
    sentence = (row.get("on_image_sentence") or "").strip()
    caption = (row.get("caption") or "").strip()
    state = (row.get("status") or "").strip()
    ids[code] += 1
    phrases[sentence.casefold()] += 1
    if not re.fullmatch(r"GPM-\d{4}", code):
        errors.append(f"Registry line {lineno}: invalid id {code!r}")
    if state not in ALLOWED:
        errors.append(f"{code}: invalid status {state!r}")
    if not sentence or not caption or not row.get("art_concept"):
        errors.append(f"{code}: missing line, caption or art concept")
    if "—" in sentence or "—" in caption:
        errors.append(f"{code}: prohibited em dash")
    # Conservative heuristic: count sentence-ending markers only.
    # Not a substitute for human grammatical editorial review.
    count = len(re.findall(r"[.!?](?:[\\\"'”’)]*)?(?=\s|$)", sentence))
    if count != 1:
        errors.append(f"{code}: expected one complete sentence, found {count} punctuation ends")
    if len(sentence) > 190:
        errors.append(f"{code}: unusually long on-image sentence")
for code, n in ids.items():
    if n > 1:
        errors.append(f"Duplicate id: {code}")
for s, n in phrases.items():
    if s and n > 1:
        errors.append(f"Duplicate line: {s[:90]}")

reffields, refs = read_csv(REFS)
if not REF_FIELDS.issubset(set(reffields)):
    errors.append(f"Reference manifest missing columns: {sorted(REF_FIELDS - set(reffields))}")
ref_ids = Counter()
for i, row in enumerate(refs, 2):
    ref_id = (row.get("ref_id") or "").strip()
    filename = (row.get("filename") or "").strip()
    state = (row.get("status") or "").strip()
    ref_ids[ref_id] += 1
    if not re.fullmatch(r"GPM-REF-\d{3}", ref_id):
        errors.append(f"Manifest line {i}: invalid ref_id {ref_id!r}")
    if state not in REF_ALLOWED:
        errors.append(f"{ref_id}: invalid ref state {state!r}")
    if state == "approved":
        path = ROOT / "references" / "approved" / filename
        if not path.is_file():
            errors.append(f"{ref_id}: approved but missing image {path.relative_to(ROOT)}")
        elif row.get("sha256") and hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            errors.append(f"{ref_id}: SHA256 mismatch")
for ref, n in ref_ids.items():
    if n > 1:
        errors.append(f"Duplicate reference id: {ref}")
if errors:
    print("VALIDATION FAILED")
    print("\n".join("- " + x for x in errors))
    sys.exit(1)
print(f"OK: {len(rows)} ideas, {len(refs)} references, statuses and one-sentence checks passed.")
