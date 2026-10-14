# Issue 6 — Old-building seismic resilience

| Field | Value |
| --- | --- |
| Official prompt | [Issue 6](https://puma.taipei/hackathon#issue-6) 「危老耐震如何查，風險評級怎麼找」 |
| Template | [Topic document standard](../research.md#topic-document-standard) v1 |
| Pain re-read | 2026-10-14 11:51 Taipei, live official page and public citizen-voice feed |
| Evidence cutoff | 2026-10-14 |
| Workflows | Inspection allocation A; public-renewal review B; T06-A–C; T06-D route finder. Status: [canonical readiness record](../research.md#problem-fit-and-separate-readiness-of-the-expanded-candidates) |
| Reading mirror | [老屋韌性研究報告](issue-6-building-resilience.html) |
| Open owner decisions | Information requests to agencies need confirmation; public reading continues by default |

Research-only findings, retrieved 2026-10-13; No application, contact, registration, account, payment, API inference, or canonical-file edit. **Evidence** below means inspected original material; **Inference** is this analysis; **Hypothesis** identifies untested practitioner value. Topic selection remains an **Owner decision**.

Scope: private residential communities in Taipei; mandatory nonresidential inspections and public-school retrofit programs are separate workflows and are not assessed here.

Method, event facts and cross-topic comparison live in the [research master](../research.md).

## 1. Official prompt and citizen pain

**Evidence — official prompt, verbatim:** issue 6 is titled 「危老耐震如何查，風險評級怎麼找」 with
tags 居住安全, 加權模型, 都更. Its pain sentence is the 「人老＋屋老」 double-aging dilemma. The
50-year-plus share of the housing stock is projected at over 20% in 2025, over 50% in 2035 and over
65% in 2045, so most homes predate the post-921 seismic code. The weighted rating model for
health-check and public-renewal priority is posed as the question 「我們要如何…？」, not as the
pain. Projections remain organizer assertions.

**Evidence — citizen voices observed, 2026-10-14 public feed sample (paraphrased):** of 76 visible
recent voices, two concern old buildings. One, under 市政, comes from a Shilin owner of a
four-storey building about 60 years old. The upper floors report unstable foundations, but the
ground and first floors are rented out by owners who do not live there, and the unanimous-consent
requirement of the 危老 route blocks reconstruction. The other, under 城市修繕 from Neihu, asks the
city to coordinate old-housing renewal as a project manager that tracks progress. A third,
two-word voice simply asks for 老宅都更. **Limitations:** a four-per-topic rolling sample; the
statutory consent rule and the households' situations are unverified here.

**Inference:** the citizen-side pain observed so far is consent and coordination after a building
is known to be old or unsafe. It is not "which building to inspect first". This matches the
downstream bottleneck evidence below (P05, X24) and the willingness thresholds (P20–P23). A
ranking of whom to inspect first addresses the policy team's suggested direction, not these
voices. Keep hypothesis A as the answer to that direction and to the EY rubric demand (P30). Open
a pain-first track for owners blocked by non-resident co-owners and missing coordination.

**Next check:** a larger set of old-building voices should come from the organizer's de-identified
event copy, now that the owner has registered. Do not collect the public feed systematically:
the operator's notice requires researchers to apply for authorization before obtaining its data,
and applying is external contact. Quotations need the operator's written consent. The pain tree
below works backward from the voices already observed.

## 2. Pain tree

**Pain tree (inference; owners of each decision are hypotheses until observed):**

| Pain (source) | Decision and owner | Fields the decision needs | Where they could come from |
| --- | --- | --- | --- |
| Co-owner dissent blocks reconstruction (voice, Shilin) | Owner or committee: which route, and what evidence would change its threshold | Households and ownership split, site area, permit year, assessment status, block and zoning context | Owner's documents; land registry (per record); promoter; CMO 危老問答集 B 法令適用篇 as baseline |
| No one coordinates or follows up (voice, Neihu) | City: where public coordination or promoter support should go | Filings by stage, age of each filing, stalled cases, household count | Promoter register snapshots over time; CMO statistics; organizer event voices |
| Elderly residents in walk-ups (official sentence) | Committee: lift or reconstruction; city: lift-subsidy outreach | Storeys, lift presence, units, residents' age, consent status | Pre-2003 no-management list; 3D model storeys; village age data (context only) |
| Owners cannot tell whether the building is safe (issue title) | Owner: apply for an initial assessment | Eligibility, subsidy, institutions | Existing CMO pack and promoters (strong baseline) |
| City needs a priority order (policy direction; EY rubric demand) | City: inspection and outreach sequence | See hypothesis A | See hypothesis A |

### Evidence behind the pain tree

**Method, 2026-10-14:** read statutes on the national law database (curl, HTMLParser):
- 都市危險及老舊建築物加速重建條例 (D0070249, amended 2023-12-06);
- 都市更新條例 (D0070008, amended 2024-11-13);
- 公寓大廈管理條例 (D0070118, amended 2022-05-11).

Also read:
- the Taipei promoter programme (FL088608, revised 2026-04-08) and its fee rule (FL089822, revised
  2026-02-03) on laws.gov.taipei;
- CMO's 危老 page and its attachments, parsed with `pdftotext -layout`: the promoter case register
  dated 115.10.1 (84 pages), the list of pre-2003 buildings without a management organization
  dated 115.07.17 (80 pages) and the elevator FAQ (169 pages, 2023-05).

The two lists contain addresses and promoter names. Only aggregates computed with
`uv run python -I` are recorded here; raw files stay outside Git. One web search lead remains
unverified at its original source, the elevator subsidy count.

**Evidence — consent thresholds differ by route:**

| Route | Consent needed | Source |
| --- | --- | --- |
| 危老 reconstruction | All land and legal-building owners in the plan area. Applications close 2027-05-31 | D0070249 §5 |
| 危老 eligibility | One of three: (1) ordered demolition or reinforcement; (2) assessment below the minimum grade; (3) age ≥30 with seismic capacity below standard, where improvement is not cost-effective or no lift exists | D0070249 §3 |
| Urban renewal in a promptly designated area | More than 1/2 of private owners and of their land and floor area | D0070008 §37(1)(2)(一) |
| What triggers prompt designation | Disaster damage, avoiding major disaster, or buildings meeting 危老 §3(1)(1)–(2) | D0070008 §7 |
| Other renewal areas, owner-led | More than 3/4 | D0070008 §37 |
| Self-delineated units | More than 4/5 | D0070008 §37 |
| Condominium reconstruction outside renewal | Unanimous, except severe decay or disaster danger. Then an owners'-meeting resolution, and a court can order dissenters to sell | D0070118 §13–14 |
| Adding a lift (permit) | Majority of co-owners and of shares; shares alone if above 2/3 | CMO elevator FAQ A-21 |
| Adding a lift (Taipei subsidy) | All owners in principle, or an owners'-meeting resolution plus undertakings | CMO elevator FAQ A-21 |

**Inference — the check is a legal lever, not only a safety check.** The issue title asks how to
check (如何查). For an owner blocked by a dissenting co-owner, an assessment below the minimum
grade can move the building from the unanimous 危老 route toward prompt designation, which needs
more than half. **Evidence — CMO 危老問答集 B 法令適用篇 Q30 (January 2026 edition, p. B65):** the city
confirms this switch. A building assessed below the minimum grade (initial assessment below 乙級)
that cannot reach 100% consent may ask the urban renewal office to propose prompt designation to
the city government. The wording 視實際情況 makes it discretionary. The same answer adds a second
link: in a self-delineated unit where every qualifying building is assessed below the minimum
grade, the environmental indicator review is waived. The FAQ does not state unit-size limits for
a single walk-up, and no count of such designations was found. Majority is also not automatic:
in a four-unit building with two dissenting owners, 2/4 is not more than half.

**Evidence — a coordinator already exists.** Taipei trains and certifies 危老重建推動師 (promoters).
They provide free legal explanation, help residents integrate their willingness, guide the
assessment and file the reconstruction plan. They also help form management organizations and
add lifts. The city pays per-stage fees, and one promoter registers per address (FL088608 壹;
FL089822 points 4–5). CMO's register of promoter filings (115.10.1) has 3,698 rows with no gaps
in the sequence:
- Stage: 3,182 initial assessment, 22 detailed assessment, 492 reconstruction plan, 2 unparsed.
- Size: median 4 households; 86% have ≤10.
- Age: of 2,524 parseable use-permit years, 2,010 are ROC 69 (1980) or earlier.
- Matching: a rough first-address match finds about 3,000 addresses with initial-assessment
  filings only, and about 187 that also carry a plan filing.

**Limitations:** this is a filing register, not completions. Its cumulative or active scope is
not stated. Address matching is approximate, and filings carry no dates.

**Inference:** the Neihu voice asks the city to act as project manager. That role is already
outsourced to per-stage-paid promoters, mostly on small pre-1981 walk-ups. The observable gap is
conversion: most addresses never move from an assessment filing to a plan filing. Whether
promoter incentives, co-owner dissent or economics cause this is unknown. A further unknown is
whether promoter affiliation affects trust.

**Evidence — 人老 branch.** The official pain sentence is the double-aging of residents and buildings.
Lift retrofits need only majority consent for the permit. The lack of a lift is also one of the
危老 §3(1)(3) eligibility conditions. A press lead (鏡週刊, 2026-04-02, citing the renewal office)
reports 167 lift-subsidy applications and 64 completions from 2015 to 2026-02. This is not yet
verified against the original.

**Evidence — building-level public lists exist.** This correction qualifies the deep-investigation
statement that building-level old-stock data exist only in restricted sources. CMO publishes two
lists:
- the promoter register above;
- a list of use permits issued before 2003 for buildings with six or more storeys, two or more
  units and no management organization. It has 5,489 entries with permit number, district,
  address, storeys above and below ground, and units (115.07.17).

Both are scoped lists, not the old-building universe. Neither has a reuse licence statement, so
treat both as readable, not redistributable.

## 3. Current practice and baseline

### Selection practice, bottleneck and professional anchors

**Owner decision — 2026-10-14:** deepen the old-building resilience research and gather more complete professional and practical detail. Research-only; no request, contact, account, submission or implementation.

**Method:** four bounded tracks ran in parallel on 2026-10-14: current Taipei selection rules and baseline (P sources), professional assessment and retrofit practice (E), old-building stock data (I), and prioritization precedents elsewhere (X). Each track read original government, professional-body, research or operator documents. HTML pages were read with the web tool or curl; PDFs were read with `pdftotext -layout`; open datasets were downloaded and parsed with `uv run python -I`. The topic owner then re-read the decisive values in the downloaded originals: the MOI proactive-assessment criteria (P02 point 5), the 2019–2021 national target/achievement table (P05), the 2026 national demand for an explicit ranking rubric (P30), Taipei 危老 counts (P29), the initial-assessment grade table (E01/E02 附表五), the single-building R variation (E10), the Taichung screen-positive share (E21), the tax-office district totals (I, 115年度 CSV sums), the MOI unit table for Da'an, and the national initial-assessment and weak-story counts (X24). Search snippets and news remain labelled leads. Raw downloads, owner names and addresses stay outside Git. Table rows below come from the track records; a row is evidence only for the sections stated in its ledger entry.

**Evidence — selection practice:** Taipei publishes no weighted ranking for either decision. Proactive initial assessment is a national eligibility filter (quick-screen F>60 or age ≥30, plus a management organization and ≥6 storeys, or the city's discretion), followed by owner consent (P02). The only ordering language lets the executing agency order applications "因地制宜" (P02 point 14). The routine assessment subsidy is applicant-initiated and reconstruction-oriented (P15–P17). Public-led renewal origination depends on land thresholds, public-land assets, a suitability report and owner willingness (P19, P24). Hazard-linked renewal channels (575, disaster-prevention renewal) start only after owners prove hazard, using ID<0.35, sea-sand listing or tags, and then clear 50/75/90% willingness thresholds (P20–P23). Taipei's closest published hazard ordering is the 2016–2017 老屋健檢 plan. Its first-phase priority classes were suspected soft storey or frontage on the 27 disaster-relief roads, prior 921/331 tags, fault or liquefaction zones, and public housing (P01). A 2014 Taipei study selected pilot villages from simulated Shanchiao-fault damage, and judged parcel-level hazard data too coarse (P25).

**Evidence — explicit official demand:** the Executive Yuan's 2026-03-16 approval of 老宅延壽機能復新計畫 (114–116) requires the MOI to "建立受理申請審查之明確評比基準及核定優先順序", and asks professional teams to select priority areas, inventory potential cases and overlay maps (P30). It targets 4–6-storey apartments aged ≥30 years, the stock that the proactive ≥6-storey rule omits. This is national demand for a transparent ranking rubric, not a Taipei commitment or allocation.

**Evidence — the bottleneck is downstream:** nationally, 2019 to 2021-09 delivered 4,147 of 19,555 planned subsidized initial assessments, 2 of 500 detailed assessments and 21 of 725 weak-storey retrofits (P05). Cumulative national initial assessments reached 17,277 by December 2024, Taipei 5,754 of them, while weak-storey subsidy applications totalled 194 (X24). In 2016 MOI linked low uptake to owners' fear that results would be disclosed and promised confidentiality (X02, X04). A detailed assessment costs about NT$0.15–1.8 million per building under the Taipei-published 2026 fee schedules, depending on floor area and fee family (E14). Weak-storey retrofit subsidy is normally ≤45%, so owners pay the rest (E08). Tokyo's route-side program reached 98.6% diagnosis but left about 2,000 buildings unretrofitted, citing cost and co-owner consensus (X13). **Inference:** a better ranking alone is unlikely to change outcomes. Its defensible value is sequencing outreach and assessment and keeping unknown cases visible.

**Evidence — professional decision anchors:** one initial-assessment danger score R drives several decisions at different cut points: 危老 grades at 30/45 (E01–E03), weak-storey subsidy at R>30 and an increased rate at R>45 (E08), PSERCB/public-building action at 60 (E12, E17), and the renewal danger criterion ID<0.35 (E07). R combines 40 qualitative points with 60 points from a first-floor-only capacity calculation, without coring. PSERCB guidance excludes hidden defects, high chloride and additions (E12). In one official teaching case, two engineering assumptions moved a building's R from 10.8 to 42.3 (E10). **Inference:** a model should target a named decision threshold. Near-threshold buildings are uncertain even after a formal initial assessment.

**Evidence — observable predictors and their limits:** official 2016 Meinong and 2024 Hualien investigations repeatedly name soft or open commercial ground storeys, arcade (騎樓) street-house columns, corner or irregular plans, single-section column splices and inadequate hooks (E25, E26). The official pre-assessment quick screen reviews drawings for tall or open ground floors, arcades or mezzanines, wall-poor ground floors, design-load and system-factor issues, incomplete frames and single spans (E10). Taichung referred 40.9% of 5,443 screened licences for initial assessment (E21). Splices, hook detailing and illegal wall removal cannot be observed in public data. Policy cutoffs use different date bases (permit applied, obtained, designed, use permit issued), and the assessment's detailing item treats post-May-1997 design as modern (E10, E17, E33). A collapsed 2016 building completed in 2000 shows that completion year is a weak proxy (E26).

**Evidence — site hazard and known conditions:** site amplification already enters R through the Taipei basin microzone or ground class (E12). Liquefaction maps are planning-grade, and the agency stated that past collapses were caused by poor structural systems, not liquefaction (E29–E31). Sea-sand status is a separately listed regime with its own sampling and demolition criteria (E22, E24). **Inference:** treat liquefaction as a geotechnical-check flag and sea-sand listing as a known-condition flag or exclusion, not as additive seismic weights.

**Evidence — stock data:** the finest open old-building data is district level. The Taipei Revenue Service's 臺北市房屋概況 115年度 reports 220,254 buildings, 201,642 (91.5%) aged ≥30 years; the district rows reconcile to DBAS's citywide building series (I). MOI's real-estate platform publishes residential units by district and quarter, as separate age, structure and floor tables, with no cross-tabulation: Taipei had 921,951 units at 115Q2, 74.5% older than 30 years (I). Building counts and unit counts rank districts differently. Building-level age, structure and floors exist only in restricted or per-record sources (qualified 2026-10-14: CMO publishes two scoped building-level lists; see T06 pain tree): house-tax records (稅捐稽徵法 §33 ¶2 permits supply to agencies and researchers for statistics or research without names), land-registry building records (per-record to anyone; bulk under local data-supply fee rules), and the NLSC 3D model. The 3D model has floors and height but no age; Taipei files are referred to the city's Department of Information Technology (I). NCDR built a 500 m grid from the tax register, available to agencies and academia on written request (I).

**Evidence — precedents:** no reviewed jurisdiction ranks individual private buildings by a continuous weighted score. Los Angeles, San Francisco, Japan and New Zealand use an observable inclusion rule, coarse deadline tiers and a binding engineer evaluation (X05–X19). Missing information triggers evaluation rather than implying safety: New Zealand deems an unassessed building earthquake-prone after 12 months; Los Angeles non-ductile concrete applies "whether identified or not"; Japan targets 耐震不明 buildings (X07, X13, X19). In FEMA's only benchmark against engineering evaluation, Level 1 rapid screening missed 1 of 31 unacceptable buildings but referred 11 of 18 acceptable ones (X20, computed). Tokyo measures route priority as road-section reachability and named 50 priority sections where few retrofits restore the most network function (X13). Japan and San Francisco express elderly or vulnerable occupancy as facility-use classes; social-vulnerability index rankings are sensitive to construction choices (X09, X12, X28, X29).

### Earlier findings, fit and disposition (2026-10-13)

**Supported:** professional assessment, renewal/retrofit feasibility and outreach coordination are different decisions. The official assessment pathway already handles consent, qualified assessment, checking and subsidy applications [S02–S04]. NCREE documents an actual community project where full reinforcement cost threatened affordability, followed by a different professional proposal and community explanation [S08]. This is concrete operator-reported difficulty, not evidence that a Taipei dashboard solves it.

**Refuted for the proposed inputs:** an individual safety score or defensible assessment/renewal priority derived from age totals, older-population counts, liquefaction zones and rescue-road lists. The freshly parsed building source is citywide annual counts, rather than building records [S12]; the liquefaction publisher explicitly rejects site diagnosis from its medium-resolution map [S11]. Building-specific assessment results are not proactively public and disclosure requires applicant consent [S04, Q19]. More mapping cannot recover these missing observations.

**Unresolved:** whether officials or community facilitators repeatedly lose time identifying the appropriate next step, and whether any new tool improves on existing professional services. Public procedure proves process, not user frustration. Available research describes intention and barriers, not a causal effect of an information intervention [S09–S10]. Authority, consent, household liquidity, professional availability and construction disruption are credible rival bottlenecks.

**Fit:** organizer issue 6 explicitly requests a weighted risk model and acknowledges unavailable individual age/structure data [S01]. The three earlier narrowed workflows contribute to its assessment/renewal objective but do not satisfy its scientific-ranking ambition; label them narrowed issue-6 proposals or explicit free-topic alternatives. C02 population context is not structural vulnerability; C04/C05 preparedness and flood exposure remain distinct. No cross-topic rank is justified. Evidence depth is uneven: current assessment procedure is strong; a historical non-Taipei outreach case is concrete; Taipei practitioner demand and municipal outreach performance remain unvalidated.

### Domain primer — work backward from lost functions

**Owner decision — 2026-10-13:** prioritize the six defined official issues; pause expanded free-topic comparison. Explore issue 6, old-building resilience, and explain the professional domain through the existing local HTML mirror. This is a research focus, not a contest entry, implementation request or authorization to publish the HTML.

**Evidence — retrieved 2026-10-13:** the official issue-6 HTML was downloaded with curl and parsed using `HTMLParser`. It explicitly links liquefaction GeoJSON, village age population, city building-count/age statistics, the fire-access register and the liquefaction query portal. It acknowledges unavailable building-level age/structure and permits simulated inputs. Assessment procedures, retrofit rules, professional services and academic/operator accounts are researcher-added sources, not organizer-listed inputs. Organizer projections and model usefulness remain attributed assertions.

**Evidence — full-file refresh, 2026-10-13:** unauthenticated curl downloads, normal TLS verification, standard-library CSV/JSON parsing through `uv run` reproduced the following. These are file censuses, not independent physical surveys. No raw personal records were retained.

| Source | File completeness and fields | Remaining quality limits |
| --- | --- | --- |
| Building counts S12 | 50 nonempty annual records, 13 columns; one additional empty CSV row. Period, total buildings, nine floor bands, age under30/30-and-over. | City aggregates, not building inventory. Later allocation audit identifies31 early zero-age years and age/floor sum discrepancies; zero semantics and causes remain unresolved. |
| Village population a6394e3f | 63,315 records, 107 columns; year/month, area code/name, sex, total, ages0–99 and100+. All rows have107 cells; no blank cells. | Mixed geographic/sex totals require filtering; registry not occupancy. Later allocation audit confirms bounded age/sex arithmetic consistency, not boundary/version joins or independent population accuracy. |
| Fire register7a800e92 | 185 records, eight columns: item ID, district code, village, listed name, listing criterion, difficult-rescue place, responsible unit, contact. All rows have8 cells; no blank cells. | Earlier file date2024-08-01; no geometry or current site verification. Text ranges need interpretation. |
| Liquefactionec40e067 | Full703,720-byte GeoJSON:136 MultiPolygons; CRS84; properties only `class`, values1/2/3 with38/45/53 features; no missing geometry. Supersedes sample-only access finding. | At the primer stage these checks were unresolved; the later allocation audit now identifies2 invalid geometries. Source class mapping, scale, independent survey coverage and exact redistribution terms remain unverified. Do not treat raw class codes as a risk score. |

**Domain evidence and source ledger:** sources below were read on2026-10-13. HTML/text inspection is limited to the linked substantive sections; search excerpts alone are not sufficient for engineering rules. No engineering analysis, site visit, materials test, professional review or model validation occurred. US guidance supplies conceptual comparison, not Taiwan legal criteria. Published material is linked/paraphrased, not redistributed as source files.

| ID | Primary source and inspected scope | Claim and boundary |
| --- | --- | --- |
| D01 | [MOI structural safety performance assessment rules](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070259), arts2,4,5,8; displayed2018-10-11 revision | Initial and detailed assessments are distinct; both require on-site investigation/testing under their applicable methods. Reports identify scope/structure/results and qualified institutions/personnel. No universal residential threshold is derived here. |
| D02 | [NCREE TEASPA FAQ](https://teaspa.ncree.org.tw/Home/FAQ), assessment/model-check/report descriptions; [download index](https://teaspa.ncree.org.tw/Home/Download) | Professional modeling includes applicability, input and result checks. Index establishes available manuals, not a completed current-method implementation. |
| D03 | [NCREE existing-RC assessment report09023](https://www.ncree.org/rcbpa/09023.pdf), full PDF downloaded and text-parsed; tables3.2–3.3 and short-column/ductility passages | Historic school-building technical description supports the kinds of as-built survey/material inputs: alterations, damage, dimensions, reinforcement and strengths. Selected passages inspected, not every page; school scope is not a general residential rule. No historic sampling quotas/default strengths adopted as current requirements. |
| D04 | [NCREE private-building weak-story program](https://privatebuilding.ncree.org.tw/), substantive explanation | Weak-story retrofit can be an interim prevention measure before full retrofit/reconstruction. Does not establish whole-building functional recovery or present funding availability. |
| D05 | [NIST Community Resilience Program](https://www.nist.gov/programs-projects/community-resilience-program), definition, dependencies and code distinction | Resilience includes preparation, resistance and recovery within a specified period; community functions depend on buildings/infrastructure and social systems. Life safety and recovery objectives need separate treatment. |
| D06 | [NIST Functional Recovery](https://www.nist.gov/programs-projects/functional-recovery-buildings-and-lifelines), objective/tasks | Functional recovery examines structures, nonstructural systems, lifelines and economic/implementation factors. This is an evolving framework, not a certified local scoring tool. |
| D07 | [NIST planning guide volumeII](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1190v2.pdf), buildings executive summary (publisher-indexed passage) | Building clusters serve community functions with differing recovery objectives and dependencies. Full guide not audited. |
| D08 | [FEMA P-58-6](https://www.fema.gov/sites/default/files/documents/fema_p-58-6_guidelines_for_design.pdf), §§3.2.2.2–3 publisher-indexed passage | Repair cost and repair time are performance measures; repair-work duration omits delays for financing, planning, permits and contractor mobilization. Direct PDF retrieval via web failed; full publication not audited. No numerical loss/time prediction or loan threshold used. |

**Inference — reverse-thinking method:** start with a named decision, hazard scenario and required function: for example, protecting life and preserving a viable housing option after a specified earthquake. Trace failures backward through unsafe structure, unusable stairs/equipment, unavailable water/power/access, then repair/finance/coordination delay. Separate (1) hazard and site demand, (2) structural vulnerability/capacity, (3) exposed occupants and consequences, (4) nonstructural/utility functionality, (5) recovery resources and (6) action feasibility. This is a synthesis for this research, not a standardized index or an additive equation. Engineering ductility is deformation capacity before loss of load resistance; it is distinct from the broader recovery meaning of resilience.

**Illustrative technical mechanisms, not site findings:** weak/soft-story mechanisms can concentrate strength deficiency or deformation at one level; these terms are related but not identical. Irregular geometry can produce torsion, short-column configurations can concentrate shear demand, inadequate reinforcement detailing can limit ductility, and corrosion/alterations can change capacity. None can be established from age totals or street-view appearance alone. Actual demand/capacity assessment requires a qualified professional to select a suitable method for the structural system, collect as-built/material evidence, check assumptions and identify failure modes; nonlinear analysis may be used when the selected method calls for it, not mandated for every assessment here.

**Assessment chain:** define scope and performance target → obtain building identity, drawings/alteration history and site conditions → qualified site survey and applicable initial assessment → appropriate detailed evaluation and material/geotechnical investigation where required → compare feasible retrofit/reconstruction/preparedness options → verified design/construction and continuing management. Population-wide screening is preliminary triage; it is not interchangeable with the legally defined initial assessment. Post-earthquake emergency usability assessment is a separate time-specific decision and does not replace pre-event evaluation.

**Consequence and recovery:** useful outputs differ by purpose: safety/failure mechanisms, damage and repairability, habitability/service disruption, recovery time, economic burden and people needing assistance. Recovery diagrams in the HTML are deliberately qualitative, fictional teaching aids with no numerical time/probability estimates. High older-population counts change assistance/consequence questions, not concrete strength. Fire access affects response/access, not frame capacity. Liquefaction context is a site-hazard clue, not a structural diagnosis. Age is a lead for code-era/history inquiry, not a deterministic verdict. Comparing interventions requires the same hazard/occupancy basis and consideration of uncertainty; arbitrary weights cannot replace calibrated evidence. Missing data means unknown, not safe or unsafe.

**Hypothesis and rejection:** a source-linked evidence-gap review for one building may help a professional decide what to inspect next. No observed practitioner need or incremental benefit over the official assessment pack is established. Reject automatic real-building safety/renewal rankings from the four starter files; reject a new checklist if it changes no professional action. Do not infer an assessed need for reconstruction from a screening flag, or equate renovation, targeted weak-story retrofit and complete seismic upgrade. Technical need, equity priority and feasibility must remain separately visible so difficult-to-organize vulnerable communities are not hidden by a convenience ranking.

**Open question / next executable check:** inspect public building/permit/cadastral source catalogs for legally reusable building identity, address/geometry, completion/permit dates, structure and floors; verify record scope and one join before claiming coverage. In parallel as a dependent later check, locate a consent-safe professional assessment example for validation, not training on unverified labels. Such sources are acquisition leads only; current public building-level coverage remains unknown. Essential private assessment/occupancy evidence must stay outside public Git. This primer does not upgrade any T06 operational decision readiness.

## 4. Candidate workflows

### Allocation hypotheses A and B — inspection and public renewal are different decisions

**Owner decision — 2026-10-13; report revised2026-10-14:** reorganize the existing report around official issue6's core resource-allocation pain, using reverse thinking and point-of-decision data assessments. Record available/missing fields, observation period, file/metadata update dates, retrieval dates, quality tests and decision suitability. Retain professional domain education as supporting explanation. HTML remains local; this request does not authorize public publication or implementation.

**Inference — scope and failure analysis:** official issue6 proposes a weighted model to prioritize inspections and public renewal. It does not itself prove that current prioritization is ineffective or that one weighted score improves it. Current municipal selection criteria, backlog, staff capacity, past decisions and their outcomes have not been obtained. Work backward from avoidable allocation mistakes: missing an important case; treating an unobserved building as safe; conflating a need for assessment with a need for reconstruction; excluding a hard-to-organize community because feasibility is low; or producing unstable rankings under plausible assumptions. Technical risk/consequence, evidence uncertainty, equity and action feasibility are separate decision dimensions, not interchangeable score components. A priority list must state its allocation unit, budget/capacity, eligible universe, decision authority and handling of unknowns. No calibrated combined score or numerical cutoff is introduced.

**Evidence — publisher metadata refreshed2026-10-13:** original Taipei catalog substantive sections were opened for all four official starter datasets. Building-count observation period is1976–2025; metadata2026-02-26, annual, resource says system integration with no independent file-update timestamp. Population latest resource update2026-10-05, metadata same day, monthly, actual downloaded periods2023-01–2026-09. Fire register file2024-08-01, metadata2025-12-09, irregular, no per-record survey date. Liquefaction catalog coverage2016-09-10–2018-03-23, metadata2025-06-17, irregular, system-integrated resource with no independent file-update timestamp. Catalog coverage is not proof of the actual survey date of every feature. All catalogs label access public/free and link general government data terms; exact resource-specific attribution/exception scope is not fully audited. Do not report retrieval2026-10-13 as a publisher update or current physical observation.

**Evidence — deeper bounded file audit2026-10-13:** downloaded the same four exact resources linked in the T06 primer using normal-TLS curl. Parsed full CSVs with Python `csv.DictReader` (populationBig5, othersUTF-8-sig); numbers parsed as integers after stripping comma separators. Tested all rows, not a convenience sample. For geometry used Shapely2.2.0 / GEOS3.14.1 `shape`, `is_empty`, `is_valid`, `explain_validity`. No `make_valid`, deduplication, imputation, geocoding or original-value correction applied. These are internal checks, not external ground truth or validated ranking tests.

| Dependency | Completed quality test and result | Qualification / allowed use |
| --- | --- | --- |
| Populationa6394e3f | 63,315 rows/107 columns. All101 age cells sum to total in every row; zero negative age/total values; zero duplicate `(year,month,area-code,sex)` keys. All21,105 area-month groups have計/男/女; all age/total cells satisfy計=男+女. All45 monthly labels2023-01–2026-09 present. | Internally consistent for the tested conditions, conditional descriptive use after selecting geographic level/sex and common date. Complete labels do not prove every village's stable coverage, boundary consistency, residence accuracy or building occupancy. |
| Building counts7889e8a0 | 50 effective annual rows/13 columns. Age bands both zero1976–2006 (31years), so their zero sums disagree with positive totals;2012 also mismatches: total232005 versus age sum232783. Floor sums mismatch2015:232280 versus total232164;2016:231611 versus total231490. | Needs qualification. Do not silently repair or treat early zero age bands as no old buildings. These arithmetic differences require publisher definitions/correction before related trend calculations; they do not prove their cause. Still city aggregate, never individual screening. |
| Fire register7a800e92 | 185 rows/8columns; no blank cells, duplicate item IDs or identical full rows;12 district codes. | Internally readable register, currentness and spatial identity unresolved. No coordinates, polygon, measured clearance, closure state or survey timestamps; an unlisted street is not proven easy to rescue. |
| Liquefactionec40e067 |136 nonempty MultiPolygons. Two fail GEOS validity: zero-based feature96 and108, both ring self-intersection. Classes1/2/3 count38/45/53. | Flag and withhold invalid features from unqualified spatial joins; preserve originals. Source-approved repair method, class mapping, scale and coverage interpretation needed. A valid polygon is not independently verified hazard truth; no automatic parcel/building diagnosis. |

Snapshot identities SHA256: population `a478cb4d3cdf509eec3453285bf0c1c542b7f53268608348ced4bafa7150bed3`; buildings `8f471e3d2ab5ef6e17d5b7408a74b370458cc12870de57e0dced2fc086c2bde4`; fire `873c138fbc367b3123412785c2d1492fa7f4b2d1f73b4788f40587ce77145797`; liquefaction `0d49ecbf7ab702ba35d3ba7c52765d4ba9952d12b2f9e3c003c71b38fe40f32c`. Original raw files are not distributed. These identify this observation, not a promise that later publisher downloads have the same bytes.

**Inference — suitability:** whole-city age totals cannot create a neighborhood building-age layer; neighborhood older-population context cannot identify residents of a building; fire-access text cannot establish a building's actual access or structural vulnerability; liquid-susceptibility geometry cannot establish building capacity. Combining those units does not recover the missing linkage. Data completeness has separate meanings: successful whole-file retrieval, geographic/time/universe coverage, complete necessary decision fields, internal consistency and independent accuracy. Passing the first or fourth does not imply the others. Use claim-specific categorical states (usable for context, conditional, blocked for a stated claim, unknown), not unsupported overall quality scores.

**Hypothesis — A, municipal inspection allocation:** a city assessment-program reviewer assigns a limited number of investigation/assessment slots across a defined candidate universe and period. Actual office/authority, existing queue/rules and user bottleneck remain unverified. Baseline must be the existing program's case selection and professional review, not an invented oldest-first policy. Input authorized building identities/status, dated site/structural evidence, relevant consequence context, missing-evidence flags, existing assessments and available slots → compare inspect/request evidence/defer with reasons → authorized reviewer issues a checkable assignment and records deferred/unknown cases. Success is fewer independently adjudicated important omissions or lower effort at equal coverage than the same-case baseline, without misrepresenting unknown as safe. Reject if existing practice already covers those decisions or missing building evidence prevents meaningful discrimination. Current public inputs support data-gap documentation only; no real queue/ranking. Demonstration specified as a disclosed fictional allocation case; decision insufficient; operational/civic gain unobserved. Adoption needs named authority, professional reviewer, secure identity/evidence handling, assessment capacity and cost; none committed. Next: verify one building identity/permit-source join, then discover current selection rules and backlog definitions without requesting personal case data.

**Hypothesis — B, public-renewal review priority:** an authorized municipal renewal reviewer decides whether a previously assessed area/case merits further public-renewal feasibility review. Exact authority/program/baseline unknown. A result of A is not an automatic B decision. Inputs need professional assessment/current status, project boundaries, reinforcement and other alternatives, public-interest/equity considerations, consent/property constraints, temporary housing, costs, funding and execution capacity → compare investigate alternatives/advance feasibility/defer with explicit unresolved issues → attributable review disposition, not a reconstruction order. Success is a better-supported, executable and professionally adjudicated review disposition than existing practice; reject automatic renewal recommendations without these inputs or when a new artifact changes no action. Existing subsidy rules are not a public-renewal allocation rule or an actual funded project queue. Demonstration specified only with fictional cases; decision insufficient; no real benefit/cost or safety result. Adoption requires municipal/legal/engineering expertise, lawful project evidence and capacity; costs unknown. Next after A's identity prerequisite: locate the exact public-renewal selection criteria and one published decision record; do not substitute private retrofit subsidy criteria.

**Validation proposal — not executed:** freeze a professional-adjudicated case set with building IDs, dated evidence and decision purpose. Compare current process against the proposed reasoned triage, including assessed/unassessed, contradictory, recently altered, high-consequence and hard-to-coordinate cases; selection is failure-mode coverage, not representative prevalence. Measure important omissions, unsupported assertions, reviewer effort, unknown-case handling and reason traceability. Test rank/list changes under plausible evidence and weight assumptions; flag unstable cases instead of claiming precise order. No arbitrary score, success percentage, equal weights, top-N budget, sensitivity range or complete candidate census is invented. Legal safety gates must remain professional gates. Observed task benefit, stable decisions and later allocation/civic outcomes are separate acceptance stages.

**Superseded next step — 2026-10-13:** verify whether one legally reusable building/permit source supplies stable identity, location, completion/permit date, structure and floor scope for one building. Completed below; the result changes what the allocation hypotheses can claim.

### Hypothesis A revised — tiered screen-to-verification sequencer

**Inference — no implementation authorized:** reframe A from a weighted safety score to a **tiered screen-to-verification sequencer**:

1. An observable inclusion rule, such as a pre-1999-12-31 construction permit, with an explicit "status unknown" class.
2. Recorded quick-screen-like attributes assign tiers with stated reasons. Missing attributes raise verification priority instead of lowering risk.
3. A separate road-segment layer counts how many candidate buildings could block each fire-rescue segment.
4. A separate support layer uses elderly occupancy and facility type to choose outreach intensity, not hazard.
5. Versioned rules and a change log.

Success still requires a frozen professional comparison. Candidate validation data are the city's confidential initial-assessment records and damage tags, accessible only through an authorized request. A disclosed fictional or district-aggregate demonstration remains possible from open data. Decision readiness stays **insufficient**.

**Hypothesis B consequence:** public renewal is driven by land, willingness and finance thresholds. A risk ranking can at most inform the city-designated policy-area clause and outreach, not select cases.

**Open questions / unfound:**
- Taipei annual proactive and owner-initiated initial and detailed assessment counts, result distributions and weak-storey completions (likely in CMO monthly reports to MOI, council business reports or Taipei audit reports).
- The Taipei quick-screen F-value list.
- Full text of the 115–118 national seismic plan.
- 575/7599 intake counts.
- Private full-retrofit costs per m².
- Taipei bulk land-registry supply rules.
- Guest-visible coverage of img2.gov.taipei.
- The current status of NCDR's grid and NCREE inventories.

**Current next step:** two routes remain, and the owner chooses between them:
- **Public read-only:** read Taipei City Council business reports and Taipei audit reports for Taipei-specific assessment and retrofit counts.
- **Information request:** request de-identified initial-assessment statistics from CMO, or house-tax statistics under 稅捐稽徵法 §33 ¶2. A request is an external contact and needs owner confirmation.

### T06-A — Reach the appropriate professional assessment pathway

**Problem/user/decision.** Hypothesized user: a Taipei condominium committee or owner representative deciding what to prepare before commissioning an initial assessment this month. Consequence: an unauthorized or incomplete submission cannot enter the illustrated process [S03–S04]. Historical national underperformance supports investigation of assessment uptake, but does not identify missing information as its cause [S13]. No contemporary applicant difficulty was observed.

**Exact baseline.** CMO already provides A1/A3 forms, the one-page flow, FAQ consent exceptions, institution/service-area/fee indexes and professional consultation stations [S03–S05]. A generic eligibility chatbot or new directory is redundant unless it measurably helps applicants assemble the correct professional-review packet. Assessment consent, inspection authority and reconstruction consent must remain separate; a renter cannot simply authorize collective work.

**Success/rejection.** Success would be fewer omitted prerequisite documents or less applicant effort than using that exact pack, without incorrect assurances. Problem rejection: competent users complete the same task from S03/S04 without extra assistance, or delays are chiefly unresolved consent/capacity. **Unresolved**; defer product-value claims. Data rejection: missing ownership/management authority, legal-building evidence or professional findings prevents an eligibility conclusion. **Supported** for open-data-only automation; narrow to an explicit missing-information checklist. An age/map safety answer is rejected.

**Workflow/dependencies/claim.** Owner-provided, private authorization status and available documents → human-reviewed missing-document comparison against dated official pack → prepare questions/documents for an approved institution → observable consultation-ready checklist. Required facts: applicant authority, building unit/legal records, relevant report/version and chosen program. These are not supplied by public citywide data; obtain only from consenting applicants outside Git. Public rules may be linked under S14; reports stay private. No structural verdict, subsidy guarantee or appointment promise.

**Validation/result.** Smallest test: compare the official pack with a paper checklist on three rule branches—single-owner exemption, committee resolution, insufficient collective consent. Three is branch coverage, not a representative sample. Manual source comparison completed: S04 Q7/Q10/Q27 already answers all three; additional routing knowledge was **not demonstrated**. Timing, comprehension and real omissions were not measured. Accept no false statement of authorization; it can cause an invalid submission. Any claimed effort gain needs counterbalanced applicant tasks and professional adjudication; no invented speed target.

**Readiness/adoption/presentation.** Demonstration **specified** as a disclosed fictional checklist; decision **insufficient**; task usability and civic outcomes unknown. CMO Use Division and approved assessment institutions are plausible operators, not committed adopters. A 100-day path needs a rule owner, review time, accessible service design and live capacity checks; costs unknown. Before/action/after example: a fictional committee has no recorded resolution → compare Q10 and prepare a meeting-record question → checklist says “authority evidence missing,” never “building unsafe.” **Next executable check:** compare Q7/Q10/Q27 against the linked current legal text and mark every consent exception before testing any checklist with an authorized practitioner.

### T06-B — Decide whether to commission a retrofit/renewal feasibility comparison

**Problem/user/decision.** Hypothesized Taipei community representative, with an existing professional assessment, decides whether to seek a scoped comparison of interim reinforcement, broader retrofit and reconstruction. NCREE's Pingtung account documents an operator encountering unaffordable full reinforcement and developing a phased alternative [S08]. The concrete problem is financing and coordination around an actionable professional option, not merely identifying an old building. Transfer to Taipei is unresolved.

**Baseline.** Existing professionals explain assessment results and evaluate alternatives; NCREE supplies cases and free explanations. Taipei has separate assessment/weak-layer routes and URO's structural-reinforcement subsidy pack, including contracts, cost breakdown and household self-funding shares [S02,S06,S14]. These are different programs; a single subsidy calculator risks mixing requirements. City renewal audit landing evidence also points to valuation transparency and supervision, not a missing risk heatmap [S13].

**Success/rejection.** Improvement would be a meeting ending with an agreed, executable professional feasibility request and explicit unresolved financing/consent items, with fewer misunderstandings than the existing professional explanation. Problem rejection: liquidity, disagreement, relocation or procurement blocks every feasible next step despite correct information. **Plausible and unresolved**, so do not promise faster renewal. Data rejection: no actual report, professional scope/quotes, ownership decision or funding-status evidence means no comparative recommendation. **Supported** for present public inputs; reject automated “rebuild versus reinforce” selection. S07 shows subsidy is capped/partial and can stop when exhausted; information cannot eliminate the funding gap.

**Workflow/dependencies/claims.** Consenting community supplies its professional report and questions → facilitator separates technical feasibility, collective authority and household funding → commission professional comparison or record a justified deferral → observable scoped request/meeting decision. Essential evidence includes construction scope, engineer's assessment of improvement benefit, consent, occupancy/disruption constraints, quotes, subsidy eligibility and actual funds. Public rules establish requirements only. Individual costs, final awards and professional availability are unknown; no synthetic engineering estimate substitutes for them.

**Validation/result.** Minimum decisive comparison is one qualified case plus one exclusion and one borderline case: an existing assessment with financing unanswered; a project already in a prohibited overlapping reconstruction stage; an applicant requesting only cosmetic improvements. These cover action versus stop branches, not effectiveness prevalence. Completed desk check: S06 distinguishes structural-benefit evidence from cosmetic works and lists exclusions; S07 makes an unconditional full-funding promise untenable. Actual case comparison is **infeasible in this scope**: no consented reports/quotes or professional adjudicator. Do not quantify household savings. Tolerance is no engineering recommendation beyond the commissioned expert's scope; compare comprehension/next-action completeness before defining a performance target.

**Readiness/adoption/presentation.** Demonstration **specified** using fictional missing-input states; decision **insufficient**; usability, adoption and civic safety gains unknown. CMO/URO, licensed professionals and owners would jointly hold authority; a facilitator cannot bind them. Within 100 days a comparison template could be reviewed, but financing, procurement and works cannot be assumed resolved; expertise/cost unknown. Before/action/after: fictional assessed community cannot fund full work → request phased-option and self-funding review → dated feasibility brief with unanswered consent/funding, not a safer-building claim. **Next executable check:** cross-read S06 exclusions with S07 annual notice into a program-specific evidence checklist; leave funding availability explicitly unverified.

### T06-C — Choose an outreach action without ranking buildings' safety

**Problem/user/decision.** Hypothesized district/community facilitator chooses the content and professional referral for one requested community meeting. NCREE's original account links an affordability concern, tailored cost/scope explanation and reported willingness change [S08]. It does not prove that lack of outreach causes low uptake in Taipei. The inspected conference abstract reports associations with neighbor agreement and subsidy familiarity [S09]; intention is not completion. Its finding that risk perception alone does not significantly drive action differs from the journal abstract calling risk perception a key driver [S10]. Different analyses and unavailable full methods prevent resolving that difference; neither establishes an outreach effect.

**Exact baseline and defensible narrowing.** Communities can already request NCREE's free explanatory visit; Taipei has community architects and promoter stations, with institutional references in S05/S14. Therefore “find a nearby adviser” alone is not an evidenced gap. A defensible hypothesis is preparing an opt-in meeting around the community's stated barrier and necessary authority, then referring to the existing professional service. Area demographics may guide language/accessibility support only after validation, never infer household need or building danger. Do not introduce a new neighborhood-priority workflow without its own owner and service-gap evidence.

**Success/rejection.** Relative success: facilitator prepares a clearer referral and one checkable next step than the existing request process, without greater administrative work or misleading claims. Problem rejection: existing staff already capture these issues, or no professional can accept referrals. **Unresolved**; do not claim an outreach bottleneck solved. Data rejection: no current outreach coverage, opt-in demand, nonparticipation reasons or available capacity means geographic targeting cannot be defended. **Supported** for current evidence; reject the citywide priority map. No public evidence of difficulty is not evidence of no difficulty.

**Workflow/dependencies/claims.** Private community request, stated concern and consent to follow up → classify the question as assessment preparation, funding/authority or professional technical explanation → facilitator prepares an existing-service referral/meeting agenda → observable invitation draft and agreed follow-up question. Sending it requires separate authorization. Necessary operational fields: request date, topic, prior contact, accessible meeting preferences, responsible service and confirmed capacity. None can be inferred from population, street polygons or liquefaction. Use fictional inputs for a demo; real participation records stay private; NCREE material is linked, not redistributed under an assumed license.

**Validation/result.** Smallest desk experiment deliberately tests three difficult messages: “our soil-map color proves danger”; “we lack neighbor consent”; “subsidy will pay everything.” Comparing the current services and sources yields: professional site referral with no safety diagnosis [S11]; consent/meeting pathway [S03–S04]; program-specific funding clarification [S06–S07]. All have an existing professional route; new operational benefit remains **unresolved**. Three cases cover the distinct safety, authority and financing error modes identified in the sources; they are not a population sample. This semantic stress test rejects unsupported messaging, not real-user pain. A later paired facilitator task should measure preparation effort and corrected misconceptions using the existing meeting request as baseline; zero false safety or funding assurances is required by the consequence, not an arbitrary accuracy percentage. Capacity must be confirmed before claiming an executable booked action.

**Readiness/adoption/presentation.** Demonstration **specified** as opt-in agenda preparation; decision **insufficient**; civic outcome unknown. NCREE/CMO and community representatives are plausible operators. A 100-day pilot needs a named professional recipient, privacy/retention owner, staff time and available meeting slots; demand, cost and willingness to adopt are unknown. Before/action/after: a fictional community requests a meeting because it saw red liquefaction shading → prepare a professional question about foundations and an assessment/consent checklist → draft referral, explicitly no danger rating. **Next executable check:** inspect the current NCREE meeting-request instructions and Taipei station service-hours attachment for required intake fields and routing; this is read-only, without submitting a request.

### T06-D — Route finder for a blocked walk-up

**Candidate — T06-D route finder for a blocked walk-up (hypothesis, not implemented):**
- Input: one building's facts.
- Output: the routes it can legally take, each route's consent threshold, and the evidence (for
  example an assessment result) that would change which routes apply.
- Action: an informed next step with a promoter or CMO.
- Baseline: the promoter's explanation and the CMO FAQ.
- Rejection: the FAQ or a promoter already answers it in one step, or blockage is economic rather
  than informational.

**Data experiment, not yet run:** freeze the promoter register now. Re-read it later and compare
stage transitions. Look for an archived older copy that would give conversion without waiting.

## 5. Evidence and data audits

### Building identity audit — public chains cover new buildings, not the old-building universe

**Owner decision — 2026-10-14:** continue focusing on issue6 old-building resilience. Research-only; no request, account, submission or implementation.

**Method — retrieved 2026-10-14:** downloaded the national open-data catalog CSV export (`https://data.gov.tw/datasets/export/csv`) and filtered Taipei/MOI dataset titles for permit, building, doorplate, sea-sand and seismic terms; data.taipei's search endpoint ignored every tested keyword parameter, so it was not used for discovery. Downloaded the resources below with normal-TLS curl and parsed them locally: XML with `xml.etree.ElementTree.iterparse`, CSV with `csv.DictReader`, shapefile with pyshp plus Shapely2.2.0, PDF with `pdftotext -layout`. Addresses were normalized only by NFKC width folding, Arabic-to-Chinese `段` numerals, district-prefix removal and floor-suffix removal; no geocoder, fuzzy matching or source correction was used. Raw files, personal names and per-building outputs stay outside Git. The catalog labels the Taipei resources Government Open Data License v1; dataset notes call permit summaries and permit maps reference-only, with the scanned permit system and approved drawings authoritative.

| ID / publisher resource | Full-file observation | Identity value and limitation |
| --- | --- | --- |
| **B01** CMO [歷年使用執照摘要 128203](https://data.gov.tw/dataset/128203), file `Taipei02_90年至114年.xml`, SHA256 `a20261e8…0e41c8` | 8,762 use permits ROC090–114 (2001–2025), no duplicate permit number. Missing: completion date219, address25, lot24. 新建7,825/增建765/修建141/改建31. Fields include original construction permit, structure, floors, completion date, every doorplate and land lot | Stable permit identity with structure/floors/completion. **Coverage starts2001**: no use permit issued before that year is present. Named designers/contractors not retained |
| **B02** CMO [建築執照套繪圖 151936](https://data.gov.tw/dataset/151936), `taipei_1151005.zip`, SHA256 `f063f6a7…bdf48734` | 10,052 TWD97 polygons; one null shape, zero invalid. `budatt_no` years ROC90–115; 1,868 zero floor values and 1,858 blank structure values; 472 IDs deviate from `year.serial.floorsF` (text suffixes, amendments) | Footprint geometry for post-2001 permits only; publisher says reference only, not proof of position |
| **B03** Civil Affairs [門牌位置數值資料 155472](https://data.gov.tw/dataset/155472), file dated2026-10-02, SHA256 `72120581…2a89ab` | 1,157,763 doorplate rows, zero blank coordinates; 270,991 floor-stripped address keys at 247,955 distinct points | Survey-built address points. An address is not a building: one building has several doorplates and the file has no building ID |
| **B04** MOI [實價登錄 Taipei season files](https://plvr.land.moi.gov.tw/DownloadOpenData), 113S1–115S3 (11 seasons; 115S3 SHA256 `b87fa4f7…837c`) | 55,614 building transactions carry `建築完成年月`, `主要建材`, `總樓層數` and an unmasked doorplate; 54,635 (98.2%) matched a B03 key after normalization | Covers only transacted addresses: 26,562 B03 keys (9.8%), of which 19,526 completed by ROC85 (1996). Four keys show two completion dates, so one address can denote several buildings. MOI open-data declaration grants attributed reuse and assigns personal-data compliance to users; separate usage-rule text not inspected |
| **B05** CMO [高氯離子列管清冊 PDF (115.9.25)](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/3e35701e-4134-4ab3-956e-a3d2a8dce18e.pdf), 14 pages, SHA256 `857cc766…62ab3`, via [listing page](https://cmo.gov.taipei/cp.aspx?n=4B7B63655A6565E9) | Sequence to180; 173 single-line rows parsed with address, original use-permit number and households. Permit years ROC50s–80s, mostly70s. First doorplate resolved to B03 for165/173 | The only inspected public building-level structural list with old permit identity. Publisher states absence from the list does not mean a building is not high-chloride. Contains owner names; none copied |
| **B06** CMO [海砂屋列管清冊 128196](https://data.gov.tw/dataset/128196) and [地震列管建築物 128208](https://data.gov.tw/dataset/128208) | 128196 has 5 rows from file `1141204_市有…`, city-owned buildings only; 128208 has 36 yellow-tag address rows from file `1150318` | 128196's title overstates scope; use B05 for the full register. 128208 addresses are free-text ranges |
| **B07** MOI Land Administration [土地建物參考資訊 173221](https://data.gov.tw/dataset/173221), generated2026-10-14 | 26 files; no Taipei row mentions high-chloride, sea-sand, seismic, red- or yellow-tag terms | Bulk land-reference export does not carry Taipei's structural listings; the publisher notes some agencies refuse batch download |

**Evidence — first verified join:** `budatt_no` is the **construction-permit** number plus floors, not the use-permit number. Linking each standard ID to B01 records whose original permit equals `YYY建字第NNNN號` gives 7,760 links: floors agree in7,721 (99.5%); where any permit doorplate resolved in B03 (6,261 links), a point lies within15m of the polygon in4,999 (79.8%). Reading the same IDs as use-permit numbers gives floor agreement in only546 of7,963 and no position agreement. Example: polygon `101.0225.6F` → `101建字第0225號` → `104使字第0224號`, RC, six floors, completed2015-05-15, one Shilin doorplate and land lot. B01+B02+B03 therefore form a reproducible identity/location/structure chain **for buildings with use permits from2001 onward** (footprints only for construction permits from2001).

**Evidence — completion-date consistency:** 27 B05-listed buildings appear in B04 with35 transactions. In all35 the completion ROC year equals the year of the listed use permit. Both values likely descend from the same permit/registration chain, so this checks internal consistency, not independent accuracy.

**Inference — consequence for allocation:** the verified building-level chain covers the newest part of the stock: issue6's target population, buildings roughly30 years or older (use permits before1996), is outside B01/B02 by construction. For older buildings, public data supply only (a) transaction-derived completion year, material and floors for about one in ten address keys, biased toward traded residential units, and (b) listed problem registers such as B05. Neither defines the eligible universe, and an untraded or unlisted building remains **unknown**, not newer or safe. A full old-building inventory with identity, completion date and structure would need an authoritative non-open source: building registration, house-tax registry or the scanned permit-image system (`img2.gov.taipei`, a script-rendered app whose coverage, query rules and terms were not observable without interactive use). Access to any of them is an owner/authority question, not a data-engineering step.

**Hypothesis consequence:** A, municipal inspection allocation, can now demonstrate a disclosed three-state universe for a fictional or authorized pilot area: buildings with 2001-or-later use permits with verified identity; older addresses with transaction-derived attributes; and buildings with no public attributes. It still cannot rank real buildings. B05 is useful as a test of whether a reviewer's list preserves known listed cases, not as risk labels for unlisted buildings. B is unchanged.

**Superseded next step:** locate current selection rules and the pre-2001 inventory holder. Completed in the deep investigation below; its next step governs.

### P — Current selection rules and baseline numbers

| Metric | Value | Period / as of | Source |
|---|---|---|---|
| Proactive initial-assessment unit subsidy (MOI → city) | NT$15,000 + NT$1,000 review + NT$500 admin per building | Rule effective 2022-05-12 | P02 |
| Proactive eligibility | F > 60, or age ≥ 30; plus management organisation and ≥ 6 storeys; or city discretion | Same | P02 |
| Weak-storey retrofit cap (general) | Plan A < 500 m²: NT$3M at 45%; Plan B: NT$4.5M at 45%; raised to NT$4.5M at 85% if initial danger score > 45, detailed assessment says retrofit or rebuild, or city-designated; Plan C repair NT$500k | Same | P02 |
| Weak-storey eligibility | Initial danger score > 30 (A/B) or > 45 (C); or detailed result; or red tag; or city decision. Public buildings and single-owner buildings (A/B) excluded | Same | P02 |
| Taipei owner-initiated initial subsidy | NT$12,000 (< 3,000 m²) / NT$15,000 (≥ 3,000 m²) + NT$1,000 | 2026-01 FAQ | P16 |
| Taipei detailed subsidy | ≤ 30% of fee or NT$400k; review 15% capped at NT$200k | 2026-01 | P16 |
| National annual targets 2022–2025 | 300 proactive; 3,000 initial; 34 detailed; 30 weak-storey; 500 reconstruction plans | Per year | P05 |
| National achievement 2019 to 2021-09 | Initial 4,147 of 19,555; detailed 2 of 500; weak-storey 21 of 725; quick screen 19,191 of 20,000 | Cumulative | P05 |
| National 2016–2017 安家固園 | Initial 7,984 of 96,000 planned; detailed 4 of 2,260; quick screen 9,125 completed of 11,000 planned | To 2018-10-29 | P06 |
| Quick-screen universe | ~36,000 pre-2000 buildings ≥ 6 storeys nationally; NT$2,000 per building | 2019 plan | P06 |
| 老宅延壽 targets | 3,000 buildings (common-area repair), 3,000 units, 600 assessments, 44 team contracts | 2025–2027 | P30 |
| Taipei 危老 cumulative applications / approvals | 1,179 / 1,047 | To 2025-11-30 | P29 |
| Taipei 危老 cumulative starts | 530 | End-2024 | P29 |
| National 危老 cumulative applications / approvals | 5,042 / 4,695 | To 2025-11-30 | P29 |
| Taipei sea-sand listed | 105 cases / 283 buildings / 5,549 households (97 demolish, 8 strengthen) | 2023-09-25 | P22 |
| Taipei high-chloride listings (CY) | 144; 71 past stop-use; 90 appeals; 10 lawsuits | 2011-01-01 to 2025-04-25 | P28 |
| 921/331 yellow tags remaining | 49 (37 + 12) | ~2023 | P22 |
| 0403 safety-concern reports, Taipei | 2,140 | 2024 | P18 |
| 0403 yellow-tag list entries | 7 | Version 2026-07-20 | P27 |
| 403 repair subsidy budget | NT$80M (foundation) + NT$31.9M (city) | Plan 2025-01-14 | P26 |
| Building stock ≥ 30 years (tax register) | 195,125 of 256,808 (75.98%) | 2022 data | P22 |
| Use-permitted buildings ≥ 30 years | 98,423 of 115,457 (85.25%) | 2021-08 | P37 |
| Simulated M6.2 Shanchiao collapse | 1,852 buildings (full or half) | 2014 study | P25 |
| Public buildings needing retrofit or demolition | 43% of listed (54% concern at initial; 66% retrofit / 14% demolish at detailed) | To 2015-05 | P07 |
| Public premises improved | 12,423 (93.9%) | 2017–2025 | P31 |
| Public-led renewal thresholds | ≥ 1,650 m² and ≥ 50% public land; or ≥ 2,000 m² renewal area | 2020 rule | P19 |
| 575 willingness thresholds | > 50% to apply; ≥ 75% to proceed | 2026-04 revision | P21 |
| Disaster-prevention renewal | ≥ 1,000 m², all buildings ID < 0.35 → +30% base floor area | Adopted 2024-03-28 | P23 |

### E — Professional instruments, thresholds, code eras and costs

Initial-assessment (危老 附表一, RC/reinforced brick) scored items; weight w is chosen by the assessor and the score is points × w. Reinforced brick drops items 1, 5, 6, 8–11 and multiplies the remaining qualitative points by 2.5.

| # | Group | Item | Points | Scoring rule |
|---|---|---|---|---|
| 1 | Structural system | Redundancy (靜不定程度) | 5 | single span 1.0 / double 0.67 / triple 0.33 / ≥4 spans 0 |
| 2 | Structural system | Basement area ratio ra | 2 | w=(1.5−ra)/1.5, bounded 0–1 |
| 3 | Structural system | Plan symmetry | 3 | poor 1.0 / fair 0.5 / good 0 |
| 4 | Structural system | Elevation symmetry | 3 | poor 1.0 / fair 0.5 / good 0 |
| 5 | Structural system | Beam span/depth b | 3 | b<3: 1.0; 3–8: (8−b)/5; ≥8: 0 |
| 6 | Structural system | Column height/depth c | 3 | c<2: 1.0; 2–6: (6−c)/4; ≥6: 0 |
| 7 | Structural system | Soft-storey significance | 3 | high 1.0 / mid 0.67 / low 0.33 / none 0 |
| 8 | Detailing | Plastic-hinge hoop detailing **by design year** | 5 | before 1974‑02: 1.0; 1974‑02 to 1982‑06: 0.67; 1982‑06 to 1997‑05: 0.33; after 1997‑05: 0 |
| 9 | Detailing | Short columns from sills/high windows | 3 | high/mid/low/none |
| 10 | Detailing | Short beams from walls | 3 | high/mid/low/none |
| 11 | Condition | Column damage | 2 | high/mid/low/none |
| 12 | Condition | Wall damage | 2 | high/mid/low/none |
| 13 | Condition | Cracking/corrosion/leakage | 3 | high/mid/low/none |
| 14 | Quantitative | 475‑yr capacity Ac1/(I·A475) | 30 | ≤0.25: w=1; 0.25–1: w=(4/3)(1−ratio); ≥1: 0; Ac1=min(x,y) |
| 15 | Quantitative | 2500‑yr capacity Ac2/(I·A2500) | 30 | same form, Ac2 |
| S | Extra | +2 each: phased build or quality doubt; prior disaster; heavier use; visible tilt. −2: lighter use | +8/−2 | R = P + S |

Grade and decision thresholds by instrument:

| Instrument | Bands / cut | Source |
|---|---|---|
| 危老 附表五 | 甲 R≤30; 乙 30<R≤45; 未達最低等級 R>45 (Taipei template) | E01–E03 |
| PSERCB / public program / public-safety report | ≤30 no concern; 30–45 slight; 45–60 concern (priority 詳評); >60 definite (retrofit/demolish) | E12, E17, E33 |
| 營建署 "high-risk dwelling" | R≥60 or Ac/(I·A) ≤0.5 (475 or 2500) | E10 |
| Urban renewal danger | ID1 or ID2 <0.35 | E07 |
| Weak-story subsidy | A/B: R>30; C: R>45; raised rate R>45 | E08, E09 |
| 危老 art. 3(3) | 乙級 + ≥30 yrs + (rebuild recommended or retrofit >½ rebuild cost, or no elevator) | E04, E05 |

Seismic code-era milestones (content and effective dates as read; snippet-only dates marked):

| Date (promulgated → effective) | Change | Source |
|---|---|---|
| 1945‑02‑26 | 建築技術規則 first issued | E16 |
| **1974‑02‑15** (63年) | 構造編 full text. Seismic forces introduced: strong, moderate and weak zones; ductility factor; force by height or period | E16, E17 |
| **1982‑06‑15 → 1982‑07‑15** (71年) | Arts 42–55 revised following the 1976 UBC: seismic coefficients redefined; **importance factor I** added | E16, E17 |
| 1989‑05‑05 (78年) | Art. 44 amended (content not read) | E16 |
| **1997‑05‑01** (86年) | Major seismic revision after Kobe: **4 zones** (一甲, 一乙, 二, 三); vertical force; dynamic analysis and **storey-strength check** for irregular buildings; liquefaction considered; isolation principles; first 「建築物耐震設計規範及解說」 (art. 41‑1) | E16, E17, E18 |
| 1999‑09‑21 | Chi‑Chi earthquake | E17 |
| **1999‑12‑29** (88年) | 規範 amended after 921: zone coefficients, spectra, vertical force; **zones reduced to 2 (甲, 乙)**. Basis of the **1999‑12‑31 policy cutoff** | E17, E18 |
| 2004‑12‑14 → **2005‑07‑01** (94年) | Hazard-based coefficients; **microzonation** (Taipei basin 4 zones); near-fault effects; collapse prevention under the MCE; isolation and damping; EPA = 0.4 S_DS | E16, E17 |
| 2011‑07‑01 (100年) | 規範 revised: Taipei basin 4 → 3 microzones; isolation provisions | E17 |
| 2022‑06‑14 → 2022‑10‑01 (111年) | 規範 partial revision: §2.17 storey-strength check must include non-structural walls for all buildings of ≥2 storeys. Effective date from a search snippet; the revision content was read in E25 | E25 (content); effective date is an unverified lead |
| 2023‑05‑10 → **2024‑01‑01** | 構造編 arts 42, 43‑1 and others amended (content not read) | E16 |

Chloride limits: CNS 3090 1994-07-22: 0.6 general / 0.3 durability; 1998-06-25: 0.3; 2015-01-13: 0.15 (per Taipei manual); MOEA 2025-12-19 relaxed fresh RC to 0.30 and stated the table does not apply to hardened concrete (E22–E24). Taipei sea-sand demolition criteria combine floor-share thresholds for chloride ≥0.6 kg/m³, carbonation and strength, or a detailed-assessment collapse PGA below 150 cm/s² (E22, 2020 manual).

Cost, subsidy and duration references (not found: private full-retrofit cost per m² by method, damper/isolation cost, actual weak-storey project costs, detailed-assessment duration):

| Item | Value | Unit / basis | Year of source | Source |
|---|---|---|---|---|
| 初評 fee (most Taipei-listed bodies) | NT$20,000 | per building <3,000 m²; +NT$2–4/m² above | schedule PDF 2026‑03 | E15 |
| 初評 fee (others) | NT$15,000–30,000 | per building; +NT$5,000 if no drawings | 2026‑03 | E15 |
| 初評 central subsidy | ≤NT$12,000 (<3,000 m²) / ≤15,000 (≥3,000 m²) + NT$1,000 review | per building | 2019‑06‑13 | E06 |
| 初評 (active outreach) | NT$15,000 + NT$1,000 review | per building | directive 2022 | E08 |
| 詳評 fee, higher family | NT$250k (<600 m²); NT$400k + 300/m² (600–2,000); NT$820k + 225/m² (2–5k); NT$1.495M + 150/m² (5–10k) | per building incl. 15% review | 2026‑03 | E14 |
| 詳評 fee, lower family | NT$150k; NT$300k + 120/m²; NT$468k + 40/m²; NT$588k + 15/m² | same | 2026‑03 | E14 |
| 詳評 subsidy | ≤30% or ≤NT$400k; review ≤15%, max NT$200k | per building | 2019 / 2026 | E06, E38 |
| Weak-story A | ≤45%, NT$3M base, +NT$100k per 50 m² over 500 m², max NT$4.5M | per building | 2022 directive; NCREE site 2026 | E08, E09 |
| Weak-story B | ≤45%, max NT$4.5M | per building | same | E08 |
| Weak-story C | max NT$0.5M | per house | same | E08 |
| Raised rate | ≤85%, max NT$4.5M (R>45 / 詳評 retrofit) | per building | same | E08 |
| Hualien tagged buildings | NT$15M (>6F), 7.5M (≤6F), 2M (house); ≤85% | per building | MOI 2025‑08‑21 | E09 |
| Weak-story duration, Plan A | 50–170 days (cases); "2–3 months, residents stay" | per case | 2019–2026 | E09 |
| Weak-story duration, Plan B | 90–380 days (cases) | per case | 2021–2023 | E09 |
| Public retrofit budgeting cap | ≤NT$5,000/m² (absent 詳評 estimate) | per m² floor area | EY 2025‑11‑17 | E37 |
| Demolition and site clearing | NT$2,500/m² | per m² | 2025‑11 | E37 |
| 改善不具效益 (危老) | retrofit cost >½ rebuild cost | ratio | 2017 | E05 |
| Sea-sand rebuild trigger | retrofit + anticorrosion >50% of rebuild (incl. relocation and rent) | ratio | 2020 manual | E22 |

### I — Old-building stock data sources and district picture

| Source | Holder | Granularity | Age? | Structure? | Floors? | Geometry? | Latest period | Access | License / legal basis | What I observed, and how |
|---|---|---|---|---|---|---|---|---|---|---|
| 臺北市房屋概況 (data.gov.tw 132020) | 臺北市稅捐稽徵處 | District (12 分處) | <30 / ≥30 only | No | 9 floor bands | No | 115年度 (file updated 2026-08-24) | Open CSV | OGDL v1 | Downloaded 3 years. 12 rows each. SHA 113 `47656df3…`, 114 `39998cff…`, 115 `7b9dc2c5…`. Sums match the 主計處 棟 series. |
| 臺北市現有營造建築物棟數 (132950, tsis a05019201) | 主計處 | City | <30 / ≥30 from 96年 | No | 9 bands | No | 114年 | Open CSV | OGDL v1 | Downloaded 65年–114年 (50 rows). SHA `8f471e3d…`. 114年: 222,459 bldgs, 202,224 ≥30y. |
| 臺北市房屋單位及面積 (132594) / 現有營造建築物總面積 (132595) | 主計處 | City | No | Yes (units/area by 構造) | No | No | annual | Open (tsis) | OGDL v1 | Catalog metadata only. |
| pip.moi.gov.tw E4040 T13/T15/T16 | MOI 不動產資訊平台 (from 房屋稅籍資料庫) | 鄉鎮市區 (Taipei 12 districts), quarterly | 10 bands | 6 classes | 5 bands | No | 115Q2 | Open CSV (GET; WAF cookies) | Not stated on site | Downloaded. 28,053 rows each. SHA T13 `0bbd31c4…`, T15 `cb5b3a86…`, T16 `a75ad896…`. Marginal tables only, no cross-tabs. |
| pip.moi.gov.tw E4040 村里 items | MOI | Village | No (household items only) | No | No | No | — | Open | Not stated | Listed on the page. No age, structure or floor table at village level. |
| 房屋稅課稅面積、坐落及起課年月 (109449) | 財政部財政資訊中心 | Record + 村里 | 起課年月 | No | No | No | ≤108 | Open CSV | OGDL v1 | Downloaded 417,874 rows. SHA `54c52e52…`. Only 51 Taipei rows, so not a Taipei inventory. |
| Other counties' 稅籍 屋齡 tables (169647 Taoyuan, 139713 Tainan, 174469 Miaoli, Keelung 房屋稅籍) | County tax offices | District | Yes | Some | Some | No | 2026 | Open | OGDL v1 | Catalog only. Shows the format Taipei does not publish. |
| NLSC 3D building model, Taipei I3S layers 0/30, 3D Tiles 0/30 | 內政部國土測繪中心 | Building (分棟 block) | No (MDATE = mapping date) | BUILD_STR mostly NA in sample | BUILD_NO, BUILD_H | 3D mesh + centroid | layer "114_A"; sample MDATE 202409 | Streaming free. Taipei physical files not supplied (→ 臺北市政府資訊局). Others: official letter, 機關及團體 only. | Platform ToS (non-transferable; attribution "內政部國土測繪中心"). No open license. | Read layer JSON and attribute PDF (SHA `ff12dc52…`). Decoded 4 attribute buffers of node 40 (643 bldgs). Statistics endpoint 404. |
| 臺灣通用電子地圖 BUILD layer | NLSC | Building block | No | No | No | 2D | 114年版 spec | WMS/WMTS open (17214/25108); files via e-shop | OGDL v1 for services | Read the 114 layer spec PDF (SHA `5b03c45c…`): ID/MDATE/SOURCE only. |
| 臺北市 1/1,000 地形圖 + 積木模型 | 臺北市政府都市發展局 | Building polygon | No | R/B/M/D material code | Roof height (model); floor annotations (inference from NLSC use of 樓層註記) | 2D/3D | 113年版 spec | Paid per sheet | 臺北市地形圖數值圖檔申請使用及收費辦法 §6 | Read the FAQ and 113 reading manual (SHA `40202c5e…`). |
| 建物標示部 (地政) | 地政事務所 / 地政局 | Building (建號) | 建築完成日期 | 主要建材 | 層數 | No (建物測量成果圖 separate) | live | Per-record paid 謄本 / API (NT$1 per record in KH) | 土地登記規則 §24-1 (anyone: 2nd class). Local 電子資料流通收費標準. | Read the law text and the KH fee standard PDF (SHA `9b7d11af…`). Taipei standard not found. |
| 房屋稅籍 (address-level) | 臺北市稅捐稽徵處 / FIA | Unit / address | 課稅年數 / 構造完成 | Yes | Yes | No | live | Restricted | 稅捐稽徵法 §33 ¶1 secrecy. ¶2 allows supply to agencies and researchers for statistics/research without names. | Read the law text on law.moj.gov.tw. |
| NCDR 500 m grid building statistics v1 | 國家災害防救科技中心 | 500 m grid | Seismic-design level (from 課稅年數) | Material | Height class (inference) | Grid | v1 (2016), v2 planned | Written request; agencies and academia only | NCDR not authorized to release records | Read the e-paper No. 129 PDF (SHA `67ae8b9d…`). |
| 使用執照摘要 (128203) / 套繪圖 (151936) | 建管處 | Permit / footprint | Permit date | Yes | Yes | Footprints (post-2001) | 2026 | Open | OGDL v1 | Previously verified (not re-tested). |
| img2.gov.taipei 建築影像管理系統 | 建管處 | Permit image | (unobserved) | — | — | — | — | Guest auto-login web app | Unknown | Observed only the JS shell and login handler. **Not observed.** |
| TELES / TERIA (NCREE/NCDR) inventories | NCREE / NCDR | (snippet: general building stock) | — | — | — | — | — | Unknown | — | **Unverified lead.** Search snippets only. |
| GEM East Asia exposure; GFZ exposure-taiwan | GEM / GFZ | Admin-1 open; finer by license | — | — | — | — | v2023.1 | — | — | **Unverified lead.** GFZ issue #6 read: no published output. |

District picture from open data (buildings: Revenue Service 115年度, all uses; units: MOI 115Q2 residential distinct addresses; the two unit systems cannot be divided into a per-building ratio; MOI tables are marginal, not cross-tabulated; "brick-type" = 磚木石造 + 加強磚造 unit share):

| District | Bldgs (115) | Bldgs ≥30y | % ≥30y | Bldgs ≤5F | Res. units 115Q2 | Avg age | Units >30y | % >30y | % >40y | % >50y | % brick-type units* | % 1–5F units | Units >25y (pre-1999 upper bound) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 松山 | 13,239 | 12,607 | 95.2 | 9,240 | 66,591 | 42.2 | 54,686 | 82.1 | 66.0 | 30.2 | 7.3 | 40.7 | 56,829 |
| 信義 | 18,266 | 17,299 | 94.7 | 14,627 | 78,671 | 40.9 | 63,134 | 80.3 | 63.5 | 26.4 | 8.1 | 54.5 | 66,970 |
| 大安 | 17,889 | 16,557 | 92.6 | 12,154 | 98,571 | 42.1 | 82,650 | 83.8 | 67.7 | 23.6 | 8.1 | 34.0 | 85,476 |
| 中山 | 18,116 | 16,477 | 91.0 | 13,420 | 97,215 | 38.7 | 67,990 | 69.9 | 56.5 | 20.7 | 10.6 | 34.1 | 75,586 |
| 中正 | 14,818 | 13,678 | 92.3 | 10,819 | 53,302 | 40.5 | 38,382 | 72.0 | 58.8 | 31.9 | 13.3 | 43.5 | 40,855 |
| 大同 | 13,636 | 12,926 | 94.8 | 11,827 | 46,788 | 41.1 | 33,350 | 71.3 | 60.5 | 34.8 | 19.0 | 50.8 | 35,035 |
| 萬華 | 24,674 | 23,848 | 96.7 | 20,014 | 71,891 | 42.8 | 57,169 | 79.5 | 67.9 | 36.9 | 17.7 | 54.8 | 59,368 |
| 文山 | 20,484 | 18,512 | 90.4 | 17,814 | 95,530 | 36.2 | 63,104 | 66.1 | 48.5 | 16.1 | 8.0 | 53.7 | 74,150 |
| 南港 | 10,037 | 9,098 | 90.6 | 8,733 | 41,435 | 35.2 | 25,162 | 60.7 | 52.9 | 20.8 | 8.3 | 54.6 | 28,460 |
| 內湖 | 19,099 | 16,064 | 84.1 | 15,457 | 93,083 | 34.3 | 61,387 | 65.9 | 43.7 | 2.4 | 1.6 | 53.9 | 71,808 |
| 士林 | 28,116 | 25,239 | 89.8 | 25,496 | 92,777 | 42.6 | 76,263 | 82.2 | 70.4 | 27.4 | 17.1 | 66.7 | 80,265 |
| 北投 | 21,880 | 19,337 | 88.4 | 20,325 | 86,097 | 39.0 | 63,282 | 73.5 | 59.6 | 23.0 | 13.9 | 62.6 | 67,738 |
| **Taipei** | 220,254 | 201,642 | 91.5 | 179,926 | 921,951 | 39.6 | 686,559 | 74.5 | 59.6 | 23.4 | 10.7 | 50.2 | 742,540 |

Snapshot hashes (prefix): Revenue Service 113/114/115 `47656df3…`/`39998cff…`/`7b9dc2c5…`; MOI T13/T15/T16 `0bbd31c4…`/`cb5b3a86…`/`a75ad896…`. Source URLs: [臺北市房屋概況 132020](https://data.gov.tw/dataset/132020); [MOI 不動產資訊平台 download area](https://pip.moi.gov.tw/Publicize/Info/E4040) (no explicit license stated); [稅捐稽徵法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340001) §33; [土地登記規則](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0060003) §24-1; [NLSC 3D maps](https://3dmaps.nlsc.gov.tw/); NCDR e-paper No.129 (2016-04) on the 500 m grid.

### X — Prioritization precedents and screening accuracy

| Jurisdiction / program | Decision unit / who decides | Screening inputs | Missing-data rule | Tiers / weights | Outcomes (numbers, dates) | Source |
|---|---|---|---|---|---|---|
| Taiwan national, 安家固園 (2016–21), then 全國建築物耐震安檢暨輔導重建補強計畫 (2019→2025) | Building (棟); owner opts in; local government subsidizes; MOI funds | Permit before 1999-12-31; preliminary assessment (初評) score form (quantitative revision 2016); later 危險度 R and 甲/乙 grades | Results confidential; no default rule; no register of stock (CY) | First two years: condominiums and soft-story buildings first; otherwise local priority by age, area or geology | 2016: 6,031–6,467 received vs 83,000 planned (7.3–7.8%). Cumulative 17,277 by Dec 2024. Soft-story strengthening: 194 applications | X01–X04, X24, X25 |
| Taiwan national 建照快篩 (2017–20) | Building permit file; local government commissions desk review of drawings | Pre-1999, RC, ≥12F (2017) → ≥9F (2018) → ≥6F (2019–20); about 36,000 permits | Results "不宜公開"; screen failure → owner notified to get 初評 | Storey-height bands as sequencing tiers | 11,337 to screen, 8,315 done; 2,191 pass vs 6,714 fail (≈1:3; source totals inconsistent); ≈0.5% of pre-1999 permits (CY, c. 2018) | X25 |
| Japan, 耐震改修促進法 (2013 amendment) | Building; owner must diagnose; administrative agency publishes results | Use × storeys × floor area (要緊急); pre-1981 + route-side + height vs road width (要安全) | Targets 耐震不明 buildings; orders to report, then publication | Categories I/II/III (collapse risk high / some / low) | 要緊急: 11,562 published, 93.7% resolved (2025-03-31). Route-side Art. 7(2)(3): about 7,300 published, about 4,100 insufficient, about 44% resolved (2024-03-31) | X12–X14 |
| Tokyo, 特定緊急輸送道路沿道建築物 ordinance | Building, aggregated to road section | Pre-1981, fronting specified emergency road, height ≥ about half road width; Is from mandatory diagnosis | Mandatory diagnosis (98.6% done); remaining 1.4% pursued by orders | Overall and section reach rates (Monte-Carlo); 50 priority sections (2026) | Overall reach 91.1% (2019-12) → 94.2% (2026-06); FY2025 target 99% missed; 58.9% of 4,829 meet seismic standard; about 2,000 unretrofitted; new targets 99% (FY2030), 100% (FY2035) | X13, X14b |
| Los Angeles soft-story (Ord. 183893 / 184081) | Building; city issues order to comply | Assessor + housing + building records (pre-1980 wood) → Google Maps online survey of 30,000 (6,000 "No", 24,000 "Possible") → site visits → 13,500 listed | Order binds the owner; owner proves prior retrofit | Priority I (16+ units) → II (3+ stories, <16 units) → III (by units, then condos/commercial); orders 2016–17 | 12,347 buildings; 95% plans, 89% permits, 76% completed at 2 / 3.5 / 7-year milestones (2024-02-01) | X05, X06, X06b |
| Los Angeles non-ductile concrete | Building | Concrete building submitted for plan check before 1977-01-13; owner checklist | Applies "whether … identified by LADBS or not" | 3 yr checklist / 10 yr plans / 25 yr completion | 1,194 active cases: 62% checklist, 12% plans, 6% construction complete (2024-02-01; later deadlines not yet due) | X07, X07b, X08 |
| San Francisco Mandatory Soft Story (2013) | Building; owner's engineer screens in or out | Type V, pre-1978, 5+ units, 2+ stories; tax-notice address list | Owner must screen; non-compliance → placard, NOV | Tiers I–IV by occupancy, units, commercial use, **liquefaction zone** | More than 5,000 required (75% of screened); more than 1,700 permits; more than 700 complete (page revised 2016-08-09) | X09, X10 |
| Berkeley SWOF (BMC 19.39) | Building | City inventory; Phase I engineer report; Phase II retrofit | No Phase I report → retrofit still required | Single tier (5+ units, pre-1978) | Of 369 listed: 293 retrofitted, 63 removed (17% over-inclusion), 13 pending or non-compliant (2026-07-23) | X11 |
| New Zealand EPB system (2017) and 2025 reform | Building; territorial authority identifies, owner's engineer assesses, register is public | Seismic risk area (high, medium, low); profile categories A/B/C; priority routes and thoroughfares chosen by community consultation | No assessment in 12 months → deemed earthquake-prone | Priority buildings get half the timeframes (high zone: identify 2.5 vs 5 yrs; remediate 7.5 vs 15 yrs) | More than 8,000 captured; about 1,500 remediated; 5,800 remaining; reform removes about 55% (2,900), about 80 need full retrofit; $8.2b savings claimed | X15–X19 |
| British Columbia school SMP | School block; ministry + district; Engineers and Geoscientists BC (EGBC) Seismic Retrofit Guidelines | Engineer applies SRG risk rating (H1–H3 = high) | Not applicable (public assets) | H1/H2/H3 | 498 projects: 233 completed, 247 future priorities (May 2026); reassessment returned some schools to the list | X22, X23 |
| Istanbul ISMEP (2006–) | Public building; IPCU / governorship | Not verified (lead) | Not applicable | Schools, hospitals, administrative buildings | 1,640 public buildings retrofitted or rebuilt by Feb 2025 | X21 |

| Study | Reference standard | Sample | Result (computed where marked) | Limits |
|---|---|---|---|---|
| FEMA P-155 (3rd ed., 2015) Ch. 10, AOC courthouse benchmark (X20) | Engineer drawing review plus ASCE/SEI 31-03 Tier 1/2 → risk level IVb/IV (acceptable) vs V/Vw/VI (unacceptable) | 49 California court buildings, mostly very high seismicity | Share sent to detailed evaluation, by true class (Level 1): IVb 43%, IV 73%, V 95%, Vw/VI 100%. **Computed:** missed unacceptable buildings: Level 1 1/31 (3%), Level 2 4/31 (13%), 2nd edition 6/31 (19%). Acceptable buildings flagged: Level 1 11/18 (61%), Level 2 7/18 (39%), 2nd edition 7/18 (39%). Overall share referred: 2nd ed 65%, L1 86%, L2 70%; experienced engineers 86% | Small, non-random sample; reference is engineering judgement, not observed damage; draft scores |
| Guzman Javier and Ichii, Kansai Univ. bulletin, Antakya 2023 (X27) | Observed damage after the 6 Feb 2023 earthquake (collapsed / heavy / slight) | 99 damaged buildings scored from pre-event Street View | All 99 scored 0.3–0.7 (56 at 0.3, 37 at 0.4, 2 at 0.5, 4 at 0.7; computed tally). Every one is below the 2.0 cut-off, including slightly damaged buildings. Mean scores differed significantly by damage level | University bulletin; damaged buildings only (no undamaged controls); exterior imagery only |
| Taiwan drawing-based 快篩 (X25) | None (no validation reported); screen output only | 8,315 screened | Fail : pass ≈ 3 : 1 (6,714 vs 2,191) | No comparison with 初評 or 詳評; counts internally inconsistent |
| Taiwan 初評 quality audits (X24, X01) | NLMA checks of submitted assessments | Not stated | Error-type shares among detected errors: inputs inconsistent with drawings 34%; structure and use coefficients not truthfully entered 29%; 2016 form revision justified by "評估人員主觀認定所造成的誤差" | Shares of errors, not error rates; no denominator |
| NZ EPB review (X17) | Policy review | National | "Inconsistency across engineering assessments"; engineers err conservative and councils rarely challenge; 39% of a 2,565-building sample outside the profile categories (figure shows 47%) | Qualitative; internal inconsistency between text and figure |
| LA soft-story funnel (X06b, X05) | Site visit | 30,000 → 24,000 "Possible" → 13,500 listed → 12,347 in 2024 status | **Computed:** desk screen "Possible" confirmed at about 56% by site visit; about 8.5% further attrition between list and 2024 status (reason not stated) | Undated deck; attrition causes inferred |

Unverified leads: 2025 Kahramanmaraş 1,015-building sidewalk-survey comparison; Sucuoğlu et al. 2007 Düzce street-survey calibration; Bingöl 2003 FEMA P-154 over-estimation; Tainan post-0206 soft-storey screening counts; ISMEP ranking method; Italy Sismabonus uptake; NZ amendment bill passage.

### Source ledger — deep investigation (retrieved 2026-10-14)

P: current selection rules and baseline.

| ID | Exact URL | Publisher | Doc date / period | How read (2026-10-14) | Limitations / licensing |
|---|---|---|---|---|---|
| P01 | https://laws.gov.taipei/law/LawSearch/LawPrint/FL083873?type=0 | 臺北市政府 (都發局) law system | Amended 2017-12-12 | curl HTML → full text, points 1–15 | Current force unclear; may be dormant |
| P02 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/0f3092a5-106a-4ce1-87b5-aefc03e9900f.pdf | MOI rule hosted by Taipei CMO | Effective 2022-05-12 | curl + pdftotext; points 1–18 and annex 1–2 | Later amendments (if any) not checked |
| P03 | https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg028196/ch02/type2/gov10/num1/Eg.pdf | 行政院公報 (MOI order 台內營字第1110817457號) | 2022-10-17 | curl + pdftotext; grep of points 2, 5, 8, 9 | Confirms P02 wording only |
| P04 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/285f873b-8e11-4d9b-87f5-d88060808044.pdf | Taipei CMO | Undated form | Full (1 page) | Blank template |
| P05 | https://www.nlma.gov.tw/filesys/file/EMMA/t1111208.pdf | MOI / Executive Yuan | Plan 111–114; MOI letter 2022-12-08 | pdftotext; targets (pp. 5–8), 108–110 review and Table 2 (pp. 9–13), work items (pp. 14–25) | National only; no city breakdown |
| P06 | https://www.nlma.gov.tw/uploads/files/69a12533822cae3fdda26360c533dc32.pdf | MOI | Plan 108–110 (revised 2020-04) | pdftotext; 安家固園 review, quick-screen sections | National only |
| P07 | https://www.nlma.gov.tw/uploads/files/c6690e7a6073db208b5b9d08dd874dbc.pdf | MOI 營建署 | 2015-07-09 plan | pdftotext; pp. 1–5 | Public-building statistics as of 2015-05 |
| P08 | https://www.nlma.gov.tw/uploads/files/2e9e5a86ec96f414d5fab9e2a0492fc0.pdf | MOI 營建署 press | 2016-05-06 | Full | Press release |
| P09 | https://www.nlma.gov.tw/uploads/files/6f751fa7fa8f02f6431ff1cd22e10f6a.pdf | MOI 營建署 press | 2016-09-08 | Full | Says results are not disclosed |
| P10 | https://www.nlma.gov.tw/uploads/files/482d647324b93037a5e97e42b335fed0.pdf | MOI 營建署 press | 2017-01-18 | Full (6,031 national initial applications to 2016-12-19) | National |
| P11 | https://www.nlma.gov.tw/uploads/files/13718f92e0f9d87a1342e008d2e99210.pdf | MOI 營建署 press | 2020-01-09 | Full | Old cap NT$2.2M, superseded by P02 |
| P12 | https://cybsbox.cy.gov.tw/CYBSBoxSSL/edoc/download/18425 | 監察院 (Control Yuan) investigation report | 2015 (data to 2015-01-13) | curl; Word file converted by textutil; full opinions | Public buildings only |
| P13 | https://uract.nlma.gov.tw/uploads/rule/B3101155-11208.pdf (also B31011071115500000.pdf, 2018 version) | 臺北市都發局 rule (promoter fees) | 2023-07-10 / 2018-11-01 | pdftotext; points 1–8 | Fees are for promoters, not owners |
| P14 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/917dedd0-c6ce-4c82-bddd-c1058d56ec6c.pdf | 臺北市都發局 | Amended 2026-02-03, effective 2026-03-03 | pdftotext; points 1–8, annex 1–2 | Point 4(5) quick-screen clause in 2023 text (P13) absent from 2026 text |
| P15 | https://cmo.gov.taipei/cp.aspx?n=023341AF71C3812D | 臺北市建築管理工程處 | Page updated 2026-10-13 | WebFetch summary of page and link list | Statistics not on page |
| P16 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/10d1e425-3d24-4801-9d68-38a6781007a1.pdf | Taipei CMO 危老問答集 vol. D | 2026-01 edition | pdftotext; Q1–Q17 | FAQ, not a legal instrument |
| P17 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/b778ea0d-7c2a-4862-884c-c441480a96ff.pdf | Taipei CMO | 2023-07-21 flowchart | Full | — |
| P18 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/963fe644-fca5-4144-8b16-8baa9876b40d.pdf | 臺北市都發局 (preface) | 2024 | Full (1 page) | Single figure, 2,140 |
| P19 | https://laws.gov.taipei/law/LawSearch/LawPrint/FL080447?type=0 | 臺北市政府 | Amended 2020-04-09 | curl HTML → full text, Arts. 1–19 | — |
| P20 | https://udd.gov.taipei/assets/tTRGRuP4dgZLeNz9yqUKyT/attachs/公辦都更2.0專案計畫.pdf | 臺北市政府 (都更處) | 2020-08 | pdftotext; full | Possibly superseded by 7599 (lead) |
| P21 | https://www-ws.gov.taipei/001/Upload/459/relfile/63555/9130790/b80ec8be-44cb-4a77-8084-9021a74fb4ce.pdf | 臺北市政府 | Revision of 2026-04-29 | pdftotext; sections 1–9 and annex 2 | No intake counts |
| P22 | https://udd.gov.taipei/assets/2bXtYvsrHEvUavHK86o9Py/attachs/防災都更專案細部計畫書.pdf | 臺北市政府 | Public exhibition 2023-11-06 | pdftotext; pp. 1–15 | Draft version |
| P23 | https://udd.gov.taipei/cms/assets/nYhkzE7gQZZbp9AF6Mgad7/attachs/細部計畫書.pdf | 臺北市政府 | Adopted 2024-03-28 | pdftotext; header and applicability grep | Later revision (2024-11 exhibition) not read |
| P24 | https://udd.gov.taipei/assets/38-12552/Documents/信義市場公辦都更說明會會議紀錄(定稿).pdf | 臺北市都發局 | Meeting 2020-02-16 | pdftotext; pp. 1–3 | Resident statements anonymised; no names copied |
| P25 | https://twur.nlma.gov.tw/resources/website/activity_extra/assist/78/course_78_B_20141229171359_1205 03臺北市推動防災型都市更新先期規劃.pdf | 臺北市都發局 slides (NLMA site) | 2014-12-05 | pdftotext; slides 1–15 | Slides, study stage |
| P26 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/d962c5cf-49e8-4c74-ac04-f44b9024c384.pdf | 臺北市政府 (CMO) | 2025-01-14 | Full | Uptake numbers not given |
| P27 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/064c57e8-7e31-4e33-9a8a-7da19c82e95f.pdf | Taipei CMO | Version 2026-07-20 | Full | Contains addresses (public list); not copied here |
| P28 | https://cybsbox.cy.gov.tw/CYBSBoxSSL/edoc/download/71107 | 監察院 | 2025-08-19 | pdftotext; full (12 slides) | Briefing slides, not the full report |
| P29 | https://www.nlma.gov.tw/uploads/files/7575bfefdd33324c2f5067d7b06047a1.pdf | 內政部國土管理署 | 2026-03 | pdftotext; pp. 3–8 (figures 1–8) | 2025 data to 11-30 only |
| P30 | https://www.nlma.gov.tw/uploads/files/a5d37b464dc02a5814200514847f5c1a.pdf | Executive Yuan letter + MOI plan + subsidy regulation | 2026-03-16 | pdftotext; pp. 1–25 and regulation Arts. 1–10 | Taipei allocation not given |
| P31 | https://www.nlma.gov.tw/uploads/files/0133aba789e1dbea0143a8c892d6ad13.pdf | Executive Yuan / MOI | Approved 2025-11-17 | pdftotext; pp. 1–3 | Central agencies only from 2026 |
| P32 | https://www.nlma.gov.tw/uploads/files/da01290e455f1b9dd70d9207dc2d98b6.pdf | 國土管理署 0403 FAQ | Updated 2024-08-01 | pdftotext; Q1–Q10 | Hualien-focused |
| P33 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070249 | 全國法規資料庫 (危老條例) | Amended 2023-12-06 | WebFetch (model summary with quotes) | Fetched through a summariser |
| P34 | https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=D0070109&flno=77-1 | 全國法規資料庫 (建築法) | Current | WebFetch | Amendment date not shown |
| P35 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070259 | 全國法規資料庫 (結構安全性能評估辦法) | Amended 2018-10-11 | WebFetch | Grade thresholds sit in annex 5, not retrieved |
| P36 | https://udd.gov.taipei/assets/6XpT6F2kpmnVhD9Bps9z57/attachs/(建管處)20539-90-09(營)臺北市海砂屋列管案件.pdf | 都發局 statistics metadata | Undated | Full | Metadata only |
| P37 | https://twur.nlma.gov.tw/resources/website/download_file/58/臺北市政府受理危老作業規定及案例說明(北區場).pdf | Taipei CMO slides | 2021-10 | pdftotext; grep for counts | Slide deck |
| P38 | https://laws.gov.taipei/law/LawSearch/LawPrint/FL029161?type=0 | 臺北市都發局 | Amended 2013-02-05 | Full | Advisory group: 21 members, chaired by CMO head |
| P39 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/d8983681-d6d2-46c5-bc70-00d223b726fc.pdf | Taipei CMO | Undated | Full | Eligibility review form |

P leads (news/snippets, not evidence): Hualien weak-storey approvals (newtalk 2026-05-08); first 575 contract in Neihu (2026-06-29 news); 2023 "7599" plan; 住都中心 implementer case counts; 913 commercial-zone ≥11F ≥30-year buildings in façade reporting; 891 Taipei 危老 approvals by 2023-11 (thesis snippet).

E: professional assessment and retrofit practice.

| ID | Exact URL | Publisher | Doc date | Read (sections, method) | Limitations / licence |
|---|---|---|---|---|---|
| E01 | https://uract.nlma.gov.tw/uploads/rule/A2001107106700000.pdf | MOI (NLMA) | amended 2018‑10‑11 | Full text arts 1–15 + 附表一–五; curl+pdftotext | Gov text; tables reproduced as text (formula glyphs partly lost) |
| E02 | https://law.moj.gov.tw/LawClass/LawAll.aspx?PCODE=D0070259 ; 附表五 https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000224311&lan=C ; 附表一 FileId=0000224307 | MOJ 全國法規資料庫 | 2018‑10‑11 | Page (WebFetch) + 附表 PDFs | Confirms no later amendment as of today |
| E03 | https://www.laws.taipei.gov.tw/law/File/0000368238 | Taipei City (law site) | PDF 2018‑08, mod 2024‑05 | Report template incl. grade table and forms | Template, not regulation |
| E04 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070249 | MOJ | 2023‑12‑06 | Arts 1–4, 11–13 via curl | — |
| E05 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070256 | MOJ | 2017‑08‑01 | Arts 3–5 | — |
| E06 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070257 | MOJ | 2019‑06‑13 | Full text | — |
| E07 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070298 | MOJ | 2021‑11‑17 | Full text | — |
| E08 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/0f3092a5-106a-4ce1-87b5-aefc03e9900f.pdf | MOI directive, Taipei-hosted copy | PDF 2022‑10 (Plan C revision 2022‑10‑17 per NCREE) | Points 1–18, annexes 6–7 | Copy, not the NLMA original; later amendments not checked in an original |
| E09 | https://privatebuilding.ncree.org.tw/ (pages /reinforcement-detail/, /qa/, /subsidy/funding/, /403花蓮地震紅黃單耐震弱層補強專區/, /20260729/5979/, /20260731/6000/, /20260803/6012/) | NCREE for NLMA | live 2026 | Case list, Q&A, subsidy, Hualien rules, news; curl HTML→text | Case costs not published; site summaries of rules |
| E10 | https://www.nlma.gov.tw/uploads/files/fad01d45d04bd16822606e6d8895d460.pdf | 營建署 (lecture, 陳啓中) | 2018‑05‑18 | Full deck (快篩 items, rule, cases, high-risk definition) | Training slides, not regulation |
| E11 | https://www.nlma.gov.tw/uploads/files/83e451405695cdb892d58aae96d135e2.pdf | 營建署 | 2018‑05 | Training plan | Context only |
| E12 | https://www.nlma.gov.tw/uploads/files/bb3513524dfc5cef717bccfde6c41666.pdf ; https://www.nlma.gov.tw/uploads/files/3e9731d5bcdad87b10981a42603971e8.pdf | 營建署 lectures (宋裕祺, NTUT) | 2017‑09 | PSERCB inputs, default parameters, site class, R bands, exclusions | Training slides |
| E13 | https://www.nlma.gov.tw/uploads/files/b281114fab8b27087547bac8a04f93ad.odt ; https://www.nlma.gov.tw/uploads/files/2a89a6be91329feda02345ff58c77d83.odt | NLMA | undated (current forms) | E1‑6‑1/6‑2 detailed-evaluation report forms; unzip content.xml | Forms, not guidance; TEASPA ≤6F note conflicts with E35 |
| E14 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/14f80ddb-58ff-4457-bd7b-2fda7a6ecd54.pdf | Taipei City (list of bodies' fee methods) | PDF 2026‑03‑09 | Full | Lists each body's filed schedule; not the NLMA contract itself |
| E15 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/f8030fa8-2e94-4a64-bd5f-4a562e7e0d90.pdf | Taipei City | PDF 2026‑03‑09 | Full | Same |
| E16 | https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=D0070116 (+ LawAll) | MOJ | latest 2023‑05‑10 | Amendment history 1–20; art. 41‑1, 42 | History lists articles, not content |
| E17 | https://mend.nccu.edu.tw/upload/60/doc/3520/建築物實施耐震能力評估及補強方案（公有建築物）106.pdf | EY program (copy hosted by NCCU) | 2017‑12‑28 | Full | Third-party mirror of EY text |
| E18 | https://www.nlma.gov.tw/uploads/files/69a12533822cae3fdda26360c533dc32.pdf | MOI | 2020‑04 (EY 2020‑04‑07) | Background, stock counts, public stats, 快篩 stats | — |
| E19 | https://www.nlma.gov.tw/filesys/file/EMMA/t1111208.pdf | MOI | 2022‑12‑08 | Execution table to 2021‑09 | — |
| E20 | https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/6cbc7f7c-3fbe-4d99-aaa1-80223fa34033 | EY | 2019‑05‑27 | WebFetch summary | Model-summarised page |
| E21 | https://www.rdec.taichung.gov.tw/media/1045328/1130417-5-市政府推動民國88年前舊有建築物耐震評估及加速都市更新-危老建築物重建-災害應變作為-公共建設及道路橋梁等建物巡檢-災後修復補助專案報告-都發-建設.pdf | Taichung City | 2024‑04‑17 | §參 | Taichung, not Taipei |
| E22 | https://www.laws.taipei.gov.tw/Law/File/0000368211 ; https://www.laws.taipei.gov.tw/Law/File/0000368212 | Taipei City | PDFs 2017‑08 / 2020‑01 | Ch. 1–5, 7 | Two versions differ on the 0.3–0.6 band |
| E23 | https://www.treca.org.tw/component/k2/download/25139_f25eaa89243138f8c4d9f615e814e3c3.html | MOEA announcement (TRECA-hosted copy) | 2025‑12‑19 | Full 1 page | Third-party host; BSMI original not fetched |
| E24 | https://udd.gov.taipei/assets/2bXtYvsrHEvUavHK86o9Py/attachs/防災型都更專案細部計畫書.pdf | Taipei City | 2023‑11‑06 | §參 (age table, chloride, ID) | Exhibition draft |
| E25 | https://www.ncree.niar.org.tw/accomplishment/technicalreports/page/12203 → https://www.ncree.org/GetFile.ashx?id=10008534 | NCREE (NCREE‑2024‑006) | 2024‑11‑08 | §4.1.2, 4.4–4.6 | Surveyed sample, not census |
| E26 | https://orgws.kcg.gov.tw/001/KcgOrgUploadFiles/408/relfile/74090/215157/f4c993e9-1f53-4ba1-9f89-43d873c809ab.pdf | NCDR + NCREE | 2016‑03 | §2.1, 3.1, conclusions | Kaohsiung-hosted copy; preliminary |
| E27 | https://peer.berkeley.edu/sites/default/files/reconnaissance_taiwan_20160206.pdf | NCKU (杜怡萱), via PEER | 2016‑02‑07 | Collapsed-building slides | Academic, one day after the event |
| E28 | https://peer.berkeley.edu/sites/default/files/ncree_20160206_v5.0.pdf | NCREE slides via PEER | 2016‑02 | TELES estimates, site list | Preliminary |
| E29 | https://www.nlma.gov.tw/uploads/files/b25839408aa615bd481d1e81885ac48b.pdf | 營建署 news release | 2017‑01‑18 | Full | — |
| E30 | https://www.ey.gov.tw/Page/9277F759E41CCD91/73230eb1-6211-41d5-8d24-473f769bc6f3 | EY | 2016‑03‑14 | WebFetch summary | Model-summarised |
| E31 | https://data.gov.tw/en/datasets/28708 | MOEA / CGS | updated 2026‑09‑22 | Metadata | OGDL v1.0 |
| E32 | https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/e45b89be-426c-4c8a-b082-7d0297f97bd5.pdf | Taipei City | 2016‑03 | Full form | — |
| E33 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070149 | MOJ | 2022‑12‑28 | Arts 3–10 | — |
| E34 | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070150 | MOJ | 2022‑12‑28 | Art. 25‑1 | — |
| E35 | https://teaspa.ncree.org.tw/ | NCREE / CECI | live (V5.1.1 2025‑08‑05) | WebFetch summary | Model-summarised |
| E36 | https://www.ncree.niar.org.tw/accomplishment/technicalreports/page/12210 → https://www.ncree.org/GetFile.ashx?id=10008558 | NCREE (NCREE‑25‑003) | 2025‑04‑01 | §1.1.2–1.1.3, Table 1‑1 | 301 pp; only ch. 1 read |
| E37 | https://www.nlma.gov.tw/uploads/files/0133aba789e1dbea0143a8c892d6ad13.pdf | EY approval + MOI plan | 2025‑11‑17 | §經費計算原則 | Public buildings |
| E38 | https://www.nlma.gov.tw/uploads/files/a5d37b464dc02a5814200514847f5c1a.pdf | EY approval + MOI plan and rules | 2026‑03‑16 | Plan pp. 8–21; rules arts 1–7 | — |
| E39 | https://www.uro.ntpc.gov.tw/Uploads/PageServiceFileGroup/2024-05/e207cfe0-91c2-460a-b053-ae84a3ff2497.pdf | New Taipei City | 2024‑05 | Full Q&A | NTPC rules |
| E40 | https://www.ey.gov.tw/Page/9277F759E41CCD91/68379aab-7359-4ab2-8e3c-bc32a24a140b | EY | 2024‑06‑22 | WebFetch summary | No counts |
| E41 | https://www.cna.com.tw/news/aipl/202609210030.aspx | CNA (news) | 2026‑09‑21 | WebFetch summary | Secondary |

X: precedents.

| ID | Exact URL | Publisher | Doc date | Sections read / method | Limitations |
|---|---|---|---|---|---|
| X01 | https://www.nlma.gov.tw/uploads/files/25a779075284513d2c0e13df93119af9.pdf | MOI (CPAMI) | 2016-08-11 | Full press release with revised 初評 form; curl + pdftotext | Press release |
| X02 | https://www.nlma.gov.tw/uploads/files/482d647324b93037a5e97e42b335fed0.pdf | CPAMI | 2017-01-18 | Full; 6,031 received; disclosure fear | Excerpt pages of a compilation |
| X03 | https://www.nlma.gov.tw/uploads/files/2e9e5a86ec96f414d5fab9e2a0492fc0.pdf | CPAMI | 2016-05-06 | Full; priority order (condominiums, soft-story first) | — |
| X04 | https://www.nlma.gov.tw/uploads/files/6f751fa7fa8f02f6431ff1cd22e10f6a.pdf | CPAMI | 2016-09-08 | Full; results not disclosed | — |
| X04b | https://www.nlma.gov.tw/uploads/files/dc092db14a63e115249272c762df77e7.pdf ; https://www.nlma.gov.tw/uploads/files/09e5790281b9e2e69c8d60b1e1e45f24.pdf ; https://www.nlma.gov.tw/uploads/files/5fa35834e7069feeb747d7d8ae7a898b.pdf | MOI / CPAMI | 2016-07-06; 2016-03-18; 2017-01-18 | Full; budget NT$1.3155b, 500 pilot cases to six southern counties | — |
| X05 | https://web.archive.org/web/20250403125142/https://dbs.lacity.gov/sites/default/files/styles/medium/public/soft-story-compliance-report.pdf | LADBS | Status as of 2024-02-01 | Citywide chart (p.1); Wayback copy because the live site returned 403 | Archived copy; no later status found |
| X06 | https://web.archive.org/web/2025/https://dbs.lacity.gov/services/specialized-services/mandatory-retrofit-programs/soft-story-retrofit-program | LADBS | 2025 snapshot | Scope, priority table, timelines | Archived |
| X06b | https://cdn-web.iccsafe.org/wp-content/uploads/01-Ray-Chan.pdf | LADBS (ICC-hosted deck) | Undated (about 2015) | Inventory steps, counts | Undated slides |
| X07 | https://web.archive.org/web/2025/https://dbs.lacity.gov/services/specialized-services/mandatory-retrofit-programs/non-ductile-concrete-retrofit-program | LADBS | 2025 snapshot | Scope, timelines, "identified or not" clause | Archived; NDC ordinance number not verified |
| X07b | https://web.archive.org/web/20260411125621/https://dbs.lacity.gov/sites/default/files/efs/pdf/publications/retrofit/non-ductile-compliance-report.pdf | LADBS | Status as of 2024-02-01 | Chart | Archived |
| X08 | https://www.iitk.ac.in/nicee/wcee/article/WCEE2012_3129.pdf ; https://iitk.ac.in/nicee/wcee/article/14_07-0072.PDF | Comerio and Anagnos (15WCEE 2012); Anagnos et al. (14WCEE 2008) | 2012; 2008 | Intro, inventory method, data-source limits | Research inventory, not the enforcement list |
| X09 | https://sfgov.org/esip/soft-story | City and County of San Francisco (ESIP) | Revised 2016-08-09 | Full page via WebFetch | Dated; no current completion figures found |
| X10 | https://www.nist.gov/node/1841271 | NIST (Zhang, Fung, Johnson, Sattar), 12NCEE | 2022 | Abstract only | Full paper not read |
| X11 | https://berkeleyca.gov/sites/default/files/documents/2024-03-25%20Soft%20Story%20Inventory%20for%20WEB.pdf (status 7/23/2026) and https://berkeleyca.gov/construction-development/seismic-safety/mandatory-earthquake-retrofit-programs | City of Berkeley | 2026-07-23 | Status key and counts; program page | Count categories partly overlapping |
| X12 | https://www.mlit.go.jp/jutakukentiku/build/content/001466564.pdf | MLIT | Law as amended (2013, 2019 order) | Overview and mandatory-diagnosis thresholds | Summary slides |
| X13 | https://www.taishin.metro.tokyo.lg.jp/assets/pdf/tokyo/r8_sokushinkeikaku_2.pdf | Tokyo Metropolitan Government | 2026-03 | Ch. 3-1 (targets, reach-rate method), 4-1 (status, issues, survey), appendix (law Art. 7; national basic policy status text) | 159 pp.; survey chart series not fully parsed |
| X13b | https://www.taishin.metro.tokyo.lg.jp/assets/pdf/tokyo/r8_sokushinkeikaku_1.pdf | TMG | 2026-03 | Plan summary (3 pp.) | — |
| X14 | https://www.mlit.go.jp/jutakukentiku/house/content/001845218.pdf | MLIT | As of 2025-03-31 | Full table by prefecture | — |
| X14b | https://www.metro.tokyo.lg.jp/information/press/2026/07/2026072911 | TMG | 2026-07-29 | WebFetch; overall reach-rate series to 2026-06 | Maps not read |
| X15 | https://www.nzsee.org.nz/wp-content/uploads/2025/09/NZSEE-Overview-of-Government-EPB-Policy-Announcement_v1.pdf | NZ Society for Earthquake Engineering | 2025-09 | Full | Professional-body summary |
| X16 | https://web.archive.org/web/2026/https://www.mbie.govt.nz/dmsdocument/31201-focusing-the-earthquake-prone-building-system-proactiverelease-pdf | MBIE / Minister for Building and Construction (Cabinet paper) | 2025-09 (released 2025-09-29) | Exec summary, paras 11–37, Table 1 | Proactive release, some redaction; live site bot-blocked |
| X17 | https://www.beehive.govt.nz/sites/default/files/2025-09/Report%20of%20Seismic%20Risk%20Management%20Review.pdf | MBIE | 2025-06 | Paras 26–29, 63–64, 96–116 | Text vs Figure 8 inconsistent (39% vs 47%) |
| X18 | https://www.building.govt.nz/assets/Uploads/managing-buildings/earthquake-prone-buildings/epb-priority-buildings.pdf | MBIE | About 2017–18 | Full | Pre-reform |
| X19 | https://www.building.govt.nz/assets/Uploads/managing-buildings/earthquake-prone-buildings/assess-earthquake-prone-buildings.pdf | MBIE | About 2017–18 | Section on missing assessments | Legislation page itself returned 403 |
| X20 | https://www.fema.gov/sites/default/files/2020-07/fema_earthquakes_rapid-visual-screening-of-buildings-for-potential-seismic-hazards-supporting-documentation-third-edition-fema-p-155.pdf (read via Wayback 2024 copy) | FEMA / ATC | 2015-01 | Ch. 10.2 (Tables 10-2, 10-3; conclusions) | See (c) |
| X21 | https://ipkb.gov.tr/wp-content/uploads/2025/03/ISMEP-2025-EN-1.pdf | Istanbul Project Coordination Unit | 2025-02 | Component B summary | Activity report; no ranking method |
| X22 | https://web.archive.org/web/2025/https://www2.gov.bc.ca/gov/content/education-training/k-12/administration/capital/seismic-mitigation | BC Ministry of Education and Child Care | 2025 snapshot | Assessment method, SRG3 reassessment | Archived |
| X23 | https://www2.gov.bc.ca/assets/gov/education/administration/resource-management/capital-planning/seismic-mitigation/smp_progress_report.pdf | BC Ministry | 2026-05 | Summary page | — |
| X24 | https://twur.nlma.gov.tw/resources/website/download_file/98/113年度PSERCB教育訓練_國土管理署政令宣導.pdf | National Land Management Agency (MOI) | 2025-01-23 | Full deck: plan, subsidies, 17,277 初評, 194 strengthening applications, disclosure FAQ, error-type shares | Chart labels garbled in extraction; county numbers read from map callouts |
| X25 | https://cybsbox.cy.gov.tw/CYBSBoxSSL/edoc/download/44032 | Control Yuan (調查意見, 107內調0082) | About late 2018 | Sections 一, 二 (rapid screening, data gaps), 安家固園 status | Totals for pass/fail inconsistent (2,191 + 6,714 ≠ 8,315) |
| X26 | https://cybsbox.cy.gov.tw/CYBSBoxSSL/edoc/download/44033 | Control Yuan | 2021-05-12 (closed 2020-07-21) | Full (1 page) | Summary only |
| X27 | https://wwwtest.kansai-u.ac.jp/Fc_ss/center/study/pdf/bulletin015/bulletin015_breaking_6.pdf | Kansai University (社会安全学研究 vol. 15) | About 2024–25 | Summary, method, data table, conclusions | Bulletin paper; damaged buildings only |
| X28 | https://par.nsf.gov/servlets/purl/10094998 | Rufat, Tate, Emrich, Antolini, *Annals AAG* | 2019 | Abstract, Table 7 and discussion | Flood hazard, not seismic |
| X29 | https://collaborate.princeton.edu/en/publications/social-vulnerability-indices-a-comparative-assessment-using-uncer/ | Tate, *Natural Hazards* 63(2):325–347 | 2012 | Abstract only (WebFetch summary) | Full text not read |
| X30 | https://www.lavoripubblici.it/documenti2020/lvpb4/dm-28.02.2017-58-coordinato.pdf | MIT Italy (DM 58/2017, consolidated) | 2017, amended 2020 | Decree articles (Allegato A not included) | Risk-class method and uptake unverified |

### Reusable source ledger (2026-10-13)

All dates below are retrieval dates **2026-10-13**, unless a publication/observation period is stated. HTML was opened with the web tool or fetched using curl and parsed locally; PDF text used `pdftotext -layout`. The exact original URLs and inspected sections below identify the observations; temporary downloads and retrieval helpers are retired after integration. Public access is not blanket redistribution permission.

| ID / original publisher and exact material | Inspected scope, period/unit and method | Access, licensing and limitations |
| --- | --- | --- |
| **S01** Campaign organizer, [市政 debug松](https://puma.taipei/hackathon#issue-6) | curl HTML, issue 6 and rules; current event framing and real/simulated disclosure | Readable; per-source terms required. Civic age forecasts and model usefulness are organizer assertions, not independently corroborated. No event participation implied. |
| **S02** Taipei Construction Management Office (CMO), [建物耐震評估](https://cmo.gov.taipei/cp.aspx?n=53F406AE758E3270) | HTML business explanation, application forms and listed professional pathways; displayed update 2026-09-17; building/棟 or 幢 | Public procedure under S14 CMO declaration; not an assessed-building inventory or uptake study. Lists mandatory assessment and proactive assistance as different routes. |
| **S03** CMO, [initial-assessment/subsidy flow, revised 2023-07-21](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/b778ea0d-7c2a-4862-884c-c441480a96ff.pdf) | Entire one-page PDF, extracted text and rendered visual inspection; A3/A1/B1/B2/A4/A5 stages, professional result branches | curl succeeded after web fetch instability. S14 scope subject to exceptions. Consent for assessment is distinct from all-owner consent for the illustrated rebuilding route. |
| **S04** CMO, [D耐震評估篇, January 2026 edition](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/10d1e425-3d24-4801-9d68-38a6781007a1.pdf) | PDF questions 3–12, 17, 19, 27; printed D86–D90/D93–D94/D99; consent exceptions, records, funding, disclosure | curl full PDF succeeded; web timed out. S14 scope. A professional FAQ, not legal advice or a current budget balance. Results need consent to disclose; no owner/person records ingested. |
| **S05** CMO, [assessment, promoters and stations portal](https://cmo.gov.taipei/cp.aspx?n=023341AF71C3812D) and [community architects](https://cmo.gov.taipei/cp.aspx?n=208761DB4C1C011B) | HTML links to 2026 assessment institutions, service areas, initial/detailed fee schedules, station locations/hours and FAQ; current page read | Index, community-architect service description and FAQ inspected; fee/station attachment bytes not inspected, so no provider count, price or current appointment capacity claimed. S14 scope; no named-person directory copied. |
| **S06** Taipei Urban Regeneration Office (URO), [FL088307 rules](https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL088307) and [2026 application pack](https://uro.gov.taipei/News_Content.aspx?n=9CAC69257CFAC70E&s=8860150E93FF8321&sms=1635F69C7777535B) | Entire rule points 2–11, effective 2025-12-22; pack document labels: assessment/improvement-benefit evidence, representation, contract, budget, self-funding share; building/project | Readable. Official rules excluded from copyright according to S14 URO declaration; other site content has qualified reuse, not blanket open licensing. Actual eligibility requires case review. |
| **S07** Taipei City/URO, [revised 2026 subsidy announcement](https://www-ws.gov.taipei/001/Upload/459/relfile/22615/7678008/fcc3298a-9b8d-468f-b8b5-b3c1c073ed20.pdf) | Both scanned PDF pages rendered and inspected; 2026-07-01 notice, annual application window/caps and budget exhaustion | Text extraction empty; visual read essential. Ordinary maximum 50% of approved engineering cost, special categories up to 80%, subject to limits; no actual award/remaining funds verified. S14 legal/official-notice distinction. |
| **S08** NCREE project office, [耐震階段性補強電子報第2期](https://privatebuilding.ncree.org.tw/wp-content/uploads/2022/04/epaper2.pdf) | Full PDF downloaded, printed pp14,24–25 operator accounts; Pingtung Linsen Road meetings 2020-02-03/03-20, community/project unit; upload path is 2022, not event date | Original operator report; copyright indicated, redistribution license unknown. Reports affordability issue and increased willingness after explanation; uncontrolled, no verified final completion or Taipei transfer. Historic subsidy tables are not current policy. |
| **S09** Kuo/Lin, NTU authors, [WSBE2026 conference abstract](https://wsbe-2026.p.asnevents.com.au/days/2026-06-10/abstract/131434) | Entire author abstract, 2024/2025 questionnaire, OLS/ANOVA; individual intention, Taiwan | Public abstract; sample size/design/full results unavailable, redistribution license unknown. Neighbor agreement/subsidy familiarity reported associations; cannot establish actual uptake or causation. |
| **S10** Shih, NTU, [2025 landlord thesis metadata/abstract](https://tdr.lib.ntu.edu.tw/handle/123456789/100194?mode=full); Kuo/Lin, [journal metadata](https://scholars.lib.ntu.edu.tw/entities/publication/585945f9-1448-4177-a366-62a25cfb16fb) | Thesis abstract, contents and rights; questionnaire/factor/logistic analysis. Journal abstract/metadata: issue date 2026-11-01, later than retrieval | Thesis campus-restricted until listed 2030 embargo lift; no bypass/full-text claims. Journal full paper uninspected; distinct analytical description from S09, so not pooled. Copyright/no redistribution grant verified. Both are author reports, not implementation outcomes. |
| **S11** Taipei Public Works, [liquefaction Q&A](https://soil.taipei/Taipei2019/Main/pages/QA_handle.html) | HTML interpretation, precision and boundary-case sections; area-level modeled susceptibility, professional foundation/geotechnical referral | Readable; exact GeoJSON class legend/rights not re-audited. Explicitly cannot determine a single building site's liquefaction. No model rerun or observed damage data. |
| **S12** Taipei DBAS, [building-count catalog](https://data.taipei/dataset/detail?id=7889e8a0-a71e-44e0-95c7-2213a7db1474), [exact CSV export](https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=6500&kind=21&type=0&funid=a05019201&cycle=4&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1) | Full UTF-8-sig CSV, Python `csv.DictReader`: 50 rows, 13 columns, ROC65–114/1976–2025; city totals, floor bands, age below/above30 | Catalog says public/free, footer links government open-data terms; no specific license-version string verified. No address, structure, assessment, village or building ID. Early age fields contain zeros; no inference of zero old buildings. |
| **S13** National Audit Office, [2021-era MOI review excerpt, printed p190](https://auditreport.audit.gov.tw/ServerFile/Get/637958482351902989b9fc1d422f4940cc93cc2e535992b47c); [Taipei renewal audit NAO-110-05](https://www.audit.gov.tw/p/405-1000-7467,c158.php?Lang=zh-tw) | First PDF section16/table33, national 2019/2020 subsidized assessment; Taipei audit landing methods/response only | National audit records below-plan assessments and incomplete reporting from ten jurisdictions: not a current Taipei failure rate. Taipei full attachment failed; curl landing encountered security interstitial. Only inspected landing claims used. Redistribution license unknown. |
| **S14** [CMO reuse declaration](https://cmo.gov.taipei/cp.aspx?n=CC5912F40B7F47CE); [URO reuse declaration](https://uro.gov.taipei/News_Content.aspx?Create=1&n=9FFBA0A9ECB48B79&s=B165EFC04CD35609&sms=73366C9BCCD2AC2A&state=F5D336F102ACBC68); [NCREE current service](https://privatebuilding.ncree.org.tw/); [2026 promoter notice](https://privatebuilding.ncree.org.tw/20260729/5979/) | Declarations; service homepage and entire July29 promoter notice; free community explanations, qualified facilitator role, staged reporting and bounded funding | CMO grants attributed reuse with exceptions; URO protects other content beyond laws/notices and reasonable-use cases. NCREE reuse unknown. July notice approval-date window ended September15; do not advertise it as new October funding. Homepage mixes current news with older FAQ funding figures. |

### Organizer starter dataset pages (2026-10-13)

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [ec40e067: 臺北市土壤液化潛勢圖](https://data.taipei/dataset/detail?id=ec40e067-930f-4058-b7dc-71399d5f3147) | Public Works Department; irregular; catalog 2025-06-17; declared 2016-09-10–2018-03-23. | [WGS84 GeoJSON](https://soil.taipei/Taipei2019/Main/pages/TPLiquid_84.GeoJSON): earlier206/sample; later T06 primer full GET200/parse:136 MultiPolygons, CRS84, `class` categorical string only. Later allocation audit finds2 invalid polygons; originals preserved, no automatic repair. [TWD97 alternative](https://soil.taipei/Taipei2019/Main/pages/TPLiquid_97.GeoJSON) linked, not separately sampled. | Numeric class-to-risk legend and map scale not established in this audit. No new survey date inferred from 2025 catalog date. Ground susceptibility is not a building structural-safety assessment. Need source legend, scale and official interpretation before scoring. |
| [a6394e3f: 臺北市各里人口數按年齡分](https://data.taipei/dataset/detail?id=a6394e3f-3514-4542-87bd-de4310a40db3) | Department of Civil Affairs; monthly; file/catalog 2026-10-05. | Latest [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=c8f5b53d-ef3d-4321-ae8e-58cd2a5ee73c): 200/full, Big5, 63,315 rows. Actual ROC year/month 112/1–115/9 (2023-01–2026-09); area code/name, sex, total, each age 0–99, 100+. Older 2021/2022 files linked separately, not sampled. | **Includes city and district totals as well as villages**, and total/male/female rows. Filter level/sex before summing to avoid double/triple counting. Registered population is not daytime occupancy or exact household/building vulnerability. Village polygons needed for map joins. |
| [7889e8a0: 臺北市現有營造建築物棟數](https://data.taipei/dataset/detail?id=7889e8a0-a71e-44e0-95c7-2213a7db1474) | Department of Budget, Accounting and Statistics; annual; catalog 2026-02-26; 1976–2025. | [Statistics CSV export](https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=6500&kind=21&type=0&funid=a05019201&cycle=4&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1): 200/full. Actual periods 65年–114年; citywide building counts by floor bands and age below/above 30 years; unit buildings (棟). | **No building addresses, footprints, construction dates or structural assessments.** Cannot join citywide age totals to village-age population and label particular homes unsafe. Suitable for citywide context only. |
| [7a800e92: 臺北市政府消防局消防通道清冊](https://data.taipei/dataset/detail?id=7a800e92-eb22-461f-b29d-8def2127a1bc) | Fire Department; irregular; file **2024-08-01**, catalog 2025-12-09. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=351307e4-ffda-4660-ac72-1c4ef3808c38): 200/full, 185 entries. ID, district code, village, listed street/place, criteria, difficult-rescue area, responsible fire unit/contact. | No geometry, coordinate or individual building safety. Geocoding needs street-range interpretation and verification. Catalog change does not prove the 2024 list is freshly surveyed. Institutional phone fields are not required in a public demo. |
| [6f03a0b8: 臺北市水利處雨量站即時資料](https://data.taipei/dataset/detail?id=6f03a0b8-7b98-4eea-8bb9-ba6bfcdc2b8b) | Hydraulic Engineering Office; catalog 2026-04-24; declared real-time 10-minute/1-minute update. | Publisher page embeds public Rain/Get API configuration; read through that supplied configuration: 200 JSON, count 42. Schema `stationNo`, `stationName`, `recTime`, `rain`; description says **current daily accumulated rainfall**, not instantaneous intensity. Endpoint base: `https://wic.gov.taipei/OpenData/API/Rain/Get`; obtain published parameters from publisher rather than copying them into Git. | No station XY in this response. Units/timezone not explicitly established by sampled metadata. **Station 025 永建國小 has recTime `206104101520`**. Under the YYYYMMDDHHmm format used by the other records this denotes 2061, inconsistent with retrieval; the root cause is unconfirmed. Other station timestamps parse as 2026-10-13 16:50–17:10. Must flag or exclude invalid/future records and assess freshness per station. One snapshot does not establish reliable warning performance. |
| [b3648c5d: 臺北市水利處雨水下水道水位監測站](https://data.taipei/dataset/detail?id=b3648c5d-15c8-416a-a603-fda7a9ac1b0d) | Hydraulic Engineering Office; irregular; file 2025-09-12, catalog 2026-09-07; coverage through 2026-09-07 declared. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=586e5233-aa60-4680-8ac1-cbb9ef7f7fde): 200/full, 233 rows. Facility ID, station name, district, longitude, latitude. WGS84 explicitly declared. | **Station locations only; no water-level value, timestamp or warning threshold.** This file cannot power an actual flooding alert without a separately verified measurement feed and threshold authority. Do not equate catalog coverage end with latest measurement. |

## 6. Readiness and integration

Preserve T06 and all three workflows as hypotheses with explicit rejections above. Carry forward **demonstration=specified / decision=insufficient**, not a safety-prioritization readiness upgrade. S12 refresh strengthens the existing `7889e8a0` aggregation limit; S11 confirms the `ec40e067` interpretation restriction without refreshing its GeoJSON audit. At the earlier deep-run stage, `a6394e3f` and `7a800e92` were not refreshed; the later T06 domain primer now records full-file shape refreshes, without upgrading physical accuracy or decision readiness. Neither is essential to these narrowed actions. The owner subsequently refocused the allocation-priority record on inspection/public-renewal decisions. The 2026-10-14 identity audit verified a permit/footprint/doorplate chain for2001+ use permits only; the same-day deep investigation found selection rules, professional thresholds, district-level stock data and precedents, and reframed A as tiered screen-to-verification sequencing. Bounded quality audits now qualify the population, building-count and liquefaction dependencies; the earlier T06-C intake comparison remains a bounded fallback, not the current priority.

Status lives in the [canonical readiness record](../research.md#problem-fit-and-separate-readiness-of-the-expanded-candidates); this section records only the issue-specific consequence.

## 7. Next actions and open decisions

**Next executable check:** two open facts decide the route finder's value. First, how often Taipei
has granted prompt designation to a 危老 case that lacked unanimity. Second, the minimum unit size
that then applies. Read the urban renewal office's designation notices and the current
臺北市都市更新自治條例. Publication or outreach is not authorized by this check.

**Open owner decision:** route 1 reads public Taipei City Council business reports and audit
reports for annual assessment and retrofit counts (default, no contact). Route 2 files information
requests for de-identified initial-assessment statistics or house-tax statistics under 稅捐稽徵法
§33 ¶2; this is external contact and needs action-time confirmation.

**Reading mirror rule:** refresh [the HTML report](issue-6-building-resilience.html) whenever this
document's conclusions change materially.

## Change log

| Date | Change |
| --- | --- |
| 2026-10-13 | Owner focus on issue 6; domain primer; allocation reorganization into decisions A and B |
| 2026-10-14 | Identity audit; deep investigation (P/E/I/X); owner rule to start from the live prompt and citizen voices; pain re-anchor and pain tree; T06-D added; moved into this topic document (template v1) |
