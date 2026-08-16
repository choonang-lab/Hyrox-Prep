# HANDOFF.md — Session Continuity & Project State

**Purpose:** This file carries the full working context for the Hyrox-Prep project so any new Claude Code session (e.g. moving from Windows to the Mac desktop app) can pick up exactly where we left off. Read this together with `CLAUDE.md` (architecture + non-negotiable conventions). Treat this file as the source of truth for *session state, decisions, and rationale*; treat the code as the source of truth for *current numbers*. **Verify volatile details (version, loads) against the actual code — this doc can lag.**

> New machine setup: `git clone https://github.com/choonang-lab/Hyrox-Prep.git`, open in Claude Code, and (optionally) tell it "read HANDOFF.md and save the key facts to memory" so continuity persists across sessions on that machine. Re-connect the **Google Drive** connector (claude.ai connectors / `/mcp`) to resume the log-review loop.

---

## 0. PRE-FLIGHT CHECKLIST — run BEFORE the two recurring tasks
*(This is the enforcement layer. The doc is long; these lists are what actually gets applied. Each bullet cites the detailed section. If a bullet and the detail ever conflict, fix the doc.)*

**A) EVERY WEEKLY REVIEW (Sunday logs):**
1. **Lead with the 3-col table** — Exercise / What I did / Tweak — before any narrative. [§7]
2. **Loads track ACTUAL logged weights**; conservative ramp; let logs drive increases. [§4]
3. **Run every change past the GUARDRAILS**: right adductor, right knee, lower back, kyphosis, HR-tempo, recovery-#1. [§4]
4. **Recovery lens**: check RHR/HRV/sleep trend; "harder = SHARPER not MORE"; never add load to fix under-recovery. [§3b, §4]
5. **Surface the gap-to-target** on the big-3 (sandbag/WB/sled pull) vs 1:35-model + AG-elite; actively push toward them. [§3e]
6. **Running floor**: hold a comfortable ~22:30–23:00 5K; do NOT chase 5K, do NOT erode below floor. [§3d]
7. **Leg-load**: no two monster leg days back-to-back; **Thursday = knee + adductor double-jeopardy** — watch as sandbag ramps. [§3d, §4]
8. **After ANY sets/weight edit, UPDATE THE CUE to match** — editing sets but leaving the prose cue is how stale cues happen (v106/107 fixed a batch). Cue must never contradict its own entry.

**B) EVERY BLOCK BUILD (W16 deload calibration + block boundaries):**
1. Build off **REAL logs + the W16 fresh baselines** (4 tests: pull/push/sandbag/WB) — do NOT pre-decide capacity-vs-durability by theory. [§3e]
2. **Capacity-vs-durability is now EMPIRICAL, per station** — §3d "compromised-marquee-from-W17" is SUPERSEDED/gated: likely **capacity-dominant W17–20, compromised in Block 3**, decided by the baselines. [§3d, §3e]
3. **Big-3 priority** (sandbag/WB/sled pull ≈ 75–86% of the gap); **SkiErg + BBJ = maintenance only** (already at target). [§3a, §3e]
4. **Guardrails as HARD gates**: transition adductor rehab→prep & keep it THROUGH the sandbag ramp; sled pull = progress LOAD not volume (back). [§4, §3d]
5. **Recovery structure**: 2 gym days; undulate emphasis; deload every ~3–4 wk; protect Sat rest. [§3d]
   - **ACCESSORY DISCIPLINE (set 2026-08-09, v114 — applies to Blocks 3-4 too):** keep accessories LEAN. Do NOT reintroduce **DB step-ups** (knee), **loaded lateral lunge**, a **2nd loaded carry** (suitcase — Farmers is the race one), or **DB thrusters**. **Adductor work capped ~3/wk** (Copenhagen Mon + Copenhagen-dynamic & eccentric-slide Thu); no duplicate Copenhagen across Mon+Wed. **Never stack a big leg day (Thu BSS/sandbag) the day before the key interval session** — Thu→Fri leg fatigue killed W17 intervals. **Sandbag HOLD 22.5kg, build DISTANCE before load.** **Sleds HOLD competition weight (152/102)** — the +10% friction overload (§3d) stays a labeled FUTURE goal, NOT an in-block ramp this cycle.
   - **DELOAD MENTAL-BREAK RULE (athlete-set 2026-07-26, applies to W16 AND every subsequent deload week):** strip the low-value "fiddly" items for a genuine mental break — **remove the Front Squat Mobility Circuit and ALL Form Film entries** from any deload week. Keep the actual training (deloaded lifts/sleds/runs) + daily mobility + adductor rehab. Do NOT carry these two into future deloads. (Done for W16 in v113.)
6. **Do NOT misread history**: the 2 races are 5 months apart (not a year); env-confounded data (heat/floor) ≠ regression. [§3a]
7. **Running**: maintain the floor; sub-20 5K is a POST-race goal only. [§3d]
8. **Cue must match sets/weight** — rewrite each entry's cue whenever load/volume changes; never leave copy-pasted cues from the prior block (this is the #1 source of drift). Re-scrub cues after a build.

---

