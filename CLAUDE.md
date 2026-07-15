# Claude Code project guide — IPNL lab website (qmohsu.github.io)

Auto-loaded by Claude Code when working in this repo. Canonical agent guide for the
site; `AGENTS.md` is the thin adapter for other agents (Codex etc.).

> **This repo is PUBLIC.** Everything committed here is world-readable. No partner
> KPIs, device models, unit counts, internal names, or private paths — ever.

## What this is

The IPNL lab website: a trilingual (**EN / zh-cn / zh-tw**) Hugo site.
`baseURL = https://ipnl.io/` (Cloudflare Pages, branded domain) with a mirror on
GitHub Pages. **Both deploy from `main` only** via `.github/workflows/`
(`cloudflare-pages.yml` + `deploy.yml`), source-only (`public/` is gitignored).

- **Hugo is pinned to 0.157.0** in both workflows. Newer local Hugo versions can
  differ on slug/alias behaviour — verify against 0.157 semantics before blaming content.
- **A branch or PR is NOT live** until merged to `main`. Preview work on the local
  server (`http://127.0.0.1:8100`), never on the production URL.
- Merging to `main` = publishing to the world → get the owner's OK first.

## Git architecture (do not "fix")

- `.git` here is a **gitfile pointer**; the real git database lives OUTSIDE the
  Dropbox-synced tree (per-machine, e.g. `~/GitData/qmohsu.github.io.git`). This is
  deliberate — a git DB inside a file-sync product corrupts. Leave the pointer alone.
- **Agent sessions that commit should work in their own `git worktree`**, not this
  main checkout — parallel sessions sharing one checkout collide on index/HEAD.
  Put worktrees outside any synced folder (e.g. `~/GitData/wt/<task>`).
- Start every session with: `git branch --show-current`, `git fetch`,
  `git status` — confirm branch and ahead/behind before editing anything.

## Site map — where things live

| Change… | File |
|---|---|
| Colours, fonts, all styling | `assets/css/main.css` (`:root` tokens; light-header overrides appended at EOF) |
| Header: logos, nav, language switch | `layouts/partials/header.html` |
| `<head>`: CSS, favicons, per-language CJK font links | `layouts/partials/head.html` |
| Home hero, hero SVG, stat cards, case tabs | `layouts/index.html` |
| Citation charts (colours hardcoded in inline JS) | `layouts/partials/scripts.html` |
| Publications filters + flagship cards | `layouts/publications/list.html` + `content/publications/*.md` |
| PNT pipeline SVG (hardcoded colours) | `layouts/shortcodes/pnt-stack.html` |
| Projects + partner cards | `content/projects/_index.md` **+ `.zh-cn.md` + `.zh-tw.md`** |
| Logos | `static/images/logos/` · partners → `static/images/partners/` |

Brand tokens: ultramarine `#2D3B97` (+ bright `#3A4DB8`) and vermilion `#D3313A`;
ivory ground `#FAF7F1`, ink text `#1A1F3A`, navy `#161B40`. Fonts: Fraunces
(headings) + Mulish (body) + Noto Serif/Sans CJK per-language. On dark heroes use
light variants (`#6E7AD0` / `#9FB0F0`) and keep highlight contrast ≥ 4.5:1 —
verify on the RENDERED page, not the CSS.

## The rules that bite

1. **Fix all three languages.** The same fact lives in EN + zh-cn + zh-tw, often in
   duplicate spots. After editing: clean-rebuild and **grep the built `public/`**
   in all three languages for the old and new values.
2. **Values are not only in `main.css`** — also inline JS charts, the PNT SVG, the
   hero SVG. Grep all of `layouts/` + `assets/` for every old hex/rgba form
   (spaced and minified).
3. **Clean rebuild before verifying, and stop the `:8100` server first** — a running
   server holds Windows file locks, `rm -rf public` half-fails, and you verify a
   stale or broken build. Kill server → `rm -rf public resources/_gen` →
   `hugo --minify --gc` → restart → grep.
4. **Images cache-bust by RENAME** (URLs aren't fingerprinted). Rename + update refs.
5. **Partner copy stays general** pending partner clearance (no device models,
   counts, deployment claims, partner-issued figures).
6. **Per-language parity**: a page without `.zh-cn.md`/`.zh-tw.md` 404s in Chinese.
   Diff built `en/` vs `zh-*/` page lists after a clean build.
7. **A Chinese title ≠ a translated page** — `grep -rl 'translation-stub' content/`
   is the truth. Never romanize names into invented Chinese; only Li-Ta Hsu → 許立達/许立达.
8. **Templates**: localize with `site.Language.Lang` conditionals, never `.Lang`
   inside `range`/`with` (breaks the build).

## Build → verify

```bash
hugo --minify --gc                                   # build (watch for error/panic)
( cd public && python -m http.server 8100 ) &        # serve
# screenshot /en/ /zh-cn/ /zh-tw/, then:
grep -roiF '<old-value>' public | wc -l              # expect 0 after a clean rebuild
```

## Git discipline

```bash
git reset                                  # unstage first — parallel sessions pre-stage
git add <only your named paths>            # never -A / .
git diff --cached --name-only              # confirm ONLY your files, no _shots/
git commit -m "<type>(scope): subject"     # no attribution trailers
git log origin/main..HEAD                  # review the to-push set
```

Never commit `_shots/` (screenshot scratch) or `public/`. Deeper recipes (logo/PIL
transforms, translation batching, broken-link audit) live in the owner's private
companion knowledge repo — ask Li-Ta. Person profiles have their own flow there too.
