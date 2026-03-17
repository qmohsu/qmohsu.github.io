#!/usr/bin/env python3
"""Fix publication metadata by re-extracting correct data from CV.

Addresses GitHub Issue #3:
- Fragmented author names (e.g., "Hsu", "L. T" as separate entries)
- Leading "and" in author entries
- Malformed patent titles with broken Markdown links
- Malformed magazine venues with stray punctuation
"""
import re
import os
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV_PATH = os.path.join(REPO_ROOT, "CV (Full) of Li-Ta Hsu.md")
PUB_DIR = os.path.join(REPO_ROOT, "content", "publications")


def looks_like_initials(s):
    """Check if a string looks like author initials (e.g., 'L. T.', 'R.')."""
    s = s.strip().replace('*', '').replace('\\', '').strip()
    if not s:
        return False
    cleaned = s.replace('.', '').replace(' ', '')
    return len(cleaned) <= 4 and cleaned.isupper() and len(cleaned) > 0


def parse_authors_from_cv(authors_str):
    """Parse authors from CV format: 'LastName, F. I., LastName2, F. I., & LastName3, F.'"""
    # Clean markup
    authors_str = authors_str.replace('**', '').replace('\\*', '')
    authors_str = authors_str.replace('*', '').replace('\\', '')
    # Remove "et al."
    authors_str = re.sub(r',?\s*et al\.?', '', authors_str)
    # Normalize ampersand
    authors_str = authors_str.replace(' & ', ', ').replace('&', ',')
    # Fix missing space after comma (e.g., "Shaheer,M.")
    authors_str = re.sub(r',([A-Z])', r', \1', authors_str)

    parts = [p.strip() for p in authors_str.split(',') if p.strip()]

    authors = []
    i = 0
    while i < len(parts):
        part = parts[i].strip()
        if not part:
            i += 1
            continue
        # Remove leading "and"
        part = re.sub(r'^and\s+', '', part).strip()
        if not part:
            i += 1
            continue

        # Check if next part looks like initials
        if i + 1 < len(parts):
            next_part = parts[i + 1].strip().replace('*', '').replace('\\', '').strip()
            if looks_like_initials(next_part):
                # Merge: "LastName" + "F. I." -> "LastName F. I."
                initials = next_part.rstrip('.')
                authors.append(f"{part} {initials}")
                i += 2
                continue

        # Standalone (might already be full name or single-initial author)
        authors.append(part.rstrip('.'))
        i += 1

    return [a.strip() for a in authors if a.strip() and len(a.strip()) > 1]


def parse_cv_journal_entries(lines, start, end):
    """Parse journal paper entries from CV lines."""
    entries = {}
    current_year = 2025

    for i in range(start + 1, end):
        line = lines[i].strip()
        if not line:
            continue

        # Year header
        year_header = re.match(r'\*\*(\d{4}).*\*\*', line)
        if year_header:
            current_year = int(year_header.group(1))
            continue
        if re.match(r'\*\*Before \d{4}', line):
            current_year = 2014
            continue

        # Publication entry
        m = re.match(r'(\d+)\.\s+', line)
        if not m:
            continue
        cv_number = int(m.group(1))
        rest = line[m.end():]

        # Extract authors (before year in parentheses)
        year_match = re.search(r'\((\d{4})\)', rest)
        year = int(year_match.group(1)) if year_match else current_year

        if year_match:
            authors_str = rest[:year_match.start()].rstrip(', ').rstrip()
            after_year = rest[year_match.end():].lstrip('. ,')
        else:
            authors_str = ''
            after_year = rest

        authors = parse_authors_from_cv(authors_str)

        # Extract title
        title = ''
        after_year_clean = after_year.replace('**', '').replace('\\*', '').replace('\\', '')

        # Title in quotes
        quote_match = re.search(r'"([^"]+)"', after_year_clean)
        if quote_match:
            title = quote_match.group(1).strip().rstrip('.')
            after_title = after_year_clean[quote_match.end():].strip().lstrip(',').strip()
        else:
            # Title before first italic *text*
            italic_match = re.search(r'\*([^*]+)\*', after_year_clean)
            if italic_match:
                title = after_year_clean[:italic_match.start()].strip().rstrip(',.').strip()
                after_title = after_year_clean[italic_match.start():]
            else:
                title = after_year_clean.strip().rstrip('.')
                after_title = ''

        # Extract venue (first italic)
        venue = ''
        venue_match = re.search(r'\*([^*]+)\*', after_title if after_title else after_year_clean)
        if venue_match:
            venue = venue_match.group(1).strip().rstrip(',.')

        title = re.sub(r'\s+', ' ', title).strip()
        # Remove markdown links from title, keep text
        title = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', title)

        entries[cv_number] = {
            'authors': authors,
            'title': title,
            'venue': venue,
            'year': year,
        }

    return entries


