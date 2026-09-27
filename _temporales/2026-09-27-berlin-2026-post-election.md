---
title: 'Berlin Elections 2026 - (III) The result: landing on the tipping point'
excerpt: 'The official result through the engine of Posts 1-2: a power jump on exactly the line the model had drawn, a government vector that jumped, and a parliament that barely moved.'
date: 2026-09-27
permalink: /temporales/2026/09/berlin-elections-2026-iii-post-election/
header:
  overlay_image: blog/2026-09-berlin-elections/berlin_vector_berlin_votes_to_power_header.jpg
  overlay_filter: 0.4
  tall: true
tags:
  - politics
  - python
  - Data Analysis
  - Data visualization
---

# Post 3: The Result — Landing on the Tipping Point

*Continuation of [Post 1 — Looking into the Party Landscape]({{ base_path }}/blog/2026/09/berlin-elections-20-d-i-intro-analysis/) and [Post 2 — The Scenario Engine]({{ base_path }}/blog/2026/09/berlin-elections-2026-ii-scenario-engine/)*

Post 2 ended by mapping the election's **tipping points**: the specific
seat configurations at which the power distribution — and therefore the
policy center of gravity (CoG) — would jump. Now the official result of the
20 September 2026 election is in, and the interesting question is not
*who won* (the polls said it), but **how close the result came to those
lines** — and what it did to the power structure and the policy projections.

The short answer: **we landed on both power-geometry tipping points at
once, by the smallest margins possible (1 seat and 3 seats)** — the exact
double tie-break that Post 2 §9.4 had identified as the only mechanism by
which the house's arithmetic could change without the government changing.
The arithmetic power distribution jumped; the realistic power did not; the
government's policy vector moved left; and the parliament's center of
gravity barely moved. Every one of these is what the model said would
happen.

## 1. The result

Official allocation — **158 seats, 80 needed for a majority**:

| Party | Vote share | Seats | Δ vs 2023 | 5% threshold |
| --- | ---: | ---: | ---: | --- |
| **Die Linke** | **25.7%** | **47** | **+25** | in (1st place) |
| CDU | 18.8% | 34 | −18 | in |
| AfD | 16.3% | 29 | +12 | in |
| Grüne | 14.3% | 26 | −8 | in |
| SPD | 12.1% | 22 | −12 | in |
| BSW | 4.7% | 0 | — | out (0.3 pts short) |
| FDP | 2.5% | 0 | — | out |
| Others | 5.6% | 0 | — | out |

![Seat shifts 2023 to 2026]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-seats-2023-2026.svg)

**A note on the house size.** Posts 1–2 ran the engine on a 130-seat base
house (majority 66) as a simplification; the actual 2026 house has 158
seats (majority 80). Everything below is therefore re-run on the **real
158-seat house** — same allocation rule (largest-remainder, 5% threshold),
same six-axis positions, same taboo set.

**The final two weeks.** Compared with the last polling window
(6 polls, 13 Aug – 14 Sep), the election day result was a **concentrated
Linke surge**: Die Linke **+5.7**, BSW +0.9, SPD +0.1, FDP −0.8, AfD −1.2,
CDU −1.0, Grüne −1.4. No other party moved more than 1.4 points; the Linke
moved 5.7. The post-election record attributes the surge to housing and
tenants' rights — the single most decisive issue for over 50% of voters in
exit polls — and to Middle-East-related mobilization of young voters
(including newly eligible 16–17-year-olds) in inner-city districts.

## 2. Where the result landed among the scenarios

![Official result vs last polls and the four scenarios]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-result-vs-scenarios.svg)

Distance to the Post 2 scenarios (root-mean-square of the vote-share
deltas):

| Scenario | RM over 5 in-house parties | RM over all 7 |
| --- | ---: | ---: |
| Current Baseline | 2.55 | 2.19 |
| Left-Green Surge | 3.28 | 2.82 |
| Conservative Shift / Firewall Breaks | 5.93 | 5.22 |

**The result is not one of the four scenarios — it is the baseline plus a
concentrated Linke surge.** The left bloc (Linke+Grüne+SPD) gained +4.1
points overall (48.0 → 52.1) — about half of the full Left-Green Surge
scenario (+9.0) — while the right bloc (CDU+AfD) lost −2.4. The Linke's
25.7% even exceeds the Surge scenario's 24.0%, but *without* the
accompanying Greens/SPD/BSW movement the Surge implies. The Conservative
Shift and Firewall Breaks scenarios are far away: the result landed on the
left side of the baseline, not the right.

