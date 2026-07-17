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

### 3a. FULL 2026 race splits (pulled 2026-07-14 from hyresult, reconciles exactly to 1:46:34)
Source: `hyresult.com/result/LR3MS4JI4B607D` · AG 50–54, **#24 in AG**, #782/1561 overall.
- **Runs (8):** 3:57 · 5:26 · 5:47 · 5:38 · 5:50 · 5:35 · 5:40 · 6:04 = **43:57**
- **Stations (8):** SkiErg 4:46 · Sled Push 4:51 · Sled Pull 7:26 · BBJ 5:20 · Row 5:31 · Farmers 2:41 · Sandbag 9:59 · Wall Balls 12:16 = **52:50**
- **Roxzone:** **9:47** (entries escalate: 0:03/0:11/0:24/0:39/0:35 → **Farmers 1:33, Sandbag 1:40**)
- 43:57 + 52:50 + 9:47 = 1:46:34 ✅

**Segment vs the 1:35 model:** run 43:57 (model ~44:30 → **already 1:35-ready, needs NOTHING**) · roxzone 9:47 (~8:00, −1:45) · stations 52:50 (~42:30, **−10:20**). The entire 11:34 gap to 1:35 is stations + roxzone.

**Improvement log — actual vs 1:35 target (ranked):** Wall Balls 12:16→8:00 (**−4:16**) · Sandbag 9:59→7:15 (**−2:44**) · Sled Pull 7:26→5:15 (**−2:11**) · Sled Push 4:51→3:45 (−1:06) · Row 5:31→5:05 (−0:26) · Farmers 2:41→2:15 (−0:26) · **SkiErg 4:46 and BBJ 5:20 are AT TARGET — no work needed.** Top 3 = 9:11 = ~86% of the station gap.

