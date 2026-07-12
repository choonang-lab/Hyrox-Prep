# HANDOFF.md — Session Continuity & Project State

**Purpose:** This file carries the full working context for the Hyrox-Prep project so any new Claude Code session (e.g. moving from Windows to the Mac desktop app) can pick up exactly where we left off. Read this together with `CLAUDE.md` (architecture + non-negotiable conventions). Treat this file as the source of truth for *session state, decisions, and rationale*; treat the code as the source of truth for *current numbers*. **Verify volatile details (version, loads) against the actual code — this doc can lag.**

> New machine setup: `git clone https://github.com/choonang-lab/Hyrox-Prep.git`, open in Claude Code, and (optionally) tell it "read HANDOFF.md and save the key facts to memory" so continuity persists across sessions on that machine. Re-connect the **Google Drive** connector (claude.ai connectors / `/mcp`) to resume the log-review loop.

---

## 1. Snapshot (as of 2026-07-05)
- **App:** live at **VERSION 95** (`choonang-lab.github.io/Hyrox-Prep`). Single-file vanilla PWA.
- **Block 2 (W13–W20)** is **built, calibrated from real W12 logs, reviewed, and shipped.** W13 starts **Mon 6 Jul 2026**.
- **Blocks 3 & 4** — planning **deferred** pending the athlete's Sep–Nov travel schedule (direction agreed; see §6).
- **Next athlete action:** on W13 Monday, **establish the Smith front-squat top set** (the one open number; W14+ progresses off it).
- **Continuity loop:** athlete logs sessions on device → app exports a backup JSON to Google Drive → we review + calibrate the next week. (See §7.)

## 2. Athlete profile & target
- ~72 kg male, **Hyrox Men's Open, AG 50–54**, racing **Fri 27 Nov 2026**.
- **Target (reframed Jul 2026):** **1:25 stretch, ~1:30–1:35 probable.** Original sub-1:15 assessed unrealistic this cycle (would need ~31 min off a 1:46:34); kept only as a labeled aspiration.
- **Recovery is his #1 limiter** (masters athlete) — do NOT add volume/intensity to "fix" what is really under-recovery.

## 3. Race analysis & weaknesses
- 2 races (HYROX Singapore, AG 50–54): 2025 **1:45:55**, 2026 **1:46:34**.
- **Running is his STRENGTH** (top ~28%). The 2026 regression was all in the run (a positive-split / fatigue *fade*, not a fitness loss). → maintain running, don't chase it.
- **Stations are the WEAKNESS** (bottom ~5–15%): biggest sinks **Wall Balls (~12:16), Sandbag Lunges (~10:00), Sled Pull (~7:27)** = ~57% of the gap to 1:25.
- **His real run limiter = durability / the compromised-run "fade,"** not raw 5K speed. Trained via the Wednesday compromised tests, not by longer easy runs.

## 4. Injury guardrails (also in CLAUDE.md — apply to ANY change)
- **Right adductor (recovering):** gates sandbag lunges, lunge/wall-ball combos, BBJ landings, lunge-to-run. Scale/skip if it flares.
- **Knee:** gates wall balls and burpee broad jumps.
- **Thoracic kyphosis:** cannot hold a free-bar front rack under load → front squat is **Smith-machine only**; free bar stays light for rack-skill. Do NOT progress the free front squat.
- **Tempo runs HR-governed** (158–165 bpm, upper Z4, 0% incline); progress by DURATION not pace.

## 5. Benchmarks (Benchmarks tab, recalibrated v84)
- Recalibrated to **1:25-primary + 1:15-stretch**, with explicit **FRESH vs RACE(compromised)** station targets.
- **5K target sub-22:30 (4:30/km)**, framed maintain-not-chase (his ~22:55 est is close; the gating benchmark is the **compromised km ~5:10–5:15**, i.e. durability).

