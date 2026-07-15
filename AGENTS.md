# Codex project guide — IPNL lab website

This file is auto-loaded by Codex when working in this repo. Keep it a thin
adapter, not a second copy of the rules.

## Canonical instructions

Read and follow [`CLAUDE.md`](CLAUDE.md) — the canonical agent guide for this repo:

- the repo is **PUBLIC**: nothing confidential, ever;
- trilingual discipline (EN / zh-cn / zh-tw — fix all three, verify the built `public/`);
- deploys from `main` only (Hugo 0.157.0 pinned); a branch is not live until merged;
- git architecture: `.git` is a gitfile pointer to a database outside the synced
  tree — leave it; committing sessions use their own `git worktree`;
- branch policy: routine fixes commit to `main`; branch only for
  preview-before-publish / cross-session / risky-bulk work, then merge-or-close
  and delete it;
- staging discipline: `git reset` → add named paths → verify → commit.

If this file and `CLAUDE.md` conflict, follow `CLAUDE.md` unless the user says
otherwise in the current conversation.
