---
title: 'Berlin Elections 2026 - (II) The scenario engine: polls, seats, and the policy that follows'
excerpt: 'The real current polls run through a voting-game engine: who can govern, what they will do, and what a few points can still change.'
date: 2026-09-18
permalink: /blog/2026/09/berlin-elections-2026-ii-scenario-engine/berlin_vector_berlin_votes_to_power_header.jpg
header:
  overlay_image: blog/2026-09-berlin-elections/berlin_votes_to_power_header.jpg
  overlay_filter: 0.4
  tall: true

tags:
  - politics
  - python
  - Data Analysis
  - Data visualization
---

# Post 2: The Scenario Engine — Polls, Seats, Coalitions, and the Policy That Follows

*Continuation of [Post 1 — Who Really Holds Power in Berlin?]({{ base_path }}/blog/2026/09/berlin-elections-20-d-i-intro-analysis/)*

Post 1 analysed a single fixed snapshot — the 2023 result. But elections are
decided by **movements**, not snapshots. In Post 2 we start from the
**actual current polls** for the 20 September 2026 election, run them through
the same voting-game engine, and follow the consequences down the chain:
**poll → 5% threshold → seats → viable coalitions → policy**. We then stress-test
the picture: what happens if the left surges, if the right shifts, and — in a
fourth what-if — if the **Brandmauer** (the CDU–AfD firewall) breaks?

## 1. The engine: from poll to policy

The pipeline is four steps, after seats allocation all computed by the `cooperativegames` package:

1. **Poll → threshold.** Parties below the **5% threshold** get no seats
   (constituency wins ignored here for simplicity).
2. **Threshold → seats.** Proportional allocation (largest-remainder) to the
   **130-seat** base house.
3. **Seats → coalitions.** All coalitions with a **majority (66 seats)**,
   excluding politically infeasible pairings — the **Brandmauer** (the AfD is
   barred from governing with *every* party, not just the CDU), the federal
   CDU's **"resolution of incompatibility"** with Die Linke, and the Greens'
   red line against governing with the CDU.
4. **Coalition → policy.** The likely government's position on each axis is the
   **seat-weighted stance** of its members:

```text
Axis Score =  Σ  ( party_seats / coalition_seats  ×  party_stance_on_axis )
              over parties in the coalition
```

The "main" coalition is the most *natural* viable one — the product of its
members' pairwise policy proximities (a coherent coalition scores higher).
The six-axis party positions are the same matrix as in Post 1
(1 = left anchor, 10 = right anchor).

## 2. First, the current polls

Before the scenarios, the data. We transcribed the full opinion-poll table of
the [Wikipedia article on the 2026 Berlin state
election](https://en.wikipedia.org/wiki/2026_Berlin_state_election) (35 rows,
February 2023 → 14 September 2026, with fieldwork dates, sample sizes and a
source link per poll) into a dataset, and computed the **current picture** as
the average of the four polls whose fieldwork ended at/after 2 September 2026
(INSA, Infratest dimap, Forschungsgruppe Wahlen), per party over the polls
that measured it, normalized to 100.

![Poll timeline]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-poll-timeline.svg)

Three things define the current race:

- **Die Linke has surged** — up **8 points** from 12.2% in 2023 to
  **20.4%** today (a two-thirds increase) — and now polls level with the CDU
  for first place.
- **The CDU has collapsed** — from 28.2% to **20.0%**, losing a third of its
  2023 share. SPD (18.4 → 12.1) and the AfD (9.1 → 17.5, nearly doubled)
  complete a field in which **three parties have each led a poll in the last
  two months** (CDU, AfD, Linke).
- **BSW has faded** — after peaking at **12%** in mid-2024 it has slid to
  **3.7%**, below the threshold. The FDP (3.0%) is also out.

The result: **five parties clear the 5% line** (Linke 20.4, CDU 20.0, AfD
17.5, Grüne 15.5, SPD 12.1) and will take all 130 seats; BSW and FDP will not
be in the house at all, based on the current polling (Thursday 17th, polls now may change abruply depending on very specific incidents).

![Current polling picture vs 2023]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-current-polls-vs-2023.svg)

The old East–West divide persists: in **East Berlin** Die Linke leads (25%)
with the AfD close behind (22%); in **West Berlin** the CDU leads (23%).

![East vs West]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-polls-east-vs-west.svg)

