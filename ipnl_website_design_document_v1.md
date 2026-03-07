# Intelligent Positioning and Navigation Laboratory (IPNL)
## Website design document for a future-proof GitHub Pages site and AI-assisted maintenance workflow

Prepared as a first-draft strategy document on 7 March 2026.

## Executive recommendation

Build the new IPNL site as a static website on GitHub Pages with a custom domain, but use GitHub Actions for deployment and automation rather than relying on the default branch-only setup. For the site generator, use **Hugo** if the priority is long-term content modeling and AI-assisted updates; use **Jekyll** only if the priority is to fork an academic template immediately and start migrating content with minimal rework. In both cases, design the site around **structured content files**, not hand-edited HTML pages.

## 1. Purpose and target state

The website should stop being a passive archive and become a durable laboratory operating surface:
- a public face for research credibility,
- a recruiting tool,
- a catalog of datasets and software,
- a home for flagship projects,
- and a repository that AI agents can safely update under human supervision.

### Goals
- Professional public identity for IPNL with a stable GitHub Pages + custom-domain setup.
- Clear research story that is understandable in under one minute.
- First-class visibility for people, publications, projects, datasets, software, awards, and openings.
- A structured content model that lets future AI agents propose updates through pull requests instead of editing pages directly.
- Low-maintenance publishing workflow with predictable files, automation hooks, validation checks, and reproducible deployment.

## 2. Audit of the current public site

The current site already contains valuable material. The redesign should preserve that substance but change how it is organized, surfaced, and maintained.

| Area | Current-state observation | Design implication |
|---|---|---|
| Established scholarly record | The site already includes extensive publications, project material, an open resource page, news/activity items, and recruitment content. | Keep these assets, but convert them into structured content types rather than long manually maintained pages. |
| Homepage emphasis | The home page leads with welcome and recruitment text, then event-style highlights. | Shift the home page toward research identity, people, flagship outputs, and recent news with short summaries. |
| People visibility | There is no strong first-class people section in the current navigation, and team identity is understated. | Add a dedicated People page with current members, alumni, roles, short bios, and links. |
| Project presentation | Projects are represented mainly as long text pages and are hard to skim. | Use project cards with thumbnail, one-sentence summary, tags, funding note, and links to paper/code/data. |
| Resource strategy | Open resources exist but are not treated as a major differentiator across the whole site. | Promote datasets, open-source repositories, and testbeds as a core part of IPNL’s public identity. |
| Maintenance pattern | The site looks manually updated and time-stamped rather than pipeline-driven. | Move to a repository where publications, news, people, and projects are separate machine-readable entries. |

## 3. What leading research groups do well

Across strong research groups in AI, robotics, vision, language, and positioning/navigation, the pattern is consistent: the best sites are not just paper lists.

| Pattern | Observed on strong sites | Implication for IPNL |
|---|---|---|
| People are easy to find | Current members and alumni are usually visible from the top navigation, often with photos and roles. | Make People a top-level page. |
| Research is grouped into themes | Groups use 4–8 enduring themes rather than presenting every project equally on the homepage. | Create a stable taxonomy for IPNL research areas. |
| Outputs beyond papers are first-class | Top groups give software, data, demos, and seminars their own visibility. | Treat datasets, code, field tools, and benchmark resources as strategic assets. |
| Homepage is selective | Homepages feature only a few flagship projects, recent news items, and selected publications. | Do not place exhaustive lists on the front page. |
| Joining information is explicit | Students and collaborators can quickly find openings, expectations, and contact channels. | Create a concise Join Us page. |
| Updates are lightweight | Recent items appear as short cards or feed entries rather than long newsletter-style essays. | Use short news entries with optional deep-dive pages only for major milestones. |

## 4. Recommended information architecture

The top navigation should be stable for years.

