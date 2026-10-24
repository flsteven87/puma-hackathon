# Issue 6 companion — the five-factor rating at building level

| Field | Value |
| --- | --- |
| Parent topic | [Issue 6 — Old-building seismic resilience](issue-6-building-resilience.md) (official prompt, practice and evidence) |
| Design decisions | 2026-10-21: analyse by building without identifying individual buildings; keep the building analysis in its own document; answer the official prompt; one score per building and a top-share cut, first priority the top 1% |
| Evidence cutoff | Computation, high-rise parameter audit and currentness check 2026-10-23; F01/source audit 2026-10-22; other evidence 2026-10-21 (D03 historical permits, MOI smallest-statistical-area age groups, both Fire Department lists, city liquefaction polygons, designated renewal areas, D01/D02 organisation lists, NCREE Meinong/Hualien case export) |
| Status | Development analysis after exposure: every field, list and the 里 bands had been seen before the contract was written. No damage label is fitted |
| Publication | Aggregates only. The per-building table carries permit numbers and stays in private research custody |
| Lay page | [老屋健檢與都更研究](../demo/issue-6-building-rating.html), built from this method contract and its aggregate derivations (see §4) |

## 1. Decision

**Evidence — the prompt (parent §1):** the event organiser asks for a 危老耐震風險加權評級模型 that integrates building
age, structure, older population, liquefaction potential and narrow-lane rescue difficulty, to order old-
building health checks (老屋健檢) and public renewal (公辦都更). It sets no case limit and no programme
eligibility. The event is organised by 沈伯洋競選辦公室; this is independent research for a potential municipal decision, not a city commission.

**Selected research focus:** Of the prompt's two decisions—building investigation priority and site-level public-renewal assessment—this building analysis chooses the first for deeper study. IPI, the worked building and the population distribution address investigation selection. The site-level conditions remain a separate context and cannot be inferred from an individual building's index.

**Question under research:** what information and analysis would help municipal reviewers turn residents' safety concerns into earlier professional investigation and a suitable next action? The parent topic's bounded citizen sample includes safety concerns, co-owner disagreement and requests for coordination; it does not establish the dominant bottleneck or prove that a ranking resolves them. Existing municipal assessment and renewal procedures are the baseline, with actual candidate selection still unknown. The five-factor trial asks whether combining structural clues and older-population, rescue and ground context adds decision-relevant information beyond a simple age/storey/material rule. It is not yet an accepted inspection order.

**Interpretation and comparison boundary:** the percentile, the three increments and the top-share cuts are research choices. Their suitability and selection gain remain unproved. A future comparison must define the professional outcome, use a comparable candidate population and investigation volume, and distinguish the simple reference rule from the municipality's observed selection. Failure to add decision-relevant information requires revising or rejecting the combination. This is a proposed validation question, not a new test result or a condition delaying the hackathon demonstration. Village totals describe the selected set; public renewal additionally needs site-wide coverage and suitability evidence under the parent topic's existing contract.

**What each factor resolves to:**

| Factor in the prompt | Data | Finest level |
| --- | --- | --- |
| Age and structure | D03 permit: material, storeys, design era from the construction-permit date | Permit record; shared by its represented buildings |
| Liquefaction | Regional potential sampled at the permit's doorplates, averaged as an increment | Doorplate points; not a foundation diagnosis |
| Narrow-lane rescue | 搶救不易狹小巷道清冊, lanes with doorplate number ranges | Listed-address relationship; not observed access |
| Rescue access | 消防通道清冊, which names 里 and street stretches without numbers | Doorplates on the named stretch |
| Older population | MOI 最小統計區 five-year age groups, 65+ share | Smallest statistical area (median 216 residents) |

## 2. Sources (retrieved 2026-10-15 to 2026-10-22)

