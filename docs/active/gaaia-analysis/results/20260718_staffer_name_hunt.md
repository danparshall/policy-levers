<!-- Generated during: convos/20260718_staffer_name_hunt.md -->

# GAAIA staffer name-hunt — 11 uncaptured priority offices

- **Date:** 2026-07-18
- **Line:** gaaia-analysis
- **Handoff:** mechanics item #1 in `results/20260717_contact_matrix.md`
- **Method:** 11 parallel research subagents, one per office. Sources:
  LegiStorm free tier, LinkedIn, member press releases, AASLH LD contact
  PDF, House disbursement scrapes (AARST), Legisletter, RocketReach,
  ZoomInfo, Florida Politics, Maryland Matters.
- **Output:** 11 new entries in `crm/contacts.yaml` (see the
  "GAAIA HOUSE OUTREACH (2026-07-18 name-hunt pass)" section — contacts
  count 25 → 36); each carrying primary staffer + 1-3 alternatives +
  front-desk fallback + confidence.
- **Preserved untouched (handoff constraint):** `burns-w-obernolte`,
  `kindler-e-foster`, `samantha-foster`.

## Design constraint (unchanged from matrix)

Every email is educational — "thanks for taking this seriously, available
for technical briefings" + "further points you may not have considered"
with no direction on a specific bill. Stays outside 501(h) lobbying caps.

## Scope — the 11 offices

- **Tier A minus Obernolte (sponsor offices, 6):** Trahan, Subramanyam,
  Franklin, Houchin, Peters, Foushee.
- **Front-of-queue Science sweep (3):** Babin, Lofgren, Stevens.
- **MD constituent lane (1):** McClain Delaney.
- **Technical uptake candidate (1):** Whitesides.

Obernolte (Burns) and Foster (Kindler) already captured on 2026-07-17.

## Summary table — primary hits

Email convention: `firstname.lastname@mail.house.gov`. Only Schrage's is
independently header-verified (via the AARST disbursement scrape);
treat the rest as best-guess pending front-desk confirmation.

| Office | Party/District | CRM id | Primary staffer | Title | Confidence |
|---|---|---|---|---|---|
| Trahan | D-MA-3 | `weinrich-j-trahan` | Jackie Weinrich | LD (2026-, ex-Matsui) | med-high |
| Babin | R-TX-36 | `janushkowsky-s-babin` | Steve Janushkowsky | Sci Cmte Staff Director | med |
| Lofgren | D-CA-18 | `powell-c-lofgren` | Chad Powell | Policy Adviser | med (inferred) |
| Foushee | D-NC-4 | `spencer-h-foushee` | Harden Spencer | LD (May 2024-) | HIGH (LD) |
| Stevens | D-MI-11 | `steadman-l-stevens` | Liam Steadman | DCoS/LD (Sept 2023-) | med |
| Subramanyam | D-VA-10 | `bagwell-s-subramanyam` | Shaefer Bagwell | LD (Mar 2026-, from Whitesides) | med |
| Franklin | **R-FL-18** | `mosley-l-franklin` | Lindsey Mosley | LD (May 2025-) | med-high |
| Houchin | R-IN-9 | `schrage-n-houchin` | **Niel Schrage** | **Sr Policy Adviser (Jan 2026-)** | **HIGH — best AI hit; email verified** |
| Peters | D-CA-50 | `cooke-d-peters` | Dillon Cooke | LD (May 2025-) | med |
| McClain Delaney | D-MD-6 | `donlon-a-mcclaindelaney` | Andrew Donlon | LD/Counsel (LD Jan 2026-) | HIGH |
| Whitesides | D-CA-27 | `verma-k-whitesides` | Kara Verma | LD (April 2026-) | med-high |

## Per-office notes (compressed)

Full details incl. source URLs, alternate staffers, fallback paths, and
red flags live in `crm/contacts.yaml` under each id. This section is a
scan-friendly digest.

### Trahan (D-MA-3) — Tier A, GAAIA co-lead
- **Route:** Weinrich (LD) → E&C/tech LA. She's health-policy-background
  (from Matsui), not an AI SME herself; ask her to loop the tech LA.
- **Alt:** Alexandra Karabatsos (prior LD, may have left).
- **Fallback:** webform `trahan.house.gov/contact/`, front desk (202) 225-3411.

