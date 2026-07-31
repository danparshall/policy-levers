# SlopChecker: Prior-Art & Landscape Report for Funder-Side Submission Screening

**Date:** 2026-07-31
**Provenance:** Deep-research run 2 for the FAI+IFP hackathon. Run 1 targeted the WRONG feature list (bill pipeline / claim-audit / Kent-o-meter, reconstructed from the morning brainstorm because the agent couldn't open the team Google Doc); this run used the actual doc contents ("slopchecker ideation," pasted by Dan) plus his clarifications (IFP tool is private; Pangram locked in; Candid + redacted partner proposals as similarity corpus). Companion convo: `convos/20260731_hackathon_brainstorm.md`.

---

## TL;DR
- **Most of SlopChecker's feature list is already solved or half-solved by existing, wireable open-source components** — DOI/metadata checks (Crossref), reference extraction (GROBID/AnyStyle), citation-hallucination detection (Hallucinator, CiteTracer, GPTZero's Hallucination Check), claim decomposition (VeriScore/FActScore, both MIT), text-similarity/dedup (datasketch MinHash + FAISS embeddings), classification (Candid's CC-BY PCS taxonomy + zero-shot), and in-line HTML annotation (Recogito, BSD-3). Pangram supplies AI-text detection via a clean paid API.
- **The genuinely open gaps — and thus the strongest pitch — are integration and domain-fit, not new algorithms:** no open-source tool today packages funder-side screening of *grant applications / blog posts / think-tank reports* into one pipeline that (a) separates cheap deterministic checks from expensive LLM checks, (b) ties each finding to an in-line span annotation, and (c) does claim↔citation *entailment* (ladder level d), which remains research-grade and unsolved in production. Solicitation-compliance and budget-feasibility checking are also open (only closed GovCon products exist).
- **Recommended one-day build:** ship the deterministic tier first (Crossref DOI resolution + GROBID reference parsing + PCS zero-shot tagging + MinHash near-dup against a Candid grants corpus + budget sanity heuristics), render results with Recogito span highlighting, then layer the expensive tier (Pangram API for AI detection; an LLM-based claim-extraction + citation-entailment pass borrowing VeriScore's MIT extractor). Treat Pangram and all detectors as **triage signals, never automated verdicts.**

## Key Findings

**1. Pangram (locked-in AI detector) is production-grade, cheap enough, and has a clean API — but its terms do not explicitly bless funder-side screening, and independent evidence says treat it as triage, not evidence.** Pangram 4 launched July 29, 2026; the API is $0.05 per 100 words (a 2–10× increase over Pangram 3's $0.05/1,000 words), 5 QPS realtime, 20% bulk discount, Python SDK with a one-line `predict()` call, sentence-level windows in the JSON response. The strongest independent evidence is Jabarian & Imas, "Artificial Writing and Automated Detection," University of Chicago Booth/BFI Working Paper 2025-116 (also NBER WP No. 34223, Aug 26 2025), which tested detectors on 1,992 pre-2020 human texts plus 1,992 AI texts across four frontier LLMs and concluded: "we show that Pangram is the only detector that meets a stringent policy cap (FPR ≤ 0.005) without compromising the ability to accurately detect AI text." Pangram itself advertises an "industry-leading 1 in 10,000 false positive rate." But its self-reported Pangram 4 figures ("over 99% accurate at finding AI-assisted writing and mixed human-AI content") are vendor claims distinct from the independent Booth FPR result, and other reviews put accuracy on *AI-edited* (human draft, LLM-polished) text near 73%. Critics (the RAID benchmark; WSJ reporting) stress that even a tiny per-document error rate produces many false accusations at scale. Pangram's ToS (last updated Aug 14, 2025) treats submissions generically as "User Content" (§8.1), neither explicitly permitting nor prohibiting third-party-authored content; it contains **no** clause banning automated adverse decisions and **no** data-retention/training clause (both deferred to the Privacy Policy). Zero-data-retention is an enterprise option. Pangram raised $9M led by Menlo Ventures on July 29, 2026 (with Haystack, ScOp, Script Capital, Cadenza), bringing its total to roughly $13M.

**2. Citation checking is a 4-level ladder; levels (a)-(c) are solved with free tools, level (d) is not.**
- **(a) Valid format / DOI resolves:** Solved. The Crossref REST API is free, needs no signup, indexes ~183M works, resolves DOIs and returns metadata; an HTTP HEAD request gives fast existence checks (200/404). DataCite covers datasets. Pure deterministic-tier work.
- **(b) Source matches what is cited (author/title):** Solved. GROBID (Apache-2.0, ~0.87–0.90 F1 on reference parsing) and AnyStyle extract structured references from PDFs; match against Crossref metadata.
- **(c) Quote exists in the paper:** Partially solved. Requires fetching the cited full text (often paywalled) then string/fuzzy matching — feasible only for open-access targets.
- **(d) Reference actually supports the citing claim:** NOT solved in production. This is citation-entailment / claim-citation accuracy, an active 2024-2026 research area (CiteCheck, CiteTracer, RefChecker). Genuinely open contribution opportunity.

**3. Whole hallucinated-citation detectors already exist as open source and as commercial features.** `gianlucasb/hallucinator` (open source) validates references against Crossref/arXiv/DBLP/OpenAlex. Academic systems CiteTracer (`github.com/aaFrostnova/CiteTracer`, code released, 97.1% accuracy on its synthetic benchmark) and CiteCheck are recent. GPTZero's Hallucination Check scanned 4,841 of the 5,290 accepted NeurIPS 2025 papers and confirmed 100 hallucinated citations across 51 papers (some write-ups say 53; GPTZero's own figure is 51), and GPTZero says it is now coordinating with ICLR. A July 2026 arXiv survey ("Detecting Hallucinated and Suspicious Citations," arXiv 2607.22693) explicitly notes that general AI-text detectors like Pangram are *not* suitable for citation-hallucination detection because they do not verify whether references exist or whether their metadata are correct — validating SlopChecker's decision to build citation checks *separately* from Pangram.

**4. Claim extraction is solved with reusable MIT-licensed modules.** VeriScore (MIT, standalone `python3 -m veriscore.extract_claims`), FActScore (MIT, `factscore/atomic_facts.py`), and Loki/OpenFactVerification (MIT, five-step pipeline that starts by breaking long texts into individual claims) all expose standalone claim-extraction stages. ClaimBuster's hosted API is live (`https://idir.uta.edu/claimbuster/api/v2/score/text/…`, requires an `x-api-key`) but its ClaimSpotter code is **GPL-3.0** — usable via API, but do not vendor the code into an MIT/Apache deliverable.

**5. Proposal-similarity infrastructure is mature and free, but the Candid corpus is metadata + short grant *descriptions*, not full proposal text.** datasketch (MinHash/LSH), FAISS, and sentence-embeddings give scalable near-dup and semantic similarity. Candid's grants data is coded to PCS and includes a `grant description` field, but government-990-sourced grants have limited descriptive text; richer text exists only where funders report directly. So Candid is a good *stand-in corpus for tagging and coarse similarity* but a weak proxy for full-text proposal dedup — the redacted partner proposals matter more for that.

**6. Topic/submitter tagging has a purpose-built, openly licensed taxonomy.** Candid's Philanthropy Classification System (PCS) is now **CC BY 4.0** — per Candid, "By removing the 'non-commercial' restriction, we're making the taxonomy available for all to use." It is downloadable and machine-actionable (most recent update November 2024); pair it with off-the-shelf zero-shot classification. This is the single best domain-fit asset for the tagging feature.

**7. Auto due-diligence on submitting orgs is well-served by charity/OSINT APIs.** Candid/GuideStar Charity Check API, Charity Navigator API, ProPublica Nonprofit Explorer (free, 1.8M orgs), IRS BMF, and CharityAPI.org (from $15/mo) give tax status, 990 financials, OFAC flags. An LLM "deep research" wrapper on top is the novel glue.

**8. Solicitation-compliance and budget-feasibility tooling is entirely commercial GovCon (no open source).** GovDash, GovEagle, Vultron, Rohirrim, and VisibleThread "shred" RFPs into compliance matrices (Section L↔M mapping); this is a proprietary market with no open-source equivalent. NOFO/solicitation parsing for the philanthropy context is an open gap. Budget cost-realism analysis exists only inside these closed GovCon suites.

**9. The output layer (in-line HTML annotation) is solved by mature open-source JS libraries.** Recogito text-annotator (BSD-3), AnnotatorJS, and Hypothesis/PDF.js render per-span highlights with metadata bodies — ideal for attaching evidence (unresolved DOI, detection score) to exact character ranges.

**10. Funder/journal/conference screening precedents are well-documented and worth citing in the pitch.** The STM Integrity Hub is the closest analog: per Science Editor (CSE, Dec 2025), 40 publishers now rely on the STM Integrity Hub to screen over 125,000 papers monthly, intercepting approximately 1,000 suspected paper-mill submissions each month, through integrations with 7 editorial systems; it integrates ~15 independent tools (Clear Skies' Papermill Alarm, PubPeer, duplicate-submission checks, tortured-phrase and AI-text detection) and launched May 2022. arXiv's 2026 one-year-ban policy for unchecked AI content, and NIH's ban on AI-"substantially developed" applications (Notice NOT-OD-25-132, released July 17 2025, effective Sept 25 2025, plus a six-application/PI/year cap — prompted after some PIs submitted more than 40 distinct applications in a single round), establish that funders and repositories are actively building exactly this class of screening.

## Details

### Feature-by-feature analysis (in doc order)

**Feature: Open source.** The deliverable must be open source. Watch license compatibility: GROBID (Apache-2.0), Recogito (BSD-3), datasketch (MIT), FAISS (MIT), VeriScore/FActScore/Loki (MIT), Candid PCS (CC BY 4.0) are all permissive and MIT/Apache-compatible. Avoid vendoring GPL-3.0 code (ClaimBuster's ClaimSpotter) — call it via its API instead, or use an MIT alternative. Pangram is a paid SaaS dependency, not code, so it does not affect your license.

**Feature: Pangram checks through API (AI detection).**
- *What it does:* Detects AI-generated / AI-assisted / human text with sentence-level `windows` (label, score, char range), fractions, and a dashboard link. Python SDK; realtime (5 QPS) and bulk modes.
- *Pricing:* $0.05/100 words (Pangram 4); 20% bulk discount; noncommercial academic credits may be available. A ~2,000-word proposal ≈ $1.00 at Pangram 4 rates.
- *Maturity:* Production; SOC 2 Type 2; used by Substack, Quora, NewsGuard. Raised $9M led by Menlo Ventures (July 29, 2026).
- *Accuracy/criticism:* Near-zero FPR independently confirmed (UChicago Booth / BFI WP 2025-116); ~73% on AI-*edited* text; reruns can differ; dangerous as evidence. Treat as one signal.
- *ToS caveat for funder screening:* No explicit permission or prohibition for third-party-authored content; no ban on automated adverse decisions; retention/training deferred to Privacy Policy. **Recommend enterprise zero-data-retention and a human-in-the-loop policy.**
- *Integrability:* Trivial (one day) — `pip install pangram`, one `predict()` call. This is the expensive tier.
- *Alternatives (short):* GPTZero (has Hallucination Check; more generous free tier; ~$0.15/1K words), Originality.ai (cheapest, ~$0.01/1K words, higher FPR), Copyleaks, Sapling, and open-source RoBERTa-based detectors (fail badly under low-FPR caps). Pangram is the right primary.

**Feature: Citation checker (4-level ladder).**
- *Level a (DOI resolves / valid format):* Crossref REST API (free, no key; "polite pool" with mailto recommended; rate limits revised Dec 1 2025). DataCite for datasets. Deterministic tier. One-day-doable.
- *Level b (metadata match):* GROBID (self-host via Docker; Apache-2.0) or AnyStyle for reference extraction → match author/title/year to Crossref. Deterministic-ish. Doable but GROBID setup eats time; consider AnyStyle or Crossref reference-matching for speed.
- *Level c (quote exists):* Fetch open-access full text (Unpaywall/OpenAlex) → fuzzy string match. Partial; paywalls block it.
- *Level d (reference supports claim):* Research-grade only. Borrow CiteCheck/CiteTracer/RefChecker approaches or an LLM entailment prompt. Expensive tier; the novel contribution.
- *Ready-made whole tools:* `gianlucasb/hallucinator` (open source, multi-database), CiteTracer (`github.com/aaFrostnova/CiteTracer`), GPTZero Hallucination Check (commercial). Scite.ai gives citation-context classification (supporting/contrasting/mentioning) via API (from ~$250/mo) — useful for level d but paid.

**Feature: Extract core claims.** Use VeriScore's MIT extractor or FActScore's `atomic_facts.py` (MIT), or Loki (MIT). All wrap an LLM for decomposition. One-day-doable via an LLM prompt if you don't want the full dependency. Expensive tier (LLM calls).

**Feature: Compute similarity to existing proposals / reviewer pool.** datasketch (MinHash/LSH, MIT) for lexical near-dup; sentence-embeddings + FAISS (MIT) for semantic similarity; Pinecone/Milvus if you want a hosted vector DB. Reviewer-matching prior art: Toronto Paper Matching System (TPMS) and OpenReview's built-in matcher, plus the ACL reviewer-paper-matching open-source code (`github.com/acl-org/reviewer-paper-matching`). Corpus caveat: Candid gives metadata + short descriptions, not full proposals — good for tagging/coarse similarity, weak for full-text dedup. Deterministic tier (MinHash) + optional embedding tier.

**Feature: Tag topics / submitter type.** Candid PCS (CC BY 4.0) taxonomy + zero-shot classification (e.g., an NLI model or LLM). Candid's own autocoder demonstrates the approach. Best domain-fit asset in the whole project. One-day-doable.

**Feature: Auto deep-research due-diligence reports.** Compose from ProPublica Nonprofit Explorer (free), Candid/GuideStar Charity Check API, Charity Navigator API, IRS BMF, OFAC — wrap with an LLM "deep research" agent. No open-source end-to-end grantee-DD tool exists; the orchestration is novel glue. Expensive tier.

**Feature: Solicitation compliance.** No open source. Commercial GovCon only (GovDash, GovEagle, Vultron, Rohirrim, VisibleThread). Approach: LLM parses the solicitation into a requirements checklist, then checks the submission against it. Open gap → novel contribution. Expensive tier.

**Feature: Budget feasibility.** No open source; exists only inside closed GovCon "cost-realism" tooling. Approach: extract budget lines, sanity-check against heuristics/benchmarks (e.g., salary ranges, indirect-cost caps). Open gap → novel contribution.

**Feature: Document types (grant apps, blog posts, think-tank reports).** No single tool spans these; PDFs need GROBID/pdfplumber, HTML/blogs need readability extraction. Ingestion normalization is unglamorous but necessary day-one work.

**Feature: Output — evidence report + deterministic/expensive tiering + in-line HTML annotation.** Recogito text-annotator (BSD-3) or AnnotatorJS for span highlights; render a JSON evidence object (DOIs that don't resolve, detection scores, dup matches) and map findings to character ranges. The doc's own deterministic-vs-expensive split is exactly right and maps cleanly onto the tools above. One-day-doable for a demo.

### Adjacent-community precedents (category validation for the pitch)
- **Academic publishing:** STM Integrity Hub (modular, 40 publishers, >125k papers/month, ~1,000 paper-mill interceptions/month, ~15 tools, 7 editorial-system integrations), Clear Skies Papermill Alarm (traffic-light), Wiley Papermill Detection, iThenticate/Turnitin (plagiarism + AI), STM's tortured-phrase and duplicate-submission checkers. These prove the modular-signals architecture SlopChecker should copy.
- **Conferences/peer review:** OpenReview matcher, TPMS, ICML/NeurIPS LLM policies; GPTZero's NeurIPS 2025 citation audit.
- **Government grants:** NIH ban on AI-substantially-developed applications (NOT-OD-25-132, effective Sept 25 2025) + 6-app/PI/year cap; NSF disclosure requirement + reviewer AI prohibition; ARPA-H IGoR AI-review pilot.
- **GovCon:** RFP "shredding" / compliance-matrix tools (commercial only).

## Recommendations

**Stage 1 — Deterministic tier (build first; highest reliability, lowest cost, most demo-credible):**
1. Ingestion: pdfplumber/GROBID for PDFs, readability for blogs.
2. DOI/reference checks: GROBID/AnyStyle extraction → Crossref resolution (levels a & b). This alone produces the headline "N DOIs don't resolve" metric.
3. Tagging: Candid PCS (CC BY) + zero-shot classifier.
4. Similarity: datasketch MinHash against a Candid grants corpus + any redacted partner proposals.
5. Budget + solicitation compliance: rule/heuristic checklists (deterministic subset).
6. Output: Recogito span annotations + JSON evidence report.

**Stage 2 — Expensive tier (layer once deterministic works):**
1. Pangram API for AI detection (enterprise zero-retention; human-in-the-loop).
2. Claim extraction (VeriScore MIT module) + citation-entailment (level d) via LLM — flag as experimental.
3. LLM due-diligence agent over ProPublica/GuideStar/OFAC.

**Positioning the pitch:** Lead with the genuine gaps — (i) an *integrated, open-source, funder-tuned* pipeline (nothing open spans grant apps + blogs + reports with tiered checks and span-level evidence); (ii) *claim↔citation entailment* (level d), which even the research tools only partially solve; and (iii) open-source *solicitation-compliance* and *budget-feasibility* checking, which today exist only as closed GovCon products. Cite the STM Integrity Hub as the proven modular analog and NIH/arXiv policies as the demand signal.

**Thresholds that change the plan:** If redacted partner proposals arrive in usable volume, prioritize embedding+FAISS semantic dedup over MinHash. If Pangram enterprise zero-retention or third-party-content permission can't be confirmed, keep AI detection strictly advisory and consider GPTZero (whose Hallucination Check doubles as a citation checker). If GROBID setup stalls the day, fall back to AnyStyle or Crossref's reference matcher.

## Caveats
- **AI detectors are triage, not proof.** Pangram's own ToS disclaims individual-prediction accuracy; independent work shows AI-edited-text weakness and rerun instability. Never auto-reject on a detector score; always human-in-the-loop. This is both an ethics and a reputational-risk point (the doc's stated concern).
- **License hygiene:** ClaimBuster ClaimSpotter is GPL-3.0 — API-only. Verify the Meta `ScalableVeriScore` fork's license before use. Everything else recommended is MIT/Apache/BSD/CC-BY.
- **Candid corpus limits:** metadata + short descriptions, not full proposal text; government-sourced grants have sparse text. Access/licensing/cost for bulk Candid data beyond the free academic subset needs confirming with Candid sales.
- **Pangram data governance:** retention/training terms live in the Privacy Policy (not the ToS) and were not fully verified; confirm before sending real applicant text.
- **Fast-moving space:** citation-hallucination detection papers (CiteCheck, CiteTracer, the July 2026 survey) are weeks-to-months old; expect churn. Some review-site figures (pricing, accuracy) are secondary sources and should be re-verified against primary docs before the pitch. The NeurIPS-2025 hallucination count appears as both "51" (GPTZero's own) and "53" (secondary write-ups).
- **IFP's internal tool** remains private; no public traces were found beyond the design doc's reference to it. STM Integrity Hub is the best public analog.