What matters most: **the government question did not move.** In the
baseline and the Surge scenario alike, the most likely government is a
left one without the CDU (RRG in the baseline; Linke+Grüne+BSW in the
Surge, where BSW clears the threshold) — and the actual result gives RRG
47+26+22 = **95 of 158 seats, a +15 margin**, up from the +9 margin the
baseline polls projected. The flip scenario (T1 below) did not fire, and
the only scenarios with a CDU-led government (Conservative Shift,
Firewall Breaks) are the two the result is farthest from.

## 3. The power jump: prediction vs actual, same house

Here is where it gets interesting. Evaluate the **prediction** (the
baseline polls of Post 2 §2) and the **actual result** in the *same*
158-seat house:

| | Prediction (baseline polls) | Actual (official result) |
| --- | --- | --- |
| Seats | CDU 37 · Linke 38 · AfD 32 · Grüne 29 · SPD 22 | CDU 34 · **Linke 47** · AfD 29 · Grüne 26 · SPD 22 |
| Largest pair (CDU+Linke) | 75 (< 80) | **81 (≥ 80)** |
| Smallest trio (SPD+Grüne+AfD) | 83 (≥ 80) | **77 (< 80)** |
| Perfect 5-way power tie | yes | **no** |
| Viable coalitions | RRG (89) · Kenia (88) | **RRG (95)** · Kenia (82) |
| Main coalition | RRG (naturalness 0.273) | RRG (naturalness 0.273) |

The prediction sat **on the edge of the tie-break geometry**: the
CDU–Linke pair was 5 seats short of being a majority, and the smallest
trio was 3 seats over. The final two weeks pushed the house across
**both** lines at once.

![Arithmetic power jump vs unchanged realistic power]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-power-jump.svg)

**The arithmetic power jumped.** In the predicted house the perfect 5-way
tie held, so every party — including the AfD — had exactly 0.200 of the
Banzhaf power. In the actual house the tie is broken and power
**concentrates on the two giants**: the CDU and the Linke (the pair that
now *is* a majority) each jump to **0.286** (Shapley–Shubik 0.300), while
the SPD, the Grüne and the AfD all fall to **0.143** (0.133). The CDU —
the party that just lost 18 seats — is now one of the two most powerful
parties in the arithmetic of the house.

**The realistic power did not move at all.** The policy-weighted indices
(each swing weighted by the naturalness of the resulting government,
taboos applied) are **identical** in prediction and actual: SPD 0.333,
Grüne 0.333, Linke 0.205, CDU 0.129, **AfD 0.000**. The reason is the
one Post 2 kept repeating: realistic power depends on *which coalitions
can form*, and the feasible set is unchanged — RRG and Kenia, exactly as
before. The tie-break changed the house's arithmetic; the **Brandmauer
and the CDU–Linke incompatibility absorbed it**. The AfD's 29 seats are
arithmetically pivotal (0.143) and, at the same time, completely
powerless in policy (0.000) — the "topology-only trap" of Post 2 §5.2,
now measured on the real house.

## 4. The tipping points: we landed on both, by 1 seat and 3 seats

Post 2 §9.4–§9.5 identified five tipping points — the configurations at
which something structural changes. Here is where the prediction sat and
where the result landed:

| # | Tipping point | Prediction (158-seat) | Actual (158-seat) | Fired? |
| --- | --- | --- | --- | --- |
| T1 | RRG falls below the majority (government flip to Kenia) | margin +9 | **margin +15** | no — moved away |
| T2 | CDU+Linke pair reaches the majority (a pair *is* a majority) | 75 (5 short) | **81 (1 over)** | **yes** |
| T3 | Smallest trio (SPD+Grüne+AfD) falls below the majority (a trio *loses*) | 83 (3 over) | **77 (3 short)** | **yes** |
| T4 | BSW or FDP crosses the 5% line (house composition changes) | BSW 3.7 / FDP 3.0 | **BSW 4.7** / FDP 2.5 | no — 0.3 pts short |
| T5 | Brandmauer breaks (CDU+AfD pair reaches the majority) | pair at 69 | **pair at 63** | no — 17 short |

![The five tipping points: prediction vs actual]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-tipping-points.svg)

Two readings:

- **The double tie-break (T2+T3) is the story of this election in the
  model's terms.** Both lines were crossed in the final two weeks, and
  both by the smallest margins the model tracks — **1 seat** on the pair
  (81 vs 80) and **3 seats** on the trio (77 vs 80). Post 2's grid had
  computed exactly what a tie-break does: it redistributes arithmetic
  power to the two giants and moves the parliament's center of gravity by
  up to 0.43 (largest on Mid-East). The actual result delivers exactly
  that — §5 shows the parliament moved 0.43 on Mid-East. Same mechanism,
  same magnitude, now on real data.