### Babin (R-TX-36) — Tier B, Science Chair
- **Route:** AI portfolio runs through **House Science majority committee
  staff**, not personal office. Janushkowsky (Staff Director) or Danny
  Smith (Sr Adviser) — both ex-Babin personal-office.
- **Alt:** Lauren Ziegler (personal-office CoS, Dec 2024-, ex-NASA
  Kennedy leg. affairs).
- **Gap:** personal-office LD slot appears vacant (Will Tucker → Blue
  Origin Nov 2025).
- **Fallback:** personal webform `babin.house.gov/contact/`, personal FD
  (202) 225-1555, cmte FD (202) 225-6371.

### Lofgren (D-CA-18) — Tier B, Science Ranking Member
- **Route:** Powell (Policy Adviser) — best inference for tech portfolio;
  **no explicit AI/tech LA surfaced** in free tier.
- **Alt:** Arlet Abrahamian (Sr Leg Counsel — likely Judiciary AI/IP);
  Ricky Le (CoS, June 2025-).
- **No named personal-office LD found.** Lofgren was urged to retire fall
  2025 → office may be in slower-hire posture.
- **Red flag:** two active LinkedIn profiles for Zoe Lofgren →
  impersonation risk. Do NOT use LinkedIn DM.
- **Fallback:** webform `lofgren.house.gov/contact`, FD (202) 225-3072 →
  ask for "LA covering AI and Science Committee portfolio."

### Foushee (D-NC-4) — Tier A, 9363 Democratic lead
- **Route:** Spencer (LD, two-source confirm) — high confidence.
- **Alt:** Arturo Reyes (Sr Policy Adviser, March 2026-; hired right
  before H.R. 9363 ramp — likely AI portfolio but unconfirmed).
- **Caveat:** Foushee is in a competitive 2026 primary with **heavy
  AI-PAC involvement on both sides** (WRAL) → office may filter
  AI-industry-adjacent outreach carefully. Lead with Canary's
  non-industry framing.
- **Fallback:** webform `foushee.house.gov/contact`, FD (202) 225-1784.

### Stevens (D-MI-11) — Tier B, Research & Tech Subc RM
- **Route:** Steadman (DCoS/LD, three-source confirm).
- **Alts (auto/tech-adjacent):** Casey Denoyer (LA, auto industry);
  Justin German (CoS, ex-Kuster DCoS/LD); Sanjay Reddy (LC, ex-health-tech
  data scientist); Brendan Greenlee (Staff Asst, data-analytics/AI).
- **Caveat:** Stevens announced **2026 Senate run** April 2025 → House
  office turnover / attention shift likely. Verify Steadman still in role.
- **Fourth-route fallback:** if Steadman punts, ask for "Democratic staff
  director, Science Committee, Research & Tech Subc" (sits under Lofgren's
  full-cmte minority staff).
- **Fallback:** `stevens.house.gov/connect-rep-haley-stevens`,
  FD (202) 225-8171.

### Subramanyam (D-VA-10) — Tier A, GAAIA co-releaser + HR 9372 sponsor
- **Route:** Bagwell (LD, March 2026- from Whitesides). Subramanyam
  personally has deep AI-policy chops (Obama OSTP AI advisor) → tech
  portfolio likely sits with Member + LD, not a dedicated LA.
- **Alts:** Chris Katson (prior LD, may still be in office); Gabriela
  Garcia-Ugalde (Comms Dir — useful for GAAIA/9372 press-side); Abby
  Carter (CoS).
- **Red flag:** LegiStorm salary shows overlapping March-2026 payments
  from Whitesides + Subramanyam — mid-month transition. If email bounces,
  Bagwell may not be fully cut over.
- **Fallback:** webform `subramanyam.house.gov/contact`, FD (202) 225-5136.

### Franklin (**R-FL-18**) — Tier A, GAAIA co-releaser Science
- **DISTRICT CORRECTION: FL-18, not FL-15** as listed in the 07-17
  contact matrix and payload-map table. Redistricted 2023. Bioguide
  F000472 = Clifford Scott Franklin, ex-Navy captain, House Science, AI
  Task Force. Update matrix + payload map at next pass.
