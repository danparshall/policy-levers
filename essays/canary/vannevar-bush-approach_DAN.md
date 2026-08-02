Industrializing a small field: Lessons from Vannevar, for the AI Safety field

AI Safety needs to quickly transform from a "community" to an "industry"; the Manhattan Project is a good example!

---

Many folks know about the "Einstein letter" which was dated 87 years ago today.  As legend has it, this led to the formation of the Manhattan Project.  But actually this is only half the story: the original forays were plagued by institutional apathy, with multiple occasions when key scientific reports just didn't move.  

In one famed instance, the Brits realized that the bomb would only require a few kilograms of uranium (instead of tons from earlier estimates), and sent a report to the head of the American uranium committee... who put it in his safe and didn't tell a soul.  Eventually Mark Oliphant realized "somebody has to, and no one else will", so he got on a military transport plane heading to the states, and started personally pounding on doors until the analysis got the attention it needed.

What probably was the biggest unlocking of the whole wartime research effort was Vannevar Bush walking into FDR's office to gain the institutional authority (and money), and then personally recruiting a handful of academics to mobilize the rest of the physicists into working on key problems (of which the Manhattan Project was ultimately the most significant).

I bring this up because from what I've found, the AI Safety community hasn't done a lot of active recruitment of senior key personnel.  As just one example, I'm reviewing materials related to the [FASR](https://www.securefrontier.ai/) program today, and while the community has adopted the "covert adversary" framework wholesale, I can't find any public indication that any of the AI Safety funders have gone to Aumann or Lindell and said "hey, you know that great paper y'all wrote?  Could you take this pile of money and do some more?"  (The UK's Alignment Project does fund cryptographers, but for watermarks and backdoors, not verification.)

I suggest that folks worried about AI Safety should change from a "pull" mindset of "Fill out a grant application on our website", to a "push" mindset of "we know we need more of X, let's find folks working on closely-related Y and see what they need to pivot".  We do have RFPs, but it looks like there's a terrible lack of active recruitment.

To their credit, it looks like Palisade has been doing great work in the past year with making AI timelines legible to policymakers (dare I say that there's an Oliphant loose among the China hawks?).  But we need folks doing the same thing on the academic side, and right now it looks like we're recruiting individual residents for small programs, instead of showing up with grants and getting entire CS research groups to change their focus.

---

## Footnote candidates (Claude-compiled 2026-08-02; wire in and delete this header)

**Einstein letter (dated Aug 2, 1939).** Full text: Wikisource, "Albert Einstein to Franklin D. Roosevelt - August 2, 1939" (en.wikisource.org/wiki/Albert_Einstein_to_Franklin_D._Roosevelt_-_August_2,_1939). Scan: FDR Presidential Library, fdrlibrary.marist.edu/archives/pdfs/docsworldwar.pdf. Drafting history (Aug 2 = date Szilard mailed drafts to Einstein; Sachs delivered to FDR Oct 11, 1939): dannen.com/ae-fdr.html.

**Briggs committee + the $6,000.** Advisory Committee on Uranium established Oct 1939, absorbed into NDRC as the Committee on Uranium July 2, 1940, redesignated Section S-1 under OSRD 1941: AIP archives catalog, history.aip.org/history/catalog/icos/769.html. The $6,000 for graphite and the committee's slow pace: Atomic Heritage Foundation, "Early Government Support - 1939," ahf.nuclearmuseum.org/ahf/history/early-government-support-1939/; official account in the Smyth Report, ch. III, atomicarchive.com/resources/documents/smyth-report/smyth_iii.html.

**Kilograms not tons.** Frisch-Peierls memorandum, March 1940 (critical mass ~1 lb of pure U-235, vs. tons of natural uranium in prior thinking): text at atomicarchive.com/resources/documents/beginnings/frisch-peierls.html. Refined by the MAUD Report, July 1941 (~10 kg, bomb feasible in ~2 years): atomicarchive.com/resources/documents/beginnings/maud.html.

**The safe + Oliphant.** Richard Rhodes, *The Making of the Atomic Bomb* (1986), p. 372: Briggs "had put the reports in his safe and had not shown them to members of his committee"; Oliphant's August 1941 flight, his visits to Briggs, Lawrence, and onward to Conant and Bush: same, pp. 372-374; summarized with the Rhodes quote at Atomic Heritage Foundation, "The S-1 Committee," ahf.nuclearmuseum.org/ahf/history/s-1-committee/.

**Bush's one-page meeting with FDR.** G. Pascal Zachary, *Endless Frontier: Vannevar Bush, Engineer of the American Century* (1997), pp. 114-115 (meeting under 15 minutes, via Harry Hopkins); Irvin Stewart, *Organizing Scientific Research for War* (1948), p. 6 ("OK - FDR" on the single sheet). Stewart was OSRD's executive secretary; his book is the official administrative history and the primary source for most NDRC/OSRD mechanics.

**The four recruits.** Bush appointed Karl T. Compton (president of MIT), James B. Conant (president of Harvard), Frank B. Jewett (president of the National Academy of Sciences and chairman of the board of Bell Labs), and Richard C. Tolman (dean of the Caltech graduate school); Rear Adm. Harold G. Bowen and Brig. Gen. George V. Strong represented the military, Conway P. Coe the Patent Office. NDRC formally established by Council of National Defense order June 27, 1940, running initially on the president's emergency fund. See Wikipedia "Vannevar Bush" (well-cited to Zachary and Stewart); full roster at Library of Congress OSRD collection guide, guides.loc.gov/technical-reports/osrd; scholarly account incl. the Hopkins route and the contracting authority in the NDRC draft charter: *The Academy in World War II*, NAS history, ncbi.nlm.nih.gov/books/NBK217891/. Division assignments (Stewart 1948): Tolman armor/ordnance (Div. A), Conant bombs/chemistry (Div. B), Jewett communications (Div. C), Compton detection/radar (Div. D). NOTE: New World Encyclopedia swaps Jewett/Tolman assignments; it is wrong, follow Stewart.

**Contracts-to-universities as the core innovation.** NDRC "introduced the use of government contracts with universities and industrial laboratories... an approach that kept scientists in their own institutions rather than conscripting them into government service": Wikipedia "National Defense Research Committee," cited to Stewart 1948 and James Phinney Baxter III, *Scientists Against Time* (1946, the Pulitzer-winning official history).

**Covert adversaries.** Y. Aumann & Y. Lindell, "Security Against Covert Adversaries: Efficient Protocols for Realistic Adversaries," *Journal of Cryptology* 23(2):281-343 (2010), doi:10.1007/s00145-009-9040-7; extended abstract in TCC 2007, LNCS 4392.

**Adoption by the AI-verification literature.** N. Cankaya, "Bit-Exact AI Inference Verification Without Performance Tradeoffs," arXiv:2606.00279 (2026) - opens by defining the governance threat model as "the covert adversary (Aumann & Lindell, 2010)"; B. Harack et al., "Verification for International AI Governance," Oxford Martin AI Governance Initiative (2025), aigi.ox.ac.uk/publications/verification-for-international-ai-governance/; Y. Shavit, "What does it take to catch a Chinchilla?," arXiv:2303.11341 (2023).

**FASR.** Frontier AI Security Residency, securefrontier.ai.

**Palisade in DC.** "Help keep AI under human control: 2026 fundraiser," palisaderesearch.org/blog/ai-control-palisade-2026 - Kasten leading the full-time DC presence; relaying METR's time-horizon results to officials.

**UK Alignment Project funds cryptographers (for other problems).** The Alignment Project (UK AISI et al.), grants list at alignmentproject.aisi.gov.uk - Vaikuntanathan (MIT), Zamir (Tel Aviv), Guruswami (Berkeley), on cryptographic-hardness/backdoor/watermark projects.