| Page | Primary purpose | Must-have content |
|---|---|---|
| Home | Research identity and fast orientation | Hero statement, mission, 4–6 research themes, 3 flagship projects, latest news, selected publications, group photo, Join Us teaser |
| Research | Explain what the lab works on | Theme pages, methods, application areas, testbeds, related projects/resources |
| Projects | Show major ongoing and completed efforts | Project cards, funding note, collaborators, dates, related papers, code, datasets, demos |
| Publications | Complete scholarly record | Filter by year/type/theme; DOI/paper/slides/code/data links; featured shelf |
| People | Human identity of the lab | PI, current members, visiting members, staff, alumni, bios, photos, links |
| Resources | Expose reusable assets | Datasets, software, benchmark results, tutorials, documentation |
| News | Signal activity and momentum | Short updates for awards, papers, workshops, talks, grants, releases, media |
| Join Us | Recruiting and collaboration | Openings, priorities, expectations, FAQ |
| Contact | Institutional trust and findability | Address, map, email, affiliation, logo usage, social links |

## 5. Homepage blueprint

1. Hero block — laboratory name, one-line mission, 2–3 action buttons, and either a group photo or research visual montage.
2. Research themes grid — 4 to 6 tiles.
3. Flagship projects — 3 cards only.
4. People strip — PI plus current members preview.
5. Latest news — 4 to 6 short items.
6. Selected publications — 3 to 5 highlighted items.
7. Open resources — datasets, benchmark tools, repositories, tutorials.
8. Join Us teaser.
9. Footer — affiliation, contact, address, social/repository links.

**Rule:** The front page should answer four questions immediately:
- What does this lab work on?
- Why is it distinctive?
- Who is here?
- What should I click next?

## 6. Page-level design guidance

### Research
Use stable theme pages, not temporary project dump pages.

### Publications
Entries should support paper PDF, DOI, code, data, slides, video, and project page when available.

### People
Use headshots, role labels, concise bios, research interests, and professional links. Separate current members and alumni.

### Resources
Split into logical subtypes: datasets, software, benchmarks, tutorials, and media/test data.

### News
Use short structured entries. Major milestones can link to a longer post.

### Join Us
Explain who the lab is looking for, the skills valued, how applicants should contact the lab, and how prospective students can prepare.

## 7. Recommended visual system

- Restrained academic palette with one primary accent color.
- Clean typography, strong spacing, and card layouts over decoration.
- Real lab imagery: field tests, platforms, maps, plots, data collection, software screenshots.
- Short paragraphs and skimmable pages.
- Consistent thumbnail ratios and image treatments.
- Mobile-first design.
- Accessibility by default.

## 8. Technical architecture recommendation

| Option | Why choose it | Risk / constraint | Verdict |
|---|---|---|---|
| GitHub Pages + GitHub Actions + Hugo | Best for structured content and automation; supports rich front matter, taxonomies, sections, menus, and archetypes | Requires initial setup and theme selection | **Recommended** |
| GitHub Pages + Jekyll | Best if you want to fork an academic template and migrate quickly; supports front matter, collections, and data files | Native GitHub Pages builds restrict plugins; more complex workflows usually push you toward Actions anyway | Strong fallback |
| Direct static HTML | Maximum control for a designer | Poor fit for AI-assisted updating and long-term maintainability | Not advised |

## 9. Content model for AI-safe updates

The rule is simple: agents should update **data entries**, not **free-form page layouts**.

| Content type | Key fields | Expected update source |
|---|---|---|
| people | name, role, status, photo, bio, interests, links, years, sort order | Manual or self-service PR |
| publications | title, authors, year, venue, type, abstract, DOI, PDF, code, data, project, tags | Automated ingest plus manual curation |
| projects | title, summary, theme, status, dates, funding, collaborators, image, links, outputs | Manual |
| resources | title, subtype, summary, license, maintainers, citation, repo/link, version, status | Manual plus repository metadata |
| news | title, date, category, summary, related people/project, cover image, link | Mostly manual or AI-drafted |
| research themes | title, summary, keywords, hero image, related assets | Manual and stable |

### Example repository layout

