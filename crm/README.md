# Policy Levers — CRM

Lightweight YAML/markdown CRM for tracking congressional advocacy contacts,
visits, and follow-ups for the policy-levers project.

## Structure

```
crm/
├── README.md           — this file
├── contacts.yaml       — canonical contact records (named staff + front-desk)
├── senators.yaml       — senator-level metadata (committees, posture, framing)
├── bills.yaml          — bills tracked, including pushback playbooks
├── visits/
│   └── YYYY-MM-DD-<name>/
│       ├── summary.md      — narrative of the visit
│       ├── followups.yaml  — action queue with due dates
│       └── (other artifacts: photos of cards, leave-behinds, etc.)
└── templates/
    └── (email templates by frame, intro letters, etc.)
```

## Conventions

### Contact IDs
`{lastname}-{firstinitial}-{senator-or-office}`
Examples: `park-d-hawley`, `katz-m-heinrich`, `samantha-foster`

Stable IDs let `followups.yaml` reference contacts without duplicating data.

### Posture taxonomy (in `senators.yaml`)
- `ally` — already on the bill or aligned
- `probable_ally` — strong cosponsor candidate
- `receptive` — open to the message
- `warming` — building relationship
- `gatekeeper` — controls access (e.g., committee chair); win condition
  may be procedural not substantive
- `cold_but_relevant` — not engaged but office matters
- `china_lane_only` — engages only on China/national-security frame
- `aware_low_priority` — knows the space, low engagement value

### Framing taxonomy (in `senators.yaml`)
- `direct` — extinction language, full catastrophic framing OK
- `catastrophic_statutory` — use bill's "loss-of-control" terms; avoid
  raw "extinction" word
- `china_hawk` — route everything through PRC/adversary frame
- `jobs_only` — labor displacement angle; don't dilute with x-risk
- (other frames as discovered)

## Workflow

**Before a visit:**
1. Pull `senators.yaml` for the offices you're visiting; review `posture` and `framing`
2. Check `contacts.yaml` for prior named contacts at each office
3. Check `bills.yaml` for current pushback playbook on bills you're discussing

**During a visit:**
- Capture: name, title, office, email, phone of any staff who give cards
- Photograph leave-behinds and business cards
- Note front-desk warm contacts even without cards

**After a visit:**
1. Create `visits/YYYY-MM-DD-<name>/`
2. Write `summary.md` (narrative, lessons learned)
3. Write `followups.yaml` (action queue with `date_due`)
4. Update `contacts.yaml` with new entries
5. Update `senators.yaml` if posture/framing changed based on what was learned

## Why YAML not a SaaS CRM

- Plain text → version-controlled, diffable, durable
- Searchable with `grep`/`rg`
- Can be processed by scripts (build email queues, calendar reminders, etc.)
- No vendor lock-in, no subscription, no data leaving the repo
- Cost: requires discipline to maintain by hand or via tooling

## TODO
- Email templates by frame in `templates/`
- Script to generate "email this week" queue from all `followups.yaml`
- Script to surface stale contacts (no contact in N days)