- **The two levers the campaign could still pull stayed closed.** The
  government flip (T1) moved *away* from the line (margin 9 → 15), and
  the threshold (T4) came within **0.3 points** (BSW 4.7) but did not
  cross — had it crossed, Post 2 §9 says the parliament would have moved
  by up to 0.33 and a sixth party would be in the house. The firewall
  (T5) held with 17 seats of margin, as the post-election record
  confirms: all parties maintain the Brandmauer, and the CDU still
  rejects coalition with the Linke — which is why the post-election
  debate describes the Left–Green–SPD coalition (95 of 158) as the
  primary viable path, exactly as the engine ranks it.

## 5. The policy center of gravity

With the seat vector and the power indices fixed, the policy projections
follow from the same seat-weighted formula as in Post 2:

| Vector (158-seat house) | Hou | Tra | Mid | Sec | Fis | Cli |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Outgoing gov 2023 (CDU+SPD, 86) | 3.69 | 3.69 | 1.90 | 7.62 | 4.19 | 4.69 |
| Prediction gov (RRG, polls, 89) | 8.40 | 8.51 | 5.55 | 2.98 | 8.52 | 8.54 |
| **ACTUAL gov (RRG, 95)** | **8.55** | **8.57** | **5.88** | **2.84** | **8.66** | **8.56** |
| Kenia alternative (actual seats, 82) | 5.21 | 5.52 | 2.56 | 6.16 | 5.55 | 6.21 |
| Parliament, prediction (power-weighted) | 5.70 | 5.60 | 3.50 | 5.70 | 6.00 | 5.90 |
| **Parliament, ACTUAL (power-weighted)** | **5.86** | **5.71** | **3.93** | **5.57** | **6.14** | **6.00** |
| Parliament, ACTUAL (per-dimension power) | 6.40 | 5.93 | 3.52 | 5.60 | 6.88 | 6.15 |

*(Hou = Housing, Tra = Transport, Mid = Mid-East, Sec = Security, Fis =
Fiscal, Cli = Climate; 1 = left anchor, 10 = right anchor.)*

![Policy center of gravity: government and parliament, prediction vs actual]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-center-of-gravity.svg)

**The government vector made the largest jump the series has produced.**
Outgoing → incoming: housing **+4.86**, transport +4.89, Mid-East +3.98,
fiscal +4.48, climate +3.87, security **−4.78** (toward the
civil-rights pole). The post-election record's own trajectory numbers
track the engine closely: the record puts the incoming government's
housing at ~8.6 (engine: 8.55), mobility/climate at ~8.8 (engine:
8.57/8.56) and security at 3.1 (engine: 2.84), and the outgoing
administration's security at 7.6 — the engine's CDU+SPD vector gives
**7.62**. The make-or-break file the record describes — the
expropriation of large real-estate firms and the rent freeze
(*Mietendeckel*) — sits exactly where the projection puts the government:
**8.55 on housing, 1.45 points from the expropriation anchor** (10.0).

**Actual vs prediction: small, and concentrated on the mobilization
axes.** The government vector moved only +0.15 (housing), +0.06
(transport), **+0.33 (Mid-East)**, −0.14 (security), +0.14 (fiscal),
+0.01 (climate) between the polls and election day. Why so little, if the
Linke surged 5.7 points? Because the government's *identity* never
changed — only its **internal weights** did: the Linke's share of the
RRG vector rose from 38/89 = 0.427 to **47/95 = 0.495** (Grüne 0.326 →
0.274, SPD 0.247 → 0.232). And Post 2 §9.3 said exactly where that kind
of re-weighting shows: on the axes with the largest stance gap *inside
the coalition* — the Mid-East, where the Linke (8.5) and the SPD (2.5)
are 6 points apart. The largest government delta is on the Mid-East
(+0.33), then housing (+0.15) — the two gaps of 6.0 and 4.5.

**The parliament stayed almost exactly where the model said it would.**
Actual vs prediction: +0.16 housing, +0.11 transport, **+0.43 Mid-East**,
−0.13 security, +0.14 fiscal, +0.10 climate. That is not zero — the
double tie-break moved it, by the predicted amount and in the predicted
direction (toward the two giants, largest on the Mid-East) — but it is
the parliament's *normal* movement under a tie-break, not a structural
shift. The house's center of gravity remains at ~5.9/5.7/3.9/5.6/6.1/6.0:
moderate on housing, firmly on the Staatsräson pole of the Mid-East,
roughly centered on security. **What gets enacted (the government, at the
left anchors) is far from where the house sits** — Post 2's
government-vs-parliament distinction, confirmed on the first real
result.

## 6. Where the winner does not fit: Die Linke vs the status quo

