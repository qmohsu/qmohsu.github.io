# Publication Frontmatter Schema

This schema is the public website contract for `content/publications/*.md`.
Keep all public-facing claims evidence-backed; do not add result/method claims from memory.

## Required Bibliographic Fields

```yaml
title: "Paper title"
slug: "year-short-slug"
authors:
  - "Surname Initials"
year: 2026
venue: "Journal or conference"
type: "journal" # journal | conference | patent | magazine | book
cv_number: 1
featured: false
quartile: "Q1"
doi: "10.xxxx/example"
pdf: ""
code: ""
data: ""
themes:
  - "urban-gnss-reliability"
tags: []
```

## Rich Paper Page Fields

Use these optional fields for flagship or media-rich publications.

```yaml
summary: "One evidence-backed sentence suitable for card/index display."
abstract: "Optional abstract or plain-language abstract."
highlights:
  - "Evidence-backed key method/result."
  - "Evidence-backed impact or artifact."
hero_image: "/images/pubs/example.png"
hero_alt: "Specific alt text for the hero image"
hero_caption: "Short caption explaining what the image shows."
figures:
  - src: "/images/pubs/example-result.png"
    alt: "Result figure alt text"
    context: "One short manuscript-backed sentence connecting this figure to the paper story."
    caption: "Caption for the figure."
video: "https://www.youtube.com/watch?v=..."
videos:
  - "https://www.youtube.com/watch?v=..."
repo: "https://github.com/org/repo"
github: "https://github.com/org/repo"
slides: "https://..."
project: "project-slug"
projects:
  - "project-slug"
resources:
  - "resource-slug"
links:
  - label: "External page"
    url: "https://..."
    type: "press"
```

## Rules

- Use `project` for the primary related project and `projects` only when there are multiple direct project links.
- Use `resources` for website resource slugs under `content/resources/`.
- Use `hero_image` only for a figure cropped from the paper PDF or an official paper/supplement source. Do not use newly generated diagrams, redrawn schematics, or generic project images unless the user explicitly approves them.
- Use `figures` for additional method/result figures cropped from the paper PDF or official paper/supplement source.
- Use `figures[].context` for one concise sentence that explains how the figure connects to the preceding method/result story. Derive it from the manuscript and figure sequence; do not repeat the caption or invent claims.
- Use `video` for one recording and `videos` for multiple recordings. Do not set both unless the first video is intentionally duplicated.
- Use `repo` or `github` for the canonical software repository. Existing `code` remains supported.
- For Chinese translation stubs, keep metadata parity for links/media even if the body remains a stub.
- Do not add `summary`, `highlights`, or captions unless the wording is traceable to the paper, an existing website page, or user-provided source.