def parse_cv_patent_entries(lines, start, end):
    """Parse patent entries from CV lines."""
    entries = {}

    for i in range(start + 1, end):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            continue

        m = re.match(r'(\d+)\.\s+', line)
        if not m:
            continue
        cv_number = int(m.group(1))
        rest = line[m.end():]

        # Special case: patent #9 has no authors/title, just a link
        if cv_number == 9 and 'CN111679298A' in rest:
            entries[cv_number] = {
                'authors': ['Wen W.', 'Zhang G.', 'Hsu L. T.'],
                'title': 'A method and system for GNSS positioning assisted by three-dimensional map',
                'venue': 'Patent',
                'year': 2024,
            }
            continue

        # Extract year
        year_match = re.search(r'\((\d{4})\)', rest)
        year = int(year_match.group(1)) if year_match else 2024

        # Authors before year
        if year_match:
            authors_str = rest[:year_match.start()].rstrip(', ').rstrip()
        else:
            # Authors before first italic or link
            first_marker = re.search(r'[\*\[]', rest)
            if first_marker:
                authors_str = rest[:first_marker.start()].rstrip(', ').rstrip()
            else:
                authors_str = rest.split('.')[0]

        authors = parse_authors_from_cv(authors_str)

        # Extract title from *italic*
        title = ''
        title_match = re.search(r'\*([^*]+)\*', rest.replace('**', ''))
        if title_match:
            title = title_match.group(1).strip().rstrip('.')
        else:
            # Fallback: text after year, before link
            if year_match:
                after = rest[year_match.end():].strip().lstrip('. ')
                link_match = re.search(r'\(\[', after)
                if link_match:
                    title = after[:link_match.start()].strip().rstrip('.')
                else:
                    title = after.split('.')[0].strip()
            else:
                title = rest[:60]

        # Remove any broken markdown link fragments from title
        title = re.sub(r'\s*\(\[[^\]]*\]\(https?://[^)]*$', '', title)
        title = re.sub(r'\s*\(\[[^\]]*\]\([^)]*\)\)', '', title)
        title = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', title)
        title = title.strip().rstrip('.')

        entries[cv_number] = {
            'authors': authors,
            'title': title,
            'venue': 'Patent',
            'year': year,
        }

    return entries