## 1. Snapshot (as of 2026-07-05)
- **App:** live at **VERSION 95** (`choonang-lab.github.io/Hyrox-Prep`). Single-file vanilla PWA.
- **Block 2 (W13–W20)** is **built, calibrated from real W12 logs, reviewed, and shipped.** W13 starts **Mon 6 Jul 2026**.
- **Blocks 3 & 4** — planning **deferred** pending the athlete's Sep–Nov travel schedule (direction agreed; see §6).
- **Next athlete action:** on W13 Monday, **establish the Smith front-squat top set** (the one open number; W14+ progresses off it).
- **Continuity loop:** athlete logs sessions on device → app exports a backup JSON to Google Drive → we review + calibrate the next week. (See §7.)

## 2. Athlete profile & target
- ~74 kg male (target race weight **75kg — at goal on the scale**), **Hyrox Men's Open, AG 50–54**, racing **Fri 27 Nov 2026**.
- **Target (reframed Jul 2026):** **1:25 stretch, ~1:30–1:35 probable.** Original sub-1:15 assessed unrealistic this cycle (would need ~31 min off a 1:46:34); kept only as a labeled aspiration.
- **Recovery is his #1 limiter** (masters athlete) — do NOT add volume/intensity to "fix" what is really under-recovery.
- **BODY COMP — it is RECOMP, not a cut (decided 2026-07-26):** he is AT goal weight (75kg target, ~74 actual, drifted +1kg over Jun–Jul) but body-fat / belly fat is creeping and annoying him. Do **NOT** advise a scale cut / calorie deficit — half the stations are ABSOLUTE loads (sled push 152 especially rewards mass) and his weakness is station STRENGTH, not weight; **weight is NOT on the critical path to 1:35/1:25** (stations + roxzone are), and a deficit fights his #1 limiter (recovery) + the W17–20 strength build. The fix is composition at held weight ~75: **(1) SLEEP first** (his erratic <6h nights drive central fat AND cap training); **(2) protein 1.6–2.2 g/kg (~120–160g)**; **(3) trim easy/liquid calories, dial carbs to activity — esp. in the W16 deload**; **(4) keep the strength work**; NEVER cut into the taper. Track WAIST (tape at navel) not just scale; recomp is slow (months). Precise macros → refer to a sports dietitian. (Athlete declined adding a waist field to the app 2026-07-26.)
- **NUTRITION targets (dialed 2026-07-26):** **Protein 170g/day FIXED** (~2.3 g/kg — anchor in GRAMS, not %; the % floats because calories cycle). Fat floor ~75g (~25%; do not drop below ~0.8 g/kg — masters hormones). **Carbs flex with the training day** (protein+fat fixed, carbs absorb the daily calorie difference → auto-periodizes to load). His prior **2-month intake avg ~2,730/day was a slight SURPLUS** (he gained ~1kg + belly fat on it) → true maintenance ~2,550–2,650. Normal-week day targets he ran: Sun 3,100 · Mon 2,900 · Tue 2,600 · Wed 2,750 · Thu 2,800 · Fri 2,650 · Sat 2,300. **W16 deload cut to ~2,500 avg** (all from carbs, protein held): Sun 2,800 · Mon 2,650 · Tue 2,400 · Wed 2,500 · Thu 2,550 · Fri 2,450 · Sat 2,200. **OUTPUT-BASED daily targets (dialed 2026-07-26 — supersedes the rough ~2,580 baseline).** Empirical TDEE from his own data: 2,730 intake + ~1kg gain over 2mo → **avg TDEE ≈ 2,625/day**; base (non-training) ≈ 2,100; training adds per day. Recommended = FUEL THE WORK, diet the easy days (~185/day deficit → ~0.2kg fat/wk, build-safe):

| Day | Session | Maint (base+burn) | TARGET |
|---|---|---|---|
| Sun | long run 90min | 3,050 | **2,900** |
| Mon | gym: sleds/squats/ergs | 2,800 | **2,650** |
| Tue | tempo + EMOM | 2,600 | **2,400** |
| Wed | pull + compromised tests | 2,600 | **2,400** |
| Thu | unilateral + sandbag | 2,550 | **2,300** |
| Fri | 5×800 intervals | 2,600 | **2,450** |
| Sat | rest | 2,100 | **1,900** |
| **avg** | | ~2,620 | **~2,430** |

