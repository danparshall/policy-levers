<!-- Generated during: convos/20260730_policy_actor_map.md -->

# Prior art: "Group X works on Problem Y via Approach Z" maps for AI policy

Scan run 2026-07-30 in response to Dan's question of whether such a page already exists.
Verdict: several partial maps, none in the Group x Problem x Approach shape. Each existing
map drops one of the three axes.

## Inventory

| Project | Axes covered | Scale / vintage | Notes |
|---|---|---|---|
| **AISafety.com/map** (`aisafety.com/map`) | Group + rough problem-area. No approach. | v2 relaunch of the 2023 "Map of AI Existential Safety"; 16 categories | Volunteer-maintained, additions via Discord. Strong on technical safety, thin on governance/policy. Entries are one-line descriptors. |
| **Mapping AI** (`aimapping.org`, Chaudhuri & Wang) | Group + stance. No problem, no approach. | ~1,800 people + orgs, US AI policy; launched ~May 2026 (Marketplace coverage) | Per-entry: regulatory stance, AGI timeline, funding model, network connections. Self-positions against aisafety.com as "safety ecosystem only". **This is the live competitor for a general-purpose map.** |
| **AI Stance Directory** (Severin Sorensen, Feb 2026) | Group + stance. | 45+ actors, 6 categories | Categories: Safety-First / Balanced-Risk-Based / Accelerationist / Labor-Worker-Centered / Strategic Opportunist / International Governance. Has a movement-trajectory column tracking drift over time. |
| **A Guide to the AI Tribes** (Michel Justen) | Ideological taxonomy only. | n/a | Cited by Mapping AI as the reference taxonomy for camps. |
| **AGORA / CSET + MIT AI Risk Initiative** | Document + risk taxonomy. No actors-as-agents. | 1,000+ governance documents; April 2026 update | Taxonomies cover risks, actors, sectors, AI lifecycle stages, legislative status, technical scope. Most methodologically rigorous thing in the space, but it maps *documents*, not organizational agendas. |
| **IAPS, "Mapping Technical Safety Research at AI Companies"** (arXiv 2409.07878) | Problem + approach + group, but narrow. | 80 papers, 3 companies (Anthropic/GDM/OpenAI), Jan 2022 - Jul 2024 | **Closest match to the target schema.** 9 approach categories + 2 nascent ones. Used for gap-finding: model organisms of misalignment, multi-agent safety, safety-by-design flagged as under-served and unlikely to become better-incentivized. Technical only; stale cutoff. |
| **EA Forum, "A map of work needed to achieve safe AI"** | Work-type map. | 2025 | Bird's-eye view of work categories, not an actor index. |
| Assorted directories (`aisecurityandsafety.org` ~180 orgs / 7 categories; MindXO Atlas ~50 orgs / 12 countries) | Group + category. | 2026 | Treat as SEO artifacts until verified. Not checked. |

## Where the gap actually is

The Group x Problem x Approach cell is empty. But emptiness alone isn't the argument for filling it.
Two objections raised in session, both survivable but both design constraints:

1. **"Approach Z" has no consensus vocabulary.** IAPS had to synthesize at least seven prior
   agendas/taxonomies (Hendrycks, Open Phil, Critch & Krueger, Ji, Anwar, Toner & Acharya, Amodei)
   into 11 categories, and practitioners still disputed the resulting labels, including from inside
   the labs being categorized. That's the *technical* side where vocabulary is comparatively mature.
   On governance it's worse: "transparency", "evals", "compute governance", "liability" each mean
   several things. Borrow a taxonomy and inherit its blind spots; build one and own a definitional
   fight. Mitigation: scope narrowly enough that every category is defensible from primary text.

2. **Maintenance is the project, and the failure is silent.** Every map above is a snapshot with a
   decay half-life in months; a stale map launders obsolete information as current. Survivors have
   either institutional funding (CSET/MIT) or a volunteer community with a recruiting function
   attached (aisafety.com). Canary has neither. If the honest answer to "what keeps this alive at
   month nine" is "Dan, manually," build something smaller than a webpage.

Corollary: entering as a general-purpose map against Mapping AI (1,800 entries, press coverage,
launched May 2026) is a losing fight. A differentiated slice isn't.

## Consumer fork (unresolved)

The design forks hard on who the page is for:

- **Hill staffer** — doesn't want a map, wants a routing table ("who do I call about compute
  thresholds, and are they credible"). Requires a credibility signal that may not be publishable.
- **Funder / field-builder** — wants the IAPS output: gap analysis, "nobody is working on X".
  Coverage completeness matters, which is expensive.
- **Canary, for coalition-building** — a *public* map does something the private `crm/` can't:
  it's a legible artifact people want to appear on, which converts maintenance from cost into
  inbound. Under this framing completeness matters far less than being the map people want to be
  listed in.

Claude's read: the third is most aligned with Canary's purpose, and it suggests inverting the
schema — index on the problem and the lever, with groups as leaves, rather than on the group.
Which is how this repo is already organized.
