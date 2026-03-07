"""Parse CV to extract publications and generate Hugo content files."""
import re
import os
import unicodedata

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "publications")

# Featured papers from research.md
FEATURED_TITLES = [
    "Hong Kong UrbanNav",
    "Factor graph optimization for GNSS/INS integration",
    "3D Mapping Database Aided GNSS RTK",
    "Robust GNSS Shadow Matching for Smartphones",
    "PositionNet",
    "GLIO",
]

def clean_text(text):
    """Remove markdown artifacts and escape sequences from text."""
    text = text.replace("**", "")
    text = text.replace("\\*", "")
    text = text.replace("\\-", "-")
    text = text.replace("\\_", "_")
    text = text.replace("\\", "")
    text = text.replace("*", "")
    # Remove markdown link syntax, keep text
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # Remove remaining special chars that break YAML
    text = text.replace("\t", " ")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def slugify(text):
    """Convert text to URL-friendly slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text[:80].rstrip("-")

def is_featured(title):
    """Check if a title matches one of the featured publications."""
    title_lower = title.lower()
    for ft in FEATURED_TITLES:
        if ft.lower() in title_lower:
            return True
    return False

def guess_themes(title, venue):
    """Guess research themes based on title/venue keywords."""
    themes = []
    t = (title + " " + venue).lower()
    if any(w in t for w in ["urban", "nlos", "multipath", "shadow matching", "gnss positioning", "gnss nlos"]):
        themes.append("urban-gnss")
    if any(w in t for w in ["factor graph", "fgo", "factor-graph"]):
        themes.append("factor-graph-optimization")
    if any(w in t for w in ["3d map", "3dma", "building model", "city model", "mapping-aided", "mapping database"]):
        themes.append("3d-mapping-aided")
    if any(w in t for w in ["lidar", "imu", "multi-sensor", "visual-inertial", "sensor fusion", "tightly coupled", "loosely coupled", "camera"]):
        themes.append("multi-sensor-fusion")
    if any(w in t for w in ["smartphone", "android", "pedestrian"]):
        themes.append("smartphone-positioning")
    if any(w in t for w in ["indoor", "uwb", "wi-fi", "wifi"]):
        themes.append("indoor-positioning")
    return themes

def parse_journal_line(line, current_year):
    """Parse a single journal paper line."""
    # Pattern: N. Authors (YEAR). Title. *Venue*, details.
    # Or: N. Authors (YEAR) "Title" ...

    # Extract number
    m = re.match(r"(\d+)\.\s+", line)
    if not m:
        return None
    cv_number = int(m.group(1))
    rest = line[m.end():]

    # Remove markdown bold markers and escape sequences
    rest = rest.replace("**", "")
    rest = rest.replace("\\*", "")
    rest = rest.replace("\\-", "-")
    rest = rest.replace("\\_", "_")
    rest = rest.replace("\\", "")

    # Try to extract year from (YYYY) pattern
    year_match = re.search(r"\((\d{4})\)", rest)
    year = int(year_match.group(1)) if year_match else current_year

    # Split at year to get authors and rest
    if year_match:
        authors_str = rest[:year_match.start()].rstrip(", ").rstrip()
        after_year = rest[year_match.end():].lstrip(". ").lstrip(",").lstrip(". ")
    else:
        authors_str = ""
        after_year = rest

    # Parse authors - split by comma but be careful of "& "
    authors_str = authors_str.replace(" & ", ", ").replace("&", ",")
    authors = [a.strip().rstrip(",").strip() for a in authors_str.split(",") if a.strip()]
    # Merge multi-part names (e.g., "Hsu" "L. T." -> "Hsu, L. T.")
    # Authors are already in "Last, F." format mostly

    # Clean up authors list - remove empty entries
    authors = [a for a in authors if a and len(a) > 1]

    # Extract title and venue from after_year
    # Title usually ends before *VenueName* (italic)
    # Or is in quotes "Title"
    title = ""
    venue = ""

    # Check for quoted title
    quote_match = re.search(r'"([^"]+)"', after_year)
    if quote_match:
        title = quote_match.group(1).strip().rstrip(".")
        after_title = after_year[quote_match.end():].strip().lstrip(",").strip()
    else:
        # Title is before the first italic *text*
        italic_match = re.search(r'\*([^*]+)\*', after_year)
        if italic_match:
            title = after_year[:italic_match.start()].strip().rstrip(",").rstrip(".").strip()
            after_title = after_year[italic_match.start():]
        else:
            title = after_year.strip().rstrip(".")
            after_title = ""

    # Extract venue (first italic text)
    venue_match = re.search(r'\*([^*]+)\*', after_title if after_title else after_year)
    if venue_match:
        venue = venue_match.group(1).strip().rstrip(",").rstrip(".")

    # Clean up title
    title = title.strip().rstrip(".").strip()
    title = re.sub(r'\s+', ' ', title)

    # Remove any remaining markdown
    title = title.replace("*", "")

    if not title:
        return None

    return {
        "cv_number": cv_number,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "type": "journal",
    }

def parse_patent_line(line):
    """Parse a patent line."""
    m = re.match(r"(\d+)\.\s+", line)
    if not m:
        return None
    cv_number = int(m.group(1))
    rest = line[m.end():].replace("**", "")

    year_match = re.search(r"\((\d{4})\)", rest)
    year = int(year_match.group(1)) if year_match else 2024

    # Authors before year
    if year_match:
        authors_str = rest[:year_match.start()].rstrip(", ").rstrip()
    else:
        authors_str = rest.split(".")[0]

    authors_str = authors_str.replace(" & ", ", ").replace("&", ",")
    authors = [a.strip().rstrip(",").strip() for a in authors_str.split(",") if a.strip() and len(a.strip()) > 1]

    # Title is in *italic*
    title_match = re.search(r'\*([^*]+)\*', rest)
    if title_match:
        title = title_match.group(1).strip().rstrip(".")
    else:
        # Fallback: text after year
        if year_match:
            title = rest[year_match.end():].strip().lstrip(". ")
            title = title.split(".")[0].strip()
        else:
            title = rest[:60]

    return {
        "cv_number": cv_number,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": "Patent",
        "type": "patent",
    }

def parse_magazine_line(line):
    """Parse a magazine article line."""
    m = re.match(r"(\d+)\.\s+", line)
    if not m:
        return None
    cv_number = int(m.group(1))
    rest = line[m.end():].replace("**", "")

    # Extract title from quotes or brackets
    title_match = re.search(r'"([^"]+)"', rest) or re.search(r'\[([^\]]+)\]', rest)
    title = title_match.group(1).strip() if title_match else "Magazine Article"

    # Year
    year_match = re.search(r'(\d{4})', rest)
    year = int(year_match.group(1)) if year_match else 2020

    # Venue in italics
    venue_match = re.search(r'\*([^*]+)\*', rest)
    venue = venue_match.group(1).strip() if venue_match else "Magazine"

    # Authors before the title/bracket
    if title_match:
        authors_str = rest[:title_match.start()].rstrip(", ").rstrip()
    else:
        authors_str = ""
    authors_str = authors_str.replace(" & ", ", ").replace("&", ",")
    authors = [a.strip().rstrip(",").strip() for a in authors_str.split(",") if a.strip() and len(a.strip()) > 1]

    return {
        "cv_number": cv_number,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "type": "magazine",
    }

def parse_book_line(line):
    """Parse a book/chapter line."""
    m = re.match(r"(\d+)\.\s+", line)
    if not m:
        return None
    cv_number = int(m.group(1))
    rest = line[m.end():].replace("**", "")

    # Title in quotes or first significant text
    title_match = re.search(r'"([^"]+)"', rest)
    if title_match:
        title = title_match.group(1).strip()
    else:
        # Get text before publisher italic
        italic_match = re.search(r'\*([^*]+)\*', rest)
        if italic_match:
            title = rest[:italic_match.start()].strip()
            # Remove author prefix
            comma_parts = title.split(",")
            if len(comma_parts) > 2:
                title = ",".join(comma_parts[2:]).strip().lstrip('"').rstrip('"')
        else:
            title = rest[:80]

    # Year
    year_match = re.search(r'(\d{4})', rest)
    year = int(year_match.group(1)) if year_match else 2025

    # Venue/Publisher
    venue_match = re.search(r'\*([^*]+Publishers[^*]*)\*', rest)
    venue = venue_match.group(1).strip() if venue_match else "Book"

    # Authors
    authors_str = rest.split(",")[0:3]
    authors = [a.strip().rstrip(",").strip().replace("*", "") for a in authors_str if a.strip()]

    return {
        "cv_number": cv_number,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "type": "book",
    }

def write_publication_file(pub, type_prefix=""):
    """Write a single publication markdown file."""
    slug = slugify(f"{pub['year']}-{pub['title'][:60]}")
    if type_prefix:
        slug = f"{type_prefix}-{slug}"

    filename = os.path.join(OUTPUT_DIR, f"{slug}.md")

    # Clean and escape for YAML
    safe_title = clean_text(pub["title"]).replace('"', '\\"').rstrip(",").strip()
    clean_authors = [clean_text(a).rstrip(",").rstrip(".").strip() for a in pub["authors"]]
    clean_authors = [a for a in clean_authors if a and len(a) > 1]
    clean_venue = clean_text(pub.get("venue", "")).replace('"', '\\"')

    featured = is_featured(safe_title)
    themes = guess_themes(safe_title, clean_venue)

    authors_yaml = "\n".join(f'  - "{a}"' for a in clean_authors)
    themes_yaml = "\n".join(f'  - "{t}"' for t in themes) if themes else ""

    content = f'''---
title: "{safe_title}"
authors:
{authors_yaml}
year: {pub["year"]}
venue: "{clean_venue}"
type: "{pub["type"]}"
cv_number: {pub["cv_number"]}
featured: {str(featured).lower()}
doi: ""
pdf: ""
code: ""
data: ""
{f"themes:{chr(10)}{themes_yaml}" if themes_yaml else "themes: []"}
tags: []
---
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename

def main():
    cv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CV (Full) of Li-Ta Hsu.md")

    with open(cv_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Parse journal papers (lines 287-468 approx, 0-indexed: 286-467)
    current_year = 2025
    journal_count = 0
    patent_count = 0
    magazine_count = 0
    book_count = 0

    # Find section boundaries
    journal_start = None
    patent_start = None
    magazine_start = None
    book_start = None
    opensource_start = None

    for i, line in enumerate(lines):
        if "2.3.1 Journal Papers" in line and "###" in line:
            journal_start = i
        elif "2.3.2 Patents" in line and "###" in line:
            patent_start = i
        elif "2.3.3 Industrial Orientated" in line and "###" in line:
            magazine_start = i
        elif "2.3.4 Book and Book Chapters" in line and "###" in line:
            book_start = i
        elif "2.3.3 Open-Source" in line and "###" in line:
            opensource_start = i

    print(f"Journal section: line {journal_start}")
    print(f"Patent section: line {patent_start}")
    print(f"Magazine section: line {magazine_start}")
    print(f"Book section: line {book_start}")

    # Parse journal papers
    for i in range(journal_start + 1, patent_start):
        line = lines[i].strip()
        if not line:
            continue

        # Year header
        year_header = re.match(r"\*\*(\d{4}).*\*\*", line)
        if year_header:
            current_year = int(year_header.group(1))
            continue

        if re.match(r"\*\*Before \d{4}", line):
            current_year = 2014
            continue

        # Publication entry
        if re.match(r"\d+\.", line):
            pub = parse_journal_line(line, current_year)
            if pub:
                write_publication_file(pub)
                journal_count += 1

    print(f"Journal papers: {journal_count}")

    # Parse patents
    for i in range(patent_start + 1, magazine_start):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            continue
        if re.match(r"\d+\.", line):
            pub = parse_patent_line(line)
            if pub:
                write_publication_file(pub, "patent")
                patent_count += 1

    print(f"Patents: {patent_count}")

    # Parse magazine articles
    for i in range(magazine_start + 1, book_start):
        line = lines[i].strip()
        if not line or line.startswith("#") or line.startswith("!") or line.startswith("Figure"):
            continue
        if re.match(r"\d+\.", line):
            pub = parse_magazine_line(line)
            if pub:
                write_publication_file(pub, "magazine")
                magazine_count += 1

    print(f"Magazine articles: {magazine_count}")

    # Parse books
    for i in range(book_start + 1, opensource_start):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            continue
        if re.match(r"\d+\.", line):
            pub = parse_book_line(line)
            if pub:
                write_publication_file(pub, "book")
                book_count += 1

    print(f"Book chapters: {book_count}")
    print(f"\nTotal: {journal_count + patent_count + magazine_count + book_count} publication files created")

if __name__ == "__main__":
    main()
