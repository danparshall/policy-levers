# AI-policy legislators & committees shortlist — 119th Congress, Aug 2026

**Purpose:** Ground the `config/sources.yaml` Senate-member rows and committee picks in Phase 8 of the leg-watcher build. Delivered as research; final source-registry rows are Dan's call.

**Provenance:** Web research by general-purpose subagent, 2026-08-04. Live-verified against local files (`bills/frontier-act/`, `bills/obernolte-trahan/`) for the Peters disambiguation. Landscape claims below carry citation links — verify at commit time if any surprise the reader.

**Context on the "watchable" criterion:** the tool exists to catch the GAAIA failure mode — discussion drafts released via press page before appearing on congress.gov. So "watchable" means the legislator's OFFICE actively publishes AI-related material through channels a scraper/RSS can catch, not just floor speeches or committee questioning.

---

## Peters clarification (verified from local bill artifacts)

The "Peters" appearing as a GAAIA / FRONTIER cosponsor is **Scott Peters (D-CA-50)**, a House rep. Verified against:
- `bills/frontier-act/README.md`: `**Cosponsors:** Reps. Scott Peters (D-CA-50), Scott Franklin (R-FL-18), Suhas Subramanyam (D-VA-10) [...], Erin Houchin (R-IN-09).`
- `bills/frontier-act/press_release_2026-07-23.html`: `<strong>Representatives Scott Peters</strong> <strong>(D-CA-50)</strong>`
- `bills/obernolte-trahan/README.md`: `**Co-releasers:** Reps. Suhas Subramanyam (D-VA-10), Scott Franklin (R-FL-18), Scott Peters (D-CA-50), Erin Houchin (R-IN-09).`
- `bills/obernolte-trahan/press_release_2026-06-04.txt`: `Scott Peters (D-CA-50)`

**Gary Peters (D-MI)** is a separate person — Senate HSGAC ranking member. Dan's tracking of him on the Senate side is legitimate on its own merits (HSGAC role); the two just need to be disambiguated wherever notes say "Peters" unqualified. STATUS.md through 2026-07-24 uses the unqualified name in the GAAIA-cosponsor context, where it should read "Rep. Scott Peters."

**Downstream:** House member watch list should include **Rep. Scott Peters (D-CA-50)**; he was not in Dan's tracked-House list before this research pass.

---

## FRONTIER Act now has a bill number

The Obernolte press release surfaced by the research gives the FRONTIER Act as **H.R. 9925** (introduced 2026-07-23). This closes the "FRONTIER Act once numbered" TODO in the tracked-bills block of `config/sources.yaml`.

---

## Senate offices — recommended watch list

Dan's operating principle (2026-08-04): keep the important-even-if-annoying ones (Cruz, Schumer) alongside the high-signal press-page drafters. So the final list runs longer than the plan's "4–6 placeholder rows" figure — some enabled hot, some enabled at lower priority for leadership/gatekeeper signal.

Ranked by early-signal yield (drafts-on-press-page workflow), keeping Dan's overrides:

