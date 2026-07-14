# Handoff — Obernolte / Trahan "Great American AI Act" ingest

**Written:** 2026-07-14 by prior session, on branch `main`, working tree clean (last commit `75a36e6` pushed).

## What Dan asked for

> "Let's discuss Obernolte-Trahan bill. Probably need to download it, then break it into chunks and add. Should be a dedicated folder probably."

Then handed over three URLs. Then stopped the prior session and asked for a handoff to a YOLO-mode agent.

## The bill (confirmed identity)

- **Name:** Great American AI Act (GAAIA) — *discussion draft*, not yet formally introduced
- **Released:** 2026-06-04
- **Lead sponsors:** Rep. Lori Trahan (D-MA-03) and Rep. Jay Obernolte (R-CA-23) — both on House Energy & Commerce
- **Co-releasers:** Reps. Suhas Subramanyam (D-VA-10), Scott Franklin (R-FL-18), Scott Peters (D-CA-50), Erin Houchin (R-IN-09)
- **Feedback address:** GAAIA@mail.house.gov (public comment period; no formal deadline mentioned in the release)
- **Length:** **269 pages**, Word-produced PDF (Microsoft Word, 2026-06-02 authored)
- **Framing** (from PR quotes): bipartisan federal framework, protect workers + national security + safety, pre-empt "patchwork of fifty state laws" (Houchin), "clear rules of the road" (Franklin), builds on House bipartisan AI Task Force
- **Committee path:** Energy & Commerce (all six sponsors sit there)

## What's already on disk

All under `/tmp/obernolte-trahan/` — **not yet moved into the repo**:

| file | what it is | size / lines |
|---|---|---|
| `great_american_ai_act_discussion_draft.pdf` | The bill itself, downloaded from trahan.house.gov | 2.1 MB, 269 pp |
| `great_american_ai_act.txt` | `pdftotext -layout` extraction of the bill | 8,948 lines |
| `press_release.html` | Raw press release (`DocumentID=3783`) | 35 KB |
| `press_release.txt` | Cleaned press-release text | 59 lines |
| `extract_pr.py` | The extractor for the press release (throwaway) | — |

**Two adjacent docs Dan did NOT link but are cited in the press release** — still need to fetch:

1. **Section-by-section summary:** `https://trahan.house.gov/uploadedfiles/gaaia_discussion_draft_section-by-section.pdf`
2. **FAQ from Trahan's office:** `https://trahan.house.gov/uploadedfiles/2026.06.03_trahan_obernolte_ai_framework_faq.pdf`

Both will be small; grab them the same way (`curl -sSL -A 'Mozilla/5.0' -o <path> <url>` — plain WebFetch got a 403 from trahan.house.gov).

## Decisions the prior session raised but Dan did NOT resolve

The prior session pushed back on the chunking premise and asked four questions. Dan responded only by dropping URLs — he did not answer these:

1. **Folder location.** Prior session proposed `bills/obernolte-trahan/` at top level (parallel to `papers/`, `essays/`, `crm/`). Alternatives considered: `crm/bills/…` (awkward tenant), `data/reference/bills/…` (wrong shelf — bill text isn't lookup data). **Recommend `bills/obernolte-trahan/` unless Dan objects; ask before creating.**
2. **Chunking approach.** The 269-page length settles the *whether* — chunk it. But *by what unit* is still open: (a) by title/subtitle/section as the bill itself is structured (natural for citation, `bills/obernolte-trahan/sec-XYZ.md`); (b) by fixed page ranges (bad — arbitrary boundaries); (c) whole text plus a section index (light-touch). **Recommend (a) — one file per top-level section, mirroring the bill's own §/Title structure — because it gives us stable citation targets for essays and leave-behinds.** Confirm with Dan.
3. **Output purpose.** Not stated. Options Dan mentioned in earlier turns of the broader project: Hill leave-behind, public Canary essay, private MATS-adjacent analysis. Ask what he's producing — it affects how much annotation scaffolding to build.
4. **Discussion-draft status.** The bill isn't formally introduced yet, so it has no `S.####`/`H.R.####` number. `crm/bills.yaml` (see AIRE Act entry) keys on bill number. Options for the yaml stub: use a placeholder key like `gaaia_draft_2026_06`, or wait until formal intro. Ask.

## Repo conventions the next session needs to know

- **Naming:** kebab-case for non-code files/dirs (spelled out in `/Users/dan/code/policy-levers/CLAUDE.md` under "File and directory naming"). So `bills/obernolte-trahan/`, not `bills/Obernolte_Trahan/`. Section files: `sec-101-definitions.md` style.
- **`crm/bills.yaml` is the existing metadata pattern** — see the `s2938` entry for shape (sponsor, cosponsors_at_intro, referred_to, status, text_url, summary, key_features, framing_assets, common_pushbacks). Add a GAAIA entry once folder is created; even without a bill number the fields are useful.
- **Nori workflow says:** research-shaped work goes in `docs/active/<branch>/`. If Dan wants the *analysis* of the bill to be a research line (not just archival storage of the text), the analysis material belongs in `docs/active/gaaia-analysis/` or similar, with the raw bill text and chunks in `bills/obernolte-trahan/`. **Storage ≠ research line — don't conflate.**
- **YAGNI applies.** Don't over-engineer. If Dan just wants the text present + section-navigable, don't build a whole annotation scaffold speculatively.
- **CLAUDE.md's honesty norms:** push back on requests that don't hold up. Prior session pushed back on chunking-for-LLM-context (weak in 2026); it's fine to push back further if a proposal seems off.

## Suggested first actions for the YOLO-mode agent

1. Read this file, `STATUS.md`, and `crm/bills.yaml` (`s2938` entry) if you haven't.
2. Grab the two missing PDFs (section-by-section, FAQ) to `/tmp/obernolte-trahan/`. Extract text from both with `pdftotext -layout`.
3. **Ask Dan the four unanswered questions above** before creating the folder or splitting the text. Do NOT assume answers.
4. Once answered: create `bills/obernolte-trahan/` (or whatever Dan picks), move the PDF + extracted text in, chunk per the agreed unit, add a `README.md` in the folder explaining what's there and pointing to the section-by-section summary.
5. Add a `gaaia_draft_2026_06` entry to `crm/bills.yaml` per that file's schema (sponsors, cosponsors, status: `discussion_draft`, text_url, comment address).
6. Commit. Push.

## Unrelated: pending item Dan should see

The prior session's SessionStart flagged **1 unacknowledged `claude-exit` invocation since 2026-07-12**. Prior session mentioned it once; Dan hasn't acted. When there's a natural pause, remind him to run `claude-exit log`.

## Things NOT to do

- Do **not** delete or modify anything under `/tmp/obernolte-trahan/` without moving it into the repo first — those are the only downloaded copies right now.
- Do **not** commit the raw PDF blob without checking `.gitignore` first (this repo git-ignores large data files by policy; a 2.1 MB bill PDF is a judgment call — Dan may want it in `papers/` conventions or as a tracked exception). Ask.
- Do **not** merge to main outside a normal push — this session is already on main and pushing directly is fine, but no rebasing/force-pushing.
- Do **not** create a worktree unless Dan asks. Prior session did all this work directly on `main`; per CLAUDE.md, "Often this repo is documentation and notes, for which you don't need to create a separate worktree."
