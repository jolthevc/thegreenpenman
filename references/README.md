# Reference-image library

The founder explicitly wants **real approved image masters in GitHub** so any new agent can inspect and accurately reproduce the visual language. This directory is structured for that purpose.

## Current honest state
**The original approved PNG images are not yet in this repository.** They exist in the creative conversation and in a separately prepared binary image-import ZIP. GitHub text tools published the operating docs but did not import those PNG bytes. Do not claim otherwise. Any `pending_import` row is not a usable reference path until confirmed.

## Library structure

```text
references/
  README.md
  manifest.csv
  approved/              # actual founder-approved PNG originals only
  candidates/            # trials, rejects, unapproved and comparison sheets
```

Each approved reference should be named like `GPM-REF-001_open-cage.png`, `GPM-REF-002_set-down-baggage.png`; accompanying rows in `manifest.csv` include exact path, visual purpose, dimensions, source, approval and SHA256.

## Candidate starter masters from the founding discussion

- **Open cage**: sage background, refined readable italic green phrase, highly restrained central bird/cage, ample empty space. Two variants exist; the founder especially singled out the simpler green italic one as a visual preference.
- **Woman setting down luggage**: approved as a *good example*, human figure and physical burden.
- **Umbrella seller**: good human/incentive example, a few distinct variants; choose one actual favored original.
- **Lion and hidden creatures**: good animal/power example; low-clutter green version.
- **Sheep and fence**: restrained metaphor for protection and constraint.
- **Boat tied to harbor**: quiet object/environment metaphor.

These are directional approvals gathered over iterations. Before promoting a particular file as **final reference master**, confirm which exact rendered variant the founder prefers if ambiguous. Other generated outputs (contact sheets, pink tests, chubby cartoon animals, colored manuscripts) are rejected style references.

## Process to import
1. Upload original image bytes (not a screenshot or compressed preview) under `references/approved/` using GitHub's Add file > Upload files, Git, or a binary-capable tool.
2. Populate `manifest.csv` with *real repo path*, date/approval, intended lesson, style attributes, dimensions and SHA256.
3. Review in GitHub at full size and check the preview. Do not link to `sandbox:/...` from repo docs.
4. Mark `status=approved` only for approved exact artwork.
5. Update README visual gallery with relative Markdown image links to imported assets; keep one style anchor and a diverse supporting set.
6. Future agents must open and inspect actual approved images, not rely on text descriptions or on screenshots of other artists.

## Copyright and originality
Do **not** place the inspiration creator's screenshots into `approved/`. They are examples of editorial effect, not art to imitate. Do not trace or adapt their distinct compositions, characters, or visual signature.
