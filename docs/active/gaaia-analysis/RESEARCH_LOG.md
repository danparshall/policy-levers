---
## Session: 2026-07-18 — 20260718_matrix_and_blog_corrections

### Topics Explored
- Applied the accumulated correction queue: Franklin FL-15→FL-18 in the contact
  matrix (+ dated correction note; revised Obernolte/Foushee narrow asks per the
  9363 adversarial review); blog corrections per the review's "defensible framing"
  list ("exact inverse" retired, repeal-and-replace → political-not-textual,
  §5002 collision + sunset mismatches added).
- Two-CAISIs section then rewritten twice on Dan's challenge ("what exactly is
  the point?"): thesis version (hedge vs. substitute, intent-agnostic ratchet),
  then final two-paragraph cut per Dan — clean sequencing story ("doing what can
  be done now, awaiting future fixes"; ASRS-before-there's-an-FAA).

### Provisional Findings
- 9363: sole referral to House Science (verified from ih print; no other House
  gate remains — suspension is the no-amendment consensus fast lane; Senate is
  the real filter). Introduction cosponsors: Foushee, Babin, Mann, Franklin
  (partially resolves matrix cosponsor open item; Mann new).
- DeepSeek/extraterritoriality tidbit VERIFIED (no US nexus in §101(8)/(12);
  all "United States" full-text hits are boilerplate) — blog unchanged there.
- **Sunset unseals the archive:** 9363 (k) terminates the section with no
  grandfather clause ⇒ plain reading strips (e)(1)/(e)(2) protections from
  already-shared info at year five; FOIA Ex. 4 partial backstop on disclosure,
  none on government-use (Landgraf retroactivity = colorable counter). Chills
  the voluntary channel in year one. Fix = one-sentence grandfather clause ⇒
  **new annex ask**, valence-neutral, natural for the Foushee email.

### Results
- Edits in place: `results/20260717_contact_matrix.md`,
  `essays/canary/gaaia-visibility-not-control_DAN.md` (header changelog logs all
  three passes). Convo: `convos/20260718_matrix_and_blog_corrections.md`.

### Next Steps
- Dan seam-check of the two-paragraph Two-CAISIs section; his transitions +
  501(h) call remain the publish blockers.
- ~~Add the (e)-grandfather-clause ask to NOTES.md~~ DONE same session
  (`1498e19`): new "H.R. 9363 asks (staff channel)" section, grandfather clause
  lead + 5 sibling items; § 112(q)(3) added to Tier 1.
- Then the standing queue: Schrage pilot email, front-desk verification pass,
  Burns/Kindler follow-ups 7/21, rh-text reconcile when GPO posts.

---
## Session: 2026-07-18 — staffer name-hunt pass (11 offices)

### Topics Explored
- Name-hunt for LD / AI-tech LA at 11 uncaptured priority offices from
  `results/20260717_contact_matrix.md` mechanics item #1: Tier A minus
  Obernolte (Trahan, Subramanyam, Franklin, Houchin, Peters, Foushee) +
  front-of-queue Science sweep (Babin, Lofgren, Stevens) + McClain Delaney
  (MD constituent lane) + Whitesides (technical uptake candidate).
- 11 parallel research subagents; sources hit: LegiStorm free tier,
  LinkedIn, member press releases, AASLH LD contact PDF, various House
  staff aggregators (Legisletter, RocketReach, ZoomInfo).

### Provisional Findings
- **Hit rate: 11/11 identified a routable staffer** (LD or Sr Policy Adviser).
  Confidence ranges high → medium; no office fell back to pure webform.
- **Best AI-portfolio hit: Niel Schrage (Houchin)** — CS background, MIT
  senior-Hill-staff-only AI seminar attendance spring 2026, email
  independently verified via AARST disbursement scrape. HIGH confidence.
- **Weakest personal-office coverage: Babin (Science Chair)** — AI portfolio
  runs through committee majority staff (Janushkowsky = Staff Director,
  Danny Smith = Sr Adviser; both ex-Babin), not personal-office LA.
  Personal-office LD slot appears vacant (Tucker → Blue Origin Nov 2025).
- **No dedicated "AI LA" surfaced in free tier for any office** — LegiStorm
  Pro paywalls the full staff roster. Route via LD or Sr Policy Adviser.
- **Cross-office staff-mobility chain:** Shaefer Bagwell moved Whitesides →
  Subramanyam as LD in March 2026 (LegiStorm salary shows overlapping
  payment); Kara Verma is Whitesides's replacement LD (April 2026). Both
  captured; Verma is ~3 months in as of 07-18.
- **Emails: house.gov `firstname.lastname@mail.house.gov` convention** used
  throughout; only Schrage's is header-verified (via disbursement list).
  Treat rest as best-guess; front-desk confirmation recommended before
  cold email at scale.

### Notable Corrections & Flags
- **Franklin district correction: FL-18, not FL-15** (redistricted 2023).
  Bioguide F000472 = Clifford Scott Franklin, ex-Navy captain. The 07-17
  contact matrix and payload-map table list him as FL-15 — outdated.
  Update `results/20260717_contact_matrix.md` and any downstream tables
  at next pass.
- **Foushee 2026 primary caveat:** heavy AI-PAC involvement on both sides
  (WRAL) → office may filter AI-industry-adjacent outreach carefully;
  lead with Canary's non-industry framing.
- **Stevens 2026 Senate run** (announced April 2025) → House office
  turnover / attention shift likely; verify Steadman still in role before
  pitch.
- **Lofgren retirement pressure** (fall 2025 SF Inquirer piece) → slower-hire
  posture; do NOT use LinkedIn DM (two active profiles, impersonation risk).
- **Do-not-email list at Franklin:** Charlie Truxal (→ Cammack CoS March
  2025), Will Sitton (→ Invariant LLC May 2025) — both stale LD names still
  appearing in older sources.
- **McClain Delaney email format:** house.gov URL renders as
  `mcclaindelaney` (no hyphen); NOT header-verified.

### Results
- `results/20260718_staffer_name_hunt.md` — full report (summary table,
  per-office notes, cross-cutting findings, corrections/flags,
  methodology + source-of-truth ranking).
- 11 new entries in `crm/contacts.yaml` under a new "GAAIA HOUSE OUTREACH
  (2026-07-18 name-hunt pass)" section. Total contacts now 36 (was 25).
- Burns/Kindler/samantha-foster left untouched per handoff constraint;
  YAML validated (parses cleanly, front_desk section intact).
- Each entry carries: primary staffer (id, title, email, source URLs),
  1-3 alternatives with emails, front-desk fallback with the ask to make,
  and a confidence rating.
- Convo: `convos/20260718_staffer_name_hunt.md`.

### Next Steps
- **Correct Franklin FL-15→FL-18** in `results/20260717_contact_matrix.md`
  Tier A table, payload-map table, and any other reference.
- **Front-desk verification pass** before cold-emailing at scale — one call
  per office (~11 calls) confirms staffer still in role and email is right.
  Cheapest at Babin (need to identify current personal-office LD anyway),
  Stevens (Senate-run turnover risk), Whitesides/Subramanyam (verify
  Bagwell transition complete). Schrage can be first email — highest
  confidence and clean disbursement-verified address.
- **Second-pass name-hunt** for Tier B Science-sweep members NOT in this
  batch (Weber, Baird, Webster, Fleischmann, Issa, Tenney, McCormick,
  Collins, Fong, Rouzer, Self, Harrigan, Biggs, Hurd, Haridopolos, Kennedy,
  Begich, Van Epps on the R side; Bonamici, Ross, Salinas, Sykes, Amo,
  Rivas, McBride, Gillen, Friedman, Riley, Menefee on the D side) —
  deferred until after 9363-lane emails land, per sequencing in matrix.
- **Try to identify Babin's current personal-office LD** via front-desk
  call — post-Tucker vacancy is a gap.

---
## Session: 2026-07-17→18 — 20260717_audit_deployment_linkage_verification

### Topics Explored
- Opus adversarial review (parallel terminal) of the "no provision joins audited to deployed" claim against GAAIA full text; multi-session git reconciliation (two divergences, one essay stash conflict).

### Provisional Findings
- Blanket claim REFUTED (§111(c) per-deployment assessment, §101(20) retrigger, §112(b) §111-compliance verification, §112(g)(1)(B) out-of-cycle reports); grep kernel verified exact (0×hash/checksum/cryptographic/fingerprint, no identity clause, no officer certification, report-level-only recordkeeping). Defensible residual: checkpoint substitution (assess A, ship B), §111(d) knowing-falsity the only hook. Converged independently with the other session's close read (Issue #1 erratum).
- Tier 3.8 provenance ask survives intact; motivating sentence reworded in NOTES.md.
- New essay tidbit (DeepSeek/extraterritoriality) needs a §101/"deploy"-reach text check before publish.

### Results
- `results/20260717_audit_deployment_linkage_review.md` (refutation table w/ line citations + grep verification; named controlling in STATUS Issue-#1 erratum).

### Next Steps
- Verify the DeepSeek/extraterritoriality claim against bill text; decide whether to consolidate this review with the close-read memo.

## Session: 2026-07-17 (late) — 20260717_hr9363_adversarial_review

### Topics Explored
- Adversarial review (explicit REFUTE stance) of `results/20260717_hr9363_comparison.md` against full texts of H.R. 9363 (ih) and GAAIA draft.

### Provisional Findings
- Inference 1 ("impossible as drafted") REFUTED — amendment executes as duplicate designation; only two numbered cross-refs, self-anchored; ~4-edit cure. Real misfire is the missed §5002 double-amendment collision (incompatible redesignation schemes).
- Inference 2 (use-immunity binds later GAAIA) REFUTED as law — GAAIA §102(d)(2)(B) is the identical clause; survives only as pre-shared-info fair-notice + optics.
- Inference 3 (ceiling vs (a)(3) hatch) SURVIVES — hatch discretionary, recommendations-only; caveat: political/textual preemption, never a legal cap on a later Congress.
- Blog "exact inverse of GAAIA's machinery" (line 71) needs reword before publish. New annex: §5002 collision; §112(q)(3) "section 111" mis-anchor; 9363 sunset-vs-(e)-confidentiality; FY2032 auth vs 5-yr sunset.

### Results
- `results/20260717_hr9363_memo_adversarial_review.md` (controls); erratum appended to `results/20260717_hr9363_comparison.md`.

### Next Steps
- Reconcile against rh text when GPO posts; reword blog line 71; fold §5002-led technical-corrections ask into Obernolte/Foushee outreach; annex the new bugs.

## Session: 2026-07-17 — 20260717_gaaia_contact_matrix
2026-07-17: contact matrix + call sheet + blog v3 + audited==deployed close read (superseded in part by adversarial review; checkpoint-substitution framing controls) + H.R. 9363 pull/comparison (§5304 collision; ceiling verdict pending review). See convo 20260717_gaaia_contact_matrix.md.
