# Upload original approved-style image files

These images were generated during brand development. They are not sourced from the inspiration artist.

**Six original rasters are provided in a separate downloadable ZIP through the founding chat.** They cannot be conjured from markdown and are not yet in GitHub. The filename manifest below maps expected image paths and full-file SHA256 checksums.

To import them:
1. Download `the_green_pen_man_reference_pack.zip` from the founding conversation.
2. Extract the six PNGs from `references/approved/` in that archive.
3. Upload these six PNGs to `references/approved/` in GitHub, preserving names.
4. Open and inspect each uploaded image; confirm it is the intended style version.
5. Change each manifest row from `pending_import` to `approved` **only after** the file is actually present and the owner confirms that exact version is acceptable as a *style reference*.
6. Run `python3 scripts/validate_content.py`.
7. Update `CONTINUITY_HANDOFF.md` to tell future agents that the assets are now browsable.

Do not conflate style-reference approval with exact on-image-copy approval.
