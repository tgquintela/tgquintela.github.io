---
title: 'Berlin Elections 2026 - (I) Looking into the party landscape'
subtitle: 'Politics to policies: An intro of the maths of power through Berlin political landscape.'
excerpt: 'Lets know the Berlin parties.'
date: 2026-09-15
permalink: /temporales/2026/09/berlin-elections-20-d-i-intro-analysis/
header:
  overlay_image: blog/2026-09-berlin-elections/berlin_vector_header_data_analysis.jpg
  overlay_filter: 0.4
  tall: true

tags:
  - politics
  - python
  - Data Analysis
  - Data visualization
---


# Introduction
It has been a while since I last published, but I am breaking the silence for a focused multi-part series on politics, power, and policy ahead of the Berlin state election on September 20, 2026.

Rather than treating the election as a simple headcount of parliamentary seats, this series looks under the hood of local governance to examine its core driving engine: how raw political power translates into actual policy outcomes. By modeling seat distributions alongside ideological stances across key municipal axes, we will explore how shifting electoral outcomes alter the tangible direction of the city.

In this first installment, we lay the quantitative baseline for our analysis:
* **The Multi-Axis Policy Framework**: Mapping Berlin's political landscape across core municipal policy dimensions (Housing, Transport, Public Safety, Climate, Fiscal Policy, and International Alignment) using empirical survey data.
* **Standardized Party Positioning**: Converting empirical datasets from voting advice applications (Wahl-O-Mat, WahlSwiper) and thematic policy audits into normalized 1.0–10.0 numerical scales for each major competing party.
* **Methodological Mechanics**: Establishing the mathematical scoring formula used to weight parliamentary seat shares against party stances to calculate future coalition policy trajectories.

With that we will know who is who in Berlin politics and how can we calibrate our policy expectations.

# Who Really Holds Power in Berlin?
### A voting-game analysis of the Abgeordnetenhaus (2023 results)

