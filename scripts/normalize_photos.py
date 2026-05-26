#!/usr/bin/env python3
"""Normalize site photos so they display upright in every browser.

Phone cameras store the image sideways plus an EXIF "Orientation" tag telling
viewers how to rotate it. When that tag is later stripped (by an editor, a
messaging app, a copy step), the image is left physically sideways with nothing
to correct it. This bakes the EXIF rotation into the pixels and drops the tag,
so the result is upright regardless of how a viewer handles EXIF.

Usage:
  python scripts/normalize_photos.py static/images/news/<file>.jpg [more...]
  python scripts/normalize_photos.py --all          # scan people + news image folders
  python scripts/normalize_photos.py --all --check  # audit only, no writes

Only images whose EXIF orientation is non-normal are re-saved (already-correct
photos are never recompressed). NOTE: a photo that is *physically* rotated with
NO orientation tag (e.g. the EXIF was stripped upstream) cannot be detected here
— always eyeball the result. The /update-person, /add-award and /add-grant
workflows include that visual check when importing images.
"""
import os
import sys
from PIL import Image, ImageOps

ORIENTATION_TAG = 274  # EXIF Orientation
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIRS = [
    os.path.join(ROOT, "static", "images", "people"),
    os.path.join(ROOT, "static", "images", "news"),
]
EXTS = ("jpg", "jpeg", "png", "webp")


def collect(args):
    if "--all" in args:
        out = []
        for d in IMG_DIRS:
            if os.path.isdir(d):
                out += [os.path.join(d, f) for f in sorted(os.listdir(d))
                        if f.lower().rsplit(".", 1)[-1] in EXTS]
        return out
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
                      f"{os.path.relpath(path, ROOT)} (orientation={orientation})")
                if not check_only:
                    fixed = ImageOps.exif_transpose(im)  # bakes rotation, drops the tag
                    kw = dict(quality=92) if im.format == "JPEG" else {}
                    fixed.save(path, format=im.format, **kw)
                changed += 1
            else:
                upright += 1
        except Exception as exc:  # noqa: BLE001 — report and continue
            print(f"[ERROR] {path}: {exc}")

    verb = "flagged" if check_only else "normalized"
    print(f"\nDone: {changed} {verb}, {upright} already upright (of {len(paths)} scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