| Rank | Senator | Party/State | Rationale | Press URL |
|------|---------|-------------|-----------|-----------|
| 1 | **Mark Warner** | D-VA | HIGHEST YIELD. Rolled out 4-bill "Framework for America's AI Future" July 21–22, 2026 via press page + Axios exclusive: Data Center Tax Accountability & Disclosure Act, AI AGENT Act, Secure AI Development Act, Safeguarding Against Fabricated Exploitation Act. Intel vice-chair. Warner-Hawley AI jobs-disclosure bill also his. **New add — was not in Dan's list.** | `warner.senate.gov/newsroom/press-releases/` |
| 2 | **Marsha Blackburn** | R-TN | Released **TRUMP AMERICA AI Act discussion draft on her press page March 18–19, 2026** — literally the GAAIA failure-mode workflow (draft-first, congress.gov later). Judiciary + Commerce. Also NO FAKES co-lead (passed Judiciary June 18, 2026). **New add — was not in Dan's list.** | `blackburn.senate.gov/press-releases` |
| 3 | **Ted Cruz** | R-TX | Gatekeeper, not drafter. Commerce chair; every AI markup notice routes through his executive-session announcements. Scheduled a late-July 2026 AI markup. Watch "Chairman Cruz Announces…" URL pattern. **Kept per Dan** (annoying-but-important). | `commerce.senate.gov/press/rep` |
| 4 | **John Curtis** | R-UT | Freshman (Romney's seat, sworn Jan 2025); AI-signature-issue senator. Three bills already: SAFE KIDS Act (chatbots+minors), AI Labeling Act w/ Schatz+Warner, CLEAR Act w/ Schiff. **New add — was not in Dan's list.** | `curtis.senate.gov/press-releases/` |
| 5 | **Josh Hawley** | R-MO | Ranking on Judiciary Privacy/Tech/Law subcommittee. AI LEAD Act (w/ Durbin), Blumenthal-Hawley bipartisan framework, AI job-loss reporting (w/ Warner), China-decoupling AI bill, deepfake letters. High-volume press page. **New add.** | `hawley.senate.gov/` |
| 6 | **Mike Rounds** | R-SD | Already tracked. Working Group original; Armed Services cyber/AI subcommittee. Consistent bipartisan AI press releases. Keep. | `rounds.senate.gov/` |
| 7 | **Chuck Schumer** | D-NY | Minority Leader (Rs control 119th Senate); Insight Forums era is over so direct AI-specific press yield is lower — but leadership signal on AI (dear-colleagues, floor scheduling counterpoints) still matters. **Kept per Dan** (annoying-but-important). | `democrats.senate.gov/newsroom` |
| 8 | **Gary Peters** | D-MI | HSGAC ranking (Paul chairs). Lower press-page yield in minority role, but the HSGAC seat gives him standing on federal AI use / procurement / gov oversight material — including any minority-side dissents. Keep at lower priority. | `peters.senate.gov/newsroom/press-releases` |

**Dropped from earlier candidate list:**
- **Todd Young (R-IN)** — Demote to committee-feed-only coverage. His AI content mostly flows through cosponsorship (Cantwell-Young Innovation Act axis), not his own press page.

**Optional adds — hold for now, prime for later:**
- **Adam Schiff (D-CA)** — freshman senator, CLEAR Act (Feb 2026 w/ Curtis), AI Ads Act (deepfake political ads). Import House-era AI-transparency focus.
- **Chris Coons (D-DE)** — NO FAKES co-lead; long-standing IP/AI patents focus.
- **Bernie Sanders (I-VT)** — AI Data Center Moratorium Act (Mar 25, 2026 w/ AOC); AI Sovereign Wealth Fund Act. Left-flank signal.
- **Bill Cassidy (R-LA)** — HELP chair; AI-and-workers hearings.
- **Hickenlooper (D-CO)** & **Schatz (D-HI)** — recurring bipartisan AI cosponsors (Future of AI Innovation Act; AI Labeling Act).

**Senate "GAAIA duo" equivalent:** None yet. Closest pairs: Blumenthal-Hawley (bipartisan framework, older), Cantwell-Young (Innovation Act axis), Warner solo as Democratic center of gravity, Blackburn as GOP framework counterpart. **Watch for Warner-Blackburn or Warner-Cruz** as the next-quarter Senate pairing to prime for.

---

## Committees to watch

**High hit rate — always-on feeds:**

| Committee | Chair / Ranking | Press/markup pages | Why it matters |
|-----------|-----------------|--------------------|-----------------|
| **Senate Commerce, Science & Transportation** | Cruz (R-TX) / Cantwell (D-WA) | `commerce.senate.gov/pressreleases`, `commerce.senate.gov/markups/` | Jurisdictional home for nearly every AI bill (S.2938 AIRE Act, etc.). Subcommittee: Fischer (R-NE) chairs Telecom/Media — held AI-networks hearing July 30, 2026. |
| **House Science, Space & Technology** | **Babin (R-TX-36)** / Lofgren (D-CA-18) | `science.house.gov/` | Passed bipartisan AI package June 2026. Obernolte chairs the Research & Technology subcommittee (Dan's earlier notes have called Obernolte "Science chair" — he's a subcommittee chair; Babin holds the full-committee gavel). |
| **Senate Judiciary** | Grassley (R-IA) / Durbin (D-IL) | `judiciary.senate.gov/press/` | NO FAKES markup June 18, 2026; June 23 Big Tech CEO hearing; ongoing chatbot-harms subcommittee hearings. |
| **House Energy & Commerce** | Guthrie (R-KY) / Pallone (D-NJ) | `energycommerce.house.gov/` | Scalise routes AI to Guthrie (STATUS.md 2026-07-17). Consumer AI, data, telecom. |

**Medium hit rate:**

| Committee | Chair / Ranking | Why it matters |
|-----------|-----------------|-----------------|
| **Senate HELP** | Cassidy (R-LA) / Sanders (I-VT) | AI workforce hearings; Sanders staff produced the "100M jobs" projection. Rare but heavy content. |
| **Senate HSGAC** | Paul (R-KY) / Peters (D-MI) | Federal AI use, agency procurement, gov oversight. |

**Low hit rate, high-value when it fires:**

| Committee | Chair / Ranking | Why it matters |
|-----------|-----------------|-----------------|
| **Senate Intelligence** | Cotton (R-AR) / Warner (D-VA, vice-chair) | Mostly closed briefings but public releases on AI natsec matter enormously. |
| **Senate Armed Services** | Wicker (R-MS) / Reed (D-RI) | DOD AI, autonomy, adversarial AI. |

**Chamber-wide floor:**
- **Majority Leader weekly lookahead** (`majorityleader.gov`) — suspension-calendar tripwire, already in the plan.
- **Senate executive calendar / daily schedule** — already in the plan.
- **`docs.house.gov`** weekly committee-repository XML for Science + E&C markup/hearing notices — already in the plan.

---

## Corrections logged for downstream doc hygiene

1. **Obernolte is subcommittee chair, not full Science chair.** Babin (R-TX-36) chairs full committee. STATUS.md 2026-07-18 already correctly references "Babin (Science Chair)" in one place, so the framing is inconsistent within Dan's own notes — worth a cleanup pass at merge.
2. **"Peters" in GAAIA-sponsor context = Scott Peters (D-CA-50), House.** Not Gary Peters (D-MI). See top of this doc for verification. Update at merge if propagating.

---

## Sources (verbatim from the research agent)

- [Obernolte/Trahan press release — GAAIA discussion draft](https://obernolte.house.gov/media/press-releases/obernolte-trahan-release-discussion-draft-great-american-ai-act)
- [Obernolte/Trahan press release — FRONTIER Act (H.R. 9925, July 23, 2026)](https://obernolte.house.gov/media/press-releases/obernolte-trahan-introduce-bipartisan-frontier-act-strengthen-oversight)
- [Blackburn press release — TRUMP AMERICA AI Act discussion draft (March 2026)](https://www.blackburn.senate.gov/2026/3/technology/blackburn-releases-discussion-draft-of-national-policy-framework-for-artificial-intelligence/3b3b6458-b6c7-478b-9859-374949586765)
- [Warner press release — Framework for America's AI Future (July 2026)](https://www.warner.senate.gov/newsroom/press-releases/warner-rolls-out-comprehensive-ai-legislative-agenda-focused-on-responsible-innovation-workers-and-national-security/)
- [Axios exclusive — Warner AI plan (July 21, 2026)](https://www.axios.com/2026/07/21/mark-warner-ai-plan)
- [House Science Committee — Babin AI package passage (June 2026)](https://science.house.gov/2026/6/chairman-babin-applauds-committee-passage-of-bipartisan-ai-legislation)
- [Senate Commerce — Cruz markup schedule](https://www.commerce.senate.gov/markups/)
- [Roll Call — Senate Judiciary NO FAKES advance (June 18, 2026)](https://rollcall.com/2026/06/18/ai-deepfakes-bill-advanced-by-senate-judiciary-committee/)
- [Curtis press release — SAFE KIDS Act](https://www.curtis.senate.gov/press-releases/)
- [Schiff/Curtis CLEAR Act press release](https://www.schiff.senate.gov/news/press-releases/news-sens-schiff-curtis-introduce-bipartisan-bill-to-protect-creators-work-implement-transparency-safeguards-in-ai-model-development/)
- [Sanders/AOC AI Data Center Moratorium Act](https://www.sanders.senate.gov/press-releases/news-sanders-ocasio-cortez-announce-ai-data-center-moratorium-act/)
- [Hawley/Durbin AI LEAD Act](https://www.hawley.senate.gov/hawley-durbin-introduce-legislation-empowering-americans-to-bring-liability-claims-against-ai-companies/)
