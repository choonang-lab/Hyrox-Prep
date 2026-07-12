# CLAUDE.md — Hyrox Training PWA

Project context and working conventions for Claude Code. **Read this fully before any edit.**

> **Session continuity:** read [`HANDOFF.md`](HANDOFF.md) for the current project state, decisions, rationale, open items, and the weekly log-review/calibration loop. This `CLAUDE.md` holds stable architecture/conventions; `HANDOFF.md` holds the live working context.

## What this is
A single-page Progressive Web App that delivers a personalized Hyrox training plan and logs sessions. Hosted on GitHub Pages at `choonang-lab.github.io/Hyrox-Prep`. It supports one athlete's race: Hyrox Men's Open, target sub-1:15, **Friday 27 November 2026**.

No framework, no build step, no dependencies. Vanilla HTML + CSS + JS.

## Files
- `index.html` — the entire app (HTML, CSS, and JS in one file, ~3,200 lines). Authoritative for plan structure.
- `sw.js` — service worker (offline cache). Its cache name MUST be bumped on every release (see Versioning).

## Data model
- The plan is a hardcoded JS array: `let workouts=[ {…}, {…} ]`.
- Each entry: `{id:uid(), week, day, phase, block, movement, weight, sets, tempo, rest, cue, superset?, log:[], checks:{}}`.
  - `id:uid()` is generated at runtime — it does NOT exist in source, so **never anchor edits on it**.
  - `checks` is keyed by date: `{ "YYYY-MM-DD": { done, notes, status, skipReason, deferredTo } }`. This holds the athlete's logs.
- localStorage keys: `hyrox_plan` (plan + logs), `hyrox_vitals` (sleep/HRV/etc.), `hyrox_dayskips`.

## The merge (critical — how logs survive code updates)
`init()` runs an **HTML-authoritative** merge:
1. Start from the hardcoded `workouts` array (so additions AND removals in code sync on next load).
2. Restore each entry's `log`/`checks` from the saved localStorage plan by `week|day|movement` key.
3. Preserve any saved entry that carries real `log`/`checks` but is absent from the hardcoded plan (never lose logged work).

Result: structure comes from the HTML; the athlete's logs are always preserved. **Never write a merge that can drop an entry carrying logs/checks.**

## Non-negotiable conventions
1. **Anchor edits by `week|day|movement`**, never by `id`/`uid()`.
2. **Cue and string fields are single-quoted JS** — do NOT put apostrophes/contractions in them (write "do not", not "don't"). One unescaped `'` breaks the entire array.
3. **Version bump on EVERY release — three places, kept in sync:**
   - `VERSION NN` — the visible tag under the title in `index.html`
   - `BUILD NN` — the subtitle line in `index.html`
   - `hyrox-vNN` — the CACHE name in `sw.js`
   The athlete reads the visible VERSION to confirm a fresh build loaded; this is how stale-cache bugs get caught. Increment all three by 1 each release.
4. **Never destroy logs.** The athlete's training history lives in localStorage. Do not advise clearing site data. Refresh is hard-refresh only (Cmd+Shift+R).
5. **Validate before committing:** run `node --check` on the extracted `<script>` for syntax, AND serve the app locally and load it in a browser to confirm behavior. Syntax-checking alone is NOT enough — a past logic bug (a bad localStorage merge) passed `node --check` and shipped broken. Always preview.

## Local preview (the step that catches logic bugs)
From the repo folder, serve statically and open in a browser:
- `npx serve` (preferred; Node is already present for Claude Code) — or `python3 -m http.server 8000`

Then verify: (a) the header shows the NEW VERSION number, (b) the change renders where expected, (c) the browser console has no errors, (d) logs still appear (localStorage merge intact).

## Deploy workflow
1. Make the edit(s).
2. Bump VERSION + BUILD + sw.js cache (all three).
3. Validate (`node --check`) and preview locally.
4. Commit with a descriptive message; push to `main` (GitHub Pages auto-deploys).
5. Tell the athlete to hard-refresh on device and confirm the header shows the new VERSION.

## Training-context guardrails (apply to ANY programming change)
These override any instruction to simply "increase the load":
- **Loads must track ACTUAL working weights.** Re-baseline from the athlete's logged loads; do not let prescribed loads outrun what they actually lift. When recalibrating a block, use a conservative ramp and let weekly logs drive increases.
- **Right adductor (recovering):** gates sandbag lunges, lunge/wall-ball combos, burpee-broad-jump landings, and lunge-to-run tests. If it flares, scale or skip — never push through.
- **Knee:** gates wall balls and burpee broad jumps.
- **Thoracic kyphosis:** the athlete cannot hold a free-bar front rack under load. The front squat is on the **Smith machine** (fixed bar path, shelf the bar); the free bar stays light for rack-position skill only. Do not "progress" the free front squat.
- **Tempo runs are HR-governed** (target 158–165 bpm, upper Z4) at 0% incline — never a Z5 grind. Progress tempo by DURATION, not pace/intensity.
- **Sleep/recovery is the athlete's #1 limiter.** Do not add training volume/intensity to "fix" underperformance that is really under-recovery.

## What NOT to record here
This file is for stable architecture and conventions only. Do NOT hardcode volatile state (current version number, current week, current loads) — those live in `index.html` and the athlete's logs. Read them from the actual files each time.