The cleanest way to read the post-election record is to measure **where
the winning party sits relative to the centre of gravity of the house it
just entered** — the model's parliament projection (power-weighted,
158-seat house, §5):

| Axis | Die Linke | Parliament CoG | Gap (Linke − CoG) | Distance | Partners CoG (Grüne+SPD) | Gap (Linke − partners) | Distance to partners |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Mid-East | 8.5 | 3.93 | +4.57 | **4.57** | 3.31 | +5.19 | **5.19** |
| Housing | 10.0 | 5.86 | +4.14 | **4.14** | 7.13 | +2.88 | **2.88** |
| Security | 1.5 | 5.57 | −4.07 | **4.07** | 4.15 | −2.65 | 2.65 |
| Fiscal | 10.0 | 6.14 | +3.86 | 3.86 | 7.35 | +2.65 | 2.65 |
| Transport | 9.5 | 5.71 | +3.79 | 3.79 | 7.67 | +1.83 | 1.83 |
| Climate | 9.0 | 6.00 | +3.00 | 3.00 | 8.13 | +0.88 | 0.88 |

*(Sorted by distance to the parliament CoG. Partners CoG = the
seat-weighted centre of the winner's anticipated RRG partners — Grüne
(26) and SPD (22) — on each axis.)*

**The top three axes by distance — Mid-East, housing, security — are
exactly the three topics the post-election record lists as driving the
debate.** In the record's own ordering housing is #1 ("the single most
decisive issue for over 50% of voters") and the Mid-East #2; by distance
the Mid-East leads by 0.4 points. That is the status-quo mismatch in one
table: the winning party governs from a position 4+ points away from the
centre of the house on precisely the axes the campaign mobilized on. The
chain the record implies — controversy on those topics, debates steered
toward them, attacks aimed at the winner on them — is, in the model, a
direct consequence of the Linke sitting farthest from the CoG on exactly
those axes.

**The same distance, against the government it will actually form.** The
last three columns repeat the measurement with a different reference: not
the whole house, but the seat-weighted centre of the winner's own
anticipated partners (Grüne 26 + SPD 22). Two things stand out. On the
Mid-East the winner sits *farther* from its future partners (5.19) than
from the whole parliament (4.57): both partners (Grüne 4.0, SPD 2.5) sit
at the opposite pole, so the axis where the whole house clusters against
the Linke is at the same time the widest gap *inside* the coming
government. On the other axes the internal gaps are far smaller than the
house gaps — climate 0.88, transport 1.83, fiscal and security 2.65 —
there the distance to the status quo is mostly a distance to the
opposition, not to the coalition. The one that matters is housing (2.88:
the Linke's 10.0 against its partners' 7.13) — the internal make-or-break
the record describes, the expropriation red line of §5.

The three topics have three different structures, and the record's
wording reflects each one:

- **The Mid-East is the discrepancy axis.** In the house, the CDU
  (1.5) and the AfD (1.0) — the two out-of-government parties — sit 0.5
  points apart at the pole opposite the Linke (8.5), and even the
  in-government SPD (2.5) and Grüne (4.0) stand 6.0 and 4.5 points from
  it. It is the only axis where all four non-Linke parties in the house
  cluster on one side (1.0–4.0) while the largest party sits alone on the
  other — the natural axis for a united opposition critique. And, as §7
  shows, it is the only axis where re-weighting the debate would flip the
  "natural" government to a CDU-led one.
- **Housing is the internal-government axis.** Inside RRG the Grüne
  (8.5) stand with the Linke (10.0) against the SPD (5.5), so the 4.14
  gap to the status quo plays out as an internal make-or-break (the
  expropriation red line, §5) rather than as an opposition attack. The
  record's framing — the Linke's surge "provides a direct mandate" to
  execute expropriation and the rent freeze — is the coalition-internal
  version of the same distance.
- **Security is the divided axis.** The CDU (9.0) and the AfD (9.5) sit
  7.5 and 8.0 points from the Linke (1.5), but the Grüne (3.0) and the
  SPD (5.5) stand in between — so the right can attack on security
  without being able to unite the house behind the attack. That is
  precisely what the record describes: "the debate remains divided
  between conservative demands for expanded law enforcement powers
  (pushed by CDU and AfD) and left-wing demands for civil rights
  protections."

The two over-focused topics (housing, Mid-East) are also, as §5 showed,
the government vector's two largest deltas (+0.15, +0.33): the campaign's
attention structure, the coalition's sensitivity structure, and the
winner's distance from the status quo all point at the same axes.