*Analysis of the power structure of the Berlin Abgeordnetenhaus as elected on
12 February 2023 — **159 seats, 80 needed for a majority**. Seat counts are the
**official 2023 results** ([source](https://en.wikipedia.org/wiki/2023_Berlin_state_election));
power indices and policy projections are computed with the
[`cooperativegames`](https://github.com/tgquintela/CooperativeGames) package.
This is an analysis of **policy power** — no vote-intent polls are used, only
party policy positions.*

Before a government is formed, the real question in a parliamentary system is not
*who won the most seats*, but **who can govern** — and what they will govern. In
Berlin's 2023 result no party holds a majority on its own, so the election is
really a contest over **coalitions**. This article uses the mathematics of
**cooperative (voting) games** to answer two questions:

1. **Who holds power?** Not just who has the most seats, but who is *pivotal* —
   whose participation decides whether a coalition can command a majority.
2. **What will policy look like?** Given that parties only govern with partners
   they can actually stand next to, which way will the governing coalition pull
   each policy dimension?

We separate **arithmetic power** (Part 1) from **realistic power** (Part 2),
because the difference between the two is where the politics actually is.

Throughout, we introduce the concepts and assumptions used to model the result,
and we draw on public **policy data and party positions** — not vote-intent
polls — to characterise where each party stands.


## 1. Power in voting games — why and how

### Why seats are not enough

In a simple majority game, a party's influence is not determined by how many
seats it holds, but by **how often it is decisive**. Consider two extremes:

- A large party that is *dispensable* — every majority works with or without it —
  has little bargaining power despite its size.
- A small party that is *essential* to every workable majority is a **kingmaker**,
  wielding influence far beyond its seat share.

Voting-game theory makes this precise. The parliament is modelled as a **weighted
voting game** `[q; w₁, w₂, …, wₙ]`, where `wᵢ` is a party's seats and `q` is the
quota (a simple majority of the 159-seat house is **80**). A coalition *wins* if
its seats reach the quota. Power is then measured by how often a party is the
decisive member of a winning coalition.

### The two indices we use

| Index | Intuition | Question it answers |
| --- | --- | --- |
| **Banzhaf** | A party is a *swing voter* when adding it turns a losing coalition into a winning one. The index counts how often this happens. | How often is this party **decisive**? |
| **Shapley–Shubik** | Parties join a coalition in random order; the *pivotal* party is the one that pushes the running total over the quota. The index is the probability a party is pivotal. | What is this party's expected **bargaining contribution**? |

Both are computed **exactly** by the package (the Banzhaf index via an O(n·q)
dynamic program, so even a full 159-seat house is tractable).

### The result: arithmetic power in Berlin 2023

Applying the two indices to the official 2023 result — a simple majority of
**80** seats in the 159-seat house — gives each party's *arithmetic* power. The
table lists each party's seat count and seat share next to its Banzhaf and
Shapley–Shubik indices; the chart below plots the same against raw seat share
(black dashed line), so you can see exactly where power departs from seats.

| Party | Seats | Seat share | Banzhaf | Shapley–Shubik |
| --- | ---: | ---: | ---: | ---: |
| **CDU** | 52 | 32.7% | **0.385** | **0.400** |
| **SPD** | 34 | 21.4% | 0.231 | 0.233 |
| **Grüne** | 34 | 21.4% | 0.231 | 0.233 |
| **Die Linke** | 22 | 13.8% | 0.077 | 0.067 |
| **AfD** | 17 | 10.7% | 0.077 | 0.067 |

![Party power vs seat share]({{ base_path }}/images/blog/2026-09-berlin-elections/party-power-vs-seat-share.svg)

Three things jump out. First, **CDU** is not just the largest party — it is the
*pivot*: its power (0.38–0.40) sits well above its 32.7% seat share, because a
majority of 80 is hard to build without it. Second, **SPD and the Greens are
tied** (0.23 each) — both are essential swing parties that CDU needs to reach
80. Third, **Die Linke and AfD are tied** at the bottom (0.077 each): both are
too small to be decisive on their own, so their power is *conditional* on which
side of the house they can pull. *(The FDP won no seats in 2023 and BSW had not
yet been founded, so neither is in this game.)*


## 2. Policy topology — why the policy dimension matters

### Not every winning coalition is equally likely

Part 1 counts *all* winning coalitions as if they were equally plausible. They
are not. A coalition of parties that **agree on policy** is far more likely to
form — and to survive — than one that clashes on every file. The **policy
topology** (how parties are arranged in policy space) determines which of the
arithmetic coalitions are *realistic*.

Ignoring this produces a systematic error: it over-weights policy-incoherent
coalitions. In Berlin the sharpest case is the **AfD**: the current state of
German politics rules out *any* coalition that includes it — not merely a
CDU–AfD pairing, but the AfD with *every* other party. This is the so-called
*Brandmauer* (firewall): a common-knowledge taboo that the AfD is excluded from
governing altogether. A model that cannot see this will forecast a far more
rightward government than reality will deliver.


### The method: weight coalitions by policy naturalness, then encode common knowledge

We do two things to turn arithmetic power into **realistic** power:

1. **Policy naturalness.** For each winning coalition we compute a *naturalness*
   weight = the product of the pairwise **policy proximities** of its members
   (proximity = 1 − distance in the 6-dimensional policy space). A coherent
   coalition scores high; a patchwork of ideological opposites scores near zero.
   We then average each coalition's policy position (seat-weighted) and weight
   the average by naturalness. This yields the **likely governing coalition's
   position on each policy axis**.
2. **Common knowledge (the Brandmauer).** We add a `forbidden_pairs` filter that
   removes any coalition containing a politically infeasible pairing. The
   Brandmauer is encoded as *every pair that involves the AfD* (AfD × CDU, AfD ×
   SPD, AfD × Grüne, AfD × Die Linke), so **any coalition containing the AfD is
   excluded** — not just CDU+AfD. This encodes what everyone already knows but a
   pure arithmetic model cannot.

### The result: realistic policy, with and without the firewall

![Coalition policy projection]({{ base_path }}/images/blog/2026-09-berlin-elections/governing-coalition-policy-projection.svg)

| Axis | Proximity only | + Brandmauer (AfD excluded) | Reading | Direction (which side) |
| --- | ---: | ---: | --- | --- |
| **security** | 6.75 | **6.55** | law-enforcement side (robust) | law-enforcement / surveillance |
| **middle_east** | 2.45 | **2.58** | Staatsräson side (robust) | Staatsräson / pro-Israel |
| housing | 4.61 | **4.81** | near the centre | slightly free-market / laissez-faire |
| transport | 4.71 | **4.96** | near the centre | slightly pro-car / car-friendly |
| fiscal | 5.01 | **5.19** | near the centre | slightly austerity / debt-brake |
| climate | 5.45 | **5.71** | slightly right of centre | slightly toward climate action |

*(Scale 1→10, midpoint 5.5. Lower = the "left anchor" of each axis, higher = the
"right anchor".)*

**Which side, in plain terms.** On the *economic* axes the realistic projection
sits just on the **free-market / fiscally-conservative** side of centre: housing
leans slightly toward the market (no rent caps), transport slightly pro-car, and
fiscal slightly toward the debt-brake / austerity — i.e. a **mild
laissez-faire / economically-right tilt**, not a decisive one. **Climate** leans
the other way (slightly toward accelerated neutrality / more climate action).
**Security** is law-enforcement-leaning and the **Middle East** leans
Staatsräson. So the likely government is **centrist overall, with a mild
free-market tilt** on the economic axes — not a right-wing government, but not
left either. The direction is the same in both columns (proximity-only and
Brandmauer), so it is robust to the firewall assumption.

The most natural feasible coalitions:

- **Proximity only:** CDU+SPD (0.38), CDU+Grüne (0.17), CDU+SPD+AfD (0.16),
  SPD+Grüne+Linke (0.13), CDU+SPD+Grüne (0.07).
- **With the Brandmauer:** **CDU+SPD (0.48), CDU+Grüne (0.22), SPD+Grüne+Linke
  (0.16), CDU+SPD+Grüne (0.09)** — every AfD coalition (e.g. the CDU+SPD+AfD
  above) is now removed from the feasible set.

**The takeaway.** The **CDU–SPD grand coalition** is by far the most natural
government — and it is exactly the one that was formed (the Wegner senate).
Encode the Brandmauer (exclude the AfD from every coalition) and CDU+SPD becomes
even more dominant (0.48), because the entire AfD-inclusive right bloc is removed
from the feasible set. The likely policy is **centrist**: housing, transport and
fiscal sit near the middle, climate is slightly right of centre, **security leans
law-enforcement** and the **Middle East leans Staatsräson** — those two are the
robust, direction-setting findings.
This is the whole point of doing the analysis in two layers: **arithmetic power
tells you who is strong; policy topology + common knowledge tells you what they
will actually do.**


## 3. Data sources and methodology

All inputs are **policy positions and policy-opinion data** — *not* opinion polls
and *not* vote-intent. We never ask "who will voters choose?"; we ask "where does
each party stand on each policy?".

### Sources

| Source | What it provides | Role | Direct links |
| --- | --- | --- | --- |
| **Wahl-O-Mat** (bpb / LZPb) | Parties' answers to ~38 standardised policy statements (agree / neutral / disagree) across the election. | Primary structured record of party *positions*. | [Wahl-O-Mat portal](https://www.wahl-o-mat.de/) |
| **WahlSwiper / VoteSwiper** (Univ. Freiburg, Prof. U. Wagschal) | Spatial political-science model (Gal–Tan + left–right) giving party coordinates and pairwise agreement percentages. | Independent cross-check / spatial validation of positions. | [VoteSwiper platform](https://www.voteswiper.org/) · [Univ. Freiburg study portal](https://uni-freiburg.de/wahlswiper-jetzt-fuer-die-bundestagswahl-2025-verfuegbar/) |
| **Policy audit — housing** (Berliner Mieterverein, Deutscher Mieterbund) | Structured party comparisons (Wahlprüfsteine) on housing / rent policy. | Grounds the **housing** axis in concrete policy commitments. | [Berliner Mieterverein](https://www.berliner-mieterverein.de) · [Deutscher Mieterbund Parteienvergleich](https://mieterbund.de/wahlpruefsteine-zur-bundestagswahl-2025/) |
| **Policy audit — transport & infrastructure** (Aktionsbündnis A100 stoppen!, Grüne Fraktion Berlin) | Structured party comparisons on transport / the A100 question. | Grounds the **transport** axis in concrete policy commitments. | [A100 stoppen!](https://theleftberlin.com/aktionsbundnis-a100-stoppen/) · [Grüne Fraktion Berlin A100 dossier](https://gruene-fraktion.berlin/a100/) |
| **Media policy comparisons** (Tagesspiegel Data Lab, rbb24) | Editorial party-positioning matrices built from manifestos and voting records. | Fills gaps and corroborates the above. | [rbb24](https://www.rbb24.de) · [Tagesspiegel Interaktiv / Data Lab](https://www.tagesspiegel.de) |

### From stances to numeric scores (weighted average)

Each policy **axis** is built from several underlying policy items. For a party
and an axis, we score each item `xᵢ ∈ {−1, 0, +1}` (against / neutral / for the
axis's "high" pole) and assign it a **thematic weight** `wᵢ` reflecting its
importance within the axis. The party's axis score is the **weighted average**,
mapped onto the 1–10 scale:

```text
S = 1.0 + 9.0 × ( Σᵢ w·xᵢ + Σᵢ w ) / ( 2 · Σᵢ w )
```

This is a standard rescaling of a weighted mean: it lands at **1.0** when the
party opposes every item, **10.0** when it supports every item, and **5.5** when
its weighted stance is balanced. The result is the 6-axis position matrix used
throughout this article:

![Party policy positions]({{ base_path }}/images/blog/2026-09-berlin-elections/party-policy-positions.svg)

| Party | Housing | Transport | Mid-East | Security | Fiscal | Climate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **CDU** | 2.5 | 2.5 | 1.5 | 9.0 | 3.0 | 3.5 |
| **SPD** | 5.5 | 5.5 | 2.5 | 5.5 | 6.0 | 6.5 |
| **Grüne** | 8.5 | 9.5 | 4.0 | 3.0 | 8.5 | 9.5 |
| **Die Linke** | 10.0 | 9.5 | 8.5 | 1.5 | 10.0 | 9.0 |
| **AfD** | 2.0 | 1.0 | 1.0 | 9.5 | 2.5 | 1.0 |
| **BSW** | 9.0 | 8.0 | 7.5 | 6.0 | 8.0 | 6.0 |
| **FDP** | 1.5 | 1.5 | 2.0 | 7.5 | 1.0 | 2.0 |

**Methodological caveat — the policy scores are heuristic, not a robust
science.** No number in the matrix above is the output of a validated survey
or measurement instrument. Each party's score on each of the six axes was
**inferred by the author** from the sources listed above (Wahl-O-Mat /
WahlSwiper statements, Wahlprüfsteine, editorial matrices) through a
transparent but **heuristic** coding of qualitative stances onto the 1–10
scale (the weighted-average formula above). The method is reproducible and
documented, but the exact score a party receives depends on which underlying
items are chosen, how they are weighted, and how each stance is coded — i.e.
it is **expert judgement, not a robust science**. Read the *directions* and
*relative ordering* of the parties as the robust findings; treat the specific
values as a best-effort encoding, not precise measurements.

*BSW and FDP are shown because they are part of the **current (pre-2026) party
landscape**. Neither held seats in the 2023 result used for the power simulation
(BSW was founded afterwards; the FDP fell below the 5% threshold), so they do not
appear in the power tables of Parts 1–2 — but they are full contenders for 2026.*

*Axis anchors:*
**Housing** 1 = free market / no rent caps → 10 = expropriation / rent freeze.
**Transport** 1 = pro-car / A100 → 10 = transit-first / car-free.
**Mid-East** 1 = Staatsräson / funding clauses → 10 = pro-Palestinian / protest,
civil and humanitarian rights.
**Security** 1 = civil rights / anti-profiling → 10 = law-enforcement /
surveillance.
**Fiscal** 1 = austerity / debt-brake → 10 = debt reform / borrowing.
**Climate** 1 = market / sceptical → 10 = accelerated neutrality.



## 4. Where each party stands — an opinionated read

The numbers above are descriptive; this section is our **take** on what they mean.
Power and position together tell you who can govern, and what they will do.

### CDU — the indispensable pivot *(52 seats · power 0.38–0.40)*
CDU's power (0.38–0.40) is well above its 32.7% seat share because a majority of
80 is hard to reach without its 52 seats: **CDU+SPD (86)** and **CDU+Grüne (86)**
both clear the quota, so CDU can choose its partner. Its profile is unambiguously
conservative — free-market housing (2.5), pro-car transport (2.5), hard security
(9.0), fiscal discipline (3.0), market climate (3.5), maximalist Staatsräson
(1.5). **Our read:** CDU is the kingmaker, and its conservative defaults set the
floor for any government. But in a CDU+SPD or CDU+SPD+Grüne government it must
compromise toward the centre — and the 2023 outcome (the CDU–SPD grand coalition)
confirms exactly that: CDU's power is real, but it is exercised *through* a
centrist partner, not alone.

### SPD — the centrist hinge *(34 seats · power 0.23)*
SPD sits near the middle on almost every axis (housing 5.5, transport 5.5,
security 5.5, fiscal 6.0, climate 6.5) and is tied with the Greens as the
essential swing party. **Our read:** SPD is the natural partner for CDU —
CDU+SPD is the single most natural government (0.38, rising to 0.47 with the
firewall). SPD's centrality is its asset: it is the bridge that makes a CDU
government workable, and it trades that centrality for the vice-chancellery and
the key ministries. In the CDU–SPD grand coalition, SPD is the party that pulls
policy toward the centre — which is why the projected policy is centrist rather
than CDU-conservative.

### Grüne — the climate-and-housing pole, tied with SPD *(34 seats · power 0.23)*
Grüne leads on climate (9.5), housing (8.5) and transport (9.5), is moderate on
the Middle East (4.0) and civil-rights oriented on security (3.0). **Our read:**
Grüne is the *other* essential swing party — CDU+Grüne (86) also clears 80, which
is why its power (0.23) matches SPD's. But in 2023 Grüne chose **opposition**:
the CDU–SPD coalition formed without it. Its realistic role is to hold the
climate-and-housing agenda and to be the alternative partner — in a
CDU+SPD+Grüne traffic-light, Grüne would push climate, housing and transport
left; in opposition, it sets the terms any future government must answer to.

### Die Linke — coherent left, conditionally relevant *(22 seats · power 0.077)*
Linke is the most left on housing (10.0), fiscal (10.0), climate (9.0) and
transport (9.5), and the most pro-Palestinian (8.5). **Our read:** Linke is
policy-coherent and radical, but at 22 seats it is **too small to be decisive
alone** — its power (0.077, tied with AfD) is *conditional*. It matters in a left
coalition (SPD+Grüne+Linke = 90 clears 80) but not in a CDU-led one. In 2023
Linke was left out of the new government (it had been part of the outgoing
red-red-green). Its realistic role is opposition and the left anchor *if* a left
coalition ever forms again.

### AfD — powerful on paper, locked out in practice *(17 seats · power 0.077)*
AfD is the far-right pole: pro-car (1.0), maximal security (9.5), Staatsräson
plus hardline migration (1.0), austerity (2.5), climate denial (1.0). **Our
read:** AfD's arithmetic power (0.077) is modest and, crucially, **locked** by
the Brandmauer — no party will govern with it, so it is excluded from *every*
coalition, not just a CDU one. Arithmetically, CDU+SPD+AfD (103) and other
AfD-inclusive majorities exist, but politically AfD cannot enter a government. So
AfD is a **permanent opposition with agenda-setting influence — especially on
security and migration — but no governing role.** Encode the Brandmauer and AfD
vanishes from the feasible coalitions; that is the political effect of the
firewall.

### BSW — the new left force, not yet in the 2023 game *(no 2023 seats)*
BSW pairs strong pro-tenant (9.0) and transit (8.0) positions with a *moderate*
security stance (6.0) and a critical-but-not-extreme foreign policy (7.5). **Our
read:** BSW is the most interesting variable for 2026. It is policy-close to both
Grüne and (on housing) Die Linke, yet its moderate security score makes it a more
"governable" left partner than either. It was founded after the 2023 election, so
it has no 2023 power figure here — but if it enters the 2026 Abgeordnetenhaus it
becomes a potential **kingmaker on the left**, the anchor that makes a CDU or SPD
government workable without AfD.

### FDP — the fiscal liberal, back in the running *(no 2023 seats)*
FDP is the classic liberal: strict debt-brake (1.0), free-market housing (1.5),
pro-car (1.5), market climate (2.0) — but a notably hawkish security stance
(7.5). **Our read:** the FDP fell below the threshold in 2023 (0 seats), so it has
no 2023 power figure here. If it clears 5% in 2026 it re-enters as a small but
potentially pivotal liberal partner: its value to CDU is fiscal discipline (the
1.0 on the debt-brake), and its security score (7.5) sits closer to CDU than its
economics suggest. As a small party its power would be *conditional* — a junior
partner at best.



## Bottom line

- **Power ≠ seats.** CDU is the pivot (0.38–0.40 vs 32.7% seats); SPD and the
  Greens are the tied swing parties (0.23); Linke and AfD are tied, smaller and
  conditional (0.077).
- **The CDU–SPD grand coalition is the natural government** — and it is the one
  that formed. Policy topology + the Brandmauer (AfD excluded from all coalitions)
  make it even more dominant.
- **The likely policy is centrist** on housing, transport and fiscal, slightly
  right on climate.
- **Two policies are robust:** security leans **law-enforcement** and the Middle
  East leans **Staatsräson**, whichever way the coalition turns.
- **The real contest is over the left anchor:** whether a future government is
  CDU+SPD, CDU+SPD+Grüne, or a left SPD+Grüne+Linke bloc decides how far left
  housing, climate and fiscal policy go.

*All indices and projections are reproducible with the
[`cooperativegames`](https://github.com/tgquintela/CooperativeGames) package
(`WeightedVotingGame`, `coalition_policy_projection`, `power_weighted_policy`)
applied to the official 2023 seat results and the party policy-position data.
An interactive version of the charts is available in
[`interactive/`]({{ base_path }}/images/blog/2026-09-berlin-elections/interactive/).*



## A simple model of a complex system — and where this goes next

Everything above is a **deliberately simple model of a deliberately complex
system**. Political and parliamentary power in a modern democracy is shaped by
far more than seat counts and policy distances, and this model knowingly leaves a
great deal out:

- **Coalitions are symbolic as well as arithmetic.** A mathematically workable
  bloc can be vetoed over a single, very specific reason — a personal feud, a
  local scandal, a one-issue red line — that no policy distance captures.
- **Party positions are not fixed.** The six-axis positions we use are a
  snapshot. Real parties drift in response to external events, leadership
  changes and the news cycle, and a static model cannot see that movement.
- **Institutional and human factors** — faction discipline, ministerial
  ambitions, the personalities at the negotiating table — all bend the outcome
  in ways a voting game does not model.

None of that is in the model, and that is the point. By stripping the system
down to its core mechanics, we can see *how much* weight the factors we *did*
include — power, policy topology, the firewall — actually carry. The
simplification is not a weakness; it is the lens that lets the important factors
show.

It also points to a bigger idea. **Politics should be about policies, not about
the shallow symbolic space that parties alone occupy.** If the real levers that
move policy are (a) **how you vote** and (b) **how you shape the narrative** —
the so-called *culture war* — then understanding and pulling those levers matters
as much as understanding the arithmetic.

That is exactly what the **next article** in this series takes up. Taking the
**current polls** as our starting point — and holding party policy positions
fixed — we run the engine forward to measure **how much power each party really
holds**, how the **5% threshold and seat arithmetic** reshape the field, and, the
central question, **how sensitive the resulting policy given the curren polls**: how
much do a few points of polling movement actually move policy, where is the
likely government robust, and where can it flip? Put differently: how much
influence does a single vote have? All of it centred on the **next Berlin state
election, on 20 September 2026**.

&nbsp;

See you there!

&nbsp;
