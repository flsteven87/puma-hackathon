# Research Brief

## Scope

Independent, public-source research into Taipei civic problems, using 市政 debug松 as the
starting point. This edition covers six organizer themes, eight expanded hypotheses and the
retained MRT question across ten tracks and 25 distinct workflows. It does not establish a
selected project, participation, an implemented application or measured municipal benefit.

## Reading guide and evidence date

This file is the single research authority. Source observations were retrieved on **2026-10-13**;
the ten-track deep run below re-read only its named sources and adds current source comparisons. Older audits retain their original scope; a retrieval does not establish current operating conditions. Earlier recommendations remain explicitly qualified as historical in this brief.

| Reading goal | Current section |
| --- | --- |
| Understand the organizer's problems and scope | [Official pain points](#official-pain-points-and-decision-fit) |
| Understand how candidates are judged | [Research umbrella policy](#research-umbrella-policy) |
| Compare all ten tracks and their separate decisions | [Current comparison](#cross-topic-decision-comparison); [historical eight-candidate comparison](#synthesis-and-recommended-order) |
| Check what is ready and what would reject a proposal | [Canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates) |
| Find additional dependencies and their verification state | [Dataset-to-candidate index](#dataset-to-candidate-index) |
| Reproduce the completed numerical comparison | [Meal-list analysis recipe](#reproducing-the-meal-list-comparison) |
| Inspect exact schemas, URLs, counts, licenses and failures | [Transport](#additional-transport-evidence-collision-review-and-youbike-transfers), [street environment](#environment-parks-and-street-service-track--outside-organizer-starters), [care services](#additional-theme-everyday-care-service-access), [flood preparedness](#flood-preparedness-twinkle-discovery-plus-original-publisher-audit), [organizer audit](#publisher-dataset-audit) |
| Read the completed problem-first investigations | [Ten-track findings](#ten-track-deep-research-findings) |
| Find the next consequential check | [Next-investigation queue](#next-investigation-queue) |
| Understand data-discovery provenance | [Twinkle source classes](#twinkle-provenance-and-role-in-this-project) and [AI/source provenance](../README.md#ai-and-data-source-provenance) |

**Interpretation:** catalog read, row sample, full-file parse and validated join are different
observations. A full parse verifies only the stated checks; it does not prove completeness,
unique real-world objects or operational accuracy. Counts refer to records unless explicitly
qualified. In particular, a meal-list row is not a verified operating site/capacity unit; an entrance
row is not a park/station; and collision rows are not asserted unique accidents or all victims.

## Data findings at a glance

**Inference — historical data-readiness finding, qualified 2026-10-13:** expanded research using
Twinkle and original publishers identified collision-site review, district senior-meal inventory
and accessible park-entry comparison as data-grounded hypotheses. This is not the current research
priority or evidence of greater problem value. The owner's latest direction requires the same
problem-first analysis across official directions and C01–C08 before further comparison. All
existing audits remain dated inputs; no candidate is selected or authorized for implementation.

**Evidence:** 22 distinct listed government dataset pages were readable, but one traffic catalog
is withdrawn. Food-business data is one citywide total, public complaint categories contain no
coordinates, the listed bus-stop file is from 2021, and the water-level dataset is only station
locations. Tree exports contain older surveys and duplicate holes. The legacy recovered VD feed
contains a 2024 timestamp; a later full read of the separate v2 feed establishes current public
access, with historical retention still unresolved. MRT offers 116 monthly index entries through August 2026; the latest
monthly CSV was successfully sampled. See the source-specific audit for dates and methods.

**Current limit:** ten tracks now have problem/baseline and bounded rejection findings; operational decision gain is still unvalidated. Follow the current comparison/queue before choosing a contest topic. No implementation, registration or organizer contact occurred; no raw citizen
reports or personal information were retained in Git.

## Official baseline

**Evidence — retrieved and independently re-read during the deep run on 2026-10-13:** the [official event page](https://puma.taipei/hackathon)
announces 市政 debug松, organized by 沈伯洋競選辦公室. Registration closes October 18 at 23:59;
capacity is 80 and attendance is free. October 23, 19:00–22:00 is online; October 24,
09:30–18:00 is onsite. At least one team member must attend onsite. Submission closes October 24
at 16:00. Dates are interpreted as 2026, local Taipei time, from the current event context;
the displayed schedule omits the year and timezone.

The seven directions concern trees, public bins, rats, Neihu traffic, bus networks, building
resilience and a self-chosen civic problem. Working demonstrations are required. Simulated inputs
are allowed with disclosure; README must identify AI tools and open-source dependencies. Coding
is permitted from Day 1. Complaint data is activity-only and must not identify people. Dataset
licenses apply individually. Teams retain copyright; organizer open-source inclusion needs consent.
Voting determines three featured works; there is no prize money.

Method: curl retrieval and standard-library HTML text inspection; web search corroboration.
Scope: this baseline verifies one organizer page. Dataset access is examined in the audits below;
organizer civic statistics/causal claims remain uncorroborated unless separately sourced. Recheck
event rules before acting.

The deep-run read again found the six themes and independent free-topic container, operable-demo
requirement, source-specific terms, activity-only organizer feedback and real/simulated disclosure.
The browser search tool again could not open this page; direct curl GET and HTMLParser extraction
succeeded. This is current page evidence, not confirmation of registration, team acceptance or
the organizer's underlying civic claims. No registration, external submission or contact occurred.

## Official pain points and decision fit

**Evidence — retrieved again 2026-10-13:** the [official issues section](https://puma.taipei/hackathon#issues)
frames the topics as citizen pain points organized by the policy team. Six prompts include desired
directions; the seventh invites an independently defined problem. The page permits disclosed
simulated inputs and prioritizes an operable solution. Its [rules](https://puma.taipei/hackathon#rules)
require a working demonstration and recommend explaining the department, data and cost needed
for implementation within 100 days.

Method: curl GET, standard-library HTMLParser text extraction and inspection of `issue-1` through
`issue-7` and `rules`. The web browsing tool could not open the page; curl succeeded. Limitations:
this verifies the organizer's framing, not the prevalence, causes or numerical claims behind it.
Citizen feedback was still announced as forthcoming; no interviews or operational outcomes were examined.

The second column paraphrases official framing; the third is **analyst inference**.

| Official prompt | Pain point and requested direction | Decision to investigate, not a validated requirement |
| --- | --- | --- |
| [Trees](https://puma.taipei/hackathon#issue-1) | Recover planting space after removals; improve shade equity | Which sites deserve feasibility checks first, and who benefits? |
| [Bins](https://puma.taipei/hackathon#issue-2) | Reduced provision and full bins; demand-informed placement and cleaning | Where should provision change, or when should collection occur? |
| [Rats](https://puma.taipei/hackathon#issue-3) | Reactive treatment; source prevention informed by food, waste and pipes | Where should inspection or source control start, and why? |
| [Neihu traffic](https://puma.taipei/hackathon#issue-4) | Concentrated morning traffic; evidence for staggered working hours | Which time windows should employers and the city examine together? |
| [Buses](https://puma.taipei/hackathon#issue-5) | Overlapping services and demand mismatch; flexible routes, with driver rest as an additional direction | Which corridor warrants an alternative subject to passenger and labor constraints? |
| [Building resilience](https://puma.taipei/hackathon#issue-6) | Aging residents and buildings; prioritize assessment and renewal | Where should professional assessment outreach begin? |
| [Free topic](https://puma.taipei/hackathon#issue-7) | Team-defined problem; starter suggestions include weather, MRT and kindergarten checks | Establish the user, recurring decision and unmet need first |

**Inference — correction to the earlier recommendation:** data readiness is not overall topic merit.
A tree inventory is a prerequisite to site review, not proof of planting feasibility or shade equity.
A bin-access comparison addresses placement, not overflow or collection dispatch. MRT charts remain
a free-topic hypothesis until tied to a recurring decision. A narrowed workflow must identify its
contribution to the official pain point and the parts it leaves unresolved.

**Open question:** which decision causes a repeated, consequential difficulty for a reachable user?
The official page does not establish a validated workflow, baseline or agreed success threshold.
Public-source research can investigate those gaps; external interviews/messages retain the existing
action-time confirmation boundary.

## Research umbrella policy

**Method — 2026-10-13:** research each topic backward from an evidenced pain point and
observable success/rejection conditions. This policy governs data discovery, comparisons and
demonstration proposals across organizer and expanded candidates. Data readiness does not establish
problem value. It preserves the distinctions between public-source research, implementation,
participant contact and operational decisions. The source search is not restricted to a provider
or government APIs; original academic, community and operator publications are relevant too.

### Decision-first sequence

1. **Establish the pain point.** Find a concrete situation, affected user, recurring trigger,
   current practice and consequence. Distinguish a published procedure from evidence of actual
   difficulty. Completion: each claim has its source and limit, or is a hypothesis with a resolution action.
2. **Bound the problem.** Name one decision owner, place/time, decision and executable action;
   compare the current process and existing tools. Test whether information is the bottleneck or
   whether authority, funding, capacity or coordination dominates. Completion: state the addressed
   and unresolved parts of the pain point and the plausible contribution of an information tool.
3. **Define success and rejection.** Before further data experiments, state what would improve
   relative to the baseline, how to observe it and what would refute that improvement. Include a
   problem-level and a data-level rejection condition. Completion: predefine supported, refuted
   and unresolved outcomes and their next actions; explain candidate-specific thresholds and sampling.
4. **Specify the user action.** Trace input → assessment/comparison → user action → checkable
   output. Separate workflows with different users or decisions even when they share data.
   Completion: one bounded example identifies who can act and why the result would change or justify a choice.
5. **Find and audit necessary evidence.** Work backward from the decision and success conditions
   to essential fields, then use broad source discovery and original-publisher verification.
   Completion: each dependency has observed access, period/unit, license, quality limits and
   decision relevance, or is explicitly missing/modeled/simulated with a consequence for the claim.
6. **Define the final presentation and compare.** Present the same bounded case from evidenced
   pain and baseline through action and result, including rejection evidence and remaining impact
   uncertainty. Completion: the required record below is complete for each workflow, unknowns
   have resolution actions, and the queue names one consequential next check per topic. Compare
   all topics on the same dimensions; topic selection and participation remain owner decisions.

### Required candidate record

Maintain these fields in the existing topic sections; the canonical readiness record owns status
and the queue owns sequencing. Link shared evidence rather than duplicating it. Use `unknown`
with a topic-specific resolution action; a source hit alone does not complete a field.

| Field | Required content |
| --- | --- |
| Problem and fit | Sourced pain and consequence; official direction/free-topic fit and overlaps; addressed/unresolved parts |
| User and decision | Affected user, decision owner, trigger, current practice and existing tools; failure/bottleneck and observed vs hypothesized claims |
| Success and rejection | Improvement relative to the existing baseline; problem-level and data-level rejection; supported/refuted/unresolved outcomes and actions |
| Workflow | One user's input → assessment → executable action → observable output, within a bounded place/time; separate other users' workflows |
| Dependencies | Essential fields and source-audit links; access, period, spatial unit, license and gaps |
| Claims | Observations, proxies, modeled scenarios and simulated inputs distinguished; permitted conclusion |
| Readiness | Separate demonstration and decision judgments; explicit civic-outcome evidence or unknown |
| Validation | Smallest decisive experiment, comparison baseline, sampling/threshold rationale, difficult cases and permitted generalization |
| Adoption | Likely department/operator, missing authority/data/expertise and cost unknowns for a 100-day path |
| Presentation | One bounded before/action/after case; permitted claim, provenance and remaining unproven benefit |
| Next action | One executable check that resolves a consequential uncertainty |

### Separate readiness judgments

- **Demonstration:** `unassessed`, `blocked` or `specified`. `specified` means a workflow, inputs,
  disclosure and observable interaction are defined sufficiently to propose implementation; it
  does not mean an application exists or passed testing. Disclosed simulation can support this status.
- **Decision:** `unassessed`, `insufficient` or `supported for bounded use`. The last status requires
  observed relevant data, validated joins/coverage and evidence of an executable, more useful
  decision relative to the baseline (for example, fewer missed review-worthy cases or reduced effort
  without worse errors). Record the permitted use, uncertainty and required human review.
  A working interface, analyst-chosen weights or synthetic outcomes cannot establish this status.

Within these existing judgments, report three distinct observations: task completion/usability,
decision usefulness relative to current practice, and civic outcomes. Civic outcomes require
appropriate outcome/comparison evidence; they may remain unknown while a bounded workflow is useful.
`specified` describes a written demo specification, including its hypothesized elements, rather
than observed usability, adoption or impact. Research progress is not an effectiveness result.

### Problem evidence and existing baseline

For each topic, distinguish organizer assertions, documented procedures/plans/budgets, operational
statistics or audits, and first-hand published/observed accounts. These answer different questions;
they are not a single evidence ladder. Record population, period, method, source independence,
conflicts and transfer limits. A formal procedure establishes a process, not user difficulty;
complaints show reported concerns, not prevalence; a study elsewhere supplies a hypothesis for
Taipei, not local proof. Primary sources include the original researchers, operators and communities,
not only government agencies. Secondary reports can lead to evidence but keep their claims attributed.

Inspect existing portals/tools and the documented manual process against the same bounded task.
Record what is already possible and which action-relevant gap remains. Reject or narrow a redundant
solution if the baseline serves the task adequately; do not require novelty where a demonstrated
accessibility or effort improvement remains. Search for contrary evidence and alternative causes,
including constraints that better information would not change. Unobserved practitioner pain,
use intention and real workflow performance remain hypotheses; public evidence can ground the
next experiment without pretending that contact or observation occurred.

### Source discovery and bounded assistance

Discovery may use search engines, public websites/portals and downloads, research papers and
repositories, university/NGO/community/operator publications, open geospatial or remote-sensing
data, public archives, and documented APIs or MCPs. Choose routes for the missing evidence,
not to accumulate sources. Inspect the exact original material for access, fields, dates, units,
coverage, transformations, reproducibility and terms. Public readability is not redistribution
permission. Restricted or inaccessible material stays a lead; do not bypass access controls.
Keep personal records out of Git and preserve source-specific restrictions and attribution.

AI-assisted discovery uses bounded questions, search routes and completion conditions. Return
exact source URLs/publishers, observed content/schema/period, licensing evidence, limitations
and contradictory findings. Uninspected hits remain leads. Check consequential claims against
original material before integration; model output is not evidence. Stop a search branch when its
assigned uncertainty is resolved or the named route is exhausted, recording the remaining unknown
and next feasible check. AI/source provenance is summarized in the repository README.

### Validation exits and fair comparison

Every experiment states supported, refuted and unresolved outcomes with corresponding continue,
revise or defer actions. Defer a workflow when its action value is refuted, essential evidence has
no feasible acquisition route, or honest narrowing no longer addresses the problem. Preserve its
candidate and explain the resume condition; lack of public evidence does not disprove a pain point.
Use sample and time bounds justified by the consequential uncertainty, not universal thresholds
or an assumed contest deadline. Exploratory manual checks support only their inspected scope;
include missing, ambiguous and boundary cases and relate error tolerance to decision consequences.

Give all official directions and existing hypotheses the same minimum problem record before
cross-topic recommendations. Report uneven investigation depth explicitly and compare problem
evidence, decision value, evidence sufficiency, testability, adoption constraints and misleading-use
risk separately. Unknown is not low value. Overlapping topics can share evidence while keeping
distinct decisions and success conditions; the free-topic direction is a container, not an extra
candidate to count against its own children. No arbitrary weighted overall score is introduced.

### Claim and recommendation controls

- Attribute organizer assertions until corroborated. Availability, factual accuracy and suitability
  for a decision require separate evidence. Verify the exact resource rather than its title or HTTP status.
- For new or substantively changed claims, link evidence to its dated observation and exact resource,
  with method and limitations; link inferences to that evidence and the reasoning. Hypotheses and
  owner decisions retain their own types. Keep historical results dated, and record unobserved
  versions or checks as unknown rather than backfilling them. A retrieval date/URL is not an immutable version.
- When changed evidence affects a conclusion, update the dependent interpretations before treating
  them as current. If a conflict or revalidation remains unresolved, qualify the affected conclusion
  as pending revalidation and record the remaining check. Model- or analyst-generated synthesis
  alone establishes neither accuracy nor operational decision readiness.
- Match conclusions to measurements. MRT gate counts are not sidewalk footfall; reports are not rat
  prevalence; tree locations are not shade; area context is not individual building safety. The
  analytical controls below own spatial, temporal and aggregation checks.
- Simulation demonstrates interaction or scenario behavior. Disclose provenance and assumptions,
  vary consequential assumptions, and distinguish simulated inputs/results from observed ones.
  Preserve official modeled scenarios as modeled evidence, not observed events.
- Compare problem fit, likely decision value, evidence sufficiency, tractable demonstration, adoption
  constraints and risk of misleading users. Explain tradeoffs; do not collapse unknowns into an
  unsupported weighted score. Label a data-readiness ordering as such.
- When essential inputs are absent, narrow the claim, investigate another source, specify a disclosed
  scenario or defer the candidate. State how narrowing changes the original problem's coverage.
- Research keeps existing scope and confirmation boundaries for professional judgments,
  implementation, participation, payment and external contact. This policy adds no approval gate
  to ordinary authorized public-source research.

### Applying the policy to the organizer-starter candidates

**Inference — refreshed after the deep run:** all six official themes and the retained MRT
hypothesis now have dated problem/baseline investigations and separate workflow records below.
Their information-tool value remains hypothesized even where original sources establish pain.
The [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates)
now covers official and expanded workflows together; it replaces the former blanket
`demonstration=unassessed` starter table. No safety rating, optimized service or causal benefit is established.

### Applying the policy to expanded free topics

C01–C08 retain their identities. Their distinct workflows received the same minimum record;
C02/C03/C06/C08 have different users and cannot transfer value between those decisions.
C05's real-facility review is blocked by missing entrance/floor evidence; a completed scenario-file
audit is not that demonstration. All operational decision judgments remain insufficient.
The historical source-readiness comparison below is preserved with its original qualification.

## Ten-track deep research findings

**Evidence and inference — deep run, 2026-10-13:** the following records extend the existing
research authority. Track numbers preserve ownership, not priority; C01–C08 retain their identities.
Source-level experiments resolve specified data or baseline questions. They do not substitute for
observed practitioner task performance, adoption or civic outcomes. Each workflow distinguishes
supported, refuted and unresolved claims and names the condition for continuing, narrowing or deferring.
Older audits below remain dated observations; only explicitly re-read dependencies are refreshed.
The canonical readiness record and next-investigation queue own status and consequential next steps.

### T01 Trees, shade and accessible park use

Research observation: **2026-10-13**, Asia/Taipei. Three workflows remain distinct: planting/shade field-review prioritization, officer accessibility inspection, and caregiver trip choice. Their common geography does not make them one decision.

#### Findings and scope

**Supported — continue narrowly:** local thermal-exposure research and original disability-community observations establish reasons to investigate shade and access. They do not establish a validated product requirement. The organizer's tree-removal number and “shade equity” framing remain organizer assertions; this pass did not independently reproduce annual removals or exposure inequality. Official tree work is an existing regulated, surveyed activity, not an unowned opportunity. [T01-S01][T01-S02][T01-S03][T01-S04]

**Refuted — revise the data proposition:** a tree-hole row is not an available planting location; an entrance labelled accessible is not a verified continuous trip. The existing Wheelroute endpoint already contains the park entrance measurements being proposed for C03. Its agreement with the park export cannot independently validate their locations: the same two gross coordinate anomalies appear in both. A new entrance map alone has no demonstrated decision gain. [T01-S06][T01-S07][T01-S08]

**Unresolved — defer operational recommendations:** practitioner effort, prioritization usefulness, present physical conditions, adoption and civic outcomes are unobserved. Public evidence supports an inspection-evidence workflow better than a safe-trip recommendation, but this is a within-track research disposition, not selection over other topics. Accessibility is a free-topic fit with partial overlap with shade equity; it does not solve planting or cooling. Event participation and implementation remain owner decisions.

Evidence depth is unequal: full structured-source checks are strongest for entrances, while heat evidence is older site research and planting evidence includes one current operator account. No interviews, site visits, route traversal, temperature measurements, simulation or application were performed.

#### Exact source ledger

All entries were inspected on **2026-10-13**. “Web GET” means opened original content with the browsing tool, not a search snippet. “curl GET” means public unauthenticated retrieval with a 35-second bound; metadata, whole-file parse and page markup are different observations. Dates below describe sources, not refreshed physical surveys. The linked source IDs are reusable citations.

| ID / publisher / title | Inspected material, period and spatial unit | Access, rights and limitations |
| --- | --- | --- |
| [T01-S01] Organizer — 市政 debug松 | curl GET 200; issue 1 and simulation/rules text; Taipei topic framing | Public page; no blanket reuse license established. Annual removal/incident claims attributed; not independently audited. No deadline relied upon. |
| [T01-S02] NTU / researcher — 應用熱感受累積量建構戶外熱舒適指標檢驗人行道綠化品質之研究 | Web GET, 2017 thesis abstract, contents, rights; Zhoushan Road campus greenway; field thermal/dynamic questionnaire experiments plus RayMan/TMY3 modeling described | Abstract public; PDF restricted and rights note 有償授權. No payment or bypass. No sample size/effect magnitude independently checked; cannot extrapolate citywide or to wheelchair users. |
| [T01-S03] NTU / Cho — 都市道路組成與行人熱舒適關係之研究 | Web GET, 2017 abstract/method/rights; Taipei 40-m roads, one validation site and modeled composition alternatives | Public metadata; global public access permission, copyright retained, no open redistribution license established. Abstract-level results, not reanalysis or all-street validation. |
| [T01-S04] Taipei laws — 行道樹管理維護自治條例 | Web GET, current displayed 2024-10-21 revision; arts. 2, 4, 6–8; city jurisdiction | Public legal text, no dataset license needed for factual summary. Establishes authority/approval, not workload pain. |
| [T01-S05] Taipei Building Administration — 本市人行道植樹規範, 1146104522 | curl GET 200 after web 502; 2025-04-25 letter, all principles; sidewalk sections/intersections | Public text; bulk republication terms not separately established. Prioritize clear width before planting; road/driveway and sight-distance restrictions. This is not an automatic eligibility formula. |
| [T01-S06] Parks Office — dataset 128274, tree inventories / tree-hole JSON | National catalog Web GET; entire linked `TaipeiTreeHole.json` curl GET 200 and JSON parse; hole records with TWD97 XY, update dates | Catalog explicitly OGDL v1; snapshot not occupancy survey. Tree and park-tree bulk resources not reread; earlier staleness findings remain historical. Hole schema/duplication tested below. |
| [T01-S07] Parks Office — dataset 152266, 公園無障礙出入口點位 | Both catalogs Web GET; exact CSV curl GET 200, Big5 decode, all eight columns/745 records; file date 2026-03-16, metadata 2026-07-22; entrance points | National catalog explicitly OGDL v1; municipal metadata specifies minimum clear width in meters, slope percent. No per-entry survey time, terrain exception, surface or continuous path. TW97 label alone does not establish precise EPSG. |
| [T01-S08] Transportation Department — 輪行臺北 / facility type 7 | Website and catalog Web GET; exact API curl GET 200, full JSON; entrance facilities, current snapshot without observation dates | Catalog says public/free; generic government-license footer exists, but dataset-specific scope not confirmed here. Width documented in centimeters versus meter-like values. API is not independently surveyed validation. |
| [T01-S09] Taipei Metro — dataset 128414, accessible elevators/ramps GPS | Catalog Web GET; exact CSV curl GET 200, Big5, 193 rows; name/exit/lon/lat plus empty column; metadata 2026-08-31 | OGDL v1 explicitly listed; network scope, not city-only; no equipment status, hours or connected walk. Not treated as a real-time service. |
| [T01-S10] 行無礙協會 / 阿里 — 從社區公園看日常生活中的障礙與問題處境 | Web GET, complete article; posted 2024, embeds 2018 authorship and surveys from ROC 100 onward including planned ROC 108; Taipei district parks | Public original advocacy/field account; reuse license not established. Entrance barriers, surfaces and slopes described; raw survey/photos not audited, tally includes time ambiguity. Neither current prevalence nor unique injury counts inferred. |
| [T01-S11] Parks Office — 北投公園周邊人行道鋪面更新 | curl GET 200 after browser timeout; 2020-09-23 release; park approaches and surface treatment | Public operator account, detailed redistribution terms unchecked. Reports repeated complaints and material choice; no independent post-work usability evaluation. |
| [T01-S12] Parks Office — 三民公園 playground information | Web GET, transport/amenities table; updated 2024-06-26, playground opened 2018; named site | Public official page, no specific open license inspected. Lists shade but no accessible toilet/rest area; current condition and geographic amenity extent unverified. |
| [T01-S13] Guandu Nature Park operator — 友善服務 | Web GET, facility locations and services; named park, no observation date supplied | Public operator page, copyright reserved; no redistribution permission inferred. Accessible toilets, ramps, wheelchair lending reported; does not certify outside approach or live availability. |
| [T01-S14] Zhao et al. — nighttime street-canyon wind-tunnel study | Web GET of author-submitted arXiv abstract/version, 2023; scaled canyon experiment | Public preprint with linked [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/) inspected; abstract inspected, full study not reanalyzed. Nighttime/extracity counterexample, not measured Taipei effect. |
| [T01-S15] Parks Office — 敦化南路一段移植榕樹補植樟樹 | Web GET main release, 2026-09-18, displayed update 2026-09-29; named street work | Public official account; release-specific reuse terms unchecked. Operator reports roots/drainage complaints, leak repair and replanting; contested-event explanation not independently verified. |
| [T01-S16] MOI / Ministry of Justice — 活動場所無障礙設施設備設計標準 | Web GET, arts. 3–4, 6–7; displayed 2015-10-22 standard, compilation cutoff 2026-10-02; parks/green spaces | Public law, factual summary only. Entrance/path, turning, surface, conditional slope and information requirements; not an entrance-data certification rule. |
| [T01-S17] Digital Affairs Ministry — OGDL v1 | Web GET, rights/attribution/disclaimer sections | Allows reuse/adaptation under attribution obligations; does not establish accuracy, physical accessibility, endorsement or rights to unrelated imagery. |
| [T01-S18] Parks Office — 行道樹路燈資訊網 | curl GET 200, public page markup: ID/district/species/area queries, relocation-history and hole queries, export controls | No login attempted; controls inspected, interactive query success/export not tested. Public readability does not establish bulk-history coverage or imagery license. |

##### Exact structured resources

- T01-S06: [tree-hole JSON](https://tppkl.blob.core.windows.net/blobfs/TaipeiTreeHole.json).
- T01-S07: [park-entry CSV](https://data.taipei/api/dataset/5a7258c2-5ded-4149-8664-ae10903fe372/resource/70defec1-fd51-471b-89fa-5c7636150e6a/download); [municipal units/file-date metadata](https://data.taipei/dataset/detail?id=5a7258c2-5ded-4149-8664-ae10903fe372).
- T01-S08: [facility type-7 JSON](https://wheelroute.gov.taipei/wheelrouteApi/api/facility/Get/7); [existing public interface](https://wheelroute.gov.taipei/).
- T01-S09: [MRT-entry CSV](https://data.taipei/api/dataset/0a3bb422-9eb5-459b-a9d4-138456516183/resource/61792c82-6609-41b2-9775-3a346934826d/download).

#### Completed bounded comparisons

**Method and bounds — predefined before parsing:** test whether inventory fields can support planting eligibility, whether entrance data add information beyond the existing source, and whether entrance-only evidence can support trip selection. Failure to represent a consequential constraint rejects that claim, not the existence of pain. Parse all modest public files rather than choose a convenient sample; this gives exhaustive checks of these snapshots without claiming representative physical inspections. No accuracy tolerance in meters is invented: CRS and ground truth are not established, so no distance/routing result is permitted.

**Planting source test:** S06 returned 2,259 hole rows, 1,308 distinct `TreeHoleID` values and 1,758 distinct JSON objects. Fields are `TreeHoleID, ShapeType, Length, Area, Region, Remark, TWD97X, TWD97Y, UpdDate`; no explicit occupied/empty, approved planting, subsurface constraint or shade field exists. Reproduction: JSON array length; set of ID; set of sorted-key serialized objects. Treating 2,259 rows as planting opportunities is rejected. Even unique IDs are inventory identifiers, not eligible locations. The nonempty attribute/remark interpretation is not validated.

**C03 source comparison:** S07 reproduced 745 unique row IDs, 251 distinct unnormalized park names and 12 districts. All widths/slopes parsed; width range 0.9–19.6 m, slope 0–8%, with 134 zero slopes. A deliberately broad magnitude screen, `100000<X<400000` and `2400000<Y<2900000`, flags ID75 華山公園 entrance 15 (`Y=277120.65`) and ID113 民生公園 entrance 2 (`X=3066305.29`). It tests gross projected-coordinate magnitude, not city-boundary membership or positional precision. Shared coordinates also occur, including 大安森林公園 IDs19/20; identical XY is a verification question, not proof of duplicate entrances.

S08 contained 940 records. Parsing `kname` as `ID_park_entrance` matched every one of the 745 S07 IDs exactly once: all widths/slopes agree; six raw park-name mismatches disappear after trimming trailing whitespace. The remaining 195 records have `width=slope=-1`; these are sentinel-like values, not measured geometry. The two matched anomalies persist geographically: ID75 latitude `2.50634257173676`; ID113 longitude `147.720552618435`. Do not auto-repair them or treat endpoint agreement as corroboration. Park API `X/Y` fields contain names rather than projected numbers. S09's separate 193-row inventory is not reconciled with those 195 records; freshness and coverage differences remain unresolved.

**Trip-task comparison:** S07 offers entrance attributes; S12 already provides site transport and amenities, while S13 provides detailed service locations. S12 lists shade but no accessible toilet; S13 reports accessible toilets and lending. This completed desk comparison refutes the assumption that an accessible-entrance label answers a toileting-dependent park choice. It does not establish the better destination, reachable route, live service or caregiver preference.

**Reproduction boundary:** the structured-resource links and full-file methods above identify the
observed calculations. The initial probe encountered a `TreeID`/`TreeHoleID` parser mismatch;
corrected schema and rerun produced the reported values. No source was replaced by generated
observations. Temporary downloads/helpers are retired after integration; no physical survey is implied.

#### A — Planting and shade field-review prioritization

**Problem, fit and baseline.** Observed local research supports cumulative thermal discomfort along one campus greenway; a separate Taipei road study identifies orientation/vegetation differences in modeled thermal comfort. Neither establishes which neighborhood currently lacks useful shade. S14 supplies a rival mechanism: canopy can impede nighttime ventilation under tested canyon conditions. Therefore tree count or undifferentiated “more trees is cooler” cannot supply the ranking. [T01-S02][T01-S03][T01-S14]

The hypothesized user is a Parks Office planner preparing one street's joint field review before a planting decision. Existing baseline is the tree-information site's inventory/history/hole controls plus authority review and field investigation; map discovery already exists. S15 describes a real operator workflow with community complaints, site inspection, excavation, utility repair, then replanting. This demonstrates an engineering/coordination barrier; it does not prove an information bottleneck or planner demand for software. [T01-S18][T01-S04][T01-S15]

**Bounded decision/action.** Input one street's candidate IDs, dated inventory and a specified daytime exposure concern → distinguish questionable records and missing feasibility/exposure evidence → planner requests targeted arboricultural/road/utility checks → an auditable field-review sheet with responsible authority and reasons. It authorizes investigation, not planting. Existing canopy, surface heat, occupied holes, future tree growth and actual user exposure remain different quantities. S05 requires clearance/visibility considerations before planting; a GIS proximity match cannot replace them. [T01-S05]

**Success and rejection.** Success is fewer unresolved or wrongly eligible sites at the same review effort than the existing map/manual sheet, or lower effort with unchanged expert-reviewed completeness. No public evidence justifies a percentage target. Problem rejection: if the planner already has a complete current queue and delay is entirely approval, utilities or budget, defer a ranking product and retain only a requested export. Data rejection: no verified occupancy, local shade/exposure and engineering constraints means no plantable-site or cooling ranking. **Observed result:** the eligibility-from-holes claim is refuted; field-review preparation remains a hypothesis; local heat concern is supported within studied scope. **Disposition: narrow and continue research**, defer automated shade-equity prioritization.

**Validation, readiness and adoption.** The completed full-file schema/identity test is the smallest decisive test of the naive opportunity count. A next decisive value test would compare the same street review sheet with the existing map/manual process, including occupied holes, duplicate IDs, intersections, narrow sidewalks and repaired utilities; all included decisions require explanation, not an invented pass rate. No practitioner test was possible under the no-contact/no-field constraints. Demonstration is **specified** as an evidence-check sheet; task usability unobserved, decision **insufficient**, civic cooling/equity outcomes unknown. A 100-day pilot requires Parks Office sponsorship, arborist and road/utility coordination, a verified exposure method and maintenance ownership; costs and authorized data access unknown.

**Presentation and next check.** Before: a raw 2,259-row hole count appears actionable. Action: expose repeated IDs and missing occupancy/constraints. After: no eligible count is asserted; the owner sees specific verification questions. Pair this real data example with S15's documented utility dependency, without inventing a location join. **Next executable check:** use S18's public ID/history query to compare one named street's records with its published project/utility account, documenting what the baseline already resolves before seeking additional data.

#### B — Officer accessibility inspection (C03)

**Problem, baseline and authority.** The original NGO account documents entrance barriers, surfaces, slopes and inspection/photo submission, while S11 reports repeated approach-surface complaints and an actual repair response. Historical evidence establishes consequential access problems, not today's count of defects. Existing baseline combines Wheelroute facility/routing labels, park information, field measurement/photos and agency review. The hypothesized user is a district park-access officer preparing a bounded survey; action ownership must follow the actual park/road manager, not automatically the district name. [T01-S10][T01-S11][T01-S08]

**Decision/workflow.** Input a named park and published entrance IDs → compare dated measurements, missing conditions and contradictions → select exact entrances/approaches for verification → produce a survey brief, annotated findings and a proposed correction routed to the responsible unit. This addresses traceability and inspection preparation; it does not remove barriers, certify compliance or redesign crossings.

**Success/rejection and completed evidence.** Success is better identification of independently confirmed inspection-worthy uncertainty, or less preparation effort at equal coverage, versus the existing portal/manual brief. Problem rejection: a sufficient current internal inspection system makes this duplicate work unless a measurable accessibility/effort benefit remains. Data rejection: unreliable identifiers/locations or unexplained units block spatial prioritization; width/slope alone cannot establish compliance because the standard also concerns surfaces, turning, signs and connected paths. [T01-S16]

The completed comparison supports a source-quality exception list and refutes the claim that simply combining two endpoints creates new entrance evidence. It also supports withholding location conclusions for the two anomalies; it does not establish a defect at either physical entrance. **Disposition: continue narrowly** with record/inspection reconciliation; broad deficiency rankings remain unresolved. Numeric general-width or slope comparisons are not violations: terrain exceptions and required assistance matter. No guessed correction is allowed.

**Validation/readiness/adoption.** The full 745-ID comparison is a census of one export, not a sample of park quality. A next pilot should include the two anomalies, shared-XY entrances, an ordinary match and conditional slope/width cases; selection targets distinct failure modes rather than representativeness. Judge correct source reproduction and preservation of uncertainty first, then officer effort/field yield against the baseline; physical tolerances require the surveyor's method. Demo **specified**, task usability unobserved, decision **insufficient**, civic access improvement unknown. Adoption needs the park manager, road authority for approaches, trained access auditors and a correction/update process; repair priority, budget and staff costs are unknown.

**Bounded presentation/next check.** Before: two portals appear to confirm 華山公園 entrance 15. Action: display source lineage and impossible geographic magnitude. After: one correction/inspection question, with no recommended path. **Next executable check:** inspect the official park plan/entrance image for IDs75 and113 and record correspondence or ambiguity; only then investigate CRS and a publisher correction route. External contact is a separate owner-authorized step.

#### C — Caregiver park-trip choice (C03)

**Problem and baseline.** S10/S11 support access friction for mobility-device users; the specific caregiver, recurring trip-planning burden and current workaround remain hypotheses. Existing baseline already offers Wheelroute, park amenity/transport pages and operator service descriptions. The proposed gain is assembling relevant evidence and unresolved conditions for a particular person's needs, not asserting no existing information. Toileting, rest, heat, wheelchair type and assistance can dominate entrance proximity. [T01-S12][T01-S13]

**Decision/workflow and boundaries.** Hypothesized user: caregiver arranging one accompanied daytime visit, without collecting identity or medical details. Input functional requirements and two named destinations → compare published entrance/service information and missing approach evidence → choose a destination for further confirmation or postpone → a dated pre-trip checklist with selected source links. The caregiver controls trip choice, not municipal repair or live elevator availability. A genuine end-to-end recommendation requires verified crossings/surfaces, continuous paths, equipment status and current service conditions; the audited points do not provide these.

**Success/rejection and observed disposition.** Success would be fewer overlooked personally essential conditions and less planning effort than consulting the existing sources, without unsupported “safe/reachable” claims. Problem rejection: the caregiver's familiar route/current tools already solve the task, or the limiting factor is assistance/transport capacity rather than information. Data rejection: any essential continuous-journey condition remains unverified, so withhold a reliable-route recommendation. The completed Sanmin/Guandu desk comparison **supports** a narrower service-evidence checklist; entrance-only trip sufficiency is **refuted**; actual destination suitability and usefulness remain **unresolved**. **Disposition: defer reliable trip choice/routing; narrow the demo to pre-trip evidence.** Absence of caregiver interviews does not refute pain.

**Validation, readiness and adoption.** The smallest completed test compared entrance-only fields against existing site service pages for a toileting-dependent hypothetical case; the requirement is explicitly hypothetical, the source records real. A later task test must include a destination with reported missing amenities, a helpful service page, an anomalous entrance, and an unverified connection. Prefer zero unsupported assurances because one can strand a user; do not turn this into a numerical injury-risk estimate. No actual trip or participant test occurred. Demo checklist **specified**; task completion/usability unknown, decision **insufficient**, civic participation/avoided-trip outcomes unknown. A 100-day service needs operator updates, disability-community co-design, transit status access and accountable maintenance; acquisition route, staffing and cost unknown.

**Presentation/next check.** Before: “accessible entrance nearby” appears sufficient. Action: surface the published missing accessible toilet at Sanmin alongside Guandu's described services and unknown approaches. After: the caregiver has explicit confirmation questions, not a declaration that either park is reachable or preferable. **Next executable check:** attempt one complete public-source chain for a named station–park entrance–toilet visit using Wheelroute and operator plans; record every unsupported segment and stop at the first essential gap. Resume dependable routing only after that gap has a verifiable acquisition route.

#### Integration consequences

Keep C03's canonical decision status **insufficient** and distinguish its officer and caregiver records. Add the observed 745-ID endpoint overlap and shared anomalies to dataset-to-candidate dependencies for 152266, 128414 and Wheelroute. Qualify any comparison implying independent corroboration, navigation, current conditions or added information; retain earlier tree/sidewalk audits as historical unless refreshed. Do not infer 195 versus193 as missing elevators without identity reconciliation. Topic selection remains an owner decision; no new canonical document, implementation, publication or external contact is implied.

[T01-S01]: https://puma.taipei/hackathon
[T01-S02]: https://tdr.lib.ntu.edu.tw/handle/123456789/68930?mode=full
[T01-S03]: https://tdr.lib.ntu.edu.tw/handle/123456789/2404?mode=full
[T01-S04]: https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL004003
[T01-S05]: https://www.dbaweb.tcg.gov.tw/taipeilaw/law_content.aspx?ID=17973
[T01-S06]: https://data.gov.tw/dataset/128274
[T01-S07]: https://data.gov.tw/dataset/152266
[T01-S08]: https://data.taipei/dataset/detail?id=2b58f15a-dec6-4b9d-91be-4eaccfda5ae7
[T01-S09]: https://data.gov.tw/dataset/128414
[T01-S10]: https://sunable.net/2024/01/09/從社區公園看日常生活中的障礙與問題處境/
[T01-S11]: https://pkl.gov.taipei/News_Content.aspx?n=43E05059FCC72525&s=DFB1F83DD2A82601&sms=72544237BBE4C5F6
[T01-S12]: https://play4u.gov.taipei/News_Content.aspx?n=4773608F226124D4&s=E478DAADE7C6A69D&sms=7B56BA5392EB632C
[T01-S13]: https://gd-park.org.tw/guide/4810
[T01-S14]: https://arxiv.org/abs/2301.05766
[T01-S15]: https://pkl.gov.taipei/News_Content.aspx?n=43E05059FCC72525&s=047437A37EE1A80C&sms=72544237BBE4C5F6
[T01-S16]: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070227
[T01-S17]: https://data.gov.tw/license
[T01-S18]: https://geopkl.gov.taipei/

### T02 Public bins and C07 market-bin responsibility audit

Research observation: **2026-10-13**. Public-source research only; no implementation, fieldwork, interview, contact or inference calls. Evidence is freshly inspected unless historical. The citizen bin finder is an existing baseline, not a fourth candidate.

#### Findings and disposition

**Supported:** there are documented service failures beyond a missing map point. Environmental Protection (DEP) acknowledged an improperly sealed bin near Youth Park in 2023; a district meeting recorded Zhengde Village's complaint about recurring overflow in July 2024. These are bounded reported incidents, not citywide prevalence or present-day observations ([T02-S05], [T02-S06]). **Supported:** a municipal sensor pilot already targeted repeated inspection effort; its public page says stage-completed, without publishing comparative performance ([T02-S08]).

**Refuted data assumptions:** rows do not necessarily identify usable individual bins or current market entrances. Downloads reproduce duplicate/aggregate locations and one nonnumeric longitude. Beitou CSV lists Xinshi Street 30; the publisher venue page instead identifies its interim market at Huanggang Road 33 ([T02-S02], [T02-S03], [T02-S04], [T02-S11]). This rejects an unqualified current-location join, not market-related sanitation pain.

**Unresolved:** practitioner value over current practice; preparation-time comparisons, work orders, collection logs and field outcomes are absent. Evidence depth differs: collection has operator-reported effort; placement has an admitted failure and policy controversy; market audit has a historical dispute and reproduced location conflict. Unknown does not mean low civic value.

**Fit:** A placement/access review partially addresses official issue 2; B collection/overflow addresses its dynamic-cleaning branch; C07 addresses market-approach inspection and responsibility, fitting issue 2 or a bounded free topic. C overlaps rat-source prevention but supplies no rat observations or disease-risk evidence. The organizer's historical bin-total and disappearance framing remains attributed; it is not a causal evaluation ([T02-S01]). Topic selection remains an owner decision.

#### Source ledger

All entries retrieved **2026-10-13**. `GET/text`: original-page web retrieval and named-section inspection. `curl/parse`: complete unauthenticated download, normal TLS verification, standard-library parsing through `uv run`. Original publishers or their official mirrors only; readability does not establish reuse rights.

| ID / original source | Inspected content, period and unit | Access, license and limitations / contrary evidence |
| --- | --- | --- |
| [S01 — Organizer, 市政 debug松][T02-S01] | GET/text: issue 2 and rules, current event page; municipal problem framing and simulation policy | Readable. Event complaints activity-only; not retrieved. Page narrative redistribution license unknown. Its statement about nonexistent overflow data cannot establish that no sensor data was ever collected. |
| [S02 — DEP, 臺北市行人專用清潔箱, catalog 121355][T02-S02]; [main CSV][T02-M] | Catalog GET/text; complete 63,540-byte Big5 CSV, 681 rows. Fields district/address/lon/lat/note; no record observation date, asset ID, fullness or schedule | Free; catalog specifies Government Open Data License v1.0. Main-file update 2026-09-30 on Taipei catalog is not a site-survey date. One longitude nonnumeric; see experiment. CRS not established. |
| [S03 — DEP, 景點商圈周邊130點][T02-S03] | curl/parse: 5,396-byte Big5 CSV, 130 rows, same five columns; aggregate site notes | Same dataset license as S02. 120 distinct coordinate strings; notes include multiple places. No independently positioned individual assets. Cross-file real-world overlap unknown. |
| [S04 — Markets Administration, 臺北市傳統市(商)場, catalog 121593][T02-S04]; [CSV][T02-V] | Catalog GET/text and complete 21,668-byte UTF-8 CSV; 47 rows, seven columns: seqno/title/body/created date/address/lon/lat. Creation dates 2012-04-13–2013-09-27 | Free, Government Open Data License v1.0. Catalog says coordinates “84”; entrance geometry absent. All XY numeric/nonblank, but that does not validate positions. Includes commercial buildings/underground shopping, not only food markets. |
| [S05 — DEP, 落實SOP…全面清查, 2023-05-19][T02-S05] | GET/text: incident, investigation and repair-SOP explanation; one Youth Park bin | Department admits unauthorized sealing and restoration, following reported complaints. No event series or current status. DEP site open declaration permits attributed reuse with exceptions ([T02-S14]); no photographs copied. |
| [S06 — Zhongshan District Office, July 2024 cityscape meeting][T02-S06] | GET/PDF text: printed pp.3–4, case 11307 proposal 6; village complaint, district-team response, closure | Actual reported long-term overflow, not measured duration. Closure follows planned inspection/enforcement/education, not an observed recurrence test. Redistribution terms unknown; screenshot retrieval failed, text was inspected. |
| [S07 — Taipei Secretariat, executive meeting 2413, 2026-09-01][T02-S07] | GET/text: report item 1, supplemental report and chair instruction; citywide policy monitoring | Orders analysis of displacement, disposal behavior and costs after bin reduction, plus hotspot/time monitoring and local reporting. No resulting evaluation attached in inspected section. Redistribution terms unknown. |
| [S08 — Taipei Information Technology, 既有人行道清潔箱數位轉型計畫][T02-S08] | GET/text: stage-completed pilot description, page updated 2024-04-10; DEP/vendor sensor management trial | States repeated patrols burden staff and exceptional delays cause overflow. Trial aims are not achieved benefits; no sample, telemetry download, accuracy, maintenance or cost results exposed. License unknown. |
| [S09 — Taipei legal database, FL076512][T02-S09] | GET/text: header/status and clauses 4–6; discontinued 2022-08-24 | Historical assignment/siting/maintenance rules, **not current authority**. Indexed 2015 three-times-daily rule is an older version. Current complete replacement SOP unresolved. Reuse declaration not inspected. |
| [S10 — Taipei legal database, 零售市場管理自治條例 FL004784][T02-S10] | GET/text: current displayed 2022-06-24 revision, articles 13–15 and 21–22; public and privately owned retail markets | Storage, same-day removal, fee and management duties differ from pedestrian-bin use. Statute establishes responsibility, not compliance. Property boundaries/contracts remain case-specific. Reuse declaration not inspected. |
| [S11 — Markets Administration, 北投市場(北投中繼市場)][T02-S11] | GET/text: history/address/hours, updated 2024-09-05 and reviewed 2024-10-15; venue | Publisher describes interim operation from 2022 at Huanggang Road 33, contrary to CSV address. Page does not supply verified entrances; physical operation on retrieval date unobserved. License unknown. |
| [S12 — Markets Administration, environmental issues in Beitou Market][T02-S12] | GET/text: three FAQ answers, 2021-06-01; Xinshi Street outside-market waste and internal cleaning | Agency attributes outside dumping to nearby residents/businesses rather than market vendors. No underlying investigation records; historical attribution, not independently verified culpability. License unknown. |
| [S13 — DEP, 北市清潔箱精準配置…, 2026-08-10][T02-S13] | GET/text from DEP environmental-quality official mirror; residential removals, high-demand siting and enforcement constraints | Department explains local-chief concurrence and staff identification/safety burden. Reports 806 groups/1,612 receptacles at that date; not reproduced asset counts. Recycling alternatives are material-specific, not universal rubbish disposal. Original DEP link timed out; mirror readable. |
| [S14 — DEP website open declaration][T02-S14]; [S15 — Government Open Data License v1.0][T02-S15] | GET/text: scope/exceptions; license rights/attribution/disclaimers | S15 permits redistribution/adaptation with attribution; S14 excludes specified third-party material and does not remove privacy obligations. Do not transfer dataset licensing automatically to unrelated pages. |
| [S16 — DEP official bin lookup][T02-S16]; [public API][T02-A] | curl: HTML shell, referenced app JavaScript and API JSON. 681 serialized records, six comma-separated fields with empty third field | Search/district-filter/map code inspected; no account needed. Live rendered usability untested: in-app browser unavailable. Separate API/software license unknown; matching S02 records inherit no new rights merely from this endpoint. |
| [S17 — DEP organizational duties][T02-S17] | GET/text: Environmental Cleanliness Management Division, district teams and direct team; page updated 2025-02-13 | Current published institutional roles support operator identification. No staffing availability or delegated site-level approvals supplied. DEP site declaration applies subject to exceptions. |

#### Completed bounded evidence comparisons

**Predeclared decision tests:** a useful access audit must add verified operational/access information beyond the existing lookup; placement fails if its apparent gap is a stale/aggregate location. Collection fails on data sufficiency if time-stamped load, collection and resource constraints cannot be observed; an already completed pilot must be checked before proposing duplicate sensing. C07 fails as a current spatial service ranking when venue/entrance or responsibility cannot be resolved. These are claim-specific rejection conditions, not invented performance targets.

**A — inventory versus existing lookup:** downloaded the three CSVs and the lookup's public API; parsed complete files, checked blanks, numeric coordinates, duplicate strings and exact normalized record equality. API records contain an extra empty third field; removing it produces the main CSV's complete ordered content exactly. This is a census of these files, not a street sample. Main file: 680 coordinate-string pairs, one pair shared by two Jiannan Bridge descriptions. Supplement: 120 pairs across 130 rows; zero exact-string intersections with main does **not** establish zero shared physical bins because precision differs. Main row 654, Maokong pothole bus-stop parking location, contains longitude `?121.595369`; numeric conversion fails. Nonblank coordinates are insufficient. Keep the original string and quarantine the record instead of silently repairing it. This narrows the product to source/field reconciliation; it does not show any missing street service ([T02-S02], [T02-S03], [T02-S16]).

**B — proposed sensing versus actual baseline:** compared organizer issue 2 with the original pilot description, current municipal instruction and the main-file schema. A city sensor trial is already documented; none of these inspected resources provides its fullness history, recorded collections, dispatch constraints or comparative result. Thus “sensing has never been tried” is refuted, while “no usable public telemetry established here” is supported. This source-level check is feasible and completed; a real dispatch comparison is infeasible without the missing series and crew constraints ([T02-S01], [T02-S07], [T02-S08]).

**C07 — market coordinate versus publisher operating venue:** deliberately selected Beitou because an original FAQ identified outside-market attribution and redevelopment makes it a difficult temporal case. Compared CSV row 2/address/creation date with the current venue page; addresses differ as above. The source conflict alone is decisive against automatic current service ranking, so no arbitrary radius or nearest-bin distance was computed. This is one purposive counterexample, not an estimated stale-record rate across 47 rows ([T02-S04], [T02-S11], [T02-S12]).

Reproduction uses the exact linked CSV/API resources, complete quoted-field-aware parses, coordinate-string sets and ordered normalized record comparison described above. Temporary raw downloads/helpers are retired after durable integration. SHA256 main `ff3cf5528c057958f89871aa5300fc633b02d0f7b37131ab29d5ddc2f8e2370d`; supplement `47b1ddfb4f0ab4d5e57afab538f71da3d41d22e59c984bdd9c10b4248223b066`; markets `460f0ab33b3888c9e2fd67ab27b7be29c2653b909df912f8210f473d3565ced5`; lookup API `793f93c30ef4f1cf7ae5b0703111b603bff34f5e129ac36673629335a073b8ba`. Initial Python HTTPS requests failed certificate-chain validation; normal `curl` succeeded without disabling TLS. Downloads are real publisher records; no modeled or simulated observations were generated.

#### A — Placement and usable access

**Problem/user/decision.** Pedestrians can be inconvenienced even when a mapped bin exists, as the admitted sealing incident demonstrates. The proposed user is a district sanitation supervisor reviewing a specific reported inaccessible or absent bin, not an observed adopter. Trigger: a location discrepancy or access complaint. Decision: verify/restore an existing asset, correct a map, or request a siting review. Actual internal preparation difficulty and frequency remain hypotheses. The published district-team/direct-team roles distinguish cleaning from repair/installation ([T02-S05], [T02-S17]).

**Exact baseline and bottleneck.** Official lookup already has keyword, district and map functionality; catalog documentation also points to TaipeiPASS nearby bins, which was not operated here ([T02-S02], [T02-S16]). Current policy targets busy commercial/tourist areas and includes local concurrence for residential reductions ([T02-S13]). The discontinued rule cannot establish today's siting approval sequence, spacing or clearance threshold. Information may resolve a stale record; sidewalk space, local objection and maintenance capacity may dominate actual installation.

**Success/rejection/disposition.** Success would be a supervisor producing the correct verify/repair/siting-review choice with fewer unresolved assets or less preparation effort than lookup plus current manual review, without treating uncertainty as absence. Problem rejection: existing practice already resolves the same cases adequately, or no executable action changes; **unresolved**, requiring an actual paired-task comparison. Data rejection: essential assets/approaches remain ambiguous; **supported** for automatic coverage rankings by the parse and aggregate-location results. **Continue narrowly** as a verification checklist, defer placement optimization.

**Workflow/dependencies/claims.** One complaint location → match source records and flag duplicate/malformed/status uncertainty → supervisor assigns a site check through normal authority → dated confirmed asset/access record and selected action. Essential: current asset identifier, observed condition, safe walking approach/crossing, public-space responsibility, current approval rules. Existing CSV supplies only candidate locations; usable status and route joins are missing. S02/S03 licensing supports attributed inventory reuse, not unobserved service claims.

**Validation/readiness/adoption.** File comparison is complete. The next decisive practical comparison should cover each observed failure type—malformed coordinate, duplicate/aggregate site, sealed/damaged asset and road-side/crossing ambiguity—rather than ten convenient points. Withhold site recommendations in unresolved cases because a false gap can divert installation resources; compare effort and unresolved-case errors without fabricating a success percentage. Demonstration **specified** for a discrepancy-review task; usability untested, decision **insufficient**, civic effects unknown. A 100-day path requires DEP inventory custody, current SOP and field-validation capacity; road expertise, costs and available staff are unknown, to resolve from the current procedure and a pilot work breakdown.

**Before/action/after presentation.** Real Maokong row: before, an unqualified map could rank a nonnumeric point; action, the supervisor sees the raw defect and requests verification; after, the record is withheld from a siting claim. Only detection/withholding occurred here, not a municipal correction. **Next executable check:** inspect the currently published DEP bin-special-section documents for the replacement siting/repair procedure and asset-status fields; if absent, retain the SOP gap and prepare an owner-reviewed information request, without sending it.

#### B — Collection and overflow response

**Problem/user/decision.** Recurring overflow is reported in a village meeting, and the pilot operator explicitly describes inspection effort. Proposed user: district shift supervisor deciding whether to advance a collection/patrol at one repeatedly overflowing cluster. Existing accounts establish reported difficulty, not a validated new-tool need ([T02-S06], [T02-S08]).

**Baseline/bottleneck.** Published responses combine routine inspection, extra hotspot collection, local notification and enforcement; the sensor pilot already targets load visibility. The July case was administratively closed after a response, without a published before/after overflow measure. A modern dashboard must compete with that whole process, not an imaginary city without sensing. Unauthorized household waste, tampering, short surges, crew travel and occupational safety are rival constraints. DEP's August statement describes identification and confrontation difficulties; sensors alone do not remove them ([T02-S06], [T02-S07], [T02-S08], [T02-S13]).

**Success/rejection/disposition.** Success: earlier correct response or fewer avoidable inspections than the actual patrol baseline, with no missed overflow/safety cases or infeasible staffing. Problem rejection: latency is dominated by unavailable crews or existing notifications already suffice; **unresolved**. Data rejection: no synchronized fullness/collection/crew record; **supported within inspected public sources**, not proof the city lacks records. **Defer real dispatch/optimization**; retain only a disclosed scenario demonstrator until trial evidence is available.

**Workflow/dependencies/claims.** Dated load/overflow observation and current crew position/availability → compare proposed extra trip with planned patrol and other obligations → authorized supervisor issues or declines dispatch → logged actual collection/response time and independently checked condition. Required: stable asset IDs, sensor missingness/false readings, collection timestamps, travel/service time, legal shifts and safety restrictions. None can be reconstructed from MRT entries, citywide tonnage or a location CSV. Telemetry reuse rights, retention and access are unknown.

**Validation/readiness/adoption.** Completed source comparison rejects novelty-by-sensor-existence. The smallest consequential performance experiment needs a baseline patrol period and matched proposed decisions at one real hotspot, including rapid household-waste loading, sensor outage/tampering and a no-available-crew case. Observe false dispatches, missed overflow and overtime together; no defensible numeric tolerance or duration can be set without actual load cadence and staffing. Historical replay cannot prove an unexecuted trip's result. Demonstration **specified only with labeled simulated loads/crews**; no simulation was run. Decision **insufficient**, civic outcomes unknown. DEP must own dispatch authority and provide operations/safety expertise; hardware maintenance, connectivity, procurement, labor cost and pilot status within 100 days remain unknown.

**Before/action/after presentation.** Use the real Zhengde complaint as context, clearly separate an optional simulated holiday overflow/crew availability panel, then show a supervisor's proposed response and the condition/time evidence needed afterward. Do not invent improved streets or claim case closure proves improvement. **Next executable check:** inspect Smart City Taipei's pilot-results/download references for site count, comparison design and retained load/collection series; defer dispatch if only the descriptive page is available.

#### T02 C07 — Market approaches and public/market/private responsibility

**Problem/user/decision.** The Beitou FAQ documents an attribution dispute: nearby waste was assigned to surrounding residents/businesses rather than market vendors. It motivates responsibility-aware inspection, while the agency's attribution remains uncorroborated. Proposed user: district sanitation supervisor preparing one joint boundary inspection with the market manager. Trigger: reported waste at a market approach. Decision: verify venue/entrance and route the issue to pedestrian-bin service, market waste handling or illegal-dumping review—not infer responsibility from proximity ([T02-S12]).

**Baseline/authority/bottleneck.** Baseline is the market publisher's venue page plus market management rules and ordinary DEP reporting. Articles 13–15 assign public-market user/container/removal and autonomous-organization hygiene duties under market supervision; articles 21–22 establish private-market committee duties and applicable stall obligations ([T02-S10]). Actual cleaning contracts, premises boundaries and waste origin remain unobserved. A sanitation supervisor cannot unilaterally rewrite a market association's contract or turn a pedestrian bin into trade-waste disposal.

**Success/rejection/disposition.** Success: a verified, correctly routed inspection case that reduces avoidable clarification or wrong-owner referrals compared with venue page plus manual rules lookup. Problem rejection: the boundary/current operator is already clear and a map adds no actionable information; **unresolved**, not disproved by absent practitioner testimony. Data rejection: a stale venue point or unidentified entrance is treated as a service gap; **supported** by Beitou. **Narrow C07** to current-site/responsibility reconciliation; defer ranked service gaps and installation recommendations.

**Workflow/dependencies/claims.** One reported approach + current venue page → reconcile old versus operating address, identify premises/public street and waste type → supervisor records the appropriate joint inspection/referral → agreed boundary/owner and dated observation, or explicit unresolved ownership. Essential: verified operating location and entrances, opening times, bin presence/status, premises boundary, contracts and collection duty. Market CSV gives context, not these joins. Attribute sources under their licenses; exclude incidental personal information from market descriptions. No rat-risk or market-causes-dumping inference is allowed.

**Validation/readiness/adoption.** Completed one deliberate hard-case comparison supports withholding Beitou's old point. Next practical sample must include its current interim entrance/public road boundary and a privately owned market to test the different authority branch; select for differing duties, not representativeness. Have the authorized operators reconcile each disputed assignment before evaluating time saved; no arbitrary radius, agreement target or extrapolated citywide failure rate. Demonstration **specified** as a source-conflict/inspection worksheet; task usability untested, decision **insufficient**, civic outcomes unknown. A 100-day pilot needs Markets Administration, DEP, association/committee and possibly contractor participation; boundary records, expertise, availability and cost unknown.

**Before/action/after presentation.** Before: CSV row 2 places “Beitou Market” at Xinshi Street 30. Action: compare the original venue page identifying Huanggang Road 33 and quarantine the old join. After: produce a current-location verification case with responsibility unresolved, rather than “no nearby bin.” This source correction is observed; field agreement and cleaner surroundings are not. **Next executable check:** inspect the Beitou redevelopment/current-site public plan for labeled interim entrances and premises boundary, then check the nearest relevant bin descriptions without interpreting missing points as absence.

#### Integration controls and next decision

Update dependent bin/C07 claims in the canonical source audit, dataset-to-candidate index, readiness and queue: preserve the historical 681/130/47 counts; add the malformed longitude, lookup equivalence, Beitou location conflict, discontinued SOP and existing pilot. Do not count all 811 bin rows as individual assets or all 47 entries as current food-market entrances. MRT gate volumes are not street footfall; complaints/enforcement counts are selected reports, not prevalence. Bin removal may displace waste, deter misuse or concentrate load; the current meeting explicitly requests analysis, so no causal direction is established ([T02-S07]).

Next priority: current operational procedure/pilot results, then verified market boundaries. No additional discovery worker is needed. Practitioner value awaits separately authorized observation; no topic selection, implementation or external request follows from this report.

[T02-S01]: https://puma.taipei/hackathon
[T02-S02]: https://data.gov.tw/dataset/121355
[T02-M]: https://data.taipei/api/dataset/a835f3ba-7f50-4b0d-91a6-9df128632d1c/resource/267d550f-c6ec-46e0-b8af-fd5a464eb098/download
[T02-S03]: https://data.taipei/api/dataset/a835f3ba-7f50-4b0d-91a6-9df128632d1c/resource/2030d728-9597-437d-81a4-cf2a44c7f114/download
[T02-S04]: https://data.gov.tw/dataset/121593
[T02-V]: https://data.taipei/api/dataset/89bebb3a-990d-4070-bd67-631a575f6d4a/resource/35acfce1-2c4d-4c70-aa75-601cdab2b3f7/download
[T02-S05]: https://www.dep.gov.taipei/News_Content.aspx?n=CB6D5C560DE4D2DD&s=CA5F41975DA9DE32&sms=72544237BBE4C5F6
[T02-S06]: https://www-ws.gov.taipei/Download.ashx?icon=.pdf&n=6Ie65YyX5biC5Lit5bGx5Y2A5YWs5omAMTEz5bm0N%2BaciOS7veW4guWuueacg%2BWgsS3mnIPorbDntIDpjIQucGRm&u=LzAwMS9VcGxvYWQvMzEzL3JlbGZpbGUvMTQyMjMvOTI2MzUxNi82YzNlOTYwNy0yMWUzLTQ5YmMtODc0Yy03NThkMWI3MjYzOTQucGRm
[T02-S07]: https://sec.gov.taipei/News_Content.aspx?n=0661423027099106&s=93E36C4B3062A2CA&sms=14AEF9A8536E3B5E
[T02-S08]: https://smartcity.taipei/News_Content.aspx?n=6986545C4A2C217F&s=AB5CE633E7AEE89B&sms=A5A97EC540EAA0BA
[T02-S09]: https://laws.gov.taipei/Law/LawSearch/LawArticleContent/FL076512
[T02-S10]: https://laws.gov.taipei/Law/LawSearch/LawArticleContent/FL004784
[T02-S11]: https://www.tcma.gov.taipei/News_Content.aspx?n=1A4C7120ABFD0F9F&s=0D2E39A27F365146&sms=26C5BF03E7963F4E
[T02-S12]: https://english.tcma.gov.taipei/News_Content.aspx?n=0D1F8364A44653BE&s=803AF208DF369701&sms=2DCE396EE03A7391
[T02-S13]: https://www.tldep.gov.taipei/Public/News/TpeDep_Detail.aspx?SN=9686320
[T02-S14]: https://www.dep.gov.taipei/News_Content.aspx?n=E184C1C509CAC820&sms=D3F1D842A6D2B9AD&s=CC1AB747D78F7D15
[T02-S15]: https://data.gov.tw/license
[T02-S16]: https://www.dep-trash-can.gov.taipei/
[T02-A]: https://www.dep-trash-can.gov.taipei:17443/i/tc
[T02-S17]: https://www.dep.gov.taipei/cp.aspx?n=DD34C671F97B74E5

### T03 Official rats: intake versus inspectable source control

Research observation: **2026-10-13**, Taipei time. Evidence depth is unequal: public intake and source schemas were directly inspected; Taipei practitioner effort, inspection outcomes and adoption were not observed.
#### Findings and disposition

**Evidence:** the organizer requests a rat-risk/propagation map combining food businesses, pipes, collection schedules and reports. Its assertions about reactive treatment and breeding windows remain organizer claims ([R01](https://puma.taipei/hackathon#issue-3)). Existing Taipei services already cover reporting and professional environmental diagnosis. Consequently, intake partially fits the official topic; source-control follow-up fits directly and overlaps T02 waste.

**Supported:** people publicly report intrusive sightings and environmental concerns; professional source inspection has plausible mechanisms and published operational precedents. **Refuted for the inspected starter resources:** a geographically resolved food/pipe/complaint training set is already available. **Unresolved:** practitioners repeatedly lose consequential information between inspection, assignment, repair and reinspection; an additional tool improves that process. Absence of public workflow evidence does not refute this pain.

**Inference:** narrow to an evidence-and-responsibility packet, conditional on an actual operator comparison. Defer another standalone reporting map because substantial intake functionality already exists. Reject complaint-density disease, abundance and propagation predictions from this source set. No weather score, rodenticide recommendation, business accusation or inferred infestation is justified.

#### Pain, competing explanations and outcome evidence

Local first-hand submissions on [Rat Radar R02](https://ratdar.taipei/reports) include accounts of indoor intrusion, droppings, noise and environmental observations. These are reported experiences, not verified frequency, diagnosis or representative practitioner interviews.

Original Vancouver complaint-content research shows why this distinction matters: many callers sought action on broader waste/property conditions rather than rats alone. Its analyzed complaints excluded dead-animal-only requests and unrelated entries; the raw municipal material cannot be shared by the authors ([R07](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296920)).

Contrary evidence prevents declaring complaints useless. Chicago researchers found correspondence with trapping success and uncontained garbage, but selected high-complaint trapping alleys within sampled communities. That supports locally validated screening, not an unconditional Taipei prevalence conversion ([R08](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2018.00189/full)). Sydney's original lockdown study compared captures, bait-station visits and complaints; these indicators changed differently. Food availability and detectability can change sightings or capture probability without a matching complaint trend ([R09](https://www.nature.com/articles/s41598-021-92301-0)).

Taiwan evidence is more relevant operationally but not a Taipei efficacy trial. The Taichung-port study distinguishes capture patterns from parasite/serology patterns and discusses winter food scarcity and bait attractiveness as explanations for capture variation. Therefore seasonality is measure-specific, not a single breeding-calendar multiplier ([R10](https://www.cdc.gov.tw/Uploads/ad9f3604-06a2-45b3-9e31-39b5461152b3.pdf)). Keelung's original operator/researcher study documents unsuccessful short reactive control, subsequent inspection-guided environmental repairs, contracts and broader responsibility; it also changed trapping/control frequency, access and equipment. Its favorable monitoring results cannot isolate software or source removal from the combined intervention. Rain affected outdoor control choices, demonstrating an operational weather constraint rather than a validated daily predictor ([R11](https://www.cdc.gov.tw/Uploads/df319391-af7a-41fe-a595-5d39cb2996f2.pdf)).

New York's published evaluation supplies a different measured outcome: repeated property inspections found declining active rat signs after a bundled neighborhood program. It was an operator evaluation without directly comparable contemporaneous inspection controls, did not record owners' specific remediation, and omitted underground populations. It supports measuring independent signs and enforcement together, not attributing improvement to a map ([R12](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6137a1.htm)).

**Hypotheses requiring local tests:** media attention, reporting access, renter/owner resources, construction displacement, food competition, species behavior, trap placement and inspection effort can rival a simple food-density explanation. Pipe presence is not a defect, open food access or confirmed travel route. A local historical market survey exists, but is dated and explicitly restricts outward research use; it is not a current public prediction dataset ([R13](https://www.cdc.gov.tw/Uploads/files/479a34c3-b0ff-4444-834f-ceccd8427fcc.pdf)).

#### Workflow A — Resident sighting intake and appropriate referral

**Problem/user/decision.** A resident encountering rats needs the appropriate existing service and enough information to request it. The affected residents are evidenced only through public self-reports; difficulty completing referral is **hypothesized**. Bound the task to one Taipei public-road sighting or apartment common-area problem, at the time of reporting. The resident can report and supply facts; they cannot order inspections, repair a neighbor's building or apply municipal enforcement.

**Exact baseline.** Rat Radar already provides a report list, pending/approved distinctions, CSV export and a review process with optional 1999 follow-through. Taipei's road FAQ explicitly routes public-road reports to 1999 and describes DEP field response ([R03](https://dahr.gov.taipei/News_Content.aspx?n=D037A6FEDF678C70&s=919F8A3496326CC5&sms=87415A8B9CE81B16)). Apartment requests use a downloadable application sent by email, fax or post. Current forms allow applications without a committee when at least half the residents, including tenants, consent. This corrects the older committee-only exclusion lead; gathering consent remains a real process requirement ([R04](https://www.dep.gov.taipei/News_Content.aspx?n=ACEFA960B5A4ACD7&s=BD28B89F7715FACD&sms=87415A8B9CE81B16)). These procedures establish available routes, not successful access or resident satisfaction; user effort remains unobserved.

**Success fixed before source parsing.** The candidate must help the resident complete an appropriate, field-complete referral with less effort than these exact routes, without losing uncertainty, privacy or consent. Observe completion, omitted essential fields, corrections and time; do not choose a percentage improvement without baseline timing. A problem rejection is no consequential failure left after using the existing route: **unresolved** for effort, with substantial duplication **supported**. A data rejection is inability to establish permission for republication or distinguish unverified/poison/non-Taipei submissions: reuse permission remains **unresolved**, and treating the export as verified Taipei infestations is **refuted**.

**Input → assessment → action → output.** The resident supplies a location jurisdiction, observed time and factual description; checks public road versus apartment common area and availability of consent; then chooses the official service. Observable output is a correctly prepared request or an identified missing prerequisite. Submission is outside this research. A returned case number would demonstrate receipt only; closure would not demonstrate elimination.

**Dependencies/claims.** Essential dependencies are current service instructions, required fields, jurisdiction and privacy terms. An optional map of other people's reports requires separate redistribution clearance. Weather, food-business density and pipe networks are unnecessary for this decision.

**Completed smallest comparison.** The researcher compared every field in the public export with the road FAQ and all three current ODT documents. The export lacks an official case identifier and inspection/remediation/reinspection fields; its status label is not a completed service record. The application already captures community identity/address, representative contact and main sighting places; the attachment introduces collective consent. This exhaustive source-field comparison is justified by a redundancy question, not a population estimate. Difficult cases inspected in the specifications were public road, committee-run building, no-committee building, pending report and poison report. No invented error tolerance was used: an incorrect authority or false verification claim would invalidate that case's recommendation.

**Readiness/adoption.** Demonstration=`specified` as the above written hypothetical task; decision=`insufficient`; task usability untested; baseline gain and civic outcomes unknown. Disposition: **defer standalone intake**, retain a narrowly justified navigation improvement only if a later observed failure warrants it. Within 100 days DEP must own instructions and receipt; service capacity, accessible alternatives, maintenance cost and consent-related exclusion remain unknown. More reports could increase workload without increasing remediation.

**Before/action/after example (simulated).** Before: an apartment resident has a sighting but no committee. Action: the packet points to the current consent attachment and the existing service rather than inventing a citywide risk ranking. After: the resident understands the prerequisite and correct route; no application, inspection or improvement is claimed. **Next check:** use R04's current application/QA in a supervised task comparison with a consenting resident, recording whether anything consequential fails; external recruitment/contact needs separate authorization.

#### Workflow B — Inspector source findings, ownership and reinspection

**Problem/user/decision.** Hypothesized decision owner: a DEP inspector coordinating one accepted community case and its adjacent public frontage through one inspection-and-recheck cycle. The bounded decision is which *observed condition* can be corrected now, by whom, and what needs a referral or repair schedule. Actual Taipei case-coordination difficulty remains unvalidated. Keelung supplies observed analogous remediation difficulty; it does not prove Taipei staff need another system.

**Baseline/authority.** Taipei's professional diagnosis already examines signs, entry holes, food management and clutter and provides recommendations ([R05](https://www.dep.gov.taipei/News_Content.aspx?n=CB6D5C560DE4D2DD&s=DE3C4D1F2B592777&sms=72544237BBE4C5F6)). The May 19 municipal minutes require joint inspection records and rechecks, source management and agency responsibility. DEP handles environmental inspection; businesses/property managers control their storage/repairs; market, park and district managers act within their properties; Sewerage Systems Office and Hydraulic Engineering Office have different sewer networks. Hoarding-house intervention requires health/legal determination and multiple agencies, not an algorithmic order ([R06](https://sec.gov.taipei/News_Content.aspx?n=0661423027099106&s=163448944F51CBB9&sms=14AEF9A8536E3B5E)). The exact internal case system and field form are unknown. Compare against those artifacts before proposing replacement; official demands do not prove staff failed to comply.

**Success and rejection, fixed before parsing.** Success would be fewer missed actionable conditions or less time assigning and verifying the same conditions than the current inspection record, without false attribution or unauthorized work. The problem rejection is that the current form already supports this task, or delay comes solely from repair funding/access/capacity: **unresolved**, so do not select implementation. Data rejection is absence of linked site observations, intervention owner/date and repeat observation: **supported for the inspected public bundle**, requiring deferral of real decision support. An alternative public source is still possible; this is not proof city agencies lack records.

**Input → assessment → action → output.** Inputs are dated professional observations of active signs and accessible food/harborage/entry defects, site access, property/network responsibility and prior actions. The inspector distinguishes evidence from suspected cause, checks which owner can act, and issues a documented referral/recommendation under existing authority. Observable output is an assigned correction with acknowledgment, followed by a comparable reinspection recording correction, persistent signs or inaccessible areas. Do not tell the public to enter pipes, handle rats or choose poison from a report map.

**Dependencies and claim limits.** Required: stable site/case IDs; inspection time, method, effort, species uncertainty and inaccessible areas; condition evidence; responsible party; permitted action; completion evidence; reinspection protocol. A zero-report area needs independent inspection, not a zero-risk label. Pipe geometry would help locate a confirmed infrastructure problem only after a verified network join. Independent repeated signs/capture indices and comparable untreated or staggered sites are needed to study outcomes; reduced complaints alone cannot establish prevalence or disease reduction.

**Completed smallest experiment and exit.** Full-file source parsing tested whether the organizer bundle could support the above chain. Food data is one citywide record; pipe data contains identifiers/topology but no coordinates; public complaint categories contain no literal mouse/vector category, address or inspection result. No observed field establishes a defect-to-repair-to-recheck link. Results reject a real priority-ranking demo from those files. This whole-schema test resolves a structural dependency; sampling more rows cannot supply missing columns. Difficult cases explicitly considered were mismatched storm/sewage networks, no-complaint sites, unresolved property owner, inaccessible subsurface habitat and repeated/poison submissions. Field comparison remains infeasible without the current internal form and linked cases; no accuracy threshold was invented.

**Disposition/readiness/adoption.** Continue **research on the inspection handoff**, defer actual prioritization. Demonstration=`specified` only for a disclosed synthetic condition/owner/recheck packet; decision=`insufficient`. Task completion, usefulness and civic improvement are separate unobserved outcomes. A 100-day path requires DEP sponsorship, existing-form access, property consent, relevant infrastructure authorities and qualified pest/repair expertise. Staff hours, travel, repairs, contractor budgets and cross-agency integration costs are unknown. Coordination may help an information bottleneck; it cannot grant access or pay for structural repairs.

**Before/action/after example (simulated).** Before: an inspector has independently observed an open food-waste container and a nearby damaged drain cover; no claim identifies where rats originate. Action: storage correction goes to the property operator, while the cover is referred only after determining its network/owner; a recheck remains open. After: two accountable actions and an explicit evidence gap replace an undifferentiated hotspot. This demonstrates accountability logic, not observed remediation. **Executable next check:** inspect the first available current Taipei joint-inspection/recheck form or published anonymized case and test for condition → owner → completion → reinspection linkage. If no public artifact exists, ask the owner to authorize a narrowly scoped DEP information request; do not fill the gap with complaint-derived labels.

#### Compact source ledger

All entries retrieved **2026-10-13**. `Web` means original page body opened, not search snippets; `curl/parse` means current bytes and local standard-library parsing. Research figures below are described qualitatively unless locally reproduced.

| ID / exact source and publisher | Inspected material, period/unit and access | License/redistribution; limits and contrary evidence |
| --- | --- | --- |
| R01 [市政 debug松, issue 3 and rules](https://puma.taipei/hackathon), organizer | curl HTML text: rat prompt, source links, simulation disclosure and 100-day guidance; contest scenario | Reuse license unknown; event-only feedback restricted. Assertions are organizer framing, not confirmed civic causation. |
| R02 [Reports](https://ratdar.taipei/reports), [export](https://ratdar.taipei/reports/export), [transparency](https://ratdar.taipei/transparency), Rat Radar operator | Web plus complete in-memory CSV parse: **1,429 rows**, **1,410 sightings/19 poison**, **1,373 reviewed/3 sent to 1999/53 pending**. Fields: time, type, location, status, description, photo URL, latitude/longitude. Live mixed-city submissions; no raw records persisted | No explicit reuse license found on inspected pages. Operator describes AI/image plus volunteer review; not professional inspection. Aggregate export counts reproduced, not unique animals/events. No intervention outcomes. |
| R03 [Public-road rat assistance FAQ](https://dahr.gov.taipei/News_Content.aspx?n=D037A6FEDF678C70&s=919F8A3496326CC5&sms=87415A8B9CE81B16), DEP content on city agency site | Web main answer; updated 2026-09-23; Taipei public roads, 1999/field response | Page has government-open-declaration link; specific terms not established here. Process only; response timing/results unknown. |
| R04 [Community service FAQ and attachments](https://www.dep.gov.taipei/News_Content.aspx?n=ACEFA960B5A4ACD7&s=BD28B89F7715FACD&sms=87415A8B9CE81B16), DEP | Web/curl; three original ODT files unzipped and `content.xml` paragraphs read: application, consent attachment, QA; current page 2026-09-23. Exact originals: [application][T03-R04-app], [consent attachment][T03-R04-consent], [QA][T03-R04-qa] | Blank official forms, no filled personal records collected. Specific redistribution grant unknown; cite/link rather than republish form. Current no-committee consent route contradicts an older exclusion lead. |
| R05 [Community rat-detective launch](https://www.dep.gov.taipei/News_Content.aspx?n=CB6D5C560DE4D2DD&s=DE3C4D1F2B592777&sms=72544237BBE4C5F6), DEP | Web diagnosis/service paragraphs; issued 2026-05-13, Taipei communities | Specific license unknown. Agency's efficacy claims are not independently evaluated; initial committee wording superseded by R04. |
| R06 [Municipal meeting 2398](https://sec.gov.taipei/News_Content.aspx?n=0661423027099106&s=163448944F51CBB9&sms=14AEF9A8536E3B5E), Taipei Secretariat | Web rat-control report and directives, meeting 2026-05-19; city/agency responsibilities | Government declaration linked, terms not established. Decisions establish duties, not completion, prevalence or practitioner pain. |
| R07 [Lee et al., Resident motivations](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296920), PLOS ONE, 2024 | Web methods/results/discussion/data statement; Vancouver 2014–May 2020 complaint texts and postal areas; qualitative coding | Article CC BY; underlying city data expressly unavailable for author redistribution. Not a representative Taipei needs survey; municipal grant disclosed. |
| R08 [Murray et al., Public complaints reflect relative abundance](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2018.00189/full), Frontiers, 2018 | curl full methods/results/discussion/license; Chicago complaint history and 2018 alley trapping/community aggregates | Article CC BY; raw operational data reuse not separately audited. High-complaint alley selection limits inference; no Taipei validation. |
| R09 [Bedoya-Pérez et al., COVID19 restrictions](https://www.nature.com/articles/s41598-021-92301-0), Scientific Reports, 2021 | Web methods/results/discussion; Sydney Oct 2019–July 2020; trap/day, station visits, suburb complaints | Open-access designation observed; exact license version/raw-data permission not verified. Changing station deployment and food detectability complicate abundance interpretation. |
| R10 [Taichung port surveillance 2017–2020 PDF](https://www.cdc.gov.tw/Uploads/ad9f3604-06a2-45b3-9e31-39b5461152b3.pdf), Taiwan CDC authors, 2023 | Official viewer → embedded PDF, curl + pdftotext; methods, seasonal tables and discussion; fixed outdoor port sites/quarter | Specific article redistribution license unknown; third-party map credited. Port sampling, bait attraction and species mix limit Taipei transfer; not a treatment trial. |
| R11 [Keelung project management 2017–2023 PDF](https://www.cdc.gov.tw/Uploads/df319391-af7a-41fe-a595-5d39cb2996f2.pdf), CDC/port-company authors, 2025 | Same PDF method; pp. 213–218 methods, stages, capture table, condition/action examples and discussion | Specific reuse license unknown. Operators coauthor; no concurrent control; frequency, access and treatment changed. Independently collected monitoring is distinct from contractor kills but not independent causal evaluation. |
| R12 [Neighborhood program evaluation](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6137a1.htm), NYC health authors/CDC MMWR, 2012 | Web inspection protocol, results/table and limitations; Bronx properties, Dec 2007–Aug 2009 | Exact reuse statement not inspected. Bundled enforcement/education/inspection; no equivalent inspection control and no subsurface evaluation. Published directional outcome, not reproduced causal estimate. |
| R13 [DOH100-DC-2002 metro survey](https://www.cdc.gov.tw/Uploads/files/479a34c3-b0ff-4444-834f-ceccd8427fcc.pdf), CDC research group, 2011 | curl/PDF text: cover, methods pp. 10 onward and discussion; historical selected markets/night markets including Taipei | Cover requires prior agency consent for outward research results; **do not publish results or repurpose as open labels**. No disease figures reproduced here. Purposive historical sites cannot validate current Taipei complaints. |
| R14 [Food-business count catalog](https://data.taipei/dataset/detail?id=9431f450-57d6-4c23-aca6-0ff50de49f0d), Health Department; [exact CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=2227c204-5f9f-4b20-8c6d-c6048eab6475) | Web + full parse: 80 bytes Big5, **one row**, five fields, citywide count **94,828**; file 2025-06-03, no observation-period column | Catalog says public/free; links R17. Counts registrations, not accessible food, operating restaurants or local density. |
| R15 [Sewage pipes catalog](https://data.taipei/dataset/detail?id=af1e6e42-5ffc-4be0-983f-51c03d5d1b17), Sewerage Systems Office; [CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=88157465-4794-41a2-a409-6180b3952f6b) | Web + full UTF-8 parse: **77,603 rows**, nine fields: city/code, pipe ID, two manhole IDs, length, two elevations, completion date; file 2026-08-27 | Public/free, links R17; no geometry, defect/inspection date or rodents. Completion date is construction, not observed condition. Stormwater manholes are not a verified join. |
| R16 [Complaint categories catalog](https://data.taipei/dataset/detail?id=cb423c17-88eb-4231-a725-f1b93247d1bf), RDEC; [11509 CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=b57a0fa8-9507-438b-b2e1-676829a72aff) | Web + full UTF-8 parse: **42,674 rows**, eight columns: case ID, main/subcategory, agency/section, receipt/delivery/closure dates. Zero category-field matches for 鼠/病媒 | Public/free, links R17. No address/narrative/XY or verified outcome. Category search does not prove no rat cases hidden inside broader categories; resource label is not exact receipt period. |
| R18 [抓捕鼠隻 execution results](https://www.dep.gov.taipei/News_Content.aspx?n=A99BC479D1AE0CB5&s=22CDDBD186F821E9&sms=139B136FD62F7F66), DEP | Web complete main content: April–August 2026 citywide aggregate captures, cage placements and bait quantities; updated 2026-09-15 | Specific reuse license unknown. No site/species/trap-night or before/after record; aggregate activity cannot resolve Workflow B. |
| R17 [Taipei government data terms](https://data.taipei/rule), Information Department | Web rights, attribution, version and disclaimer sections | Page identifies first edition, permits attributed reuse/reproduction/derivatives and describes CC BY 4.0 compatibility. Catalog labels R14–16 only as public; preserve publisher attribution and unresolved resource-specific exceptions rather than infer all websites share this license. |

#### Reproducibility and integration boundary

L01 discovery was reviewed; only independently reopened original sources were used. Its inaccessible studies remain leads.

Local aggregate counts above were reproduced through curl GET, UTF-8-sig/Big5 decoding and complete `csv.DictReader` parsing. ODT forms were unzipped and their `content.xml` paragraphs inspected; CDC PDFs were read with `pdftotext`. Temporary source/helper files are retired after durable integration. No public citizen payload was saved. R04 attachment restrictions are essential to any intake summary; R13 use restriction travels with that historical lead.

Coordinator integration should qualify the existing rats readiness entry, R02 notes and dataset-to-candidate interpretations for food/pipes/complaints. Retain the historical source observations and candidate identity; do not upgrade decision readiness, imply the official prompt is wholly solved, or silently select a topic. The consequential next source check is the current Taipei inspection/recheck artifact in Workflow B; no additional general data discovery is necessary before resolving that gap.

[T03-R04-app]: https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvMzYzL3JlbGZpbGUvMzE4MjAvOTU3Njk2Mi84Njg4NTY3OC1mYzkwLTQ5NzktYWIwMy1kYWE0MDRkZDIwNzUub2R0&n=MDEu6Ie65YyX5biC56S%2b5Y2A6byg6aGe5YG16Ziy5pyN5YuZLeeUs%2biri%2bihqC5vZHQ%3d&icon=..odt

[T03-R04-consent]: https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvMzYzL3JlbGZpbGUvMzE4MjAvOTU3Njk2Mi9hOTEyOGNlYi02Yzk2LTQ2NmYtODc3NC1lMmRlNTA3N2VhM2Mub2R0&n=MDIu56S%2b5Y2A6byg6aGe5YG16Ziy5pyN5YuZ55Sz6KuL6KGoLemZhOS7ti5vZHQ%3d&icon=..odt

[T03-R04-qa]: https://www-ws.gov.taipei/Download.ashx?u=LzAwMS9VcGxvYWQvMzYzL3JlbGZpbGUvMzE4MjAvOTU3Njk2Mi83MTI3MTcyNC1lYzBjLTQ5MzctOGNiMi1hMDI5MTZhNjQzNDIub2R0&n=6byg6aGe5YG16ZiyUUEgLm9kdA%3d%3d&icon=..odt

### T04 Official Neihu traffic: timing requires an executable employer decision

Research observation: **2026-10-13**. Source IDs below are track-local. Evidence, inference and hypothesis are distinguished; no participant contact, account creation, paid access, inference API, implementation or publication occurred.

#### Findings and scope

**Supported, with attribution:** Neihu commuting difficulty has local evidence beyond the organizer prompt. Taipei DOT's [2015 corridor survey announcement (S02)](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=2CEEE779A43E7C0B&sms=72544237BBE4C5F6) identifies concentrated work-start times and congestion at named corridors. An independent [2025 first-person commute account (S03)](https://www.ptt.cc/bbs/home-sale/M.1742977427.A.6F6.html) describes early departure, multiple rail transfers, crowding, and choosing rail reliability over uncertain road travel. This supports one experienced burden and workaround, not population prevalence or demand for our tool. No HR practitioner reported an analytical bottleneck in the inspected evidence.

**Refuted:** the claim that staggered hours, commute visualization and employer coordination are new or absent interventions. DOT advocated employer flexibility in 2015; [TUIC's original 2021 study (S04)](https://tuic.gov.taipei/neihu_traffic/) already combines road, telecom and ticket evidence into maps and policy options. [DOT's 2025 employer campaign (S05)](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=58C6C7A781571AC3) already combines remote work, incentives and employer participation. A generic heatmap cannot claim an established unmet need.

**Unresolved:** a new coordination artifact would improve an employer's choice or the city's expansion decision. Public procedure establishes institutional practice, not practitioner pain. Employer authority to change schedules is evidenced in particular company actions, but employee feasibility, operating constraints and willingness across firms remain unvalidated.

**Source recovery:** the stale legacy feed does not establish that current Taipei measurements are unavailable. Full [VDLive.xml (S08)](https://tcgbusfs.blob.core.windows.net/blobtisv/VDLive.xml) parses as a current v2 snapshot. Fresh historical **upstream freeway** measurements are also downloadable with explicit reuse terms [S10](https://tisvcloud.freeway.gov.tw/). Neither supplies verified complete historical coverage of the requested city bridges and RuiGuang corridor.

**Fit:** directly addresses [organizer issue 4 (S01)](https://puma.taipei/hackathon#issue-4), whose morning-concentration and policy-benefit assertions remain attributed. Separate from C01 collision-site review: traffic counts are not injury risk or safety improvement. Shares transport context with T05 buses and T10 metro/YouBike, but does not redesign their services. Two distinct candidate workflows follow; personal route/ETA lookup is an existing comparator, not an additional proposed candidate. Evidence depth is strongest for public processes and source suitability, weaker for lived experience, and absent for observed HR-tool use or causal civic benefit. No topic selection is made.

#### Bounded baseline and competing explanations

**Evidence:** S02 reports a 2015 employee questionnaire with concentrated start times and corridor-specific timing differences. Its historical time comparisons do not estimate savings after thousands of commuters change behavior. Questionnaire sample, response rate and underlying trip records were not exposed in the announcement. They cannot establish 2026 concentration.

**Evidence:** S04 explicitly uses 2019 traffic and June 2020 telecom/ticket inputs. Its through-traffic estimate, attributed to a commissioned report, shows why not every passing vehicle is an employer-addressable commute. The residual classified as private transport includes walking; it must not become a count of drivers. The source is valuable contrary evidence against a single-cause timing story, not a current mode-share census.

**Evidence:** [DOT's 2026 update (S06)](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=B2603ED5E6FD0229) describes road openings, additional buses, Wenhu capacity measures and corporate green transport. Its aggregate improvement assertions lack downloadable underlying observations here. [Current coordination (S07)](https://dot.gov.taipei/News_Content.aspx?n=D739A9F6B5C0AB95&s=8A2AA8E9530EBC91&sms=72544237BBE4C5F6) already incorporates LINE GO matching by departure, time and destination. The [official Greater Taipei Bus portal (S12)](https://ebus.gov.taipei/) exposes routes/stops, dynamic information and transfer planning. Menu inspection establishes functions, not a completed commute-planning usability test.

**Inference:** a defensible baseline comprises DOT/association employer outreach, existing company rules and incentives, commissioned corridor surveys, TUIC analysis, and current commute tools. A tool must improve selection or evaluation of an **implementable** timing trial, beyond restating peak windows. School pickup/drop-off, fixed customer hours, shift coverage, rail/bus crowding, construction, through traffic and road capacity are rival constraints; their relative contribution was not measured. City coordination cannot substitute for employer and worker agreement. Changing a clock time can move a queue into another interval or corridor rather than remove it.

#### Completed source experiment: what is actually usable?

**Predefined source test:** a timing comparison needs timestamped measurements, direction and vehicle units, topology joins, shoulder periods, repeated comparable weekdays and an acquisition/reuse route. Reject current-history inference from a static inventory or stale snapshot; reject causal savings from a single count profile. This test addresses source feasibility and baseline redundancy, not practitioner effectiveness.

**Method and result:** unauthenticated curl GETs, complete XML/GZIP parsing with Python ElementTree, XLSX ZIP/XML inspection, and PDF text/link extraction. Reproduce the named checks from the exact source URLs, namespaces, workbook sheets/rows and aggregation rules below; the original snapshots were parsed in full, with no missing-cell imputation.

1. **Current city feed, supported narrowly.** Static VD.xml has **641 unique VDID**; VDLive.xml has **650**, with **all 641** static IDs matched and **9** live-only IDs. Static UpdateTime is `2026-10-13T00:00:00.000+08:00`; live UpdateTime `2026-10-13T18:52:40.001+08:00`, measurement timestamps `18:52:00`, LinkVersion `25.12.1`. Exact RoadName filtering finds **12 堤頂大道, 4 瑞光路 and 4 民權東路六段** static records. These names do not establish complete bridge or district coverage. `VRHT600` advertises six lanes but its live record contains five; `VPMSV40` and `VRPSV00` share a southbound LinkID. Summing all sensors would risk repeated counting. The citywide live snapshot contains status codes 0/1/2; unknown and abnormal records require exclusion, not zero-filling. [S08](https://tcgbusfs.blob.core.windows.net/blobtisv/VDLive.xml), [S09](https://thbapp.thb.gov.tw/opendata/vd1.aspx).

2. **A real historical local 15-minute sample, supported; complete morning history, refuted for this source.** The official annual-survey pointer leads to [A023 汐湖二橋 XLSX (S11)](https://online.bote.gov.taipei/botedata/%E4%BA%A4%E9%80%9A%E6%B5%81%E9%87%8F/113%E5%B9%B4%E5%BA%A6/XLS/A023-113.xlsx), dated **2024-09-10, sunny**. Sheet2 has raw quarter-hour counts; ingress rows 5–8 reproduce the PDF's 07:00–08:00 totals: **278 small vehicles, 765 motorcycles, 4 buses, 9 bicycles**. Rows 9–12 reproduce 08:00–09:00: **236, 779, 4, 3**, respectively. The inspected pre-07:00 and post-09:00 template cells are blank; sheet3 includes `#NUM!` ratio errors. Raw counts and PCU must remain separate. This boundary sample demonstrates that historical 15-minute data need not always be self-collected, while failing the organizer's complete 07:00–09:30 repeated-weekday requirement. No travel-time field exists in this sample.

3. **Historical freeway access, supported; substitution for city streets, rejected.** Following the publisher's history index, complete `VDLive_0700.xml.gz` samples for **2026-09-01** and campaign day **2025-09-23** contain **3,763** and **3,255** VDLive elements. Each has **15** identifiers containing 內湖, 堤頂 or 東湖; the 2025 sample includes two local status=1 records. LinkVersion changes from `24.02.1` to `25.06.1`. These are genuine historical measurements, not simulated values, but one minute per date proves access and quality hazards, not daily completeness or trends. Freeway ramps omit city bridge approaches and most motorcycle movements. [S10 history index](https://tisvcloud.freeway.gov.tw/history-list.php).

**Sampling rationale:** one current full-city join tests identity coverage; one local survey checks quarter-hour granularity, aggregation and boundary missingness; two archived dates test current and intervention-period access plus changed topology. They are deliberately source tests, not a statistical outcome sample. Tolerance is zero for silently treating missing intervals as observed zero or mixing directions/units, because either can reverse a timing choice. Numeric policy-benefit thresholds require measurement variability and owner-agreed service constraints; none is invented.

#### T04-W1 — Employer chooses whether and when to trial flexibility

**Problem/user/trigger/authority.** Hypothesized user: HR/operations coordinator at one RuiGuang-road employer preparing for construction or recurrent late arrivals. Affected employees have locally evidenced commuting burdens, but this employer's lateness, retention or coordination cost is unknown. Decision: retain current hours, trial an earlier/later voluntary start window, or prefer another existing commute measure. Employer operating authority and employee feasibility are required; DOT and the association can coordinate evidence and transport support. This narrows official fit to a timing trial, leaving network capacity and nonparticipating traffic unresolved.

**Exact baseline and success.** Compare an evidence/constraint sheet against existing company scheduling rules, DOT/association consultation, S02's generic timing advice, and existing route/transfer tools. Success would be a feasible trial decision with fewer unresolved constraints or less preparation effort, without missed coverage, school/care or customer-service obligations. Observe preparation time, justified selection/rejection and errors in the same decision case; no such user test was run.

**Rejection/disposition.** Problem rejection: the employer already has adequate flexible hours and tools, cannot move its required staff, or the proposed evidence changes no choice. **Unresolved → narrow** to feasibility assessment, not optimization. Data rejection: no current complete corridor profile or employee feasibility inputs. **Supported for present evidence → defer** choosing an optimal start time. The stronger claim that public road data alone identify switchable workers is **refuted**: no employee destination, required start time or care obligations is measured.

**Workflow/dependencies/claims.** Aggregate commuting constraints and current work rules + directed corridor history → compare feasible windows and alternative measures → HR records a trial or documented no-trial decision → signed internal schedule/coverage plan, with voluntary participation and review date. Essential missing inputs are aggregate employee origin/mode, eligible participation, required onsite coverage, school/care constraints, and the appropriate historical city-road series. Personal records should remain private. S08 gives observed point measurements; S11 gives dated counts; neither estimates door-to-door time or causal savings. Any shifted profile is a labeled scenario with participation assumptions, not a predicted outcome.

**Smallest decisive validation/readiness.** First compare the current company process with a single bounded decision packet, including one flexible employee group and a fixed-shift or care-constrained group as difficult cases. Two contrasting groups test whether authority/feasibility, rather than charts, determines the choice; this is not a representative employee sample. Infeasible in this run because the inspected sources supplied no employer process or employee aggregate, and contact/accounts were excluded. Completed public-source comparison already establishes substantial baseline capability and insufficient current local history. **Demonstration=specified** for a disclosed evidence/constraint packet; **decision=insufficient**. Task usability untested; incremental decision usefulness unresolved; civic delay, emissions and equity outcomes unknown.

**Adoption/presentation/next check.** A 100-day path needs one consenting employer, HR/labor review, association cooperation, transport expertise and permitted data; staffing, survey, integration, employee burden and transport costs remain unknown. Bounded before/action/after example: before, an HR coordinator considers a later RuiGuang start because of generic peak advice; action, identify required onsite coverage and reject an unsupported timing recommendation; after, a documented no-trial or constrained-trial decision replaces an unqualified savings promise. This example is hypothetical, not an observed employer outcome. **Executable next check:** inspect the public TDX historical-service catalog for `VRGUF00`, `VS6TI00`, `VSGRX40`, `VSNRE00`, recording date retention, downloadable fields and exact license; stop at login or payment, and keep the trial deferred if no permitted history route is verified.

#### T04-W2 — City determines whether a coordinated trial merits expansion

**Problem/user/trigger/authority.** Hypothesized user: DOT/Traffic Engineering Office evaluator working with the Neihu association after an employer campaign. Executable decision: continue, revise or stop expansion of a specific timing intervention. Coordination activity is observed; analytical difficulty for this evaluator is not. Employers own schedules; city units own monitoring and relevant transport operations. No authority to impose company hours is inferred.

**Baseline and comparative success.** S05 compares 2025 campaign-day RuiGuang peak counts with the previous year's period, while mixing remote work, modal incentives and exceptional early departure. The account does not isolate staggered hours. S06 additionally reports road and transit interventions. Success relative to that baseline would be a reproducible, topology-consistent assessment that distinguishes timing from mode/remote-work changes and detects displaced congestion before expansion. This is decision-quality improvement; no observed causal benefit follows from publishing the assessment.

**Rejection/disposition.** Problem rejection: after matching controls and participation, total commute burden does not improve, or worsens in shoulder periods/adjacent corridors; a lower single peak is insufficient. **Unresolved → continue only evaluation design**, not expansion advice. Data rejection: campaign participation by intervention type, complete treated/control histories, or topology/event comparability is unavailable. **Supported for this run → defer causal attribution**. Attribution of the reported campaign reduction specifically to staggered hours is **unsupported**, rather than evidence the intervention failed.

**Workflow/evidence/action/output.** Intervention dates and aggregate eligible/actual participants by timing/mode/remote-work treatment + directed road flow, speed, queue/travel-time records + incidents/weather/school/construction calendars → compare like weekdays and unaffected corridors, test spillover and pre-existing trends → DOT recommends continue/revise/stop for that trial → a reviewable evaluation memo and monitoring scope. Required outcome evidence includes independent door-to-door travel-time/reliability observations and transit crowding, not merely speeds at points. Historical freeway data are upstream context; S11 is a dated independent count sample. Rights for public evidence and employer aggregates require separate verification; no campaign microdata was obtained.

**Decisive experiment/readiness.** The completed source-level experiment rejects a public-data-only replication of S05's RuiGuang causal claim: neither raw campaign city measurements nor comparable controls/participation were found in the inspected original publication. Missing evidence does not disprove campaign benefits. For a permitted future trial, examine the full **06:30–10:30** morning window to capture shoulders, and afternoon outcomes if working hours move. Start with every weekday in a pre/post school-term week, same weekdays and corridor boundaries, plus an unaffected corridor chosen by comparable pre-trends and no spillover. One week spans weekday patterns but cannot establish causal precision; expand based on observed variability and confounding, not a fabricated significance threshold. Holidays, rain, incidents, changed ramps, school days, absent motorcycles and abnormal detectors are mandatory difficult cases. If a credible control cannot be found, report descriptive change only. **Demonstration=specified** for an evaluation memo with disclosed missing inputs; **decision=insufficient**; usability and civic effects untested.

**Adoption/presentation/next check.** A 100-day evaluation needs DOT/TEO custody of historic series, employer treatment logs, a transport evaluator, data/privacy agreements and an agreed nonworsening constraint; procurement, monitoring cost and participating-firm capacity are unknown. Before/action/after example: before, a single peak reduction supports an expansion narrative; action, inspect abnormal ramp data, controls and later intervals; after, label the result descriptive and withhold a timing-effect conclusion. **Executable next check:** follow S10's archive links for one treated-day and matched prior-week morning ramp series with their dated static metadata, respecting the publisher's >40-second request spacing, then assess gaps before considering any treatment comparison. This resolves a bounded upstream acquisition uncertainty, not the missing RuiGuang causal evidence.

#### Compact reusable source ledger

All sources were retrieved/inspected **2026-10-13**. HTML inspection used primary-source web reads or curl of original content; searches were leads only. The ledger preserves original URLs, periods and quantitative parsing methods; task-owned source/helper files are retired after integration. Public text is summarized with attribution; no bulk redistribution right is inferred from readability.

| ID / publisher and exact source | Inspected method, sections, period and unit | Permission, quality limits and contrary evidence |
| --- | --- | --- |
| S01 — Puma organizer, [市政 debug松 / issue 4 and rules](https://puma.taipei/hackathon#issue-4) | curl HTML, issue-4 and rules; proposed 07:00–09:30/15-minute dashboard and permitted simulation | Organizer framing only; no measured prevalence/effect; feedback not inspected; redistribution terms unknown. No deadline relied upon. |
| S02 — Taipei DOT, [內湖地區分散上下班 可大幅節省交通時間](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=2CEEE779A43E7C0B&sms=72544237BBE4C5F6), 2015-08-31 | Original HTML body and linked five-page corridor attachment; 2015 questionnaire/corridor summaries | Historical departmental assertions, raw sample and replication unavailable; exact text/data reuse terms not audited. Already advocates flexibility, contrary to novelty. |
| S03 — Original community author, [淡水通勤內湖實測](https://www.ptt.cc/bbs/home-sale/M.1742977427.A.6F6.html), 2025-03-26 | Original post/main account and author's reliability explanation; one self-reported rail commute | Unverified identity/timings, self-selection, no population inference; copyright/reuse unknown; no personal identifiers retained. Existing early schedule already mitigates crowding for this person. |
| S04 — TUIC + Taipei DOT, [從數據看內湖科學園區通勤模式](https://tuic.gov.taipei/neihu_traffic/) | curl HTML and public app JS text; study framing, methods, annotations, policy and source footer; 2019 road/2020-06 ticket/telecom, 250m grid and districts | Original analysis with modeled population/proxy residuals; not current worker observations. Reuse license for underlying telecom/ticket data unknown; not obtained. Through traffic and transfers rival timing explanation. |
| S05 — Taipei DOT, [內科通勤轉型有成效 產官共挺綠運輸](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=58C6C7A781571AC3), 2025-10-08 | Original HTML campaign account, 2025-09-23 RuiGuang versus previous-year peaks; named employer actions | Publisher-reported aggregate outcome, no raw counts/control/treatment isolation. Text/data license not audited. Multiple measures confound timing attribution. |
| S06 — Taipei DOT, [市府積極改善內湖交通，旅行時間下降6.07%](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=B2603ED5E6FD0229), 2026-08-16 | Original HTML engineering, transit and corporate-program paragraphs; seven-road afternoon summary | Aggregate institutional claims, not independently reproduced; original observations/weights absent. Reuse unknown. Existing road/public-transport improvements confound before/after. |
| S07 — Taipei DOT, [內科揪團逗陣來 少開車、散車流](https://dot.gov.taipei/News_Content.aspx?n=D739A9F6B5C0AB95&s=8A2AA8E9530EBC91&sms=72544237BBE4C5F6) | Original HTML, 2026 activity and LINE GO matching description | Documents an existing coordination tool, not effectiveness or observed HR pain; operator matching flow not tested; reuse unknown. |
| S08 — Taipei TEO bucket, [VD.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/VD.xml), [VDLive.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/VDLive.xml); [static catalog](https://data.gov.tw/dataset/135705), [legacy dynamic catalog](https://data.taipei/dataset/detail?id=e57afe7f-3c9e-4f31-9208-eed859a92600) | Full curl/ElementTree, static 721,871 bytes/live 1,855,333 bytes; identifiers, links, lanes, coordinates, status and timestamps; point/lane/vehicle/minute units | Static catalog states OGD License v1.0/free. Legacy catalog names OGD v1.0 but links GetVDDATA.xml, **not verified to license the exact discovered v2 URL**: v2 redistribution authorization remains unresolved. Single current snapshot; mismatched lanes and repeated LinkID. Preserve earlier stale GetVDDATA finding. |
| S09 — Highway Bureau, [VD dynamic schema](https://thbapp.thb.gov.tw/opendata/vd1.aspx) | Original schema tables: one-minute vehicle counts, km/h, occupancy %, -99 abnormal, status codes, DataCollectTime | Shared v2 semantics; city-specific detector calibration still unknown. Absent vehicle class may be omitted; zero-volume speed is not stopped traffic. Schema text license not separately audited. |
| S10 — Freeway Bureau, [terms](https://tisvcloud.freeway.gov.tw/), [history index](https://tisvcloud.freeway.gov.tw/history-list.php), [2026 sample](https://tisvcloud.freeway.gov.tw/history/motc20/VD/20260901/VDLive_0700.xml.gz), [2025 sample](https://tisvcloud.freeway.gov.tw/history/motc20/VD/20250923/VDLive_0700.xml.gz) | curl index/terms; full gzip XML samples at 07:00, measurements 06:59; NFB authority, directed lane/class records; named local ramp test | Terms explicitly permit free reproduction/distribution/adaptation, require attribution to 交通部高速公路局「交通資料庫」 and >40-second repeated request spacing; system failures disclaimed. Not city street/motorcycle coverage. Two snapshots do not establish complete weekdays. |
| S11 — Taipei TEO, [annual survey catalog](https://data.taipei/dataset/detail?id=68767aa4-6703-4760-8a0e-74c641d66b90), [national license record](https://data.gov.tw/en/datasets/128230), [pointer CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=e2311fce-e104-41cd-b8c7-57ad433fc49a), [A023 XLSX](https://online.bote.gov.taipei/botedata/%E4%BA%A4%E9%80%9A%E6%B5%81%E9%87%8F/113%E5%B9%B4%E5%BA%A6/XLS/A023-113.xlsx), [A023 PDF](https://online.bote.gov.taipei/botedata/%E4%BA%A4%E9%80%9A%E6%B5%81%E9%87%8F/113%E5%B9%B4%E5%BA%A6/PDF/A023-113.pdf) | CP950 pointer CSV → PDF hyperlink index → 2024 road index → local station files; full XLSX ZIP/XML and PDF text; one bridge, directions, vehicle classes, quarter-hour counts and hourly PCU; 2024-09-10 | National pointer dataset OGD v1.0; linked station workbook has no separate explicit redistribution statement inspected. Report metadata elsewhere can be restrictive: do not propagate pointer license automatically. Blank template periods, formula errors, single-day sampling, no travel times; raw counts reconcile. |
| S12 — Taipei/New Taipei governments, [大臺北公車](https://ebus.gov.taipei/) | Original HTML menu inspection; routes/stops, dynamic/GIS/transfer planning; displayed update 2026-10-12 | Existing tool functions observed, route-specific outcome not tested; copyrighted interface and no bulk data reuse inferred. |

**Integration disposition:** retain the Neihu candidate, correct the blanket live-feed/history unavailability inference, and narrow its readiness. Historical freeway and annual quarter-hour samples are feasible research inputs; complete city-corridor history, exact v2 reuse permission, employer feasibility and incremental practitioner value remain decisive gaps. The immediate topic-level next check is W1's named-city-detector historical-catalog/rights check; no application or simulated savings is warranted by these findings.

### T05 Official buses: service decisions and executable driver rest

Research-only report, retrieved **2026-10-13 (Asia/Taipei)**. These findings do not select a topic or authorize implementation. Evidence depth is unequal: one documented operator safety failure is much stronger than evidence that a new public planning interface would improve planners' work.

#### Findings and disposition

**Supported:** Taipei already reviews routes, approves service changes, offers reservation buses, publishes annual route passenger statistics, and operates an internal Operations Management System (OMS). Public passenger testimony describes irregular waits; official accident investigation documents a mismatch between planned and actual duty. These establish specific historical difficulties and existing responses, rather than a citywide diagnosis. [T05-S02][T05-S03][T05-S04][T05-S05][T05-S06][T05-S07]

**Refuted within inspected inputs:** route geometry, estimated arrivals, and annual totals cannot establish redundant passenger demand or feasible driver duties. The previously audited organizer sources are not the whole evidence universe: official route-level statistics are accessible. However, that improvement in granularity still does not reveal stop/hour demand. A generic reservation or route-map demonstration would duplicate existing functions. [T05-S03][T05-S05][T05-S13][T05-S14]

**Unresolved:** current practitioner difficulty, marginal benefit over internal tools, lawful access to demand/duty records, and physical availability of rest facilities. The monitoring recommendation currently displays “awaiting reply or in progress”; this is not proof that improvements have not occurred. [T05-S08] Narrow service research to an evidence packet for a specified review; defer operational redesign and live duty advice until essential records and a responsible practitioner exist. Missing public evidence does not refute pain.

**Fit/overlap:** both workflows fit official issue 5, whose demand/overlap assertions remain organizer claims and whose page explicitly acknowledges unavailable stop boarding/alighting data. [T05-S01] Service reliability overlaps T04 Neihu congestion and T10 transfers, but neither road speed nor MRT OD substitutes for bus demand. Driver duty shares service constraints, yet has a different owner/action. Facility provision is treated as a required constraint within duty review, not a separately validated capital-planning workflow. No real-time network optimizer is justified.

#### Exact source ledger

All rows were retrieved on **2026-10-13**. “Web” means opening original publisher content through the browsing tool; “curl” means a direct unauthenticated GET. None required an account, payment, or model inference. Publication dates are distinguished from retrieval dates. Linked identifiers resolve to exact original URLs below.

| ID / publisher / title | Inspection, period and unit | Access, licensing, quality and contrary evidence |
| --- | --- | --- |
| [T05-S01] Organizer, 市政 debug松 | curl HTML/text, issue 5 and rules; present event framing | Public. Organizer calls for stop demand, DRTS and rest/parking review; permits disclosed simulation. Civic assertions unverified; source-specific terms still control. |
| [T05-S02] Taipei law database, 聯營公車申請分配調整路線及車次處理原則 | Web plus curl all seven points; displayed revision 2013-03-04, effective 2013-04-01; route/service authority | Public administrative rule, not operating observations. Points 5–7 inspected: alternatives, surveyed segment usage, approval and committee disputes. Redistribution permission not separately inspected; quote no long extracts. |
| [T05-S03] PTO, 20621-01-04 行車效率按路線分114 | Full 15-page PDF; curl, `pdftotext -layout`, rendered page 1; calendar 2025, compiled 2026-03-25; route/branch annual totals | Passenger trips, operated segments/km, revenue, mean passengers per segment, revenue/km. Six diagnostic rows checked. PTO declaration [T05-S16] supplies OGDL v1 with exceptions. No stop, hour, OD, occupancy, cost or driver identity. Route 21 ceased during the year; historical totals are not current service. |
| [T05-S04] PTO, 公車營運調整; August 2026 attachment v2 | Current HTML index plus complete [August attachment](https://www-ws.gov.taipei/001/Upload/458/relfile/22562/3499374/2b3ccd55-ca0e-4cf4-9ed5-c8352bdbf754.pdf) text; effective dates and route/change descriptions | Public; [T05-S16]. Actual approvals include route renaming, opening, extensions, changed timetables and reduced service. No underlying demand analysis or before/after outcomes. Latest inspected listed month was August, not an assertion of all subsequent changes. |
| [T05-S05] Taipei/New Taipei bus portal, 臺北市預約公車 | Web page explanation and navigation; reservation service | Public instructions; booking not attempted. Low/inconsistent-demand services already use reservation analysis. Stops remain served; passengers without reservations may board. Raw reservation data and redistribution terms unknown. |
| [T05-S06] Taipei, 公車好行 揪夥來talk座談會會議紀錄 | Full 56-page PDF downloaded/text searched; actual meeting **2020-08-22**, despite recent search indexing; printed pp.3–4, 29–30, 52–53 | Passenger waiting testimony, union shortage/work-pressure accounts, city response describing schedules and onboard headway displays. Self-selected testimony, not prevalence or current measurement. Public agency copy; [T05-S16] exceptions apply; avoid participant personal details. |
| [T05-S07] TTSB, TTSB-HOR-26-04-002 final investigation | Full 131-page PDF curl/text; §§1.14–1.15, 2.3, 4.2 and Appendix 5 inspected; printed pp.109–110 replayed; rendered p.109 | Published April 2026; accident 2024-11-17; duty records September–November 2024 for one driver. [T05-S17] permits attributed reuse subject to privacy/third-party exceptions. Findings, operator interviews, and investigator-derived tables differ; no raw vouchers. Fatigue-model outputs are official modeled estimates, not measured impairment; none reused here. |
| [T05-S08] TTSB-HSR-26-04-008, monitoring recommendation | Web recommendation, recipient, status, update date | Taipei DOT recipient; status awaiting reply/in progress, last changed 2026-04-28. [T05-S17]. Public status is not an implementation audit. |
| [T05-S09] TTSB-HSR-26-04-005, actual duty after changes | Web content/status; 2026-04-28 publication, 2026-05-13 change | Operator recipient; oversight delegated to competent authority. [T05-S17]. No accessible live duty extract or verified completion on this page. |
| [T05-S10] PTO, 友善公車駕駛員工作環境 體恤如廁需求 | Web original 2020-09-30 announcement, entire substantive body | [T05-S16]. Designated toilet opportunities/terminal or route changes are already contemplated. Text alternates single-trip and round-trip wording around 150 minutes: do not encode this press release as a compliance rule. No facility coordinates, opening/access rights, capacity or current inspection results. |
| [T05-S11] National Audit Office, 2024 Taipei final-account audit, transport opinion (5) | Original HTML chapter/opinion title opened; linked PDF returned a script/challenge document to curl | Public audit identifies staffing shortage, subsidy administration and safety concerns; source-reported, not reproduced prevalence. HTML title supports only that finding; detailed counts not used. Redistribution terms uninspected. |
| [T05-S12] CECI, 公共運輸數據整合分析與視覺化呈現 | Web original researcher article, 2024-12-13; source-permissions table, route-use and OD sections; Taoyuan/Tainan examples | Existing dashboards already combine ticket OD and networks. Ticket data explicitly controlled in those examples; not proof of Taipei access restrictions. Public article is not underlying data/license; redistribution unknown. |
| [T05-S13] PTO, 公車路線軌跡, catalog `efad90af` | curl catalog + complete [GetBusShape.gz](https://tcgbusfs.blob.core.windows.net/blobbus/GetBusShape.gz), gzip/JSON parse; 1,010 objects | Root is a **JSON array**, keys `UniRouteId,RouteID,SubRouteID,wkt,utime,GoBack`; timestamps 2023-06-14–2026-09-23. No demand/duty fields. This corrects the earlier brief's `BusInfo` wrapper description for this response. Geometry not fully validated. Catalog/public access does not independently establish payload redistribution terms. |
| [T05-S14] PTO, 預估到站時間(公車), catalog `f11a5af0` | Web catalog + full [GetEstimateTime.gz](https://tcgbusfs.blob.core.windows.net/blobbus/GetEstimateTime.gz) JSON; 29,402 `BusInfo` entries, publisher update `2026/10/13 18:56:30` | Keys `RouteID,StopID,EstimateTime,GoBack`; `EssentialInfo` declares WGS84. Catalog says public/free and links government terms; exact payload attribution terms need publisher documentation. No historical demand, vehicle-to-driver link or non-driving work. Single snapshot; no prediction-accuracy result. |
| [T05-S15] MOTC/PTX, 公車API靜態資料使用注意事項 | Web original documentation, sections 1, 6–10, 14–15 | Distinguishes stop/station/group, actual/display stop order, branches, operators and timetable variants. Public docs; license and current TDX quotas unverified. Documentation is not authenticated data access; no account created. |
| [T05-S16] PTO, 政府網站資料開放宣告 | Web substantive authorization and exceptions | OGDL v1, attributed reuse; personal data, special third-party works and logos excluded/qualified. Applies to agency publications, not blanket permission for private duty/IC records. |
| [T05-S17] TTSB, 政府網站資料開放宣告 | Web authorization and exceptions | Free, nonexclusive, sublicensable attributed reuse; privacy, logos and specially restricted works remain outside blanket permission. No agency endorsement. |
| [T05-S18] Taipei bus operators' association / joint management committee homepage | Web current substantive notices and source attribution | Publishes PTO's favorable service narrative and satisfaction assertion, alongside shorter routes/rest measures. Survey method not inspected; no percentages adopted. All-rights-reserved footer. Counterweight to assuming universal dissatisfaction; operator interest and repeated city text limit independence. |

#### Workflow A — Decide whether a specified corridor/service proposal deserves further review

**Pain, user and boundary.** In the 2020 public meeting a passenger described variable waits and clustered 307 buses; the city acknowledged reliability concerns and cited mixed-traffic effects. [T05-S06] This supports an experienced reliability problem, not the organizer's claim that overlapping routes waste demand. Hypothesized user: a PTO route-review analyst preparing one weekday corridor/service case with its operator. Trigger: an operator adjustment application or specific repeated passenger concern. Output: retain current service, request a targeted demand survey, or advance a supported alternative for formal review. It is not an automatic route-cut instruction.

**Exact baseline.** Operators review service/load and apply for changes; PTO approval and the route committee govern adjustments. [T05-S02] The August list proves changes already occur, rather than establishing difficulty doing them. [T05-S04] Public eBus supplies navigation/ETA/reservation functions; internal planning capabilities cannot be inferred from that public interface. [T05-S05] CECI's existing OD dashboard elsewhere also defeats any novelty claim for drawing flows. [T05-S12] The remaining hypothesis is that a compact, provenance-linked case reduces missed constraints or preparation effort compared with existing documents/internal analysis.

**Success and rejections, fixed before the data check.** Success would be a reviewer reaching the same defensible retain/survey/advance disposition with fewer missing decisive facts or less preparation effort, without losing access for protected/low-volume trips. No numerical time-saving target is justified without baseline observation. Problem rejection: existing review already produces that case adequately, or vehicle/staff/funding constraints make the proposed action unavailable. **Unresolved**, requiring the same-case practitioner comparison; narrow, do not assert an unmet software need. Data rejection: inputs cannot resolve stop/time/direction demand, alternatives and affected trips. **Supported for current public inputs**; defer redesign. Absence of rider OD does not show absence of demand.

**Completed decisive experiment.** Compared the citywide-only starter baseline with [T05-S03], current changes [T05-S04], and actual feed schemas [T05-S13][T05-S14]. Chose six diagnostic annual rows: high-volume 307, low-average 68, 212/main/night/direct variants, and discontinued 21. These test aggregation, branch identity and temporal validity; they are not a representative route sample. Reproduced passengers ÷ operated segments: 307 `16,398,514 / 322,900 = 50.785`, 68 `25,679 / 9,060 = 2.834`, 212 `878,070 / 39,000 = 22.515`, 212-night `39,358 / 4,380 = 8.986`, 212-direct `1,392,760 / 63,876 = 21.804`, 21 `73,761 / 4,938 = 14.937`. All reproduce the published whole-number means when rounded; that rounding is the only numerical tolerance used. They are **passengers per operated segment, not simultaneous load**. Route 68's mean below five does not satisfy a peak-period, particular-segment boarding/alighting test. [T05-S02][T05-S03] Route 21's annual row survives its midyear termination; current names must not be joined blindly. Result: route-level context is supported; stop/time redesign evidence is insufficient. No route overlap or removal recommendation was computed.

**Input → action → observable output.** A dated proposal, branch-specific ordered stops, timetable, actual operated trips, stop/time boardings/alightings and transfers, passenger access needs, vehicle/staff limits and alternative-service availability → compare current service with one explicitly bounded alternative and identify unknowns → analyst requests the missing survey or submits a review packet → an attributable review disposition and survey specification. Required joins include direction/operator/branch/version; MOTC warns that display order can merge actual branches. [T05-S15] Demand and staffing access/retention/license are unknown; annual statistics cannot fill missing cells. Only real historical totals and real approvals were analyzed; no simulated passenger counts were created.

**Adoption, presentation and next check.** PTO/operator cooperation, transport-planning expertise, cross-city authority where applicable, ticket-data permission and a retained baseline are prerequisites for a 100-day pilot; integration, survey and staffing costs remain unknown. A proposed presentation shows “68 has a low annual mean” before review, the analyst checking its peak/segment/access evidence, and “request demand evidence; retain service pending review” afterward. This is a bounded research disposition, not improved service. Demonstration **specified** as an evidence-gap case; task usability untested, decision **insufficient**, civic ridership/reliability/equity outcomes unknown. Next executable check: follow [T05-S04]'s Blue 27 August reduction to its official operator notice and published review rationale, then test whether the reason and affected demand are actually disclosed; stop with a named access gap if they are not.

#### Workflow B — Review an operator's changed duty against actual work and feasible rest

**Pain and baseline.** TTSB documents post-plan changes missed by review. The baseline combines advance rosters, actual-return vouchers, supervisors, internal OMS/GPS/driver links and sampled oversight. [T05-S07] A published union account describes shortage/work pressure, but it dates to 2020 and is not a prevalence measure. [T05-S06] This candidate addresses one operator dispatcher's changed-duty review; agency enforcement is a downstream authority, not a second proposed user interface. Trigger: leave, swap, extra work or delay changing the planned duty. The user and historical failure are evidenced; willingness to adopt an external tool is hypothesized.

**Success/rejection before replay.** Success means identifying a consequential plan/actual discrepancy and a feasible human-approved remedy that the existing review missed, while distinguishing unavailable information from compliant rest. Problem rejection: an already deployed OMS/dispatch process now checks the same transitions adequately, or the only remedy requires staffing/facility resources unavailable to the operator. **Unresolved**: [T05-S08][T05-S09] do not establish today's operations. Data rejection: public ETA/timetables cannot link actual duties across dates or show genuine release from work and usable facilities. **Supported**; operational advice is deferred. The historical monitoring gap is supported, not inferred from the existence of rest law.

**Completed comparison/replay.** Compared Appendix 5's September nominal leave list with its actual dated work rows, then inspected the entire September 7–26 interval, including the stated leave dates and surrounding non-work boundaries. Of the five listed September leave dates, **three—13, 20, 24—contain actual work**, while 6 and 27 have dashes. All **20 dates September 7–26** have work records. This reproduces the report's described consecutive-work episode; one day's inspection or a roster-only check cannot recover it. Method: full PDF `pdftotext -layout`, date/start/end extraction, manual cross-check of printed pp.109–110 and rendered p.109. No detection-rate generalization or invented performance threshold follows from one selected accident case. [T05-S07]

The same check found a source consistency issue: September 7's `05:45–17:50` span is **725 minutes**, while reported driving is **752 minutes**. The rendered original confirms both values. Preserve the discrepancy; do not silently correct it or calculate a compliance score from that row. Appendix footnotes define duty as first departure to last return and interday interval as the gap between those events; neither establishes all preparation/closeout work or actual sleep. This is historical derived evidence, not a current operator export. Safety-review tolerance is therefore categorical: unresolved identity/time/work semantics must block a “compliant” conclusion; numerical thresholds require current rules and qualified review.

**Executable workflow and evidence.** Authorized pseudonymous driver ID, planned and actual duty events, changes, all work activities, preceding/following duties, genuine release periods and facility access → compare the change and its temporal neighbors, flag contradictions and unavailable rest → dispatcher obtains supervisor/labor review and revises assignment or records that a vehicle/driver substitute is unavailable → approved versioned roster, identified replacement and confirmed rest opportunity. These are proposed actions, not actions taken. Public route ETAs have no driver link; a bus being stationary is not proof of rest. Facilities require opening times, permission, toilets, safe large-bus standing, usable capacity and transfer/walking time. The existing toilet announcement supplies none of those location-level facts. [T05-S10][T05-S14] No licensed public current duty/facility table was established; private records require explicit lawful custodianship and access terms, not publication.

**Rival explanations and limits.** More information cannot create reserve drivers, acceptable pay, depot space or operating budget. The audit independently names staffing/subsidy issues; those may dominate software. [T05-S11] TTSB's report also examines road geometry, attention/health and occupant protection; this is not a causal proof that a rest app prevents accidents. Its §4.2 records strengthened targeted sampling from July 2025, so “nothing changed” is false as a description of the published response. [T05-S07] The operator association's positive service narrative is further contrary evidence to universal failure, with limited independence. [T05-S18]

**Readiness, presentation, adoption and next check.** Demonstration **specified** only as a disclosed historical discrepancy-review case; no scheduling app exists or was tested. Decision **insufficient** for present operations; source comparison supports investigating actual-duty review, not its marginal practitioner value or fewer crashes. A proposed before/action/after presentation uses September 13: nominal leave → reviewer discovers a `05:40–12:34` work record and checks adjacent days → discrepancy sent for human review, with no asserted historical correction. Future simulation must be separate from real records. A 100-day path needs one operator, dispatcher/supervisor and labor expertise, secure authorized actual-duty history, current rule interpretation, OMS integration and verified facility access; procurement, reserve-driver and facility costs are unknown. Next executable check: search published 2026 DOT council/traffic-meeting responses for `TTSB-HSR-26-04-008` and evidence of continuous cross-day/changed-duty checks; if unavailable, preserve that exact operator-system gap for coordinator/owner-approved inquiry. Do not request or expose personal duty/health records during public discovery.

#### Reuse, remaining gaps and provenance

Retain both candidates with these narrow dispositions. No independent public evidence was found establishing current terminal restroom/rest capacity; no blanket assertion that such data does not exist is made. No additional discovery worker is needed to reach the present data-rejection conclusions. The next consequential gap is access to the **existing** operator/agency review process and its outputs, not more route geometry.

The full-PDF/field methods and exact sources above support reproduction. Task-owned PDF/text/helper files remain outside Git and are retired after durable integration. Feed bytes SHA256: shape `57c35a701a586eec133282580bdf018a4b4229e6c2b0d694e7754b017976f524`; ETA `a4d8b299b53d1427454f9b86bebc818c696813641f0203c377aea2e8af8a028e`. No implementation, contact, registration, paid access, API inference, external publication or primary-memory mutation occurred.

[T05-S01]: https://puma.taipei/hackathon#issue-5
[T05-S02]: https://laws.gov.taipei/Law/LawSearch/LawArticleContent/FL055169
[T05-S03]: https://www-ws.gov.taipei/001/Upload/458/relfile/22583/9559858/756d8a33-254e-4aa3-a4cf-55c686ddba4a.pdf
[T05-S04]: https://pto.gov.taipei/News_Content.aspx?n=AAEEE8A01971ECFB&s=331F98EA06A47E38
[T05-S05]: https://ebus.gov.taipei/ProjectBus/Taipeidrts
[T05-S06]: https://www-ws.gov.taipei/001/Upload/458/relfile/22569/8240132/32ab3edd-9076-4065-89b5-7dd02b6a0354.pdf
[T05-S07]: https://www.ttsb.gov.tw/media/9608/1131117%E8%87%BA%E5%8C%97%E5%B8%82%E5%A4%A7%E6%9C%89%E5%85%AC%E8%BB%8A%E5%BF%A0%E5%AD%9D%E6%9D%B1%E8%B7%AF%E5%BE%80%E6%9D%B1%E9%8E%AE%E6%B1%9F%E8%A1%97%E5%8F%A3%E8%BF%BD%E6%92%9E%E5%A4%A7%E9%83%BD%E6%9C%83%E5%85%AC%E8%BB%8A%E4%BA%8B%E6%95%85%E8%AA%BF%E6%9F%A5%E5%A0%B1%E5%91%8A.pdf
[T05-S08]: https://www.ttsb.gov.tw/1133/1154/1173/23110/50079/
[T05-S09]: https://www.ttsb.gov.tw/1133/1154/1173/23110/50067/
[T05-S10]: https://pto.gov.taipei/News_Content.aspx?n=D065CCB1467288C8&s=44F6ECF9638101D1&sms=72544237BBE4C5F6
[T05-S11]: https://auditreport.audit.gov.tw/Book/ChapterOpinion/6388905949752158694b4077cdc3e147bc903389ff3664d5ca
[T05-S12]: https://www.ceci.org.tw/modules/article-content.aspx?i=823&s=19
[T05-S13]: https://data.taipei/dataset/detail?id=efad90af-4bbe-4c6a-ac60-06f3e52d8a97
[T05-S14]: https://data.taipei/dataset/detail?id=f11a5af0-7b37-48ef-98cc-f6f102ed43c6
[T05-S15]: https://motc-ptx.gitbook.io/tdx-zi-liao-shi-yong-kui-hua-bao-dian/data_notice/public_transportation_data/bus_static_data
[T05-S16]: https://pto.gov.taipei/News_Content.aspx?n=AB37908B5E9D3D00&s=1FE4B2FEF52B0D74&sms=1DD9E1F91DA4D5BC
[T05-S17]: https://www.ttsb.gov.tw/1233/2043/13478/post
[T05-S18]: https://busgroup.org.tw/

### T06 Official building resilience

Research-only findings, retrieved 2026-10-13; No application, contact, registration, account, payment, API inference, or canonical-file edit. **Evidence** below means inspected original material; **Inference** is this analysis; **Hypothesis** identifies untested practitioner value. Topic selection remains an **Owner decision**.

Scope: private residential communities in Taipei; mandatory nonresidential inspections and public-school retrofit programs are separate workflows and are not assessed here.

#### Findings, fit and disposition

**Supported:** professional assessment, renewal/retrofit feasibility and outreach coordination are different decisions. The official assessment pathway already handles consent, qualified assessment, checking and subsidy applications [S02–S04]. NCREE documents an actual community project where full reinforcement cost threatened affordability, followed by a different professional proposal and community explanation [S08]. This is concrete operator-reported difficulty, not evidence that a Taipei dashboard solves it.

**Refuted for the proposed inputs:** an individual safety score or defensible assessment/renewal priority derived from age totals, older-population counts, liquefaction zones and rescue-road lists. The freshly parsed building source is citywide annual counts, rather than building records [S12]; the liquefaction publisher explicitly rejects site diagnosis from its medium-resolution map [S11]. Building-specific assessment results are not proactively public and disclosure requires applicant consent [S04, Q19]. More mapping cannot recover these missing observations.

**Unresolved:** whether officials or community facilitators repeatedly lose time identifying the appropriate next step, and whether any new tool improves on existing professional services. Public procedure proves process, not user frustration. Available research describes intention and barriers, not a causal effect of an information intervention [S09–S10]. Authority, consent, household liquidity, professional availability and construction disruption are credible rival bottlenecks.

**Fit:** organizer issue 6 explicitly requests a weighted risk model and acknowledges unavailable individual age/structure data [S01]. The three narrowed workflows contribute to its assessment/renewal objective but do not satisfy its scientific-ranking ambition; label them narrowed issue-6 proposals or explicit free-topic alternatives. C02 population context is not structural vulnerability; C04/C05 preparedness and flood exposure remain distinct. No cross-topic rank is justified. Evidence depth is uneven: current assessment procedure is strong; a historical non-Taipei outreach case is concrete; Taipei practitioner demand and municipal outreach performance remain unvalidated.

#### Reusable source ledger

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

#### T06-A — Reach the appropriate professional assessment pathway

**Problem/user/decision.** Hypothesized user: a Taipei condominium committee or owner representative deciding what to prepare before commissioning an initial assessment this month. Consequence: an unauthorized or incomplete submission cannot enter the illustrated process [S03–S04]. Historical national underperformance supports investigation of assessment uptake, but does not identify missing information as its cause [S13]. No contemporary applicant difficulty was observed.

**Exact baseline.** CMO already provides A1/A3 forms, the one-page flow, FAQ consent exceptions, institution/service-area/fee indexes and professional consultation stations [S03–S05]. A generic eligibility chatbot or new directory is redundant unless it measurably helps applicants assemble the correct professional-review packet. Assessment consent, inspection authority and reconstruction consent must remain separate; a renter cannot simply authorize collective work.

**Success/rejection.** Success would be fewer omitted prerequisite documents or less applicant effort than using that exact pack, without incorrect assurances. Problem rejection: competent users complete the same task from S03/S04 without extra assistance, or delays are chiefly unresolved consent/capacity. **Unresolved**; defer product-value claims. Data rejection: missing ownership/management authority, legal-building evidence or professional findings prevents an eligibility conclusion. **Supported** for open-data-only automation; narrow to an explicit missing-information checklist. An age/map safety answer is rejected.

**Workflow/dependencies/claim.** Owner-provided, private authorization status and available documents → human-reviewed missing-document comparison against dated official pack → prepare questions/documents for an approved institution → observable consultation-ready checklist. Required facts: applicant authority, building unit/legal records, relevant report/version and chosen program. These are not supplied by public citywide data; obtain only from consenting applicants outside Git. Public rules may be linked under S14; reports stay private. No structural verdict, subsidy guarantee or appointment promise.

**Validation/result.** Smallest test: compare the official pack with a paper checklist on three rule branches—single-owner exemption, committee resolution, insufficient collective consent. Three is branch coverage, not a representative sample. Manual source comparison completed: S04 Q7/Q10/Q27 already answers all three; additional routing knowledge was **not demonstrated**. Timing, comprehension and real omissions were not measured. Accept no false statement of authorization; it can cause an invalid submission. Any claimed effort gain needs counterbalanced applicant tasks and professional adjudication; no invented speed target.

**Readiness/adoption/presentation.** Demonstration **specified** as a disclosed fictional checklist; decision **insufficient**; task usability and civic outcomes unknown. CMO Use Division and approved assessment institutions are plausible operators, not committed adopters. A 100-day path needs a rule owner, review time, accessible service design and live capacity checks; costs unknown. Before/action/after example: a fictional committee has no recorded resolution → compare Q10 and prepare a meeting-record question → checklist says “authority evidence missing,” never “building unsafe.” **Next executable check:** compare Q7/Q10/Q27 against the linked current legal text and mark every consent exception before testing any checklist with an authorized practitioner.

#### T06-B — Decide whether to commission a retrofit/renewal feasibility comparison

**Problem/user/decision.** Hypothesized Taipei community representative, with an existing professional assessment, decides whether to seek a scoped comparison of interim reinforcement, broader retrofit and reconstruction. NCREE's Pingtung account documents an operator encountering unaffordable full reinforcement and developing a phased alternative [S08]. The concrete problem is financing and coordination around an actionable professional option, not merely identifying an old building. Transfer to Taipei is unresolved.

**Baseline.** Existing professionals explain assessment results and evaluate alternatives; NCREE supplies cases and free explanations. Taipei has separate assessment/weak-layer routes and URO's structural-reinforcement subsidy pack, including contracts, cost breakdown and household self-funding shares [S02,S06,S14]. These are different programs; a single subsidy calculator risks mixing requirements. City renewal audit landing evidence also points to valuation transparency and supervision, not a missing risk heatmap [S13].

**Success/rejection.** Improvement would be a meeting ending with an agreed, executable professional feasibility request and explicit unresolved financing/consent items, with fewer misunderstandings than the existing professional explanation. Problem rejection: liquidity, disagreement, relocation or procurement blocks every feasible next step despite correct information. **Plausible and unresolved**, so do not promise faster renewal. Data rejection: no actual report, professional scope/quotes, ownership decision or funding-status evidence means no comparative recommendation. **Supported** for present public inputs; reject automated “rebuild versus reinforce” selection. S07 shows subsidy is capped/partial and can stop when exhausted; information cannot eliminate the funding gap.

**Workflow/dependencies/claims.** Consenting community supplies its professional report and questions → facilitator separates technical feasibility, collective authority and household funding → commission professional comparison or record a justified deferral → observable scoped request/meeting decision. Essential evidence includes construction scope, engineer's assessment of improvement benefit, consent, occupancy/disruption constraints, quotes, subsidy eligibility and actual funds. Public rules establish requirements only. Individual costs, final awards and professional availability are unknown; no synthetic engineering estimate substitutes for them.

**Validation/result.** Minimum decisive comparison is one qualified case plus one exclusion and one borderline case: an existing assessment with financing unanswered; a project already in a prohibited overlapping reconstruction stage; an applicant requesting only cosmetic improvements. These cover action versus stop branches, not effectiveness prevalence. Completed desk check: S06 distinguishes structural-benefit evidence from cosmetic works and lists exclusions; S07 makes an unconditional full-funding promise untenable. Actual case comparison is **infeasible in this scope**: no consented reports/quotes or professional adjudicator. Do not quantify household savings. Tolerance is no engineering recommendation beyond the commissioned expert's scope; compare comprehension/next-action completeness before defining a performance target.

**Readiness/adoption/presentation.** Demonstration **specified** using fictional missing-input states; decision **insufficient**; usability, adoption and civic safety gains unknown. CMO/URO, licensed professionals and owners would jointly hold authority; a facilitator cannot bind them. Within 100 days a comparison template could be reviewed, but financing, procurement and works cannot be assumed resolved; expertise/cost unknown. Before/action/after: fictional assessed community cannot fund full work → request phased-option and self-funding review → dated feasibility brief with unanswered consent/funding, not a safer-building claim. **Next executable check:** cross-read S06 exclusions with S07 annual notice into a program-specific evidence checklist; leave funding availability explicitly unverified.

#### T06-C — Choose an outreach action without ranking buildings' safety

**Problem/user/decision.** Hypothesized district/community facilitator chooses the content and professional referral for one requested community meeting. NCREE's original account links an affordability concern, tailored cost/scope explanation and reported willingness change [S08]. It does not prove that lack of outreach causes low uptake in Taipei. The inspected conference abstract reports associations with neighbor agreement and subsidy familiarity [S09]; intention is not completion. Its finding that risk perception alone does not significantly drive action differs from the journal abstract calling risk perception a key driver [S10]. Different analyses and unavailable full methods prevent resolving that difference; neither establishes an outreach effect.

**Exact baseline and defensible narrowing.** Communities can already request NCREE's free explanatory visit; Taipei has community architects and promoter stations, with institutional references in S05/S14. Therefore “find a nearby adviser” alone is not an evidenced gap. A defensible hypothesis is preparing an opt-in meeting around the community's stated barrier and necessary authority, then referring to the existing professional service. Area demographics may guide language/accessibility support only after validation, never infer household need or building danger. Do not introduce a new neighborhood-priority workflow without its own owner and service-gap evidence.

**Success/rejection.** Relative success: facilitator prepares a clearer referral and one checkable next step than the existing request process, without greater administrative work or misleading claims. Problem rejection: existing staff already capture these issues, or no professional can accept referrals. **Unresolved**; do not claim an outreach bottleneck solved. Data rejection: no current outreach coverage, opt-in demand, nonparticipation reasons or available capacity means geographic targeting cannot be defended. **Supported** for current evidence; reject the citywide priority map. No public evidence of difficulty is not evidence of no difficulty.

**Workflow/dependencies/claims.** Private community request, stated concern and consent to follow up → classify the question as assessment preparation, funding/authority or professional technical explanation → facilitator prepares an existing-service referral/meeting agenda → observable invitation draft and agreed follow-up question. Sending it requires separate authorization. Necessary operational fields: request date, topic, prior contact, accessible meeting preferences, responsible service and confirmed capacity. None can be inferred from population, street polygons or liquefaction. Use fictional inputs for a demo; real participation records stay private; NCREE material is linked, not redistributed under an assumed license.

**Validation/result.** Smallest desk experiment deliberately tests three difficult messages: “our soil-map color proves danger”; “we lack neighbor consent”; “subsidy will pay everything.” Comparing the current services and sources yields: professional site referral with no safety diagnosis [S11]; consent/meeting pathway [S03–S04]; program-specific funding clarification [S06–S07]. All have an existing professional route; new operational benefit remains **unresolved**. Three cases cover the distinct safety, authority and financing error modes identified in the sources; they are not a population sample. This semantic stress test rejects unsupported messaging, not real-user pain. A later paired facilitator task should measure preparation effort and corrected misconceptions using the existing meeting request as baseline; zero false safety or funding assurances is required by the consequence, not an arbitrary accuracy percentage. Capacity must be confirmed before claiming an executable booked action.

**Readiness/adoption/presentation.** Demonstration **specified** as opt-in agenda preparation; decision **insufficient**; civic outcome unknown. NCREE/CMO and community representatives are plausible operators. A 100-day pilot needs a named professional recipient, privacy/retention owner, staff time and available meeting slots; demand, cost and willingness to adopt are unknown. Before/action/after: a fictional community requests a meeting because it saw red liquefaction shading → prepare a professional question about foundations and an assessment/consent checklist → draft referral, explicitly no danger rating. **Next executable check:** inspect the current NCREE meeting-request instructions and Taipei station service-hours attachment for required intake fields and routing; this is read-only, without submitting a request.

#### Integration consequence

Preserve T06 and all three workflows as hypotheses with explicit rejections above. Carry forward **demonstration=specified / decision=insufficient**, not a safety-prioritization readiness upgrade. S12 refresh strengthens the existing `7889e8a0` aggregation limit; S11 confirms the `ec40e067` interpretation restriction without refreshing its GeoJSON audit. Existing `a6394e3f` and `7a800e92` audits were not refreshed; neither is essential to these narrowed actions. The executable topic-level next check is T06-C's intake/actual-service comparison; if it yields no missing action-relevant field, defer the outreach tool as redundant instead of adding another map.

### T07 C01 collision-site review

Research date: **2026-10-13**. Scope: independently defined free topic; one bounded workflow, preparing an auditable question and evidence packet for a traffic-engineering site review. This is distinct from Neihu commute timing (T04) and bus-network redesign (T05) or YouBike transfer analysis (T10/C08). Their operational data might eventually inform a review, but congestion relief and collision prevention are different decisions. No topic selection, application, contact, registration, paid access or model inference occurred. No operational action was executed.

#### Findings and disposition

**Supported:** Taipei has recurring collision-review work, existing official screening tools, and documented problems with how locations and comparison periods are interpreted. Public accounts also demonstrate disagreement about what a collision concentration implies for an engineering response. The evidence does **not** establish that Taipei practitioners lack a dashboard or spend excessive time preparing review lists. A published process is evidence of the process, not practitioner pain.

**Refuted/narrowed:** the premise that a new count/severity map supplies a missing screening capability. The national hotspot page already exposes geographical and temporal selection and multiple ordering measures; a Taipei district meeting already publishes intersection/time-band analysis. Retain C01, but reject a generic replacement map as the demonstrated contribution. A source-linked review packet remains a hypothesis requiring comparison with existing official packets, including internal tools that this investigation could not inspect. [S02](https://roadsafety.tw/AccLocCbi), [S03](https://www-ws.gov.taipei/001/Upload/324/relfile/13900/9379464/88d1e364-a8d8-49f4-89fa-8f8d826f50d1.pdf)

**Unresolved:** current practitioner effort, missing-information frequency, access to case diagrams/intervention records, and whether a prepared packet changes the decision to inspect. Absence of public proof does not disprove the pain. Demonstration: **specified**, as a written bounded task only. Decision: **insufficient**. Task usability, incremental decision usefulness and fewer injuries are all unobserved. Evidence depth is greater for tool redundancy and unsafe data interpretations than for adoption or user value; it does not justify a cross-topic winner.

**Fit:** the organizer explicitly permits a self-defined municipal problem and requires an operable demonstration. This establishes contest fit, not demand for C01. Organizer claims remain attributed. [S01](https://puma.taipei/hackathon)

#### Pain, consequence and exact existing baseline

**Evidence — local difficulty:** Taipei DOT's 2012 explanation identified a concrete interpretation failure: national aggregation combined adjacent facilities into apparently single dangerous locations, including bridge approaches, other roads and a riverside parking area. The city used a different selection basis and subsequently analysed the underlying locations. This supports the need to identify the actual facility before assigning a review; it is historical evidence, not proof of an unresolved 2026 defect. [S04](https://dot.gov.taipei/News_Content.aspx?n=C41A7FC0570A20B3&s=F8170E663DA380C4&sms=72544237BBE4C5F6)

Taipei's 2015 mayoral direction requested quarterly rolling reviews rather than annual ritual reporting, explicitly criticizing the old practice's limited effect. This is a published management assessment, not measured analyst workload or proof the direction remains current. [S05](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=A98F53BA5A65D451&sms=72544237BBE4C5F6)

A contemporary difficult case is Roosevelt/Keelung (Gongguan). The engineering office's 2025 announcement attributes collision problems to movement geometry and weaving, and reports rejecting a proposed marking-only alternative after expert review. These are official assessments, including modeled expectations, not independently validated causal estimates. [S06](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=E3E2C3DF697050ED) In October 2025, Taiwan Vision Zero Alliance published reports of obstructed pedestrian signals, insufficient turning storage and bus delays after conversion. These are original community assertions; sampling, prevalence and causes were not established. The claims justify specific inspection questions, not adoption of the group's remedies. [S07](https://www.tvza.org.tw/新聞稿/News2025/20251003)

The 2026 city response to disputed Gongguan injury figures illustrates why the time window matters: it contrasts a three-year monthly baseline with a same-season comparison raised in council questioning. The response is not independent verification of effectiveness. Its endpoint and comparison choices need inspection before interpreting improvement; this report does not reproduce or endorse its reduction percentages. [S08](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=BEDD9D580E1DE92A)

**Exact baseline for the proposed task:**

| Existing resource/process | Already possible | Remaining uncertainty |
| --- | --- | --- |
| S02 national hotspot page | Select year/month/city/district; order by CBI, cases, deaths or injuries; read its location definition and geocoding limitations | No completed live result-query/timing test here; internal agency capabilities may exceed the public page |
| S03 Songshan May 2025 meeting packet, PDF pp. 2–3 | Read prior-year monthly comparison, Q1 intersection/time-band matrix and police-station responsibilities | Case inclusion and geometry definitions are not fully documented in the inspected pages; not a citywide tool audit |
| S04 documented city workflow | Police screening followed by Traffic Engineering Office analysis, interagency field review and improvement proposals | Historical operating description; current delegations/service standards need confirmation |
| S09 Gongguan official project index | Find review-meeting records and project presentations in one place | Index inspected, linked records not fully audited; directly challenges the assumption that all review evidence is scattered |
| S10/S11 IOT guidance | Existing professional inspection/checklist and design-reference approach | Additional software must assist its use, not substitute automatic remedies for professional judgment |

Original IOT field research supplies relevant **contrary evidence**: two Kaohsiung pilot inspections found judgment/wording difficulties, but participating operators considered the checklist duration appropriate and warned that extra steps could deter adoption. Professional and organizational deliberation remained necessary after filling it. This supports a small, optional aid; it does not establish Taipei workload. The pilot is geographically limited and the current checklist has subsequently evolved. [S10](https://www.iot.gov.tw/zh_tw/archive/pub/reports/-47122178), [S11](https://www.iot.gov.tw/zh_tw/more_announcement/創新路口事故分析與改善技術-99404448)

#### Complete candidate record — C01-W1: prepare the next site-review question

**Observed versus hypothesized user.** Observed institutional actors are Taipei Police and the Traffic Engineering Office, plus community participants publishing specific concerns. A Traffic Engineering Office analyst as the daily packet-preparation user remains a hypothesis. The user is not an injured person choosing a safer route, and this track does not add a separate citizen route-ranking workflow.

**Decision, trigger, authority and bounds.** For one already shortlisted Taipei intersection at a scheduled review, decide whether the next action is a targeted field check, retrieval of missing case evidence, or continued monitoring, and state why. The analyst prepares; the responsible office and interagency review authorize engineering action. Public engineering publications establish agency involvement, not an individual user's permission to alter signals. A fatal-incident response cannot wait for a public annual CSV. Quarterly/monthly reporting and a disputed local facility supply recurring triggers, but present-day workload/cadence remain unvalidated.

**Input → assessment → action → observable output.** Input the official shortlist, explicitly dated A1/A2 observations, the named facility/boundary, existing intervention status and attributed concern. Compare patterns against the official packet; flag ambiguous geography, missing severity and changed road geometry. The authorized reviewer records “inspect this feature,” “obtain this missing record,” or “monitor,” with source links and reasons. Output is one review request with responsible office, scope, unresolved evidence and an acknowledgement/status field. Sending it is outside this research run. A map is supporting presentation rather than the decision itself.

**Success relative to baseline.** A reviewer can reach the same defensible disposition with less retrieval/reconciliation work, or identify an action-relevant omission in the existing packet without introducing a false location, victim group or remedy. Compare paired preparations of the same case; record elapsed work, corrected errors, omitted evidence and resulting disposition. No two-minute/five-site target is justified by observed workload, so the previous proposed usability threshold should remain historical, unvalidated text rather than an acceptance result.

**Problem rejection:** reject the incremental aid if the official/public-plus-internal baseline already supplies the information and preparation advantage is absent; also reject it if the limiting step is authority/funding/professional agreement that a packet cannot change. **Disposition:** the “missing hotspot map” claim is refuted at capability level; packet benefit and dominant bottleneck are unresolved. Continue only as a bounded comparison, not implementation.

**Data rejection:** reject subgroup priority or exposure-risk interpretations if all-party/victim linkage and exposure are unavailable; reject an official-ranking reproduction if event identity, severity definitions or facility boundaries cannot be reconciled. **Disposition:** the available first-party extract supports rejecting victim rankings; exposure-risk claims are unsupported; unique-event and official-severity reproduction remain unresolved. Narrow to attributed historical records and explicit unknowns rather than inventing identifiers or silently filling missing values.

**Dependencies and permission.** Essential: authoritative facility boundary/version, observation period, event definition, incident count basis, collision type, event-level severity, official review/intervention status and the evidence needed for the specific field question. S12 supplies a licensed annual extract, not the complete operational packet. Scene diagrams, all-party linkage, current signal operation, actual speeds/exposure and staff queue/capacity were not acquired. Do not redistribute article images/diagrams under an assumed dataset license. OGDL requires attribution and does not make raw personal event display appropriate. [S12](https://data.gov.tw/dataset/130110), [S14](https://data.gov.tw/license)

**Smallest decisive experiment and completed result.** Before parsing data, the rejection test was whether official tools already served basic place/time screening and whether the extract could safely supply the proposed review evidence. The completed research-only comparison inspected three deliberately different evidence situations: Songshan's ordinary named-intersection/time matrix; S04's adjoining-road/bridge aggregation ambiguity; and Gongguan's changed geometry and disputed comparison period. These cover concrete failure classes, not a representative sample or citywide accuracy estimate. A single silent wrong-facility or wrong-victim interpretation is unacceptable in this diagnostic test because it changes the review's target; no invented statistical tolerance is used.

Result: baseline screening capability exists; explicit geography and temporal qualification are consequential; source-only research cannot establish an improved practitioner disposition. No highest-count ten-unit experiment was run: selecting such units without an authoritative aggregation boundary would test arbitrary bins, and the narrower workflow has not earned a new ranking. A paired practitioner comparison is infeasible in this run because no practitioner participation or internal packet access is authorized/available; simulated completion cannot resolve it. The public-source experiment resolved redundancy and semantic rejection conditions, not user value.

**Adoption/100-day path.** Likely operational sponsor: Traffic Engineering Office, with police data stewardship and appropriate road/works agencies. Authority to receive the output, share restricted diagrams, define case units, maintain boundaries and put the review into a real queue is unknown. Engineering expertise, information-security review, procurement/support effort and cost are unestimated. IOT's 2025 national review also identifies funding/local capacity constraints; this is a rival explanation, not a Taipei-specific budget finding. [S15](https://www.iot.gov.tw/zh_tw/archive/pub/reports/-8910095) A 100-day claim must therefore concern an approved, bounded preparation pilot, not accident reduction or automatic construction delivery.

**Bounded before/action/after presentation.** Historical Songshan example: before, the reviewer opens the May 2025 meeting PDF and its Q1 time-band table. Action, select Minquan East/Dunhua North, preserve its period and official facility wording, link the existing time pattern, and mark missing geometry/diagram evidence. After, produce a request to verify the named approach and relevant observation period, with the official packet attached by link. This is a proposed interaction using real published material; no new field finding, sent request, observed time saving or safety gain is claimed. Gongguan and the bridge example are difficult-case checks, not additional workflows.

**One executable next check:** retrieve and inspect the linked **Roosevelt/Keelung roundabout micro-adjustment review-meeting record** from S09 and test whether it already contains the facility boundary, collision-pattern rationale and rejection reasons the proposed packet would add. Record matched/missing items against those three fields; if already present, narrow further or defer C01 before any interface build. A later practitioner task needs separately authorized participation.

#### Decision-critical data experiment

A fresh full GET of the 2025 CSV was parsed in memory with Python standard-library `csv.DictReader`; no individual rows were saved. It reproduced **4,082,763 bytes and 22,762 published rows**, all ROC year 114 and party sequence 1, spanning all twelve months. X and Y each have two blanks. This establishes extract shape, not unique crashes. No publisher event ID appears in its header. Nonblank event death/injury fields coexist with first-party personal injury coding, so neither row count nor vehicle-code grouping should be presented as a full victim census. The exact CSV and aggregate-only parsing method above support reproduction; CSV SHA256 `61f0bdb52a49176746ab8b66926224b294498c9e26b2dec6eefe44906fdffa0c`.

The post-2023 form separates incident-level casualty counts (form I) from party-specific injury/type (form II). Party injury codes distinguish death within 24 hours, injury, no injury, unknown and death within 2–30 days. Importantly, the current linked form I shows 24-hour casualty boxes but no separate 2–30-day death box, whereas the CSV still includes that column. The form alone does not establish how that export is maintained or whether injuries overlap later deaths. Fresh missingness: **7** blanks in death count, **10** in 2–30-day deaths and **1** in injuries; do not convert blanks to zero or reproduce official CBI without a publisher mapping. These are reproduced missing-field counts, not mortality totals. [S13](https://www-ws.gov.taipei/001/Upload/467/relfile/32284/5040008/7ddb52e9-ebae-4834-b41a-5f41d5074279.pdf)

All inspected CSV observations are real published historical records; no simulated inputs were generated. Municipal engineering expectations are official assessments/models where identified. Counts are not risk without exposure; first-party codes are neither all road users nor a safe basis for blame or vulnerability rankings. Coordinate CRS and boundary validation remain missing, so no spatial join or geocoded site ranking is claimed.

#### Compact reusable source ledger

All retrieved **2026-10-13**. Methods: **H** = current HTML/text inspection through web and/or curl, not search snippets; **P** = full PDF download/text extraction, relevant pages visually inspected where stated; **C** = complete CSV GET and in-memory aggregate parse. Public access succeeded without login/payment. Unless explicitly stated, redistribution license was **not established**; links and attributed paraphrases are used. Search results were leads only.

| ID / publisher / exact source | Inspected scope, period/unit | Access, license, limits/contrary evidence |
| --- | --- | --- |
| S01 / organizer / [市政 debug松](https://puma.taipei/hackathon) | H: free-topic/rules sections, current event page | Public curl; content license unknown; organizer scope only |
| S02 / MOTC road-safety platform / [肇事熱點](https://roadsafety.tw/AccLocCbi) | H: selectors, data notes; case/site units; years/months available in markup | Curl after web timeout; license unverified. A1/A2 excludes A3; intersection plus near-corner 10 m definition, address-positioning error; no exposure. Current dashboard warning identifies preliminary 2023–2025/2026 Jan–July results; ranking execution not tested |
| S03 / Taipei Songshan District / [May 2025 meeting record](https://www-ws.gov.taipei/001/Upload/324/relfile/13900/9379464/88d1e364-a8d8-49f4-89fa-8f8d826f50d1.pdf) | P: cover and pp. 2–3 rendered; April comparison and 2025 Q1 hourly intersection chart | 15-page PDF; chart raster not fully text-extractable. License unknown; existing local capability, not observed preparation pain |
| S04 / Taipei DOT / [透過事故分析，戮力改善危險路段](https://dot.gov.taipei/News_Content.aspx?n=C41A7FC0570A20B3&s=F8170E663DA380C4&sms=72544237BBE4C5F6) | H: local workflow and aggregation explanation, 2012 historical road/site cases | Curl body; license unverified; contemporary applicability unknown |
| S05 / Taipei City / [quarterly hotspot-review direction](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=A98F53BA5A65D451&sms=72544237BBE4C5F6) | H: 2015 management statement | Curl body; license unverified; criticism attributed, not a workload study |
| S06 / Traffic Engineering Office / [2025 engineering announcement](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=E3E2C3DF697050ED) | H: named geometry, mechanisms, alternative appraisal | Curl body; license unverified; official engineering/model claims not independently reproduced |
| S07 / Taiwan Vision Zero Alliance / [2025-10-03 original statement](https://www.tvza.org.tw/新聞稿/News2025/20251003) | H: specific post-conversion reported concerns | Original community publisher; license unknown; advocacy/source-selection bias, not incident prevalence |
| S08 / Traffic Engineering Office / [2026 comparison-window response](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=BEDD9D580E1DE92A) | H: through 2026-05-20 versus prior three-year baseline and disputed seasonal comparison | Curl body; license unverified; attribution, no independent outcome replication |
| S09 / Traffic Engineering Office / [Gongguan improvement source index](https://bote.gov.taipei/Content_List.aspx?n=0BF59FDB6FCCE759) | H: review-record/presentation index | License unverified; linked contents not audited; evidence is already partly consolidated |
| S10 / IOT / [2023 inspection-checklist research](https://www.iot.gov.tw/zh_tw/archive/pub/reports/-47122178) | P: linked 93-page report §§3.4–3.5, 4.1–4.2; two Kaohsiung 2022 pilots, practitioner feedback | Free linked PDF despite printed-book price; license unverified. Geographic transfer limit; operator approval of existing duration is contrary evidence |
| S11 / IOT / [current method/guidance summary](https://www.iot.gov.tw/zh_tw/more_announcement/創新路口事故分析與改善技術-99404448) | H: 2025-09-15 update, design reference/checklist evolution | License unverified; 2023 prototype is not assumed current standard |
| S12 / Taipei Police Traffic Division / [dataset 130110](https://data.gov.tw/dataset/130110), [2025 CSV](https://data.taipei/api/dataset/2f238b4f-1b27-4085-93e9-d684ef0e2735/resource/83d6d29c-6801-41a2-95c6-47d551646db3/download) | H+C: catalog annual 2012–2025 resources; 2025 extract headers, month/party/missingness | Free, catalog OGDL v1.0. No event ID/full-party linkage, privacy-sensitive attributes excluded; annual refresh; observation year differs from 2026 metadata date |
| S13 / Taipei Police linked form / [post-2023-07-01 codebook](https://www-ws.gov.taipei/001/Upload/467/relfile/32284/5040008/7ddb52e9-ebae-4834-b41a-5f41d5074279.pdf) | P: four pages; pp. 1/3 visually inspected, incident versus party fields | Public; standalone redistribution terms unknown. Not a complete export transformation specification |
| S14 / national platform / [OGDL v1.0](https://data.gov.tw/license) | H: grant, attribution, disclaimer sections | Redistribution/adaptation permitted for covered data with attribution; not automatic coverage of every linked article/figure |
| S15 / IOT / [2025 improvement-program review](https://www.iot.gov.tw/zh_tw/archive/pub/reports/-8910095) | H: July 2025 publication abstract; national financing/capacity findings | Free abstract; license unverified; full report not audited, national findings cannot be imputed to Taipei |

**Verification:** all 16 distinct report URLs returned HTTP 200 in a fresh GET check; this checks reachability, while the inspections above establish the stated content. Task-owned aggregate/link receipts, downloaded documents and inspection images are disposable after durable integration; the source links and inspected methods remain here.

**Integration consequence:** revise C01's generic-map value claim, replace arbitrary usability acceptance with a baseline comparison, retain annual-data/codebook limits and mark decision usefulness insufficient. Preserve its candidate identity; selection remains an owner decision. No application test suite applies to this research-only report.

### T08 C02 senior meals and C06 childcare

Research observation: **2026-10-13**. The twelve-district calculation is preserved unchanged. Four decisions: meal planning, resident meal access, parent choice and municipal childcare planning. No implementation, API inference, account, registration, contact or payment.

#### Findings and disposition

- **Supported:** local meal-service implementation barriers include premises, suppliers, operator willingness and reaching residents who cannot attend. Original interviews and an operator's account support these mechanisms; their citywide prevalence in 2026 is unknown [T08-S02, S03, S16]. Inventory ratios do not establish shortage.
- **Refuted:** basic childcare discovery is an unserved feature. Taipei already offers address/district/type searches, fees and dated assessments [T08-S07]. **Unresolved:** parent difficulty or willingness to use another presentation. A discrepancy supports source-reconciliation research, without proving value.
- **Supported:** richer alternatives exist beyond the previously audited CSVs: current childcare capacity/enrollment and meal-day information are public [T08-S12, S15]. **Refuted:** their mere presence establishes available places, eligible demand or current acceptance.
- **Defer** automatic shortage rankings, vacancy recommendations and “best center” scores. **Continue only as bounded hypotheses:** source reconciliation and a human-reviewed investigation checklist. No topic selected.

**Fit:** independent free-topic workflows under current organizer rules, including disclosed simulation [T08-S01]. C02 overlaps C03/C04 population/access context; C06 overlaps transport/commuting context, while decisions remain distinct. Evidence depth is unequal: childcare received a full-roster parse; meals received purposive correspondence checks and operator-page reads. No user task was observed.

#### Reusable source ledger

All sources below were retrieved on **2026-10-13**. `GET` means current publisher content, not a search snippet. `P` means Taipei Social Welfare's [website reuse declaration](https://dosw.gov.taipei/cp.aspx?n=8E5BB52262D3A54D&s=B1A7C295503FEBEA): attribution required, with exclusions for specifically restricted third-party works and personal data. Separate map-service rights remain unknown. Contacts and personal names are omitted.

| ID | Exact original source / publisher | Inspected material, method, period/unit | Rights, limits and contrary evidence |
| --- | --- | --- | --- |
| T08-S01 | PUMA, [2026 civic hackathon](https://puma.taipei/hackathon) | curl GET + HTML text; issues/free-topic and rules | Website redistribution unknown; organizer assertions attributed. No participation action. |
| T08-S02 | Chang Mao-nan / NTU, [Research on the Execution of Elderly Health Promotion Policy in Taipei City](https://politics.ntu.edu.tw/wp-content/uploads/2018/07/finalP05322022.pdf), July 2018 | Original thesis, printed pp.99–103 methods and 116–120 meal analysis; web full PDF text. Interviews with officials, experts and older users; Taipei | Redistribution unknown. Historical qualitative/local evidence, not representative 2026 need; premises/reach barriers oppose a mapping-only explanation. |
| T08-S03 | JJS Association, [elder care](https://www.jjs.org.tw/elder-care) | Current operator page, GET; Nan-jichang communal meals, pickup and delivery descriptions | All rights reserved; link/paraphrase only. Undated self-report, no audited attendance/outcomes. |
| T08-S04 | Taipei Social Welfare, [135495 meal catalog](https://data.gov.tw/dataset/135495), [CSV](https://data.taipei/api/dataset/fe55795c-a220-4b88-bde1-5b994321f8af/resource/86d839db-85c7-48b0-991b-dc86922eb093/download) | curl + standard-library CSV: 62,304 bytes, 440 rows; serial/name/district/code/address/contact; no row observation date | National catalog re-read: OGDL v1. Facility inventory, no meals/seats/attendance; shared addresses occur. |
| T08-S05 | Taipei Social Welfare, [meal service page](https://dosw.gov.taipei/News_Content.aspx?n=222C9779823FA161&s=10DED4DB1CD357DC), [115.08 PDF](https://www-ws.gov.taipei/001/Upload/358/relfile/17939/4155558/f2547c51-e66e-4452-a14d-60a33d874e50.pdf) | GET; 457,113 bytes, 12 pages; pdfplumber tables, Poppler text/render. August 2026 site/village/type/address list; page says age 60+, no documents | P. Type/service slots do not specify meal weekdays, capacity or active attendance. Listing is not operational verification. |
| T08-S06a | Taipei Social Welfare, [121337](https://data.gov.tw/dataset/121337), [public CSV](https://data.taipei/api/dataset/9c9a3f77-8340-48d8-bc0e-f9155521b758/resource/a02ccc34-dd28-4c5d-b527-c5433ec1a453/download) | GET/CSV: 3,562 bytes, 29 rows; type/name/收托人數/address/contact; no row date | OGDL v1 re-read. Count label alone is ambiguous; one sampled value conflicts with September roster. |
| T08-S06b | Taipei Social Welfare, [121278](https://data.gov.tw/dataset/121278), [private CSV](https://data.taipei/api/dataset/081df75e-85c7-464c-b125-546920911c5c/resource/e7cdaca3-e9da-46f9-b857-395e6e8e06a6/download) | GET/CSV: 28,984 bytes, 223 rows; type/name/postcode/address/contact and empty trailing header | OGDL v1 re-read. No capacities or observation dates; not whole childcare system. |
| T08-S06c | Taipei Social Welfare, [156685](https://data.gov.tw/dataset/156685), [assessment CSV](https://data.taipei/api/dataset/e7b45593-9d44-469c-97fa-f1a52c69ebaa/resource/43c0bdc5-ddb0-40bf-accd-a096d8c5ac23/download) | GET/CSV: 21,520 bytes, 292 institution rows; district/code and ROC110–114 (2021–2025), no shared facility ID | OGDL v1 re-read. Blank years, closures and guidance notes coexist with grades; 2026 results absent. |
| T08-S07 | Taipei Social Welfare, [baby map](https://map.dosw.gov.taipei/taipeiWelfare_map/all_new/baby_map.aspx?ccms_cs=1); its [layer 6 schema](https://arcgiserv.gov.taipei/server/rest/services/SL/THEMEMAP_NEW/MapServer/6?f=pjson) | curl HTML/controller/schema; public `query` endpoint, selected nonpersonal fields; Orca browser search controls inspected | Layer copyright blank; bulk redistribution permission unknown. UI labels `babycount` intake **ceiling**. Search did not complete in this browser session; API access worked. Mixed service categories require filtering. |
| T08-S08 | Taipei Social Welfare, [public-center service/admissions](https://dosw.gov.taipei/cp.aspx?n=8fc706ae75a8d802&s=259FD803E23234D6); [registration portal](https://welfare.gov.taipei/Nursery/) | Current GET; eligibility, priority, application limits, notice/acceptance, hours; portal redirects to login | P for service page; portal reuse unknown. Procedure proves rules, not parent difficulty; no login or application. |
| T08-S09 | Taipei Social Welfare, [assessment page](https://dosw.gov.taipei/News_Content.aspx?n=754B679D07789088&s=8F3A87EEBC671E8B), [public 115/9 results](https://www-ws.gov.taipei/001/Upload/358/relfile/17950/3171134/2d000a59-4853-4610-a4e5-41e78488f1f2.pdf), [private 111–115 results](https://www-ws.gov.taipei/001/Upload/358/relfile/17950/3171134/23bc49f2-af47-4ee7-ba77-82f09ec44411.pdf) | Live curl HTML differs from web's older cached attachments. PDFs 115,309/630,796 bytes; tables/text and public page rendered; institution/year/grade/domain score bands | P. Private latest file includes corrected guidance status. Public footer still says three-year cycle. |
| T08-S10 | Taipei Laws, [assessment/rewards regulation FL036157](https://laws.gov.taipei/law/LawSearch/LawArticleContent/FL036157) | GET, current 2026-03-25 amendment, arts.5–9 | Official law text; reuse declaration linked but not separately audited. Current art.7 says four years with exceptions; not the three-year indicator revision cycle. Grades are administrative assessments, subject to revocation/correction. |
| T08-S11 | Taipei Social Welfare, [public-center list](https://www-ws.gov.taipei/001/Upload/358/relfile/16495/116142/cbc57fdf-019d-4c07-b7ba-69ff2a4288bd.pdf) | GET, 91,277 bytes, two pages; name/收托人數/founding date/operator/address | P. No snapshot date in inspected table; differs from newer full registry. |
| T08-S12 | Taipei Social Welfare, [current registry page](https://dosw.gov.taipei/News_Content.aspx?n=754B679D07789088&s=E98851957DAB63AE&sms=A9E1F2A9FDEB0E62), [11509 PDF](https://www-ws.gov.taipei/001/Upload/358/relfile/17950/3171139/f346574f-7998-47e3-9b66-f0651a379238.pdf) | Current GET, 16 pages, explicitly **2026-09-30**; pdfplumber all tables and rendered page 2; facility/type/address/approved intake/actual enrollment/core hours/fees/assessment | P. Monthly reported snapshot, not attendance observation or current offerable vacancies; home-based nannies outside this institution roster. |
| T08-S13 | Taipei Social Welfare, [147154 catalog](https://data.taipei/dataset/detail?id=aeaaa517-089c-42a7-ad5b-60fef89c3545), [quasi-public CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=75bb5396-4880-4301-9dde-2f7ccae00d57) | GET/CSV: 34,764 bytes, 215 rows; approved/actual enrollment, assessment, district; file timestamp 2024-12-20, metadata 2025-12-11, no row period | City license link, exact national license not re-audited. Accessible historical alternative; do not silently merge periods. |
| T08-S14 | Taipei RDEC, [December 2025 poll release](https://tct.gov.taipei/News_Content.aspx?n=B4C9AF5D5D4BF947&s=434A63C92CC8645C&sms=72544237BBE4C5F6) | Live curl/HTML text; Dec.15–17 residential-phone survey, published n=1,071 adults, weighting described | Redistribution unknown. Reports subsidy/work-care/place priorities and substantial policy satisfaction; not specifically under-two parents or search-task study. |
| T08-S15 | Jianshun operator, [2026 Nangang sites](https://jianshun.org.tw/3/service_detail/30); city [ESP site 3869](https://esp.gov.taipei/openData/orgInfo/3869) | Original operator table GET: separate opening/meal weekdays; ESP current curl includes week Oct.11–17 and services | Operator explicitly prohibits copying; link/paraphrase only. ESP reuse unknown; changing displayed week is not a verified activity timestamp. No accepting-new-user field. |
| T08-S16 | Taipei Social Welfare, [2023-06-21 minutes](https://www-ws.gov.taipei/001/Upload/358/relfile/18001/9002854/a5fb897a-18f6-4afe-888b-fa433485e196.pdf), [2025-09-03 minutes](https://www-ws.gov.taipei/001/Upload/358/relfile/18001/9471497/8b98c147-b3fc-4443-a732-21ee6544ad65.pdf) | Original PDFs/web full text, printed pp.4–5 and p.4 respectively: premises/operator constraints, attributed shift-worker complaints, demand-analysis instruction | P. Statements/questions in minutes, not completed demand studies; employer-survey percentage not independently verified and not used here. |
| T08-S17 | Taipei Audit Office, [2024 Social Welfare audit opinion index](https://auditreport.audit.gov.tw/Book/ChapterOpinion/638890594975314669cb3eb49f56ae4627bd6395edd6eb6e93) | Original index GET via web: supply-target, staffing/incentive problems. Full PDF too large for web; curl/browser met Imperva/CAPTCHA | Detailed rates/waitlist numbers remain **unverified leads**, excluded from findings. No CAPTCHA bypass. Reuse unknown. |
| T08-S18 | Taipei Social Welfare, [2025–27 assessment indicators](https://www-ws.gov.taipei/001/Upload/358/relfile/17950/3171134/bfd98594-e5de-41a1-8d62-d021726f73bb.pdf) | GET, 616,912 bytes; administrative, care-activity and health/safety domains; selected operating/personnel-record checks | P. Three-year indicator edition is not proof of annual evaluation or individual safety. |

#### Completed bounded evidence experiments

The screen tested source correspondence and semantics. A wrong identity, erased status note or invented vacancy is unacceptable because it can misdirect a family; a missing match must remain missing. Purposive difficult cases do not estimate prevalence. No universal 95% threshold is retained.

**Meals:** ten CSV IDs `1,2,3,10,89,90,112,113,162,306` cover a service center, basement, long institutional names, two co-located pairs and the JJS operator. Removing only whitespace from extracted PDF cells reproduced all ten name/address correspondences. This supports transcription correspondence, not independent current activity. IDs89/90 share an address but have different operators/types; collapsing them automatically would erase information. The service page's age60 eligibility also differs from the preserved calculation's age65 denominator. **Disposition:** retain that dated inventory comparison unchanged; reject interpreting it as eligible-population coverage or shortage. Current meal volume, participation and accessibility remain unresolved.

**Childcare:** first ten public CSV records plus six initial private records and four branch/guidance cases produced 19 unique normalized name/district assessment matches and one unmatched newer public center, Jilin (opened 2025). Normalization removed city/private prefixes and whitespace; private branch names remained distinct. The current public assessment PDF also omits Jilin, while the current registry lists it: missing assessment is not failure. Ten private matches were checked against the current assessment tables; neither name/district matching nor their lack of addresses proves legal identity continuity.

The ten public names were queried through the map's observed layer endpoint with `name,babycount,teamYN,score_year,score,town`, no geometry or personal fields. Nine count values agreed with the old CSV; Minglun was 40 versus36. The explicitly dated registry resolves the operative comparison toward36 approved/36 enrolled; the undated list is not a competing current capacity observation. Daan's map says ROC112/2023甲等, while the current assessment PDF says ROC115/2026優等. Rendered year columns confirmed this is not extraction drift. Current law's four-year interval and the PDF's three-year footer remain a documented conflict; do not automatically flag a center overdue from the footer [T08-S06–S12].

**Municipal counterexample:** parsing every table of T08-S12 yielded consecutive unique serials1–314. Publisher-reported ordinary public centers:29, approved/enrolled1,244/1,244; public homes:64,772/772; ordinary private centers:213,6,714/4,669. Employer/agency-attached categories were kept separate. No parsed enrollment exceeded approval. This reproduces a reported snapshot pattern, not independent occupancy observation; it refutes a uniform citywide “all institutions need more capacity” inference. It establishes neither demand satisfied nor currently saleable places. Reproduction uses the exact linked dated roster, every extracted PDF table, consecutive serial checks and category-preserving sums; temporary sources/helpers are retired after durable integration. No shortage result was calculated.

#### T08 C02-A — Meal planning and inventory

**Problem/user/decision.** Historical researcher interviews identify operational and reach barriers; 2023 minutes explicitly record premises and applicant willingness as constraints [T08-S02, S16]. These support a real service-development problem. The hypothesized user is a Social Welfare/district coordinator deciding which **existing listed sites in one district** need verification before the next planning meeting. Spreadsheet burden is unobserved. Addressed problem: a defensible audit queue; premises, recruitment and reaching housebound people remain unresolved.

**Baseline/action.** The baseline combines published lists, district officers, operator schedules and welfare-map layers. Its HTML includes population/planned-facility tools; outputs were untested. Input: dated inventory and target district → assess co-location, service type and unverified activity → coordinator requests a site check → observable output: a source-linked list with questions and responsible follow-up. No automatic new-site order.

**Success/rejection/validation.** Success requires less preparation effort than this baseline while preserving every action-relevant exception. Problem rejection is **supported for a map-only remedy**: premises/operator capacity can dominate. A useful audit queue remains **unresolved**, not disproved. Data rejection is **supported for shortage claims** because rows omit meals, seats and attendance. Ten-row correspondence passed only its narrower question. The decisive next experiment is one district packet with every changed/ambiguous row, compared with the coordinator's existing packet; no allowable false merge, and efficiency must improve without omitted issues. Practitioner comparison is infeasible in this no-contact dispatch.

**Dependencies/claims/adoption.** T08-S04/S05 and registered population support inventory context; schedules, actual participation, current operator confirmation and accessible entry are required for service adequacy. Age65 ratios stay proxies. Demonstration **specified** as an audit checklist; decision **insufficient**; nutritional/social outcomes unknown. A 100-day adopter needs the senior-welfare unit, district/operator stewardship and domain judgment; collection permissions, staff time and maintenance cost are unknown.

**Presentation/next check.** Before: two Xinlong rows appear like two independent venues. Action: show their shared address and different types without deleting either. After: one venue-verification question is recorded, with two provider records retained. Next: compare those two published records against their current public operator activity calendars to establish whether their meal sessions overlap; absence of calendars leaves overlap unresolved.

#### T08 C02-B — Older resident or helper choosing a meal service

**Problem/user/decision.** JJS describes distinct communal, pickup and delivery services for people with different mobility/preferences [T08-S03]. This is operator-observed need, not evidence that residents cannot search. A hypothetical older Nangang resident/helper needs a meal on a named weekday next week. The resident chooses an option to verify; the operator decides acceptance. A nearby point does not grant access.

**Baseline/workflow.** The current city list/ESP, district officers and Jianshun's published meal weekdays already support discovery [T08-S05, S15]. Input: weekday, district and desired communal/pickup mode → compare **meal days**, entry conditions and missing fields → user confirms with operator → output: confirmed attendance arrangement or recorded rejection. No contact occurred here. Prices, booking lead time, eligibility, free seats, dietary suitability and step-free entry must be known before claiming a usable option.

**Success/rejection/validation.** Success is avoiding a wasted visit versus reading the current pages and calling. Problem rejection is **unresolved**: information may help, but mobility, preference and capacity can remain decisive. Data rejection is **supported for an immediately bookable recommendation**: current inventory cannot establish acceptance. It is **refuted for the narrower assertion that no public meal-day information exists**. The smallest comparison uses one weekday case plus Sunday and a housebound case; these distinguish weekly opening from meals and attendance from delivery. The desktop check found Jianshun explicitly separates those schedules; no booking/visit outcome was observable. Resident-task speed is infeasible without an authorized participant.

**Claims/readiness/adoption.** Link to operator text rather than redistribute its restricted table. A source-backed call checklist is **specified**; suitability decision **insufficient**; improved nutrition/isolation unknown. A 100-day path needs operator-owned updates and an offline/helper route; staffing, update burden and accessible entry verification costs are unknown.

**Presentation/next check.** Before: the 重陽 site at 臺北市南港老人服務暨日間照顧中心 is listed as open Monday–Friday. Action: show that its operator lists meals Tuesday/Thursday and mark price/acceptance unknown. After: Monday is rejected from the published schedule, not from an invented availability estimate. Next: inspect that center's own current public admission/meal notice for those missing conditions; otherwise retain a confirmation-required linkout.

#### T08 C06-A — Parent childcare choice

**Problem/user/decision.** The 2025 poll supports cost/work-care/place concerns, while also reporting policy satisfaction [T08-S14]. It does not validate an information bottleneck. Hypothesis: a parent returning to work must choose which eligible center to visit/apply to. The parent controls applications; admissions staff control eligibility, priority and an actual offer. Current rules include residence/age qualifications and generally one large public center plus one public home, so a geographic shortlist alone can be misleading [T08-S08].

**Baseline/workflow.** Compare the existing baby map, current registry, dated assessment attachments and official application portal. Input: coarse district, start date, hours and service type → reconcile current source versions and identify missing offer conditions → parent requests confirmation/visits and applies through the official route → output: a dated, explained application choice. Use no real family address or sensitive eligibility record in a demonstration.

**Success/rejection/validation.** Generic “nearby centers with assessments” differentiation is **refuted** by the existing feature set. A reconciliation benefit is **supported only at the data-task level** by the Daan discrepancy; parent decision gain remains **unresolved**. Data rejection is **supported for a current vacancy/best-center claim**. Ratings are intermittent administrative results; improvement/closure notes and revocation rules must survive display [T08-S09/S10/S18]. The smallest decisive task compares official baseline versus a reconciliation sheet for a changed grade, a new unassessed center, a renamed/near-name branch and an age/time-ineligible case. Identity/status exceptions must remain explicit; speed cannot compensate for eligibility or safety errors. The 20-case desktop check was completed; an observed parent comparison is infeasible under no-contact scope.

**Adoption/readiness/presentation.** A source-reconciliation demonstration is **specified**, decision **insufficient**, successful enrollment and child welfare unknown. Social Welfare and operators would need update custody, admissions expertise and an independently tested parent workflow; public-source reuse and maintenance cost remain unsettled. Before: Daan shows a 2023 grade in the map. Action: compare the 2026 official attachment without replacing it with a generic quality score. After: the parent can ask a current, specific question; no admission or safety improvement is claimed. Next: an owner-authorized observed baseline task with a parent is the decisive check; public-source searching cannot establish willingness or effort reduction.

#### T08 C06-B — Municipal childcare planning

**Problem/user/decision.** The audit index identifies supply-target/staffing issues; municipal minutes ask whether low external-care use reflects insufficient capacity and call for district analysis [T08-S16/S17]. A question is not a resolved causal finding. Hypothesized planner: Social Welfare childcare team choosing between investigating public-place pressure, private affordability/time mismatch, staffing, or a premises constraint in a bounded district planning cycle.

**Baseline/action/success.** Existing baseline includes official registries, approvals, admissions queues, population/facility maps and a commissioned demand-analysis process. Input: a common-date service-type inventory plus demand/queue evidence → assess competing explanations → planner selects a verification or policy-analysis request → output: a justified investigation brief, not an automatic construction budget. Success means a different, defensible investigation or less preparation work than the existing process. The public snapshot demonstrates differentiation but does not prove that officials lack it.

**Rejections/experiment.** Problem rejection is **supported for a blanket more-sites diagnosis**: heterogeneous reported utilization and documented time/cost/premises constraints admit rival explanations. Whether a new planning tool changes the decision is **unresolved**. Data rejection is **supported for shortage allocation**: no same-date deduplicated active demand, acceptable hours/price, staffing constraints or rejected offers was acquired. It is **refuted for purely descriptive capacity/enrollment comparison** because a dated richer roster exists. The smallest decisive experiment needs one district's active deduplicated queues plus comparable public/private/home-based supply, with cases of full public centers, below-cap private centers, shift-worker needs and duplicate/cancelled applications. Exact reconciliation of identities/periods is required; no invented shortage tolerance. Public-roster parsing was completed, but this demand comparison is infeasible without authorized aggregate operational evidence. Capacity minus enrollment is not a vacancy or unmet-demand estimate.

**Claims/adoption/presentation/next.** Keep age cohorts, continuation beyond age two, household location and actual intended use distinct from registered under-three population. Demonstration **specified** for competing explanations; decision **insufficient**; parental employment/birth outcomes unknown. A 100-day path needs departmental authority, admissions/data stewards, domain analysts and budget/staffing partners; those commitments and cost are unknown. Before: fewer listed sites appears to justify expansion. Action: separate service types and queue/affordability/time hypotheses. After: choose a demand-validation request rather than label a shortage. Next: locate the completed public report for the 2025-09-30 district demand-analysis instruction in T08-S16 and inspect its sample, deduplication and acceptable-service definition; if unavailable, defer allocation pending an authorized aggregate-data route.

#### Integration boundary

Update C02/C06 interpretations and the dataset-to-candidate index for the richer sources and version conflicts; do not overwrite the historical twelve-district observation or infer source freshness from catalog dates. The old 95%-join target should not be a universal readiness gate: Jilin illustrates a legitimate missing assessment. No human-task usability, adoption or civic improvement was observed. Private downloads are recoverability material, not permission to publish operator tables or personal fields.

Verification: all 34 cited URLs were checked with curl HEAD; 33 returned200, while the law endpoint returned405 to HEAD but its current article was read successfully with web GET. Generated page images and task browser tabs were removed after inspection; temporary source bytes and parsing helpers remain outside Git and are retired after durable integration.

### T09 C04 shelter inventory reconciliation and C05 rainfall-scenario preparedness review

Research observation: **2026-10-13**, Taipei time. Scope: two separate pre-disaster workflows; no application, registration, contact, payment, API model inference, live evacuation instruction or individual-facility safety classification. These are preparedness research findings, not operational instructions.

#### Findings, fit and contrary evidence

**Supported — a concrete administrative problem exists historically.** Taipei's 2023 fiscal-year audit found inconsistent shelter information across published lists, district evacuation maps and the city disaster app, and questioned basement locations designated for flooding. Its 2024 fiscal-year follow-up records improvement, rather than establishing that those specific defects persist ([S01][T09-S01], [S02][T09-S02]). Separately, the Taipei Audit Office's September 2025 account describes incorrect/out-of-city shelter information in the Hydraulic Engineering Office's LINE service and reports correction, including adding 47 Taipei locations ([S03][T09-S03]). These are observed audit findings and reported remedies; they neither measure practitioner frustration nor prove a new tool would improve outcomes.

**Supported — present public sources still require reconciliation.** The current Education open-data file, Education website attachment and April 2026 water-disaster protection plan differ in at least the inspected fields described below. These are source inconsistencies, not proof that any location is currently unsafe or available. **Refuted:** “newest catalog timestamp establishes one operational master” and “all listed capacity is simultaneously usable.” Education's own notice says residents must confirm actual opening through district/village channels and not every listed place opens ([S04][T09-S04]).

**Unresolved — incremental practitioner value.** The city already publishes inventories, district procedures, disaster maps, app links and a staff collaboration platform. No practitioner task observation, internal-system access or time comparison occurred. Missing public evidence does not disprove pain; it prevents a supported decision-readiness claim. A June 2026 Da'an operator announcement describes an overnight, unscripted shelter exercise with university/community/volunteer participation and a feedback meeting; the district chief attributes a large-disaster capacity shortfall to the existing priority-school arrangements ([S05][T09-S05]). This is an operator assertion and planned-exercise account, not independently measured unmet demand or an after-action effectiveness result.

**Fit — inference.** Both are the organizer's free-topic branch, with overlap with building resilience through preparedness and accessibility, not a substitute for structural assessment. The current event page permits disclosed simulated inputs and calls for operable demonstrations; it does not validate either problem ([S06][T09-S06]). C04 owns who maintains and reconciles listed information; C05 owns what a verified facility reference point and operating arrangements imply for a professional review under an official modeled scenario. They can share provenance but require different actions and success measures. Evidence depth is unequal: C04 has current source comparisons and local operational audits; C05 has complete public-file technical checks but no validated facility-location join or practitioner decision experiment. Neither is selected.

#### Source ledger

All retrievals below occurred **2026-10-13**. “Web” means opened original full content, not a search snippet; “GET” means direct curl download. Catalog dates are metadata, not observation dates. Mirrors are not independent corroboration.

| ID / original publisher and title | Exact inspected material, period/unit and method | License, access and limitations / contrary evidence |
| --- | --- | --- |
| [S01][T09-S01] Taipei Audit Office, 112年度消防局主管審核意見 | Three-page original PDF, printed pp.152–154; web full text, especially shelter subsection pp.153–154. Audit references February 2024 inventory and earlier preparedness work; institutional and district units. | Resource-specific reuse terms not established; cite/paraphrase only. Historical nonconformities and source conflicts; agency response reports map/app correction, limiting claims of continuing defects. |
| [S02][T09-S02] Taipei Audit Office, 113年度消防局主管 | Two-page original PDF, printed pp.149–150; web full text. October 2024 indoor-area/capacity audit and prior-year follow-up. | Redistribution unknown. Describes capacity revisions and corrected information; audit's denominator/indoor-area method cannot be transplanted to undefined current spreadsheet fields. |
| [S03][T09-S03] Taipei Audit Office, pumping automation and public shelter-information correction | Original HTML main article; web, dated 2025-09-11, recounting July/September 2024 checks and subsequent follow-up. | Specific terms unverified; paraphrase only. Pump failures are also a rival explanation for flooding; corrected LINE defects are not a current failure rate. |
| [S04][T09-S04] Education Department, 115年臺北市避難收容處所一覽表 | Original notice main text, updated 2026-03-12; web. [Attached 1150224 ODS][T09-WEBODS]: GET, ZIP/XML parse in memory, 87,422 bytes, 419 SA-ID rows. | Website declaration allows attributed reasonable research use, not a blanket open license for every attachment. No contacts retained in report; attachment comparison used institutional fields only. No opening/occupancy feed. |
| [S07][T09-S07] Education Department, open-data shelter inventory, national ID134683 / city aaf97773… | National catalog full web; metadata 2026-09-14. Exact [resource][T09-EDU]: GET, 88,568-byte ODS despite CSV label; XML SA-ID rows, hazard/accessibility/service villages/capacity/maximum/area; citywide institutions, no XY. | National catalog explicitly OGDL v1, free, irregular updates. File-format and catalog-schema mismatch; stable ID in this snapshot does not prove stable longitudinal identity. |
| [S08][T09-S08] Social Welfare Department, 114年 inventory, national ID135484 / city f327232d… | National catalog web, metadata 2025-12-12; exact [CSV][T09-SOC]: GET/full csv.DictReader, 77,891 bytes, 399 rows, district/name/hazard/service villages/capacity/area, no SA ID or XY. | OGDL v1/free in national catalog. Older year, different publisher/schema; no explicit supersession statement found. |
| [S09][T09-S09] Taipei City Government, 115年度水災危險潛勢地區保全計畫, WRA-hosted | Exact current PDF GET, 60 pages, cover April 2026; pdftotext; rendered and visually inspected Appendix 1, printed p.21, PDF p.24. Also inspected chapter 2 and Appendix 7 printed pp.34–35. Model map / institution-address list. | Document-specific redistribution unknown; cite limited findings. URL was indexed as older material, but retrieved cover is 2026: URL/date alone is not immutable provenance. Appendix 7 gives addresses, not verified entrance XY. |
| [S10][T09-S10] Hydraulic Engineering Office, 112年 rainfall accumulation scenarios, ID121550 / fa1e8012… | Original catalog web/GET, WGS84; metadata 2026-09-09, modeled year 112. Three exact KML GETs and full XML/geometry inspection: [78.8][T09-K78], [100][T09-K100], [130][T09-K130] mm/h. Fields GRIDCODE, depth, case, year, AGENCYCODE; polygon units. | OGDL v1/free. Catalog omits runoff below 15 cm, warns against prediction of individual storms and land-use determinations. Official modeled evidence, not observed floods; no forecast confidence or local validation errors supplied. |
| [S11][T09-S11] Taipei EOC, map information system | Original HTML web, water panel: historical floods and 78.8/100/130 layers, district selection and map tools. | Portal layer-specific redistribution/version not verified. Inspected interface controls, not rendered current layers or feature services; 130 panel wording groups depths differently from KML. |
| [S12][T09-S12] Disaster Prevention Office, 80th work meeting, 2025-07-31 | Original 20-page PDF web, conclusions and tracked shelter items. Minimum staffing, backup plans during reconstruction, simultaneous opening exercises. | Redistribution unknown. Some staffing/backup items closed in meeting; continued deficiency cannot be inferred solely from their presence in the tracker. |
| [S13][T09-S13] Taipei law system, emergency evacuation and shelter plan | Current consolidated administrative rule, amended 2022-09-07; web plus GET PDF/pdftotext, investigation and task-allocation provisions. | Rule text provides authority, not evidence of inconvenience or compliance; no full attachment redistribution asserted. |
| [S05][T09-S05] Da'an District Office, university shelter-opening exercise announcement | Original EOC-hosted operator article web, June 23/24 2026 publication; planned June 24–25 exercise and participant roles. | No resource-specific license checked. Describes intended training and attributed capacity concern; no completed performance measurement. |
| [S14][T09-S14] Zhongzheng District Office, village-office list | Original page web; inspected first 12 listed village names only, including the 9 names attached to SA100-0002. | Terms unverified; names used solely for bounded administrative spelling check; pagination prevents a district-wide coverage claim. Personal contact columns excluded. |
| [S15][T09-S15] MODA, OGDL v1 | Original license full web; grant, attribution and disclaimer sections. | Redistribution/adaptation permitted for datasets released under this license with attribution; permission does not make data an official recommendation or guarantee. |
| [S06][T09-S06] Organizer, 市政debug松 | GET/full HTML text; free-topic and data/disclosure rules inspected. | Rules/source-specific licenses apply; organizer problem framing remains attributed. No activity-only citizen material accessed. |

#### T09 C04 — inventory reconciliation before preparedness review

**Problem, user, trigger and authority.** Observed pain is unreliable consistency of public operational reference information in specific audits, with potential confusion for inquiry and coordination, rather than a proven shortage of shelter-list apps. Hypothesized user: the district preparedness coordinator preparing an annual review, an exercise or a response to a revised list. The district coordinates local shelter operations; Education assists designation/data building; Public Works supports hazard assessment; Social Welfare supplies relief resources. These roles are evidenced, while the actual spreadsheet reviewer and correction approval chain remain unobserved ([S13][T09-S13]). Bound the task to **Zhongzheng's 27 current institutional records**, checking source/field discrepancies and service-village references. Exclude choosing an open shelter, allocating residents or deciding structural suitability.

**Exact baseline and bottleneck.** Existing baseline is the Education notice/ODS, the two open-data inventories and Appendix 7 of the protection plan, read side by side, then referred to the responsible district/Education unit. Already available fields include disaster suitability, accessibility and service villages; a searchable list alone adds little. The proposed contribution is an explicit discrepancy packet with source/version, district, ID/name, raw fields and unresolved interpretation. Whether this reduces effort beyond a spreadsheet comparison or internal TSAGE remains a hypothesis. Alternative causes include deliberate hazard-specific backup status, renamed/merged institutions, changed administrative assignment, publication lag and inaccessible operating floors; more data cannot create staff or suitable space.

**Success/rejection fixed for the check.** Success for research: preserve every current district row, show exact raw differences and distinguish absence from a conflict without guessing identity. Later decision success requires the coordinator to resolve the same cases with no lost consequential discrepancy and less work than the baseline; measure errors and task time, with tolerances agreed around the actual correction consequences, not an invented speed target. Problem rejection: if the authoritative internal workflow already resolves these cases and the packet changes neither effort nor correction quality, defer a new tool. Disposition **unresolved**, requiring a supervised practitioner comparison. Data rejection: if common identity, backup semantics or capacity definitions remain unresolved, reject automatic eligibility/coverage allocation. Disposition **supported for rejection of automation**, while retaining a manual inquiry workflow.

**Completed smallest experiment.** Full in-memory parsing of the [older CSV][T09-SOC] and [current ODS][T09-EDU] reproduced 399 older rows and 419 current SA-ID rows (419 IDs,418 distinct names). No contact fields were persisted in the sanitized analytic extract. For all 27 Zhongzheng rows, exact **district+name** matching found 25 older counterparts and 6 water-disaster-field differences: two 是→否 school records and four 是→是(備用) MRT records. Current district flags are 14是,4是(備用),9否; accessibility flags 26是/1否. The two unmatched cases are retained, including a university name with a compatibility-character spelling and a cross-district underground-mall assignment. This census avoids sampling away the consequential backup and unmatched cases; it does not validate their operational meanings.

The citywide comparison illustrates the join hazard: district+name gives 387 paired current rows/36 flag differences, while name-only gives 389/37, because 中山地下街 and 西門地下街 have differing district assignments across the files. The earlier canonical 386/37 figure was **not reproduced**; qualify that historical comparison pending recipe/version reconciliation rather than silently treating these denominators as interchangeable. Two same-name/same-address 雙永國小 records have different SA IDs, so even current names cannot be deduplicated automatically.

The Education website attachment matches all 419 catalog IDs and all inspected institutional fields except one site's area. More decisively, Appendix 7 of the retrieved April 2026 plan lists 螢橋國中 and 螢橋國小 as flood-shelter reference locations, while the current Education file says 水災=否 for both. This supports a present **publication-consistency question**, not an assertion of incorrect designation. For SA100-0002, all 9 service-village names occur in the inspected district-office page; this validates those spellings only. The 31-person capacity is one facility attribute shared by its listed villages; no capacity was multiplied across villages or equated to demand.

**Input → assessment → action → output.** Dated source files and the district filter → exact ID/name/field comparison with unmatched rows → coordinator asks the designated data owners to confirm scope and intended revision → an owned correction/confirmation record and a checked downstream-publication list. Research prepared the questions; no inquiry was sent. “Accessibility=yes” does not establish a usable toilet, lift during outage, flood-accessible entrance or ability to accommodate a particular person. Population/65+ joins are unnecessary for this reconciliation and remain unvalidated for demand allocation.

**Readiness, adoption and presentation.** Demonstration **specified** as a discrepancy-review table; usability untested. Decision **insufficient**; no practitioner comparison or authoritative conflict disposition. Civic benefit, fewer mistaken inquiries or improved evacuation outcomes **unknown**. Within 100 days, Education/district publication ownership and Social Welfare/operator staffing would need agreement; expertise in shelter operations and accessibility, update labor and cost are unknown. The 2025 meeting's staffing/backup closures are contrary evidence to assuming nothing has been addressed ([S12][T09-S12]). A bounded before/action/after example is the two 螢橋 records: before, conflicting published fields; action, prepare dated verification questions for the responsible owners; after, an unresolved-confirmation packet with no safety label. **Next executable check:** compare those two institutional entries and their stated revision dates against Zhongzheng's latest publicly posted flood shelter/evacuation maps; record agreement or publication mismatch, without contacting anyone.

#### T09 C05 — facility preparedness review using official modeled rainfall

**Problem, user and decision.** The historical audit establishes that shelter designation and hazard context have needed joint review; it does not establish that a new overlay workflow is missing ([S01][T09-S01]). Hypothesized user: district planner working with a facility manager and Public Works technical assessor before a drill. The decision is whether to request examination of a verified entrance/operating-floor arrangement and an accessible alternative under a named scenario. Designation/opening stays with authorized agencies. Overlap with C04 ends at source identity and semantics; C05 must independently establish spatial/operating relevance.

**Baseline and required evidence.** EOC already exposes scenario layers alongside historical events, and the catalog supplies KML for desktop GIS ([S11][T09-S11], [S10][T09-S10]). An additional colored flood map is redundant unless it improves an actual review. Required evidence is a confirmed inventory version, independently verified entrance references/footprints, operating floor/elevation and barriers, relevant approach access, model scenario/legend and a human review decision. No verified entrance coordinates were obtained from the inspected inventory or plan. Geocoding an address into a campus centroid would not close that gap. Licensing for those future coordinates/footprints and their redistribution remains unknown.

**Original method and competing explanations.** The current 2026 protection plan's Appendix 1 labels the 130 mm/h map a normal-operation scenario, identifies SOBEK, assumes functioning pumps/unobstructed drainage and no levee leakage, and explains that the numerical result is conditional. Its notes identify particular-year topographic/land-use and waterworks inputs; a new publication date does not make them 2026 terrain. The same plan combines short-duration scenarios with longer-duration rainfall and historical/local evidence for official preparedness decisions ([S09][T09-S09]). A functioning normal-operation model cannot represent pump failure, blocked drains, uneven real rainfall, subsequent works or every hazard. The separate pump-system audit therefore limits, rather than validates, event prediction ([S03][T09-S03]). Facility floors and staff may dominate action even when a nearby reference point intersects a polygon.

**Success/rejection and completed experiment.** Predefined technical success: each scenario's actual classes/fields are read, holes and boundaries are retained, and invalid geometry is disclosed rather than silently repaired. Problem rejection: defer if the existing GIS/agency assessment already produces the same review decision with equal effort, or if no manager can execute the requested follow-up. Disposition **unresolved**; no baseline practitioner trial. Data rejection: reject automatic facility classification if essential entrance/floor evidence or reliable geometry is absent. Disposition **supported for rejecting unattended classification**, not for rejecting manual preparedness review.

All three [78.8][T09-K78], [100][T09-K100] and [130][T09-K130] files were inspected, replacing the earlier one-scenario-only audit. XML Polygon counts are 1,945 /7,330 /29,738 for 78.8/100/130 mm/h. Depth classes respectively extend through 0.50–1.00 m, 1.00–2.00 m and Above 2.00 m; year=112 and case fields match each resource. Full polygon construction with all inner rings in **Shapely 2.2.0 / GEOS 3.14.1** found 9/57/287 invalid polygons, with ring self-intersections among the inspected failure examples. All outer rings were closed; none of the constructed polygons was empty. This is a complete technical census, chosen because one silently mishandled consequential polygon can change a review; it establishes no geographic error rate against reality. No geometry repair, affected-facility count or area estimate was performed. Reproduction: parse every KML XML Polygon, construct its exterior and all interior rings without repair, and count `is_valid`, `is_empty` and unclosed exteriors using the stated Shapely/GEOS versions. Inventory matching uses the exact district+name and name-only keys stated above; ODS IDs and institution fields come from ZIP/XML parsing. Temporary source/helper files are retired after integration. No facility data were simulated.

The smallest **decision** experiment is presently infeasible: no independently checked entrance/operating-floor pair and no practitioner judgment were available. Do not manufacture 10–20 campus points to simulate validation. Resume with one owner-confirmed facility case and include its uncertain entrance, boundary/hole and alternative-access cases; determine positional tolerance from source accuracy and whether the review decision changes, not an arbitrary meter buffer. Record supported/revise/defer outcomes. KML validity alone cannot prove numerical-model accuracy.

**Input → assessment → action → output; readiness and presentation.** Verified reference and operating arrangements + selected official modeled scenario → inspect class/geometry uncertainty and compare existing GIS assessment → authorized planner requests a site-specific preparedness check or drill inject → documented review reason, unresolved assumptions and responsible follow-up. No operating-site decision was executed. Demonstration **blocked** for a real facility-review claim until the reference evidence is obtained; a scenario-file audit interaction could be specified separately, but is not this workflow's decision demonstration. Decision **insufficient**, civic outcomes **unknown**. Within 100 days, Public Works model/GIS expertise and district/facility/education coordination are prerequisites; current-version stewardship, survey availability, staff effort and costs remain unknown. Before/action/after presentation: before, three files assumed interchangeable; action, inspect actual depth classes and topology; after, a reproducible scenario-specific audit with invalid geometries awaiting technical handling. This completed research example supports provenance, not facility safety. **Next executable check:** inspect the selected district's official facility evacuation-plan drawing for an entrance, operating floor and map date, recording explicit absence if no public drawing establishes them; proceed to spatial comparison only if location uncertainty can be bounded.

[T09-S01]: https://auditreport.audit.gov.tw/ServerFile/Get/63857343671535387732936c497e7f4385b7c5951a3f09fc50
[T09-S02]: https://auditreport.audit.gov.tw/ServerFile/Get/63889059497583639589f0f529507348cc8cb9f9d4732cbd98
[T09-S03]: https://www.audit.gov.tw/p/405-1000-10938,c500.php?Lang=zh-tw
[T09-S04]: https://www.doe.gov.taipei/News_Content.aspx?n=BA819C04388F2B6E&s=929AD2A327986813&sms=69B4E6B26379EE4E
[T09-S05]: https://eoc.gov.taipei/News/Detail/845
[T09-S06]: https://puma.taipei/hackathon
[T09-S07]: https://data.gov.tw/dataset/134683
[T09-S08]: https://data.gov.tw/dataset/135484
[T09-S09]: https://fhy.wra.gov.tw/disaster/Uploads/Download/%E6%B0%B4%E7%81%BD%E4%BF%9D%E5%85%A8%E8%A8%88%E7%95%AB/%E8%87%BA%E5%8C%97%E5%B8%82%E6%B0%B4%E7%81%BD%E4%BF%9D%E5%85%A8%E8%A8%88%E7%95%AB.pdf
[T09-S10]: https://data.gov.tw/en/datasets/121550
[T09-S11]: https://www.eocmap.gov.taipei/eocmap?WaterInfo=1
[T09-S12]: https://www-ws.gov.taipei/Download.ashx?icon=.pdf&n=MTE0MDczMeeBvemYsui%2BpuesrDgw5qyh5bel5L2c5pyD6K2w57SA6YyELnBkZg%3D%3D&u=LzAwMS9VcGxvYWQvNjkxL3JlbGZpbGUvNTYxMTgvOTUwODI4MC9kOWYxZGEzMC04N2QwLTQ0MWEtOTE2OC1iNDUxZTE4YmZiM2QucGRm
[T09-S13]: https://laws.gov.taipei/Law/LawSearch/LawArticleContent/FL029692
[T09-S14]: https://zzdo.gov.taipei/News.aspx?n=D7F52863BB7C9EA7&sms=D982815F3A372FF5
[T09-S15]: https://data.gov.tw/license
[T09-EDU]: https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=4c92dbd4-d259-495a-8390-52628119a4dd
[T09-SOC]: https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=3f20cc14-91a9-41de-8d03-6e019ec4d82c
[T09-K78]: https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/173adcbe-0f2e-4941-b2bc-127c09db0391/download
[T09-K100]: https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/4b14c3a0-fcf2-48d4-9c93-e27784cae29d/download
[T09-K130]: https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/2954e8d4-cb67-40c9-8ab8-019ad10b758e/download

[T09-WEBODS]: https://www-ws.gov.taipei/Download.ashx?icon=..ods&n=MTE15bm06Ie65YyX5biC6YG%2F6Zuj5pS25a656JmV5omA5LiA6Ka96KGoKDExNTAyMjQpIC0g6KGo5qC85ZCr6KGo6aCtLm9kcw%3D%3D&u=LzAwMS9VcGxvYWQvMzQyL3JlbGZpbGUvMzY5NjcvNzY0NTQzOC9iZjExYzM0OC01MjExLTQ4ZmMtOTZjOS1iMDliMTM1ZWY2Zjgub2Rz

### T10 MRT service review and C08 YouBike: three separate decisions

**Research observation: 2026-10-13 (Asia/Taipei).** Research only; no implementation, inference API, accounts, payment, publication or practitioner contact. Sources below were inspected as original publications or publisher downloads; search snippets alone are not treated as verification. Publicly documented processes do not establish analyst frustration or willingness to adopt another tool.

#### Findings, fit and disposition

**Supported:** retain the MRT hypothesis, narrowed to recurring service-review evidence. The operator's 2025 passenger survey recommends examining shorter headways on lines with more dissatisfaction about waiting, while its annual performance report says service indicators met statutory management values. These are compatible: compliance does not settle passenger experience. Neither establishes a missing analytical tool. [T10-S02][T10-S03]

**Supported:** YouBike availability difficulty has original local evidence: a transport survey records expressed interest in improving borrowing/returning availability, and the audit documents station/peak-period failures despite satisfactory systemwide performance. These are different populations and periods, not a current failure rate. [T10-S05][T10-S06]

**Refuted:** 2023 transfer rentals can represent present shortage, all bicycle demand, exact multimodal transfers or required truck dispatch. **Unresolved:** whether an auditable historical review changes an operator decision beyond existing dashboards; whether a new commuter lookup improves the already available operator, Metro and accessible transport interfaces. Preserve all three hypotheses; do not promote them to decision-supported status. [T10-S04][T10-S07][T10-S08][T10-S09]

**Fit/inference:** these are free-topic candidates under organizer issue 7, with contextual overlap with Neihu commuting (T04), bus services (T05) and accessible station approaches (C03). They do not establish bus boarding demand, street footfall or safe cycling routes. The organizer's official page was returned in original-domain search indexing, but direct web/curl reads were blocked; the topic worker could not independently revalidate fit. The integrator separately retrieved the full official event page successfully by curl/HTMLParser on the same date (see Official baseline), resolving the event-scope check without validating the civic problem. No deadline is used here. [T10-S01]

#### Reusable source ledger

All retrieval dates are **2026-10-13**. “Unknown rights” means no item-specific redistribution grant was established; cite/summarize rather than republish whole documents. OGDL v1 catalog declarations support reuse with attribution, not claims of accuracy or endorsement. Website interface inspection does not verify every native-app interaction.

| ID / original publisher and exact source | Inspected material, period/unit and method | Rights, access, quality and contrary evidence |
| --- | --- | --- |
| **T10-S01** Organizer, [市政 debug松](https://puma.taipei/hackathon#issue-7) | Official-domain indexed content lists free topic and starter MRT data; attempted web open and curl GET | Direct reads failed/403. Event content not independently downloaded; participation and claims remain attributed; redistribution unknown. |
| **T10-S02** Metro Taipei, [114 annual performance report](https://www-ws.gov.taipei/001/Upload/405/relfile/18288/132392/de6c2851-5c91-4e96-a27a-22a2b6658441.pdf), linked from [operator index](https://www.metro.taipei/cp.aspx?n=2EC550B62FFE16C2) | Complete PDF via curl; pdftotext; printed pp.1–3: 2025 network, daily ridership, line peak/offpeak headways, punctuality and legal management values | Public PDF; redistribution unknown. Operator-reported aggregate compliance cannot exclude local waiting problems or establish causal improvement. |
| **T10-S03** Metro Taipei, [114 passenger satisfaction survey](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=fa621cd2-2d90-4ed0-9c2a-397a41092a30) | Complete 13,428,984-byte PDF, curl/pdftotext; abstract, methods, sample allocation and recommendations. Face-to-face exit survey, age 15+, 2025-09-15–27, 1,079 valid responses | Item redistribution grant not checked. Sample/time/location limits; not a census or observed analyst workflow. Recommends waiting-time review, yet reports generally high satisfaction. |
| **T10-S04** Metro Taipei, [hourly OD catalog](https://data.taipei/dataset/detail?id=63f31c7e-7fc3-418b-bd82-b95158755b4d), [index CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=eb481f58-1238-4cff-8caa-fa7bb20cb4f4), [API rules](https://www.metro.taipei/cp.aspx?n=BDEB860F2BE3E249) | Curl CSV census: 116 index rows, January 2017–August 2026. Latest monthly URL sampled by Range: HTTP206, 8,192/312,474,694 bytes, schema 日期/時段/進站/出站/人次 | Operator rules reference OGDL; catalog says public/free. Full-month coverage remains unaudited. Gate OD lacks platform waiting, train occupancy, denied boarding and exit-level transfer IDs. Crowding/arrival/member APIs require application; no application made. |
| **T10-S05** Audit authority, [113 audit extract, transport pp.乙79–80](https://auditreport.audit.gov.tw/ServerFile/Get/63889289612421155881e71de3dcf04416b330afed176c7dcc) | Original two-page PDF read through web; August 2024 operator data, contracts, peak windows and agency response | Whole-report download hit bot protection; exact extract accessible. Audit found 317/1,443 operating stations below 90% seeing-bike rate despite 93.03% overall. Capacity/staffing responses existed; no 2026 inference. Redistribution unknown. |
| **T10-S06** Taipei DOT, [112 second transport opinion survey](https://www-ws.gov.taipei/001/Upload/390/relfile/52906/9012754/e0185bbd-7891-4a31-a3db-82733ac1dab4.pdf) | Complete PDF curl/pdftotext; abstract/methods pp.5–6 and YouBike section. CATI/RDD, 2023-07-26–31; 1,073 adult recent car/motorcycle drivers, weighted; reported overall margin ±3 points | Multiple-response preferences: 23.2% borrowing availability, 21.6% return availability; cycling environment also prominent. Driver population, stated intentions, not all commuters or verified lost trips. Redistribution unknown. |
| **T10-S07** Taipei DOT, [169174 transfer-rental catalog](https://data.gov.tw/dataset/169174), [December CSV](https://data.taipei/api/dataset/d51e8336-fceb-4275-a81a-2a246f4fca1b/resource/8ddb45ba-a0f5-41d6-85a0-1691096fdcf8/download) | Catalog original web read; complete CSV curl, UTF-8 CSV/datetime census in task scratch. 2023 only, twelve monthly resources; six fields: borrow/return times/names, rental duration, borrow date | OGDL v1/free. Explicitly discontinued. Bus/MRT-to-bike subset; no preceding transit station, person/trip identifier or historical coordinates. See reproduced defects below. Raw trips not saved. |
| **T10-S08** Taipei DOT, [137993 catalog](https://data.gov.tw/dataset/137993), [current JSON](https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json) | Full urllib GET/JSON parse, source time 2026-10-13 19:05:52; 1,819 unique station IDs/names, 1,791 active and 28 inactive. IDs, addresses, coordinates, status, capacity, rental/return counts and multiple timestamps | OGDL v1/free, advertised minute refresh. Twelve districts plus separate NTU campus category; not thirteen districts. Snapshot, not arrival guarantee. `Quantity` differed from rent+return in 834 rows: capacity must not be reconstructed from those two counts. |
| **T10-S09** Operators, [YouBike map](https://youbike.com.tw/region/taipei/stations/), [full-station extension](https://www.youbike.com.tw/region/i/news/service/636dadfab4d24b651b690267/), [Metro Taipower Building](https://web.metro.taipei/pages/tw/station/040), [accessible transport list](https://atis.taipei.gov.tw/aspx/park/bikeL.aspx?lang=zh-Hant-TW&region=%E5%A4%A7%E5%AE%89%E5%8D%80) | Original web content: station search/status legends, borrowing/return counts, exit/address associations; extension announcement displayed 2026-02-11 | Already supports current lookup; extension requires authenticated app, once per rental, 15 minutes. Native app not operated. Metro extractor's count timestamps were older than direct JSON; never use them as simultaneous measurements. Unknown website reuse rights. |
| **T10-S10** Taipei DOIT, [166491 seeing-bike](https://data.gov.tw/dataset/166491), [CSV](https://data.taipei/api/dataset/ba0dafae-043c-4730-b97e-2defd7af766c/resource/55a1ce30-7c99-497c-bdcd-bb88b848c803/download); [174976 seeing-space](https://data.gov.tw/dataset/174976), [CSV](https://data.taipei/api/dataset/65f4c67c-56c8-4b52-abda-5b58946dfecd/resource/d969e222-7fb3-49f1-95f7-3894a8b9f2bb/download) | Original national descriptions specify June 2026, operating 06:00–23:59 availability proportions; full CSV parse: each 1,752 rows, stop_id/name/capacity/XY/category/geometry. Bike categories high/middle=1,710/42; space=1,747/5 | OGDL v1/free. Published category cutoffs are 90% and 60%; boundary equality wording ambiguous. Rows contain neither period nor numeric rate. Taipei seeing-space page still described December 2025: period provenance conflict must accompany use. December-named space file also parsed: 1,696 rows. Not hourly archives or unmet demand. |
| **T10-S11** Taipei DOIT, [166492 aggregated OD](https://data.gov.tw/dataset/166492), [weekday GeoJSON](https://data.taipei/api/dataset/c7dbdb7c-6bbd-495a-bd23-49b22defd83e/resource/a1b54bc5-02f9-4f82-accf-61b4105227d0/download), [city dashboard](https://citydashboard.taipei/dashboard?city=taipei&index=youbike) | National HTML curl inspection specifies June 2026, weekday/weekend resources. Full weekday JSON parsed: 14,820 features; station IDs/names, transaction count, districts, width, LineString. Dashboard indexed components and original repository release notes inspected; live dashboard extraction empty | OGDL v1/free for dataset. No hourly/time/per-trip fields; lines connect stations, not legal cycling routes. Dashboard exact task interaction untested; existence corroborated by S12, not live performance. |
| **T10-S12** MOTC Institute of Transportation, [public-bike dispatch research](https://www.iot.gov.tw/uploads/column_entry_file/file/67c81b8d085777e248fc256e/%E7%B8%A3%E5%B8%82%E5%85%AC%E5%85%B1%E8%87%AA%E8%A1%8C%E8%BB%8A%E7%A7%9F%E8%B3%83%E8%BB%8A%E8%BC%9B%E8%AA%BF%E5%BA%A6%E8%AA%B2%E9%A1%8C%E7%A0%94%E6%9E%90-%E7%A0%94%E7%A9%B6%E5%B0%88%E8%BC%AF-final.pdf) | Original 30-page PDF web text, printed pp.19–23: supply, dispatch staffing, availability monitoring and existing Taipei dashboard | Supports capacity/space/staffing barriers and an existing analytical baseline; references earlier local cases, not new field observation. Redistribution unknown. |
| **T10-S13** The Reporter, [original 2024 investigation](https://www.twreporter.org/a/data-reporter-taipei-youbike-free-ride-for-the-first-30-minutes) | Original full article, interviews and methods; minute collection 2024-02-19–03-22; weekday/rain/inactive exclusions | Original investigation rather than secondary lead. Officials describe internal dashboards and practical fairness/destination-direction objections to group dispatch. Independent collection did not find a clear overall deterioration in first policy month; supply changed concurrently. No causal attribution; copyright, data redistribution unknown. |
| **T10-S14** Community operator, [查 Bike](https://youbike.wolf-yuan.dev/); community [missing-field request](https://data.gov.tw/suggests/136848) | Original pages: history service explicitly warns blocked upstream/stale data, displayed February 2026 timestamps; request seeks timestamped failed-return reports | Establishes an existing history comparator and requested evidence gap, not prevalence. History coverage/license unverified; not a current source. Public request does not establish release of requested records. |
| **T10-S15** YouBike, [Gongguan capacity change](https://www.youbike.com.tw/region/main/news/status/635259df1ff4ab6e32449c86/), [temporary closure](https://www.youbike.com.tw/region/ntpc/news/status/636ca1abada5c3459f269ba6/) | Original 2022-10-21/11-10 notices: named station loses docks for construction, then closes temporarily; directs users to exits 3/4 | Same name can span capacity/service changes. Notices predate examined month and do not establish 2023 capacity or 2023–26 continuity. Redistribution unknown. |
| **T10-S16** Metro Taipei, [2025-11-04 operating response](https://www.metro.taipei/News_Content.aspx?n=30CCEFD2A45592BF&s=37E21D4F53E84437), [GO functions](https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=16CA4EDF934E9211) | Original releases read: gate flow management/control-centre monitoring, staff deployment and headway response; GO arrival/crowding/journey features | Operator assertions of improvement not independently evaluated. Strong redundancy comparator; no evidence that another historical chart improves dispatch. Redistribution unknown. |

#### A. Recurring MRT service-review decision — retained hypothesis

**Problem/user/baseline.** Observed passenger waiting dissatisfaction supplies a bounded issue; the hypothesized user is an operator service-planning reviewer preparing a regular line/time review, not a commuter or bus planner. Exact decision: request a targeted waiting/platform observation and feasibility assessment, retain current service, or escalate a justified headway proposal. Baseline is the annual passenger survey and performance tables, public OD aggregation, and the operator's existing flow-management/control-centre process. Internal analyst effort and cadence are unknown. [T10-S02][T10-S03][T10-S16]

**Success/rejection specified before further OD experiments.** Improvement would be fewer unsupported review proposals, or less effort reaching the same defensible shortlist, versus that baseline. A problem rejection is that existing review already combines these sources adequately; **unresolved**, so no additional chart is justified yet. A data rejection is that OD alone identifies actual waiting/crowding or feasibility; **supported rejection**, because required measurements/constraints are absent. High ridership is not sufficient reason to shorten headways. Statutory compliance and strong existing tools are contrary evidence, not a reason to delete the hypothesis.

**Workflow/dependencies.** Chosen line/time and documented complaint or survey finding → compare like weekday/season OD with service measurements and baseline rationale → authorized reviewer requests/declines observation → dated review note naming evidence, constraints and responsible follow-up. Essential additions are actual headway/platform waiting, denied boarding or crowding, event/weather calendar, service changes, available trains/staff and safe minimum operating constraints. Public hourly OD cannot supply them. Member APIs exist but are unacquired; current data cannot retrospectively repair a 2025 review. [T10-S04]

**Smallest decisive experiment/result.** Compare the same review note produced using existing reports against a provenance-linked evidence packet, with one concerned line/time, one apparently compliant control and one event-disrupted case. Three purposive cases test distinct failure mechanisms, not statistical representativeness. Require exact source/period/count reconciliation and no unsupported action; measure time and reasons without inventing a percentage improvement target. Completed source audit found a real review recommendation and a capable baseline; the action comparison is **infeasible this run** without operator baseline output and service observations. Full 312 MB monthly download would not resolve that uncertainty; only index/schema were checked.

**Readiness/adoption/presentation.** Demonstration=specified as an evidence-review card; task usability untested; decision=insufficient; waiting, accessibility, emissions and safety outcomes unknown. A 100-day pilot needs Metro reviewer sponsorship, operating expertise and an approved comparison; staffing, data approval and cost unknown. Bounded before/action/after example: before, “shorter waits requested” beside system-level compliance; action, reviewer requests a specific station/time observation rather than automatic extra trains; after, a traceable accept/defer note. This is a proposed interaction, not a completed improvement. **Next check:** extract the survey's line-specific waiting results and sampling limits into one review case, checking whether it identifies a defensible observation window without additional assumptions.

#### B. Historical YouBike transfer analysis — C08 retrospective review

**Problem/user/baseline.** Historical station availability failures and expressed borrowing/return concerns are evidenced, but the claim that a reviewer struggles to understand the transfer subset is hypothetical. User: DOT/YouBike review analyst; trigger: a retrospective station-cluster review; authority: request verification/field study, not dispatch trucks. Baseline is a spreadsheet group-by of the six-column CSV plus existing city/agency dashboards. Current monthly OD and availability categories are stronger contextual comparators than pretending no history exists. [T10-S05][T10-S06][T10-S07][T10-S10][T10-S11][T10-S12][T10-S13]

**Success/rejection.** Success means identifying an auditable historical question that changes or justifies the next review action beyond baseline. Problem rejection: the old slice supplies no additional action-relevant question; **unresolved**, defer operational promotion. Data rejection: historical subset plus live snapshot reconstructs inventory, total demand or the preceding MRT leg; **supported rejection**. No invented shortage threshold is used. [T10-S07][T10-S08]

**Completed decisive experiment.** Census the already accessible December file, selected to resolve the prior incomplete-month audit, then inspect nine Gongguan/Taipower exit names including the difficult `_1` suffix. This deliberately bounded cluster tests exit distinctions; it cannot estimate all-city identity accuracy. Python standard-library CSV/datetime/hash parsing received 62,285,127 bytes, SHA256 `d70247cd83d6539714cd5d8dd03e607f2143c5ce5c65391b80542a1bcc3b6cf8`: 518,189 rows and all 31 borrowing dates; no parsed start/end outside December, end-before-start or borrow-date disagreement. All borrow/return minute and second fields were zero. Duration strings passed the inspected HH:MM:SS format check, with no zero values and four values of at least 24 hours; these are review flags, not proven errors. All 518,189 duration strings differed from rounded timestamp subtraction. December 4 had 4,813 records versus 17,569 on December 5; the cause and completeness are unresolved, so date presence is not a completeness guarantee. There were 858 excess identical rows under all-six-field equality: no trip ID means these cannot safely be removed as duplicate journeys. Exact duration cannot be recovered by subtracting rounded timestamps. [T10-S07]

Across 1,834 distinct endpoint names, prefix-only exact matching found 1,291 in the current inventory and left 543 unmatched; matched endpoint occurrences were 1,013,224/1,036,378. These are name correspondences, not validated historical station identities. Unmatched examples include `?公公園` and renamed/institutional-looking names; encoding corruption, cross-city returns, closures and renames are rival explanations. No fuzzy substitution was applied. Nine selected exit names each had one current match. Taipower exit 2 and exit 2 `_1` map to distinct IDs `500101104` and `500101207`, with different addresses; preserve that suffix. Original Gongguan notices prove earlier capacity/closure changes, while 2023 location/capacity continuity remains **unresolved**. [T10-S08][T10-S09][T10-S15]

**Workflow/claims.** Historical month and explicit name set → departure/return profiles with unmatched/precision warnings → reviewer requests historical identity or inventory verification → reproducible review question and inclusion/exclusion table. In the inspected month Gongguan exit 2 has 15,615 subset departures and 1,227 subset returns; their difference is **not** net inventory loss because nontransfer trips, trucks and stock are missing. Current capacity cannot be projected backward. Permitted result is historical subset description; present shortage/optimization is infeasible. [T10-S07]

**Readiness/adoption/presentation.** Demonstration=specified; parsing task completed, user task untested; decision=insufficient; civic benefit unknown. DOT/operator historical identity ledger, inventory/dispatch records, subset selection semantics and transport expertise are needed for a 100-day review; costs/access unknown. Before: a historical departure-heavy station appears to need more bikes. Action: distinguish transfer-only records and obtain matching-period inventory. After: “needs corroboration,” not a truck order. Capacity, fleet supply, weather, pricing changes and fairness can dominate information. **Next check:** search original operator notices for Gongguan exit 2's reopening, moves and capacity during December 2023; retain the identity gap if those notices cannot establish it.

#### C. Current commuter station choice — separate C08 hypothesis

**Problem/user/baseline.** A commuter arriving at a chosen station risks a failed pickup/return, but this run observed no individual failed journey. The rider has authority to choose another station or walk; no authority to rebalance bicycles. Existing YouBike map/app, Metro station pages and an accessible government table already expose availability; the operator also offers a full-station extension. A generic new lookup is highly redundant. [T10-S06][T10-S09]

**Success/rejection.** Compare the same origin/destination task against those tools: locate a currently reported usable pickup and return, recognize source age, and choose a feasible fallback with less effort and no worse mistakes. Problem rejection that lookup capability is absent is **refuted**; incremental accessibility/effort benefit remains **unresolved**. Data rejection of “available on arrival” or chronic-reliability claims from one snapshot is **supported**. Stale/inactive data must lead to an explicit unknown, never a recommended station.

**Completed feasibility check/workflow.** Full publisher snapshot and station/address comparisons establish that current lookup inputs exist; they do not establish reliable routes or bikes' physical usability. Input trip ends and retrieval time → compare active stations, source time, reported bikes/slots and user constraints → rider selects station/fallback → record chosen station IDs and refresh before departure. Nine-cluster count inspection includes low availability (Taipower exit 2: two bikes) and suffix ambiguity. No walking distance or legal route was invented; source and collection times must stay distinct. [T10-S08]

**Smallest decisive experiment/readiness.** Paired tasks for normal, zero-bike, full-return, inactive/stale and similarly named exits cover different consequential errors; purposive cases require correct station/status/time handling, not a fabricated “under 30 seconds” target. Compare time, errors and understood uncertainty against the official accessible table and YouBike map. This run completed data/input inspection only; actual rider task comparison and arrival verification are **infeasible without authorized participant observation**, so decision=insufficient. Demonstration=specified as a timestamped comparison; usability and civic outcomes unknown. Native-app behavior was not tested. A community history service's stale-data warning is contrary evidence against trusting third-party freshness. [T10-S14]

**Adoption/presentation/next check.** A 100-day path needs an identified unmet user need, accessibility testing, lawful walking/cycling information, maintained feed monitoring and operator-rule expertise; maintenance cost unknown. Before: rider considers Taipower exit 2. Action: at the recorded 19:05:52 snapshot compare its two reported bikes with the distinct `_1` station's 30, inspecting addresses. After: a provisional choice with refresh/fallback, not guaranteed availability or a route recommendation. Counts are a dated real observation; the rider/action is hypothetical. **Next check:** perform the same no-login exit-2 versus `_1` lookup on the official accessible transport page and operator map, recording whether both names, timestamps and fallback options can already be distinguished; stop if the proposed information gap disappears.

#### Integration qualification

Evidence depth is unequal: the transfer file received a complete census, MRT only an index/schema audit, and commuter products a public-content comparison rather than native-app or practitioner testing. Replace only affected C08/137993/169174 readiness, dependency-index and next-action statements: preserve earlier dated counts; add hourly timestamp precision, identical-row ambiguity, unmatched-name volume and the newly audited category/OD datasets. Qualify “no availability history” as **no complete time-resolved inventory/unmet-demand archive established**. The new evidence does not select a topic or validate practitioner value. The complete-file counts, identity normalization, exact source links and stated methods above support reproduction. Temporary aggregate/helpers are retired after durable integration; raw trip rows were processed in memory only.

[T10-S01]: https://puma.taipei/hackathon#issue-7
[T10-S02]: https://www-ws.gov.taipei/001/Upload/405/relfile/18288/132392/de6c2851-5c91-4e96-a27a-22a2b6658441.pdf
[T10-S03]: https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=fa621cd2-2d90-4ed0-9c2a-397a41092a30
[T10-S04]: https://data.taipei/dataset/detail?id=63f31c7e-7fc3-418b-bd82-b95158755b4d
[T10-S05]: https://auditreport.audit.gov.tw/ServerFile/Get/63889289612421155881e71de3dcf04416b330afed176c7dcc
[T10-S06]: https://www-ws.gov.taipei/001/Upload/390/relfile/52906/9012754/e0185bbd-7891-4a31-a3db-82733ac1dab4.pdf
[T10-S07]: https://data.gov.tw/dataset/169174
[T10-S08]: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
[T10-S09]: https://youbike.com.tw/region/taipei/stations/
[T10-S10]: https://data.gov.tw/dataset/166491
[T10-S11]: https://data.gov.tw/dataset/166492
[T10-S12]: https://www.iot.gov.tw/uploads/column_entry_file/file/67c81b8d085777e248fc256e/%E7%B8%A3%E5%B8%82%E5%85%AC%E5%85%B1%E8%87%AA%E8%A1%8C%E8%BB%8A%E7%A7%9F%E8%B3%83%E8%BB%8A%E8%BC%9B%E8%AA%BF%E5%BA%A6%E8%AA%B2%E9%A1%8C%E7%A0%94%E6%9E%90-%E7%A0%94%E7%A9%B6%E5%B0%88%E8%BC%AF-final.pdf
[T10-S13]: https://www.twreporter.org/a/data-reporter-taipei-youbike-free-ride-for-the-first-30-minutes
[T10-S14]: https://youbike.wolf-yuan.dev/
[T10-S15]: https://www.youbike.com.tw/region/main/news/status/635259df1ff4ab6e32449c86/
[T10-S16]: https://www.metro.taipei/News_Content.aspx?n=30CCEFD2A45592BF&s=37E21D4F53E84437

### Cross-topic decision comparison

**Inference — after all ten investigations:** the same minimum problem record is complete for
**25 distinct workflows**, with explicit hypotheses where public evidence cannot validate a user
need. Evidence depth is unequal: full-file technical checks are stronger for entrances, scenarios,
transfer rentals and the childcare roster; lived/practitioner evidence is mostly historical,
self-selected, operator-reported or geographically limited. No interviews or observed practitioner
comparisons occurred. Unknown value is not low merit. Free topic contains the independent problems;
it is not an extra candidate competing with its children.

| Track | Possible actionable contribution | Problem/evidence depth and limits | Baseline/adoption constraint | Bounded next experiment |
| --- | --- | --- | --- | --- |
| T01 Trees/C03 | Planting field review; officer exceptions; caregiver confirmation | Heat/access pain has scoped original evidence; shared entrance errors and missing continuous trip/plantability limit claims | Existing tree/Wheelroute/park tools; utilities, survey and repair capacity may bind | Check named-street history and two anomalous entrance plans before any ranking |
| T02 Bins/C07 | Verify/repair/siting review; overflow response; market boundary referral | Incidents/patrol burden documented; same lookup data, stale venue and no public synchronized load/crew series | Existing lookup and sensor trial; current SOP, crews and contracts unresolved | Inspect replacement procedure and sensor-trial results; verify interim-market boundary |
| T03 Rats | Correct referral; observed-condition owner and reinspection | Self-reports and source-control precedents; no local linked public inspection/action/outcome chain | 1999, Rat Radar and professional diagnosis already exist; access/repair responsibility can dominate | Read current joint-inspection/recheck artifact before any predictor discovery |
| T04 Neihu | Employer feasible trial; city expansion evaluation | Local burden and existing campaigns; fresh feeds/history are geographically incomplete and treatment attribution unavailable | Existing TUIC/DOT/employer coordination; coverage, care obligations and through traffic rival timing | Verify named-city-detector history/rights; do not equate freeway coverage to city corridors |
| T05 Buses | Service evidence request; changed actual-duty review | Route statistics and one investigated duty failure; no stop/time demand or authorized present duty/facility record | Approval/OMS/reservation systems already exist; staffing and facilities may dominate | Trace one approved reduction rationale and current duty-monitoring response |
| T06 Buildings | Assessment preparation; professional feasibility; opt-in meeting | Professional process and historical affordability barriers; no building-specific safety or outreach-effect evidence | Existing CMO/URO/NCREE routes; consent, liquidity, professionals and work disruption | Compare current meeting intake and station service fields before proposing another referral tool |
| T07 C01 | One review question for an already shortlisted site | Local geometry/time disputes and capable baseline; event/victim/exposure semantics incomplete | National hotspot tool and official packets exist; engineering agreement/capacity may dominate | Inspect the existing Gongguan review record for the proposed packet’s three fields |
| T08 C02/C06 | Meal audit and resident confirmation; parent reconciliation and planning investigation | Original meal barriers, current schedules/roster and specific version conflicts; no acceptance/vacancy/deduplicated demand | Existing maps/admissions/professionals; premises, staff, cost and hours compete with information | Find completed district childcare demand analysis; preserve meal inventory arithmetic and separate eligibility |
| T09 C04/C05 | Publication discrepancy confirmation; facility preparedness follow-up | Local audits and current conflicts; three modeled files audited, invalid geometry and missing entrance/floor evidence | Existing inventories/EOC GIS/coordination; authoritative meaning and operating resources unresolved | Compare two conflicting school records against latest district flood maps |
| T10 MRT/C08 | Metro observation request; historical transfer question; current provisional station choice | Survey/audit pain with contrary compliance; coarse old subset, ambiguous identities and capable current tools | Existing control centre, dashboards and maps; fleet/staffing/space may dominate | Extract line-specific waiting evidence; verify historical identity and existing exit-name lookup |

**Research recommendation, not topic selection:** the next public-source investment can be C04's
two-school publication check: it starts from a reproduced current discrepancy, a documented local
audit concern and a named district source, and can reject a supposed information gap without
implementation or contact. It cannot establish practitioner usefulness or shelter safety. C06's
completed demand-analysis report is another consequential public check because richer supply data
now exists and the unresolved question is demand/acceptable service. If the owner seeks an official
six-theme route, T02's existing sensor-trial result or T06's existing service-intake comparison should
precede another map. These are conditional experiments with different constraints, not a ranked
winner or an automatic build decision.

An implemented demo remains a separate owner request. Operational adoption requires a named
custodian, existing-process comparison, lawful evidence access, expertise and available capacity;
100-day staff/procurement/maintenance costs are unknown. Source parsing completed research tasks;
it did not establish user task success, baseline decision gain or target civic outcomes.

## Expanded solution research beyond organizer starters

**Owner decision — 2026-10-13:** use Twinkle to discover additional data and investigate civic
solution themes through independent agents. Four tracks owned transport, flood preparedness,
street environment and everyday care services. Root verified selected original resources and
integrated their findings into this existing research owner. No application was built, no topic
selected, and no external registration/contact/payment occurred.

### Synthesis and recommended order

For current decisions use [the ten-track comparison](#cross-topic-decision-comparison). The table below is the retained earlier data-audit snapshot, including its then-incomplete checks; it is not the current readiness or next-action owner.

**Inference — retained historical data-readiness comparison:** the displayed C01–C08 order records
the earlier source audit, not the current investigation order or relative problem value. The
problem-first queue below supersedes its sequencing. All official directions and expanded
hypotheses require the same minimum problem record before recommendations; source-specific
Evidence, Hypotheses and Open questions remain in the four tracks.

| Candidate ID (not priority) | Additional real inputs beyond organizer starters | Hypothesized decision and bounded workflow | Unresolved gate / claim boundary |
| --- | --- | --- | --- |
| [**C01 Collision-site review**](#c01-collision-site-review) | `130110`: 22,762 published 2025 fatal/injury collision rows, 12 months; all first-party sequence 1, two missing coordinate rows | Traffic engineer filters a district/time band, compares observed collision concentrations and road/signal attributes, and prepares an auditable field-review list | Decode post-2023 codebook, confirm event/party/severity semantics and aggregate units; no exposure denominator, safest-route, all-pedestrian-victim or causal intervention claim |
| [**C02 Senior-meal inventory**](#c02-senior-meal-service-inventory) | `135495`: 440 meal-list rows + previously audited 2026-09 age-population data; root successfully joined all 12 districts | Social-welfare planner compares listed sites per 1,000 registered older residents and selects areas for site/activity/capacity investigation | Site list lacks row observation dates, meals/seats/hours/attendance; the ratio is an inventory proxy, not demonstrated service shortage or actual demand |
| [**C03 Accessible park entries**](#c03-accessible-park-entry-comparison) | `152266`: 745 park entrance rows with width/slope/TW97 XY; `128414`: 193 MRT accessible entrance rows | Park-access officer/caregiver compares published entrances and source conditions; flags entries or approaches requiring survey | Root found two coordinate-magnitude outliers; validate CRS and points, no common stable ID or complete walking topology. An inspection comparison, not wheelchair-safe navigation |
| [**C04 Shelter preparedness**](#c04-village-shelter-preparedness) | `tp-00002066`/`134683`: 419 SA-ID records in a 2026 ODS, plus service-village/hazard/accessibility/capacity fields and age population | District preparedness coordinator audits listed flood eligibility, backup/accessibility and service-village coverage, producing questions before exercises | Resolve differing agency inventories and flag/capacity semantics, district-qualified village joins, shared capacities and latest authority; no live opening/occupancy or evacuation instruction |
| [**C05 Rainfall-scenario review**](#c05-rainfall-scenario-facility-review) | `121550`/`tp-00000862`: official 2023 modeled 78.8/100/130 mm/h accumulation scenarios; one KML parsed with 1,945 polygons | Facility planner checks verified points against scenario depth bands for a preparedness review | Geocode/verify entrances, audit remaining scenarios; explicitly **government-modeled input**, not real flood observation or prediction. Intersection does not prove a building/shelter unsafe |
| [**C06 Childcare evidence**](#c06-childcare-evidence-shortlist) | `121337`:29 public-operated centers; `121278`:223 private; `156685`:292 assessment rows with uneven 2021–2025 coverage | Parent/planner forms a local evidence-linked shortlist and sees which assessment year applies | Verify name/address joins, active status, assessment cycles and meaning of 收托人數; no vacancies, capacity shortage or generic best-center score |
| [**C07 Market-bin audit**](#c07-market-bin-service-audit) | `121593`:47 geocoded markets + existing bin inventory | Sanitation supervisor prepares an inspection list of approaches, listed bins and unresolved public/private responsibility | Venue point is not a pedestrian entrance/catchment; no footfall, overflow or operational cost data. Audit candidate, not placement/collection optimization |
| [**C08 YouBike patterns**](#c08-youbike-transfer-patterns-and-current-availability) | `169174`:2023-only transfer-rental subset; December full response had 518,189 rows; `137993`:current publisher 1,819-station snapshot | Operations analyst explores historical station/time patterns; commuter uses a separate timestamped current station lookup | Full-month validation and historical/current station identity needed; no unmet demand, truck schedule or availability history. Old transfer subset cannot justify present redispatch/shortage predictions |

**Inference — earlier source-audit scope:** the first three had bounded real-data foundations in
that audit; this does not privilege them in the current problem-first queue. Flood preparedness
has administrative/scenario inputs distinct from real-time safety advice.
Original shade optimization, rodent prediction, individual-building safety ranking and bus-demand
network redesign remain unsupported by the missing outcomes/constraints; new catalog hits do
not cure those gaps. User value still requires validation with a named practitioner, and any
external contact needs owner authorization.

### Problem fit and separate readiness of the expanded candidates

**Canonical current judgment — 2026-10-13, after the deep run:** this stable section now owns
readiness for official themes and expanded candidates, separated into all 25 workflows below.
`specified` is a written bounded demo proposal, including disclosed hypothetical inputs where
noted; no application or participant test exists. Every row has **decision=insufficient** for its
operational action and **target civic outcome=unknown**. Completed source/schema comparisons and
historical descriptive calculations are supported only within their stated scope. They do not
satisfy the baseline decision-gain requirement.

| Distinct workflow | Demonstration | Decisive boundary / research disposition |
| --- | --- | --- |
| T01 planting/shade review | specified | No verified eligibility/exposure; field-sheet gain untested |
| T01 / C03 officer inspection | specified | Shared source errors; independent location/condition and officer comparison missing |
| T01 / C03 caregiver confirmation | specified | Checklist only; reliable journey/routing deferred |
| T02 placement/access | specified | Verification checklist only; current asset/SOP/approach unknown |
| T02 collection/overflow | specified | Labeled simulated load/crew task only; actual telemetry/crew comparison absent |
| T02 / C07 market responsibility | specified | Current entrances/boundaries/contracts unresolved; no service-gap ranking |
| T03 resident referral | specified | Existing intake; incremental resident benefit and reuse rights untested |
| T03 inspection/recheck | specified | Synthetic accountability packet only; linked actual cases absent |
| T04 employer feasibility | specified | Evidence/constraint packet only; employee feasibility/history missing |
| T04 city evaluation | specified | No treatment-isolating controls/participation or full corridor history |
| T05 service proposal review | specified | Annual route context cannot supply stop/time demand or feasible redesign |
| T05 actual-duty/rest review | specified | Historical discrepancy case; present authorized duty/usable facilities missing |
| T06 assessment preparation | specified | Fictional checklist; existing pack covers tested branches |
| T06 retrofit/renewal feasibility | specified | Professional case, financing/consent and quote evidence absent |
| T06 opt-in outreach | specified | Existing services; intake gain and available professional capacity unknown |
| T07 / C01 site-review packet | specified | Existing screening/packets; incremental value and semantic joins unresolved |
| T08 / C02 planning inventory | specified | Correspondence checked; activity/capacity/queue benefit unvalidated |
| T08 / C02 resident meal access | specified | Call checklist only; current acceptance/price/access unknown |
| T08 / C06 parent choice | specified | Reconciliation only; no offered vacancy or observed parent advantage |
| T08 / C06 municipal planning | specified | Dated descriptive supply available; active deduplicated demand absent |
| T09 / C04 inventory reconciliation | specified | Current conflicts reproduced; authoritative meaning and practitioner gain unknown |
| T09 / C05 real-facility review | blocked | Verified entrance/operating floor absent; invalid polygons require technical handling |
| T10 MRT service review | specified | Retained hypothesis; platform/service constraints and reviewer comparison absent |
| T10 / C08 historical transfer review | specified | Full census; hour-rounded times, subset limits and historical identity unresolved |
| T10 / C08 current commuter choice | specified | Timestamped provisional lookup; official baseline gain/arrival reliability untested |

Problem-level rejections distinguish redundancy/capacity constraints from absent pain evidence;
data-level rejections distinguish missing operational evidence from complete source-level tests.
Each detailed record owns its completed comparison, difficult cases, supported/refuted/unresolved
exit, operator/authority/cost unknowns and one next check. The queue below owns the topic-level
next action. Neither this table nor the historical C01–C08 order selects a topic.

### Independent verification and a real cross-dataset calculation

**Evidence — root readback, 2026-10-13:** full publisher reads reproduced park745/MRT193,
collision22,762 (year114, first-party1, two missing XY), senior-meal440, latest shelter419 unique
SA IDs/88,568-byte ODS and scenario1,945 polygons/893,437-byte KML. Counts are records, not
asserted unique events, operating facilities or validated coverage. No raw individual accident,
journey, personal/contact or account records are retained in Git.

The park CSV's numeric fields all parsed, width0.9–19.6m and slope0–8%, with134 zero-slope values.
However, two entries have suspicious projected-coordinate magnitude: ID75 has Y277120.65;
ID113 has X3066305.29. This flag uses X>1,000,000 or Y<1,000,000 as a coarse magnitude test,
not a validated Taipei boundary or a diagnosis of the cause. No digit insertion, swap or automatic
repair was performed. The other 743 records are not thereby proven geographically valid.

**Evidence — calculated comparison:** root read the latest population file and meal CSV directly,
selected ROC115/month9/sex計 and exactly the twelve district-name aggregate rows, summed ages65–99
plus100+ (and75–99 plus100+ for a second age context), and joined meal district names. All12
unique district codes matched and site counts reconciled to440. This avoids adding village,
district, city and male/female totals together. The ratio is `listed sites / registered65+ *1000`.
The meal list has no row observation timestamp and an older indexed file date, so this is a
**retrieved inventory compared with September2026 demographics**, not a verified simultaneous
supply-demand measurement.

| District | Listed sites | Registered age65+ (2026-09) | Sites per1,000 age65+ |
| --- | ---: | ---: | ---: |
| Neihu |30|56,612|0.530|
| Shilin |39|66,670|0.585|
| Zhongshan |36|54,560|0.660|
| Datong |20|28,499|0.702|
| Songshan |34|47,588|0.714|
| Wenshan |43|57,746|0.745|
| Zhongzheng |26|34,690|0.749|
| Daan |57|74,246|0.768|
| Wanhua |36|45,365|0.794|
| Xinyi |46|53,434|0.861|
| Beitou |50|56,447|0.886|
| Nangang |23|25,380|0.906|

Sources: [meal inventory](https://data.gov.tw/dataset/135495),
[meal CSV](https://data.taipei/api/dataset/fe55795c-a220-4b88-bde1-5b994321f8af/resource/86d839db-85c7-48b0-991b-dc86922eb093/download),
[population publisher](https://data.taipei/dataset/detail?id=a6394e3f-3514-4542-87bd-de4310a40db3),
[population CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=c8f5b53d-ef3d-4321-ae8e-58cd2a5ee73c).

**Inference:** Neihu's lower ratio makes it a possible *inventory/activity-validation* target,
not proof of insufficient meals: seats, eligibility, cross-district users, operating days and
attendance are unknown. This calculation demonstrates an actual tractable join and an explainable
comparison, not a validated causal/service-adequacy conclusion.

### Reproducing the meal-list comparison

**Evidence / method record:** this preserves the actual completed calculation, not new measurements
or an implementation requirement. Exact [population and meal download links](#independent-verification-and-a-real-cross-dataset-calculation)
and the twelve result rows are owned by the preceding section.

1. Read the population CSV with a quoted-field-aware parser; decode the publisher's Big5/CP950
   encoding. Required headers are `年份`, `月份`, `區域代碼`, `區域別`, `性別`, each
   `65歲數量` through `99歲數量`, and `100歲以上`. For age75+, use75–99 plus100+.
   Strip numeric whitespace/separators and reject unparseable values rather than replacing them with0.
2. Select `年份=115`, `月份=9`, `性別=計`. Match `區域別` to the twelve meal-list district names;
   this selects district aggregates only. Do not sum city/district/village records together, and do
   not add male/female rows to the already-total sex row. Check twelve distinct `區域代碼` values.
3. Read the UTF-8 meal CSV, using `行政區` and `行政區代碼` for identity checks. Count listed rows
   by district. The completed calculation joined **exact district names** and checked the resulting
   twelve population codes; it did not establish every meal row's code/physical-site uniqueness.
4. Compute `age65plus = sum(age65…age99) + age100plus`; require a positive denominator.
   Compute `listed_rows_per_1000 = district_meal_rows * 1000 / age65plus`.
   Keep integer numerators/denominators; round only the displayed final ratio to three decimals.
5. Reconcile twelve matched districts and440 total meal rows, with no silently dropped district.
   The published comparison's Neihu value is30/56,612×1000≈0.530; Nangang is23/25,380×1000≈0.906.
   These are reproducibility examples, not service-quality or hardship rankings.
6. Record the exact population month, source retrieval date, resource URL and meal-list freshness
   uncertainty with the output. If a fresh retrieval changes a count/schema, create a newly labeled
   observation in this same section; do not silently overwrite the2026-10-13 result.

**Rejection conditions:** missing district/month/sex fields, duplicate population district rows,
zero/unparseable age denominator or unmatched district names invalidate the calculation. A failed
facility deduplication/activity check does not invalidate the raw-row arithmetic, but blocks the
stronger interpretation as distinct operating facilities. Missing capacity, hours, attendance,
eligibility and cross-district use blocks a service-shortage conclusion even if arithmetic passes.

**Next unresolved check:** compare the pilot meal rows with current official operating/service
information and separate duplicate or co-located entries. No household location or user-specific
health data is required to reproduce this district-level calculation.

### What Twinkle contributed, and what it did not establish

**Evidence:** Twinkle successfully discovered datasets outside the organizer list and returned
metadata and samples. Root inspected `tw_query_dataset` and successfully read two public park
entrance rows (ID1/2, TW97 XY, width/slope) through `execute_tool`, after older `tw_query_rows`
column-based calls were rejected as `QUERY_NOT_ALLOWED`. The working structured schema uses
`select`, `filters`, `aggregate`, `group_by`, `order_by`, `limit`. This is a bounded correction
based on a diagnosed runtime-policy mismatch, not a blind repeated call. The current MCP skill
packs remain withdrawn; no old skill was installed.

A shared authenticated connection cached identical successful requests. Four tracks' successful
calls reported36credits; root's structured two-row read reported1, for **37 reported successful-call
credits**. Four row-policy error responses lacked a charge report; their billing is unverified,
so37 is not asserted to be the account's exact balance decrement. No top-up, purchase or model
inference tool was used. Root's final read reported zero USD/LLM cost. Temporary verification
threads started no model turns; credentials stayed in Codex's local credential storage.

Observed caveats: normalization date is not observation date; metadata join hints may name absent
columns; a live-named YouBike mirror was hours behind its publisher; the two shelter inventories
have different agencies/versions/rows and37 flood-flag differences among386 name-matched current
rows. **That comparison does not prove37 real-world eligibility changes or that the newer file
supersedes every responsibility of the older agency.** Resolve authority and scope before choosing
one. Existing tree/park/market datasets are complementary, but no extra catalog creates missing
canopy, pedestrian exposure, rodent outcomes, bus passenger demand or real-time shelter occupancy.

The full track evidence follows. All proposed usability/success thresholds are acceptance ideas,
not completed user tests. Original-publisher licenses and privacy restrictions remain controlling.

**Evidence — documentation verification:** all42 newly introduced unique Markdown HTTP links
returned200 on bounded curl HEAD checks; actual resource contents were checked separately as
described in each track. Owned documents passed credential/callback-pattern inspection and
`git diff --check`. Documentation-only research requires no application test suite. Temporary
MCP clients, schemas and research drafts are cleaned after their findings are committed here.


### Dataset-to-candidate index

This is a navigation index, not a second source audit. The linked track owns exact publisher and
resource URLs, retrieval method, period, fields, license and limitations. Candidate IDs C01–C08
refer to the eight expanded hypotheses, not organizer issue numbers. National and `tp-` aliases
are the same dependency when they resolve to the same publisher resource.

| Dataset identity | Candidate use | Observed evidence state / unresolved dependency | Detailed owner |
| --- | --- | --- | --- |
| `130110` / `tp-00001025` collision records | C01 essential | T07 full 2025 aggregate audit; first-party extract, no event ID; current form does not resolve export 2–30-day-death semantics | [T07](#t07-c01-collision-site-review) |
| `137993` YouBike current inventory | C08 current lookup | T10 later 1,819-station snapshot; active/inactive and campus category separated; no arrival guarantee; capacity differs from bike+slot sums | [T10](#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `169174` transfer rentals | C08 historical | Full December census completed; all 31 borrow dates, hour-rounded times, 858 identical-row excess and 543 unmatched current names; completeness/identity still unresolved | [T10](#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `135775` monthly YouBike total | C08 context only | MCP sample and publisher schema; no station dimension | [Transport audit](#exact-new-dependencies-and-observed-access) |
| `152266` park entrances | C03 officer/caregiver | T01 745-ID match with Wheelroute, identical width/slope and shared two gross location anomalies; source agreement is not independent validation | [T01](#t01-trees-shade-and-accessible-park-use) |
| `128414` / `tp-00001516` MRT accessible entrances | C03 essential | Full CSV parsed; network extends beyond Taipei, no downtime or shared entrance ID | [Street-environment audit](#additional-datasets-and-actual-reads) |
| `126553` garbage/compost collection totals | C07 context only | Full CSV parsed; no district/team dimension despite title | [Street-environment audit](#additional-datasets-and-actual-reads) |
| National catalog `121593` markets | C07 essential | Direct publisher discovery/full CSV; not independently discovered through MCP, no all-food-business coverage | [Street-environment audit](#additional-datasets-and-actual-reads) |
| Wheelroute `2b58f15a…` | C03 baseline/potential | 940 API records; 745 park measurements match, remaining 195 sentinel-like; separate 193-row MRT inventory not reconciled; units/topology/current conditions unresolved | [T01](#t01-trees-shade-and-accessible-park-use) |
| `135495` meal list; current 115.08 PDF/operator schedules | C02 planning/access | 440-row descriptive ratio preserved; ten source correspondences checked; age60 eligibility differs from age65 denominator; schedules exist, activity/capacity/acceptance unknown | [T08](#t08-c02-senior-meals-and-c06-childcare) |
| `121337` public childcare | C06 | Old count source differs from dated September roster; 29 public centers not the full supply system; no offered vacancy | [T08](#t08-c02-senior-meals-and-c06-childcare) |
| `121278` private childcare | C06 | Earlier 223 rows retained; dated full registry distinguishes service categories/periods; legal identity joins require review | [T08](#t08-c02-senior-meals-and-c06-childcare) |
| `156685` assessment CSV; 115/2026 PDF | C06 parent evidence | 292-row CSV ends2025; newer PDF and map disagree in inspected case; law/footer cycle conflict retained; missing assessment is not failure | [T08](#t08-c02-senior-meals-and-c06-childcare) |
| `135696` childcare enrollment | C06 context only | Full semiannual citywide series; no local/center vacancy inference | [Care-service audit](#evidence--retrieved-2026-10-13) |
| `121550` / `tp-00000862` rainfall scenarios | C05 | All three KMLs fully parsed; 1,945/7,330/29,738 polygons, 9/57/287 invalid under stated GEOS; modeled inputs, no validated facility join | [T09](#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `135484` / `tp-00003479` welfare shelters | C04 | Older399-row source retained; T09 exact district+name joins differ from earlier recipe; scope/authority unresolved | [T09](#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `134683` / `tp-00002066` education shelters | C04/C05 | 419 IDs/418 names; website ODS and April2026 plan compared; two school conflicts, shared capacities and authoritative semantics unresolved | [T09](#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `tp-00003001` flood facilities; `tp-00003003` flood works | C04/C05 context leads | Catalogs inspected only; resource rows not read, annual aggregates cannot prove local protection | [Flood audit](#evidence-additional-dataset-inventory) |
| Existing village/district age population (`a6394e3f…`) | C02 essential; C04/C06 potential | Full source parsed earlier; C02 twelve-district join checked, village joins unvalidated | [Organizer population audit](#building-resilience-and-open-topic-weather-six-additional-dataset-pages) |
| Existing bin inventory `121355` | C07/T02 | T02 lookup equals681-row CSV; nonnumeric longitude, aggregate/duplicate sites; market point may be stale | [T02](#t02-public-bins-and-c07-market-bin-responsibility-audit) |
| Existing trees, pits and sidewalk geometry | C03 optional context | Full inventory/geometry checks earlier; stale surveys/duplicates, no measured shade or connected path | [Organizer tree audit](#trees-and-shade-four-dataset-pages) |
| T04 city v2 VD/static; annual survey128230; NFB archive | Official Neihu | Current public readings and historical local/upstream samples verified; exact city-v2/station-workbook rights and complete corridor history unresolved; NFB >40s request spacing | [T04](#t04-official-neihu-traffic-timing-requires-an-executable-employer-decision) |
| T05 2025 route statistics / OMS-duty evidence | Official buses | Route-level context and one TTSB actual-duty case; stop/time demand, current private duty and rest facilities absent | [T05](#t05-official-buses-service-decisions-and-executable-driver-rest) |
| T06 building7889e8a0; soilec40e067; professional packs | Official buildings | Full city-aggregate parse and official soil interpretation; no individual safety/priority inference; current professional routes already exist | [T06](#t06-official-building-resilience) |
| T03 food9431f450 / pipeaf1e6e42 / complaintcb423c17 / current ODT | Official rats | Full fields rechecked; no spatial outcome/repair chain. No-committee consent route verified; third-party reports require rights/privacy review | [T03](#t03-official-rats-intake-versus-inspectable-source-control) |
| T08 dated September2026 full registry;147154; baby-map layer6 | C06 | 314 serials, approved/actual/hours/fees/type; older215-row CSV has no row dates. Map/API rights unknown; actual enrollment is not offered vacancy | [T08](#t08-c02-senior-meals-and-c06-childcare) |
|166491 /174976 availability categories;166492 aggregated OD | C08 | Full June2026 catalog-labeled resources; category boundary/period conflicts, no numeric hourly rates or unmet demand; LineString not cycling route | [T10](#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| MRT63f31c7e / 2025 survey/performance | Retained MRT | Index/schema, waiting recommendation and contrary compliance; no full OD-month or platform/service-constraint validation | [T10](#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |

Search-only leads, including bicycle lanes, bridge access and bicycle parking, remain in the
transport track. They must not silently become essential inputs. None of these observations
establishes all-city completeness or an operationally reliable live service.


### Additional transport evidence: collision review and YouBike transfers

**Later observation:** T07 re-read collision semantics and T10 completed the December transfer census; their deep records own current qualifications. The source tables below preserve earlier audit scope. Complete date presence does not establish completeness, and current exact-name matches do not establish historical station continuity.

**Evidence — retrieved 2026-10-13.** This independent track used Twinkle authenticated `tw_search_datasets` three times (bicycles, YouBike, fatal/injury collisions) and `tw_get_dataset` twice, each with bounded samples: 10 credits total, no model/inference tool, no payment. All five returned `cost_usd=0.0` and cache hits. Publisher checks used official catalog HTML, live JSON and CSV GETs; Python standard-library parsers produced aggregates without retaining personal rows. Root owns integration; this note changes no repository files.

#### Exact new dependencies and observed access

| Twinkle ID / official source | Publisher, license and coverage | Actual observations / limitations |
| --- | --- | --- |
| `130110` (duplicate local-catalog alias `tp-00001025`), [Taipei fatal/injury collision data](https://data.gov.tw/dataset/130110) | Taipei Police Department Traffic Division; OGDL v1.0, free; annual resources ROC 101–114 (2012–2025) indexed; metadata 2026-06-11. [2025 CSV](https://data.taipei/api/dataset/2f238b4f-1b27-4085-93e9-d684ef0e2735/resource/83d6d29c-6801-41a2-95c6-47d551646db3/download). | Actual complete GET: 4,082,763 bytes, 22,762 rows, all `發生年度=114`, all `當事人序號=1`, all 12 months. Relevant fields: date/hour/minute, district, location, deaths, 2–30-day deaths, injuries, weather/light, speed limit, road type, intersection/signal codes, collision type, first-party vehicle code and coordinates. Only 2 rows lack each XY; observed X 121.4611803–121.6520178, Y 24.9659305–25.1832948, consistent with lon/lat but authoritative CRS still to verify. A row appears to represent first party, not every casualty; do not infer injured pedestrian counts from first-party vehicle type. 157 blank vehicle codes. Catalog links different codebooks before/after 2023-07-01. Do not expose personal demographic/occupation/impairment fields or exact individual event details in a demo. No unique accident ID observed; identical time/place can collide, and reported injury count semantics need codebook confirmation. |
| `137993`, [Taipei YouBike 2.0 real-time information](https://data.gov.tw/dataset/137993) | Taipei Transportation Department; OGDL v1.0, free; advertised every minute. [Actual JSON](https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json). | Twinkle sample and schema showed 1,819 normalized rows; first sample `srcUpdateTime=2026-10-13 01:54:52`. Direct publisher GET had 1,819 rows, all `srcUpdateTime=2026-10-13 17:40:52`; 176 records had zero rentable bikes, 51 zero return slots in this snapshot. These counts are observations, not all-city outage rates; active flags need filtering. Actual fields: `sno,sna,sarea,mday,ar,sareaen,snaen,aren,act,srcUpdateTime,updateTime,infoTime,infoDate,Quantity,available_rent_bikes,latitude,longitude,available_return_bikes`. 13 distinct area strings, so validate geographic scope rather than assume exactly 12 Taipei districts. Historic catalog schemas use older field names; inspected current schema governs. Twinkle's cached sample must not be represented as a live reading. One snapshot cannot establish chronic shortages or forecast future availability. |
| `169174`, [Taipei transfer-to-YouBike rentals](https://data.gov.tw/dataset/169174) | Taipei Transportation Department; OGDL v1.0, free. Official description explicitly covers **2023 only and will not update further**, despite metadata updated 2026-10-05. Twelve monthly resources describe bus/MRT-transfer rentals, not all trips. [December resource](https://data.taipei/api/dataset/d51e8336-fceb-4275-a81a-2a246f4fca1b/resource/8ddb45ba-a0f5-41d6-85a0-1691096fdcf8/download). | Actual publisher GET requested bytes 0–8191 but the server ignored Range and returned the full 62,285,127-byte CSV: parser received 518,189 data rows. Headers `借車時間,借車站,還車時間,還車站,租借時數,借車日期`; first sampled rental times `2023-12-16T23:00:00+08:00`. Only header/count/first timestamp validated: complete month dates, uniqueness, trips crossing month and duration validity remain unchecked. No card/person ID or prior transit station in inspected header. No station ID or coordinates: station-name reconciliation is required. Do not infer which MRT exit or bus route was used. Raw trips were held only in process memory; aggregate for publication. |
| `135775`, [YouBike Taipei station monthly usage](https://data.gov.tw/dataset/135775) | Taipei Transportation Department; OGDL v1.0, free; semiannual updates; metadata 2026-10-05. [Publisher resource](https://data.taipei/api/dataset/d8cefb03-aba2-41ca-9996-d8774313cdc6/resource/8f690548-61bc-4bff-8baa-01d465eb672c/download). | Twinkle metadata/sample returned actual columns `民國年,西元年,月份,發布機關名稱,機關代碼,臺北市YouBike每月使用量（次數）`, 66 normalized rows. Sample periods 2020/11 and 2020/12, counts 2,730,442 and 2,072,168. **Despite title, no station dimension.** Official catalog corroborates that schema. Exact final period not inspected; unsuitable for station-level demand, only citywide monthly context. Twinkle `join_keys_domain_hint` contains hypothetical route/station IDs absent from actual columns; hints are not observed join keys. |

Other Twinkle discoveries: `127189` city bicycle-lane inventory, `143893` riverfront access points, `144066` bicycle-passable bridges, `128415` and alias `tp-00001515` MRT bicycle parking coordinates. These were search hits only; no publisher resources/schema were established in this bounded pass (national pages for 127189/128415 timed out). They are leads, not usable dependencies or proof a legal/walkable/cyclable routing graph exists.

#### C01 Collision-site review

**Hypothesis:** a traffic engineer or district transport reviewer repeatedly chooses which corridor segments/time windows to inspect next. Show annual observed injury-collision counts, severity, time-of-day and road/signal cohorts; an evidence card links the exact year/source and missingness. Rank **inspection candidates**, without claiming true individual travel risk or a causal remedy.

**Inference / joins:** the verified 2025 collision CSV alone supports a useful first historical screen. Optional joins to organizer sidewalk/tree inventory or independently verified school/road geometry should use a validated projected CRS and auditable spatial bins/intersection boundaries; this pass did not verify school/road additions. Normalize ROC dates and decode the post-2023 codebook before selecting cohorts. Do not join first-party vehicle codes as though they identify all injured pedestrians.

**Smallest honest demo:** one district, 2025 only; spatially aggregate events into stable cells or verified corridor segments; filter a time band; compare top observed counts with a citywide/district baseline and show excluded/missing records. Display aggregate facts, not individual locations with demographics. An age-specific pedestrian solution remains blocked on full-party coverage, safe aggregation and code definitions.

**Current validation boundary:** T07 supersedes the former arbitrary time/site target. Compare the same official review packet and proposed evidence packet, preserving facility, period and victim/event uncertainty; no highest-count ranking is justified without authoritative aggregation boundaries.

**Missing / claim limits:** no pedestrian/cyclist exposure denominator, near misses, actual speeds, crossing volumes, verified intervention dates or cost constraints. Raw collision count cannot mean risk per crossing, blame, safest route, or demonstrated causal benefit. First-party-only rows severely limit victim subgroup analysis. No forecast or citywide optimal remediation claim.

**Data foundation and limits:** the published collision records support investigating a bounded historical comparison. Professional action recommendations and pediatric/pedestrian-specific safety claims remain unsupported; use the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates) for current status.

#### C08 YouBike transfer patterns and current availability

**Hypothesis:** a YouBike operations analyst repeatedly selects station/time bands for field review; alternatively a commuter chooses an available nearby pickup/return station. Use the 2023 **transfer-rental subset** to show historical departures/arrivals by hour/day and contrast contemporaneous live capacity/availability only with clear date separation.

**Inference / joins:** group 169174 by normalized station name and local hour; count departures and returns separately. Resolve aliases against 137993's `sna` after removing version prefixes, but do not silently fuzzy-match. A 2023 station may have closed, moved, split or changed capacity by 2026. Report matched/unmatched names and require manual verification of ambiguous matches. Citywide monthly 135775 can provide trend context but is not a direct transfer-subset reconciliation total. Previous MRT OD can supply separate 2023 station demand context only after explicit spatial/name validation; it cannot identify a transfer or reconstruct the prior transit leg.

**Smallest honest demo:** for a manually verified cluster of 5–10 stations, show 2023 December hourly transfer pickup/return profiles and historical imbalance, then a separately timestamped publisher snapshot and nearby alternatives. Historical net trips are not inventory or unmet demand. Keep current commuter choices based on live capacity alone. Stronger operational redispatch/forecast claims require historical station availability and truck/capacity constraints.

**Current validation boundary:** T10 completed the full month census and retained identity/completeness gaps. Compare current official tools on correct station/status/time handling and understood uncertainty; the former time target is withdrawn. A dated lookup never guarantees arrival availability.

**Missing / claim limits:** 2023 sample is dated and transfer-only, lacks unmet rentals, truck redispatches, guaranteed station identity/history and prior transit leg; one live snapshot cannot establish reliability or future availability. Historical trip imbalance does not prove a shortage or tell an operator how many trucks to send.

**Data foundation and limits:** descriptive historical transfer analysis and current lookup require full-month and station-identity validation, with historical/live separation explicit. These are different decisions; their unresolved joins do not establish current operational usefulness. Current status belongs to the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### Open questions / executable next steps

**Historical candidate-local options:** the later deep record and current ten-track queue supersede completed or no-longer-justified checks below; these are not outstanding mandatory work.

1. For collision review, parse the official post-2023 codebook and verify event vs party/severity semantics; audit all 2025 dates and privacy-safe aggregation. Do not start from a pedestrian risk score.
2. For YouBike, fully audit the already reachable December 2023 resource and resolve a small station cluster to the 2026 publisher inventory with explicit match/move checks.
3. Verify actual data needs with one intended analyst/commuter only after owner authorizes contact. No implementation, external contact, registration, payment or source-count-based readiness claim occurred.

### Environment, parks and street service track — outside organizer starters

**Later observation:** T01 matched all 745 park IDs/measurements across the existing endpoints and reproduced shared location anomalies; T02 established bin-lookup equivalence, a malformed longitude and a market-address conflict. The following earlier audits remain descriptive; apply those current limits before any spatial recommendation.

**Evidence — retrieved 2026-10-13.** This independent track used three authenticated Twinkle searches (2 credits each) and two metadata/sample reads (2 credits each), for 10 reported credits. No paid inference, payment, top-up, login or external message occurred. Queries: `臺北 公園`, `無障礙出入口` with agency `臺北`, and `垃圾 清運` with agency `臺北`. Broad multiword search returned irrelevant Taipei datasets; the narrower entrance search found useful sources. This is not an exhaustive catalog search. Two metadata calls read dataset 152266 and 126553 with two sample rows. Four publisher CSVs were then downloaded and completely parsed with curl and standard-library CSV. Python HTTPS verification failed due to certificate-chain verification; curl verified/downloaded the same resources successfully. No verification bypass was used.

#### Additional datasets and actual reads

All four national catalog pages declare **Open Government Data License v1.0**, free access. Public-page retrieval and file reads occurred on 2026-10-13. Dataset metadata dates are not field survey dates.

| Dataset / identity | Observed publisher access, schema and coverage | Consequence / limitations |
| --- | --- | --- |
| **Park accessible entrances**, Twinkle `152266`; [official catalog](https://data.gov.tw/dataset/152266), [Taipei page](https://data.taipei/dataset/detail?id=5a7258c2-5ded-4149-8664-ae10903fe372), [CSV](https://data.taipei/api/dataset/5a7258c2-5ded-4149-8664-ae10903fe372/resource/70defec1-fd51-471b-89fa-5c7636150e6a/download) | Parks and Street Lights Office. Twinkle normalised 2026-08-31; catalog 2026-07-22; publisher file 2026-03-16. Complete Big5 CSV: **745 entrance rows, 251 distinct park names, all 12 districts**, 46,966 bytes. ID, district, park, entrance, TW97 X/Y, sidewalk width and slope. Publisher specifies width as **minimum clear width in meters**, slope in percent. First entrance: Youth Park entrance 1, width 1.8 m, slope 8%; its coordinates are projected. Twinkle sample matched original sample. | Strong additional evidence for accessible green-space entrance analysis; not park boundaries, opening hours, canopy cover, shade or temperature. Number of distinct names is not an audited number of unique facilities. Twinkle says `geo_has_twd97=false` despite actual TW97 columns: inspect actual schema rather than trust enrichment flags. All-city completeness, coordinate validity and current entrance condition remain unverified. |
| **MRT accessible elevators/ramps**, Twinkle search IDs `128414` and duplicate municipal entry `tp-00001516`; [official catalog](https://data.gov.tw/dataset/128414), [CSV](https://data.taipei/api/dataset/0a3bb422-9eb5-459b-a9d4-138456516183/resource/61792c82-6609-41b2-9775-3a346934826d/download) | Taipei Rapid Transit Corporation; irregular, catalog 2026-08-31. Complete Big5 CSV: **193 rows**, 10,392 bytes. Index, elevator/ramp name, exit number, longitude, latitude; trailing unnamed empty column. First example Zoo Station exit elevator 1, exit 1, 121.5797157/24.9982136. | Genuine entrance positions allow station-to-park screening rather than measuring from a station centroid. Coverage includes the MRT network, not automatically Taipei-city-only: spatially filter. Does not provide downtime, opening hours or continuous accessible routes. Twinkle discovery was read; its normalized rows were not read for this dataset. Municipal/national duplicates must not be counted as independent evidence. |
| **Historical garbage/compost/pig-feed collection**, Twinkle `126553`; [official catalog](https://data.gov.tw/dataset/126553), [CSV](https://data.taipei/api/dataset/4363ed33-6f01-420c-aef7-acb016ee3eef/resource/683f30f8-5313-4ab3-8133-75a8c9f782fa/download) | Taipei Environmental Protection Department. Catalog 2026-09-11; Twinkle normalised 2026-10-08. Complete Big5 CSV: **32 rows/months, 2024-01–2026-08**, 929 bytes; year/month and garbage, compost and pig-feed tonnes. First sample 2026-08: 31,534 / 3,300 / 0 tonnes. Twinkle sample matched publisher. | Title says “各區隊”, but **there is no district or team field**. Treat as an unlabeled citywide aggregate pending publisher clarification. Suitable for aggregate monthly trends, not neighborhood/bin loads or collection routing. Remove thousands separators; ROC year conversion required. No bin fullness, missed collection, crew capacity, costs or service schedule. |
| **Traditional markets**, [official catalog `121593`](https://data.gov.tw/dataset/121593), [CSV](https://data.taipei/api/dataset/89bebb3a-990d-4070-bd67-631a575f6d4a/resource/35acfce1-2c4d-4c70-aa75-601cdab2b3f7/download) | Taipei Markets Administration. Catalog 2026-09-04, annually. Complete UTF-8 CSV: **47 market rows**, 21,668 bytes; sequence, title, descriptive content, creation date, address, longitude and latitude. First example Dalong public market, 121.514306/25.075139, creation date 2012/4/13. | Direct-source supplement, **not observed via Twinkle; no Twinkle ID asserted** (121593 is the national catalog ID). Geocoded venue context improves on the organizer's single citywide food-business count. It is not all food businesses, stall counts, visitor volume, waste quantity or rat ground truth. Creation date is not inspection/update date. Use title/address/XY only; avoid republishing incidental personal information from text. |

**Additional source, publisher API read:** [Wheelroute Taipei facilities](https://data.taipei/dataset/detail?id=2b58f15a-dec6-4b9d-91be-4eaccfda5ae7), Taipei Department of Transportation, offers facility types for ramps, entrances, toilets, sidewalks, marked sidewalks and crossings. The publisher describes width in **centimeters** (unlike the park CSV's meters), slope in percent and geometry; API example is `https://wheelroute.gov.taipei/wheelrouteApi/api/facility/Get/7`. Catalog declares public/free, dated 2025-10-13. No Twinkle identity asserted. A bounded curl GET of type 7 succeeded (160,058 bytes, JSON list) and exposed `kind`, `kname`, `lon`, `lat`, `X`, `Y`, `width`, `slope`. First MRT records had width/slope **-1**, while park entries had values such as width **1.5**, slope **5**. Some park records put a park name and entrance name in **X/Y**, not numbers. The documentation says centimeters, but 1.5 matches the meter-valued park inventory: this is an unresolved unit inconsistency, not a confirmed conversion. Use documented park CSV units and original XY rather than combining the API blindly. Do not infer detailed reuse license, complete topology, real-time condition or navigable connectivity from this response. -1 must not be treated as a measured negative width/slope.

#### C03 Accessible park-entry comparison

**Hypothesis — data-grounded extension, not a priority judgment.** User: district park-access improvement officer or an older resident's caregiver. Repeated decision: which entrance to inspect/improve first, or which listed entrance to examine for a planned park trip. Compare **actual park entrances** from dataset 152266 with **actual MRT accessible entrances** from 128414, display published widths/slopes and explain why a nearby park centroid is not an entrance. Population by age already audited in the organizer starter list can add coarse district/village context only after boundary joins are verified.

There is **no observed common stable entrance ID** across the two CSVs; their row indices are dataset-local. Station names/exit labels need manual normalization for station-level OD links, and approximate name/coordinate matching must report ambiguous cases.

Required joins: reproject TW97 coordinates to the appropriate CRS after confirming EPSG:3826 rather than relying on a field label alone; normalize whitespace/numeric fields; spatially filter Taipei; compare projected straight-line distances between entrance points. Group by district/park/entrance, not name alone. A distance rank is an inspection shortlist, **not an accessible walking route**. Full sidewalks/crossings/ramps and connectivity must be established before claiming a usable route. No invented paths or “wheelchair safe” labels.

Smallest honest demo: choose one district and two parks; show official entrance widths/slopes, nearby accessible MRT entrances, source dates, distance interpretation and a shortlist of entrances whose missing/outlier fields require survey. Allow user-specified width/slope filters clearly labeled as preferences, not regulatory certification. Measure reproducibility against publisher rows, percent valid coordinates/width/slope, deduplication and correspondence of 5–10 manually checked entrances. User usefulness still needs a park officer/caregiver task test.

**Inference — data foundation and limits:** geometry, width and slope are observed inputs for investigating an entrance comparison; they do not establish turn-by-turn accessibility or a cooling route. The two accessible-entry datasets and existing tree/sidewalk records can coexist, but tree points cannot supply shade. A live heat or shade model still needs canopy geometry, height/crown parameters, building shadows, time-dependent radiation/temperature and validation; older residents' registered addresses are not outdoor exposure. See the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### C07 Market-bin service audit

**Hypothesis — bounded extension of organizer bin prompt.** User: district sanitation supervisor planning a weekly field survey. Repeated decision: which market approaches or public street segments to inspect for missing service, signage or overflow first. Use the **47 geocoded market venues** plus already-audited official bin-location files, optionally park accessible entrances and verified MRT demand for context. This replaces an unusable citywide food-business-count input with specific public venues.

Required joins: normalize venue and bin coordinates in a metric CRS, deduplicate bins and resolve rows that represent multiple positions; match venue approaches to public street segments (market point is not its entrance or walking boundary). Report venue-to-listed-bin distances with a configurable inspection radius. Do not label missing points as confirmed absence or normalize by MRT demand as if it were street pedestrians. Distinguish market premises' own waste collection from pedestrian public bins.

Smallest honest demo: one market cluster, list the nearest inventoried bins and explain public/private service responsibility, identify map/data gaps and produce a field-inspection list. Success measure: valid coordinate/join fraction and agreement of a small field sample on whether listed bins/entrances exist, plus time saved preparing an inspection list. No claim that adding bins reduces litter without observation/intervention testing.

**Inference — data foundation and limits:** location records support investigating a spatial service inventory, not optimized placement or collection schedules. Dataset 126553 supplies only overall seasonal context; its citywide tonnage cannot estimate bin loads. Still missing pedestrian demand, municipal bin catchments, litter/overflow observations, actual cleaning schedules, costs and operational responsibility. Market points cannot predict rodent prevalence. Rat sighting ground truth, reporting effort, interventions and licensing remain unmet; no rat risk score is recommended. See the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### Recommendation and executable next action

**Historical candidate-local options:** the later deep record and current ten-track queue supersede completed or no-longer-justified checks below; these are not outstanding mandatory work.

**Inference — historical data-discovery result:** retain accessible green-space entrance comparison and bin/market audit as hypotheses; investigate their problem value under the current queue. Do not select shade optimization, rat prediction or neighborhood collection optimization on current evidence. Neither candidate is an owner selection or implementation authorization.

**Open question / next:** validate the complete 745-row park file for missing/outlier width/slope/XY and district/park duplicates, confirm projection and select one district for a 5–10 entrance manual correspondence check against current publisher maps. Audit connecting sidewalk/crossing geometry before proposing routes. Keep all user-specific mobility locations out of Git.

### Additional theme: everyday care-service access

**Later T08 observation:** richer current registry/meal schedules and assessment PDFs are audited above. Approved versus actual enrollment is available for a dated roster, but acceptance/vacancy and active deduplicated demand are not established; earlier CSV-only gaps below describe that earlier source set. Preserve the 440-row/September-demographic recipe unchanged.

#### Evidence — retrieved 2026-10-13

Method: authenticated Twinkle `tw_search_datasets` searches for `共餐` and `托嬰`, scoped to 臺北市; two `tw_get_dataset` metadata reads without row samples; official catalog HTML; direct publisher CSV GETs with curl and in-memory Python standard-library CSV parsing. No account registration, top-up, inference API, external message or applicant/person-level data. Phone/name/contact columns were not printed or retained. All five new datasets below are from Taipei Department of Social Welfare and declared OGDL-1.0-TW in official national catalogs; attribution is required. They are outside the organizer's specific starter datasets.

Twinkle spent 8 credits on successful searches/metadata, with cost_usd=0 on those receipts. Two bounded `tw_query_rows` attempts specifying only nonpersonal columns were rejected at the policy stage as `QUERY_NOT_ALLOWED`; inspect_tool still advertises these arguments, whereas the runtime demands `tw_query_dataset` structured queries. The bridge allowed only the older tool, so further MCP calls stopped; publisher CSV reads establish actual row access instead. No quota/top-up request appeared. Twinkle's quality tier is a provider label, not a validity assessment.

| Exact Twinkle ID / publisher catalog | Observed publisher resource | Verified content, dates and limitations |
| --- | --- | --- |
| **135495 — 臺北市銀髮族服務_臺北市老人共餐單位一覽表** ([national](https://data.gov.tw/dataset/135495), [Taipei](https://data.taipei/dataset/detail?id=fe55795c-a220-4b88-bde1-5b994321f8af)) | [CSV](https://data.taipei/api/dataset/fe55795c-a220-4b88-bde1-5b994321f8af/resource/86d839db-85c7-48b0-991b-dc86922eb093/download) | Complete 62,304-byte UTF-8 CSV parsed: **440 rows**, six columns: serial, site name, district, district code, address, institutional phone. All 12 districts present: counts range from20(Datong) to57(Daan). Twinkle row count agrees. National metadata and Twinkle updated2026-09-18, normalization2026-09-28; Taipei indexed page shows file2025-06-11. This discrepancy and absent row observation dates mean freshness remains unverified. No coordinates, meal days/hours, attendance, capacity, price, eligibility or barrier-free access. National live curl confirms OGDL; web tool failed that URL while curl succeeded. |
| **121337 — 臺北市嬰幼兒照顧服務_公辦民營托嬰中心** ([national](https://data.gov.tw/dataset/121337), [Taipei](https://data.taipei/dataset/detail?id=9c9a3f77-8340-48d8-bc0e-f9155521b758)) | [CSV](https://data.taipei/api/dataset/9c9a3f77-8340-48d8-bc0e-f9155521b758/resource/a02ccc34-dd28-4c5d-b527-c5433ec1a453/download) | Complete3,562-byte UTF-8 CSV: **29 rows**, institution type/name, `收托人數`, address, phone. First3 count values48,48,40. National metadata2026-03-10; Taipei indexed file2025-11-18; Twinkle normalized2026-09-30. No measurement timestamp. **Do not call `收托人數` vacancies, licensed capacity or current enrollment until publisher semantics are resolved.** No coordinates/hours/waitlist/fee. |
| **121278 — 臺北市嬰幼兒照顧服務_私立托嬰中心** ([national](https://data.gov.tw/dataset/121278)) | [CSV](https://data.taipei/api/dataset/081df75e-85c7-464c-b125-546920911c5c/resource/e7cdaca3-e9da-46f9-b857-395e6e8e06a6/download) | Complete28,984-byte UTF-8 CSV: **223 rows**; institution type/name, postal code, address, phone, plus an empty trailing column header. National metadata2026-03-10. Twinkle discovery returned normalized=true, but no MCP metadata/row query for this ID. No capacity, vacancies, fees, operating hours, coordinates or stable institution identifier. |
| **156685 — 臺北市托嬰中心評鑑結果** ([national](https://data.gov.tw/dataset/156685)) | [CSV](https://data.taipei/api/dataset/e7b45593-9d44-469c-97fa-f1a52c69ebaa/resource/43c0bdc5-ddb0-40bf-accd-a096d8c5ac23/download) | Complete21,520-byte UTF-8 CSV: **292 rows**, serial/name/district/district code plus ROC110–114 assessment columns (2021–2025). Nonblank per year59/119/78/81/128; thus **not a balanced annual panel**. Metadata2026-07-30. Twinkle discovered normalized dataset. No shared institution ID with center registries; missing evaluation cannot mean failure. Code/grade meanings and assessment cycles remain to validate. |
| **135696 — 臺北市托嬰中心收托人數** ([national](https://data.gov.tw/dataset/135696)) | [CSV](https://data.taipei/api/dataset/64f09ad9-718f-4df0-9707-8e3601587a5b/resource/46a0d037-52eb-479a-a10f-a44fdeb37a81/download) | Complete920-byte UTF-8 CSV: **20 semiannual rows**,2015H1–2024H2 (ROC104–113); period, citywide total enrollment, under1,1–under2,2–under3. Last total7,029. Metadata2025-12-30. **Citywide series**, no center or district; not a local vacancy/capacity series. Twinkle discovered normalized dataset. |

Existing, already publisher-audited prerequisite: [village population by age](https://data.taipei/dataset/detail?id=a6394e3f-3514-4542-87bd-de4310a40db3), actual2023-01–2026-09 records, sex/age and geographic totals. Select one month, village level and sex total before aggregation; exclude city/district total rows. This is registered population, not service demand or daytime population. Village geometry/address geocoding is a separately unresolved dependency.

#### Inference

The strongest directly supportable baseline is a **district-level service inventory adjusted for age composition**. Facility names and locations are not enough to infer service adequacy. Raw site counts can be normalized by registered target-age population for a comparison, but that remains an availability proxy: a meal site with ten seats and one with100 seats currently count equally. The 29public+223private childcare rows are not asserted to be the complete childcare system; community public childcare homes and other forms require separate inventories. The292 assessment rows cover a different historical universe; never treat all unmatched centers as unevaluated/bad.

#### C02 Senior-meal service inventory

- **Hypothesized user / repeated decision:** Social Welfare neighborhood service planner or district community-care coordinator comparing where to investigate or pilot another senior-meal location each planning cycle. The role, recurring workflow and demand remain unvalidated.
- **Decision improved:** select3 districts/then villages for field validation based on registered65+ population, listed meal-site availability and older-population trends. This prioritizes investigation, not automatically closing/creating sites.
- **Required joins:** meal district code ↔ population district aggregates. A second phase geocodes public facility addresses ↔ village polygons; validate every pilot site's match. District-level first version needs no geocoding. Existing sidewalk/tree layers could contextualize a later walk audit but cannot prove accessible routes.
- **Smallest demonstrable workflow:** choose a month and age65+/75+ → show twelve district counts and sites per1,000registered older residents → inspect3areas and exact source dates → create a field-check list. Geographic catchments only after geocoding/network validation; no unsupported “10-minute barrier-free walk” promise.
- **Success measure:**100% of displayed counts trace to source rows; all12district joins resolved; coordinator can identify and explain3validation targets; actual reduced planning time needs user testing.
- **Missing / validation:** site activity and address freshness, seats, attendance, meal dates/hours, eligibility, fees, duplicate/co-located sites and wheelchair routes. Older population is potential need, not actual users. The completed descriptive comparison does not establish a capacity gap or route access; use the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### C06 Childcare evidence shortlist

- **Hypothesized users / repeated decisions:** parent shortlisting centers when returning to work/moving; municipal childcare planner comparing the geography of listed options against under3population each planning cycle. These are separate proposed workflows, neither validated with users.
- **Decision improved:** parent sees nearby listed public/private choices with dated official assessment history; planner compares counts against registered0–2population and separates inventory from unknown availability.
- **Required joins:** institution normalized name + district/address with explicit unmatched/ambiguous status; no stable shared ID exists. District extracted from address is a validation step. Assessment year/date remains visible; do not convert intermittent grades into annual trends or generic quality scores.
- **Smallest demonstrable workflow:** select one district → list public/private options and matched dated assessment → compare district listed-center count per1,000registered0–2children → mark vacancies/fees/hours as requiring official confirmation. No real parent address/input stored. First validate20institution joins manually.
- **Current success measure:** preserve every included identity, assessment year and status exception, then compare the same parent task against the existing map/registry. The former universal join-percentage target is withdrawn; legitimate missing assessments remain missing.
- **Missing / validation:** complete service-type inventory, common IDs, currently active status, assessment meanings/cycles, capacity semantics, actual vacancies/waitlists, operating hours, cost and commuting preferences. Citywide historical enrollment is contextual only; these inputs do not establish resource-allocation or vacancy predictions. See the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### Open question / recommended next executable action

**Historical candidate-local options:** the later deep record and current ten-track queue supersede completed or no-longer-justified checks below; these are not outstanding mandatory work.

The twelve-district meal/population comparison is completed in the [dated calculation and recipe](#reproducing-the-meal-list-comparison). Remaining C02 checks are facility duplication and current activity/date/capacity: manually verify10facility entries against official current service pages. A new retrieval creates a new dated observation, not a replacement for the recorded result. Do not label lower per-capita site ratios as proven service shortage. For C06, validate public-center `收托人數` definition and20registry↔assessment joins first; if rates are poor, keep raw sources separate with explicit linkouts. These are candidate-local options under the [current queue](#next-investigation-queue); no topic or implementation is selected.

### Flood preparedness: Twinkle discovery plus original-publisher audit

**Later observation / pending historical revalidation:** T09 audited all three KMLs, found invalid geometries and current publication conflicts. Its exact district+name join produced 387 pairs/36 water-flag differences, and name-only produced 389/37; the earlier 386/37 result below was not reproduced. Preserve it as a historical observation pending recipe/version reconciliation, not a current denominator or operational change count. C05 real-facility demonstration is blocked pending verified entrance/floor evidence.

Retrieval date: 2026-10-13. Ownership: independent read-only flood track; no repository edits, application code, login, payment, or external message. All solution proposals below are **Hypotheses**, not selected products or validated operational advice.

#### Evidence: method and MCP limits

Used the authenticated shared Twinkle MCP bridge, inspected schemas first, then searched `淹水` + agency `臺北` (10 hits), `避難收容` + agency `臺北` (8 hits), and `降雨積水` (5 hits). Read metadata of `tp-00003479` with sample_rows=0; attempted a 3-row query with only institutional/noncontact fields. Confirmed discovery/metadata cost: 8 credits. Attempted row tool advertises 1 credit but returned a policy error, so actual charge for that failure is unconfirmed; total exposure at most 9 credits, no top-up. USD/LLM fields returned 0.0 for successful calls. No inference tool used.

`tw_query_rows` was described as accepting columns, where and group_by, but an accepted-schema call with columns returned `QUERY_NOT_ALLOWED`: “不接受 SQL 片段(columns)。請改用 tw_query_dataset 的結構化條件(filters / select / aggregate / group_by / order_by)。” This is a runtime/documentation mismatch, not proof rows are absent. A repeat after the local display-helper failure again returned the policy error; root receipts do not establish that it was served from cache. Failed-call billing is unverified. No out-of-scope inference tool was used.

Original data were read directly with curl, Python standard-library csv and XML/ZIP parsing. CSV full-file and one KML full-file were inspected; latest ODS was parsed in memory without saving its contact/name/phone fields. Only nonpersonal counts, institutional examples and schemas are retained here.

#### Evidence: additional dataset inventory

These are outside the organizer starter list. Twinkle IDs with national and `tp-` equivalents can refer to the same underlying source: **do not count mirrors as independent evidence**.

| Exact Twinkle ID / title | Publisher and URL | Access, schema, date, geographic coverage and license | Suitability / limitations |
|---|---|---|---|
| `tp-00000862` and `121550` — 臺北市降雨積水模擬圖（112年更新版） | Taipei Hydraulic Engineering Office; [national catalog](https://data.gov.tw/dataset/121550), [city catalog](https://data.taipei/dataset/detail?id=fa1e8012-ebb4-473b-888e-97f9a9ce365e) | Twinkle search returns KML resources; `tp-` says normalized=true but national ID says false, both geo flags=false. Official publisher explicitly states WGS84. Three scenarios 78.8/100/130 mm/hour, depth >15cm, model year ROC112/2023. National catalog lists OGDL v1/free, metadata 2026-09-09. Full [78.8 scenario KML](https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/173adcbe-0f2e-4941-b2bc-127c09db0391/download) downloaded (893,437 bytes); XML contains GRIDCODE, depth, case, year, AGENCYCODE. 1,945 Polygon elements in three Placemark depth classes: 0.15–0.30m, 0.30–0.50m, 0.50–1.00m; case=78.8mm_hr, year=112. | Strong foundation for scenario comparison/asset-exposure screening. These are **official simulated scenarios**, not real observations or forecasts. Do not interpret the absence of a polygon as no flood risk; <15cm omitted. Officially for disaster prevention/preparedness, unsuitable for land-use/development restrictions. One scenario fully parsed; other two linked, not yet downloaded. |
| `tp-00003479` and `135484` — 114年臺北市可供避難收容處所一覽表 | Taipei Social Welfare Department; [city catalog](https://data.taipei/dataset/detail?id=f327232d-9230-44d0-bf0c-df151802da32), [national catalog](https://data.gov.tw/dataset/135484) | Twinkle metadata: 399 rows, CSV, 2025-06-16 upstream, mirrored 2026-09-30, actual columns include district/village/address, disaster flags, accessibility, service villages, capacity, area; no XY, join_keys empty. Full [publisher CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=3f20cc14-91a9-41de-8d03-6e019ec4d82c) 77,891 bytes parsed: 399 rows/12 districts, flood flag 是206/否193, accessibility 是360/否39. Twinkle declares OGDL v1 attribution required; city page says public/free and links government license. | A real accessible older inventory, not current opening/capacity. **A separate newer education inventory is available; authority, scope and responsibilities must be reconciled before selecting an operational source.** Metadata notes contain `synthetic; ... data.taipei mirror` but this does not establish fabricated records: direct publisher CSV independently matches the reported 399-row structure. The “not on data.gov.tw” note conflicts with discovered national ID135484. |
| `tp-00002066` and `134683` — 臺北市可供避難收容處所一覽表 | Taipei Education Department; [city catalog](https://data.taipei/dataset/detail?id=aaf97773-3631-40e2-b3cc-da87bf2ce1d5) | Twinkle search identifies this separate dataset, no metadata/rows read via MCP. Official file updated **2026-09-14**, public/free, government-license link. [Download](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=4c92dbd4-d259-495a-8390-52628119a4dd) catalog labels CSV but GET is **88,568-byte ODS ZIP**, parsed in memory: 450 XML rows, **419 institutional records with SA-prefixed ID** across12districts. Water disaster 是173/是(備用)21/否225, accessibility 是380/否39. Fields additionally include 最大容納人數; no XY. Header 名稱(學校機關全銜) differs from old CSV. Contact/person fields exist but excluded from retained results. | Newer separately published inventory, still no verified operational authority, live opening, occupied beds or safe route. The comparison used an exact-name lookup of the old file (399 distinct names), matched against each of419 current SA-ID records:386 current rows had an old-name match; **37 of those386 matched rows** had different flood flags. Current file has419 distinct SA IDs but418 distinct names (雙永國小 appears twice), so these are row-level comparisons, not a complete stable-ID change history; renamed/new records are excluded and name collisions may map to the same old record. Among the matched rows, e.g. 螢橋國中 changed 是→否. **Source selection changes the displayed eligibility flag; an actual operational eligibility change is not established.** Names alone are not stable IDs and may merge records; no join completeness claimed. The school example establishes a source-version difference only, not an evacuation recommendation. |
| `tp-00003001` — 臺北市防洪設施 | Taipei DBAS; [publisher catalog](https://data.taipei/dataset/detail?id=4bb8d221-8c9b-4a27-b16a-b944de7c3d07) | Twinkle search: annual CSV, normalized, no latlon/TWD97. Publisher catalog inspected: 1968–2025, 2026-04-10 metadata, river-name/statistical-period, levee/revetment lengths (m), pumping station/gate counts. Public/free, government license link. **Resource rows not read**. | Useful annual river/city context, not pumping capacity, equipment coordinates, uptime or neighborhood flood prediction. Not a substitute for live sensors. |
| `tp-00003003` — 臺北市防洪工程 | Taipei DBAS; [publisher catalog](https://data.taipei/dataset/detail?id=e9377af0-6565-4742-bec1-a10c3b846981) | Twinkle search: annual CSV. Publisher catalog inspected: 2008–2025, 2026-04-10 metadata, annual environmental-improvement/maintenance/mitigation/disaster-repair lengths of levees/revetments in meters. Public/free, government license link. **Resource rows not read**. | Context only; annual lengths cannot establish intervention effectiveness or neighborhood maintenance priorities. |

The three scenarios have separate official resource URLs: [100mm/h KML](https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/4b14c3a0-fcf2-48d4-9c93-e27784cae29d/download), [130mm/h KML](https://data.taipei/api/dataset/fa1e8012-ebb4-473b-888e-97f9a9ce365e/resource/2954e8d4-cb67-40c9-8ab8-019ad10b758e/download). Web text extraction rejects XML/CSV/ODS content types; successful direct curl/file parsing, not that extractor error, establishes access to the inspected resources.

#### Inference: data sufficiency

This track is substantially more ready for **pre-disaster preparation analysis** than real-time flood warning. Real reference data exist for shelter type/accessibility/capacity/service villages, plus official modeled inundation polygons. The missing work is address geocoding, village-boundary joins and version/flag interpretation; it is not necessary to invent rainfall observations. Twinkle quality tier and normalization flags did not reveal real resource format, observation/model date or version drift. Use it to discover, then pin publisher versions.

The organizer rain API's previously observed year2061 anomaly and its station-locations-only water-level dataset remain unresolved. Do not bring these into a live warning solution without independent freshness/threshold verification.

#### C04 Village shelter preparedness

**User:** district-office disaster-preparedness coordinator. **Repeated decision:** before typhoon season/exercises, which villages need shelter inventory confirmation, accessible alternatives or capacity review?

**Required fields and joins:** latest shelter ID/address/water-disaster eligibility/accessibility/service-village strings/capacity + district-qualified village names and current boundaries + latest village population/65+ age groups already audited in repo. Normalize service-village strings, qualify by district, deduplicate facility IDs. Count served villages separately from allocating capacity: one shared shelter's full capacity must not be assigned to every served village. Geocode only an authorized selected district using official address/point source, record match confidence; missing XY must stay missing. Population registers measure registered residents, not actual evacuation demand.

**Smallest honest demonstration:** choose one district, show flood-eligible facilities, backup flags and accessibility; for each village show whether a listed facility serves it and share of65+ registered residents. Display capacity as a facility attribute and explain that it is shared. A useful first demo is a table with flagged data-confirmation tasks; no map, route or modeled occupancy is required. Show 2025vs2026 changes as provenance, not automatically actionable alerts.

**Success measure:** manually checked village-service and eligibility joins match the publisher for a selected small sample; coordinator can find 3 concrete inventory questions faster than searching spreadsheets. Measure task time/decision agreement with a coordinator; no claim of increased evacuation safety before testing.

**Missing/remaining validation:** no user interview; service-village spelling/district joins; field meaning of flood suitability and 備用; difference between normal/max capacity; occupancy assumptions; newest-file authority and update cadence. A bounded administrative comparison does not establish evacuation instructions. See the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### C05 Rainfall-scenario facility review

**User:** district disaster planner/facility manager. **Repeated decision:** under standardized rainfall scenarios, which designated facilities or access approaches should receive a preparedness review or an alternative plan first?

**Required fields and joins:** the three official 2023 inundation KML scenarios + geocoded latest shelter points/verified entrance positions + optional village polygons. Spatial point-in-polygon with scenario/depth class; preserve WGS84 input, use projected CRS only for distance/area. A building centroid is not its entrance, ground-floor elevation or operating floor. Do not infer that a shelter inside a polygon is unsafe; it may use upper floors. Official scenarios cover modeled surface accumulation, not every mechanism of flooding.

**Smallest honest demonstration:** one district, 10–20 manually verified institutional points, one fully audited 78.8 scenario initially; display “reference point intersects modeled depth band” and request manual facility review. Add100/130 only after their full files/legends are validated. Keep official modeled inputs visibly labeled; no generated flood observations. Do not output “safe evacuation route”.

**Success measure:** every demo point/location and intersected class independently checked against official KML; no silent geocode failures; user can explain why each review candidate appears. Later validate review usefulness with a district practitioner, not predictive flood accuracy.

**Missing/remaining validation:** official entrance XY source, three-scenario geometry integrity/full classes, floor/elevation/entrance barrier data, safe routes/current closures, capacity under each hazard. Scenario review does not establish automated shelter selection or routing. See the [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates).

#### Open questions / next executable action

**Historical candidate-local options:** the later deep record and current ten-track queue supersede completed or no-longer-justified checks below; these are not outstanding mandatory work.

1. First validate the latest 2026 education shelter ODS for a single district and formal flood/backup capacity semantics; determine whether social-welfare2025data is superseded or owns a different operational process.
2. Obtain an official institutional-coordinate/address source, manually check10points, and download/parse both remaining scenarios. No address may be silently assigned to a city/district centroid.
3. Ask one preparedness coordinator whether village-service inventory comparison is a repeated useful task before selecting/building either proposal.

No owner solution selection, implementation, model inference, registration, messaging or paid access occurred.

### Next-investigation queue

**Current research dispositions — 2026-10-13:** all ten assigned tracks completed their public-source
investigation and minimum workflow records. The table now names unresolved consequential checks;
it is neither a launch queue nor a priority ranking. The first-check queue and C01-first priority
are superseded. Source-level results can reject a proposed interpretation while user value remains
unknown. No implementation, participation or contact is authorized by this table.

| Track | Completed investigation disposition | One bounded next public-source action |
| --- | --- | --- |
| T01 | Narrow inspection/checklist; defer shade/routing recommendations | Compare named-street history and the two anomalous entrance plans; preserve missing connections |
| T02 | Narrow placement/C07 verification; defer real collection optimization | Inspect current replacement SOP and published sensor-trial results before more mapping |
| T03 | Defer duplicate intake; investigate inspection/ownership/recheck | Find a current public joint-inspection/recheck form and test condition→owner→completion linkage |
| T04 | Retain timing trial/evaluation hypotheses; no optimal clock or causal savings | Inspect named-city-detector historical catalog, retention and exact reuse terms; stop at auth/payment |
| T05 | Narrow service/duty evidence reviews; defer operational redesign | Trace Blue27 reduction rationale and current TTSB actual-duty monitoring response |
| T06 | Narrow professional preparation and opt-in meeting; reject safety rankings | Compare current NCREE meeting intake and Taipei station service fields with the proposed packet |
| T07 / C01 | Narrow next site-review question; generic hotspot gap refuted | Inspect Gongguan micro-adjustment review record for boundary, rationale and rejection reasons |
| T08 / C02/C06 | Narrow meal/access and parent reconciliation; defer shortage/vacancy claims | Find completed district childcare demand-analysis report requested in2025 and inspect sample/deduplication/acceptable service |
| T09 / C04/C05 | Manual discrepancy review; real facility-scenario demo blocked | Compare the two螢橋 school references with latest Zhongzheng flood maps/revision dates |
| T10 MRT / C08 | Retain metro review; historical subset and current lookup separate | Extract line-specific waiting results for one review case; retain historical station/lookup checks in its workflow records |

The [current comparison](#cross-topic-decision-comparison) recommends the two-school publication
check as a next research experiment, not topic selection. Every workflow retains its own additional
resolution/resume condition in the detailed record. Practitioner effort/acceptance tests require
separately authorized participation; absent public records do not prove agencies lack them or
people do not experience difficulty. Do not substitute invented labels, arbitrary buffers or
weighted scores for unresolved evidence.

## Research questions

These are organizer-direction questions, not claims of feasibility, demand or a second priority list.
The [current queue](#next-investigation-queue) governs research sequencing.

| Direction | Next evidence to seek | Decision the check informs |
| --- | --- | --- |
| Trees / shade | Tree locations, condition and sidewalk geometry; distinguish removal from planting opportunities | Can an actionable site comparison be supported? |
| Public bins | Locations, service responsibility and usable demand observations | Can placement or collection alternatives be compared honestly? |
| Rats | Reporting bias, spatial resolution and independently supported predictors | Is an exploratory map justified without claiming predictive accuracy? |
| Neihu traffic | Detector coverage, timestamp quality and history access | Can morning traffic changes be shown using observed data? |
| Bus networks | Stop-level ridership availability and driver-rest constraints | Is route analysis possible without invented passenger demand? |
| Building resilience | Building-level availability, aggregation limits and expert validation needs | Can a screening demonstration avoid unsupported safety judgments? |
| Open topic | A specific civic user, repeated task and accessible evidence | Does it offer a clearer bounded research target? |

## Investigation sequence

| Stage | Observed state | Remaining work |
| --- | --- | --- |
| Organizer dataset audit | Completed point-in-time access/schema audit of 22 distinct government catalog pages | Refresh the exact chosen dependency; complete workflow-specific field/coverage checks |
| Expanded discovery | Four tracks completed Twinkle discovery and publisher reads; eight hypotheses recorded | Search hits and unparsed sources remain leads, not dependencies |
| Descriptive cross-source analysis | Twelve-district meal-list/age-population comparison reproduced | Verify listed facilities' activity/date/capacity before any service-adequacy conclusion |
| Problem/decision validation | Ten tracks/25 workflows investigated; source-level rejection comparisons complete, practitioner gain untested | Follow the current queue; separately authorize practitioner comparison if selecting a pilot |
| Selection and implementation | No topic selected; no contest app built | Owner selection/request and rechecked event rules required before implementation |

The [next-investigation queue](#next-investigation-queue) owns the executable research sequence.
Existing validation thresholds are proposed checks, not completed tests or measured user benefits.

## Open questions

- **Participation:** research does not establish registration or acceptance. Owner decision needed
  if participation is desired; check the current process before collecting personal details.
- **Data:** listed sources have now received publisher-level access/schema checks below. A selected
  workflow still needs full-slice completeness, spatial joins, field units and suitability validation.
- **Demonstration timing:** the page permits coding from Day 1. Eligibility of pre-existing code
  is unclear; check official clarification before reusing a prebuilt contest artifact.
- **Practical delivery:** no topic, team, budget or application stack has been selected. Research
  should first identify a useful workflow and its necessary evidence.

## Data investigation scope and method

**Owner decision — 2026-10-13:** investigate the data mentioned by the organizers in depth before
selecting a topic. This authorizes public-source research, not contest implementation or registration.

**Owner decision — 2026-10-13, historical refined scope, superseded for prioritization:** the
earlier data-readiness-first direction led to expanded discovery beyond organizer starter APIs.
The current umbrella policy now places evidenced problems and success/rejection criteria first.
The owner separately requested finding and configuring a Taiwan open-data MCP at repository scope. This authorizes research-tool
configuration, not a contest application or paid subscription.

**Evidence — retrieved 2026-10-13:** the [organizer's issues section](https://puma.taipei/hackathon#issues)
lists government datasets and supplementary websites. It still says the de-identified citizen
feedback will be released soon; no download for that feedback was observed. Its rules restrict that
feedback to this event, prohibit real personal information, and require disclosure of simulated data.
Do not confuse that forthcoming feedback with Taipei's public complaint-category dataset.

Method: follow the organizer's links to publishers, inspect public HTML/metadata and resource
responses with curl and standard-library parsers, and use primary-source web search to recover
moved links. Publisher checks are point-in-time public reads without official-account login or purchases.
Earlier authenticated Twinkle discovery is described in [the discovery provenance](#taiwan-open-data-discovery-provenance); this public edition includes no authentication material. HTTP 200
is not a usable-data verdict: inspect content type, actual columns, records and observation dates.
Publication/update timestamps do not establish the dates represented by rows. A resource sample
does not establish complete geographic coverage, join success or model validity. No private citizen
feedback, report descriptions, photographs, names or exact report coordinates are stored in Git.

## Supplementary platforms and organizer-only inputs

All observations below were retrieved on **2026-10-13**. These are separate from the dataset-ID audit.

| Source | Evidence and observed access | Restrictions / limitations | Consequence for a candidate |
| --- | --- | --- | --- |
| [Organizer citizen feedback](https://puma.taipei/hackathon#issues) | curl HTML: release is forthcoming; no resource inspected | Activity-only; de-identification is not permission to re-identify or republish. Schema, volume, dates and spatial precision unknown | A feedback-driven tool must remain a hypothesis until released and inspected. Do not make this an essential dependency yet |
| [Tree/streetlight information website](https://geopkl.gov.taipei/) | curl returned 200 and the public page contains a tree-movement-history search interface | Query website, not a demonstrated bulk history export; no bulk-data license or complete removal series established. Python TLS verification failed in this environment while curl succeeded | Useful for manually validating a small number of tree records; does not establish complete annual removal causes |
| [TDX API guide](https://tdx.transportdata.tw/api-service/swagger) and [homepage](https://tdx.transportdata.tw/) | Official indexed guide describes basic, advanced, historical and other service families. Guest access is browser-only basic service, at most 20 requests per source IP/day; member programmatic access requires Client ID/Secret. Homepage describes a basic-member monthly allowance of 3 points | No account, token or authenticated historical query used. Endpoint-specific historical availability, dates, retention, charges and license still need verification; the existence of a historical service does not prove Taipei VD history access | Treat static topology, live snapshots and historical series as three different dependencies. Do not assume a free unlimited API, or that self-collection is the only historical-data route |
| [Rat Radar reports](https://ratdar.taipei/reports), [CSV export](https://ratdar.taipei/reports/export), [transparency page](https://ratdar.taipei/transparency) | curl CSV parsed **1,429 rows** with columns report time, type, location, status, description, photo URL, latitude, longitude. Time span in export: 2026-05-01 13:20 to 2026-10-13 08:11; 1,410 rat reports and 19 bait reports. Status: 1,373 reviewed, 3 reported to 1999, 53 pending. Coordinates nonempty in all rows | Mixed cities and report types; pending entries explicitly unverified. Reviewed does not mean independently confirmed infestation. Export/reports/transparency/home pages inspected did not expose an explicit reuse license; absence in these pages is not proof none exists. Text/photos can contain personal or identifying information; no raw reports retained | Observable data for exploring **reported sightings**, subject to permission and privacy review. Cannot equate report density with rat prevalence or infer propagation. Filter city, type and review status, deduplicate, aggregate and check reporting bias |
| [Old night-market entry](https://foodtracer.taipei.gov.tw/Front/Nightmarket), [official move notice](https://foodtracer.taipei.gov.tw/), [new entry](https://foodtracer.health.gov.taipei/Front/Nightmarket) | Old organizer URL fails curl hostname certificate validation. Official indexed move notice names the new host. New-host curl returned 200 but the page title was **maintenance**; one repeat returned no usable text | No live vendor table, export or API read established. [Government catalog 62075](https://data.nat.gov.tw/dataset/62075) describes 14 night markets, vendors and ingredient provenance; this indexed description is not a current resource-access result | A moved official website is recoverable, but night-market food disclosure is not a complete geocoded inventory of all restaurants or a rat-risk label |
| [Taipei liquefaction portal](https://soil.taipei/) and [official Q&A](https://soil.taipei/Taipei2019/Main/pages/QA_handle.html) | Root returns an HTML refresh to [current landing page](https://soil.taipei/Taipei2019/Main/pages/index.html); curl reads the public query information | Official Q&A states the medium-resolution city map cannot determine liquefaction at an individual building site; professional assessment requires foundations and geotechnical information. No bulk download rights inferred from the query interface | Supports contextual area-level screening and referral; cannot validate a building safety score |
| [Education Department check portal](https://www.doe.gov.taipei/News_Link.aspx?n=9E714C7EB1702778&sms=10FAB7D5E5149055) | curl 200 and primary-source web inspection: an index linking personnel announcements, kindergarten public/building inspections and other checks | An HTML index, not a verified normalized dataset or complete registry. No personnel records ingested; current legal publication/reuse scope and coverage were not audited | Potential navigation/lookup workflow only after resolving the exact source and permissible fields; unsuitable as a default personal-data aggregation project |
| [Taipei data catalog](https://data.taipei) | Organizer offers this as a general discovery entry point | Not a dataset dependency by itself | Select and audit an exact dataset/resource rather than citing the catalog as evidence of access |

**Inference:** the organizer's data list is a starting bibliography, not a ready-made analytical
dataset. Website availability, machine-readable availability, permission to reuse, and fitness for a
particular decision are four independent checks.

## Additional recovery check: Taipei VD dynamic feed

**Evidence — retrieved 2026-10-13:** after discovering the organizer's county-traffic catalog entry
was withdrawn, primary-source search found the [Taipei VD data catalog](https://data.taipei/dataset/detail?id=e57afe7f-3c9e-4f31-9208-eed859a92600).
Its embedded metadata names Open Government Data License v1.0 and links to
[GetVDDATA.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/GetVDDATA.xml). curl returned 200;
Python ElementTree parsed the full 502,557-byte response: 724 `VDDevice` elements and 2,195
`LaneData` elements, with `DeviceID`, `TimeInterval`, lane number, volume, average speed,
occupancy and vehicle-class volumes. However, **`ExchangeTime` was `2024/11/14T16:46:02`**.
No fresh measurement timestamp was established. The file's `TimeInterval=5` in inspected devices
is not sufficient documentation of units or every device's aggregation semantics.

**Inference — legacy endpoint only:** this is an accessible but stale snapshot, not a verified live feed. Do not present it
as 2026 traffic, start a collector under the assumption it updates, or claim Neihu morning-peak
history is available. The later v2 observation below resolves current public access through a
different resource; historical coverage still needs independent evidence. This recovery check is an additional dataset,
outside the 22 unique government dataset links in the organizer's list.

**Evidence — independent integrator readback, 2026-10-13, later observation:** full curl GETs of
[VDLive.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/VDLive.xml) and
[VD.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/VD.xml), parsed with namespace-aware Python
ElementTree, returned 650 unique live `VDID` values and 641 unique static values. The live
`UpdateTime` was `2026-10-13T18:53:40.001+08:00`; static time was midnight of the same date.
Both declared `LinkVersion=25.12.1` and `UpdateInterval=60`. Exact identifier-set comparison
matched all 641 static IDs and left nine live-only IDs. The live schema contains link/lane,
speed, occupancy, vehicle-class volume and collection-time fields. This is a source snapshot,
not proof every reading is fresh, valid or independent. Live-only IDs lack a static location
in this comparison; no location was invented. The update interval does not establish the
measurement aggregation interval. This readback does not establish archived weekday history,
Neihu commuter origins, employer shift feasibility or any causal travel-time benefit.

## Analytical controls before selecting a topic

**Inference — proposed acceptance checks, not measured results:**

1. **Match the unit of analysis.** City totals, district food-business counts, village populations,
   stops, trees and building sites cannot be joined as if they were equivalent observations.
   Never distribute a district total across points and label the result observed demand or risk.
2. **Establish spatial keys.** Prefer stable publisher IDs. For coordinate joins, check CRS, axis
   order, Taipei bounds and geometry validity; for name joins, normalize Taipei spelling and aliases
   but report unmatched records. A 300 m straight-line buffer is a scenario, not a measured walking
   catchment; roads, crossings and entrances can change accessibility.
3. **Align time.** State each dataset's observation period and refresh behavior. Join traffic
   by detector, direction, lane, vehicle class and timestamp. Only sum disjoint count intervals;
   do not sum rates or speeds, and do not count the same vehicles repeatedly across downstream
   detectors. Verify the publisher's aggregation definition before making 15-minute statistics.
4. **Separate observation from counterfactual.** An assumed 10% shift in commuters, candidate bin
   placement, future tree canopy, synthetic bus boardings or a manually weighted risk score is a
   scenario. Label inputs and results accordingly. It does not prove reduced travel times,
   garbage overflow, rodent numbers or earthquake losses.
5. **Measure dependency quality.** For a chosen workflow, report records used, missing values,
   duplicates, successful joins, stale timestamps, invalid units and coverage gaps. Missing live
   readings are unknown, not zero. A fresh metadata date cannot rescue an old resource.
6. **Keep licenses separate.** Record each dataset's exact terms and attribution. A government's
   open-data license does not automatically cover third-party reports, photographs, tiles or
   the organizer's activity-only feedback. Unknown permission blocks redistribution, not further
   read-only investigation. Use an explicitly licensed public-data sample for a reproducible demo.

## Publisher dataset audit

**Evidence — retrieved 2026-10-13:** the organizer supplies 26 government dataset link
occurrences, representing **22 distinct dataset pages** (4 on data.gov.tw and 18 on data.taipei).
Every distinct page was read successfully with curl. A browser-index read of the bus-stop page
returned 503 once, but the direct page and its ZIP both returned 200. Python's default TLS library
rejected the Taipei portal certificate chain; curl succeeded with its normal verification. These
are client-specific observations, not proof of universal availability.

Method: extract organizer anchors; read publisher HTML and metadata; follow actual download
links; request the first 262,144 bytes with HTTP Range where supported; parse full responses when
servers ignored Range. Follow pointer CSVs to their actual sources. Tree inventories and the bus
shape GZIP were subsequently read in full to resolve duplication and dates. Requests used public
endpoints without account login. No raw records, credentials, restricted complaints, or personal
information were retained in Git. Counts describe this retrieval, not guaranteed totals in future
exports. Metadata dates below are **catalog dates**, unless labeled file, survey, record or coverage.
A successful HTTP response is an access check, not a complete accuracy assessment.

Reproduction method: HTTP GET each linked source/download; decode CSV using the response charset
(Big5 where labeled); parse CSV with a quoted-field-aware reader and count nonempty data rows
without the header. JSON counts use array length or FeatureCollection `features` length; tree
uniqueness uses TreeID, hole uniqueness uses TreeHoleID and serialized whole-object equality.
The earlier GZIP-method description used a `BusInfo` wrapper; the T05 re-read found the shape response is a root JSON array, while ETA retains `BusInfo`. Wrapper/version continuity with the earlier read is unverified; use the observed response schema. The bus SHP ZIP record count
uses the DBF header rather than validated geometry. Date bounds are lexical bounds of the stated
fixed-width strings, with blank values reported separately. Invalid-looking survey dates are
flagged as suspected placeholders; their original meaning was not confirmed with the publisher.

### License and interpretation

**Evidence:** all four national catalog pages explicitly name Government Open Data License v1.
The 18 Taipei pages say `公開` (public), free, and link the platform's
[Government Open Data License v1](https://data.taipei/rule). That policy permits reuse and derived
services without individual written permission, subject to attribution. Preserve publisher,
release title/version and year; link the license. Platform openness does not erase third-party
rights or establish that a separate event-only complaint feed is open data. No separate resource
license override was observed in the sampled pages. Recheck terms when freezing a project source.

Resource labels in the inventory use “Download CSV/asset” for exact public URLs of the form
`https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=<rid>`.
Older national-catalog links sometimes use `/api/dataset/<dataset>/resource/<rid>/download`;
those exact links were also tested successfully below. `200/full` means the response ignored the
requested Range or the file was deliberately read in full; `206/sample` means a byte-range sample.

### Trees and shade: four dataset pages

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [128274: 臺北市行道樹及公園樹木分布圖](https://data.gov.tw/dataset/128274) | Parks and Street Lights Office; irregular; catalog 2026-07-28. Three public inventories. | [TaipeiTree.json](https://tppkl.blob.core.windows.net/blobfs/TaipeiTree.json), [TaipeiParkTree.json](https://tppkl.blob.core.windows.net/blobfs/TaipeiParkTree.json), [TaipeiTreeHole.json](https://tppkl.blob.core.windows.net/blobfs/TaipeiTreeHole.json): initially 206/sample, subsequently full parsed JSON. 90,441 street trees, 72,011 park trees, 2,259 hole rows. TreeID, district, road/park, species, Diameter, TreeHeight, SurveyDate, TWD97X/Y, UpdDate. Matching CSV/XML alternatives appear on publisher page. | All street-tree export dates equal 2026-10-13; 86,800 survey dates precede 2025. Park export date 2026-07-14; 57,961 surveys precede 2025. One street survey and 161 park surveys blank; earliest nonblank values 1900-01-01 / 1899-12-30 look like placeholders. Both TreeID sets unique and XY nonblank, but coordinates not independently surveyed. Diameter/height units were not established by the page. No crown polygon, leaf density, tree health or sunlight time series. Hole export has 1,308 unique IDs and 1,758 exact unique objects: deduplication is required before counting. |
| [134908: 臺北市人行道固定設施物_樹穴](https://data.gov.tw/dataset/134908) | New Construction Office; irregular; catalog 2026-09-22. | [Exact resource](https://data.taipei/api/dataset/693705fa-4604-4207-bd50-8a9ce9fcfbc6/resource/3e2b359b-8dae-46e4-a747-5912d8743d0e/download): 200/full, 27,304,373 bytes; GeoJSON with EPSG:3826; 56,720 MultiPolygon features. OBJECTID, Name, Town_N, X_3826/Y_3826. | Name values include **50,904 樹穴 and 5,816 花圃**. Not every feature is a tree hole and no occupancy/plantability field was observed. Distinct publisher inventory from 128274's holes; no verified common key. Catalog freshness does not establish survey freshness. |
| [715d3a83: 臺北市人行道固定設施物_人行道範圍圖](https://data.taipei/dataset/detail?id=715d3a83-8445-4496-b6bf-b0900538b7e7) | New Construction Office; irregular; file 2026-01-14, catalog 2026-09-22; coverage starts 2020-10-26. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=b11d6142-1d71-41d5-a843-7b7cfcea61ef): 200/full, 24,404,580 bytes, 15,053 GeoJSON features, EPSG:3826. ID, Town_N, NAME_Road, PSTART/PEND, side, SW_LENG_ItemValue, SW_WTH_ItemValue, Shape_AR_ItemValue, SWW_WTH (clear width), code, geometry. | Rich sidewalk geometry supports spatial joins. Width/length units not explicitly established in the observed metadata. District uses codes in the sample, unlike Chinese district names in other sources. No building shadows, walking graph or crossing accessibility. |
| [ea732fb5: 臺北市公園基本資料](https://data.taipei/dataset/detail?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6) | Parks Office; irregular; catalog 2026-08-26. | [Parks JSON API](https://parks.gov.taipei/parks/api/): 200/full, 813 entries. Name, district, location, longitude/latitude, managing unit, construction year, village, opening times, facilities and transport text. | Actual API names differ from catalog: `pm_LandPublicArea`, `pm_opening_stime`, `pm_opening_etime` rather than `pm_area`, `pm_opening_s/e`. Coordinate reference not explicitly declared by API. No per-record observation timestamp, park boundary or measured shade coverage. |

**Inference:** the tree/sidewalk combination supports an inventory or field-survey prioritization
workflow. It does not establish measured shade, an empty planting space, a safe planting decision,
or a causal cooling benefit. A demonstrator must label any shade estimate as modeled and disclose
its missing canopy/building inputs.

### Bins and complaints: four shared dataset pages

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [121355: 臺北市行人專用清潔箱](https://data.gov.tw/dataset/121355) | Environmental Protection Department; irregular; catalog 2026-09-30. | [Main CSV](https://data.taipei/api/dataset/a835f3ba-7f50-4b0d-91a6-9df128632d1c/resource/267d550f-c6ec-46e0-b8af-fd5a464eb098/download): 200/full, 681 rows; [130-location CSV](https://data.taipei/api/dataset/a835f3ba-7f50-4b0d-91a6-9df128632d1c/resource/2030d728-9597-437d-81a4-cf2a44c7f114/download): 206, complete 5,396-byte file, 130 rows. Both Big5. District, address, longitude, latitude, note; all coordinates nonblank. | Main file has 680 unique coordinate pairs; supplementary file has 120. Some supplementary notes describe multiple places (e.g. `3處`, `11處`). **811 rows does not prove 811 individual bins.** No unique bin ID, collection frequency, overflow, usage or installation date. CRS not explicitly stated in metadata; degree-valued coordinates need confirmation. Main notices prohibit household waste. |
| [63f31c7e: 臺北捷運各站分時進出量統計](https://data.taipei/dataset/detail?id=63f31c7e-7fc3-418b-bd82-b95158755b4d) | Metro Taipei; monthly; catalog/file 2026-09-15; 2017-01 through 2026-08. Shared by bins, Neihu traffic and open topic. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=eb481f58-1238-4cff-8caa-fa7bb20cb4f4): 200/full, 116 monthly URL-index rows. Latest points to [202608 CSV](https://tcgmetro.blob.core.windows.net/stationod/%E8%87%BA%E5%8C%97%E6%8D%B7%E9%81%8B%E6%AF%8F%E6%97%A5%E5%88%86%E6%99%82%E5%90%84%E7%AB%99OD%E6%B5%81%E9%87%8F%E7%B5%B1%E8%A8%88%E8%B3%87%E6%96%99_202608.csv). Both catalog HTTP URL and HTTPS upgrade returned 206/sample. Actual schema: 日期, 時段, 進站, 出站, 人次; first observed day 2026-08-01, hour `00`. | Index rows are not ridership records. Latest large monthly file was sampled only; full date coverage/completeness not audited. OD means origin/destination, with people counts per pair; correct aggregation required. Station names include line-prefix variants such as `G大坪林`, `O景安`; station normalization needed. Gate traffic is a demand proxy, not observed sidewalk footfall or bin demand. |
| [cb423c17: 臺北市陳情系統類別資料](https://data.taipei/dataset/detail?id=cb423c17-88eb-4231-a725-f1b93247d1bf) | Research, Development and Evaluation Commission; monthly; catalog 2026-10-08; advertised coverage 2016-11 through 2026-09. Shared by bins and rats. | Latest `11509` resource [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=b57a0fa8-9507-438b-b2e1-676829a72aff): 200/full, 42,674 rows and unique case IDs. Exactly eight columns: ID, main/subcategory, receiving agency/section, received/delivered/closed dates. No public narrative/address/XY fields. Observed received dates span 2026-07-21 to 2026-10-05 despite September filename. | Monthly resource label does not restrict every case's received date to that month. No subcategory literally containing 鼠 or 病媒 was found in this resource. Broad categories include disease prevention and street cleaning; those do not isolate rats. Reporting bias and lifecycle dates matter. Cannot geocode cases or equate counts with rat prevalence. Event-only complaints are a separate restricted source, not this file. |
| [48aa5bca: 臺北市公車站牌位置圖](https://data.taipei/dataset/detail?id=48aa5bca-2a4f-4fb7-a658-43cba51d5d56) | Public Transportation Office; irregular; file **2021-04-11**, catalog **2022-08-29**. Shared by bins and bus networks. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=dfd68d8e-d3b9-44df-b614-8850c103239f): 200/full, 90,888-byte ZIP containing SHP/SHX/DBF/CPG; DBF reports 3,407 records. Catalog declares TWD97. BSM_BUSSTO station ID, BSM_CHINES name. | ZIP has **no .prj**; do not infer CRS from missing sidecar alone—use publisher declaration and verify. DBF date aligns with old file. Record count is header read, not full geometry validation. Cannot assume old stop IDs/locations join current ETA. A current stop source and join audit are needed. |

**Inference:** bins have a comparatively accessible basic location inventory. Comparing nearest
listed locations is plausible; optimizing placement/collection still needs actual pedestrian
movement, waste volume, bin capacity and service constraints. MRT traffic may weight exploration,
but must not be relabeled as street footfall.

### Rats: three additional dataset pages

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [af1e6e42: 臺北市污水下水道管線](https://data.taipei/dataset/detail?id=af1e6e42-5ffc-4be0-983f-51c03d5d1b17) | Sewerage Systems Office; annual; file/catalog 2026-08-27. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=88157465-4794-41a2-a409-6180b3952f6b): 200/full, 77,603 rows. City/code, pipe ID, upstream/downstream manhole IDs, length, pipe-bottom elevations, completion date. | **No geometry/XY** in this CSV. Cannot map pipes without matching sewerage manhole locations; rainwater manholes are a different network and an unverified join. `NULL` completion dates and zero elevations seen. Length/elevation units not specified in observed metadata. No rat observations. |
| [3e62c860: 臺北市水利處雨水下水道人孔資料](https://data.taipei/dataset/detail?id=3e62c860-0753-4c79-8fe1-bcb3e0243534) | Hydraulic Engineering Office; irregular; file 2026-06-29, coverage ends 2025-06-09. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=dcaebd40-45e1-48f6-9d2e-00e1c0283f8a): 200/full, 19,443 rows. Map sheet, manhole ID, X/Y, catchment, district/village, road, type/status, depth/dimensions/elevations explicitly meters. | Coordinates look projected, but CRS not explicitly declared by observed page; require authority confirmation before overlays. IDs contain apostrophe wrapping requiring normalization. Rainwater, not sewage. Static infrastructure proximity alone cannot establish rat habitat or risk. |
| [9431f450: 臺北市食品業者登錄數](https://data.taipei/dataset/detail?id=9431f450-57d6-4c23-aca6-0ff50de49f0d) | Health Department; irregular; file 2025-06-03, catalog 2026-07-16. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=2227c204-5f9f-4b20-8c6d-c6048eab6475): 206, complete **80-byte Big5 CSV**. One record: administrative area 臺北市, count 94,828, content 全部. | **Organizer labels this “分區”, but actual data is one citywide total.** No restaurant points, district totals or dated period column. Unsuitable for local food-business density or spatial rat predictors. |

**Inference:** public complaint categories plus infrastructure are not a validated rat-training
set. A predictive risk score would need independent, spatially resolved outcome observations,
reporting-effort controls and validation. The food count and sewer pipe CSV do not supply the
spatial inputs their organizer labels might suggest.

### Neihu traffic and buses: five additional dataset pages

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [47cb9090: 臺北市車輛偵測器(VD)靜態資料](https://data.taipei/dataset/detail?id=47cb9090-e1c9-4b1d-b299-b11c375c5ee2) | Traffic Engineering Office; irregular catalog, 2025-09-09. Pointer CSV says daily. | [VD.xml](https://tcgbusfs.blob.core.windows.net/blobtisv/VD.xml): 206/sample; XML UpdateTime **2026-10-13T00:00:00+08:00**, UpdateInterval 60, authority TPE, LinkVersion 25.12.1. VDID, link/direction/lane information, PositionLon/Lat, road metadata. [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=153b5377-bf34-4ad3-a715-704545d3eb9d) is a 312-byte pointer CSV, not readings. | Static equipment/source inventory, not speeds or flows. Need matching dynamic feed and stable VDID/time semantics. Catalog update frequency, pointer and payload interval differ; do not conflate them. XML sampled, not full detector/Neihu coverage audit. |
| [166031: 縣市即時路況(VD)](https://data.gov.tw/dataset/166031) | Catalog names 地政司; irregular; last metadata 2024-09-11. | Page contains **下架說明** and lists schema but **no current downloadable resource**. References TDX and `https://adsapi.stois.nchc.tw/docs.json`; no active measurement response verified from this entry. | Treat this organizer link as **not established usable**. No observed support for organizer's “every five minutes” promise. Replacement source, access requirements, interval, historical retention and lane/vehicle aggregation must be verified separately. |
| [efad90af: 臺北市公車路線軌跡](https://data.taipei/dataset/detail?id=efad90af-4bbe-4c6a-ac60-06f3e52d8a97) | Public Transportation Office; catalog 2025-11-26; pointer CSV says daily. | [TstBusShape.json](https://tcgbusfs.blob.core.windows.net/blobbus/TstBusShape.json): 206/sample. Pointer [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=f3246e89-3579-470b-8034-085576bead32) leads to [GetBusShape.gz](https://tcgbusfs.blob.core.windows.net/blobbus/GetBusShape.gz): full GZIP parsed, 1,010 geometry records. **Later T05 readback:** the shape payload is a root JSON array, correcting this brief's earlier `BusInfo` wrapper description; its continuity with earlier bytes was not established. RouteID, SubRouteID, UniRouteId, WKT line, GoBack, utime; WGS84 declared. Actual utime 2023-06-14 through 2026-09-23. | Shape is geometry, not passenger demand, scheduled service or vehicle trace. No verified count of distinct operating routes; separate directions/subroutes create records. Per-record timestamps vary. Source spelling `UniRouteId` differs from description `UniRouteID`. |
| [f11a5af0: 臺北市預估到站時間(公車)](https://data.taipei/dataset/detail?id=f11a5af0-7b37-48ef-98cc-f6f102ed43c6) | Public Transportation Office; catalog 2025-12-18. Pointer says annually, while live payload is current. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=2749b84d-a09c-4c03-a7ff-710e7ebf209c) is a 601-byte pointer CSV. [GetEstimateTime.gz](https://tcgbusfs.blob.core.windows.net/blobbus/GetEstimateTime.gz): complete 167,679-byte GZIP parsed, 29,402 entries; EssentialInfo UpdateTime **2026/10/13 17:12:20**, WGS84. RouteID, StopID, EstimateTime seconds, GoBack. | Negative ETA sentinels: -1 not departed, -2 traffic control/no stop, -3 last bus passed, -4 no service today. Observed counts 1,617 / 138 / 3,104 / 1,309 respectively. Do not average sentinels as durations. GoBack is also categorical. One snapshot proves live access, not cadence, prediction accuracy, headway history or ridership. |
| [90dd063e: 臺北市聯營公共汽車客運業務](https://data.taipei/dataset/detail?id=90dd063e-2aca-49aa-a7fb-73130610313c) | Department of Budget, Accounting and Statistics; annual; catalog 2026-03-30; 1968–2025. | [Statistics CSV export](https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=5700&kind=21&type=0&funid=a05023701&cycle=4&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1): 200/full. Actual periods 57年–114年. Citywide route count, vehicle-km, service counts, passenger trips, revenue, accessible vehicles; units in column headers. | **Annual citywide totals**, not route/stop/hour ridership. Useful for context, not deciding a route deletion or bus reallocation. No driver shifts, labor constraints, crowding, transfer penalties or route costs. |

**Inference:** public data can support current ETA display and route geometry exploration.
It cannot support a defensible network redesign without route/stop passenger demand, schedules,
capacity and operating constraints. Neihu congestion analysis needs an observed dynamic detector
feed and history; static metadata plus MRT OD does not measure road congestion or demonstrate
that a transport intervention caused a change.

### Building resilience and open-topic weather: six additional dataset pages

| Publisher source | Publisher / date / coverage | Observed resource and fields | Limitations and useful interpretation |
| --- | --- | --- | --- |
| [ec40e067: 臺北市土壤液化潛勢圖](https://data.taipei/dataset/detail?id=ec40e067-930f-4058-b7dc-71399d5f3147) | Public Works Department; irregular; catalog 2025-06-17; declared 2016-09-10–2018-03-23. | [WGS84 GeoJSON](https://soil.taipei/Taipei2019/Main/pages/TPLiquid_84.GeoJSON): 206/sample; CRS84, MultiPolygon, `class` categorical string. [TWD97 alternative](https://soil.taipei/Taipei2019/Main/pages/TPLiquid_97.GeoJSON) linked, not separately sampled. | Numeric class-to-risk legend and map scale not established in this audit. No new survey date inferred from 2025 catalog date. Ground susceptibility is not a building structural-safety assessment. Need source legend, scale and official interpretation before scoring. |
| [a6394e3f: 臺北市各里人口數按年齡分](https://data.taipei/dataset/detail?id=a6394e3f-3514-4542-87bd-de4310a40db3) | Department of Civil Affairs; monthly; file/catalog 2026-10-05. | Latest [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=c8f5b53d-ef3d-4321-ae8e-58cd2a5ee73c): 200/full, Big5, 63,315 rows. Actual ROC year/month 112/1–115/9 (2023-01–2026-09); area code/name, sex, total, each age 0–99, 100+. Older 2021/2022 files linked separately, not sampled. | **Includes city and district totals as well as villages**, and total/male/female rows. Filter level/sex before summing to avoid double/triple counting. Registered population is not daytime occupancy or exact household/building vulnerability. Village polygons needed for map joins. |
| [7889e8a0: 臺北市現有營造建築物棟數](https://data.taipei/dataset/detail?id=7889e8a0-a71e-44e0-95c7-2213a7db1474) | Department of Budget, Accounting and Statistics; annual; catalog 2026-02-26; 1976–2025. | [Statistics CSV export](https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=6500&kind=21&type=0&funid=a05019201&cycle=4&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1): 200/full. Actual periods 65年–114年; citywide building counts by floor bands and age below/above 30 years; unit buildings (棟). | **No building addresses, footprints, construction dates or structural assessments.** Cannot join citywide age totals to village-age population and label particular homes unsafe. Suitable for citywide context only. |
| [7a800e92: 臺北市政府消防局消防通道清冊](https://data.taipei/dataset/detail?id=7a800e92-eb22-461f-b29d-8def2127a1bc) | Fire Department; irregular; file **2024-08-01**, catalog 2025-12-09. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=351307e4-ffda-4660-ac72-1c4ef3808c38): 200/full, 185 entries. ID, district code, village, listed street/place, criteria, difficult-rescue area, responsible fire unit/contact. | No geometry, coordinate or individual building safety. Geocoding needs street-range interpretation and verification. Catalog change does not prove the 2024 list is freshly surveyed. Institutional phone fields are not required in a public demo. |
| [6f03a0b8: 臺北市水利處雨量站即時資料](https://data.taipei/dataset/detail?id=6f03a0b8-7b98-4eea-8bb9-ba6bfcdc2b8b) | Hydraulic Engineering Office; catalog 2026-04-24; declared real-time 10-minute/1-minute update. | Publisher page embeds public Rain/Get API configuration; read through that supplied configuration: 200 JSON, count 42. Schema `stationNo`, `stationName`, `recTime`, `rain`; description says **current daily accumulated rainfall**, not instantaneous intensity. Endpoint base: `https://wic.gov.taipei/OpenData/API/Rain/Get`; obtain published parameters from publisher rather than copying them into Git. | No station XY in this response. Units/timezone not explicitly established by sampled metadata. **Station 025 永建國小 has recTime `206104101520`**. Under the YYYYMMDDHHmm format used by the other records this denotes 2061, inconsistent with retrieval; the root cause is unconfirmed. Other station timestamps parse as 2026-10-13 16:50–17:10. Must flag or exclude invalid/future records and assess freshness per station. One snapshot does not establish reliable warning performance. |
| [b3648c5d: 臺北市水利處雨水下水道水位監測站](https://data.taipei/dataset/detail?id=b3648c5d-15c8-416a-a603-fda7a9ac1b0d) | Hydraulic Engineering Office; irregular; file 2025-09-12, catalog 2026-09-07; coverage through 2026-09-07 declared. | [Download CSV/asset](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=586e5233-aa60-4680-8ac1-cbb9ef7f7fde): 200/full, 233 rows. Facility ID, station name, district, longitude, latitude. WGS84 explicitly declared. | **Station locations only; no water-level value, timestamp or warning threshold.** This file cannot power an actual flooding alert without a separately verified measurement feed and threshold authority. Do not equate catalog coverage end with latest measurement. |

### Cross-dataset validation still required

**Inference — organizer-starter scope:** within the organizer's listed sources, observed access
supports investigating bounded MRT OD analysis, listed-bin accessibility or tree/sidewalk surveys.
This is not an ordering of the expanded candidates or an owner topic selection; see the
[current comparison](#synthesis-and-recommended-order) and [queue](#next-investigation-queue).
The most consequential unresolved joins are current bus StopID vs 2021 SHP IDs, sewage
pipes vs sewage manhole geometry, village population vs village boundaries, and tree positions vs
sidewalk polygons after EPSG:3826 reprojection. Distance must be calculated in an appropriate
projected CRS, not directly in longitude/latitude degrees.

**Open question:** before committing to a candidate, audit the full selected time slice for
missing/duplicate records, coordinate extent, ID join rate and date semantics. Obtain publisher
field documentation for units, risk-class legend and current bus-stop mappings. Keep measured
quantities separate from proxies: MRT riders are not street pedestrians; complaints are not
prevalence; tree positions are not shade; equipment locations are not readings; citywide building
age is not individual structural risk. No inaccessible source is silently replaced with simulated
observations.

## Research verification and limits

**Evidence — 2026-10-13:** independent readback reproduced the food CSV's single citywide row,
the tree-hole counts (2,259 rows / 1,308 IDs / 1,758 unique objects), the 116-row MRT index and
latest-month CSV header/first-day records via a 4,096-byte range, and the stale recovered VD XML.
A second rain read again returned 42 stations and the anomalous station 025 timestamp, now
`206104101530`; its changed suffix does not resolve the inconsistent apparent year.

All **71 unique Markdown HTTP links** were checked with bounded curl HEAD requests: 67 returned
200. The four exceptions were the two old food-platform URLs (certificate mismatch), the new
food-platform path (empty HEAD response; earlier GET returned a maintenance page), and the
supplementary national night-market catalog on data.nat.gov.tw (502; indexed metadata only).
These exceptions are documented in the platform table rather than silently marked usable.
HEAD checks do not replace the resource GET/schema checks above. No placeholder resource URLs
remain. `git diff --check` passed. Documentation-only work requires no application test suite.

**Open question:** complete-month MRT validation, operational ground truth, current bus-stop
joins, source-unit clarification and any authenticated TDX access remain outside the verified
results. This research establishes data readiness, not the validity of a predictive model or the
impact of a municipal intervention.

## Taiwan open-data discovery provenance

### Twinkle provenance and role in this project

**Evidence — official service pages re-read2026-10-13:** the
[provider's Taiwan source inventory](https://hub.twinkleai.tw/zh-TW/data/country/tw) distinguishes
central-government catalog material, government websites not necessarily indexed centrally,
community sources, and provider-derived content. Its source/coverage counts are provider claims,
not independently enumerated facts in this project.

| Source class | What is established / example | Project handling |
| --- | --- | --- |
| Government original | Tree data128274 has direct publisher CSV/JSON/XML; government datasets also exist outside data.gov.tw | Use MCP for discovery, then pin the exact original resource/version for analysis |
| Government material collected/normalized by Twinkle | Local catalogs, procurement and tourism sources are listed by the provider; the MCP may supply a cached/normalized copy | Verify what was transformed, the observation period, update delay and coverage; provider processing dates are not source observation dates |
| Community content | Provider lists Taiwan.md and community-maintained event information | Label the actual publisher; do not describe it as government data or assume government terms |
| Provider-derived content | Provider identifies its IVOD speech-to-text output as AI transcription, not an official record | Distinguish source video from derived transcript and inspect the specific license; no derivative transcript was used in our eight solution analyses |

The [license page](https://hub.twinkleai.tw/zh-TW/licenses) describes passing through source terms;
this is a provider statement, not a blanket license for every payload. The exact dataset/resource
and rights-holder terms control the dependency. The
[Skills page](https://hub.twinkleai.tw/zh-TW/skills) still says its old packs are withdrawn while
being rewritten, with MCP unaffected. Twinkle was used for bounded discovery and structured-row reads; provider processing remains distinct from original-publisher evidence. Source facts, transformations and solution conclusions
must remain separately attributable.