**And the record shows the §7 narrative lever in action after the vote.**
Given the result, the seats are fixed: the only way to still change who
governs — to close the power gap between the two viable coalitions — is
to make the less natural one (the CDU-led Kenia) look more natural. §7
says that requires over-focusing on the one axis where the natural
coalition is internally divided: the Mid-East, where the Linke (8.5) and
the SPD (2.5) sit 6 points apart inside the RRG — i.e. campaigns that
change the given narratives on exactly that axis. That is what the
post-election antisemitism campaign did. The pro-Palestinian positions
that drove the Linke's surge (the +5.7 mobilization axis, §1) were
re-coded as antisemitism — in German public argument the two are
routinely conflated — and within days the question dominating the
coverage was no longer who had won but whether the Linke could govern
at all (the governability debate,
[tagesschau, 22 Sep 2026](https://www.tagesschau.de/inland/regional/berlin/rbb-debatte-ueber-regierungsfaehigkeit-der-linken-reisst-alte-wunden-auf-102.html)).
The campaign was read as having precisely the function the model
predicts: a sociologist describing the debate said its function was to
put pressure on the Linke — and on the SPD and the Grüne — so that they
do not coalise with it, or to weaken the Linke's other issues in
coalition talks
([taz, 23 Sep 2026](https://taz.de/Linke-und-Antisemitismus/!6215302/)).
The Linke's own Palästina-LAG had called the wave a "tiring media
campaign," and party figures rejected the accusations as a smear
([B.Z. Berlin](https://www.bz-berlin.de/berlin/ulrike-eifler-und-die-linke-das-antisemitismusproblem-ist-real-6aae46f8b1857e86757a6f4c);
[ruhrbarone, 8 Sep 2026](https://www.ruhrbarone.de/die-linke-berlin-antisemitismus-im-gepaeck-das-freizeitprogramm-steht/265836/)).
And the target was moving: the prospective partners were publicly
drawing further red lines before any left coalition
([WELT, 25 Sep 2026](https://www.welt.de/politik/deutschland/plus6ab383ffa15a9fecb668c756/linke-das-war-auch-die-haltung-der-nazis-wirft-gysi-dann-merz-vor.html)),
on a question the pre-election wave had already put on the agenda —
"how deep antisemitism sits in the Berlin Linke"
([Tagesspiegel, 1 Sep 2026](https://www.tagesspiegel.de/berlin/judenhass-in-den-eigenen-reihen-so-tief-sitzt-der-antisemitismus-in-der-berliner-linkspartei-16001270.html)).
The vote was already in; what the campaign moved was the salience of
the RRG's internal discrepancy axis — the lever of §7. Whether that
alone flips the naturalness ranking (the model says it needs the
Mid-East weighted ≈3.1×) is what the coming coalition talks will
measure.

Selected German coverage of the wave (30 Aug – 25 Sep 2026):

| Date | Source | Story |
| --- | --- | --- |
| 30 Aug | [Tagesspiegel](https://www.tagesspiegel.de/berlin/yalla-yalla-intifada-offener-judenhass-im-wahlkampf-der-neukollner-linken--grune-zweifeln-an-regierungsfahigkeit-15997499.html) | Neukölln rally — "Yalla Yalla Intifada": the Grüne publicly doubt the Linke's government capability |
| 1 Sep | [Tagesspiegel](https://www.tagesspiegel.de/berlin/judenhass-in-den-eigenen-reihen-so-tief-sitzt-der-antisemitismus-in-der-berliner-linkspartei-16001270.html) | "How deep antisemitism sits in the Berlin Linke" — the accusation wave peaks pre-election |
| 7 Sep | [Tagesspiegel](https://www.tagesspiegel.de/berlin/yalla-yalla-intifada-polizei-ermittelt-nach-umstrittenem-konzert-bei-neukollner-linken-16025615.html) | Police open an investigation into the Dahabflex appearance at a Linke event |
| 8 Sep | [ruhrbarone](https://www.ruhrbarone.de/die-linke-berlin-antisemitismus-im-gepaeck-das-freizeitprogramm-steht/265836/) | Chronicle of the inner fight; the party's own Palästina-LAG calls the criticism wave a "tiring media campaign" |
| 18 Sep | [Tagesspiegel](https://www.tagesspiegel.de/berlin/antisemitismus-und-anti-polizei-plakate-elif-eralp-geraet-beim-tagesspiegel-hauptstadtgesprach-in-erklarungsnot-16071379.html) | Eralp in *Erklärungsnot* over the antisemitism accusations in the last pre-election debate |
| 22 Sep | [tagesschau](https://www.tagesschau.de/inland/regional/berlin/rbb-debatte-ueber-regierungsfaehigkeit-der-linken-reisst-alte-wunden-auf-102.html) | "Can the Linke govern Berlin — and does it want to?" — the governability debate becomes the dominant frame |
| 23 Sep | [taz](https://taz.de/Linke-und-Antisemitismus/!6215302/) | Sociologist Ullrich: the debate's function is pressure on the Linke, SPD and Grüne not to coalise |
| 23 Sep | [3sat](https://www.3sat.de/kultur/kulturzeit/antisemitismusvorwuerfe-gegen-die-linke-berlin-sendung-vom-23-09-2026-100.html) | Kulturzeit devotes a 36-minute segment to the accusations against the Berlin Linke |
| 25 Sep | [WELT](https://www.welt.de/politik/deutschland/plus6ab383ffa15a9fecb668c756/linke-das-war-auch-die-haltung-der-nazis-wirft-gysi-dann-merz-vor.html) | Gysi–Merz exchange escalates; Grüne and SPD draw further red lines before a left coalition |
| 25 Sep | [Tagesspiegel](https://www.tagesspiegel.de/berlin/kann-die-linke-berlin-regieren-gebt-elif-eralp-eine-faire-chance-16090239.html) | Counter-voice: "Give Elif Eralp a fair chance" |

**The firewall is the record's quietest — and the model's loudest —
finding.** The AfD gained 12 seats (29) but *lost* in the final window
(−1.2), and the post-election record confirms that all parties maintain
the Brandmauer. In the model's terms that is the entire story of the
AfD's result: the tie-break made the AfD **arithmetically pivotal**
(0.143 — it swings the house in combinations no coalition may form), and
the firewall converted that back to **0.000 realistic power**. The AfD's
29 seats did not buy a single point of government policy — the
government's vector moved *left*, not right, in the final window. Post 2
§10.4 called the firewall the model's biggest narrative lever (worth
1.1–3.3 points on every axis); the post-election result is the first
real-world observation of it holding. Norms of that kind are made, kept
and broken by public argument, not by seat counts — and this one held.

**And the closest call of the election was a model line, not a podium
position.** BSW's 4.7% sits 0.3 points below the 5% threshold — the T4
tipping point. The post-election record notes the BSW's continued
relevance in the debate; the model notes that the single most likely
structural event of the *next* election, if the current band holds, is
BSW entry — which Post 2 §9 priced at up to 0.33 of parliament movement
and a change in the set of feasible coalitions.

## 7. Re-weighting the axes: when would a CDU-led government be "natural"?

**Setup.** The engine's naturalness (the product of pairwise policy
proximities, Post 1) treats the six axes as equally important. But a
campaign never argues in an equal-weight space: salient topics weigh
more. Parties can decide where to put the focus, media can follow and coalitions that used to be natural find their red lines or just simply re-prioritize.
If we **re-weight the axes** — change the importance of each
dimension — the parties' distances change, and with them the naturalness
ranking of the viable coalitions. In the real house the viable
governments are exactly two (RRG 95, Kenia 82 — every other majority
coalition contains a forbidden pair), so the question is a head-to-head:
*under which axis weights is the CDU-led coalition the more natural
government?*

**How the distance is computed.** Every party is a point in the six-axis
policy space of the position matrix (Post 1 §3) — the CDU at (2.5, 2.5,
1.5, 9.0, 3.0, 3.5), the SPD at (5.5, 5.5, 2.5, 5.5, 6.0, 6.5), the Grüne
at (8.5, 9.5, 4.0, 3.0, 8.5, 9.5) and Die Linke at (10.0, 9.5, 8.5, 1.5,
10.0, 9.0) for (Housing, Transport, Mid-East, Security, Fiscal, Climate).
The engine's pairwise **distance** is the Euclidean distance between those
points,

```text
d(p, q)  =  √  Σᵢ ( xₚ,ᵢ − x_q,ᵢ )²                over the six axes i
```

which lives on a 0 → 9√6 ≈ 22.0 scale (0 = identical on every axis,
22.0 = opposite on every axis). The engine maps it to a **proximity** in
[0, 1] by dividing by that maximum,

```text
proximity(p, q)  =  1 − d(p, q) / ( 9√6 )
```

and the **naturalness** of a coalition is the product of the proximities
of all its pairs (Post 1 §2): RRG multiplies Linke–Grüne, Linke–SPD and
Grüne–SPD; Kenia multiplies CDU–Grüne, CDU–SPD and Grüne–SPD. At equal
weights this is the engine's naturalness (RRG 0.273 vs Kenia 0.172), and
the CDU–Grüne pair sits at 0.369 — the weakest pair in either coalition.

**What re-weighting does.** Re-weighting an axis is exactly what a salient
topic does to this space: it stretches it along that axis. Give the
Mid-East axis a weight λ (the other five stay at 1) and the distance
becomes the weighted Euclidean distance

```text
d_λ(p, q)  =  √ ( Σᵢ≠Mid ( xₚ,ᵢ − x_q,ᵢ )²  +  λ ( xₚ,Mid − x_q,Mid )² )
```

(first sum over the other five axes), with the normalization following the
stretch — the maximum weighted distance is 9√(5+λ), so
proximity_λ(p, q) = 1 − d_λ(p, q) / ( 9√(5+λ) ). A pair's proximity then
moves in the direction set by one comparison only — **how far apart the
pair is on the emphasized axis, relative to its gaps on the other five**:

- a pair **close** on the emphasized axis is stretched *less* than the
  space itself — its normalized distance shrinks and its proximity
  **rises**;
- a pair **far** on the emphasized axis is stretched *more* than the
  space — its proximity **falls**.

As λ → ∞ the other five axes drop out entirely and the proximity of two
parties reduces to **1 minus their gap on the emphasized axis** (1 −
Δ/9): the space collapses onto its one-dimensional shadow along that
axis. The sweep λ = 1 → 16 moves continuously between the full
six-dimensional geometry and that shadow — nothing about the parties
changes, only which dimension the distance listens to.

**In plain terms.** Picture the parties as cities on a map, and the
distance between two parties as the distance between two cities.
Emphasizing one axis is like stretching the map along that one
direction: cities that were already close along the stretch get even
closer, cities that were far apart along it get pushed farther — while
everything in the other five directions is compressed by comparison. No
city has moved; only the shape of the map has changed.

That is exactly what it means for a single topic to dominate a debate.
On the Mid-East axis the CDU (1.5) sits next to both its Kenia partners
— the SPD (2.5) and the Grüne (4.0) — while Die Linke (8.5) sits alone
at the opposite end, 6 points from the SPD and 4.5 from the Grüne. If
the Mid-East were the only issue being talked about, the CDU would read
as a natural partner of both, and the Linke as an unnatural partner of
either — no matter what the five other issues say. The λ dial is that
made continuous: λ = 1 is the full six-topic conversation, and the
larger λ, the more the ranking is decided by a single topic.

Concrete case, Mid-East at λ = 8: the CDU and the Grüne are only 2.5
apart on the Mid-East (1.5 vs 4.0) — the smallest of their six gaps — and
their proximity rises from 0.369 to 0.525; Die Linke and the SPD are 6.0
apart (8.5 vs 2.5) — the largest of their six gaps — and their proximity
falls from 0.523 to 0.413. Same parties, same five other axes: the change
of focus alone re-arranged the geometry.

**Method.** Raise the weight λ of one axis (the others stay at 1), from
λ = 1 (equal weights — where the weighted computation reproduces the
engine's naturalness exactly: RRG 0.273 vs Kenia 0.172) up to λ = 16,
and recompute the proximities and the two coalitions' naturalness with
the weighted distances.

**Result: only one of the six axes can flip the ranking.**

| Axis emphasized (λ: 1 → 16) | Leader at λ = 16 | Flip point |
| --- | --- | --- |
| Housing | RRG (0.276 vs 0.155) | none — the left's lead *widens* |
| Transport | RRG (0.280 vs 0.103) | none |
| **Mid-East** | **Kenia (0.166 vs 0.370)** | **λ ≈ 3.1** |
| Security | RRG (0.315 vs 0.154) | none |
| Fiscal | RRG (0.315 vs 0.183) | none |
| Climate | RRG (0.379 vs 0.155) | none |

Interpretive "salience" regimes (the weight profile a campaign induces):
**mid-east-first** (Mid-East 8×) makes **Kenia the natural government**
(0.304 vs 0.186); **order-first** (security + Mid-East + fiscal at 6×)
keeps RRG but narrows the margin to 1.15 (0.249 vs 0.217, from 1.59 at
equal weights); housing-first, security-first, climate-first,
economy-first and mobility-first all keep RRG — mostly with a *wider*
margin (housing-first: 0.275 vs 0.159).

![Re-weighting the axes: the naturalness sweep]({{ base_path }}/images/blog/2026-09-berlin-elections/berlin2026-iii-naturalness-sweep.svg)

**Why only the Mid-East.** The CDU is 5.5–7.0 points away from the
Grüne on five of the six axes (the exception is the Mid-East, where they
are 2.5 apart) — so the CDU–Grüne pair (equal-weight proximity 0.369) is
the weakest pair inside any viable coalition, and emphasizing any of
those five axes penalizes Kenia — the only viable coalition containing
that pair — more than it penalizes RRG. The Mid-East is the structural
exception: there the CDU (1.5) and the Grüne (4.0) sit close together
while the Linke (8.5) is the outlier, 6 points from the SPD (2.5).
Weighting the Mid-East 8× pulls the CDU–Grüne proximity *up* (0.369 →
0.525) and pushes both left pairs *apart* (Linke–SPD 0.523 → 0.413;
Grüne–Linke 0.763 → 0.599) — and at **λ ≈ 3.1** (the Mid-East weighted
about three times as much as each of the other axes) the ranking flips:
the CDU-led coalition becomes the more natural one.

**Read with §6.** The Mid-East is simultaneously (a) the axis where the
winning party sits farthest from the status quo (4.57), (b) the only
axis where the whole other parties in the house align against the Linke,
and (c) the only axis where re-weighting the debate would flip the
natural government to the CDU. It is the axis of maximum structural
instability — and the record shows the campaign did mobilize around it,
with two opposing model effects: on the *vote-share* side it worked for
the Linke (the mobilization axis of the +5.7 surge), while on the
*naturalness* side it worked against the left (it is the axis that makes
Kenia natural). The seat result (RRG 95) says the vote-share effect
won — but if the Mid-East's effective salience had held at λ ≥ 3.1
through the coalition talks, the "natural" government the model would
point to is the CDU-led one, not the RRG.

**Scope note.** Re-weighting can only *reorder* the two viable
governments, not create a third. There is no "Grüne-led" or "SPD-led"
viable government in this house: the only majority *pair* (Linke+CDU, 81)
is forbidden, and every viable three-party coalition contains *both* the
Grüne and the SPD — they are the common hinge of RRG and Kenia. What the
axis weights change is not who is *possible* but which of the two is
*attractive* — and the taboos (a different lever, Post 2 §8) are what
keep a third option (CDU+AfD) off the table at all.

- **The winner's distance from the status quo points at the debate.** The
  Linke sits 4+ points from the parliament's center of gravity on exactly
  three axes — Mid-East (4.57), housing (4.14), security (4.07) — and those
  are the record's three debate topics. The Mid-East is the axis of maximum
  structural instability: the whole in-house opposition clusters against
  the Linke there, and it is the *only* axis whose re-weighting (λ ≈ 3.1)
  flips the "natural" government from RRG to a CDU-led Kenia — while
  emphasizing any other axis keeps or strengthens the left's naturalness.

Given the results of the election, the only way to change the final results and close power gaps is to make less natural colations seen as more natural.
The only way to achieve that effect is by over focusing on the axis that creates differences in the more natural coalition creating campaigns that change the given narratives.
This aligns with what we have seen after the elections with the smearing campaigns
to Die Linke and anti-semitism (usually conflated in Germany with Palestinian rights).
We can see that in the media articles cited above.

## Bottom line

- **The engine reproduces the official result seat for seat** (47/34/29/
  26/22 on the real 158-seat house) — and the result is not one of the
  four scenarios, but the **baseline plus a concentrated Linke surge**
  (+5.7 in the final window; left bloc +4.1, right bloc −2.4).
- **Red–Red–Green governs with 95 of 158 seats** (margin +15, up from the
  projected +9) — the government flip never came, and the firewall held
  with 17 seats of margin.
- **We landed on both power-geometry tipping points at once, by 1 seat
  and 3 seats.** The CDU+Linke pair crossed into majority (81 vs 80) and
  the smallest trio fell out (77 vs 80) — the double tie-break of Post 2
  §9.4, now measured on the real house.
- **Arithmetic power jumped; realistic power did not.** The perfect
  5-way tie (0.200 each) became CDU/Linke 0.286 and SPD/Grüne/AfD 0.143 —
  while the policy-weighted indices are *identical* to the prediction
  (SPD/Grüne 0.333, Linke 0.205, CDU 0.129, **AfD 0.000**): the Brandmauer
  absorbed the entire geometry change. The AfD is arithmetically pivotal
  and policy-irrelevant at the same time.
- **The government vector made the model's biggest leftward jump**
  (housing 3.69 → 8.55, security 7.62 → 2.84 between administrations),
  and actual-vs-poll difference was small (+0.33 max, on the Mid-East)
  because only the coalition's *internal weights* changed — the Linke now
  prices 0.495 of the vector, and the two over-focused campaign topics
  (Mid-East, housing) are exactly the two largest deltas.
- **The parliament's center of gravity barely moved** (+0.43 max, on the
  Mid-East — the tie-break's predicted signature): what gets *enacted*
  sits at the left anchors; where the *house* sits is almost unchanged.
- **The campaign's narratives and the model's levers line up:** over-focus
  moves shares toward the anchor party of the over-focused axis (input
  1); attacks move shares but not positions, so their effect on enacted
  policy is capped at re-weighting; and the firewall — a pure narrative
  object — is what keeps 29 far-right seats at 0.000 policy power.

