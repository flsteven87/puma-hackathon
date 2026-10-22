# Issue 6 companion — the five-factor rating at building level

| Field | Value |
| --- | --- |
| Parent topic | [Issue 6 — Old-building seismic resilience](issue-6-building-resilience.md) (official prompt, practice and evidence) |
| Design decisions | 2026-10-21: analyse by building without identifying individual buildings; keep the building analysis in its own document; answer the official prompt; one score per building and a top-share cut, first priority the top 1% |
| Evidence cutoff | Computation/F01 audit 2026-10-22; other evidence 2026-10-21 (D03 historical permits, MOI smallest-statistical-area age groups, both Fire Department lists, city liquefaction polygons, designated renewal areas, D01/D02 organisation lists, NCREE Meinong/Hualien case export) |
| Status | Development analysis after exposure: every field, list and the 里 bands had been seen before the contract was written. No damage label is fitted |
| Publication | Aggregates only. The per-building table carries permit numbers and stays in private research custody |
| Lay page | [哪些老房子，該先做耐震健檢？](../demo/issue-6-building-rating.html), built from this document's numbers |

## 1. Decision

**Evidence — the prompt (parent §1):** the event organiser asks for a 危老耐震風險加權評級模型 that integrates building
age, structure, older population, liquefaction potential and narrow-lane rescue difficulty, to order old-
building health checks (老屋健檢) and public renewal (公辦都更). It sets no case limit and no programme
eligibility. The event is organised by 沈伯洋競選辦公室; this is independent research for a potential municipal decision, not a city commission.

**Decision here:** which historical-permit candidates merit earlier professional investigation, and which follow-up route could reach them after current identity, previous assessment and applicable programme conditions are checked. This document is the primary inspection-priority report. Village totals summarize the candidates geographically; they do not supply a separate priority score.

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
| Signed Tgbs class model (parent §4) through the parent's cleaned record table | Research approximation of class damage probability under the code design scenario, by class, storeys, design era and site zone | Up to 7 storeys; not collapse; no Taiwan validation of the order |
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
the record's fields because the permit carries none per building. Records of up to 7 storeys are scored;
taller records fall outside this implementation's class table (the national model has a high-rise RC class,
C1H, which the signed model does not carry) and form a separate *tall lane*, described by the
same factors and never scored.

**Score:** the parent's loss-chain quantity, with each factor at its finest level:

`E = p × O × (1 + δR) × (1 + λL)`

p is the building's chance of moderate or worse damage under the code design scenario; O the 65+ share of
its smallest statistical area; R is 1 for an audited text-confirmed F01 narrow-lane relationship or the unchanged fire-access stretch flag; possible-only F01 relationships receive no increment in the main documented-evidence scenario and are included in a separate scope sensitivity; L is the
liquefaction value at its doorplates (1 high, 0.5 medium, 0 low). δ and λ are the two declared policy
multipliers.

**Uncertainty and the priority score:** 4 implementations of the national model × 100 draws of the design era
where the permit date straddles a boundary × δ, λ ∈ {0, 0.25, 0.5}: 3,600 recomputations. In each, E is divided
by the 棟數-weighted median of the pool and multiplied by 100. A record's *priority score* is the median of
its 3,600 values, rounded to 0.1: 100 is the typical old building. A stress test recomputes the score with
4–7-storey classes given the 1–3-storey values.

**Inputs at the finest public level (owner choice after exposure):** O and the fire-access flag are taken
at the finest adopted levels in §1, with F01 refreshed and decimal-rounding links recovered on 2026-10-22. The signed model and other inputs remain unchanged.

**Bands (changed after exposure, owner choice):** records are ordered by the score and the pool's buildings
(棟數) are counted down from the top. *Band 1* is the top 1%, *band 2* the rest of the top 10%, band 3 the remainder; the record that crosses a line counts inside. Both lines are policy
choices sized to inspection capacity; the lay page lets the reader move the line from 0.5% to 10%. Every
record of one permit shares its score, because the permit carries no attributes per building.