| Source | Use here | Limits |
| --- | --- | --- |
| D03 historical use permits (parent §5) | Material, storeys, 棟數, households (戶數), construction-permit date, doorplates | A permit is not a current building; ROC 51 is missing |
| Signed Tgbs class model (parent §4) through the parent's cleaned record table | Research approximation of class damage probability under the code design scenario, by class, storeys, design era and site zone | Low/mid classes plus supported RC/steel/SRC high and superhigh classes; not collapse; no Taiwan validation of the order |
| MOI 最小統計區 five-year age groups, 113Y12M (data.gov.tw 18255) and area boundaries, 2015 (data.gov.tw 25128), OGDL v1 | 65+ share of the smallest statistical area holding the building's doorplate; below 50 residents the next level up (CODE1), then the 里 registry (parent §5) | Registered population, not building occupants; 2015 boundaries against 2024 counts; 0.24% of scored buildings fall back to the 里 share |
| Fire Department F01 搶救不易狹小巷道清冊 (273-row original CSV, corroborated against the 1150730 PDF) and 消防通道清冊 (parent §5) | Rescue flag: a doorplate on a listed narrow lane, or on a street stretch the 消防通道清冊 names (community-participation entries excluded) | F01 dates differ by resource; only text-confirmed F01 scope is counted in the main scenario, possible scope is tested separately; unlisted is not confirmed access; 158 of 162 access entries placed, 18 of them partly |
| City liquefaction-potential polygons (parent §5) | Value at the doorplates | Area estimate, not a site diagnosis; export class1/2/3=HIGH/MED/LOW now verified against the original renderer and all136 geometries. Missing source coverage is not low susceptibility |
| Designated renewal areas (parent §5, public-renewal B) | Whether a building lies in a renewal-area piece | Designation, not a project |
| D01 organisation registration (file 2026-10-05) and D02 可輔導成立公寓大廈管理組織清冊 (115/07/17) | Route for buildings of 6 storeys or more | Registration, not activity |
| NCREE Meinong 2016 / Hualien 2018 case export (parent §5) | What to look at on site | Purposive case series |

## 3. Method (contract declared before the run)

**Pool (old buildings):** located D03 records that are new builds, not superseded by a later permit on the
same doorplate, with a use permit by ROC 85 (30 years in 2026, the age threshold of the city's assessment
programmes). Counts are in buildings (棟數); a D03 record covers one or more buildings, and each inherits
the record's fields because the permit carries none per building. Low/mid material coverage is unchanged. The upstream archive is re-audited before its old class filter: 2,907 eligible tall records represent 3,808 buildings. Of these, 2,896 records / 3,796 buildings have explicit pure RC, steel or SRC labels and enter the calculation; 11 records / 12 buildings remain unscored because their material is mixed, blank, unsupported or implausible. The admitted scored pool is 25,301 records / 42,141 buildings; 42,153 buildings complete this scope check including the unresolved tall records. This is not all Taipei stock or an expansion of low-rise steel/SRC coverage.