**Sources and caveats.** The current baseline averages INSA (7–14 Sep),
Infratest dimap (7–9 Sep), Forschungsgruppe Wahlen (7–10 Sep) and INSA
(26 Aug–2 Sep). Most rows are aggregated by
[wahlrecht.de](https://www.wahlrecht.de/umfragen/landtage/berlin.htm); direct
links: [Civey 25 Jun–9 Jul](https://dawum.de/Berlin/Civey/2026-07-13/) ·
[Civey 20 Jul–3 Aug (Tagesspiegel)](https://www.tagesspiegel.de/berlin/umfrage-zur-berlin-wahl-linke-springt-auf-platz-eins--wegner-ruckzug-nutzt-cdu-nicht-15913067.html) ·
[Civey 13–27 Aug (Tagesspiegel)](https://www.tagesspiegel.de/berlin/linke-vor-cdu-und-afd-neue-umfrage-sagt-dreikampf-um-wahlsieg-in-berlin-voraus-15997950.html) ·
[BSW-commissioned poll, 21–26 Aug (PDF)](https://bsw.berlin/wp-content/uploads/260909_PM_Wahlumfrage_Berlin_Anlage.pdf) ·
[2023 result](https://en.wikipedia.org/wiki/2023_Berlin_state_election) ·
[East/West tables](https://www.wahlrecht.de/umfragen/landtage/berlin/west.htm).
Two caveats: some INSA polls are commissioned by the right-wing populist
portal *Nius* (not subject to Presserat ethics rules), and the BSW-commissioned
August poll is a party outlier (CDU 13.5 / AfD 21.1). Neither enters the
baseline average — the Nius polls predate the September window, and the BSW
poll is excluded as party-commissioned.

## 3. Four scenarios

| Party | Current Baseline | Left-Green Surge | Conservative Shift | Firewall Breaks† |
| --- | ---: | ---: | ---: | ---: |
| CDU | 20.0 | 15.0 | **24.0** | 24.0 |
| SPD | 12.1 | 14.0 | 11.0 | 11.0 |
| Grüne | 15.5 | 19.0 | 11.0 | 11.0 |
| Die Linke | **20.4** | **24.0** | 15.0 | 15.0 |
| AfD | 17.5 | 13.0 | **21.0** | 21.0 |
| BSW | 3.7 | 6.0 | 3.0 | 3.0 |
| FDP | 3.0 | 2.0 | **6.0** | 6.0 |
| Others | ~7.8 | ~7.0 | ~9.0 | ~9.0 |

The **Current Baseline** is the real polling picture of §2. The **Left-Green
Surge** pushes the ongoing leftward drift further (Linke 24, Grüne 19, BSW
back over the line at 6, CDU 15, AfD 13); the **Conservative Shift** is its
mirror (CDU 24, AfD 21, the left down, FDP back over the line at 6). Both are
illustrative counterfactuals, not predictions. †**Firewall Breaks** reuses the
Conservative Shift polls exactly — it is *not* a new poll. It is a **what-if**
that drops the Brandmauer (§8), so the same parliament is free to form a
government that includes the AfD.

**Threshold dynamics — the quiet game-changer:**
- **BSW** hovers on the 5% line: **out** in the baseline (3.7) and the shift
  (3.0), but **back in** under the surge (6.0) — nine seats from a couple of
  polling points.
- **FDP** is the same story on the right: **out** in the baseline (3.0) and
  the surge (2.0), **back in** under the shift (6.0).
- **Die Linke** is safely in everywhere (15–24) — the left surge is no longer
  a question of *whether* Linke enters the house, but of how dominant it gets.

And note the structural change since 2023: **no two-party coalition can reach
66** (the largest pair, CDU+Linke, has 61 seats) — every viable government in
every scenario needs **at least three parties**.

## 4. Seat calculations (130-seat house)

![Seat distribution by scenario]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-seats-by-scenario.svg)

| Party | Baseline | Left-Green Surge | Conservative Shift | Firewall Breaks† |
| --- | ---: | ---: | ---: | ---: |
| CDU | 30 | 21 | **36** | 36 |
| SPD | 18 | 20 | 16 | 16 |
| Grüne | 24 | 27 | 16 | 16 |
| Die Linke | **31** | **34** | 22 | 22 |
| AfD | 27 | 19 | 31 | 31 |
| BSW | **0** | 9 | 0 | 0 |
| FDP | **0** | 0 | 9 | 9 |
| **Total** | 130 | 130 | 130 | 130 |

†Identical to the Conservative Shift (same polls) — breaking the firewall
changes which coalitions are *allowed*, not the seat arithmetic.

The biggest structural change since 2023 (159-seat house): **Die Linke becomes
the largest party** (31 vs CDU's 30), the CDU loses 22 seats, the AfD gains 10,
and BSW — which peaked at 12% in mid-2024 — falls back out of the house.

## 5. Power: arithmetic, topology, and common knowledge

### 5.1 Arithmetic power: the pivot is gone

Post 1 showed the CDU as the 2023 parliament's indispensable pivot
(Banzhaf 0.385 vs 32.7% seats). Running the same indices on the projected
2026 parliament gives a surprising result:

| Party | Seats | Banzhaf | Shapley–Shubik |
| --- | ---: | ---: | ---: |
| Die Linke | 31 | 0.200 | 0.200 |
| CDU | 30 | 0.200 | 0.200 |
| AfD | 27 | 0.200 | 0.200 |
| Grüne | 24 | 0.200 | 0.200 |
| SPD | 18 | 0.200 | 0.200 |

**A perfect five-way tie.** Every party that clears the threshold has exactly
the same arithmetic power. The reason is the shape of the seat vector: *every
pair* of parties falls short of the 66-seat majority (the biggest, CDU+Linke,
has 61) while *every trio* clears it (the smallest has 69). So each party is
decisive for exactly the same set of coalitions — the six pairs of its four
partners — and no more. The CDU's power has fallen from 0.385 to 0.200; the
largest party (Linke, 31) is exactly as strong as the smallest in the house
(SPD, 18). **Nobody is the pivot** — which is precisely why this election is
a three-party formation problem, not a two-party one.

It also means the parliament projection of §7 is unusually clean: weighting
by power with five equal powers reduces to the **simple average of the five
parties' positions**.

### 5.2 Realistic power: the policy-weighted indices

Arithmetic power counts every swing as equally likely. But as Post 1
argued, coalitions are **not** equally likely to form — a coherent one is.
So we re-weight the indices by the **policy topology**: each swing of party
*i* on a losing coalition S is weighted by the *naturalness* of the winning
coalition S∪{i} (the product of its members' pairwise policy proximities,
as in Post 1), and swings that would create a coalition that *cannot form*
(Brandmauer, CDU–Linke incompatibility) never count:

```text
phi_i  =   Σ  nat(S ∪ {i})                    (policy-weighted Banzhaf)
           over S where i is a swing, S∪{i} feasible

phi_i  =   Σ  nat(S ∪ {i}) · |S|! (n−|S|−1)! / n!   (policy-weighted
           over S where i is a swing, S∪{i} feasible   Shapley–Shubik)
```

Both indices agree to within 0.02 in every scenario (same swings, same
weights, near-identical combinatorics), so the table shows the weighted
Banzhaf; the weighted Shapley–Shubik is in parentheses in the text where it
differs. The Firewall-Breaks column drops all taboos, as the scenario does.

![Policy-weighted power by scenario]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-policy-weighted-power-by-scenario.svg)

| Party | Current Baseline | Left-Green Surge | Conservative Shift | Firewall Breaks |
| --- | ---: | ---: | ---: | ---: |
| CDU | 0.129 | 0.074 | **0.333** | **0.448** |
| SPD | **0.333** | 0.170 | **0.333** | 0.059 |
| Grüne | **0.333** | **0.345** | **0.333** | 0.053 |
| Die Linke | 0.205 | 0.271 | 0.000 | 0.045 |
| BSW | — | 0.141 | — | — |
| AfD | **0.000** | 0.000 | 0.000 | 0.387 |
| FDP | — | — | 0.000 | 0.008 |

**The baseline: the left holds the hinges.** SPD and the Greens (0.333
each) are the realistic powerhouses — each is decisive in *both* viable
governments (RRG and the Kenia alternative). Die Linke (0.205) is decisive
only in RRG, but that is the most natural government, so its weight is
heavy. The CDU (0.129) is decisive only in the less natural Kenia. And the
**AfD is exactly zero**: with 27 seats — second only to Linke — it is a
swing in *no feasible government at all*. The firewall does not merely keep
the AfD out of government; it removes its power.

**The topology-only trap.** Remove the taboos and the same weights make the
far-right coalition *attractive*: the AfD's realistic power jumps to 0.166 —
*above* Die Linke's 0.142 — because the CDU–AfD proximity (0.860) makes
coalitions containing both "natural" in policy space. In the Conservative
Shift the effect is stronger still: topology-only gives the AfD 0.387,
almost matching the CDU's 0.448. The common-knowledge layer is what restores
sanity — this is Post 1's arithmetic-vs-realistic distinction doing exactly
its job, now quantified per scenario.

**Across scenarios:**
- **Surge** — the Greens become the realistic pivot (0.345); BSW enters at
  0.141 (it is in the most natural government, Linke+Grüne+BSW); the CDU
  drops to 0.074.
- **Conservative Shift** — a Kenia three-way tie (CDU/SPD/Grüne 0.333 each);
  Die Linke (0.000) is left with no feasible government it can join.
- **Firewall Breaks** — power concentrates in the right bloc: **CDU 0.448 +
  AfD 0.387 = 83% of all realistic power** (weighted Shapley–Shubik:
  0.460 / 0.414); every other party is marginal (≤ 0.06). This is the
  arithmetic face of the §8 finding.
- **The CDU's power is scenario-conditional** — 0.129 (baseline) → 0.074
  (surge) → 0.333 (shift) → 0.448 (firewall): the CDU is a pivot only when
  the polls put it inside a natural government.

*(If the Greens' no-Kenia red line were added as a further taboo, the CDU's
baseline power would fall to exactly zero — RRG would be the only feasible
government — and the Conservative Shift would have no feasible government at
all. We do not hard-code a single lead candidate's campaign statement into
the engine.)*

## 6. Coalition options: one realistic government

The set of viable governments, ranked by naturalness:

- **Current Baseline** — the most natural government is a left one:
  **Die Linke + Grüne + SPD (73 seats, naturalness 0.273)**. The centrist
  alternative **CDU + Grüne + SPD** (the Kenia coalition, 72 seats, 0.172) is
  a close second. (Before the taboos are applied, CDU+Linke+SPD (79) and
  CDU+Grüne+Linke (85) are larger but far less coherent.) Then the taboos do
  their work: the federal CDU's incompatibility resolution forbids *any*
  CDU–Linke coalition, and Green lead candidate Graf has ruled out working
  with the CDU. Strip those out and **Red–Red–Green is the only coalition
  that can actually form** — matching the consensus read of the campaign.
- **Left-Green Surge** — the left grows so large that **Die Linke + Grüne +
  BSW (70)** becomes the *most natural* government (0.401) — the SPD is not
  even needed, and BSW's crossing of the threshold turns it into a
  governing party. (Linke+Grüne+SPD, 81, remains a close, more conventional
  second.)
- **Conservative Shift** — the CDU grows and the FDP returns; the most natural
  government is **CDU + Grüne + SPD (68)**, a CDU-led Kenia.
- **Firewall Breaks** — the *same polls* as the Conservative Shift, but the
  Brandmauer is dropped. The most natural government becomes **CDU + AfD (67,
  naturalness 0.860)** — a right bloc that is *infeasible* in every other
  scenario (§8).

## 7. Two different policy projections

There are **two distinct questions**, and they give different answers:

- **Government projection** — *what the governing coalition will actually do.*
  The seat-weighted stance of the **main viable coalition**, with taboos
  applied. A *constrained* projection: only coalitions that can actually
  govern count.
- **Parliament projection** — *where the parliament's centre of gravity sits.*
  Weights **every party in the house by its power** (not just seats) and
  applies **no taboos** — the whole legislature, regardless of who governs.
  As §5 showed, with five equally powerful parties this is the simple average
  of the five parties' positions.

### 7.1 Government projection (coalition, taboos apply)

![Government policy by scenario]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-government-policy-by-scenario.svg)

The main coalition's seat-weighted position on each axis
(1 = left anchor, 10 = right anchor):

| Axis | Baseline<br>(Linke+Grüne+SPD) | Left-Green Surge<br>(Linke+Grüne+BSW) | Conservative Shift<br>(CDU+Grüne+SPD) | Firewall Breaks<br>(CDU+AfD) |
| --- | ---: | ---: | ---: | ---: |
| Housing | 8.40 | **9.29** | 4.62 | **2.27** |
| Transport | 8.51 | **9.31** | 4.85 | **1.81** |
| Mid-East | 5.54 | **6.64** | 2.32 | **1.27** |
| Security | 2.98 | **2.66** | 6.76 | **9.23** |
| Fiscal | 8.52 | **9.16** | 5.00 | **2.77** |
| Climate | 8.55 | **8.81** | 5.62 | **2.34** |

With the real polls, the most likely government is **left**: housing 8.40,
transport 8.51, fiscal 8.52, climate 8.55 — close to the left anchors — and
security 2.98 on the civil-rights side. A CDU-led government (Conservative
Shift) mirrors this: free-market housing (4.62), pro-car transport (4.85),
austerity (5.00), market climate (5.62), hard security (6.76), and a
deep Staatsräson posture (2.32).

**The RRG tension point.** The projected RRG government sits at **8.40 on
housing** — near the expropriation anchor. That is exactly where the real
coalition talks will strain: Left lead candidate Elif Eralp has made beginning the
expropriation of large housing companies a *red line* for entering any
coalition, while SPD lead candidate Steffan Krach has publicly refused to accept it.
The axis on which the RRG government will be made or broken is the one the
projection says it will govern hardest.

### 7.2 Parliament projection (all parties, no taboos, power-weighted)

![Parliament policy projection by scenario]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-parliament-policy-power-weighted.svg)

The whole parliament's power-weighted centre of gravity (all five parties,
**no taboos** — here equal power, so the simple average of the five):

| Axis | Baseline | Left-Green Surge | Conservative Shift | Firewall Breaks |
| --- | ---: | ---: | ---: | ---: |
| Housing | 5.70 | 6.28 | 4.64 | 4.64 |
| Transport | 5.60 | 6.20 | 4.41 | 4.41 |
| Mid-East | 3.50 | 4.00 | 3.02 | 3.02 |
| Security | 5.70 | 5.25 | 6.71 | 6.71 |
| Fiscal | 6.00 | 6.50 | 4.96 | 4.96 |
| Climate | 5.90 | 6.35 | 4.77 | 4.77 |

*(Firewall Breaks is identical to the Conservative Shift here: the parliament
projection weights **all** parties and applies **no taboos**, so breaking the
firewall — which only changes which *government* can form — leaves the
parliament's centre of gravity untouched.)*

**Why the two differ.** The government projection is more *extreme* than the
parliament projection, because the government is a **subset** (the governing
coalition) while the parliament includes *all* parties. In the baseline, the
RRG government pushes housing to **8.40**, but the parliament as a whole
—which still contains the CDU (30) and the AfD (27) — sits at **5.70**: the
out-of-government parties pull the legislative centre back toward the middle.
So **what gets enacted** (government) is further from the centre than
**where the parliament sits** (parliament).

### 7.3 Per-dimension power index (where the contested axes are pulled)

![Per-dimension power projection by scenario]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-parliament-policy-per-dimension.svg)

Weighting each party by `power × |stance − 5.5|` (its *pull* on each axis)
amplifies the polar parties — those with both high power and a stance far from
the centre. The result shows **where power is most concentrated** on each axis:

| Axis | Baseline | Left-Green Surge | Conservative Shift | Firewall Breaks |
| --- | ---: | ---: | ---: | ---: |
| Housing | 6.07 | 6.75 | 4.87 | 4.87 |
| Transport | 5.68 | 6.38 | 4.33 | 4.33 |
| Mid-East | **3.09** | **3.58** | **2.62** | **2.62** |
| Security | 5.93 | 5.33 | **6.93** | **6.93** |
| Fiscal | 6.56 | 7.10 | 5.37 | 5.37 |
| Climate | 5.83 | 6.40 | 4.59 | 4.59 |

**Reading:** the per-dimension index pulls the **Mid-East** hard toward the
Staatsräson pole (2.62–3.58) in *every* scenario — even under a left
government — because the whole Berlin spectrum, from Grune to CDU (excepting slightly die Linke), sits on
that side of the axis; it is a **consensus axis**. **Security** is different:
it tracks *which bloc governs* — civil-rights-leaning (5.33–5.93) under left
governments, law-enforcement-leaning (6.93) under a CDU-led one. By contrast,
**housing, transport, fiscal and climate** stay split around the centre
(4.3–7.1): power is *contested* on those axes, so the governing coalition's
identity — not small poll wiggles — decides the outcome.

## 8. Breaking the firewall: the CDU–AfD breakthrough

The three polling scenarios all keep the **Brandmauer** in force — the AfD is
excluded from *every* governing coalition. The fourth scenario — **Firewall
Breaks** — asks the question the other three cannot: *what if the firewall
falls?* It holds the Conservative Shift polls fixed and simply drops the
taboo, so the same parliament (same seats, same centre of gravity) is free to
form a government that includes the AfD.

**Why the CDU is the break point.** When the firewall falls, it does not break
evenly — it breaks at the **CDU**, for two reinforcing reasons. First, the CDU
is essentially tied with the FDP for closest to the AfD in the 6-axis policy
space (proximity 0.860 vs 0.851), and far closer than SPD (0.682), BSW
(0.447), Grüne (0.369) or Die Linke (0.228). Second — and decisive — the CDU
is the **only party large enough to form a majority with the AfD**:
CDU+AfD = 67 seats, just over the 66-seat majority, while AfD+Linke (53),
AfD+SPD (47), AfD+Grüne (47) and AfD+FDP (40) fall far short. So the CDU is
both the most natural and the only *possible* partner — if the firewall
breaks, it breaks here.

The effect is immediate and one-directional. With the taboo gone, **CDU+AfD
(67 seats)** becomes the single most natural coalition (naturalness 0.860 —
more than double the leading coalition of any other scenario) and it takes
power. Because CDU and AfD sit close together in policy space on most axes,
the government's position jumps toward the **right anchor on every axis**:

- **Housing 4.62 → 2.27, Transport 4.85 → 1.81, Fiscal 5.00 → 2.77, Climate
  5.62 → 2.34** — free-market housing, pro-car transport, austerity, and a
  market-based climate stance.
- **Mid-East 2.32 → 1.27** — even harder on the Staatsräson pole.
- **Security 6.76 → 9.23** — the hardest law-enforcement position of any
  scenario.

Two things stand out. First, the shift is **large and uniform**: every axis
moves right, by 1.1–3.3 points — far bigger than any polling nudge in §9.
The firewall is not a small correction; it is the single largest policy lever
in the model. Second, the **parliament is unchanged** (§7.2–7.3): breaking the
firewall moves the *government* to the right without moving the *parliament*
at all. That is exactly the difference between the government and parliament
projections, made visible.

**The takeaway:** the Brandmauer is what keeps a right-leaning parliament from
producing a far-right government. While it holds, the most natural government
in the Conservative Shift is the CDU-led **CDU+Grüne+SPD**, and the AfD's
polling rise is — remarkably — **policy-irrelevant** (see the §9 sensitivity:
+2 AfD / −2 CDU moves *no axis at all*). The moment the firewall breaks — and
it can only break at the CDU — the same house yields a **CDU+AfD** government
that is right on *every* axis.

## 9. Policy sensitivity: what the polls can still change

The scenarios of §3–§8 are *story* scenarios — clean, interpretable, and far
apart from each other. The question a campaign actually asks is different:
**starting from the most likely polls, what can still move, and by how much?**
So instead of moving the polls in wide arcs, we confine the variation to a
realistic error band around the current baseline, and run the *full* chain —
seats → most likely government → **government policy on all six axes** *and*
**the whole parliament's policy on all six axes** — for every variation.

### 9.1 Two layers of variation around the most likely polls

**Layer 1 — a deterministic grid of 41 bounded variations.** Every
variation is anchored on the §2 baseline, zero-sum (whatever one party gains,
another loses), and grouped in four families:

- **Single-party sweeps (14):** each party ±3 points, compensated pro-rata
  by the other in-house parties (by "Others" for BSW/FDP).
- **Paired swings (21):** all 20 direct donor → recipient transfers of 4
  points among the five in-house parties, plus a 2-point CDU → AfD probe.
  This includes the case of the **AfD overtaking the CDU** (CDU 16.0 / AfD
  21.5).
- **Threshold pins (4):** BSW and FDP each pinned at 4.5 (just out) and 5.5
  (just in).
- **Bloc drifts (2):** the whole left bloc (Linke/Grüne/SPD) against the
  whole right bloc (CDU/AfD), drifting 6 points pro-rata in either
  direction — the edges of the band, where the biggest single-party move
  is 3.2 points (the CDU) and the point is that *all five* parties move in
  the same direction at once.

**Layer 2 — a Monte Carlo over the whole band (20,000 draws).** Instead of
picking the variations by hand, each party's share is drawn from a normal
whose standard deviation is *measured*, not assumed: the standard deviation
of that party across the last eight polls (fieldwork 4 Aug – 14 Sep, with the
BSW party-commissioned outlier excluded exactly as in §2):

| Party | σ (pts) | Party | σ (pts) |
| --- | ---: | --- | ---: |
| CDU | 0.99 | Die Linke | 1.51 |
| SPD | 1.77 | AfD | 0.46 |
| Grüne | 0.93 | BSW | 0.71 |
| FDP | 0.45 | | |

Each draw is renormalized to sum to 100 and run through the full engine.

### 9.2 The scenario grid: 41 variations, both projections

The complete result. **Government** = the most-likely (main) coalition's
seat-weighted policy; **parliament** = the power-weighted centre of gravity
of the whole house. Values are *deltas vs the baseline*; "—" means exactly
0.00 on all six axes (Hou = Housing, Tra = Transport, Mid = Mid-East, Sec =
Security, Fis = Fiscal, Cli = Climate; 1–10 scale).

| Scenario | Main government (seats) | **Government Δ** Hou Tra Mid Sec Fis Cli | **Parliament Δ** Hou Tra Mid Sec Fis Cli |
| --- | --- | --- | --- |
| **Current Baseline** | **Linke+Grüne+SPD (73)** | — | — |
| CDU +3 | Linke+Grüne+SPD (70) | −0.03 −0.04 0.00 +0.02 −0.02 −0.03 | +0.08 +0.06 +0.21 −0.06 +0.07 +0.05 |
| CDU −3 | Linke+Grüne+SPD (76) | −0.02 −0.01 −0.02 +0.01 −0.01 −0.01 | — |
| SPD +3 | Linke+Grüne+SPD (76) | −0.21 −0.22 −0.22 +0.19 −0.19 −0.15 | — |
| SPD −3 | Linke+Grüne+SPD (70) | +0.19 +0.19 +0.22 −0.17 +0.17 +0.12 | — |
| Grüne +3 | Linke+Grüne+SPD (76) | −0.02 +0.04 −0.12 +0.02 −0.02 +0.04 | — |
| Grüne −3 | Linke+Grüne+SPD (70) | −0.03 −0.10 +0.11 +0.01 −0.01 −0.09 | — |
| BSW +3 | Linke+Grüne+SPD (68) | −0.01 −0.01 0.00 +0.01 −0.01 −0.01 | +0.18 +0.13 +0.33 −0.05 +0.13 +0.05 |
| BSW −3 | Linke+Grüne+SPD (73) | — | — |
| Die Linke +3 | Linke+Grüne+SPD (76) | +0.10 +0.04 +0.24 −0.10 +0.10 0.00 | +0.08 +0.06 +0.21 −0.06 +0.07 +0.05 |
| Die Linke −3 | Linke+Grüne+SPD (70) | −0.15 −0.10 −0.28 +0.14 −0.14 −0.05 | — |
| AfD +3 | Linke+Grüne+SPD (70) | −0.03 −0.04 0.00 +0.02 −0.02 −0.03 | — |
| AfD −3 | Linke+Grüne+SPD (76) | −0.02 −0.01 −0.02 +0.01 −0.01 −0.01 | — |
| FDP +3 | Linke+Grüne+SPD (68) | −0.01 −0.01 0.00 +0.01 −0.01 −0.01 | −0.07 −0.08 +0.15 0.00 −0.10 −0.08 |
| FDP −3 | Linke+Grüne+SPD (73) | — | — |
| CDU → Die Linke +4 | Linke+Grüne+SPD (79) | +0.12 +0.07 +0.22 −0.11 +0.11 +0.03 | — |
| CDU → AfD +4 | Linke+Grüne+SPD (73) | — | — |
| CDU → Grüne +4 | Linke+Grüne+SPD (79) | +0.01 +0.07 −0.12 0.00 0.00 +0.07 | — |
| CDU → SPD +4 | Linke+Grüne+SPD (79) | −0.22 −0.23 −0.23 +0.19 −0.19 −0.16 | — |
| Die Linke → CDU +4 | Linke+Grüne+SPD (67) | −0.14 −0.09 −0.26 +0.13 −0.13 −0.04 | — |
| Die Linke → AfD +4 | Linke+Grüne+SPD (67) | −0.14 −0.09 −0.26 +0.13 −0.13 −0.04 | — |
| Die Linke → Grüne +4 | Linke+Grüne+SPD (73) | −0.12 0.00 −0.37 +0.12 −0.12 +0.04 | — |
| Die Linke → SPD +4 | Linke+Grüne+SPD (73) | −0.37 −0.33 **−0.49** +0.33 −0.33 −0.21 | — |
| AfD → CDU +4 | Linke+Grüne+SPD (73) | — | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| AfD → Die Linke +4 | Linke+Grüne+SPD (79) | +0.12 +0.07 +0.22 −0.11 +0.11 +0.03 | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| AfD → Grüne +4 | Linke+Grüne+SPD (79) | +0.01 +0.07 −0.12 0.00 0.00 +0.07 | — |
| AfD → SPD +4 | Linke+Grüne+SPD (79) | −0.22 −0.23 −0.23 +0.19 −0.19 −0.16 | — |
| Grüne → CDU +4 | Linke+Grüne+SPD (**66**) | −0.01 −0.10 +0.16 0.00 0.00 −0.10 | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| Grüne → Die Linke +4 | Linke+Grüne+SPD (73) | +0.12 0.00 +0.37 −0.12 +0.12 −0.04 | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| Grüne → AfD +4 | Linke+Grüne+SPD (67) | −0.01 −0.09 +0.14 0.00 0.00 −0.09 | — |
| Grüne → SPD +4 | Linke+Grüne+SPD (73) | −0.25 −0.33 −0.12 +0.21 −0.21 −0.25 | — |
| SPD → CDU +4 | Linke+Grüne+SPD (67) | +0.26 +0.27 +0.27 −0.23 +0.23 +0.18 | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| SPD → Die Linke +4 | Linke+Grüne+SPD (73) | **+0.37** +0.33 **+0.49** −0.33 +0.33 +0.21 | +0.16 +0.11 +0.43 −0.13 +0.14 +0.10 |
| SPD → AfD +4 | Linke+Grüne+SPD (67) | +0.26 +0.27 +0.27 −0.23 +0.23 +0.18 | — |
| SPD → Grüne +4 | Linke+Grüne+SPD (73) | +0.25 +0.33 +0.12 −0.21 +0.21 +0.25 | — |
| CDU → AfD +2 | Linke+Grüne+SPD (73) | — | — |
| BSW 4.5 (just out) | Linke+Grüne+SPD (73) | — | — |
| BSW 5.5 (just in) | Linke+Grüne+SPD (68) | −0.01 −0.01 0.00 +0.01 −0.01 −0.01 | +0.18 +0.13 +0.33 −0.05 +0.13 +0.05 |
| FDP 4.5 (just out) | Linke+Grüne+SPD (73) | — | — |
| FDP 5.5 (just in) | Linke+Grüne+SPD (68) | −0.01 −0.01 0.00 +0.01 −0.01 −0.01 | −0.07 −0.08 +0.15 0.00 −0.10 −0.08 |
| Left bloc +6 / right −6 | Linke+Grüne+SPD (82) | −0.03 −0.04 0.00 +0.02 −0.02 −0.03 | — |
| **Right bloc +6 / left −6** | **CDU+Grüne+SPD (72) \*** | **−3.48 −3.31 −3.09 +3.49 −3.25 −2.63** | **−0.99 −1.10 −0.64 +1.01 −0.93 −1.04** |

\* the one scenario that changes the *identity* of the main government.

### 9.3 The most likely government: six axes that barely move — and the one flip

**The government is almost rock-solid.** 40 of the 41 variations keep
Red–Red–Green as the most likely government, with RRG's seat count ranging
from 66 (Grüne → CDU +4, *exactly* at the majority line) to 82 (left bloc
drift). The single flip is the full **6-point rightward drift**: the left
bloc shrinks just enough that RRG falls short of 66 (Linke 27 + Grüne 21 +
SPD 16 = 64) and the Kenia coalition (CDU 35 + Grüne 21 + SPD 16 = 72)
becomes the *only* viable government. There the government jumps by about
**three points on every axis** — housing 8.40 → 4.92, Mid-East 5.54 → 2.45,
security 2.98 → 6.47, fiscal 8.52 → 5.27. Note what that scenario is *not*:
no single party moves by more than 3.2 points (the CDU) — the extremity is
in the *coordination*, all five parties moving in the same direction at
once, not in any one party's move. It is the closest the grid gets to a
common shock like the post-Wegner step-down.

**Seven scenarios move the government by exactly zero** — and two of them are
the dramatic ones: the **AfD overtaking the CDU** (CDU 16.0 / AfD 21.5, at
+2 and at +4) and its mirror (AfD 13.5 / CDU 24.0). As long as the
Brandmauer holds, the AfD's polling trajectory is *completely*
policy-irrelevant for the government: it adds seats only to a party that no
coalition may contain, so the governing coalition — and its policy — cannot
see it. (The BSW/FDP "just out" pins are the same story at the 5% line:
below the threshold a party is arithmetically invisible.)

**Within RRG, policy moves by at most 0.49** — on Mid-East — and only when
the coalition's *internal weights* are reshuffled: a 4-point exchange
between the SPD and Die Linke (8.1/16.4 → 16.1/8.1). The sensitivity
follows the *stance gap inside the coalition*, not the axis importance:
Mid-East is the most sensitive because Linke (8.5) and SPD (2.5) are 6
points apart inside RRG, while climate is the least (Linke 9.0 vs SPD 6.5,
a 2.5 gap). Housing (≤0.37), transport, security and fiscal (≤0.33) sit in
between. None of these is a direction change — they are re-weightings of
the *same* left government.

### 9.4 The parliament: rigid, with exactly three ways to move it

**28 of the 41 scenarios leave the parliament's centre of gravity exactly
where it is** (5.70 / 5.60 / 3.50 / 5.70 / 6.00 / 5.90). This is structural,
not accidental: as long as the same five parties are in the house and no
pair reaches 66 seats while every trio does, the perfect five-way power tie
of §5.1 holds — and the power-weighted parliament then reduces to the
*simple average of the five parties' positions*, a number that does not
depend on the seat counts at all. Any seat redistribution that preserves
that geometry leaves the centre of gravity fixed, no matter how the polls
wiggle.

It moves, in the grid, in exactly three ways:

1. **The house composition changes.** BSW crossing the line (4.5 → 5.5, or
   the +3 sweep) puts a sixth party in the house and shifts the centre
   toward BSW's position (housing +0.18, Mid-East +0.33); FDP crossing
   shifts it toward the FDP's market anchors on the economic axes
   (fiscal −0.10, climate −0.08).
2. **The tie breaks.** When a swing lifts the CDU or the Linke so that the
   CDU–Linke pair itself reaches 66 seats (AfD → CDU +4 gives CDU 36 +
   Linke 31 = 67) — or, in the ±3 sweeps, when the smallest trio (SPD +
    Grüne + AfD) drops below it (65 in the CDU +3 case) — power is no longer
    equally split (raw Banzhaf: CDU 0.286 / Linke 0.286 / SPD, Grüne, AfD
    0.143 each). The centre of gravity then tilts toward the two giants:
    +0.16 housing, **+0.43 Mid-East**, −0.13 security. The *government* is
    untouched in all eight tie-break scenarios — it stays Red–Red–Green
    (any small government move there is the ordinary internal re-weighting
    of §9.3, not the tie-break).
3. **The bloc drifts far enough to change the house** — the flip scenario
   above, where the parliament itself moves a full point right (housing
   5.70 → 4.71, security 5.70 → 6.71).

Two things stand out in (2). First, in those scenarios the **AfD's
arithmetic power rises from 0 to 0.143** — the raw geometry of the house
has made it a pivot. But its *policy-weighted* (realistic) power stays at
exactly **0.000**, because the Brandmauer still bars every coalition it
could join: the AfD's polling rise is visible in the house's arithmetic
and inert in its policy. Second, the tilt shows up in the *parliament*,
not the government: in six of the eight scenarios the house's centre of
gravity moves further (up to 0.43) than the government's policy does,
while the government's identity never changes.

![Policy sensitivity fan]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-sensitivity-policy-fan.svg)

*Each panel: one policy axis. Dashed line + open dot: the baseline. Thin
black line: the deterministic grid range (non-flip scenarios). Blue bands:
the Monte Carlo p1–99 (light) and p5–95 (dark), with the median; red diamond
(the only one) marks the single government-identity flip. Top row: the most
likely government; middle row: the parliament (power-weighted); bottom row:
the parliament's per-dimension power projection. The contrast is the
finding: the government's bands are small but nonzero; the parliament's are
essentially points.*

### 9.5 The whole band at once: the Monte Carlo

| Question | Answer |
| --- | --- |
| P(Red–Red–Green is the most likely government) | **99.7%** |
| P(a CDU-led government — Kenia — is the most likely) | 0.3% |
| BSW clears the 5% line | 2.9% |
| FDP clears the 5% line | 0.0% |
| The perfect 5-way power tie breaks | 9.7% |
| The parliament moves > 0.05 on any axis | 8.9% |
| Government, max axis-move vs baseline (median / p95) | 0.12 / 0.30 |
| Parliament, max axis-move vs baseline (median / p95) | **0.00** / 0.21 |

The policy bands (p5 / median / p95 over the 20,000 draws):

| Axis | Government | Parliament |
| --- | ---: | ---: |
| Housing | 8.19 / 8.38 / 8.58 | 5.70 / 5.70 / 5.78 |
| Transport | 8.30 / 8.49 / 8.70 | 5.60 / 5.60 / 5.66 |
| Mid-East | 5.29 / 5.54 / 5.79 | 3.50 / 3.50 / 3.71 |
| Security | 2.82 / 2.99 / 3.16 | 5.64 / 5.70 / 5.70 |
| Fiscal | 8.34 / 8.51 / 8.68 | 6.00 / 6.00 / 6.07 |
| Climate | 8.40 / 8.53 / 8.67 | 5.90 / 5.90 / 5.95 |

*(Baseline government: 8.40 / 8.51 / 5.54 / 2.98 / 8.52 / 8.55; baseline
parliament: 5.70 / 5.60 / 3.50 / 5.70 / 6.00 / 5.90.)*

Read the parliament column first: on five of six axes the p5 is *the
baseline itself* — in 95% of draws the parliament is either exactly where
it started or shifted by the small tie-break / BSW-entry amounts (housing
up to +0.18, Mid-East up to +0.33); it moves nearly a full point only in
the rare 0.3% of draws where the bloc drifts far enough to flip the
government. Security is the mirror image (p5 5.64, below the baseline):
there the tie-break and BSW-entry scenarios shift the centre slightly the
other way, because the AfD — which sits at 9.5 on that axis — *loses*
weight when the tie breaks.

*Caveat:* the draws treat each party's error as independent. A **common
shock** that moves the whole field at once (a Wegner-style incident, a
scandal) is not what independent errors generate — its closest grid
analogue is the bloc drift, and we have seen that a coordinated 6-point
rightward drift is what flips the government. The Monte Carlo says such a
coordinated drift is *rare* inside the band (0.3% of draws); it does not
say it is impossible.

![Monte Carlo summary]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-ii-sensitivity-monte-carlo-summary.svg)

### 9.6 What this means for the campaign

- **The bloc question is effectively settled.** Inside the realistic
  polling band, RRG is the most likely government in 99.7% of draws. The
  campaign's remaining battles are therefore not about *whether* the left
  governs, but about (a) the **internal weights** of that government — the
  SPD ↔ Linke ↔ Grüne balance, worth at most ~0.5 on the most sensitive
  axis — and (b) **house entry**, where BSW's 2.9% threshold crossing is
  the most likely structural event and moves the parliament by ≤0.33.
- **Policy is flat inside the band and discrete at its edge.** A 1–4 point
  swing anywhere in the field moves the government by ≤0.49; the only
  in-band path to a different government is a *coordinated* 6-point bloc
  drift, which jumps policy ~3 points on every axis. There is no continuous
  middle ground — which is why the 5% line and the 66-seat line are the
  only real campaign battlegrounds.
- **The parliament is even more rigid than the government.** 28 of 41 grid
  scenarios (and 90% of the Monte Carlo draws) leave it exactly where it
  is: the CDU and the AfD — the parties *outside* the government — are what
  pin the house's centre of gravity at 5.70 / 5.60 / 3.50 / 5.70 / 6.00 /
  5.90. What gets *enacted* (the government) wiggles; where the *house
  sits* does not.
- **The firewall is the model's largest policy-irrelevance result.** Even
  an AfD that overtakes the CDU moves the projected government by **0.00**
  on every axis; its polling success converts into seats it can never
   convert into policy while the Brandmauer holds. §8 shows what the break
   costs: the same lever, flipped, is a 1–3 point move on every axis.

## 10. Why it still matters: votes set the weights, narratives set the anchors

§9 ends in something that can be read as an argument for staying home: the
bloc question is settled (RRG in 99.7% of draws), the parliament does not
move (90% of draws), and the AfD's rise changes nothing. But that reading
confuses one of the model's *inputs* with the model itself. The election
moves exactly one input — and it is not the only one that matters.

### 10.1 The model has three inputs; the vote moves one of them

Every number in this series is computed from three inputs:

1. **Poll shares** (→ 5% threshold → seats → coalitions) — what **voting**
   moves.
2. **The six-axis position matrix** (Post 1, §1 here) — where each party
   stands on housing, transport, Mid-East, security, fiscal, climate — what
   **programs and narratives** move.
3. **The taboo set** (the Brandmauer, the CDU–Linke incompatibility) — what
   **common knowledge** moves.

§9 held inputs 2 and 3 fixed and swept input 1. Its findings — a flat
government, a frozen parliament — are findings about *poll shares alone*.
They say nothing about the other two levers.

### 10.2 What the vote still decides: the government policy vector

What gets enacted comes from the **government policy vector** (§7), not
from the parliament's centre of gravity. That vector is where the polling
band still has real teeth:

- **The internal weights.** The RRG vector is the seat-weighted average of
  three parties (Linke 31, Grüne 24, SPD 18 — weights **0.42 / 0.33 /
  0.25**). §9 showed a 4-point SPD↔Linke exchange moves the vector by up to
  0.49 — and those seat shares are the *bargaining currency* of the
  coalition talks. The §7.1 housing red line is negotiated at exactly this
  scale: a party that wins or loses a few seats does not change the
  "average" so much as the price of the concessions it makes inside it.
- **House entry.** BSW's 2.9% threshold-crossing probability is the most
  likely structural event in the whole band; it moves the parliament's
  centre of gravity by up to 0.33 and changes which coalitions exist at
  all. The FDP mirror-image works the same way on the right.
- **The edge of the band.** The 6-point coordinated drift that flips the
  government is 0.3% of the Monte Carlo — a tail event, not an
  inevitability. The ballot is the only instrument that pushes the band
  back from that edge; no narrative holds a 66-seat line by itself.

So: the vote will not move the parliament's centre of gravity much — but it
sets the weights that decide (a) *which of the three left parties* prices
the government policy vector, (b) *who else is in the house*, and (c) how
close the field can come to a different government.

### 10.3 What the vote cannot do: the narrative's leverage

Now hold the polls fixed and move the position matrix instead — the effect
of **programs and narratives**. The model quantifies it directly (1–2 point
shifts of a party's stance, everything else fixed):

| Lever | Government vector (max axis move) | Parliament centre of gravity |
| --- | ---: | --- |
| 3-point poll swing (one party) | ≤ 0.28 | 0.00 in 10/14; ±0.21 (tie break), ±0.33 (BSW entry) |
| 4-point poll swing (paired) | ≤ 0.49 | 0.00 in 14/20; ±0.43 (tie break) |
| **1-point stance move — SPD (in government)** | **0.25** | **0.20** |
| **1-point stance move — Die Linke (in government)** | **0.42** | **0.20** |
| **2-point stance move — SPD housing (5.5 → 7.5)** | **0.49** | **0.40** |
| 1-point stance move — any out-of-government party (e.g. AfD) | 0.00 | 0.20 |
| 6-point coordinated poll drift (band edge, §9) | ~3.0 (flip) | ~1.0 |
| Firewall break (taboo change, §8) | 1.1–3.3 | 0.00 |

Three readings:

1. **A 2-point stance move matches the entire polling grid.** If the SPD's
   housing position shifts 5.5 → 7.5 — two points toward the expropriation
   anchor — the projected RRG government moves **8.40 → 8.89**: a +0.49
   shift, as large as the largest of all 41 polling scenarios, and the
   parliament follows by +0.40. The §7.1 fight over the housing red line
   is, in the model, a 0.49-point lever on the very axis the government is
   projected to govern hardest.
2. **The parliament is rigid to polls, not to positions.** The §9.4
   rigidity was a statement about *seat redistribution*. In the five-way
   tie, every party carries exactly 1/5 of the parliament's weight — so a
   1-point stance move by *any* party, even one that cannot govern, shifts
   the house's centre of gravity by 0.20 on that axis. The "frozen"
   parliament of §9.4 is movable by narrative — just not by any single
   party's polls.
3. **The leverage is unequal, and the inequality is the game.** Inside the
   government, a 1-point stance move by the Linke (0.42) is worth about 70%
   more than the same move by the SPD (0.25) — the seat weights do the
   pricing. And the two instruments *multiply*: a party that gains seats
   (vote) while moving its position (narrative) sees both effects compound
   on the same vector. The rational campaign objective is not "win" but
   "maximize my party's (seats × stance) on the axes I care about."

### 10.4 The model's biggest lever is already a narrative

The single largest policy result in this series is not a polling finding at
all. It is the **Brandmauer** — a taboo that exists as common knowledge, a
story the parties agree to tell. §5.2 and §8 quantified it: without it, the
same arithmetic geometry gives the AfD 0.166 of realistic power, and the
same Conservative-Shift parliament yields a CDU+AfD government that is
right on *every* axis (housing 2.27, security 9.23). The firewall is worth
**1.1–3.3 points on every axis** — more than any polling scenario in the
grid. Norms like this are narrative objects: they are made, kept and
broken by public argument, not by seat counts. And the polling record
itself shows fields moving on argument: after the CDU lead candidate's
step-down (10 Jul), the next Infratest dimap (13–15 Jul) had the Linke up
2 points (20 → 22), the AfD down 2 (18 → 16) and the CDU recovering 3
(17 → 20) — the whole field reshuffled 1–3 points by one event.

### 10.5 The division of labour

- **The vote sets the weights.** Who is in the house, which coalition
  governs, and the relative bargaining weight of the parties that do
  (0.42 / 0.33 / 0.25 — not 0.33 / 0.33 / 0.33).
- **The narrative sets the anchors.** Where each party stands on each axis:
  a 2-point stance move by one party shifts the *enacted* policy as much as
  the entire polling band — and it lasts a whole legislature, not an
  election result.
- **Common knowledge decides what the weights may apply to.** The taboos —
  firewall and incompatibility — are worth more than any poll swing, and
  they move by public argument, not by ballots.

The election decides who bargains. The campaign narratives decide what is
on the table. The taboos decide which deals can be signed at all.

## Bottom line

- **The polls have moved left, and the CDU is no longer the pivot.** Die Linke
  is the largest party in the projected house (31 vs 30), and — surprisingly —
  **all five parties in the house have exactly equal power (0.200)**: a
  perfect five-way tie, because no pair reaches a majority and every trio does.
- **Realistic power belongs to the left — and the firewall zeroes the AfD.**
  The policy-weighted indices (each swing weighted by the naturalness of the
  resulting government) put SPD and the Greens at 0.333 in the baseline
  (hinges of both viable governments), Die Linke at 0.205, the CDU at 0.129,
  and the AfD at exactly **0.000** despite 27 seats. Without the taboos the
  same weights would give the AfD 0.166 — the CDU–AfD proximity seduces the
  topology, and common knowledge is what restores sanity. Break the firewall
  and the CDU+AfD bloc alone captures 83% of realistic power (0.448 + 0.387).
- **One realistic government: Red–Red–Green (73 seats).** The Brandmauer plus
  the CDU–Linke incompatibility plus the Greens' no-Kenia red line rule out
  every other viable coalition. It would enact a left government (housing
  8.40, climate 8.55) while the parliament's centre of gravity stays moderate
  (5.70) — and its make-or-break file is **housing expropriation**.
- **What gets enacted ≠ where the parliament sits.** The governing coalition
  (constrained by taboos) enacts a more extreme policy than the whole
  parliament's power-weighted centre of gravity — the out-of-government
  parties pull the parliamentary centre back toward the middle.
- **The 5% threshold and the majority threshold are the real levers** — a
  couple of polling points put the BSW or the FDP in or out of the house, and
  a few more can flip the government from left-led to CDU-led.
- **Polling inside the realistic band changes little — asymmetrically.**
  A 20,000-draw Monte Carlo with error bands *measured* from the last eight
  polls keeps RRG as the most likely government in **99.7%** of draws: the
  government's max axis-move is 0.12 at the median (0.30 at p95), and the
  parliament does not move at all in 90% of draws. The only in-band path to
  a different government is a *coordinated* 6-point bloc drift, which jumps
  the government ~3 points on every axis. The AfD's polling rise on its own
  moves the projected government by exactly **0.00**.
- **The firewall is the decisive variable for how far right the government
  goes.** Holding the polls and the parliament fixed, breaking the Brandmauer
  turns the most natural government from a CDU-led Kenia into a
  **CDU+AfD** bloc that is right on every axis (housing 4.62→2.27, climate
  5.62→2.34, security 6.76→9.23) — a shift no amount of small polling
  movement produces.
- **Votes set the weights; narratives set the anchors.** The bloc question
  is nearly settled inside the band, but the government policy vector — the
  thing that gets enacted — is still decided by the seat weights (0.42 /
  0.33 / 0.25 inside RRG), by house entry, and by the parties' positions
  themselves: a 2-point stance move by one party (SPD housing 5.5 → 7.5)
  shifts the projected government by as much as the entire 41-scenario
  polling grid (8.40 → 8.89) — and the model's single biggest lever is
  already a narrative: the firewall, worth 1.1–3.3 points on every axis.

*All figures are computed by the reusable `scenario_engine.py` (edit
`SCENARIOS` / `POSITIONS` / `TABOOS` / `SCENARIO_TABOOS` to run your own polls
and firewall assumptions). `poll_analysis.py` reproduces the current-polls
picture from `data/polls_berlin_2026.csv`; `sensitivity.py` +
`sensitivity_charts.py` reproduce §9 (the 41-scenario grid and the 20,000-draw
Monte Carlo, with error bands measured from the last eight polls) from the
same data; the §10 stance-leverage figures are the same engine run with a
1–2 point shift applied to a party's row in `POSITIONS`. This is a
simulation, not a forecast — the counterfactual scenarios are illustrative
polling configurations, not predictions.*