**Routes, after the order (feasibility, never risk):** first verify present building identity, previous assessments, organisation and applicable procedure. For walk-ups (under 6 storeys), the owner-applied 危老 assessment subsidy (M02) is a documented route; M03 is a 2016 reconnaissance precedent whose current force was not checked, not a present consent exemption or committed deployment. Six-storey-or-higher records with registered organisations are candidates for checking proactive initial-assessment eligibility (M01, 50 planned cases in 2026, not remaining slots); solicitation, consent and qualified assignment still follow the applicable procedure, and organisation/city-recognition status needs confirmation. A represented-building count is not a programme case count. Being inside a designated renewal-area piece is a geographic clue for B's separate area-scope and suitability review, not inherited public-renewal priority.

## 4. Results

**Evidence — calculation 2026-10-22:** the same 25,225 historical permit records represent 42,054 buildings; 38,345 are scored and 3,709 taller buildings remain unscored. These are included historical records, not a complete present-day city inventory. The parent §5 coverage audit retains unlocated old permits separately; missingness is concentrated in older masonry and cannot be read as low geographic need. Every old score, band and member frequency was reproduced before changing the input. The current scenario uses confirmed F01 links plus the unchanged second fire-access list; ambiguous F01 links receive no additional rescue multiplier in this scenario, not a finding of good access.

| Band | Permit records | Represented buildings | Score range | Walk-up buildings | Registered households |
| --- | ---: | ---: | --- | ---: | ---: |
| 1 | 221 | 385 | 229.1–362.6 | 236 | 2,582 |
| 2 | 2,288 | 3,467 | 161.2–229.0 | 3,096 | 30,437 |
| 3 | 19,896 | 34,493 | 0.0–161.1 | 29,317 | 332,947 |