KEY FINDING: his OLD plan OVER-FED the low-output days (Thu 2,800 = 2nd-highest for a moderate day; Sat rest 2,300) — the likely source of the creep; output-matching pulls exactly those down. **Dial:** eat the *Maint* column (~2,620 avg) instead for maintenance-recomp (max build support, minimal fat loss) — recommend the TARGET cut given the goal is belly fat at goal weight. Estimates ±10–15% → calibrate to scale + waist, not the formula. Gentle deficit only — recovery is the limiter; NEVER cut into the taper. Reassess by weight + waist every 2–3 wks: holding ~75 + waist shrinking = dialed; stalled after 3 wks = trim ~100 off the two biggest days.

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
> **⚠ SUPERSEDED IN PART (2026-07-17): the compromised-marquee-from-W17 emphasis below is NOT final.** He argued (correctly) that capacity feeds durability and that he cannot convert station capacity he does not yet have — and 2 of the big-3 have NO fresh baseline yet. So the **sequencing is now gated on the W16 fresh baselines** (§3e): likely **capacity-dominant W17–20, compromised work shifted into Block 3** (which is already the "Race Specificity" block). The session *shapes* below (engine day, sled, sandbag, roxzone, running trim) still stand; what changes is **capacity-first emphasis in Block 2B**, decided per-station by the baselines. Do NOT apply the "compromised from W17" reading without checking §3e.

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
- **FRICTION / OVERLAP stance (2026-07-17):** competition carpet is higher-friction than his gym floor → **his gym sled times FLATTER him** (a given weight is easier at the gym than on race carpet). **He CANNOT rehearse on the carpet — he races Day 1**, so gym overload is his ONLY friction-prep tool (raises its importance vs someone who could test the surface). **PROGRESS GOAL (over time, no deadline): ~+10% overload over race weight → Push ~167.5kg, Pull ~112.5kg** — training these on the slicker gym floor ≈ race weight on carpet. **Sequencing (do NOT jump):** OWN race weight cleanly first (152 / 103, back-tolerant) → THEN creep toward +10%, guardrail-gated. **Asymmetric risk:** Push (+10% → ~167.5) is calf/recovery-gated, lower risk — can chase more freely. **Pull (+10% → ~112.5) is BACK-gated** — it may never safely reach +10%; accept whatever overload the back tolerates, back stays the governor, never force it for the number. **Race-day pacing:** expect the carpet to be harder than every gym session — pace the sleds conservatively, do NOT set race pacing off gym times. **Surface/calibration (resolved 2026-07-17):** gym = standard gym sled flooring; **μ is not measurable and does not need to be.** +10% is a **STRENGTH-MARGIN target, not a precise friction match** — its job is to make race weight feel sub-maximal on any surface, which is robust to the exact gap. Do NOT try to derive μ from his data (race sleds are compromised+fatigued, gym are fresh — confound > signal). **Calibrate via a HYROX365 AFFILIATE session** (official sled + competition turf, year-round — NOT the race venue) if reachable → one session directly reveals the gym-vs-carpet gap at a known weight; **athlete will find an affiliate session when he can.** Else refine the % via a **post-race feedback loop** (compare gym overload times to actual race sled times, adjust next cycle).

**RUNNING TRIM MAP — LOCKED:** running is 1:35-ready (43:57 vs ~44:30 model) → drop to minimum effective dose; freed recovery FUNDS the station work (reallocate, do not add).
- **Tue Tempo:** KEEP (~25–30 min, HR-gov 158–165; do NOT chase 35) — threshold = the race run demand, most specific.
- **Wed compromised:** becomes the ENGINE DAY half-sim (below); Test A/B drop to **periodic checkpoints** (do not run full tests + half-sim same week).
- **Fri 800m intervals:** CONVERT → run + sandbag lunges (compromised). VO2 = least-specific + most recovery-expensive, and speed is not his limiter (ran 4:20).
- **Sun long run:** 90 → **60 min** (race never runs 90 continuous; frees Sun leg-freshness).
- Net ~30km → **~22–25km/wk**; composition flips VO2-heavy → threshold + compromised-durability. Keep the aerobic base (long-60 + compromised volume — do not cut to zero). Optional speed insurance: 4–6×100m strides biweekly, cheap.
- **MAINTENANCE FLOOR (his explicit ask 2026-07-17) — the trim must NOT erode running below this:** hold a **comfortable ~22:30–23:00 5K through the cycle** (he is at ~22:55 now). This is a HARD floor, and it is the **launchpad for the post-race sub-20 push** — do not let running drift so he has to rebuild a base in Dec. Floor is held by: tempo (threshold, the main 5K maintainer) + biweekly strides (top-end) + long-60 (base). **The strides go from "optional" to expected** given this floor. If a 5K check drifts >23:00, ADD BACK a light running stimulus — the floor wins over squeezing the last of the recovery budget. Check: 5K TT at block boundaries (already scheduled ~W17/W20) + tempo pace-at-HR as the ongoing signal.
- **POST-RACE (Dec 2026+): sub-20 5K = a legitimate DEDICATED goal** on the path to AG-elite / 1:25 — the AG-50-54 elites run ~18–19 min fresh (Raward in-race 34:53 = 4:22/km → fresh ~sub-19), so at that level running IS a differentiator, not just station support. His steelman (a faster fresh 5K lowers race pace ~1:1 if the fatigue tax holds) is VALID. But NOT this cycle: running capacity is NOT his binding constraint (he races 35–55s/km UNDER fresh pace — headroom, unlike stations where he is over capacity), he is already at the 1:35 run target, the station gap is 8× the run gap even vs AG-elite, and a masters 22:55→sub-20 is a slow high-volume project that competes with station recovery. So: MAINTAIN now (per the floor), CHASE sub-20 post-race.

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