def parse_cv_magazine_entries(lines, start, end):
    """Parse magazine article entries from CV lines."""
    entries = {}

    for i in range(start + 1, end):
        line = lines[i].strip()
        if not line or line.startswith('#') or line.startswith('!') or line.startswith('Figure'):
            continue

        m = re.match(r'(\d+)\.\s+', line)
        if not m:
            continue
        cv_number = int(m.group(1))
        rest = line[m.end():]

        # Clean markup
        rest_clean = rest.replace('**', '').replace('\\*', '').replace('\\', '')

        # Magazine format: Authors, "Title", *Venue*, details
        # Or: Authors, "[Title](url)", *Venue*, details

        # Extract title from quotes or [text](url)
        title = ''
        title_match = re.search(r'"\s*\[([^\]]+)\]\([^)]*\)\s*[,.]?"', rest_clean)
        if not title_match:
            title_match = re.search(r'"\[([^\]]+)\]\([^)]*\)', rest_clean)
        if not title_match:
            title_match = re.search(r'\[\s*([^\]]+)\s*\]\([^)]*\)', rest_clean)
        if not title_match:
            title_match = re.search(r'"([^"]+)"', rest_clean)

        if title_match:
            title = title_match.group(1).strip().rstrip('.,')
            authors_str = rest_clean[:title_match.start()].rstrip(', "').rstrip()
        else:
            title = 'Magazine Article'
            authors_str = rest_clean.split(',')[0]

        # Authors: magazine format uses "LastName I." without comma separation
        # But they're comma-separated between authors
        # E.g., "Hsu L. T., Tsai W. M., Jan S. S."
        authors_str = authors_str.replace(' & ', ', ').replace('&', ',')
        # Split by comma, merge last-name + initials pairs
        authors = parse_authors_from_cv(authors_str)

        # Extract venue from *italic*
        venue = ''
        venue_match = re.search(r'\*([^*]+)\*', rest_clean)
        if venue_match:
            venue = venue_match.group(1).strip().rstrip(',.')

        # Extract year
        year_match = re.search(r'(\d{4})', rest_clean)
        year = int(year_match.group(1)) if year_match else 2020

        entries[cv_number] = {
            'authors': authors,
            'title': title,
            'venue': venue,
            'year': year,
        }

    return entries


def parse_cv_book_entries(lines, start, end):
    """Parse book/chapter entries from CV lines."""
    entries = {}

    for i in range(start + 1, end):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            continue

        m = re.match(r'(\d+)\.\s+', line)
        if not m:
            continue
        cv_number = int(m.group(1))
        rest = line[m.end():]

        rest_clean = rest.replace('**', '').replace('\\*', '').replace('\\', '')

        # Title in quotes or from [text](url)
        title = ''
        title_match = re.search(r'"([^"]+)"', rest_clean)
        if not title_match:
            title_match = re.search(r'\[([^\]]+)\]\([^)]*\)', rest_clean)
        if title_match:
            title = title_match.group(1).strip()
            authors_str = rest_clean[:title_match.start()].rstrip(', "').rstrip()
        else:
            title = rest_clean[:80]
            authors_str = ''

        authors_str = authors_str.replace(' & ', ', ').replace('&', ',')
        authors_str = re.sub(r',\s*".*', '', authors_str)
        authors = parse_authors_from_cv(authors_str)

        # Venue/Publisher
        venue = ''
        venue_match = re.search(r'\*([^*]*Publishers[^*]*)\*', rest_clean)
        if not venue_match:
            venue_match = re.search(r'\*([^*]+)\*', rest_clean)
        if venue_match:
            venue = venue_match.group(1).strip().rstrip(',.')

        # Year
        year_match = re.search(r'(\d{4})', rest_clean)
        year = int(year_match.group(1)) if year_match else 2025

        entries[cv_number] = {
            'authors': authors,
            'title': title,
            'venue': venue,
            'year': year,
        }

    return entries