**Evidence — scope and structure sensitivity:** the main first-priority set contains 385 represented buildings in 62 villages. Removing the mid-rise uplift retains **332/385**. Including possible F01 scope links instead gives 385 first-priority buildings, sharing **363/385** with the main set; removing uplift in that possible-scope scenario retains **347/385**. The broad scope is not a physical upper bound. Tracing every disagreement record found that all 22 possible-only entrants (14 permits) have doorplates on an unlisted branch of a listed lane or outside the listed stretch, while the 22 buildings they displace keep unchanged inputs; the main set therefore stands ([parent §5](issue-6-building-resilience.md#first-priority-disagreement-review-2026-10-22)). No individual rank is published within a band.

**Evidence — missing-liquefaction stress (2026-10-22):** the parent's [paired test](issue-6-building-resilience.md#missing-liquefaction-input-stress-test-2026-10-22) holds all other inputs/draws/weights fixed and sets only uncovered points to the highest increment. It retains384 of the current385 first-priority棟;1 leaves and4 enter, giving388 after full ties. Top10% retains3,793/3,852;59 leave and47 enter (3,840 selected). Current structural uplift-off remains332/385; removing uplift in the joint missing-input stress retains328/388. This is one hypothetical joint assignment, not a global rank bound, geological observation or bootstrap robustness. Current published scores/list remain unchanged.

**Evidence — inputs:** 1,193 scored buildings have confirmed F01 narrow-lane links; 580 have possible-only F01 relationships. Union with the unchanged fire-access list gives 2,762 rescue-flagged scored buildings. These are historical address associations, not current access observations. Original source dates remain distinct from the calculation date.

**Evidence — input variation:** 94 first-priority buildings occur in the top 1% in at least 90% of the 3,600 model/era/weight combinations. The minimum top-10% member frequency in the main first-priority set is 86.7%. This is conditional input sensitivity; records were not bootstrapped and no sampling-stable set is claimed.

**Evidence — routes:** 236 first-priority buildings are walk-ups. Of the 149 with six or seven storeys, 68 have a registered organisation and 81 require organisation/recognition checks; 68 of the latter appear on the no-organisation assistance list and 13 appear on neither organisation list. 13 first-priority buildings lie in designated renewal-area pieces; that alone does not establish public-renewal suitability.

**Evidence — three kinds of first priority:** every first-priority building is a pre-1982 4–7-storey design in a statistical area at least 25% aged 65+, and the selected set is partitioned descriptively by its listed-address flag, then its doorplate-mean increment; these groups do not identify a causal entry factor. 105 buildings (664 households) are on a listed rescue lane; 97 are walk-ups, mainly 中正 and 大同, and only 5 stay in the top 1% in at least 90% of the 3,600 combinations, because their position depends on the rescue weight. 149 (1,060) are off the lists with a doorplate-mean liquefaction increment of at least 0.75 (not an observed site class), mainly 中山 and 大安; 32 meet that input-frequency threshold. 131 (858) are off the lists with a doorplate-mean increment from 0.25 to below 0.75 (not observed MED) and the highest 65+ share (39%), 94 of them in 大安 and 76 with six or seven storeys; 57 meet that input-frequency threshold. Uplift-off retention is 84 / 129 / 119. The kinds describe the result for site preparation and routing; they are not a second selection step.

**Evidence — geographic summary:** 大安區 163, 中山區 88, 萬華區 51, 中正區 36, 大同區 30, 松山區 10, 士林區 7. Village totals describe where the candidates are; they are not another ranking. A permit can represent several buildings whose attributes and scores are shared. The map, distribution, 0.5–10% capacity slider and anonymized worked example are rebuilt from this run.

**Evidence — tall lane:** 2,820 records / 3,709 buildings above seven storeys remain outside the implemented model classes. Their updated rescue relationships are retained without scoring; age, organisation and renewal routing are unchanged.

## 5. What the evidence supports

**Evidence / inference — municipal comparison, 2026-10-22:** the parent's [municipal research comparison](issue-6-building-resilience.md#municipal-research-comparison-and-selection-blind-spots-2026-10-22) distinguishes city disaster planning, renewal pilots and actual assessment procedures. The current structural term leaves 5,929 represented C1M/P buildings tied at the highest structural-only median at published precision; the composite's finer distinctions therefore depend partly on older-neighbourhood share and policy multipliers. This is an older-resident-emphasis investigation scenario, not a maximisation of people protected or an independently validated safety order. Code-level basin demand does not reproduce the city's spatial fault scenario; unlocated and taller buildings can be omitted before scoring. Current scores and the 385-building set remain unchanged.

**Inference — investigation:** use the main band as a documented-evidence scenario for professional investigation, with the possible-scope result beside it. The first-priority scope disagreement is resolved in favour of the main set; buildings reached only through a listed narrow lane remain a route-through question for site review, not a scored flag. The route depends on building/storey and organisation evidence; high score does not establish programme eligibility, safety, consent or funding.

**Inference — structural limits:** Yujing supports numerical consistency with the national model at one shaking level, and Nantou supports parts of material/era ordering. Neither validates the mid-rise uplift or Taipei inspection gain. Hence uplift-off remains a separate stress test and is not averaged into the main score. NCREE's selected earthquake cases suggest ground-floor wall interruption is worth checking, not a validated selection rule.

**Inference — public renewal:** B remains its separately dated area-level research case; the building refresh does not transfer inspection cuts to renewal suitability or repair B's sparse coverage.

**Evidence / inference — independent method deepening, 2026-10-22:** the parent's [five-track source and linkage audit](issue-6-building-resilience.md#independent-method-deepening--source-and-linkage-results-2026-10-22) completed a fixed-area F05 permit/footprint diagnostic and a conservative 110-institution care diagnostic. Their one/many/unmatched groups prevent equating source records with current buildings; 13 single-permit care rows concern the unscored tall lane. A new nursing register reconciles to 1,101 opened beds, not occupants. Tgbs supplies tall classes but requires upstream taxonomy and full parameter/code-domain checks; source availability does not validate individual condition. Historical event shaking is not design demand, and planned road width is not measured access. The subsequent full liquefaction audit verifies city semantics and source coverage while retaining national unknown/year/geometry flags. No score, weights, signed model or candidate universe changed; the 385 result and 332/385 uplift-off result remain the reference calculation.

**Existing-input qualification:** the municipal export-to-renderer bridge is now verified for all136 features (parent §5 liquefaction audit):1=HIGH,2=MED,3=LOW. No category swap or score change follows. National TYPE/year categories remain separate; unobserved ground/foundation conditions and current L's no-evidence/averaging conventions remain limitations.

**Coverage implication:** all25,225 existing L values reproduce. In the scored lane,1,456 permits/3,051 represented棟 lie wholly outside the city map, plus201/847 partially outside. Current zero contribution means no evidenced increment, not observed LOW; an average across addresses need not describe one MED site. These groups must remain visible when explaining the unchanged score. The paired joint-input test is complete; it does not certify all heterogeneous missing assignments. National raw-versus-repaired point membership is unchanged in this audit, but its NOT/null-year and invalid-feature flags remain explicit; no automatic source swap follows.

## 6. Limits

- Historical permit identity, existence and entrances remain unverified; unlocated buildings are outside the pool and old masonry is underrepresented.
- A permit can represent multiple buildings; area population is not the occupants of an individual building.
- F01's 580 possible-only scored buildings do not get a rescue increment in the main scenario; the alternative quantifies one broad scope assumption, not all possible mapping errors. Doorplate positions are not surveyed entrances, and the disagreement review checked text and geometry, not vehicle access. Unlisted never means easy access.
- The second fire-access list is unchanged; its earlier partial placements remain a limitation.
- Damage means moderate or worse under a design-earthquake class scenario, not collapse, an individual safety diagnosis or a validated municipal priority.
- Input-frequency sensitivity is not record-bootstrap robustness. The 1%/10% cuts are policy choices; ties and the crossing permit remain together.

## 7. Next actions and open decisions

- **Owner direction — independent optimisation (2026-10-22):** preserve the research question and independent criteria. The parent's method-admission plan examines stock identity, spatial demand, exposure/support, structural coverage and rescue/site mechanisms. Incorporate an input only after its source and decision-specific measurement checks pass; neither matching the city nor retaining this 385-building set is success. Current scores remain unchanged while these checks are pending.
- **Done:** the main/possible first-priority disagreement (29 permits / 44 buildings) was traced to source text, the publisher's sub-alley listing convention and doorplate geometry; the main set stands.
- **Done 2026-10-22:** the lay page distinguishes regional potential, unknown coverage and multi-doorplate means; presents the bounded384/385 joint-stress finding beside unchanged385/332 results; uses descriptive groups and conditional assessment routes. Scores, map geometry and interactive capacity data are unchanged.
- **Next:** national liquefaction numerical replacement remains a separate research question; numerical results are unchanged.
- **Separate follow-ups:** completed F05/care diagnostics have not adopted new inputs. F04 finest geometry is recovered and joined to permits in one fixed rectangle, where its brick symbol does not locate masonry permits. A [desk pre-check](issue-6-building-resilience.md#first-priority-currentness-desk-pre-check-2026-10-22) of the first priority finds 311/385 represented buildings on a municipal segment whose floor annotation matches the permit, and 74 with a site-check prompt; the lay page states this aggregate split in its first-use step; scores are unchanged; current-site/LTC identity, upstream tall/mixed taxonomy and soil-profile CRS remain explicit research questions.


## Change log

- 2026-10-21: created for the official prompt's five factors and both actions: one median priority score per
  building record, first priority the top 1% of buildings and second wave the rest of the top 10%; the 65+
  share and the fire-access flag at their finest public levels.
- 2026-10-22: fire-lane lists linked by confirmed doorplate match, with possible-scope and uplift-off checks
  (385 first priority, 332 retained uplift-off); missing-liquefaction stress (384/385 retained); desk
  pre-check against the 2025 municipal layer (311 consistent, 74 site-check prompts). Scores unchanged.
