#!/usr/bin/env python3
"""
orcid_diff.py — weekly check for new publications via ORCID public API.

Diffs the current ORCID works list against a saved snapshot. Prints any new
entries with title + year + put-code, and updates the snapshot.

Usage:
    python orcid_diff.py
    python orcid_diff.py --reset   # discard snapshot, treat all as known
    python orcid_diff.py --json    # output JSON instead of human-readable

Requires:  pip install requests

Run weekly (manually, via cron, or via Windows Task Scheduler).
Output also written to a log file alongside the snapshot.

Status as of 2026-05-02:
    - Li-Ta's ORCID: 0000-0002-0352-741X
    - Vault location for the diff log: 00 Home/Weekly Publication Check.md (Tracker section)
"""
import argparse
import datetime
import json
import pathlib
import sys

try:
    import requests
except ImportError:
    print("ERROR: 'requests' not installed. Run: pip install requests")
    sys.exit(1)

ORCID = "0000-0002-0352-741X"
BASE = f"https://pub.orcid.org/v3.0/{ORCID}"
HEADERS = {"Accept": "application/json"}
SNAPSHOT = pathlib.Path(__file__).parent / "orcid_snapshot.json"
LOG = pathlib.Path(__file__).parent / "orcid_diff_log.txt"


def fetch_works():
    """Fetch the full works summary list from ORCID public API."""
    r = requests.get(f"{BASE}/works", headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_work_detail(put_code):
    """Fetch one work's full detail (title, year, journal)."""
    try:
        r = requests.get(f"{BASE}/work/{put_code}", headers=HEADERS, timeout=20)
        r.raise_for_status()
        d = r.json()
        title = d.get("title", {}).get("title", {}).get("value", "(no title)")
        year = d.get("publication-date", {}).get("year", {}).get("value", "?") if d.get("publication-date") else "?"
        journal = d.get("journal-title", {}).get("value", "(no venue)") if d.get("journal-title") else "(no venue)"
        return title, year, journal
    except Exception as e:
        return f"(fetch failed: {e})", "?", "?"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reset", action="store_true", help="discard snapshot, treat all as known")
    ap.add_argument("--json", action="store_true", help="JSON output mode")
    args = ap.parse_args()

    today = datetime.date.today().isoformat()

    # Fetch current state
    try:
        data = fetch_works()
    except requests.exceptions.RequestException as e:
        print(f"ERROR fetching ORCID: {e}")
        sys.exit(1)

    current = {g["work-summary"][0]["put-code"] for g in data.get("group", [])}

    # Load prior snapshot
    if args.reset or not SNAPSHOT.exists():
        prior_codes = set()
        prior_date = "never"
    else:
        prior = json.loads(SNAPSHOT.read_text())
        prior_codes = set(prior.get("putcodes", []))
        prior_date = prior.get("last_check", "never")

    new_codes = current - prior_codes

    # Fetch detail for each new entry
    new_entries = []
    for pc in sorted(new_codes):
        title, year, journal = fetch_work_detail(pc)
        new_entries.append({"put_code": pc, "year": year, "title": title, "journal": journal})

    # Output
    if args.json:
        print(json.dumps({
            "check_date": today,
            "prior_check_date": prior_date,
            "total_works_in_orcid": len(current),
            "new_since_last_check": new_entries,
        }, indent=2, ensure_ascii=False))
    else:
        print(f"=== ORCID diff @ {today} (prior: {prior_date}) ===")
        print(f"Total works in ORCID: {len(current)}")
        print(f"New since last check: {len(new_entries)}")
        print()
        if new_entries:
            for e in new_entries:
                print(f"  NEW [{e['year']}] {e['title']}")
                print(f"       venue: {e['journal']} · put-code {e['put_code']}")
                print()
        else:
            print("  (no new publications)")

    # Append to log
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"\n=== {today} ===\n")
        f.write(f"prior: {prior_date}; total: {len(current)}; new: {len(new_entries)}\n")
        for e in new_entries:
            f.write(f"  [{e['year']}] {e['title']} — {e['journal']} (put-code {e['put_code']})\n")

    # Save snapshot
    SNAPSHOT.write_text(json.dumps({
        "putcodes": sorted(current),
        "last_check": today,
        "total": len(current),
    }, indent=2))


if __name__ == "__main__":
    main()
