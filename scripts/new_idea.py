#!/usr/bin/env python3
"""Create one unique numbered draft in the idea registry. Does not approve/publish."""
import argparse
import csv
import re
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[1] / "content" / "IDEA_REGISTRY.csv"


def main():
    parser = argparse.ArgumentParser(description="Add one GPM idea in copy_draft state.")
    for key in ("pillar", "subject_type", "on_image_sentence", "art_concept", "caption"):
        parser.add_argument("--" + key.replace("_", "-"), required=True)
    args = parser.parse_args()
    values = vars(args)
    with REGISTRY.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    proposed = values["on_image_sentence"].strip()
    if "—" in proposed or not re.search(r"[.!?]$", proposed):
        parser.error("Sentence must end in punctuation and not use em dash")
    if any(r["on_image_sentence"].strip().casefold() == proposed.casefold() for r in rows):
        parser.error("This wording already exists in the registry")
    ids = [int(r["id"].split("-")[-1]) for r in rows if re.fullmatch(r"GPM-\d{4}", r["id"])]
    newid = f"GPM-{max(ids, default=0) + 1:04d}"
    entry = {k: values.get(k, "") for k in fields}
    entry["id"] = newid
    entry["status"] = "copy_draft"
    rows.append(entry)
    with REGISTRY.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Created {newid} in copy_draft state. Editorial approval still required.")


if __name__ == "__main__":
    main()
