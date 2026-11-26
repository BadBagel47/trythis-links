# trythis-links – working instructions

> **Global agent rules:** https://raw.githubusercontent.com/BadBagel47/agent-rules/main/AGENTS.md (fallback: the file `AGENTS.md` in the repo `BadBagel47/agent-rules` via GitHub). Read them at the start of every session; they apply before the project rules below. This is a web project, so `WEB.md` in the same repo applies too.
> **Handoff:** `docs/HANDOFF.md` · **Backlog:** `docs/BACKLOG.md` · **Decisions:** the "Decisions" section in `docs/HANDOFF.md`

## What the project is
A structured link page: hand-picked channels and sites in groups. During development it is published on GitHub Pages (https://badbagel47.github.io/trythis-links/); a subdomain of `trythis.one` is parked (F-002). The main site `trythis.one` lives in the separate repo `BadBagel47/trythis.one`; this repo only holds the link page.

## Structure
- `index.html`: the whole page (HTML, CSS and JS in one file, no build step, no dependencies)
- `links.json`: all groups and links; the page renders from it. Add links here.
- `assets/fonts/`: Inter, bundled locally with its OFL licence
- `assets/images/`: card pictures. After adding links, run `python3 tools/fetch-images.py` (needs Pillow) to fetch them.
- `tools/`: development tools, never published
- `.github/workflows/pages.yml`: publishes only the site files (`index.html`, `links.json`, `assets/`) to GitHub Pages on every push to `main`
- `.assetsignore`: files Cloudflare must not publish (for later, F-002). Anything new that is not part of the site goes in it in the same commit.

## Project rules
_None approved yet._ Proposed rules are listed in `docs/HANDOFF.md` until the owner approves them.
