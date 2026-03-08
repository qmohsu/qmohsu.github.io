#!/usr/bin/env python3
"""Look up DOIs for all publications via CrossRef API and update front matter."""

import io
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error

# Force UTF-8 output on Windows to avoid cp1252 encoding errors
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
import urllib.parse
from difflib import SequenceMatcher

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
PUBLICATIONS_DIR = os.path.join(PROJECT_ROOT, "content", "publications")
LOG_FILE = os.path.join(SCRIPT_DIR, "doi_lookup_log.json")

CROSSREF_API = "https://api.crossref.org/works"
MAILTO = "lt.hsu@polyu.edu.hk"
USER_AGENT = f"IPNL-DOI-Lookup/1.0 (mailto:{MAILTO})"

# Matching thresholds
HIGH_THRESHOLD = 0.85
LOW_THRESHOLD = 0.60


def normalize_title(title):
    """Normalize a title for comparison."""
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def title_similarity(a, b):
    """Compare two titles with fuzzy matching."""
    return SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


def parse_front_matter(filepath):
    """Extract metadata from YAML front matter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, content

    yaml_str = match.group(1)

    title_m = re.search(r'title:\s*"(.+?)"', yaml_str)
    year_m = re.search(r'year:\s*(\d+)', yaml_str)
    doi_m = re.search(r'doi:\s*"(.*?)"', yaml_str)
    pub_type_m = re.search(r'type:\s*"(.*?)"', yaml_str)
    authors = re.findall(r'-\s*"(.+?)"', yaml_str)

    return {
        'title': title_m.group(1) if title_m else '',
        'year': int(year_m.group(1)) if year_m else 0,
        'doi': doi_m.group(1) if doi_m else '',
        'pub_type': pub_type_m.group(1) if pub_type_m else '',
        'authors': authors,
    }, content


def get_author_lastnames(authors):
    """Extract last names from author list for querying."""
    lastnames = []
    for a in authors:
        a = a.strip()
        if not a:
            continue
        # Handle "Hsu L. T" or "Hsu, L.-T." or "L. T" (fragment)
        parts = re.split(r'[,\s]+', a)
        # Take first substantial part (>1 char, not just initials)
        for p in parts:
            cleaned = re.sub(r'[^a-zA-Z]', '', p)
            if len(cleaned) > 1:
                lastnames.append(cleaned)
                break
    return lastnames


def query_crossref(title, authors, year):
    """Query CrossRef API for a publication. Returns (doi, confidence, message)."""
    # Truncate very long titles
    query_title = title[:150] if len(title) > 150 else title

    params = {
        'query.bibliographic': query_title,
        'rows': '5',
        'select': 'DOI,title,author,published-print,published-online,container-title,score',
        'mailto': MAILTO,
    }

    # Add author filter — use "Hsu" as anchor since PI is on most papers
    lastnames = get_author_lastnames(authors)
    hsu_present = any('hsu' in ln.lower() for ln in lastnames)
    if hsu_present:
        params['query.author'] = 'Hsu'
    elif lastnames:
        params['query.author'] = lastnames[0]

    url = CROSSREF_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return None, 0, f"HTTP {e.code}"
    except Exception as e:
        return None, 0, f"Error: {e}"

    items = data.get('message', {}).get('items', [])
    if not items:
        return None, 0, "No results from CrossRef"

    best_doi = None
    best_score = 0
    best_cr_title = ""

    for item in items:
        cr_titles = item.get('title', [])
        if not cr_titles:
            continue
        cr_title = cr_titles[0]
        sim = title_similarity(title, cr_title)

        # Check year match (within ±1)
        cr_year = None
        for date_field in ['published-print', 'published-online']:
            if date_field in item:
                parts = item[date_field].get('date-parts', [[]])
                if parts and parts[0]:
                    cr_year = parts[0][0]
                    break

        # Penalize year mismatch
        year_ok = True
        if cr_year and year and abs(cr_year - year) > 1:
            year_ok = False
            sim *= 0.7  # Reduce score for year mismatch

        if sim > best_score:
            best_score = sim
            best_doi = item.get('DOI')
            best_cr_title = cr_title

    if best_doi and best_score >= LOW_THRESHOLD:
        confidence = "high" if best_score >= HIGH_THRESHOLD else "medium"
        return best_doi, best_score, f"{confidence} match (score={best_score:.3f})"

    return None, best_score, f"No good match (best={best_score:.3f}, title='{best_cr_title[:60]}')"


def update_doi_in_file(filepath, doi):
    """Replace doi: "" with the found DOI in the file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple and safe replacement — only replaces first occurrence of empty doi
    updated = content.replace('doi: ""', f'doi: "{doi}"', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated)


def main():
    results = {
        "found_high": [],
        "found_medium": [],
        "not_found": [],
        "errors": [],
        "skipped": [],
    }

    files = sorted([
        f for f in os.listdir(PUBLICATIONS_DIR)
        if f.endswith('.md') and f != '_index.md'
    ])

    total = len(files)
    print(f"Looking up DOIs for {total} publications...\n")

    found_count = 0
    for i, filename in enumerate(files, 1):
        filepath = os.path.join(PUBLICATIONS_DIR, filename)
        meta, content = parse_front_matter(filepath)

        if not meta or not meta['title']:
            results['errors'].append({"file": filename, "reason": "Could not parse"})
            print(f"  [{i:3d}/{total}] E {filename} -- parse error")
            continue

        if meta['doi']:
            results['skipped'].append(filename)
            print(f"  [{i:3d}/{total}] S {filename} -- already has DOI")
            continue

        # Skip patents (CrossRef won't have them)
        if meta['pub_type'] == 'patent':
            results['not_found'].append({
                "file": filename,
                "title": meta['title'][:80],
                "reason": "Skipped (patent — not in CrossRef)"
            })
            print(f"  [{i:3d}/{total}] - {filename} -- patent, skipped")
            continue

        doi, score, message = query_crossref(
            meta['title'], meta['authors'], meta['year']
        )

        if doi:
            update_doi_in_file(filepath, doi)
            found_count += 1
            entry = {
                "file": filename,
                "doi": doi,
                "score": round(score, 3),
                "title": meta['title'][:80],
            }
            if score >= HIGH_THRESHOLD:
                results['found_high'].append(entry)
                print(f"  [{i:3d}/{total}] + {filename} -> {doi}")
            else:
                results['found_medium'].append(entry)
                print(f"  [{i:3d}/{total}] ? {filename} -> {doi} ({message})")
        else:
            results['not_found'].append({
                "file": filename,
                "title": meta['title'][:80],
                "reason": message,
            })
            print(f"  [{i:3d}/{total}] X {filename} -- {message}")

        # Rate limiting: ~1 req/sec
        time.sleep(1.0)

    # Write log
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    high = len(results['found_high'])
    medium = len(results['found_medium'])
    not_found = len(results['not_found'])
    errors = len(results['errors'])
    skipped = len(results['skipped'])

    print(f"\n{'='*60}")
    print(f"Results: {high} high-confidence, {medium} medium-confidence,")
    print(f"         {not_found} not found, {errors} errors, {skipped} skipped")
    print(f"Total DOIs added: {high + medium}")
    print(f"Log saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()