```text
ipnl-website/
├── content/
│   ├── people/
│   ├── publications/
│   ├── projects/
│   ├── resources/
│   ├── news/
│   ├── research/
│   ├── join/
│   └── contact/
├── data/
│   ├── navigation.yaml
│   ├── settings.yaml
│   └── redirects.yaml
├── static/
│   ├── images/
│   ├── files/
│   └── social/
├── layouts/ or themes/
├── scripts/
│   ├── sync_publications.py
│   ├── validate_content.py
│   └── generate_previews.py
└── .github/workflows/
    ├── preview.yml
    ├── validate.yml
    ├── deploy.yml
    └── sync-publications.yml
```

## 10. AI-agent workflow and governance

Do not give agents direct production-editing power. Give them **proposal power**.

- All automated changes should happen through pull requests.
- Protect the default branch with required review, required status checks, and CODEOWNERS for high-risk paths.
- Use separate Actions for validation, preview build, and deploy.
- Grant minimum necessary token permissions.
- Prefer a GitHub App over a personal access token for long-lived automation.
- Treat site content as public.
- Keep explicit schemas and validation scripts.

## 11. Automation roadmap

| Phase | Scope | Outcome |
|---|---|---|
| Phase 1 — foundation | Choose generator, design system, templates, and migrate minimal content | Deployable MVP |
| Phase 2 — content enrichment | Add structured people, publications, projects, resources, news, search, SEO | Professional research website |
| Phase 3 — controlled automation | Add publication sync, schema validation, previews, issue/PR templates | Reliable AI-assisted maintenance |
| Phase 4 — advanced automation | Add highlighting, draft news generation, stale-content detection | Continuous improvement without chaos |

## 12. What IPNL should prepare now

| Asset / decision | Why it matters |
|---|---|
| Group photo and headshots | Immediately improves credibility and quality |
| Current members and alumni list | Needed for a serious People page |
| 4–6 research themes | Backbone of navigation and homepage |
| 3 flagship projects | Needed for homepage and project cards |
| Resource inventory | Makes datasets and code visible |
| Publication source of truth | Prevents metadata drift |
| Join Us copy | Attracts the right applicants |
| Brand decisions | Keeps the site visually coherent |

## 13. Suggested initial research-theme labels for IPNL

- Urban positioning and GNSS resilience
- Multi-sensor integrated navigation
- Cooperative and collaborative positioning
- Autonomous systems and trustworthy navigation
- Intelligent transportation and location-aware systems
- Open datasets, benchmarks, and field validation

## 14. Notes on discoverability, accessibility, and trust

- Use a custom domain and enforce HTTPS.
- Generate sitemap and structured metadata.
- Add privacy-friendly analytics only if the lab will use them.
- Use lightweight static search.
- Keep the footer year current automatically.

## 15. Decision summary

**Recommended default decisions**
- Navigation: Home, Research, Projects, Publications, People, Resources, News, Join Us, Contact
- Stack: Hugo + GitHub Actions + GitHub Pages + custom domain
- Search: Pagefind
- Publication source of truth: ORCID/Crossref/DOI with manual curation
- Governance: pull-request-only automation with branch protection, CODEOWNERS, preview builds, and deployment protection

## Appendix A. Benchmark sites reviewed

- Stanford NLP Group
- Oxford VGG
- Princeton Vision & Learning Lab
- CMU AirLab
- MIT HAN Lab
- Stanford IPRL
- ETH Autonomous Systems Lab
- Stanford GPS Lab
- University of Calgary PLAN Group
- UT Austin Radionavigation Laboratory

## Appendix B. Platform and standards references reviewed

- GitHub Pages / GitHub Actions
- Jekyll documentation
- Hugo documentation
- Pagefind / Lunr
- Plausible / GoatCounter
- WCAG 2.2
- Google search / structured data guidance
- ORCID / Crossref / DOI metadata documentation

This document is intentionally opinionated. The point is not to preserve the current site structure more elegantly; it is to build a lab website that can remain credible and maintainable for years while still being safe to automate.
