#!/usr/bin/env python3
"""Clean up publication metadata: remove duplicate authors, fix remaining edge cases."""
import re
import os
import glob

PUB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "publications")

# Manual fixes for known edge cases
MANUAL_FIXES = {
    # (type, cv_number): {'authors': [...], 'title': '...', 'venue': '...'}
    ('journal', 59): {
        'authors': ['Jia Q', 'Hsu L. T', 'Wu R'],
    },
    ('journal', 49): {
        'authors': ['Zhang Z', 'Li Y', 'He X', 'Hsu L. T'],
    },
    ('journal', 9): {  # 2025 multiple faults
        'authors': ['Yan P', 'Hu Y', 'Wen W', 'Hsu L. T'],
    },
    ('journal', 144): {
        'venue': 'Journal of the Chinese Society of Mechanical Engineers',
    },
    ('journal', 66): {
        'venue': 'IEEE Transactions on Instrumentation and Measurement',
    },
    ('journal', 65): {
        'venue': 'IEEE Transactions on Aerospace and Electronic Systems',
    },
    ('patent', 11): {
        'authors': ['Wang Y', 'Hsu L. T'],
    },
    ('patent', 7): {
        'authors': ['Wang Q', 'Huang X', 'Shaheer M', 'Mohammad T', 'Zhang X', 'Luo M', 'Hsu L. T', 'Wu X', 'Xiao F', 'Usmani A'],
    },
    ('patent', 3): {
        'authors': ['Wang Q', 'Huang X', 'Shaheer M', 'Mohammad T', 'Zhang X', 'Luo M', 'Hsu L. T', 'Usmani A'],
    },
    ('patent', 9): {
        'authors': ['Wen W', 'Zhang G', 'Hsu L. T'],
        'title': 'A method and system for GNSS positioning assisted by three-dimensional map',
    },
}


def process_file(filepath):
    """Process a single publication file: deduplicate authors and apply manual fixes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter
    fm_match = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    after_fm = content[fm_match.end():]

    # Extract type and cv_number
    type_match = re.search(r'^type:\s*"([^"]*)"', fm_text, re.MULTILINE)
    cv_match = re.search(r'^cv_number:\s*(\d+)', fm_text, re.MULTILINE)
    pub_type = type_match.group(1) if type_match else ''
    cv_number = int(cv_match.group(1)) if cv_match else 0

    key = (pub_type, cv_number)
    changed = False

    # Extract current authors
    authors = []
    authors_match = re.search(r'^authors:\s*\r?\n((?:\s+-\s+"[^"]*"\r?\n?)*)', fm_text, re.MULTILINE)
    if authors_match:
        authors = re.findall(r'-\s+"([^"]*)"', authors_match.group(1))

    # Deduplicate authors (preserve order)
    seen = set()
    unique_authors = []
    for a in authors:
        if a not in seen:
            seen.add(a)
            unique_authors.append(a)

    # Apply manual fixes
    manual = MANUAL_FIXES.get(key)
    if manual:
        if 'authors' in manual:
            unique_authors = manual['authors']
            changed = True
        if 'title' in manual:
            safe_title = manual['title'].replace('"', '\\"')
            fm_text = re.sub(r'^title:\s*".*"', f'title: "{safe_title}"', fm_text, flags=re.MULTILINE)
            changed = True
        if 'venue' in manual:
            safe_venue = manual['venue'].replace('"', '\\"')
            fm_text = re.sub(r'^venue:\s*".*"', f'venue: "{safe_venue}"', fm_text, flags=re.MULTILINE)
            changed = True

    # Check if dedup changed anything
    if unique_authors != authors:
        changed = True

    if not changed:
        return False

    # Rebuild authors YAML
    if unique_authors:
        new_authors_yaml = 'authors:\n' + '\n'.join(f'  - "{a}"' for a in unique_authors)
    else:
        new_authors_yaml = 'authors:'

    # Replace authors block in front matter
    # Use a more robust replacement: find "authors:" line and all following "  - " lines
    lines = fm_text.split('\n')
    new_lines = []
    in_authors = False
    authors_replaced = False
    for line in lines:
        if re.match(r'^authors:\s*', line):
            in_authors = True
            if not authors_replaced:
                new_lines.append(new_authors_yaml)
                authors_replaced = True
            continue
        if in_authors:
            if re.match(r'^\s+-\s+"', line):
                continue  # Skip old author lines
            else:
                in_authors = False
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_fm_text = '\n'.join(new_lines)
    new_content = f'---\n{new_fm_text}\n---{after_fm}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    basename = os.path.basename(filepath)
    if unique_authors != authors:
        print(f"Fixed: {basename} [{len(authors)} -> {len(unique_authors)} authors]")
    else:
        print(f"Fixed: {basename} [manual fix applied]")
    return True


def main():
    pub_files = sorted(glob.glob(os.path.join(PUB_DIR, '*.md')))
    print(f"Processing {len(pub_files)} publication files...")

    fixed = 0
    for f in pub_files:
        if process_file(f):
            fixed += 1

    print(f"\nTotal files fixed: {fixed}")


if __name__ == '__main__':
    main()