**ACCESSORY CUTS (v104, 2026-07-17) — CUT across W15–20, CARRY INTO the Block 3 build (leaner accessory set):** removed — Tibialis Wall Raises, Banded Pallof Press, Front Squat Mobility Circuit (Wed only — Mon dose KEPT for the actual front squat), Dead Hang (Thu only — Wed dose KEPT for grip/sled-pull), SkiErg Technique Drill 4×→1× (Mon kept; ski is at AG-elite, over-invested). **(Air Squats were cut then RE-ADDED v105 — kept: post-tempo, pre-fatigued legs = compromised squat endurance + mental discipline; NOT a fresh accessory.)** Lateral Lunge — Loaded **reduced 3→2 sets** (NOT cut — it is frontal-plane adductor prep; keep it, just lighter, through the sandbag ramp). **KEPT as guardrail/prehab (do not cut):** Face Pulls + Incline Y-raises (posture/kyphosis), Copenhagen + Eccentric Adductor Slide (adductor), one Dead Hang (grip). Rationale: recovery-first — cut GENERIC accessories, keep the ones on guardrail/prehab duty. Block 3 inherits this leaner set.

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
- **Right adductor (recovering — GOOD progress as of 2026-07-17):** gates sandbag lunges, lunge/wall-ball combos, BBJ landings, lunge-to-run. Scale/skip if it flares.
  - **Status 2026-07-17:** long-lever Copenhagen = only a **slight, very mild twinge** (≈ GATE 2, but not yet silent/"pain-free"); dynamic version more strain (but that exercise is hard regardless). Close to recovered, NOT cleared.
  - **Do NOT lighten the adductor rehab yet — TRANSITION it, do not drop it.** Same exercises (Copenhagen, eccentric adductor slide, loaded lateral lunge), new job: rehab → **prep/insurance that protects the sandbag ramp** (eccentric adductor strength is the best protector against exactly the lunge loading coming). Keep the frequency THROUGH the W16 sandbag baseline + the W17+ 45→100m ramp — that ramp is the biggest adductor load in the plan, so dropping the work right as you load it hardest is when strains recur. Timing note: he wants to lighten "soon"; the honest answer is AFTER the ramp is tolerated, not before.
  - **CLEARANCE = asymptomatic under LOADED sandbag (GATE 3 = 60m @20kg pain-free, then the 100m build) DURING and NEXT-DAY — not a plank twinge.** The Copenhagen shows healing; the loaded lunge + next-day response is what actually clears him. Only then drop to true maintenance.
  - Not a medical assessment — gate system + symptom-monitoring is the self-check; formal clearance = physio.
- **Knee (RIGHT — status 2026-07-17):** gates wall balls and burpee broad jumps.
  - **Pattern:** RIGHT knee only, flares **after heavy single-leg work on Thursday** (BSS + step-ups + sandbag lunges + lateral lunge). Unilateral + load-specific → mechanical/loading issue, not systemic. **Currently in the ACCEPTABLE band** (mild ache after, settles).
  - **Acceptable band:** mild ache AFTER, gone within ~24h; no pain DURING reps, no swelling. **Tripwires → back off + physio (not "monitor"):** pain DURING the movement / sharp / pinpoint · ache lingering >48h or worsening session-to-session · swelling, giving way, pain on stairs or the eccentric descent · pain at rest.
  - **Highest-yield check (do this):** film right-leg BSS + step-ups from the front for **knee valgus / knee drifting past toes** (vs the left) — most common cause of unilateral single-leg knee pain, usually a **glute-med/stability asymmetry**; fix = glute-med activation (band walks / abduction cue) before single-leg work + control the eccentric + trim step-up height / BSS depth if it bites at the bottom.
  - **THURSDAY = DOUBLE-JEOPARDY DAY:** stacks BOTH gated joints (right knee AND adductor) under single-leg load, and the **W17+ sandbag ramp (45→100m) lands on the same day** → both loads rising together. Watch Thursday closely as the ramp progresses; if knee OR adductor creeps up the tripwire list, first move = **spread the single-leg stack**, do not push through. (Not a medical assessment — self-check via the band above; formal = physio.)
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