## 6. Periodization
- **Block 1** ≤ W12 (W2 started Mon 20 Apr 2026). **Block 2** = W13–W20. **Block 3** from W21 (~31 Aug). **Block 4** to race day.
- **Blocks 3 & 4 = 13 weeks, W21–W33** (race is **Fri 27 Nov = Friday of W33**). **Planning DEFERRED** until travel is known.
- **Agreed direction to resume from (not yet built):**
  - **Block 3 = W21–28 "Race Specificity" (8 wk):** 3A accumulate race-specific work (deload W24) + 3B intensify. Convert Block-2 strength → race-pace endurance; couple stations to running; PACING + roxzone become the main event.
  - **Block 4 = W29–33 "Peak & Taper" (5 wk):** W29 full sim → W30 sharpen → **2-week taper** (W31–32) → W33 race week (opener + rest → race Fri).
  - **Strength → MAINTENANCE** in 3–4 (front squat/RDL ~every 10–14d; no more max-strength building this close).
  - **Simulations:** 1 full is the floor, **2 the sweet spot** (an early *diagnostic* ~W24–25 + a W29 *dress rehearsal*); **do NOT exceed 2** (recovery limiter). Lean on cheaper **half-sims** for the bulk.
  - **No Hyrox event within reach Sep–Oct** → sims must be self-run/split using his equipment (sled/row/ski only ~2 days/wk); likely "sim across a week" rather than one session.

## 7. The continuity / calibration loop (how we work each week)
1. Athlete trains and **logs sessions on device** (status + notes per exercise).
2. App exports a full-plan backup to **Google Drive**: filename `hyrox-backup-YYYY-MM-DD.json`, in his Drive root. Schema `{version, plan:[ {…entry…} ]}`.
3. We **download the latest backup**, extract that week's logs, and **calibrate the next week** to actuals (respecting the guardrails: loads track logged working weights; conservative ramps; let logs drive increases).
4. **Where the logs live:** each entry's **`checks`** map, keyed by date → `{done, notes, status, skipReason, deferredTo}`. **NOT** in `log:[]` (that array stays empty). The `notes` field is where the athlete records what he actually did / how it felt.
5. Backups are large (~700KB–1MB) → they exceed a single tool result; the download tool saves them to a file — decode the base64 `content`, parse JSON, and diff against the prior backup to find *new* logs.

## 8. Block 2 detail (W13–W20, current build)
Equipment constraint drives the week: he has **sled/row/ski only ~2 days** → machines clustered on **Mon + Wed**.
- **Mon = Hyrox Gym Day** (strength-first): Form Film → Smith Front Squat → RDLs → Sled Push → Sled Pull → **Row 2×1k → Ski 2×1k** (alternating, race distance, controlled race pace, progress by tightening rest). ~3h — long; open "trim Monday" ideas noted below.
- **Tue = Run + Skill:** Handstand (moved here), BBJ Form Skill + Form Film, **Wall Ball EMOM (W14–19, 6→10 min)** / Wall Balls 100-for-time (W13 & W20 only), **Tempo Run**, **Air Squats** (after tempo).
- **Wed = Pull + Core + BOTH compromised run tests** (Equipment Day 2).
- **Thu = Unilateral + Sandbag + adductor progressions** (Copenhagen Dynamic, Eccentric Adductor Slide, Loaded Lateral Lunge; Bulgarian, Step-Ups, Farmers, Thrusters). No machines.
- **Fri** intervals (Track 800m) + handstand · **Sat** rest · **Sun** long run.
- **SkiErg Technique Drill (home, 5 min) 4×/week** (Mon/Wed/Thu/Fri mornings).
- **Mesocycle:** 2A = W13–16 (accumulate, **W16 deload ~−45%**); 2B = W17–20 (intensify, **W20 = test week**).

**Key progressions (verify in code):**
- **Sled Push** 130→141→**152 (race by W15)**→[106 DL]→152→152(4×)→160(overload)→re-test.
- **Sled Pull** 87.5→95→**102 (race)**→[72 DL]→102→102(4×)→107(overload)→re-test.
- **RDL** 90→92.5→95→[DL]→95→97.5→100.
- **Smith Front Squat** AUTO-REGULATED: W13 = *calibrate* a clean 5-rep top (start ~50kg, LOG it); W14+ = "W13-top +2.5/+5/+7.5/+10kg". *He front-squatted free bar all of W12 and never set a Smith number — the top is genuinely unknown until W13.*
- **Wall Ball EMOM** W14–19: 6→8→[5 DL]→9→10→10 min. **Tempo** 25→35 min @5:00/km. **800m intervals** 4→6 reps, 3:24→3:18 (calibrated rebuild — he FAILED 6×800 in W12).
- **Long run FLAT 90 min** all weeks (deload/taper 60) — deliberate: maintenance, not chase (validated by his 07-04 long run: 90min/13k/143bpm).
- **Sandbag Lunges** distance builds 45→**100m (race)** at 25kg (weight chip = kg, sets chip = distance).
- **BBJ "Distance Build"** added W17–19 (15/20/25m), adductor+knee-gated — his only race-pace BBJ exposure (standard BBJ is knee-down form-skill only).

