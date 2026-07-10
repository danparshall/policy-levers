# WAMI to satellite: TEL tracking literature (2026-07-10 session)

Feed for Q1 (AI/nuclear stability), targeting-channel-erosion spine. Started from Dan's question about the Iraq "rewind the tape" drone system; ended at the public literature on whether persistent overhead sensing can kill shoot-and-scoot.

## The WAMI lineage (confirmed, with corrections)

- Concept: Wide-Area Motion Imagery. Gigapixel-class staring sensor over a whole city, ~1-2 fps, everything archived; analysts scrub backward from an IED strike to the emplacement, then to origin, then forward to map the network. Ross McNutt's framing: "Google Earth with TiVo."
- Iraq-era systems were MANNED aircraft: Constant Hawk (Army, 2006), Angel Fire (AFRL/USMC, 2007). The drone version is Gorgon Stare on MQ-9s (~2011, Afghanistan), Increment 2 carrying DARPA ARGUS-IS (1.8 gigapixel).
- Payoff was network mapping (safe houses, financiers, cameramen), not just a single home base. Forward-tracking from the emplacement site mattered as much as rewind.

## Satellite regimes (physics forks the problem)

Single-sat LEO WAMI is impossible (minutes of dwell). Diffraction: 1 m resolution from GEO needs ~24 m aperture (1.22 * 550nm * 3.6e7 m / 1 m). So three regimes:

1. Archive-and-revisit: Planet (~200 Doves, whole landmass daily at ~3 m; the rewindable archive OSINT actually uses), BlackSky, SAR players (ICEYE/Capella/Umbra) for night/cloud. Rewind at daily-to-hourly cadence.
2. GEO staring, coarse: Gaofen-4 (~50 m optical, stares continuously; carrier groups yes, trucks no). Persistence bought with resolution.
3. Proliferated LEO with track custody: NRO's 100+ sat proliferated architecture (Starshield core, reported), plus dedicated Space Force/NRO/NGA GMTI birds expected from 2028 (enabling EO/low-end-radar/mesh sats already up; JSTARS replacement). AMTI follow-on: $7.06B in FY27 reconciliation procurement; both aimed at early-2030s IOC under Golden Dome. GMTI output is Doppler track files, i.e. the rewind done as data rather than pixels.

## Literature map: can this find shoot-and-scoot TELs?

Pessimist pole (sensing revolution breaks concealment):
- Lieber & Press 2017, "The New Era of Counterforce" (Int'l Security 41:4). Geospatial coverage analysis of NK's road network; concedes in fn. 98 it doesn't transfer to Russia/China scale. Effectively WAMI-logic over a small road-poor country.
- Green & Long 2015, "Stalking the Secure Second Strike" (JSS). Cold War hider-finder history; US got closer to holding Soviet second-strike at risk than nuclear-revolution theory predicts.
- Bracken 2015, "The Hunt for Mobile Missiles" (FPRI). Frames it as a big-data/network problem, not a sensor problem.

Optimist pole (TELs survive competent operation):
- MacDonald 2025, "Tracking Mobile Missiles" (JSS 48(2) 297-333); thesis version MacDonaldT__2021 in papers/. Space radar is the necessary sensor (night/cloud); current gaps of tens of minutes preclude custody; effective capability needs many dozens of dedicated radar sats; existing scholarship assumes sub-optimal TEL operation; commercial-sensor conglomerates unlikely to matter. Key scaling: search area after gap t grows ~(v*t)^2, so revisit time enters quadratically. 20-min gap at highway speed = ~30 km radius ambiguity per vehicle.
- Wu Riqiang 2020, "Living with Uncertainty" (Int'l Security). Chinese-perspective survivability modeling; read in Beijing as "our arsenal is more fragile than Americans assume."

Empirics and OSINT:
- Gulf War Air Power Survey: ~1,500 anti-Scud sorties, zero confirmed mobile TEL kills. The base rate already in the Q1 spine; MacDonald says it still binds, L&P say the sensor revolution broke it.
- Decker Eveleth (CNS, later AEI): commercial imagery found Yumen/Hami silo fields (2021), mapped PLARF garrisons and TEL infrastructure. Precise shape of the demonstration: finds FIXED infrastructure superbly (compresses "search China" to "watch these exits"); is not wartime custody of dispersed TELs.

Stability layer:
- JSS 2025 special issue "The End of MAD?" (the MacDonald paper is in it): combined technologies could enable persistent tracking of mobile platforms, weakening deterrence / catalyzing arms racing, while the same technologies can also aid survivability (deception, comms, warning).
- Geist & Lohn, RAND 2018: perception of AI-fused tracking degrades crisis stability whether or not it works.
- CSIS "Extending the Horizon": states openly that GMTI sats "could provide the data necessary to target mobile missile launchers."

## Q1 hooks

- Erosion claim has a clean pessimist/optimist structure with quantitative work on both sides; MacDonald is the strongest public counterweight to L&P and directly models the constellation question.
- The (v*t)^2 gap-scaling pairs naturally with the Bernoulli d^3 move: both are "the physics tells you which variable is the whole game" arguments.
- The stability-relevant variable is the adversary's ESTIMATE of custody capability. Nobody public has run the analysis at Starshield-class numbers with AI cueing (classified parameters); opacity plus visible constellation growth pushes the estimate up regardless of ground truth. That is the crisis-stability mechanism even if MacDonald is right about ground truth.
- Caution for the draft: dedicated GMTI is 2028-vintage; claims about CURRENT capability should lean on what actually flies (Starshield EO/radar, commercial SAR). Gen. Chilton et al. publicly argue space-based targeting is not ready. Genuine open question, not settled erosion.

## Artifacts this session

- papers/MacDonaldT__2021--hide_and_seek_remote_sensing_strategic_stability.pdf (6.1 MB, DSpace; T&F PDF of the article is Cloudflare-blocked, indexed by DOI)
- PAPER_INDEX.md: two MacDonald entries added
- PAPER_SUMMARIES.md not updated (needs an actual read-through; queue if wanted)
