# Research Log: academic-recruitment

Created: 2026-08-02
Purpose: Map how AI Policy funders recruit (or fail to recruit) established adjacent-field academics (cryptographers, economists), using the Vannevar Bush / OSRD playbook as the pitch frame.

---

(Sessions logged here, newest first)

## 2026-08-02 — Landscape + Bush playbook (line start)

Session started from Dan's question: has anyone in the AI safety community reached out to Aumann & Lindell (covert-adversary MPC, J. Cryptology 2010) with grant money for compute-treaty verification work, and how much is "actively recruit relevant academics" part of the ethos?

**Findings (cryptographers):**
- The covert-adversary *model* is now standard framing in AI-governance verification (Cankaya arXiv 2606.00279 opens with it, citing Baker 2025, Harack et al. 2025, Scher & Thiergart 2024, Wasil et al. 2024). No public evidence anyone has engaged Aumann or Lindell themselves. Lindell leads Coinbase's crypto team (Unbound acquired Jan 2022, on leave from Bar-Ilan); Aumann is the reachable academic of the pair.
- Better primitive for treaties: publicly verifiable covert security (PVC — Asharov & Orlandi "Calling Out Cheaters", then Kolesnikov, Damgård, Xiao Wang et al.). Cheating produces a transferable certificate showable to allies/UN — what enforcement actually needs. PVC authors are the live recruitment targets.
- Ecosystem: Oxford Martin AIGI verification team (Harack et al. 2025 report, 27 authors; Hardware AI Governance Lab; open expression-of-interest), MIRI TGT (Scher & Thiergart), Mauricio Baker six-layer report (arXiv 2507.15916), FlexHEG (Petrie/Aarne/Ammann/Dalrymple 2506.15093), Shavit 2023 Chinchilla, FLI-convened ~40-person verification workshop (early 2026, "datacenter lie detector" post), ARIA "Trust Everything, Everywhere" seeds, commercial (EQTY Lab Verifiable Compute w/ Intel+NVIDIA; EigenAI deterministic inference Jan 2026).
- **Key distinction: the money is pull-shaped, not push-shaped.** Coefficient Giving TAS RFP (~$40M, academic start-up packages) exists but is alignment-scoped and requires the professor to find it. Nobody is walking into a cryptographer's office with an agenda and a check. Schmidt Sciences AI safety science program is the closest to curated commissioning; still alignment-flavored.

**Findings (economists — the instructive contrast; Dan's "only Brynjolfsson-ADP" was an undercount):**
- Agenda + home: Brynjolfsson/Korinek/Agrawal NBER research agenda (WP 34256, nine Grand Challenges, Sloan + Bradley funded, from Asilomar 2024); UChicago Press TAI volume (16 studies incl. Chad Jones on x-risk spend); Korinek's EconTAI Initiative at UVA (Sept 2025) + NBER TAI workshop.
- Money aimed at RAs + data: Stripe Economics of AI Fellowship — $10k baseline, extra for data purchases, TA/RA-unit buyouts for grad students.
- Data pipelines: Anthropic Economic Index + Economic Advisory Council (Korinek member) + Economic Futures Program; OpenAI usage data to Brynjolfsson et al. ("How People Use ChatGPT"); ADP payroll collab ("Canaries in the Coal Mine"); Census BTOS, Ramp, LinkedIn as adoption instruments.
- Caveat: most of this is Sloan/Stripe/NBER/labs, not the safety community. Safety-native econ field-building is thin (early OpenPhil seeds: Trammell/GPI, Epoch; Coefficient Abundance & Growth adjacent). Pattern across both fields: safety community writes the gap into agendas, then broadcasts an RFP or waits for a mainstream patron. Economists got a patron; cryptographers have none yet (ARIA closest candidate).

**Bush playbook (distilled for the pitch):**
1. Pre-position before the ask (Carnegie Institution presidency, NACA chair — inside before asking).
2. One page, right intermediary (Hopkins), small ask: <15-min Oval Office meeting, "OK—FDR" in the margin (June 1940; NDRC formally June 27, 1940).
3. Move the money, not the scientists: NDRC's core innovation was contracts to universities/industrial labs, scientists stay in their institutions.
4. Recruit through peer elites, cascade down: Conant, Compton, Jewett, Tolman each recruited their networks.
5. Upgrade authority when it binds: EO 8807 → OSRD (June 28, 1941), own budget (~$536M total), development authority, direct presidential line; absorbed the moribund Briggs Uranium Committee as S-1.
6. Hand off at scale: March 1942 Bush memo → War Department/Groves for production ($400M estimate vs eventual ~$1.9B).

**Einstein letter (Aug 2, 1939 — session ran on its 87th anniversary):**
- Full text: https://en.wikisource.org/wiki/Albert_Einstein_to_Franklin_D._Roosevelt_-_August_2,_1939 (also atomicarchive.com/resources/documents/beginnings/einstein.html; scan in FDR Library PDF fdrlibrary.marist.edu/archives/pdfs/docsworldwar.pdf; drafting history at dannen.com/ae-fdr.html).
- The letter's recommendation #2 is literally "fund the relevant academics in place" (speed up experimental work via funds + industrial-lab cooperation). Opening exhibit for the pitch.
- What it actually produced: Briggs committee, $6,000, 18 months of dither. The prestige letter got a committee; the bomb required Bush's machinery.

**Pitch frame:** two-panel contrast. Panel 1: community already wrote its Einstein letter (CAIS extinction statement, May 2023 — same move, same result: attention then committees). Panel 2: nobody has done the Bush move; the activity is "pick the Conants" — 4-5 peer-credible academics per field, fund through them, contracts-in-hand push recruitment. Pre-empt: Bush had a war + emergency authority, and his contracting innovation is now the default (NSF descends from OSRD) — so the modern move is targeted commissioning + peer-cascade, executable by philanthropy without an emergency.

**Next:** draft the pitch doc (audience TBD: funder-facing memo vs. blog post vs. both); decide whether the SlopChecker/funder-screening thread (project files) connects; candidate "Conant list" per field.

Convo: `convos/20260802_academic_recruitment_landscape.md`.