def parse_cv():
    """Parse the full CV and return a map of (type, cv_number) -> metadata."""
    with open(CV_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find section boundaries
    journal_start = patent_start = magazine_start = book_start = opensource_start = None

    for i, line in enumerate(lines):
        if '2.3.1 Journal Papers' in line and '###' in line:
            journal_start = i
        elif '2.3.2 Patents' in line and '###' in line:
            patent_start = i
        elif '2.3.3 Industrial Orientated' in line and '###' in line:
            magazine_start = i
        elif '2.3.4 Book and Book Chapters' in line and '###' in line:
            book_start = i
        elif '2.3.3 Open-Source' in line and '###' in line:
            opensource_start = i

    cv_data = {}

    if journal_start is not None and patent_start is not None:
        journals = parse_cv_journal_entries(lines, journal_start, patent_start)
        for num, data in journals.items():
            cv_data[('journal', num)] = data

    if patent_start is not None and magazine_start is not None:
        patents = parse_cv_patent_entries(lines, patent_start, magazine_start)
        for num, data in patents.items():
            cv_data[('patent', num)] = data

    if magazine_start is not None and book_start is not None:
        magazines = parse_cv_magazine_entries(lines, magazine_start, book_start)
        for num, data in magazines.items():
            cv_data[('magazine', num)] = data

    if book_start is not None and opensource_start is not None:
        books = parse_cv_book_entries(lines, book_start, opensource_start)
        for num, data in books.items():
            cv_data[('book', num)] = data

    return cv_data


def read_front_matter(filepath):
    """Read a publication file and return (front_matter_dict, raw_content)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse YAML-like front matter between --- delimiters
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None, content

    fm_text = fm_match.group(1)
    after_fm = content[fm_match.end():]

    # Extract key fields
    fm = {}

    # type
    type_match = re.search(r'^type:\s*"([^"]*)"', fm_text, re.MULTILINE)
    fm['type'] = type_match.group(1) if type_match else ''

    # cv_number
    cv_match = re.search(r'^cv_number:\s*(\d+)', fm_text, re.MULTILINE)
    fm['cv_number'] = int(cv_match.group(1)) if cv_match else 0

    # title
    title_match = re.search(r'^title:\s*"(.*)"', fm_text, re.MULTILINE)
    fm['title'] = title_match.group(1) if title_match else ''

    # authors (YAML list)
    authors = []
    authors_section = re.search(r'^authors:\s*\n((?:\s+-\s+"[^"]*"\n?)*)', fm_text, re.MULTILINE)
    if authors_section:
        authors = re.findall(r'-\s+"([^"]*)"', authors_section.group(1))
    fm['authors'] = authors

    # venue
    venue_match = re.search(r'^venue:\s*"(.*)"', fm_text, re.MULTILINE)
    fm['venue'] = venue_match.group(1) if venue_match else ''

    fm['_raw_fm'] = fm_text
    fm['_after_fm'] = after_fm

    return fm, content


def has_fragmented_authors(authors):
    """Check if an author list has fragmented entries (single-word last names without initials)."""
    if not authors:
        return False

    single_word_count = 0
    for a in authors:
        a = a.strip()
        # Single word (just a last name, no spaces)
        if ' ' not in a and '.' not in a and len(a) > 1:
            single_word_count += 1
        # Leading "and"
        if a.startswith('and '):
            return True

    # If more than half are single-word entries, likely fragmented
    return single_word_count >= 2 or (single_word_count >= 1 and len(authors) <= 3)


def has_malformed_title(title):
    """Check if a title contains broken markdown link fragments."""
    return bool(re.search(r'\(\[.*\]\(https?://', title)) or bool(re.search(r'\]\(https?://patentimages', title))


def has_malformed_venue(venue):
    """Check if a venue starts with a comma or contains broken quoted text."""
    return venue.strip().startswith(',') or bool(re.search(r'^,\s*"', venue))


def rebuild_front_matter(old_fm_text, new_authors=None, new_title=None, new_venue=None):
    """Rebuild front matter text with updated fields."""
    fm_text = old_fm_text

    if new_authors is not None:
        # Build new authors YAML
        if new_authors:
            authors_yaml = 'authors:\n' + '\n'.join(f'  - "{a}"' for a in new_authors)
        else:
            authors_yaml = 'authors:'

        # Replace existing authors block
        fm_text = re.sub(
            r'^authors:\s*\n(?:\s+-\s+"[^"]*"\n?)*',
            authors_yaml + '\n',
            fm_text,
            flags=re.MULTILINE
        )
        # Also handle empty authors (no list items)
        fm_text = re.sub(
            r'^authors:\s*$',
            authors_yaml,
            fm_text,
            flags=re.MULTILINE
        )

    if new_title is not None:
        safe_title = new_title.replace('"', '\\"')
        fm_text = re.sub(
            r'^title:\s*".*"',
            f'title: "{safe_title}"',
            fm_text,
            flags=re.MULTILINE
        )

    if new_venue is not None:
        safe_venue = new_venue.replace('"', '\\"')
        fm_text = re.sub(
            r'^venue:\s*".*"',
            f'venue: "{safe_venue}"',
            fm_text,
            flags=re.MULTILINE
        )

    return fm_text


def fix_publication_file(filepath, cv_data):
    """Fix a single publication file. Returns description of changes or None."""
    fm, raw_content = read_front_matter(filepath)
    if fm is None:
        return None

    pub_type = fm['type']
    cv_number = fm['cv_number']
    key = (pub_type, cv_number)

    changes = []
    new_authors = None
    new_title = None
    new_venue = None

    # Check if we have CV data for this entry
    cv_entry = cv_data.get(key)

    # Fix fragmented authors
    if has_fragmented_authors(fm['authors']):
        if cv_entry and cv_entry['authors']:
            new_authors = cv_entry['authors']
            changes.append(f"authors: {fm['authors']} -> {new_authors}")
        else:
            # Try to merge fragmented entries heuristically
            merged = merge_authors_heuristic(fm['authors'])
            if merged != fm['authors']:
                new_authors = merged
                changes.append(f"authors (heuristic): {fm['authors']} -> {new_authors}")

    # Fix leading "and" in authors (even if not fragmented)
    if new_authors is None and fm['authors']:
        fixed = [re.sub(r'^and\s+', '', a).strip() for a in fm['authors']]
        if fixed != fm['authors']:
            new_authors = fixed
            changes.append(f"removed leading 'and' from authors")

    # Fix malformed titles
    if has_malformed_title(fm['title']):
        if cv_entry and cv_entry['title']:
            new_title = cv_entry['title']
            changes.append(f"title: '{fm['title'][:50]}...' -> '{new_title[:50]}...'")

    # Fix malformed venues
    if has_malformed_venue(fm['venue']):
        if cv_entry and cv_entry['venue']:
            new_venue = cv_entry['venue']
            changes.append(f"venue: '{fm['venue'][:50]}...' -> '{new_venue}'")

    if not changes:
        return None

    # Rebuild and write
    new_fm_text = rebuild_front_matter(fm['_raw_fm'], new_authors, new_title, new_venue)
    new_content = f'---\n{new_fm_text}\n---{fm["_after_fm"]}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return changes


def merge_authors_heuristic(authors):
    """Attempt to merge fragmented author entries heuristically."""
    merged = []
    i = 0
    while i < len(authors):
        a = authors[i].strip()
        # Remove leading "and"
        a = re.sub(r'^and\s+', '', a).strip()
        if not a:
            i += 1
            continue

        # Check if next entry looks like initials
        if i + 1 < len(authors):
            next_a = authors[i + 1].strip()
            next_a = re.sub(r'^and\s+', '', next_a).strip()
            if looks_like_initials(next_a):
                merged.append(f"{a} {next_a}")
                i += 2
                continue

        merged.append(a)
        i += 1

    return merged


def main():
    print("Parsing CV for correct metadata...")
    cv_data = parse_cv()
    print(f"Found {len(cv_data)} CV entries")

    # Process all publication files
    pub_files = sorted(glob.glob(os.path.join(PUB_DIR, '*.md')))
    print(f"Found {len(pub_files)} publication files")

    fixed_count = 0
    for filepath in pub_files:
        filename = os.path.basename(filepath)
        changes = fix_publication_file(filepath, cv_data)
        if changes:
            fixed_count += 1
            print(f"\nFixed: {filename}")
            for c in changes:
                print(f"  {c}")

    print(f"\n{'='*60}")
    print(f"Total files fixed: {fixed_count}")
    print(f"Total files unchanged: {len(pub_files) - fixed_count}")


if __name__ == '__main__':
    main()