- **Route:** Mosley (LD, May 2025-; portfolio = nat sec/approps/veterans).
- **Alt:** Melissa Kelly (CoS).
- **Do-NOT-email (stale LDs in older sources):** Charlie Truxal (→ Rep.
  Kat Cammack CoS March 2025); Will Sitton (LD 2023-May 2025 → Invariant LLC).
- **Fallback:** webform `franklin.house.gov/contact/`, FD (202) 225-1252
  → ask for LA on Science Cmte / AI Task Force portfolio.

### Houchin (R-IN-9) — Tier A, GAAIA co-releaser E&C
- **STRONGEST AI-PORTFOLIO HIT OF THE PASS.** Schrage: CS background
  (Harvard), prior tech-and-competition work at Invariant, invited to
  MIT senior-Hill-staff-only "Future of AI" seminar spring 2026. Email
  **independently verified** via AARST disbursement scrape (not just the
  standard-format construction).
- **Alts:** Caroline Bender (CoS, Nov 2025-; prior LD/Sr LA — practical
  escalation given LD vacancy); Parker Armstrong (Comms Dir).
- **Gap:** personal-office LD slot vacant — Jon Van Buren departed Oct
  2025, no public successor.
- **Recommend:** first email in the pilot batch → highest confidence,
  cleanest address.
- **Fallback:** webform `houchin.house.gov/contact`, FD (202) 225-5315.

### Peters (D-CA-50) — Tier A, GAAIA co-releaser E&C
- **Route:** Cooke (LD, May 2025-). NB: this is Rep. Scott Peters
  (D-CA-50, bioguide P000608, House), **NOT Sen. Gary Peters (D-MI)**.
- **Alts:** Adam Taylor (DC CoS, May 2025-, formerly LD); Ziyan Adisa
  Sears (Sr LA, Energy Policy Jan 2026- — closest confirmed E&C staffer);
  Lena Jacobson (Comms Dir, press-only).
- No dedicated AI/tech LA surfaced; portfolios split by subject (Health,
  Energy) — LD is the correct routing target.
- **Fallback:** webform `scottpeters.house.gov/email-me`, FD (202)
  225-0508 → ask for LA covering E&C Comms & Tech / AI.

### McClain Delaney (D-MD-6) — Tier B + MD CONSTITUENT bonus
- **Route:** Donlon (LD/Counsel; LD Jan 2026-, Leg Counsel from Jan 2025).
  Freshman office → small legislative shop; tech policy likely sits
  directly with Donlon given member's own NTIA/Common Sense Media
  background.
- **Alts (CoS context — two names in play):** Kaylee Robinson (CoS Jan
  2026-, prev LD Rep. Cartwright); Sonny Holding (listed as CoS in Jan
  2025 Maryland Matters piece — may have moved/reshuffled).
- **Constituent hook:** Canary is a Maryland org → lead with that.
- **Email format caveat:** house.gov URL renders as `mcclaindelaney`
  (no hyphen); NOT header-verified.
- **Fallback:** webform `mcclaindelaney.house.gov/contact`, FD (202)
  225-2721 → confirm Donlon covers Science / AI portfolio.

### Whitesides (D-CA-27) — Tier B, ex-NASA CoS / technical uptake
- **Route:** Verma (LD, April 2026-). Prior LD (Bagwell) left for
  Subramanyam March 2026; Verma ~3 months in as of 07-18. AI likely
  rolls up to LD directly.
- **Alts:** Jennifer Goedke (CoS); Gabriel Harrison (LA, climate/nat
  resources, Climate Crossroads Fellow 2025-26).
- **Caveat:** Verma's prior background (Harder, McDonald Rivet, Jackson
  Lee; CyberHouston intern) shows no strong AI-policy footprint — brief
  from first principles rather than assuming context.
- **Stale aggregators:** Legisletter still lists Bagwell as LD.
- **Fallback:** webform `whitesides.house.gov/contact/`, FD (202) 225-1956.

## Cross-cutting findings

- **11/11 offices produced a routable staffer.** No office fell back to
  pure webform.
- **No dedicated "AI LA" title surfaced in any of the 11 offices in
  free-tier sources.** LegiStorm Pro paywalls the full portfolio-tagged
  roster. Route via LD or Sr Policy Adviser; front-desk call is the
  cheapest way to close the specific-AI-owner question.