**W13 calibration from W12 logs (2026-07-05):** rows rolled back 60→57.5kg ("felt heavy, hold"); Y-raises 5→4kg; glute thrust 22.5→25, thrusters →8, lateral lunge →3 (bumped to achieved); RDL 90 + incline press 27.5 held; intervals 6×800 (failed) → 4×800. Wall-ball unbroken = 40; air squats = 43.

## 9. UI / theme state
- **Light Hyrox theme (v88+):** off-white `#F4F4F1` bg, white cards, `--accent` = black ink, **acid-yellow `#E4FF3A`** reserved for pops (+Add button, logo highlight, weight pill, active-tab underline, race-chip = black chip / yellow text). Icons = **uniform black squares** (phase colour lives on the card LEFT BORDER only). Log bar = black outline, yellow on hover; **"all done" state = black fill + yellow ✓** (v94).
- Theme lives in the **`:root` tokens (~line 14)** + a **"Light Hyrox accents" override block near `</style>`.** To reskin, edit those two spots.
- Interactions (v90): **tap an expanded card anywhere to close**; **long-press the open log to close** (mirrors the open gesture), with a **tap-shield (v91/v93)** that swallows the trailing touch + suppresses text-selection.
- Header (v86/v92): `⋯` overflow menu (Load/Save/Export/Reset) + live **race-day countdown chip**; `syncHeaderOffsets()` pins the week-nav bar to the header's real height (don't reintroduce hardcoded 50/65px offsets).

## 10. Deploy & versioning
- **Deploy = GitHub Actions Pages** (`.github/workflows/pages.yml`, `build_type=workflow`). Push to `main` auto-deploys.
- **Version bump on every app release, 3 places in sync:** `VERSION NN` + `BUILD NN` in `index.html`, `hyrox-vNN` in `sw.js`.
- **Never assume push = live.** Verify: `curl "…/index.html?cb=$RANDOM" | grep VERSION` and `gh run list`.
- **GitHub Pages soft limit ~10 builds/hour** — we tripped it this session (deploys failed "try again later," had to wait ~1hr). **Batch changes into fewer deploys.** If a deploy fails transiently, re-dispatch with `gh workflow run pages.yml`.
- **Validate before commit:** `node --check` on the extracted `<script>` AND preview in a browser (a past merge bug passed node --check but shipped broken).

## 11. Open items / next actions
- [ ] **W13 Monday:** establish + LOG the Smith front-squat top set (unlocks W14+ numbers).
- [ ] **Weekly loop:** after W13, athlete re-uploads logs → **calibrate W14** off real W13 numbers (esp. Smith top).
- [ ] **Merged backup JSON** (his logs + current v95 plan) so his history travels onto the device via `restore.html` — discussed, **not yet built**.
- [ ] **Blocks 3 & 4:** build once travel schedule is known (direction in §6).
- [ ] Optional: add his **143 bpm** as the Zone-2 marker on the long-run card.

## 12. Version history (context)
v84 Benchmarks recalibrate · v85 Block 2 W13–20 shipped · v86 contrast + phase colours + overflow menu + countdown · v87 dark theme (tried, disliked) · v88 **light Hyrox theme** · v89 remove per-day +Add + fix card-eject `</div>` bug · v90 tap/long-press toggles · v91 tap-shield · v92 header/pill overlap fix · v93 shield text-select fix · v94 log-bar black+yellow · **v95 program-review fixes (flat-90 long run, sandbag load/distance split, cautious BBJ build).**
