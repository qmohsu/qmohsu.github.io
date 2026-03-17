#!/usr/bin/env python3
"""Add provenance metadata to news entries.

Addresses GitHub Issue #5:
- Classify each news entry by source type
- Add source_url and source_site fields
- Document date semantics
"""
import re
import os
import glob

NEWS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "news")

# Provenance classification based on Issue #5 audit
PROVENANCE = {
    # legacy IPN Lab / AAE activity page migrations
    "2017-gnss-summer-school.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2017-icase-keynote.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2018-asia-mae-workshop.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2018-gnss-summer-school.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2018-ion-gnss.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2018-songshan-lake.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2019-dr-suzuki-visit.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2019-ion-gnss.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2019-ipnl-retreat.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2019-qianhai-competition.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2020-urbanloco-dataset.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2021-halloween.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-astri-visit.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-certificate-awards.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-cheung-chau.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-saic-meeting.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-student-outing-july.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2022-student-outing-october.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2023-dr-huang-visit.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2023-dr-peng-visit.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2023-gnss-seminar.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    "2023-itsc-workshop.md": {
        "source_type": "legacy_ipnl_migration",
        "source_site": "legacy-ipnl",
    },
    # AAE news adaptations
    "2023-per-enge-award.md": {
        "source_type": "aae_news_adaptation",
        "source_site": "aae",
        "source_url": "https://www.polyu.edu.hk/aae/news-and-events/news/2023/dr-hsu---2022-per-enge-early-achievement-award/",
    },
    "2024-ion-most-cited.md": {
        "source_type": "aae_news_adaptation",
        "source_site": "aae",
        "source_url": "https://www.polyu.edu.hk/aae/news-and-events/news/2025/20251002_gnss-most-cited/",
    },
    "2025-stanford-top2.md": {
        "source_type": "aae_news_adaptation",
        "source_site": "aae",
        "source_url": "https://www.polyu.edu.hk/aae/news-and-events/news/2025/20250925_aae-scholars-2025/",
    },
    # PolyU main page adaptations
    "2024-google-grant.md": {
        "source_type": "polyu_adaptation",
        "source_site": "polyu-rio",
        "source_url": "https://www.polyu.edu.hk/rio/news/2024/20241126---polyu-aviation-researcher-supported-by-google/",
    },
    "2022-endowed-young-scholars.md": {
        "source_type": "polyu_adaptation",
        "source_site": "aae",
        "source_url": "https://www.polyu.edu.hk/aae/news-and-events/news/2021/dr-lt-hsu---limin-endowed-young-scholar/",
    },
    # PolyU event page adaptation
    "2024-ipin-conference.md": {
        "source_type": "polyu_event_adaptation",
        "source_site": "polyu-events",
        "source_url": "https://www.polyu.edu.hk/aae/News-and-Events/Event/2024/10/14---IPIN2024",
    },
    # Original local news
    "2024-google-visiting.md": {
        "source_type": "original_local",
        "source_site": "original",
    },
    "2025-ion-technical-rep.md": {
        "source_type": "original_local",
        "source_site": "original",
    },
}

# Date semantics documentation:
# The `date` field in news entries represents the EVENT date (when the
# achievement/event occurred), not the source publication date.
# For adapted entries, the source may have been published later.
DATE_NOTES = {
    "2024-google-grant.md": "Event date; official PolyU pages published 2024-11-26/28",
    "2024-ion-most-cited.md": "Event date; official AAE page published 2025-10-02",
    "2025-stanford-top2.md": "Event date; official AAE page published 2025-09-25",
}


def add_provenance_to_file(filepath, prov_data, date_note=None):
    """Add provenance fields to a news file's front matter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_match = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    after_fm = content[fm_match.end():]

    # Check if provenance fields already exist
    if 'source_type:' in fm_text:
        return False

    # Build provenance lines
    prov_lines = []
    prov_lines.append(f'source_type: "{prov_data["source_type"]}"')
    prov_lines.append(f'source_site: "{prov_data["source_site"]}"')
    if 'source_url' in prov_data:
        prov_lines.append(f'source_url: "{prov_data["source_url"]}"')
    if date_note:
        prov_lines.append(f'date_note: "{date_note}"')

    # Append provenance to end of front matter
    new_fm = fm_text.rstrip() + '\n' + '\n'.join(prov_lines)
    new_content = f'---\n{new_fm}\n---{after_fm}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    news_files = sorted(glob.glob(os.path.join(NEWS_DIR, '*.md')))
    print(f"Found {len(news_files)} news files")

    fixed = 0
    for filepath in news_files:
        basename = os.path.basename(filepath)
        if basename == '_index.md':
            continue

        prov_data = PROVENANCE.get(basename)
        if not prov_data:
            print(f"WARNING: No provenance data for {basename}")
            continue

        date_note = DATE_NOTES.get(basename)
        if add_provenance_to_file(filepath, prov_data, date_note):
            fixed += 1
            src = prov_data['source_type']
            url = prov_data.get('source_url', '')
            print(f"Added: {basename} [{src}]{' -> ' + url[:60] if url else ''}")

    print(f"\nTotal files updated: {fixed}")


if __name__ == '__main__':
    main()