### 6a. Block 3 pre-build brief (drafted 2026-08-09 — read before building W21+)
1. **The pivot = capacity → DURABILITY.** Blocks 1-2 built fresh capacity; Block 3 trains expressing it under fatigue (his real gap: fresh 100 WB beats a 1:15 athlete; races 5:43/km off 4:20 fresh). Marquee work: **compromised wall balls** (after the engine), **sandbag broken across runs**, **sled singles inside sims** (race weight = stations 2/3), **coupled run→station→run**, half/full sims, and the **Friday slot → compromised running** (train the fade, not the top end — fresh intervals are polishing a strength [[hyrox-injury-guardrails]]). Matches the @dailyhyrox "stations that matter damage your next run" logic.
2. **Leg-load sequencing is a HARD design rule.** W17 proved stacking Thu legs before Fri running kills the running; Block 3's compromised work is even MORE leg-dominant → never put the hardest coupled/leg day the day before the key running/sim day. Single most likely thing to quietly wreck the block.
3. **Recovery gets MORE conservative, not less.** Compromised/sim work is more systemically taxing than capacity work + masters + post-flu + recovery is #1 limiter → ONE true hard day (the sim), deload every ~3-4wk, protect Sat, gate hard days on HRV/RHR (the flu proved that gate works). Do NOT let "race specificity" become daily grinding.
4. **Bake in the free wins:** roxzone <0:45 transitions in EVERY sim (his 2-yr leak: Farmers-in 1:33 / Sandbag-in 1:40 ≈ 2min free, zero fitness/injury cost); even pacing off the opener (his runs drift 38s vs a reference 9s).
5. **Carry-forward guardrails** (see §0-B standing prefs + §4): sandbag 22.5 + build distance; knee = no step-ups; back-governed sled at **competition weight** (overload chase OFF this cycle); Smith FS; lean accessories; Copenhagen ~3/wk; running = maintain floor, do not chase.
6. **Settle BEFORE building:** (a) **re-test clean baselines** (fresh WB100, sandbag distance, sled singles) — the flu scrambled the W17 compromised tests, so those calibration numbers are unreliable; W20 test week gives some. (**Flu confirmed FULLY RESOLVED 2026-08-09 → cleared to resume full load + run the re-tests.**) (b) **TRAVEL SCHEDULE (Sep-Nov) is the open dependency** — sim placement/equipment access depends on it; cannot design without it.
7. **Do NOT pre-build now** — calibrate at the W20 boundary off W18-20 execution + W20 test + post-flu recovery trend + travel dates.
8. **Plyometrics — NOT in Block 3 (decided 2026-08-09).** Wrong phase (plyos = general-prep/base quality; Block 3 = specificity/peaking → EXPRESS existing qualities, do not introduce a new high-impact stimulus), wrong joints (knee + adductor both gated; plyos are the highest-impact thing, right on them; also just off flu), wrong recovery context (#1 limiter, leg-heavy week we just de-loaded via the accessory cull). The reactive/power quality is ALREADY covered race-specifically: **BBJ** (horizontal plyo) + explosive **sleds** + **wall-ball** throw. Substitute for the running-economy/GCT benefit = **STRIDES** (4-6 × 15-20s @ ~85-90%, smooth NOT sprint, full recovery), ~1×/wk. **Placement:** he has only ONE easy run (Sun Z2 long) → do NOT tack strides onto the fatigued end of the 90min run (tired legs + knee). Do them **FRESH — folded into the Friday track warm-up** (already at Serangoon, warm, ideal surface); optional few at the START of the Sunday run. Running-form metrics are otherwise GOOD (cadence 185 @ easy pace is a strength; GCT 238ms slightly long = the only headroom); running is a strength not a limiter, so do not over-invest in form. **True plyometrics** (depth jumps/bounding) = POST-RACE off-season development item, once knee/adductor cleared. Also watch **L/R asymmetry** (GCT balance / stride) if the watch surfaces it — maps to the right-knee/adductor one-sidedness [[hyrox-injury-guardrails]].
9. **WORKED EXAMPLE — the Block 3 compromised session (adapted from a coach template, 2026-08-09).** This is the template for the compromised/coupled slot (item 1). Use **Part 2 as the core session; Part 1 optional.**
   - **PART 2 (the keeper) — coupled run→station→run:** 1km @ threshold/race pace → WB EMOM 5min → 1km → Sandbag EMOM 5min → 1km to finish. Trains the run-off-station fade = his exact gap.
     - **Wall balls:** RACE weight **6kg** (NOT the template's "heavy"), durable rep count (start ~10-12/min, build toward 15), **STOP on form not the clock** — knee-gated.
     - **Sandbag:** **22.5kg, ~10-15m/min or just 2-3 min** — NOT the template's 24m×5=120m (that is ~2× his continuous tolerance on a still-gated adductor = strain setup). Adductor-gated, stop on any twinge.
     - **Runs:** 1km @ threshold/race; scale to 600-800m if 1km too long.
     - Enter SCALED, auto-regulate UP week to week.
   - **PART 1 (threshold intervals 5×6min) = OPTIONAL / lower-yield** — polishes his already-strong engine [[hyrox-injury-guardrails]]. Use only on an occasional "run-bias" week, keep short (3×5min). **Do NOT stack Part 1 + Part 2 in one session** (recovery limiter) — one part per session.
   - **Placement:** ONE hard day (Wed half-sim or the converted-Friday slot); protect the day after (leg-load sequencing, item 2). **Bias the MOVEMENTS side** (his gap = stations + durability, not runs), within the joint gates.
10. **Compromised TESTS re-oriented (2026-08-09, v115).** Single-station tests are too SHALLOW for him — his fade is **CUMULATIVE** (minute 94, 8 stations deep), not acute-off-one-station, so they read "pass" and hide the real weakness.
    - **Test A** (1km→50WB→1km): **PASSED repeatedly & comfortably** — 4:24/km off WB vs a ~5:10-5:15 durability gate (WB adds only ~10s/km). No longer diagnostic → keep as an occasional benchmark / fold into the coupled session; do NOT treat as a weekly KPI.
    - **Test B RE-ORIENTED ski→run → Sled Push 152kg → 1km run** (shipped W18-20 v115). Ski→run was early/B-tier/low-run-damage and rewarded the anti-race behaviour of pushing the ski (his W17 fail). Sled→run = highest run-damage transition = his real fade. **Targets:** sled ~2:45-3:00; post-sled 1km ~4:30-4:45 (≤4:45 = 1:35 pace, ≤4:30 = 1:25); REAL metric = shrink the post-sled km toward his clean threshold km (~4:15), within ~10s = durability win. Do NOT sandbag the sled to protect the run (hides the damage).
    - **Expect Test B to also read "easy"** (cumulative, not acute) → the TRUE durability driver is the coupled compromised session (item 9), NOT single-station tests; A/B are periodic diagnostics only. Block 3: evolve both into the coupled session; a **sandbag→run** diagnostic is also high-value (his #2 weakness) but watch the adductor if it lands near the Thu sandbag day.

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
   - **⚠ TIMEZONE OFFSET (−1 day) — known + accepted, do NOT "fix" naively (2026-07-17):** check-date keys are stamped **one calendar day EARLY**. Cause: `index.html` builds each training day at LOCAL midnight then keys it with `date.toISOString().slice(0,10)` (UTC); athlete is Singapore (UTC+8), so local-midnight → previous day UTC. So a **Monday** session is stored as **Sunday**, etc. — a consistent −1 on EVERY entry regardless of log time. **When reading a backup, add +1 day to interpret the real training day** (e.g. W14 stamped 07-12→07-18 = actually trained Mon 07-13→Sun 07-19; he trains a normal Mon–Sun week). It is **harmless to him** (app writes+reads the same shifted key, checkmarks land correctly, nothing lost) — decision (2026-07-17) is to **LEAVE the app as-is** and just account for −1 here. A real fix would need a one-time key-migration (+1 day on all existing checks) or it would orphan his history — do NOT change the keying without that migration.
5. Backups are large (~700KB–1MB) → they exceed a single tool result; the download tool saves them to a file — decode the base64 `content`, parse JSON, and diff against the prior backup to find *new* logs.

### 7a. Weekly review log (newest first)
**W18 reviewed + W19 calibration batch (2026-08-16, v119).** First week with all the changes; **full completion.** Wins: accessory cull worked (Thu lighter — no step-ups/suitcase/thrusters); RDL held 95 (v117 gate worked); sandbag 80m @20kg **continuous**; Test B ran in new sled→run form (3:15 sled / 4:40 run — good first baseline). **Problems:** (1) **SLEEP tanked Friday** — two sub-5h nights mid-week (4.6h, 5.0h) → Fri intervals failed AGAIN (3:30 + 400m). 3rd Friday miss, but cause rotates (W17 legs, W18 sleep) → it's an INPUT problem (protect sleep), not a plan bug. (2) **KNEE flag** — slight pain Fri after Thu Bulgarian 4×10 → the pre-agreed trigger. (3) Ski 2×1000 failed (600m) — gassed + pacing. **Batch applied v119 (W19):** RDL HOLD 95 (form still watching, reverted the pencilled 97.5); **BSS → 3×8 @ 17.5** (knee — cut volume AND held load, did not jump to 20); WB EMOM → 12/min (his ask); removed Mon SkiErg drill (duplicate — it was Mon-only anyway, §8 "4×/wk" note was stale); **Row+Ski → held-pace rewrite + SPM cues** (row 24-28 spm cruise/leg-drive; ski ~32 spm / 30-34, power-per-stroke-not-rate) — 2×1000 each kept, KPI = hold the /500m split across BOTH reps, first-250m-easy, progress-when-repeatable; W20 ergs are the 1×1000 exit TT (SPM cues added). **⚠ SOLARIS CARPET CORRECTION:** athlete says Solaris carpet is **LOWER friction than competition** → his W18 sled times there (push 2:32-2:36) are **misleadingly fast, NOT a benchmark.** Reinforces §3d: every trainable surface flatters him vs race carpet → pace race-day sleds conservatively; do not benchmark off gym/Solaris times.

**Sandbag pattern dose 12.5→15kg (2026-08-09, v118 — carry into the W19 refresh).** Athlete found 12.5kg too light; bumped to **15kg** across W18-20 (Tue/Wed/Fri/Sun + W20 Tue/Sun). In line with the cue's own progression rule (progress once 8/leg is easy) and the endorsed **15kg ceiling** — still sub-working-weight (~60% of the Thu builder), grease-the-groove, adductor-gated. **BOUNDARY (recorded): HOLD 15kg — do NOT push this daily dose toward race weight** (frequency × heavy on the gated adductor = strain setup; race-weight sandbag lives ONLY in the Thu builder + Block-3 compromised session). W14/15/17 pattern-dose entries left at 12.5 (history).

**W17 reviewed + W18-20 accessory cull (2026-08-09, v114).** W17 (return-from-flu) — **full recovery confirmed**: HRV rebounded 38→95-134, RHR 54-59, energy 4. BUT he returned TOO HOT (day-1 sleds ABOVE target at 155/105 with HRV still 38; RDL 95 top, form broke) and the week's structure bit him — **2 failed sessions**: Wed compromised Test B (could not finish the 1k post-ski) and Fri intervals (1×800 @3:15 + only 300m, "glutes fried from Thu BSS"). Knee pain on step-ups; sandbag 25kg had to be broken (30+10+10+10). **Fixes shipped v114 (W18-20):** sandbag 25→**22.5kg** (build DISTANCE first); **CUT** step-ups (knee), lateral lunge, Wed Copenhagen, suitcase carry, thrusters → adductor **5→3/wk** (Thu 3→2), Thursday **12→8 items** (relieves the Thu→Fri leg-fatigue chain that killed Fri intervals); sleds **HOLD competition weight** (W19 160/107→152/102, no in-block overload). Bulgarians left 4×10 — trim to 3×8 only if Fri still suffers. RDL held 95 (fix form, no add). Lesson banked: after illness, ease the FIRST session; do not stack a big leg day before the key interval day.

**W16 ended in ILLNESS — flu (reviewed 2026-08-02).** W16 deload was executed flawlessly (full completion, all edits followed), BUT recovery markers went the WRONG way: **HRV avg 108 (W15) → 67 (W16), crashed to 38 on 08-02**; RHR up (~66→~70); energy stuck at 2 — despite BETTER sleep (7.0h avg). Cause = **a virus incubating, not under-recovery**: athlete confirmed a bug (blocked nose, sore throat, now COUGH → likely flu). Lesson: a paradoxical HRV drop during a well-slept deload = look for illness/stress before adding load.
- **W17 INTENSIFICATION POSTPONED — do NOT ramp.** All W17 load flags (RDL +2.5 / pull → 102–103 / intervals → 3:20–3:25 / tempo back to full 27–30min) are PARKED until markers rebound — gated on symptoms + HRV/RHR, NOT a date.
- **Guidance given (2026-08-02):** STOP training fully (cough = below-neck/systemic → **viral myocarditis risk**; never train through flu/fever). Rest until symptoms clearly resolving + **≥24–48h symptom-free, no fever**, THEN graded return: easy Z1–2 only → resume intensity only once **HRV back ~90+ / RHR <65 and feels well**; hard/compromised work comes LAST. **Calorie deficit OFF — eat at maintenance+ to recover** (fighting infection). See-a-doctor flags: high/persistent fever, chest pain/tightness, breathlessness, palpitations, chest-deep or worsening cough, no improvement after ~1 week.
- **Runway is fine:** ~17 wk to race (27 Nov); losing 1–2 wk to illness costs ~nothing — do NOT compress/rush the block.
- **NEXT:** when he turns the corner, reshape the coming week into an easy GRADED-RETURN week (not the built W17). For now days are skipped/rest. Nutrition targets (§2) resume only after recovery.

**Sandbag pattern-dose restored to W17-20 (edited 2026-07-26, v112).** Athlete noticed the light "Sandbag Lunge — Pattern Dose" (12.5kg, 6-8/leg, grease-the-groove) vanished from W16 on. It was a W14-15-only add that never propagated into the W13-20 build. Restored to **W17/18/19 Tue/Wed/Fri/Sun** and **W20 Tue/Sun** (test-week taper); **W16 deliberately left without it** (deload stays lean; Thu 15kg×30m is the one light sandbag touch). This is §3d sandbag touch #3 and matters most during the W17-20 distance ramp (25kg 60→100m) on the adductor; well-tolerated in W14-15 (zero groin complaint). NOTE the Fri *compromised* sandbag (§3d touch #2) remains absent from W17-20 by design (capacity-first reframe pushed compromised work to Block 3).

**W16 deload + handstand reprogram (edited 2026-07-26, v111).**
- **W16 Thursday trim:** the deload was real on every day EXCEPT Thursday (kept all 12 movements + a step-up rep bump 8→12). Cut **DB Step-Ups** (redundant unilateral vs Bulgarian; the anti-deload rep bump) and **Asymmetrical Suitcase Carry** (2nd loaded carry; kept Farmers as the race-specific one). Thursday now 10 items / 3 loaded leg-carry movements — matches the rest of the deload. Kept the adductor-rehab trio (Copenhagen dynamic, eccentric slide, lateral lunge) — they aid recovery + adductor continuity.
- **Handstand reprogram (W16→W20, athlete-directed):** shift from 2×/wk (Tue/Thu, kick-up drills) to **daily except Saturday** short micro-doses — added Mon/Wed/Sun (now Mon/Tue/Wed/Thu/Sun practice + Fri coached = 6 days). New prescription: **~5 min = wrist prep + 3-5 chest-to-wall PEEL-OFF freestanding holds**; **kick-up DEFERRED** (revisit later, in the Fri coached slot). Cue rewritten: balance from the fingertips, line (ribs down/glutes/push tall), learn the pirouette bail, **wrists are the governor** (any niggle = skip). Rationale: handstand is a skill → frequency > volume, and it is low systemic load so it does not fight recovery or the deload. Fri coached session left unchanged. Coaching lever flagged for later: introduce kick-up-to-balance + press work in the coached session once off-wall hold time is consistent.

**W15 reviewed 2026-07-26** (backup `hyrox-backup-2026-07-26.json`; trained Mon 07-20→Sun 07-26, stamped 07-19→07-25 per the −1 offset). App at **v110**. **Full completion — every session done, no skips.** Highlights:
- **800m intervals: all 5 held** (3:30/3:25/3:25/3:25/**3:20**, neg-split) vs only 3 + a 200m the week before — the durability chase is landing (aided by cooler/overcast + perf shoes, but real). Target 3:24–3:30 met.
- **Tempo:** 27 min, faded 12→11.5kmh at 20:30, **HR 161** (in 158–165 band) — threshold-pace endurance still building; HR-governed correctly.
- **Sled Pull:** went to **100kg** ×3×50m (above the 97.5 plan), set-3 fade (3:57) = auto-reg zone, **no back murmur**. **Sled Push:** 145×3, big set-1→2 drop-off (2:58→3:29) = near fresh ceiling at 145; no calf cramp (glute-drive cue working).
- **Sandbag:** held **22.5kg** 1×50m (correct, did not chase 25); **zero adductor complaint** all week (Copenhagen both sides at 45s, eccentric slides + lateral lunges done).
- Self-regulation notes from logs: "RDL felt stronger, +2.5 in W17"; "hold Smith FS 52.5, BB row 60 post-deload."
- **Perf shoes now standard for all runs** → judge runs by HR, not pace/distance (shoe + weather confound week-to-week).
- **Recovery:** vitals fine but **sleep erratic** (4 nights <6h incl. 5.62 today); energy dipped to 2 today post long-run; weight crept 73.6→74.7. Ordinary end-of-block fatigue → **W16 deload is well-timed.** No load added.
- **Guardrails all green** (adductor / knee / back / kyphosis / HR-tempo). No mid-block calibration change; big-3 on plan (pull closing 100→103; WB & sandbag stay conservative until the W17+ compromised/coupled work).
- **→ W17 flags** (apply at the W16/W17 build): RDL +2.5kg; HOLD Smith FS 52.5 / BB row 60 / sled push 145; sled pull → 102–103 if back stays quiet; intervals target → 3:20–3:25.

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
- **Sled Push** 130→141→**152 (race by W15)**→[106 DL]→**152×3 HELD W17-19** (progress by TIMES / tighter rest, NOT sets — Option B v116; both the overload 160 AND the 4th set cancelled)→**W20 1× for-time test**.
- **Sled Pull** 87.5→95→**102 (race)**→[72 DL]→**102×3 HELD W17-19** (same — quality not sets; set-3 back-governed auto-reg)→**W20 1× test**.
- **RDL** 90→92.5→95→[DL]→**95 HOLD W18 (FORM-GATED — form is the limiter at the top per his W17 log; earn the next jump only when all 5 top reps are clean)**→97.5 W19 (if 95 clean)→**[100 DROPPED v117 — no max-chase, W20 is light taper]**.
- **Smith Front Squat** AUTO-REGULATED: W13 = *calibrate* a clean 5-rep top (start ~50kg, LOG it); W14+ = "W13-top +2.5/+5/+7.5/+10kg". *He front-squatted free bar all of W12 and never set a Smith number — the top is genuinely unknown until W13.*
- **Wall Ball EMOM** W14–19: 6→8→[5 DL]→9→10→10 min. **Tempo** 25→35 min @5:00/km. **800m intervals** 4→6 reps, 3:24→3:18 (calibrated rebuild — he FAILED 6×800 in W12).
- **Long run FLAT 90 min** all weeks (deload/taper 60) — deliberate: maintenance, not chase (validated by his 07-04 long run: 90min/13k/143bpm).
- **Sandbag Lunges** distance builds 45→**100m (race)** at **22.5kg** (dropped from 25kg v114 — build DISTANCE first; weight chip = kg, sets chip = distance).
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
- [ ] **W16/W17 BUILD (next — W16 is the deload):** apply the W15-review W17 flags → **RDL +2.5kg**; **HOLD** Smith FS 52.5 / BB row 60 / sled push 145; **sled pull → 102–103** if back stays quiet; **intervals target → 3:20–3:25**. Build W17–20 off real W14/W15 logs + post-deload recovery (per §3c/§3d/§3e), NOT before.
- [x] **W13 Monday:** Smith front-squat top set established (W15 at 52.5 top / 47.5×2).
- [x] **Weekly loop:** running each Sunday (W15 reviewed 2026-07-26, see §7a).
- [ ] **Merged backup JSON** (his logs + current v95 plan) so his history travels onto the device via `restore.html` — discussed, **not yet built**.
- [ ] **Blocks 3 & 4:** build once travel schedule is known (direction in §6).
- [ ] Optional: add his **143 bpm** as the Zone-2 marker on the long-run card.

## 12. Version history (context)
v84 Benchmarks recalibrate · v85 Block 2 W13–20 shipped · v86 contrast + phase colours + overflow menu + countdown · v87 dark theme (tried, disliked) · v88 **light Hyrox theme** · v89 remove per-day +Add + fix card-eject `</div>` bug · v90 tap/long-press toggles · v91 tap-shield · v92 header/pill overlap fix · v93 shield text-select fix · v94 log-bar black+yellow · **v95 program-review fixes (flat-90 long run, sandbag load/distance split, cautious BBJ build).**