**High-rise parameter admission (2026-10-23):** the [NCREE Tgbs manual](https://www.ncree.niar.org.tw/accomplishment/technicalreports/page/12223), Tables 2-5/2-7 and 5-1–5-8, supplies separate RC/steel/SRC classes for 8–18 and 19+ storeys. The extension uses the complete period, capacity, modal, damping and fragility chain and the historical >30 m coefficient branch. It imports the signed model without modifying it; all original low/mid cells reproduce. Typical class geometry is not measured building geometry. Pre-code uses the same low-code approximation. The generic structural-system coefficient K=1 is declared rather than observed, SRC elastic damping 7% is a concrete-composite approximation, and 19+ main classes use the manual's special-design ductility assignment rather than verified individual compliance. Separate stresses use K=0.67/1.33, SRC damping 5%, and era-level rather than special-design ductility. These assumptions do not establish equivalence to official software or individual safety.

**Numerical checks:** 126 class/formula/boundary checks pass; all 148 used tall class/era/site/world cells have valid finite probabilities and converged crossings. Refining the displacement grid and ceiling changes the tested probabilities by at most 0.000002693. Original low/mid scores, bands and input frequencies reproduce before the expanded population is scored. Existing era draws are preserved; added records use a separate deterministic stream. Every member's population-weighted reference median is then recomputed over the expanded stock.

**Display name:** Investigation Priority Index (IPI; 調查優先指數) denotes the final median normalized priority score below. This is a locally defined research index, not an official or empirically validated safety measure. Each calculation member uses a building-weighted median of 100 before aggregation; 100 is neither a ceiling nor necessarily the median of the final scores. The name does not change the formula, weights or candidate population.

**Score:** a declared policy index combining a structural class prior and contextual indicators, with each factor at its finest adopted level:

`E = p × (1 + αF) × (1 + δR) × (1 + λL)`

p is the research model's class-conditional Moderate+ damage estimate under the code design scenario, used only as a relative prior, not a calibrated building probability. F is the building-weighted mid-rank percentile of O, the 65+ share of its smallest statistical area, within the scored pool: F = (W(O<o) + ½·W(O=o)) / W, computed once (0.0001 at O=0, at most 0.99998; equal shares receive equal F). R is 1 for an audited text-confirmed F01 narrow-lane relationship or the unchanged fire-access stretch flag; possible-only F01 relationships receive no increment in the main documented-evidence scenario and are included in a separate scope sensitivity. L is the liquefaction value at its doorplates (1 high, 0.5 medium, 0 low). α, δ and λ are the three declared policy increments, each in {0, 0.25, 0.5}.

**Why these inputs (rationale checked 2026-10-23):** material, storeys and design era enter one engineering procedure rather than receiving separate arbitrary age/material points. They describe a class, not present walls, alterations or retrofit. The older share expresses a preference for neighbourhoods with more registered older residents; it does not measure the building's occupants, mobility or the number of people protected. A listed address supplies an access-check lead, and regional liquefaction potential supplies a ground/foundation-check lead. Neither is an observed rescue delay or foundation failure. These roles justify investigating the factors; they do not determine their numerical combination.

**Why increments rather than direct multiplication:** multiplying p by O would make the older share a proportional weight: a lower structural prior could be fully offset by a higher older share, and a building with no registered older residents nearby would score zero whatever its structural prior. Every contextual term therefore enters as an increment of the form (1 + x), so no input can zero a score, and the elderly term uses a continuous rule rather than a hard threshold. A rank percentile was adopted: it bounds the elderly increment to 0–α, responds to a building's position among old buildings rather than to the ratio of shares, and keeps equal shares at equal values instead of breaking ties by row order. Japan's 2025 review of its seismic-retrofit basic policy (MLIT) names homes of older households as a priority and observes lower retrofit rates where ageing is higher; it supports the direction, not a coefficient. No inspected source calibrates α, δ, λ or the medium-liquefaction value 0.5. A threshold rule (increment when O ≥ the pool's 75th percentile, 27.2%) would tie 216 buildings at the 1% line and select 457.

**What the increment trades:** the elderly term adds at most 50%, the same ceiling as liquefaction, while same-era class priors differ by about 2×. The older share therefore orders buildings within a class far less than a direct multiplier would; 24 first-priority buildings lie in the lowest tenth of older share and enter on structure and liquefaction. The rank keeps the order of O and discards its scale: shares from about 20.7% to 27.2% span half the percentile range, while 37.6% to 50.9% occupy only the last 1%. A higher older share therefore never lowers the increment, but it does not guarantee a better overall rank. All three 25% increments together multiply the base by 1.953, an interaction imposed by the formula rather than measured. This is an explicit research preference, not a derived expected loss or validated exchange rate.

**Zero-share boundary (resolved by the change):** the [source-traced zero-share audit](issue-6-building-resilience.md#priority-rationale-and-zero-share-audit-2026-10-23) found three permits representing ten scored buildings with O=0; original area-age counts are zero for ages 65+, with population at least 50 and unique polygon matches, so this is not missing-value imputation. Under multiplication they scored zero. Under the percentile increment they keep their structural prior and score 86.3–94.1 (band 3). Removing this mechanical suppression does not make the index an accepted inspection order.

**Why combine settings:** the grid exposes sensitivity to selected implementation, era and policy assumptions; its median supplies one reproducible displayed index. The grid's range, equal representation and median are themselves choices, not learned probabilities or a policy-neutral consensus. The 10,800 recomputations are not independent empirical validations. Report the combined input/policy frequency as such, never as engineering confidence. Normalizing the index to 100 changes its reading scale, not its evidential strength; 200 does not mean twice the damage risk or twice the benefit.

**Uncertainty and the priority score:** 4 implementations of the national model × 100 draws of the design era where the permit date straddles a boundary × α, δ, λ ∈ {0, 0.25, 0.5}: 10,800 recomputations. In each, E is divided by the 棟數-weighted median of the pool and multiplied by 100. A record's *priority score* is the median of its 10,800 values, rounded to 0.1: 100 is the typical old building. A stress test recomputes the score with 4–7-storey classes given the 1–3-storey values.

**Inputs at the finest public level (owner choice after exposure):** O and the fire-access flag are taken
at the finest adopted levels in §1, with F01 refreshed and decimal-rounding links recovered on 2026-10-22. The signed model and other inputs remain unchanged.

**Bands (changed after exposure, owner choice):** records are ordered by the score and the pool's buildings
(棟數) are counted down from the top. *Band 1* is the top 1%, *band 2* the rest of the top 10%, band 3 the remainder; the record that crosses a line counts inside. Both lines are illustrative workload fractions chosen for the demonstration, not thresholds calibrated to observed inspection capacity. Every
record of one permit shares its score, because the permit carries no attributes per building.

**Routes, after the order (feasibility, never risk):** first verify present building identity, previous assessments, organisation and applicable procedure. For walk-ups (under 6 storeys), the owner-applied 危老 assessment subsidy (M02) is a documented route; M03 is a 2016 reconnaissance precedent whose current force was not checked, not a present consent exemption or committed deployment. Six-storey-or-higher RC records with registered organisations are candidates for checking proactive initial-assessment eligibility (M01, 50 planned cases in 2026, not remaining slots); solicitation, consent and qualified assignment still follow the applicable procedure, and organisation/city-recognition status needs confirmation. Steel/SRC records first need a material-specific procedure check; floor count alone does not establish M01 eligibility. A represented-building count is not a programme case count. Being inside a designated renewal-area piece is a geographic clue for B's separate area-scope and suitability review, not inherited public-renewal priority.

## 4. Results

**Evidence — calculation 2026-10-23 (percentile elderly increment):** 25,301 historical permit records represent 42,141 scored buildings. All admitted high-rise classes are compared with low/mid classes in the same 10,800-setting procedure. These are represented historical buildings, not verified current stock. The main rescue flag uses confirmed F01 relationships and the unchanged second fire-access list. Unlisted means no evidenced increment, not easy access.

| Band | Permit records | Represented buildings | Score range | Walk-up buildings | Registered households |
| --- | ---: | ---: | --- | ---: | ---: |
| 1 | 386 | 424 | 298.6–521.3 | 0 | 17,388 |
| 2 | 2,737 | 3,792 | 152.6–298.5 | 2,069 | 88,220 |
| 3 | 22,178 | 37,925 | 2.2–152.5 | 30,580 | 424,690 |

**Evidence — candidate characteristics:** 424 represented buildings from 386 permits lie in 105 villages; three are tied at the 1% line. All are 8–18 storeys: 413 RC, 4 steel and 7 SRC. Design eras comprise 183 pre-first-code and 241 low-code buildings. Recorded households total 17,388, not current occupants. Neighbourhood older share ranges from 9.2% to 50.9%; its building-weighted mean is 28.3%. 265 buildings carry the high liquefaction value; the building-weighted mean L is 0.81. These formula-selected characteristics are not external validation.

**Evidence — why the set is all high-rise:** at the code design scenario (Taipei basin zone 1, first implementation reading, RC), the signed model's class values for P(≥moderate) are C1M 16.3% / C1H 34.1% before ROC 63 and C1M 11.8% / C1H 28.2% for ROC 64–70; modelled spectral displacement is about 4 cm for C1M and 13 cm for C1H. Pre-1982 code design strength is similar across the two classes, while the basin spectrum keeps long-period demand high, so a same-era high-rise carries about twice the mid-rise structural value. The three increments add at most 50% each and do not close that gap; the structural term alone already ranks only high-rise at the top. The 424 candidates are the higher-increment part of 1,488 pre-1982 high-rise buildings: 63% have a mean liquefaction value of at least 0.75 versus 20% of the others, and their building-weighted older share is 28.3% versus 23.9%. The best-ranked 4–5-storey walk-up sits at 3.11% of represented buildings; 2,069 walk-ups lie in the rest of the top 10%. Candidates record 41.0 households per building versus 12.6 across the scored pool.

**Evidence — high-rise parity stress (largest sensitivity):** giving every admitted 8+-storey record the C1M value of the same era, implementation reading and zone, with all other inputs and seeds unchanged (the main run is reproduced exactly first), retains only **19/424** main candidates (429 selected with ties). The new top 1% contains 410 buildings of 4–7 storeys, including 357 walk-ups, and 19 high-rise buildings; its line falls to 181.6. The worked example falls from 329.5 to 133.8, outside the top 10%. The composition of the first priority therefore rests almost entirely on the high-rise/mid-rise class ratio, which Taiwan damage data have not yet validated. The main result keeps the published class values; this stress is reported beside it, never averaged into it.

**Evidence — separate sensitivity checks:** removing only the 4–7-storey uplift retains **400/424** main candidates (422 selected). High-rise parameters themselves do not change in that stress, but the population reference median and median aggregation can alter relative ordering. Possible F01 links retain **412/424** (422 selected); their uplift-off run retains 399. Assigning every unknown municipal-liquefaction point the highest increment retains **411/424** (422 selected); the top 10% retains 4,145/4,216 (4,215 selected). Unknown points affect 1,791 records / 4,247 buildings. Requiring a positive elderly increment (α ∈ {0.25, 0.5}, 7,200 settings) retains **386/424**. These are bounded hypothetical inputs, not observations or global rank bounds.

| High-rise assumption changed alone | Original candidates retained | Total selected with ties |
| --- | ---: | ---: |
| Generic system K=0.67 | 424/424 | 550 (141 tied at the line) |
| Generic system K=1.33 | 404/424 | 422 |
| 19+ ductility follows era | 396/424 | 436 |
| SRC elastic damping 5% | 420/424 | 424 |

These separate runs do not establish a joint lower retention bound. No record bootstrap or engineering confidence is claimed. 190 buildings enter the top 1% in at least 90% of the combined model/era/policy settings; this is input frequency only.

**Evidence — descriptive groups after selection:** first partition by the listed-address flag, then split remaining records at mean liquefaction increment 0.75. These are preparation groups, never another selection funnel or causal-entry tests.

| Group | Buildings | Recorded households | ≥90% settings selected | Uplift-off retained |
| --- | ---: | ---: | ---: | ---: |
| Listed-address flag | 21 | 1,282 | 7 | 21 |
| Off-list, mean ground increment ≥0.75 | 255 | 10,047 | 119 | 233 |
| Remaining candidates | 148 | 6,059 | 64 | 146 |

**Evidence — geography and routes:** Zhongshan171, Wanhua62, Daan60, Zhongzheng54, Datong38, Songshan27, Beitou6, Xinyi3 and Shilin3. Village counts have no within-band rank. 225 RC buildings have registered organisations; 188 need organisation/recognition checks; eleven steel/SRC buildings need a material-specific procedure check. Of the 225, 152 also pass the currentness desk check below (all points on segments, matching floor annotation); they record 8,620 households in 68 villages, led by Zhongshan 63 and Daan 36, and need no further step before an invitation. Every other group needs one step; the step decides how a candidate is invited, not when, and invitations keep index order. The other 73 registered buildings first need a site identity check. Of the 188, 122 appear on the CMO assistable-organisation list (D02) and 66 on neither list; neither status establishes eligibility or consent. 3 lie in designated renewal pieces, not proven renewal projects. No first-priority candidate is a walk-up.

**Evidence — currentness desk check:** municipal layer metadata matches the previously audited layer hash. Candidate points select 254 geometry leaves. Four fail the unchanged geometry bounding-box check and remain excluded; 19 represented buildings in their envelopes conservatively require a geometry/site check. Accepted geometry yields 259/424 buildings with all recorded points on segments and a matching floor annotation; the remaining 165 carry floor, coverage, label or geometry prompts. A match is not proof of survival or identity. No feature geometry or identified permit is published.

**Evidence — term ranges and worked arithmetic:** across scored records the structural estimate p spans 0.3–38.7 per 100 buildings; its building-weighted middle 90% (P5–P95) spans 1.8–16.3, a 9.1× spread. Each increment spans ×1.00–1.50, and all three at the 50% ceiling multiply by 3.4. The worked example has p 28.2; its smallest statistical area has 32.3% aged 65+, the 94th building-weighted percentile, so at α = 0.25 the elderly factor is 1 + 0.25 × 0.94 = 1.236; it has no listed-lane relationship (1.00) and liquefaction value 1.0 (1.250 at λ = 0.25). Its raw index is 43.5; that setting's building-weighted pool median is 14.0, so the setting scores 310. Its median across settings is 329.5 (range 239–436; 72% of its settings exceed the final first-priority line). 116 permits share its district, storey, class and era.

**Aggregate derivations:** district/village map counts, distribution and the anonymous worked example are regenerated from this run. The worked example is a 12-storey RC low-code class record in Daan with at least 20 same district/floor/class/era peers; it discloses no permit or address. Record-to-building aggregation and area-context limits apply to every chart.

## 5. What the evidence supports

**Inference — investigation:** the reproducible index supplies reasons and site-check leads, not an accepted municipal inspection order. The first-priority geography changes when model coverage expands; that alone does not establish that high rises are physically less safe. Neighbourhood older share and the declared increments affect the order within a class. The structural-only calculation's highest median belongs to one represented building; the actual highest 1% includes ties totalling 1,201. Neither group is an empirical safety finding. Mid-rise uplift-off retention is 400/424 and the separate high-rise stresses above must accompany structural interpretation.

**Inference — evidence transfer:** the Yujing comparison tests numerical consistency for its low/mid classes at one shaking level; Nantou supports parts of material/era ordering. Neither validates the added high-rise order, individual condition or Taipei selection benefit. Weak storeys, alterations, material strength, retrofit and foundations require different evidence. Selected NCREE earthquake cases suggest what to examine on site, not a validated selection rule.

**Inference — other workflows:** public renewal remains the separately dated area-level case. The high-rise rerun does not repair its sparse coverage or transfer building cuts to renewal suitability. Care-institution and footprint diagnostics remain source/linkage checks; bed counts are not occupants. National liquefaction source semantics, NOT/year flags and geometry qualifications remain separate from the adopted municipal source. Historical shaking is not design demand.

## 6. Limits

- Unlocated stock, pre-archive buildings and unsupported materials remain outside scoring. Low-rise material coverage is unchanged. Permit existence and entrances are not established by the currentness check.
- A permit may represent several buildings; statistical-area residents are not individual building occupants. The ten zero-share buildings now keep their structural prior; their low elderly increment is not evidence about actual occupants.
- Source-linked fire flags do not measure vehicle access or delay. Possible scope is a sensitivity scenario; the second list retains partial-placement limits.
- High-rise K, SRC damping, special-design assignment and typical geometry are explicit class approximations. The separate stresses quantify selected assumptions, not all uncertainty or joint robustness.
- Moderate-or-worse class damage under a design scenario is not collapse probability, present structural diagnosis or a validated priority. Input-frequency checks do not resample records.
- Top 1%/10% are illustrative workload fractions; whole ties and multi-building permits remain together. No within-band ranks are published.

## 7. Next actions and open decisions

Before operational use, justify the objective and the size of the three increments, including whether the elderly increment should exceed the liquefaction one. Define a professional outcome and compare this rule with an age/storey/material reference at the same candidate scope and investigation volume; compare actual municipal selection separately if its records become available. Retaining the current candidates or matching the city is not success. Revise or reject the combination if it adds no decision-relevant information.

Currentness/site checks, prior assessment, organisation and applicable procedure can proceed as evidence tasks without accepting this index as an operational order. Material-ambiguous high-rise records and current structural condition require additional evidence. National liquefaction replacement and citywide completeness remain separate questions.

## Change log

- 2026-10-23: older share enters as a bounded rank-percentile increment (1 + αF), α ∈ {0, 0.25, 0.5}; 10,800 settings. First priority 424 buildings; no building scores zero.

- 2026-10-23: added the first-priority reading (why the set is all high-rise) and the high-rise parity stress (23/422 retained); main formula and result unchanged.
- 2026-10-23: extended supported high-rise coverage, rebuilt the full population calculation and separate stresses, and refreshed candidate descriptions/currentness checks. The formula, narrative architecture and immutable signed model are preserved. Numerical custody and superseded results remain in internal provenance and Git.