- **Cross-office staff-mobility chain (captured both ends):** Shaefer
  Bagwell moved Whitesides → Subramanyam as LD in March 2026 (LegiStorm
  salary shows overlapping March payments — mid-month transition);
  Kara Verma is Whitesides's replacement LD (April 2026).
- **Committee-staff routing dominates at the Science Chair (Babin).**
  When a member chairs a committee whose jurisdiction is your topic, the
  personal-office LA becomes vestigial for that topic — committee majority
  staff is the substantive contact. Same pattern may show up when we get
  to Guthrie (E&C chair) in a later pass.
- **Recent-turnover risk is universal.** LegiStorm salary records show
  major reshuffles in 6 of the 11 offices in the last ~12 months
  (Trahan LD, Franklin LD, Peters LD, Whitesides LD, Subramanyam LD,
  Houchin CoS+LD). Aggregators (Legisletter, RocketReach, ContactOut,
  the AASLH LD PDF) lag reality by 3-12 months and can list the wrong
  person. Rule: trust LegiStorm salary records + a fresh press release,
  distrust aggregators.
- **Two Democratic offices in the batch are in a shifting-attention state**
  Foushee (competitive 2026 primary, AI-PAC-heavy) and Stevens (2026
  Senate run). Both still worth pursuing — the caveats are about tone
  and cadence, not about writing the offices off.

## Corrections & flags

- **Franklin district FL-15 → FL-18.** Update
  `results/20260717_contact_matrix.md` Tier A table (currently row 24),
  payload-map table, and the "Overlaps to exploit" line (row 40). No
  substantive change to targeting, just the label.
- **Contact matrix "Obernolte holds an E&C seat per DLA Piper" verification
  bullet** (open item, row 70) still not verified this pass; unchanged.
- **9363 cosponsor pull** (open item, row 71) still not done; not part of
  this task.

## Recommended next steps

1. **Correct Franklin FL-15→FL-18** in `results/20260717_contact_matrix.md`.
   Small mechanical edit, no analysis needed.
2. **Pilot email: Niel Schrage (Houchin).** Highest confidence, cleanest
   address. If Canary's education-first framing gets a substantive reply
   from Schrage, that's calibration for the rest of the batch.
3. **Front-desk verification pass** before cold-emailing at scale — one
   call per office (~11 calls, ~2 hrs). Priority order:
   - **Babin** — need current personal-office LD anyway (Tucker gap).
   - **Stevens** — Senate-run turnover risk; verify Steadman still in role.
   - **Whitesides + Subramanyam** — verify Bagwell mid-March transition
     complete; test whether Verma is triaging or actively taking meetings.
   - **Lofgren** — confirm Powell is the AI-covering LA (currently inferred).
   - Others — spot-check based on bounces.
4. **Second-pass name-hunt** for the remaining Tier B Science-sweep
   members not in this batch (18R + 11D; see contact matrix rows 36-38).
   Sequencing per matrix: only after 9363-lane emails to this batch land.
5. **Update `crm/senators.yaml`** with House-side entries for these 11
   members (currently Senate-focused only) — one row per member with
   posture, framing, and any relevant chamber context. Not a blocker for
   emails, but the CRM was designed with that structure and drift is
   easier to prevent than to fix later.

## Methodology notes (for reproducibility)

- **Fan-out shape:** 11 parallel general-purpose agents, one per office,
  each given the member's name/party/district/phone/office and a
  structured prompt (target = LD or AI/tech LA; sources in priority
  order; return format specified).
- **Source-of-truth ranking (established this pass):**
  1. LegiStorm salary records (most current, hardest to fake)
  2. Member's own press releases with a staff contact byline (verifiable)
  3. LegiStorm bio pages (current as of last salary posting, ~monthly lag)
  4. LinkedIn profiles (self-updated; verify against LegiStorm)
  5. Aggregators (Legisletter, RocketReach, ZoomInfo, AASLH PDF) — treat
     as leads only; verify against #1-#3
- **Failure modes observed:**
  - `houchin.house.gov` returned 403 to WebFetch (may need browser fetch
    for press-release footers on Houchin's own site)
  - `democrats-science.house.gov` returned 403
  - `foushee.house.gov` press-release footers returned 403
  - Multiple aggregators still list departed staff (Bagwell as
    Whitesides's LD, Sitton as Franklin's LD, Tucker as Babin's LD)
