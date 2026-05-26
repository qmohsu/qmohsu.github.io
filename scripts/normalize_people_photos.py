#!/usr/bin/env python3
"""Normalize people photos so headshots display upright in every browser.

Phone cameras store the image sideways plus an EXIF "Orientation" tag telling
viewers how to rotate it. When that tag is later stripped (by an editor, a
messaging app, a copy step), the image is left physically sideways with nothing
to correct it. This bakes the EXIF rotation into the pixels and drops the tag,
so the result is upright regardless of how a viewer handles EXIF.

Usage:
  python scripts/normalize_people_photos.py static/images/people/<slug>.jpg [more...]
  python scripts/normalize_people_photos.py --all          # scan static/images/people
  python scripts/normalize_people_photos.py --all --check  # audit only, no writes

Only images whose EXIF orientation is non-normal are re-saved (so already-correct
photos are never recompressed). NOTE: a photo that is *physically* sideways with
NO orientation tag cannot be detected here — always eyeball the result. The
companion /update-person workflow includes that visual check.
"""
import os
import sys
from PIL import Image, ImageOps

ORIENTATION_TAG = 274  # EXIF Orientation
PEOPLE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "static", "images", "people",
)
EXTS = ("jpg", "jpeg", "png", "webp")


def collect(args):
    if "--all" in args:
        return [
            os.path.join(PEOPLE_DIR, f)
            for f in sorted(os.listdir(PEOPLE_DIR))
            if f.lower().rsplit(".", 1)[-1] in EXTS
        ]
    return [a for a in args if not a.startswith("--")]


def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    paths = collect(args)
    if not paths:
        print(__doc__)
        return 1

    changed = upright = 0
    for path in paths:
        try:
            im = Image.open(path)
            orientation = im.getexif().get(ORIENTATION_TAG)
            if orientation and orientation != 1:
                print(f"[{'WOULD-FIX' if check_only else 'FIXED'}] "
                      f"{os.path.basename(path)} (orientation={orientation})")
                if not check_only:
                    fixed = ImageOps.exif_transpose(im)  # bakes rotation, drops the tag
                    save_kw = {}
                    if im.format == "JPEG":
                        save_kw = dict(quality=92, subsampling="keep")
                    fixed.save(path, format=im.format, **save_kw)
                changed += 1
            else:
                upright += 1
        except Exception as exc:  # noqa: BLE001 — report and continue
            print(f"[ERROR] {path}: {exc}")

    verb = "flagged" if check_only else "normalized"
    print(f"\nDone: {changed} {verb}, {upright} already upright "
          f"(of {len(paths)} scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
