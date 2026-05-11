#!/usr/bin/env python3
"""Soft-dedup pass for content/publications/*.md.

Runs after parse_publications.py + lookup_dois.py. Groups files by DOI (primary)
or normalized (title, year, first-author-surname) (fallback), picks the most
complete copy per group, deletes the rest, and records each decision to
scripts/dedupe_log.json for audit.

Usage:
    python scripts/dedupe_publications.py [--dry-run] [--verbose]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable

SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT: str = os.path.dirname(SCRIPT_DIR)
PUB_DIR: str = os.path.join(REPO_ROOT, "content", "publications")
LOG_PATH: str = os.path.join(SCRIPT_DIR, "dedupe_log.json")


@dataclass(frozen=True)
class Pub:
    path: str
    doi: str
    title: str
    year: int
    authors: tuple[str, ...]
    themes: tuple[str, ...]
    quartile: str
    pdf: str
    code: str
    data: str
    cv_number: int


def _strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
    return s.replace('\\"', '"')


def _parse_scalar(text: str, key: str) -> str:
    m = re.search(rf'^{re.escape(key)}:\s*(.*)$', text, re.MULTILINE)
    if not m:
        return ""
    raw = m.group(1).strip()
    # Skip list openers ("[]" or empty after colon -> caller should use list parser)
    if raw.startswith("[") or raw == "":
        return ""
    return _strip_quotes(raw)


def _parse_yaml_list(text: str, key: str) -> list[str]:
    inline = re.search(rf'^{re.escape(key)}:\s*\[\s*\]\s*$', text, re.MULTILINE)
    if inline:
        return []
    block = re.search(
        rf'^{re.escape(key)}:\s*\n((?:[ \t]+-[ \t]+.*\n?)+)', text, re.MULTILINE
    )
    if not block:
        return []
    items = re.findall(r'-[ \t]+(.*)', block.group(1))
    return [_strip_quotes(it.strip()) for it in items if it.strip()]


def parse_pub(path: str) -> Pub | None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    fm = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not fm:
        return None
    fm_text = fm.group(1)

    try:
        year = int(_parse_scalar(fm_text, "year") or "0")
    except ValueError:
        year = 0
    try:
        cv_number = int(_parse_scalar(fm_text, "cv_number") or "0")
    except ValueError:
        cv_number = 0

    return Pub(
        path=path,
        doi=_parse_scalar(fm_text, "doi"),
        title=_parse_scalar(fm_text, "title"),
        year=year,
        authors=tuple(_parse_yaml_list(fm_text, "authors")),
        themes=tuple(_parse_yaml_list(fm_text, "themes")),
        quartile=_parse_scalar(fm_text, "quartile"),
        pdf=_parse_scalar(fm_text, "pdf"),
        code=_parse_scalar(fm_text, "code"),
        data=_parse_scalar(fm_text, "data"),
        cv_number=cv_number,
    )


def normalize_doi(doi: str) -> str:
    d = doi.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if d.startswith(prefix):
            d = d[len(prefix):]
    return d.strip()


def normalize_title(title: str) -> str:
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def first_author_surname(authors: tuple[str, ...]) -> str:
    if not authors:
        return ""
    a = authors[0].strip().rstrip(",.")
    tokens = a.split()
    if not tokens:
        return ""
    # "Hsu L. T." form -> first token is surname.
    # "Chi-Lok Tsang" form -> last token is surname.
    rest_looks_like_initials = any(
        ("." in tok) or (tok.isupper() and 1 <= len(tok.replace(".", "")) <= 3)
        for tok in tokens[1:]
    )
    surname = tokens[0] if rest_looks_like_initials else tokens[-1]
    return re.sub(r'[^a-z\-]', '', surname.lower())


def has_full_first_name(pub: Pub) -> bool:
    """True if at least one author entry has a multi-char alphabetic token in
    position 2 — a soft signal of 'Chi-Lok Tsang' style over 'Tsang, C. L.' style."""
    for a in pub.authors:
        tokens = a.split()
        if len(tokens) >= 2:
            second = tokens[1].rstrip(",.").replace("-", "")
            if second.isalpha() and len(second) >= 3:
                return True
    return False


def primary_key(pub: Pub) -> str | None:
    d = normalize_doi(pub.doi)
    return d or None


def fallback_key(pub: Pub) -> tuple[str, int, str] | None:
    t = normalize_title(pub.title)
    s = first_author_surname(pub.authors)
    if not t or pub.year <= 0 or not s:
        return None
    return (t, pub.year, s)


def score(pub: Pub) -> int:
    s = 0
    if normalize_doi(pub.doi):
        s += 3
    if pub.themes:
        s += 2
    if pub.quartile:
        s += 1
    if has_full_first_name(pub):
        s += 1
    if pub.pdf:
        s += 1
    if pub.code:
        s += 1
    if pub.data:
        s += 1
    return s


def pick_keeper(group: list[Pub]) -> Pub:
    return max(
        group,
        key=lambda p: (score(p), p.cv_number, len(os.path.basename(p.path))),
    )


def group_publications(pubs: Iterable[Pub]) -> list[list[Pub]]:
    primary_groups: dict[str, list[Pub]] = {}
    no_doi: list[Pub] = []
    for p in pubs:
        k = primary_key(p)
        if k:
            primary_groups.setdefault(k, []).append(p)
        else:
            no_doi.append(p)
    fallback_groups: dict[tuple[str, int, str], list[Pub]] = {}
    for p in no_doi:
        k = fallback_key(p)
        if k:
            fallback_groups.setdefault(k, []).append(p)
    return [*primary_groups.values(), *fallback_groups.values()]


def fields_not_in_keeper(keeper: Pub, loser: Pub) -> dict[str, object]:
    lost: dict[str, object] = {}
    if loser.quartile and not keeper.quartile:
        lost["quartile"] = loser.quartile
    if loser.themes and not keeper.themes:
        lost["themes"] = list(loser.themes)
    if loser.pdf and not keeper.pdf:
        lost["pdf"] = loser.pdf
    if loser.code and not keeper.code:
        lost["code"] = loser.code
    if loser.data and not keeper.data:
        lost["data"] = loser.data
    if normalize_doi(loser.doi) and not normalize_doi(keeper.doi):
        lost["doi"] = loser.doi
    return lost


def append_log(entries: list[dict[str, object]]) -> None:
    if not entries:
        return
    existing: list[dict[str, object]] = []
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if not isinstance(existing, list):
                existing = []
        except (json.JSONDecodeError, OSError):
            existing = []
    existing.extend(entries)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _rel(path: str) -> str:
    return os.path.relpath(path, REPO_ROOT).replace("\\", "/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="Print decisions without deleting."
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Show scan totals and singleton groups."
    )
    args = parser.parse_args()

    if not os.path.isdir(PUB_DIR):
        print(f"error: publications directory not found: {PUB_DIR}", file=sys.stderr)
        return 1

    md_files = sorted(
        os.path.join(PUB_DIR, name)
        for name in os.listdir(PUB_DIR)
        if name.endswith(".md") and name != "_index.md"
    )

    pubs: list[Pub] = []
    for path in md_files:
        pub = parse_pub(path)
        if pub is None:
            print(f"warning: could not parse frontmatter: {_rel(path)}", file=sys.stderr)
            continue
        pubs.append(pub)

    groups = group_publications(pubs)
    duplicates = [g for g in groups if len(g) > 1]

    if args.verbose:
        print(f"Scanned {len(pubs)} publication files.")
        print(f"Found {len(groups)} unique groups; {len(duplicates)} contain duplicates.")

    log_entries: list[dict[str, object]] = []
    deleted_count = 0
    timestamp = datetime.now(timezone.utc).isoformat()

    for group in duplicates:
        keeper = pick_keeper(group)
        losers = [p for p in group if p.path != keeper.path]
        pkey = primary_key(keeper)
        fkey = fallback_key(keeper)
        key_repr = pkey if pkey else (f"title+year+author={fkey}" if fkey else "?")

        per_loser_records: list[dict[str, object]] = []
        for loser in losers:
            per_loser_records.append(
                {
                    "path": _rel(loser.path),
                    "title": loser.title,
                    "doi": loser.doi,
                    "cv_number": loser.cv_number,
                    "fields_not_in_keeper": fields_not_in_keeper(keeper, loser),
                }
            )
        log_entries.append(
            {
                "timestamp": timestamp,
                "dedup_key": key_repr,
                "kept": {
                    "path": _rel(keeper.path),
                    "title": keeper.title,
                    "doi": keeper.doi,
                    "score": score(keeper),
                    "cv_number": keeper.cv_number,
                },
                "removed": per_loser_records,
                "dry_run": args.dry_run,
            }
        )

        action = "would delete" if args.dry_run else "deleting"
        print(f"\nDup group [key={key_repr}]")
        print(f"  KEEP   (score={score(keeper)}, cv={keeper.cv_number}): {_rel(keeper.path)}")
        for loser in losers:
            lost = fields_not_in_keeper(keeper, loser)
            tail = f"  [loses fields: {lost}]" if lost else ""
            print(
                f"  {action} (score={score(loser)}, cv={loser.cv_number}): "
                f"{_rel(loser.path)}{tail}"
            )
            if not args.dry_run:
                try:
                    os.remove(loser.path)
                    deleted_count += 1
                except OSError as e:
                    print(f"  ERROR removing {loser.path}: {e}", file=sys.stderr)
                    return 2

    if duplicates and not args.dry_run:
        append_log(log_entries)

    if args.dry_run:
        print(
            f"\nDry run: {len(duplicates)} duplicate group(s) found, 0 files deleted."
        )
    else:
        print(
            f"\nDone: removed {deleted_count} duplicate file(s) across "
            f"{len(duplicates)} group(s)."
        )
        if log_entries:
            print(f"Decisions logged to {_rel(LOG_PATH)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