**2025 race baseline (pulled 2026-07-14, `hyresult.com/result/LR3MS4JI42AD24`, reconciles to 1:45:55; AG 50–54, #29):**
- Runs 41:13 · Stations 53:10 · Roxzone 11:32.
- Stations 2025: SkiErg 4:53 · Sled Push 4:16 · Sled Pull 6:48 · BBJ 5:59 · Row 5:23 · Farmers 2:28 · Sandbag 10:34 · Wall Balls 12:49.
- **Two-race read (2025→2026):** total 1:45:55→1:46:34 (+39s). Runs +2:44, stations −0:20 (flat), roxzone **−1:45 (improved)**.

**CRITICAL TIMELINE — do NOT read the two races as a year of training (corrected 2026-07-17):** race 1 = **last week Nov 2025**, race 2 = **last week Apr 2026** → only **5 months apart**, and he took a **1.5-month break** between them = **~3.5 months of actual training**. (Corroborated: hyresult labels BOTH races **season 8** — `s8-2025-singapore-expo` + `s8-2026-singapore`.) Any "his times did not move in a year / stagnation" reading is WRONG.
**Environment-adjusted he clearly IMPROVED:** strip the heat off the runs (−2:44) and the poor floor off the sleds (−1:13) → **~1:42:37 vs 1:45:55 = ~3:18 better in ~3.5 months.** And his **non-sled stations moved −1:33** (sandbag −0:35, WB −0:33, BBJ −0:39, SkiErg −0:07; Row +0:08, Farmers +0:13) — WITHOUT any of the coupling/durability work now designed. **The stations DO respond**; the re-orientation is aiming a better stimulus at something already inching, not at an immovable object.

**IMPORTANT — environment-confounded, do NOT read as regression (athlete confirmed):**
- The **2026 run being +2:44 slower is ENVIRONMENTAL** (warmer venue + heat), not fitness loss. His TRUE run ceiling is 2025's **41:13 — already inside the 1:35 model (~44:30). Running is emphatically not the problem.**
- The **2026 sleds being slower (push +0:35, pull +0:38) is FLOORING** (2026 poor surface; sled times are floor-dependent) — a surface artifact, not a strength regression.
- The first Hyrox run is a **short km in both races** (corral start) → the ~4:00 opener is a distance artifact, NOT a hot start. No pacing-error problem; post-opener runs were stable (~5:05 in 2025).

**What SURVIVES the two-race comparison (env-independent, genuinely actionable):**
- **Roxzone late-station ENTRIES are a 2-year behavioural leak** — Farmers-In 1:38 (2025) / 1:33 (2026) and Sandbag-In 1:48 (2025) / 1:40 (2026); every other transition 0:03–0:55. Transitions are unaffected by heat/floor → this is real. ~3:15 of walk-in on two stations, both years. (He HAS improved overall roxzone 11:32→9:47, mostly on exits — the two entries are the stubborn remainder.) → drives the §3d roxzone rehearsal (attack farmers + sandbag entries).
- **Worst-3 stations identical both years:** Wall Balls, Sandbag, Sled Pull. Priority ranking confirmed across two independent races.

### 3b. THE KEY INSIGHT — it is a DURABILITY problem, not a capacity problem
- His **fresh** 100 wall balls = **6:01** (W13). A **1:15 reference athlete** (Yew Meng Tan, AG 40–44, 1:15:25, same race — `hyresult.com/result/LR3MS4JI4B63A0`) did **6:34 in-race**. **His fresh wall balls are FASTER than a 1:15 athlete under race fatigue.** He loses **6:15 to fatigue** at station 8.
- Same pattern on the run: he ran **4:20** on a single compromised test km (W14) but averaged **5:43/km across 8 in-race**. Capacity is fine; expressing it at minute 94 is not.
- → **Fresh volume is NOT the fix.** The Wednesday EMOM is deliberately slotted "legs fresh," which trains the thing he is already good at. The fix is **coupling stations to accumulated fatigue** = exactly Block 3's job. This raises Block 3's priority above everything else.
- Reference-athlete pacing lesson: his runs post-opener were **4:11–4:20 (9s spread)**; ours drifted 5:26→6:04 (38s), off a 3:57 opener blowout. Roxzone: his never exceeded 0:50.

### 3c. Post-W16 ramp (agreed 2026-07-14 — build at the W16/W17 calibration, NOT before)
W16 is the deload; **W17–W20 (2B intensify) is where these ramp**, gated on post-deload recovery markers:
1. **Wall balls under fatigue** (top lever) — introduce compromised/coupled WB, not just the fresh EMOM.
2. **Sandbag lunges under fatigue** — adductor-gated as always.
3. **Sled pull** — already reaching race weight 102kg by W15; hold there.
4. **Roxzone discipline** — target every station entry <0:45 (~2 min, free, zero injury risk). Rehearse in any sim work.
Do NOT pre-build W17–20 now: calibrate off W14/W15 logs + how he comes out of the W16 deload.

### 3d. W17+ re-orientation — LOCKED design principles (2026-07-14)
**Frame (agreed):** 2 Hyrox-gym days only (realistic). Gym = sled + strength maintenance (day A) and compromised engine (day B). Wall balls done at HOME; sandbag PORTABLE. Running trimmed (see §3c). "Harder = SHARPER not MORE": re-orient toward **fatigued/compromised expression**, funded by trimming running, capped by recovery. Whole week is leg-dominant → **undulate emphasis week to week + deload every ~3–4 wk**; two monster leg days must never sit back-to-back. Wed (compromised engine → compromised wall balls, a half-sim) is the ONE hardest day; Thu (BSS/step-ups + sandbag) is the deliberate MODERATE counterweight.

**WALL BALLS — LOCKED (weakness #1, −4:16):**
- Gap is **DURABILITY, not capacity** — fresh 100 = 6:01 beats a 1:15 athlete's in-race 6:34. Do NOT train more fresh volume; train the wrecked state.
- **Marquee = compromised**, stacked on Wednesday AFTER the compromised engine (run→ski/row/sled→run→wall balls). Wall balls done systemically wrecked = the station-8 scenario.
- **Touches (max 3, distinct jobs):** (1) Wed compromised — durability, HARD; (2) EMOM — pacing/density, fresh-ish, MODERATE (can be made race-like by pre-running or cutting rest/raising reps); (3) OPTIONAL light skill/grease-the-groove dose (5 min, low reps, perfect depth + knee tracking) — **NOT a 3rd hard EMOM.**
- **KNEE-GATED:** wrecked wall balls = form breaks first → **cap volume, stop on form not the clock.** Tally weekly knee load (Wed WB + EMOM + skill dose + any BBJ + running); the skill dose is the FIRST thing cut if knee/recovery complain.

**SANDBAG LUNGES — LOCKED (weakness #2, −2:44):**
- Gap is **fatigued expression + distance, NOT load.** **HOLD load at 22.5kg** (race 20kg + margin) — do NOT chase the current plan's 25kg overload; he still struggles at 22.5 fresh, loads track actual.
- **Three touches:** (1) **Thu fresh distance-builder** after the BSS/step-up primer (priming validated — makes lunges feel easier) → 60→80→100m; (2) **Fri compromised** at race weight 20kg, broken across run intervals (run→20–40m→run) — the money session, lunging wrecked; (3) light **pattern-dose** 12.5kg 6–8/leg skill.
- **Proposed volume trajectory (ADDUCTOR-GATED, calibrate off W15/W16 logs — target not commitment):** W16 deload 15kg×30m · W17 ~100m/wk (Thu 60 + Fri 40) · W18 ~140m (80+60) · W19 ~160–180m (100+60–80) · W20 taper ~40m. Block 3 consolidates at ~100m race-weight COMPROMISED.
- **BIGGEST adductor gamble in the plan:** 45m/wk (W13) → ~160–180m/wk (W19) is a 3–4× ramp on the gated joint. **Hard stop:** any groin talk → cut Fri compromised FIRST, hold Thu, stop progressing distance. Ramp slows on any doubt.

**SLED — LOCKED (push −1:06, pull −2:11):** two touches across the 2 gym days, different jobs.
- **Mon (fresh) = strength + technique.** Sled Push 3×50m building load → race 152kg; cue **GLUTE-DRIVE** (fixes the W13 calf cramp). Sled Pull **3×50m — his call to keep 3; set 3 is AUTO-REGULATED**: stop the instant the back murmurs or form drifts — set 3 is a conditional bonus, never a mandatory grind. Groove braced-hinge + leg-drive; **FILM the pull.** Strength maint (Smith FS + RDL) rides here alternate weeks only (keeps Mon from ballooning).
- **Wed (compromised, inside the half-sim) = specificity.** run → 1×50m push (race wt) → run → 1×50m pull (race wt) → run → wall balls. Single sets = stations 2/3 exactly; pull as 1 set = no set-3 back point.
- **Load progression:** Push → toward 152kg (calf/glute-drive gated). Pull → **progress toward race weight 103kg** (athlete wants race-weight specificity — NO fixed 95kg cap). Load and volume both tax the back, so do not max both at once: (a) the **Wed compromised SINGLE (1×50m) is the primary race-weight exposure** — no set-3 volume risk, push race weight there FIRST; (b) on **Mon 3×50m, as load climbs the set-3 auto-reg tightens / drop to 2 sets** — 2 clean sets at higher load is a win, not a miss. Back stays the GOVERNOR: quiet → keep climbing (103 and into overload); flares as load rises → LOAD backs off.
- **Lower-back note (new, MINOR):** minor strain onsets at set 3 of the 50m pull — fatigue/dosing, not gross rounding. Managed by the set-3 auto-reg rule above; back is the pull VOLUME limiter. Escalate to physio only if it stops settling in a few days, sharpens, or radiates.

**RUNNING TRIM MAP — LOCKED:** running is 1:35-ready (43:57 vs ~44:30 model) → drop to minimum effective dose; freed recovery FUNDS the station work (reallocate, do not add).
- **Tue Tempo:** KEEP (~25–30 min, HR-gov 158–165; do NOT chase 35) — threshold = the race run demand, most specific.
- **Wed compromised:** becomes the ENGINE DAY half-sim (below); Test A/B drop to **periodic checkpoints** (do not run full tests + half-sim same week).
- **Fri 800m intervals:** CONVERT → run + sandbag lunges (compromised). VO2 = least-specific + most recovery-expensive, and speed is not his limiter (ran 4:20).
- **Sun long run:** 90 → **60 min** (race never runs 90 continuous; frees Sun leg-freshness).
- Net ~30km → **~22–25km/wk**; composition flips VO2-heavy → threshold + compromised-durability. Keep the aerobic base (long-60 + compromised volume — do not cut to zero). Optional speed insurance: 4–6×100m strides biweekly, cheap.

**ENGINE DAY (Wed) — LOCKED:** the weekly HALF-SIM, durability centerpiece + hardest day.
- **4 run→station rounds, priority-weighted, ~45–55 min:** R1 run 600–800m → SkiErg 500–1000m; R2 run → Sled Push 1×50m (race wt); R3 run → Sled Pull 1×50m (race wt, up to 103); R4 FINISHER run → compromised Wall Balls (money set, most wrecked).
- **Rules:** wall balls ALWAYS last (station-8 rehearsal); sled = compromised singles (back-safe); Row swaps Ski alternate weeks; runs @ threshold, HR-aware. Progression W17→20: runs → 1km, add a 5th round, tighten transitions, more WB volume — recovery-gated.
- HALF-sim, NOT a full sim (full sims stay capped at 2, Block 3–4).
- **Stacks ALL gated joints** (pull=back, WB=knee) under fatigue → within-session auto-reg applies hardest; drop a round when in doubt.
- **Logistics:** wall balls are done at HOME → ideally get a ball AT the gym so round 4 stays continuous; else do WB immediately post-gym (accept minor fatigue dissipation).

**ROXZONE REHEARSAL — LOCKED:** a LAYER on the engine day (+ any sim), not a separate session. Race bled ~2 free min; late entries blew out (Farmers-In 1:33, Sandbag-In 1:40 vs 0:03–0:39 early).
- **Time every transition, target <0:45.** Rehearse it **FATIGUED** (rounds 3–4 — where it blows out), not fresh. Mental reframe: roxzone = dead clock, NOT recovery (standing 60s barely drops HR, costs a full minute); cue "walk with intent, enter, start." Attack the known-slow entries (farmers, sandbag).
- Optional once/block: a dedicated transition drill (rapid run→station changeovers, minimal station work).

**W17+ RE-ORIENTATION DESIGN = COMPLETE** (wall balls · lunges · sled · running trim · engine day · roxzone). Build W17–20 at the W16 deload calibration off real W14/W15 logs + post-deload recovery — NOT before. BSS/step-ups/glute-thrust stay maintenance-only (Thu sandbag primer + Mon activation).

### 3e. AG-50-54 ELITE STATION TARGETS + testing routine (locked 2026-07-17)
Confirmed across BOTH races from the Singapore AG 50-54 **top-5 medians** (Nov-2025 + Apr-2026, `hyresult` — pulled the top 5 each year). His station gap to these measured **~18 min at both races** (2025 ~18:04, 2026 ~18:48); the **big-3 (sandbag/WB/sled pull) = ~75% of it**. These are real, age-appropriate targets hit by his actual peers — NOT 20-something elite times.
**Do NOT read that repeated ~18 min as stagnation** — the races are only 5 months apart with a 1.5-month break between (~3.5 months training), and environment-adjusted he improved ~3:18 (see §3a timeline note). The gap is real and large; the trend is positive.

| Station | AG-50-54 elite (NORTH STAR) | This-cycle (1:35 model) | His 2026 actual |
|---|---|---|---|
| SkiErg | ~4:40 | at target | 4:46 ✅ already there |
| Farmers | ~1:34 | ~2:15 | 2:41 |
| Row | ~4:35 | ~5:05 | 5:31 |
| Burpee BJ | ~4:30 | ~5:30 | 5:20 (near) |
| Sled Push | ~2:30 | ~3:45 | 4:51 |
| **Sled Pull** | ~4:15 | ~5:15 | 7:26 (+3:11) |
| **Wall Balls** | ~7:30 | ~8:00 | 12:16 (+4:46) |
| **Sandbag Lunges** | ~4:20 | ~7:15 | 9:59 (+5:39) |

**DIRECTIVE — actively PUSH him toward these (his explicit request 2026-07-17):** every weekly review and calibration, frame the big-3 station progressions against **closing the gap to these targets**, and **surface the current gap-to-target each review**. Near-term this-cycle target = the 1:35-model column; NORTH STAR = the AG-elite column (multi-year). Hold the line — do NOT let "good enough" drift set in on sandbag/WB/sled pull. Note: sandbag going from ~10:00 → 4:20 is a MULTI-YEAR arc, gated hard by the adductor; the honest this-cycle win is the 1:35-model numbers.

**TESTING ROUTINE (recovery-limited → test sparingly, mostly fold into existing sessions):**
1. **Passive weekly:** TIME the compromised big-3 reps INSIDE the Wed engine day (no added load) → running trend vs target. This is the primary progress signal (compromised = the real gap).
2. **Fresh benchmark at each deload week (~every 3-4 wk, fresh + low-volume):** one rotating big-3 station fresh-for-time — Sandbag 100m@20kg / Wall Balls 100-for-time / Sled Pull 50m@race-wt — vs its AG target. Measures raw capacity trend cleanly.
3. **Block-boundary battery (W16 deload · W20 exit · ~W24 · ~W29 sim):** big-3 FRESH + COMPROMISED + the secondaries (push/row/farmers/BBJ) once; log all gaps-to-target, recalibrate.
4. **Metric hierarchy:** COMPROMISED times = primary (closes the 18-min gap); FRESH times = secondary (capacity). Track both against the AG targets.
5. **Test guardrails:** skip any test when RHR/HRV flag run-down; sandbag/WB tests are adductor/knee-gated → a joint flare = FAILED test, redo when healthy, never push through for a number.

**SANDBAG baseline/re-test protocol (his Q 2026-07-17):** at **race weight 20kg** (NOT 22.5), **fresh** (ideally the W16 deload slot). Capture TWO safe numbers — (a) **unbroken max distance**: lunge to the FIRST genuine break, then STOP (do not grind past — that is where the adductor gets hurt); (b) **100m for time with PLANNED breaks** (pre-decide a break every ~20-25m), recording total time + break count. Do NOT do a max 100m unbroken-or-bust grind — he is built to ~45m, so that is pure adductor risk with low info value. Form-break/adductor twinge = effort over. AG-elite ~4:20 (mostly unbroken); his honest first number will likely be ~7-10 min with breaks — that is FINE, it is the baseline to beat. Reduced-weight lunging = the BUILD (pattern dose), NOT the test — keep the test at race weight so it tracks the real thing.

**SLED baseline protocols (added 2026-07-17).** *Correction to the record: he CAN pull/push race weight — he did both in the race. His 87.5-95kg training loads are a RAMP, not a ceiling. Do not infer capability from training load (Claude made that error).* What is genuinely MISSING is his **fresh time at race weight** on both sleds.
- **Sled PULL:** fresh **50m @ 103kg** for time, single set. Warm up building 87.5 → 95 → 103 (short pulls). Film it (braced hinge + leg drive). **Single set = BACK-SAFE** — his back issue is set-3 VOLUME, not load, so a one-set max sidesteps it. Log time + rest-pauses. Reference: at 87.5kg fresh he did 3:39-4:17 (W13); AG-elite race pull ~4:15 (so their fresh ~3:30-4:00).
- **Sled PUSH:** fresh **50m @ 152kg** for time, single set. Warm up building 130 → 141 → 152. Film it and **cue GLUTE DRIVE** — his W13 limiter was **CALVES cramping**, not legs; if calves go again that is a TECHNIQUE tell, not a strength ceiling. Reference: at 130kg fresh he did 2:23-2:58 (W13); his true in-race is ~4:16 (2025; the 2026 4:51 was the poor floor).
- **FLOOR CAVEAT — important:** sled times are floor-dependent, so **gym-fresh vs race-in-race is CONFOUNDED** (his 2025→2026 sled "decline" of 1:13 was purely a worse floor). **The clean diagnostic is fresh vs compromised AT THE SAME GYM** — fresh 50m @ race wt (this test) vs the compromised 50m @ race wt inside the Wed engine day. Same floor → the delta IS durability. Use that, not race-derived comparisons.
- **SCHEDULING TRAP:** do **NOT** test both sleds in one session — a max push pre-fatigues the pull and destroys its "fresh" status. **One sled test per gym day.**

**W16-END = ESTABLISH ALL FOUR FRESH BASELINES (the gate for the W17+ build).** He is currently MISSING the fresh baseline on 2 of the big-3, which is exactly why capacity-vs-durability has been argued rather than known. Test at the END of the W16 deload (freshest he will be), one effort per session:
| Session | Test |
|---|---|
| Gym day 1 | Sled **Pull** fresh 50m @ 103kg |
| Gym day 2 | Sled **Push** fresh 50m @ 152kg |
| Portable day | **Sandbag** — unbroken max distance + 100m w/ planned breaks @ 20kg |
| Home (optional) | **Wall Balls** 100 for time (re-baseline vs the 6:01 W13 mark) |

**The fresh number is the DIAGNOSTIC — it settles capacity vs durability per station:** fresh close to his in-race time → **capacity-dominant** (barely better fresh than wrecked); fresh much faster than in-race → **durability-dominant**. Build W17-20 off these four numbers, per station — do NOT pre-decide the capacity/durability split by theory.

## 4. Injury guardrails (also in CLAUDE.md — apply to ANY change)
- **Right adductor (recovering):** gates sandbag lunges, lunge/wall-ball combos, BBJ landings, lunge-to-run. Scale/skip if it flares.
- **Knee:** gates wall balls and burpee broad jumps.
- **Thoracic kyphosis:** cannot hold a free-bar front rack under load → front squat is **Smith-machine only**; free bar stays light for rack-skill. Do NOT progress the free front squat.
- **Tempo runs HR-governed** (158–165 bpm, upper Z4, 0% incline); progress by DURATION not pace.
- **Lower back (MINOR, monitor — new 2026-07-14):** minor strain onsets at set 3 of the 50m sled pull (fatigue/dosing, not gross rounding). Back is the pull VOLUME limiter → set 3 auto-regulated (stop on murmur/form drift, never grind), technique = braced hinge + leg drive. Load DOES progress toward race weight 103kg (no 95kg cap) but load+volume never both max at once — Wed single is the safe race-weight exposure, Mon volume flexes down as load climbs, back stays the governor. See §3d SLED. Escalate to physio only if it stops settling / sharpens / radiates.

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

> **REQUIRED OUTPUT FORMAT (agreed 2026-07-14).** Every **Sunday**, when the athlete sends the weekly logs, the FIRST deliverable is a **3-column table**, one row per exercise he logged:
>
> | Exercise | What I did | Tweak for next week (from the log) |
> |---|---|---|
> | e.g. Smith Front Squat | 50 top / 45×2 — "able to squat deeper on smith" | → 52.5 top / 47.5×2 (+2.5, all clean) |
> | e.g. Row/Ski 2×1k | 4:26 / 4:25 — failed 2nd round | → cut to 1k + 250m (his call; engine failed) |
>
> Rules: one row **per logged exercise** (not per session); column 2 quotes his actual numbers/notes; column 3 is the **specific** prescribed change (or **HOLD** / **CUT**) with the one-line reason from his log. Present this table **before** any narrative, guardrails, or version work. Everything else (fatigue read, vitals, deploy) comes after.

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
