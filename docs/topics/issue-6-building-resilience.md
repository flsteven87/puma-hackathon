# Issue 6 — Old-building seismic resilience

| Field | Value |
| --- | --- |
| Official prompt | [Issue 6](https://puma.taipei/hackathon#issue-6) 「危老耐震如何查，風險評級怎麼找」 |
| Template | [Topic document standard](../research.md#topic-document-standard) v1 |
| Pain recorded | 2026-10-14 11:51 Taipei, live official page and public citizen-voice feed |
| Evidence cutoff | 2026-10-15 |
| Workflows | Current question: whether evidence improves one municipal investigation-selection decision (§4). A real, aggregate permit/organisation reconciliation now tests a preparatory step; no selection gain is established. Initial-assessment eligibility and post-assessment tracking remain separate fictional references. Public-renewal review B is deferred. Status: [canonical readiness record](../research.md#problem-fit-and-separate-readiness-of-the-expanded-candidates) |
| Reading mirror | [老屋韌性研究報告](issue-6-building-resilience.html) |
| Open owner decisions | Research and a bounded real-data explanation are authorised; production implementation and final entry selection are not. A historical practitioner comparison is deferred beyond hackathon delivery. No dashboard is presumed; external requests and publication require confirmation |

Research-only findings, evidence retrieved 2026-10-13 through 2026-10-15. Local fictional-data prototypes are documented in §4. No production application, external contact, payment or case-data request was performed. **Evidence** means inspected original material; **Inference** is analysis; **Hypothesis** identifies untested practitioner value. Product selection remains an **Owner decision**.

Scope: private residential communities in Taipei; mandatory nonresidential inspections and public-school retrofit programs are separate workflows and are not assessed here.

Method, event facts and cross-topic comparison live in the [research master](../research.md).

## 1. Official prompt and citizen pain

**Evidence — official prompt, verbatim, re-read 2026-10-14 13:59 Taipei:**

> 台北面臨「人老＋屋老」的雙老困境。50 年以上老屋在 2025 年突破 20%，2035 年將破 50%，2045 年超過 65%，代表多數房屋是在 921 地震修正耐震法規之前興建。我們要如何整合屋齡、建築結構、高齡人口、土壤液化潛勢與狹小巷弄消防搶救困難圖資，建立「危老耐震風險加權評級模型」，讓市府科學化排出老屋健檢與公辦都更的優先順序？

**Interpretation:** residents are the affected population; the city is the explicitly named
decision user; inspection and public-renewal priorities are the requested decisions. A weighted
model is the proposed method, whose usefulness must be tested against existing practice.
The age forecasts remain organizer assertions. The working research scope is municipal
decisions A/B, not a selected product or an assumption that existing officials lack a method.

**Evidence — citizen voices observed, 2026-10-14 public feed sample (paraphrased):** of 76 visible
recent voices, two concern old buildings. One, under 市政, comes from a Shilin owner of a
four-storey building about 60 years old. The upper floors report unstable foundations, but the
ground and first floors are rented out by owners who do not live there, and the unanimous-consent
requirement of the 危老 route blocks reconstruction. The other, under 城市修繕 from Neihu, asks the
city to coordinate old-housing renewal as a project manager that tracks progress. A third,
two-word voice simply asks for 老宅都更. **Limitations:** a four-per-topic rolling sample; the
statutory consent rule and the households' situations are unverified here.

**Inference, bounded to this sample:** these voices raise consent and coordination concerns.
They do not establish their prevalence, prove that either building had a professional assessment,
or rule out a municipal inspection-allocation problem. Use them to test whether resource
decisions connect to an executable next action; do not replace the official municipal objective
with a resident tool on this evidence alone. T06-D remains a secondary, unvalidated hypothesis.

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
| City needs inspection/public-renewal priorities (explicit official objective) | City: inspection allocation and public-renewal review, kept separate | See hypothesis A | See hypothesis A |

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

**Evidence — unreachable or legally restricted owners, read 2026-10-15:** statutes re-read on the
national law database (curl, HTMLParser); CMO 危老問答集合併版 (PDF created 2025-11-06, modified
2025-11-17, 273 pp., SHA-256 `3a21746c1790b34f3a33071f66ee732c87fd4c74b816146acdd5effe21450bca`)
parsed with `pdftotext -layout`; Taipei Land Administration dataset
[臺北市未辦繼承登記土地建物列冊管理辦理標售](https://data.gov.tw/dataset/134972) (metadata
2026-10-13; CSV SHA-256 `fc14f9b639166c4d3c0b53547fd5add6a43f1b073c2ab5e42d581e178c29b094`) parsed in full.

| Owner situation | 危老 reconstruction (all owners, D0070249 §5) | Urban renewal consent count |
| --- | --- | --- |
| Heirs have not registered the inheritance | Must finish inheritance registration first, then all owners consent (FAQ E-31, 2019-07-30 MOI letter) | Counted by the share of consenting co-heirs (D0070008 §39) |
| Unregistered over one year, listed by the land office | No exclusion found in the act | Excluded from the count (§24(3), applied by §37) |
| Court-restricted: seizure, provisional attachment or disposition, bankruptcy | Not prohibited, but the FAQ advises removing the restriction first because the building permit must follow within 180 days (E-33) | Excluded (§24(4)) |
| Estate administrator appointed | Depends on the court's appointment scope (E-32) | — |
| Owner living abroad | Can authorise a relative with the consular-affairs form (E-28) | — |
| Unregistered ancestral trust or deity association | No exclusion found in the act | Excluded (§24(5)–(6)) |

Under 土地法 §73-1, an inheritance unregistered for a year is listed for 15 years before the
National Property Administration auctions it. Taipei's dataset reports 2,607 buildings and 19,052
land parcels under that listing at the latest year-end; new building listings rose from 206 (2021
cohort) to 459 (2025 cohort). **Limitations:** citywide and not limited to old or reconstruction
sites; the dataset counts building entries with partial shares; registered heirs who disagree,
and inheritances under one year old, are not counted. Leads, unverified: press accounts from New
Taipei and Beitou describe elderly owners unwilling to move and owners adding demands at
re-signing; neither is a Taipei prevalence measure.

**Inference:** in 危老, a single unreachable or legally stuck owner works as a veto, and the
remedies are slow (heirs' cooperation, or 15 years to auction). Urban renewal removes most of
these owners from the count, which is part of why the city's FAQ Q30 lets a building assessed
below the minimum grade switch toward prompt designation. How many stalled Taipei 危老 cases
involve such owners is unknown; neither the promoter register nor any agency report records why
an integration failed.

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

**Inference:** a promoter service already covers explanation and coordination. This snapshot
contains many more initial-assessment filings than plan filings, but cannot measure progression,
duration, abandonment or a cause of delay. The address match does not establish that an address
never advanced. Comparing dated versions or cohorts is needed before describing a conversion
bottleneck. Promoter incentives, dissent, economics and trust remain untested explanations.

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

### Municipal allocation baseline — bounded refresh (2026-10-14)

**Question and predeclared exits:** before designing a priority tool, identify one programme's
owner, unit, capacity, eligibility, consent gate and actual selection evidence. Support further
research if a published decision exposes an unresolved, action-relevant information gap. Reject
another ranking if the existing process already answers the same task. If only rules and totals
are available, record selection performance as unresolved; do not manufacture a deficient queue.

**Evidence — M01, 2026 Taipei proactive initial assessment:** city announcement
府都建字第11561076341號, 2026-04-17, gazette No. 71 p. 36 (PDF p. 37), names a planned 50 cases, not observed completion or remaining capacity.
Eligibility is quick-screen F>60 or age ≥30, with ≥6 storeys and a management organization,
or city recognition. CMO's use section receives applications. Attached rules points 5–6 specify
eligibility, city solicitation, consent, then assignment to a qualified institution. The announcement
does not show invitations, accepted/refused candidates, a backlog or an oversubscription rule.
Point 14's discretionary ordering sits in the weak-storey subsidy provisions; it is not evidence
of an inspection-queue ranking. The separate NT$13.5m weak-storey budget is not an assessment slot.

**Evidence — M02, Taipei 2025 reported activity:** UDD 114年度主管決算, total explanation p. 31
(PDF p. 35), reports 166 approvals for the 危老 structural-assessment subsidy; ordinary weak-storey
design-fee applications numbered 4 and the 0403 scheme separately numbered 5. Design-fee
applications are not completed retrofits. Proactive assessments appear as two lines of 50 cases /
NT$0.8m, labelled retained and current budget; without case IDs or clarification do not sum them
into 100 unique buildings, compare them as a cohort, or calculate conversion. This corrects the
previous blanket statement that no Taipei annual counts were found. Multi-year results and
assessment-grade distributions remain missing. The report's p. 2 attributes lower related grant
receipts partly to application-dependent spending; this is an agency explanation, not a causal study.

**Evidence — M03, historical implementation example:** CMO's 2016-11-03 announcement describes
prioritizing the Chongqing and Heping road axes within high-liquefaction-potential areas and the
27 rescue-road network for professional reconnaissance of ≥30-year buildings. It allows requests
from tenants and applicants without majority consent. The stated 1,500 buildings is a year-end
target, not observed completion. Reconnaissance is not statutory initial assessment. This shows
an existing place-first outreach approach, not its current force or superior performance.

**Evidence — M04, public-renewal selection:** the live city law system lists the 2020-04-09
revision. Articles 4–7 define eligible areas, written suitability assessment and city selection;
UDD reviews applications from other agencies, stating reasons if unnecessary or reporting to
the city for selection. Article 5 requires ten report contents, including willingness,
public-interest, relocation and finance; it does not specify ten weighted factors. These are
project-level gates, not an all-city building risk ranking or evidence of review difficulty.

**Evidence — M05, contrary evidence on weighting:** the 2018 citywide renewal-area designation
plan pp. 7–9 explicitly uses weighted overlay scoring to identify potential/need areas before
boundary adjustment. It is a different decision from selecting a public-renewal project or
assessing structural safety. Reject the blanket claim that Taipei never uses weighted planning;
purpose-specific criteria and validation remain necessary.

**Evidence — M06/M07, bounded advancement case:** URO's 2023-12-29 account of 虎林街60巷 reports
a 2023-07 application, 83.93% doorplate-household willingness for entry, technical financial and
floor-exchange estimates, and 91.07% willingness before simulated allocation. A 2025-05-27
follow-up reports city agreement to the Taipei housing/renewal centre as implementer and
investor-procurement preparation. Neither is completed reconstruction or a comparison with
rejected candidates. Doorplate-household intent is this programme's measure, not statutory
owner/area consent. The live URO FAQ (updated 2025-10-28, reviewed 2026-09-11) confirms the
staged 75/90/90 process. This is community-initiated 7599, not every public-led selection route;
these percentages cannot be applied to A or the Shilin voice.

**Inference:** the immediate A unit can be an eligible programme candidate, rather than every
old building in Taipei. The new evidence establishes an announced programme scale and a documented
process; it does not establish excess demand, wasted slots or missing software. A public-only
all-city ranking remains unsupported. Resident consent, access and available professionals are
separate execution gates, not safety weights. A candidate lacking evidence stays unresolved;
missingness alone does not give it unlimited priority over every other unknown candidate.

**Outcome of this desk check:** rules and planned programme scale are supported; selection quality and
incremental tool value remain unresolved. No original case-level 2026 inspection selection
record was located in the inspected announcement, annexes or 2025 accounts. The B case supports
reconstructing a stage gate, not comparative priority, software benefit or the performance of
city-initiated suitability review.

### Assessment and retrofit activity — separate cohorts and unresolved bottlenecks

**Owner decision — 2026-10-15:** continue deepening issue 6. Beyond the 2026-10-24 demonstration,
the owner cares whether the work actually solves the problem. This research therefore judges each
candidate by whether it moves a building toward lower risk, not only by whether it ranks buildings.

**Question and predeclared exits (2026-10-15 checkpoint):** test the premise behind hypothesis A,
that the 50 proactive slots are oversubscribed so that ordering matters. Supported if the agency
reports more willing candidates than slots; refuted if slots go unfilled for lack of consenting
candidates; unresolved if only filled totals exist. Then trace what follows an assessment.

**Evidence — M08, the city solicits before it assigns:** CMO's annex 5 flow for the proactive
programme (PDF created 2023-02-08) runs: contract the assessment institutions → the executing
agency consults a management organisation or owners → consent → the agency assigns an institution
→ the agency sends the report to the building. The 2022 UDD account (M09) adds that consent forms
are collected until 50 are in hand before cases are dispatched. The agency conducts solicitation before assignment. The 2026-04-17 announcement also accepts citizen applications (rechecked in §4); this is not an agency-only intake route. A concerns a bounded investigation-selection decision; programme and operator still need confirmation.

**Evidence — M09, UDD final accounts 2022–2025, 辦理情形 rows (reporting-period order):**

| ROC year (AD) | Proactive initial assessment | Owner-initiated 危老 assessment subsidy | Weak-storey retrofit | Source page |
| --- | --- | --- | --- | --- |
| 111 (2022) | 50 planned; contract let, consents being collected, none completed; executed in 112 | 194 initial + 1 detailed | 4 applications, 2 at design, no works paid | 總說明 p. 33 / PDF p. 36 |
| 112 (2023) | 50 completed (111 retained) and 50 completed (112 budget), NT$0.8m each | 82 approvals | 3 design-fee cases; 1 works completion paid (NT$4.5m) | 總說明 pp. 31–32 / PDF p. 35 |
| 113 (2024) | 50 completed (113 retained) and 50 (labelled 114 budget) | 200 approvals | 3 design-fee cases | 總說明 p. 32 / PDF p. 36 |
| 114 (2025) | Two lines of 50 completed (labelled 114 retained and 114 budget); see M02 | 166 approvals | 4 design-fee cases; 403 scheme 5 design-fee cases | 總說明 p. 31 / PDF p. 35 |

The accounts' revenue notes repeat across 2023–2025 that the assessment and retrofit subsidies
"須民眾主動申請" and fell short of budget; 2025 realised 48.98% of a NT$252m allocation. The 2025
account (總說明 p. 5 / PDF p. 9) gives the agency's own explanation for low retrofit completion:
an application needs only more than half of owners, but the subsidy is capped at 80% of works,
households pay about 20%, works are generally expensive, and residents doubt what they will
actually pay. By contrast, sea-sand demolition subsidies ran out of budget and carried cases to the
next year (2023–2025 rows). **Limitations:** labels overlap across years, so do not sum the 50-case
lines into unique buildings (M02 rule). No invitation, refusal, waitlist, candidate-pool or grade
record appears. Design-fee applications are not completed retrofits.

**Evidence — M10, UDD reports to the city council, 2026-04 and 2026-07:** of the 2024-04-03
earthquake's 2,140 damage reports, 2 buildings received red and 26 yellow tags. By 2026-02-28 one
red was demolished, one red and 18 yellows repaired, 3 were in weak-storey retrofit, and 8 central
weak-storey applications were all in NCREE design review (2026-04 report, printed pp. 77–78 /
PDF pp. 79–80). The city used prompt designation for tagged buildings: 41 areas, about 5.72 ha,
lowering the filing threshold to 50% (same pages). The 575 dangerous-building project received 7
applications and assisted 5 communities by 2026-05-31; one signed an investor (2026-07 report,
PDF p. 76). Promoter filings reached 3,635 by 2026-05-31; three residents' signatures bring a
resident architect, ten bring a community briefing (PDF p. 53). **Limitations:** agency-reported
progress; no case list or independent check.

**Inference — what the funnel shows:**
1. The proactive programme's reported limit is its 50-case budget, and it fills every year.
   The premise is half-supported: slots fill, but demand beyond 50 and refusals are unobserved.
2. Scale: about 50 proactive and 80–200 owner-initiated assessments a year, against 201,642
   buildings aged ≥30 years (I). A better order changes which 50 buildings get a free assessment.
3. Downstream activity warrants investigation, not a measured cohort-conversion claim: single-digit retrofit design applications a year
   in 2022–2025 and one paid works completion in 2023. The agency itself names household cost and
   uncertainty about the actual burden. Risk falls only where an assessment leads to retrofit or
   reconstruction; 危老 reconstruction (P29: 1,179 applications, 530 starts) is the larger exit and
   depends on site economics.
4. Who no channel reaches: the proactive rule needs ≥6 storeys and a management organisation, so
   walk-ups and the 5,489 listed ≥6-storey buildings without one (pain tree) enter only by city
   discretion. They overlap the 人老 stock the official prompt names.

**Inference — each exit stalls at a different gate (route map; mirrored as a diagram in the HTML
report's section 03):**

| Exit after assessment | Consent gate | Observed volume | Where it stalls | Evidence type |
| --- | --- | --- | --- | --- |
| Weak-storey retrofit | More than half of owners to apply (agency, 2025 account) | 3–5 design applications a year; one paid works completion 2022–2025 | Household share, high cost, doubt about actual burden | Agency statement (M09) |
| 危老 reconstruction | All owners (D0070249 §5); applications close 2027-05-31 | Taipei 1,179 applications, 1,047 approvals to 2025-11-30; 530 starts by end-2024 (P29) | Unanimity and site economics for the cases that do not proceed | Statute and one citizen voice; prevalence unknown |
| Urban renewal | More than 1/2 after discretionary prompt designation; 3/4 or 4/5 otherwise (D0070008); 575 project >50% to apply, ≥75% to proceed | 575 project: 7 applications, 5 assisted, 1 investor signed by 2026-05-31 (M10) | Low intake; finance and investor procurement | Volume observed; cause unverified |

Consent is therefore one gate among several, not the single blocker: retrofit needs only a
majority yet stalls on money, while reconstruction's unanimity rule binds a subset whose size is
unknown. Selection quality upstream is unverified rather than shown to be adequate.

**Consequence:** an assessment-priority model alone cannot establish physical risk reduction.
Selection quality and downstream implementation require separate validation; the observed counts
do not identify the dominant bottleneck. Follow-up needs an executable referral or action, but a
funded construction outcome is not a prerequisite for testing an upstream information improvement. Whether that doubt is magnitude
(work costs too much) or uncertainty (the share is unknown until design) is unresolved; §7 owns it.

### Household burden check — magnitude, uncertainty or access? (2026-10-15)

**Question and predeclared exits (§7, 2026-10-15):** is the retrofit burden mainly magnitude or
uncertainty? Supported (uncertainty) if public rules and cases yield a pre-design self-pay range
narrow enough to change a meeting's decision; refuted if the share is knowable only after design
or public cases cannot bound it.

**Evidence — subsidy rules:** P02 point 8 (CMO-hosted MOI rule, effective 2022-10-17, PDF p. 3,
SHA-256 `51b99be0ff2c5e0c0dc3e7e9ff98af92cca580170faa6450111de41d57dc1414`): plans A and B pay at
most 45% of total retrofit cost, capped at NT$3m (plan A, layer under 500 m², rising NT$0.1m per
50 m² to NT$4.5m) or NT$4.5m (plan B). The rate rises to 85%, cap NT$4.5m, when the initial danger
score exceeds 45, a detailed assessment requires retrofit or rebuild, **or the executing agency
recognises a potential seismic hazard**. The subsidy covers design, supervision, works and permit
certification. The 403 scheme caps each building at NT$15m (≥6 storeys), NT$7.5m (<6) or NT$2m
(detached), at 85% (M10). Plan annexes 6–7 (CMO, 2023-02-08) are engineering criteria and carry no
cost figures. NCREE's programme pages state rules only; no case costs are published there.

**Evidence — observed cases (originals read 2026-10-15):**

| Case | Scale | Cost and subsidy | Household share | Source and limits |
| --- | --- | --- | --- | --- |
| New Taipei, Xinzhuang (first completion) | 5-storey apartment | Works NT$5.29m; 85% rate, NT$4.5m cap | NT$0.8m in total, under NT$0.1m each; PTS reports NT$80k each | [NTPC release 2024-01-22](https://www.ntpc.gov.tw/ch/home.jsp?id=e8ca970cde5c00e1&dataserno=d5b95e3934fe202cf8d8ded22dce0ca3); [PTS 2024-07-02](https://news.pts.org.tw/article/703006). Agency account; household count not stated |
| Hualien, 華爾街 (red tag) | 12 storeys, 246 households | Works about NT$70m+ (county official) | Not stated; if one building at the NT$15m cap, about NT$224k each (inference) | [CTEE 2026-01-10](https://www.ctee.com.tw/news/20260110700569-431401). Building count, other aid and final cost unverified |
| Hualien, 蓮花 (yellow tag) | 4 × 17 storeys, 128 households | Maximum NT$15m per building at 85% | Not stated | [Newtalk 2026-05-08](https://newtalk.tw/news/view/2026-05-08/1033993), citing MOI/NCREE |
| New Taipei, U-shaped complex | Several buildings, plan A | 85% approved, NT$4.5m cap per building | — ; works cannot start | [Moneyweekly 2026-01-30](https://www.moneyweekly.com.tw/_Article?AID=209034). Attributed account; site unnamed |

The New Taipei complex could not start because a few owners in a structurally critical building
refused to take part; dropping it would leave the retrofit unbalanced. The account states no
public power compels them; only owners' litigation can. In Hualien, the county attributes slower
agreement partly to retrofit reducing some units' floor area. Taipei context: PTS quotes 14
weak-storey approvals in Taipei in 2024, while the 2024 account (M09) pays design fees for 3; these
are different stages.

**Computed — self-pay for a 10-household walk-up under the rules (scenario, NT$10k):**

| Total cost | R > 45 (85%, cap 450) | R 30–45, plan B (45%, cap 450) | R 30–45, plan A < 500 m² (45%, cap 300) |
| --- | --- | --- | --- |
| 300 | 4.5 each | 16.5 | 16.5 |
| 530 | 8.0 | 29.1 | 29.1 |
| 700 | 25.0 | 38.5 | 40.0 |
| 900 | 45.0 | 49.5 | 60.0 |

The cost band 300–900 is an assumption anchored on one observed 5.29m case, not a Taipei
distribution. The cap binds at 529 (85%), 667 (plan A) and 1,000 (plan B).

**Inference — result against the exits:** unresolved, and the question splits three ways.
1. **Magnitude depends on the regime.** Below the cap at 85%, households pay a fixed 15% of cost;
   the one observed walk-up paid about NT$80k each. At 45% the same building costs three to four
   times more per household. Large buildings exceed the cap, and costs per household rise.
2. **Uncertainty is half removable.** The subsidy side is fully knowable before design: the rate
   follows the initial score, the cap follows the plan and the household count is known. The cost
   side is not: no public cost-per-area reference exists, and above the cap every extra unit of
   cost falls on households. NCREE reviews every design and therefore holds the cost data.
3. **Access is a separate gate.** Applying needs a majority, but works sit in specific units,
   often the ground floor; one refusing owner can stop a funded project, and floor-area loss
   hits those units hardest.

**Consequence for the endgame:** a pre-design estimator is defensible for the subsidy side and for
the near-threshold decision (R just under 45 changes the household share several-fold; a detailed
assessment or the agency's own hazard recognition can lift the rate to 85%). It cannot by itself
remove cost uncertainty without a cost reference, and it cannot resolve access refusals.
The agency's discretion to recognise hazard and raise the rate is a city lever the stall board
should expose. No Taipei cost distribution, household allocation rule or refusal count is public.
The access gate is analysed with the other owner situations in the next subsection.

### Owner reachability and standing — the second stall (2026-10-15)

**Owner decision — 2026-10-15:** demonstration direction (a). The city stall board leads, the
resident route and self-pay estimate is its entry, and physical risk is an admission threshold
rather than the ranking. Alongside the information gap, the owner asks to cover buildings that
stall because owners cannot be reached or are in other situations. Reversible; planning and a
`/reverse-thinking` audit follow.

**Question and predeclared exits:** are unreachable or legally constrained owners a stall
distinct from dissent, with their own levers? Supported if public rules give each situation a
route-specific remedy that a community or the city can trigger; refuted if persuasion is the only
remedy; prevalence stays unresolved unless a count exists.

**Evidence — three ways an owner drops out (originals read 2026-10-15; M11–M14):**

| Kind | Situation | What the rules say | Source |
| --- | --- | --- | --- |
| Cannot be found | Anyone holding the public transcript | The class-2 transcript, open to anyone, shows the first character of the name and part of the ID; the registered address is shown unless the owner asked to mask it after the street. The class-3 transcript (full name and address) goes only to the owner or a party with a legal duty to notify or a change of rights | 土地登記規則 §24-1; transcript rules points 2–4 (M12) |
| | 危老 organiser | Not a listed party. CMO's answer: elect a manager or form a committee and register it; its chair may then obtain all owners' class-3 transcripts. Until then a consent form may carry the masked name | FAQ B-14 (p. B53), D-09 (M11) |
| | Urban-renewal organiser | Owners holding more than 1/10 by headcount or by land and floor area, an approved preparatory group or the (prospective) implementer may obtain class-3 transcripts for the unit and adjoining land; Taipei URO confirms the range first. The authority itself notifies all owners when a summary or plan is approved | Transcript rules point 4(6); URO procedure 2021-01-22 (M12); D0070008 §22, §32 |
| Cannot sign validly | Unregistered inheritance, court restriction, estate administrator, abroad | See the §2 table | §2 |
| | Owner under guardianship | A guardian's disposal of the ward's real property is void without court permission (民法 §1101 ¶2(1), applied to adults by §1113). No source read settles whether consenting to 危老 reconstruction counts as disposal | M14 |
| Present but blocks the works | Refuses entry to a unit that holds the retrofit | Main beams, columns and load-bearing walls are common parts (公寓大廈管理條例 §7). Residents may not refuse entry the committee needs to repair common parts (§6 ¶1(3)); after notice the authority may fine NT$3,000–15,000 repeatedly (§47(3)), or the committee may sue (§6 ¶3) | M13 |

Whether a weak-storey retrofit that permanently takes a unit's floor area counts as "repairing
common parts" under §6 is untested here. The New Taipei account in the burden check reports that
no compulsion was available; it is an attributed account, not a legal finding.

**Evidence — the management organisation decides how a missing owner counts:**
- Retrofit subsidy: with a registered organisation the chair applies with an owners'-meeting
  resolution; without one, more than half of owners by headcount and share must sign (headcount
  ignored above two-thirds of shares) (P02 points 10–11).
- A re-convened owners' meeting opens with three owners and one-fifth of owners and shares, and
  decides by a majority of those present. The minutes are served on every owner; the resolution
  stands unless written objections from more than half of all owners and shares arrive within
  seven days (§32).
- A committee may apply for a seismic assessment with meeting minutes instead of individual
  consent forms (FAQ D-10, D-12, pp. D88–D90). Proactive initial assessment admits only buildings
  with a management organisation, unless the city uses discretion (P02 point 5).
- Forming one: owners elect a convener; failing that, the city may designate a temporary convener
  (§25) or a manager (§29). §29-1 (2022) lets the city order buildings deemed at risk to form an
  organisation within a deadline, with guidance as a city duty and fines of NT$40k–200k per unit
  (§49-1). MOI's criteria (announced 2023-06-06) cover only buildings of 11 storeys or more that
  failed a fire or building-safety inspection, and mention no seismic assessment; the statute lets
  a city publicly expand them (§29-1 ¶2). A bounded search found no Taipei expansion; absence is
  unverified.
- Taipei pays a promoter NT$20k–90k, by household count, for guiding a pre-2003 building of six
  or more storeys to register an organisation (FAQ H-06, p. H205), drawing on the list parsed in §2.
- 危老 still needs every owner (D0070249 §5). An organisation helps find owners; it does not lower
  that threshold.

**Evidence — counts:** only the inheritance listing (2,607 building entries; §2) is public. No
public source counts untraceable owners, owners under guardianship or refusals of entry. CMO's
monthly report template for 危老 work stations records briefings, hours, visitors and consultation
content, not why an integration failed (station report form, SHA-256
`97a0df652de51d4cb50849802647995f19bd9aa4eb9467cb33d1ab91a1822740`). A search for studies of the
causes returned financial and general integration studies, no count of owner situations (lead,
unverified).

**Inference — result against the exits:** supported for mechanisms, unresolved for prevalence.
1. "Cannot be found" depends mostly on the route and the building's organisation. Renewal
   organisers and registered committees can lawfully obtain full addresses; a 危老 organiser in a
   building without one cannot. Under signatures, a missing owner works as a "no"; under a §32
   resolution, the owner counts only by objecting.
2. Each situation has a matching lever and an owner of that lever: findability → organisation and
   transcript route (city convener designation, promoter fee, §29-1 expansion); standing → heir
   registration, guardianship court step, estate administrator, consular authorisation, or a move
   to prompt-designated renewal where listed and restricted owners leave the count; access → §6
   notice and §47 fine (scope untested), a design that avoids the unit, or the hazard-recognition
   rate lift.
3. A stall board can record each assessed building's stall as information, money, findability,
   standing or access, and show the lever and who holds it. It cannot find people: identities stay
   with the organisation and the land office under personal-data rules. The city-facing board
   should carry stall categories and counts, never owner names.
4. The endgame's crack narrows but stays open. If most stalls are unaffordable cost, digital help
   is marginal; where they are findability or standing, the city already holds a lever. The inspected public sources do not establish which dominates; internal records may already exist. Whether a new board adds value remains a hypothesis.

**Consequence for the demonstration:** use fictional buildings with stall categories and levers;
show no real owner, address or count beyond the published inheritance figure. The management
organisation is a recurring gate: it admits a building to proactive assessment, decides whether a
missing owner blocks a retrofit application and opens the transcript route for 危老.

### Selection practice, bottleneck and professional anchors

**Owner decision — 2026-10-14:** deepen the old-building resilience research and gather more complete professional and practical detail. Research-only; no request, contact, account, submission or implementation.

**Method:** four bounded tracks ran in parallel on 2026-10-14: current Taipei selection rules and baseline (P sources), professional assessment and retrofit practice (E), old-building stock data (I), and prioritization precedents elsewhere (X). Each track read original government, professional-body, research or operator documents. HTML pages were read with the web tool or curl; PDFs were read with `pdftotext -layout`; open datasets were downloaded and parsed with `uv run python -I`. The topic owner then re-read the decisive values in the downloaded originals: the MOI proactive-assessment criteria (P02 point 5), the 2019–2021 national target/achievement table (P05), the 2026 national demand for an explicit ranking rubric (P30), Taipei 危老 counts (P29), the initial-assessment grade table (E01/E02 附表五), the single-building R variation (E10), the Taichung screen-positive share (E21), the tax-office district totals (I, 115年度 CSV sums), the MOI unit table for Da'an, and the national initial-assessment and weak-story counts (X24). Search snippets and news remain labelled leads. Raw downloads, owner names and addresses stay outside Git. Table rows below come from the track records; a row is evidence only for the sections stated in its ledger entry.

**Earlier source scope — qualified by the municipal baseline above:** the inspected sources did not establish a current cross-programme seismic ranking. Do not infer that Taipei has no selection criteria or internal prioritization. Proactive initial assessment is a national eligibility filter (quick-screen F>60 or age ≥30, plus a management organization and ≥6 storeys, or the city's discretion), followed by owner consent (P02). P02 point 14 allows ordering in the weak-storey subsidy context; it does not establish how initial-assessment candidates are ranked. The routine assessment subsidy is applicant-initiated and reconstruction-oriented (P15–P17). Public-led renewal origination depends on land thresholds, public-land assets, a suitability report and owner willingness (P19, P24). Hazard-linked renewal channels (575, disaster-prevention renewal) start only after owners prove hazard, using ID<0.35, sea-sand listing or tags, and then clear 50/75/90% willingness thresholds (P20–P23). Taipei's closest published hazard ordering is the 2016–2017 老屋健檢 plan. Its first-phase priority classes were suspected soft storey or frontage on the 27 disaster-relief roads, prior 921/331 tags, fault or liquefaction zones, and public housing (P01). A 2014 Taipei study selected pilot villages from simulated Shanchiao-fault damage, and judged parcel-level hazard data too coarse (P25).

**Evidence — explicit official demand:** the Executive Yuan's 2026-03-16 approval of 老宅延壽機能復新計畫 (114–116) requires the MOI to "建立受理申請審查之明確評比基準及核定優先順序", and asks professional teams to select priority areas, inventory potential cases and overlay maps (P30). It targets 4–6-storey apartments aged ≥30 years, the stock that the proactive ≥6-storey rule omits. This is national demand for a transparent ranking rubric, not a Taipei commitment or allocation.

**Evidence — historical national uptake, not a Taipei cohort funnel:** nationally, 2019 to 2021-09 delivered 4,147 of 19,555 planned subsidized initial assessments, 2 of 500 detailed assessments and 21 of 725 weak-storey retrofits (P05). Cumulative national initial assessments reached 17,277 by December 2024, Taipei 5,754 of them, while weak-storey subsidy applications totalled 194 (X24). In 2016 MOI linked low uptake to owners' fear that results would be disclosed and promised confidentiality (X02, X04). A detailed assessment costs about NT$0.15–1.8 million per building under the Taipei-published 2026 fee schedules, depending on floor area and fee family (E14). Weak-storey retrofit subsidy is normally ≤45%, so owners pay the rest (E08). Tokyo's route-side program reached 98.6% diagnosis but left about 2,000 buildings unretrofitted, citing cost and co-owner consensus (X13). **Inference:** these records justify investigating downstream feasibility alongside selection. They do not identify the current Taipei bottleneck or establish that a new ranking improves outcomes.

**Evidence — professional decision anchors:** one initial-assessment danger score R drives several decisions at different cut points: 危老 grades at 30/45 (E01–E03), weak-storey subsidy at R>30 and an increased rate at R>45 (E08), PSERCB/public-building action at 60 (E12, E17), and the renewal danger criterion ID<0.35 (E07). R combines 40 qualitative points with 60 points from a first-floor-only capacity calculation, without coring. PSERCB guidance excludes hidden defects, high chloride and additions (E12). In one official teaching case, two engineering assumptions moved a building's R from 10.8 to 42.3 (E10). **Inference:** a model should target a named decision threshold. Near-threshold buildings are uncertain even after a formal initial assessment.

**Evidence — observable predictors and their limits:** official 2016 Meinong and 2024 Hualien investigations repeatedly name soft or open commercial ground storeys, arcade (騎樓) street-house columns, corner or irregular plans, single-section column splices and inadequate hooks (E25, E26). The official pre-assessment quick screen reviews drawings for tall or open ground floors, arcades or mezzanines, wall-poor ground floors, design-load and system-factor issues, incomplete frames and single spans (E10). Taichung referred 40.9% of 5,443 screened licences for initial assessment (E21). Splices, hook detailing and illegal wall removal cannot be observed in public data. Policy cutoffs use different date bases (permit applied, obtained, designed, use permit issued), and the assessment's detailing item treats post-May-1997 design as modern (E10, E17, E33). A collapsed 2016 building completed in 2000 shows that completion year is a weak proxy (E26).

**Evidence — site hazard and known conditions:** site amplification already enters R through the Taipei basin microzone or ground class (E12). Liquefaction maps are planning-grade, and the agency stated that past collapses were caused by poor structural systems, not liquefaction (E29–E31). Sea-sand status is a separately listed regime with its own sampling and demolition criteria (E22, E24). **Inference:** treat liquefaction as a geotechnical-check flag and sea-sand listing as a known-condition flag or exclusion, not as additive seismic weights.

**Evidence — aggregate stock data:** the inspected open population-wide age tables are district level; D03 (§5, retrieved 2026-10-15) separately supplies historical individual permit attributes, without establishing a current stock census. The Taipei Revenue Service's 臺北市房屋概況 115年度 reports 220,254 buildings, 201,642 (91.5%) aged ≥30 years; the district rows reconcile to DBAS's citywide building series (I). MOI's real-estate platform publishes residential units by district and quarter, as separate age, structure and floor tables, with no cross-tabulation: Taipei had 921,951 units at 115Q2, 74.5% older than 30 years (I). Building counts and unit counts rank districts differently. Authoritative contemporary building attributes may come from restricted or per-record sources; this is not an exclusive-source claim after the D03 archive discovery. Sources include house-tax records (稅捐稽徵法 §33 ¶2 permits supply to agencies and researchers for statistics or research without names), land-registry building records (per-record to anyone; bulk under local data-supply fee rules), and the NLSC 3D model. The 3D model has floors and height but no age; Taipei files are referred to the city's Department of Information Technology (I). NCDR built a 500 m grid from the tax register, available to agencies and academia on written request (I).

**Evidence — inspected precedents:** the reviewed Los Angeles, San Francisco, Japan and New Zealand programmes do not establish a transferable continuous-score safety verdict. This is a bounded source comparison, not a claim about every jurisdiction or a rejection of transparent policy scoring. Los Angeles, San Francisco, Japan and New Zealand use an observable inclusion rule, coarse deadline tiers and a binding engineer evaluation (X05–X19). Missing information triggers evaluation rather than implying safety: New Zealand deems an unassessed building earthquake-prone after 12 months; Los Angeles non-ductile concrete applies "whether identified or not"; Japan targets 耐震不明 buildings (X07, X13, X19). In FEMA's only benchmark against engineering evaluation, Level 1 rapid screening missed 1 of 31 unacceptable buildings but referred 11 of 18 acceptable ones (X20, computed). Tokyo measures route priority as road-section reachability and named 50 priority sections where few retrofits restore the most network function (X13). Japan and San Francisco express elderly or vulnerable occupancy as facility-use classes; social-vulnerability index rankings are sensitive to construction choices (X09, X12, X28, X29).

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

### Post-assessment stall board — supporting hypothesis

**Current disposition:** the fictional board at `prototype/stall-board/board.html` explores
post-assessment coordination. It is not the core product or evidence of improved selection.
Its distinct user task is to record a stalled assessed case, a responsible person and a next action.
Practitioner need and benefit over existing internal tracking are unverified. The narrative reset
below governs the primary research direction; this supporting workflow remains available for inspection.

| Critical pain (evidence) | What digital help can reach | Board part | What it cannot do |
| --- | --- | --- | --- |
| Why a building is approached is not visible; walk-ups and buildings without an organisation fall outside proactive assessment (M08, P02, §2 list) | Show eligibility gates, missing evidence and the reason each candidate was approached or deferred; flag buildings without an organisation | Intake (hypothesis A) | Prove a building safe, or rank unknowns by missingness |
| Residents doubt what they will pay (M09) | Route gates and the subsidy-side self-pay before design; flag scores near 45 and the hazard-recognition rate lift | Resident entry and money check (T06-D, burden check) | Give one cost figure before a cost reference exists |
| The works cost more than households can pay (burden check) | Show the subsidy regime, the cap and which lever applies (85% recognition, 403 scheme, phased option) | Money stall | Pay for the works |
| Owners cannot be found (owner reachability) | Track organisation status and the transcript route; prompt convener designation or promoter guidance | Findability stall | Locate people or hold names and addresses |
| Owners cannot sign validly (§2, M14) | Name the situation and its remedy: heir registration help, guardianship court step, consular authorisation, or a switch to prompt-designated renewal | Standing stall | Decide legal capacity |
| An owner refuses entry (burden check, M13) | Record the refusal and the available step: a §6 request or a design that avoids the unit | Access stall | Compel entry; §6 scope untested |
| No one coordinates or follows up (Neihu voice) | Every building has an owner of its next action and a date; overdue items surface | The board itself | Replace promoters, architects or the city's authority |
| No one records why integration fails (M10, station form) | Stall categories counted across buildings show where a city lever matters | Board summary and stall-distribution map | Establish prevalence before real use |

**Success, predeclared:** compared with the city's current tracking, more assessed-risky buildings
reach a funded next step (retrofit design approval, 危老 or renewal filing) within a fixed period,
and every stalled building carries a recorded reason and lever owner. An earlier, testable
proxy: with fictional cases, a city officer names the stall and the next lever faster and with
fewer omissions than with current documents.

**Rejection:** the city already tracks stalls and levers per building; most stalls are
unaffordable cost with no lever; or the city cannot lawfully hold stall reasons per building.
Then shrink to the resident estimator or stop.

**Data:** a working board runs on the city's own records (assessment results, subsidy
applications, promoter filings, organisation registrations); the scoped public lists do not provide the complete case evidence needed (§5). The demonstration uses fictional buildings and labelled public aggregates (district
stock, the inheritance listing, programme counts). A cost reference would improve the estimator, but baseline records, case evidence and practitioner need are also missing for a claim of decision value.

**Prototype / reading outline (updated 2026-10-15):** `prototype/stall-board/index.html`
presents the research method, official pain, existing practice, data limits, real aggregate
reconciliation and allocation hypothesis. S01–S04 remains a disclosed fictional rule explanation,
not evidence of allocation benefit. `board.html`
retains the separate A04 post-assessment workflow. No city officer has tested either; no real
selection or improved outcome is established.

### Research direction — explain and test one investigation decision

**Owner decision — 2026-10-15:** rebuild the argument from the research method, original pain and
supplied data, with one author. The requested HTML revision applies this reset. Neither an intake
checklist nor a post-assessment board is a predetermined product endpoint.

**Method:** evidenced pain → existing practice → bounded decision → predeclared success/rejection
→ necessary evidence → comparison → presentation. The organizer proposes a weighted model, but
that method must earn its place by improving a named decision. The campaign organizer is not a
verified government commissioning client. Two resident voices establish possible consent and
coordination constraints, not their prevalence or a municipal software requirement.

**Endgame (hypothesis):** in one municipal old-building investigation round, staff can explain which
candidates merit professional attention, what evidence supports that choice and what to check next.
The loop is candidate pool → traceable evidence → comparison with current practice → human-reviewed
action → professional findings → checked selection performance. Investigation selection, formal
assessment eligibility, public-renewal feasibility and post-assessment tracking are distinct decisions.

**Invariants:** every recommendation carries a source, unit/date and next action; area aggregates
never become individual diagnoses; assistance need stays separate from execution feasibility;
unknown is neither safe nor automatically highest priority; simulation never counts as observed gain.

**What the evidence changes:** the four supplied files are not a joinable building inventory.
The B01–B06 identity audit and scoped CMO lists improve knowledge of coverage but still do not define
the old-building candidate universe (§5). Published programme rules demonstrate existing practice;
annual counts do not reveal comparative selection quality. Different assessment and retrofit totals
cannot establish a cohort funnel or identify the dominant bottleneck. Downstream barriers therefore
remain a separate research question, not proof that selection is either adequate or inadequate.

**Post-event effectiveness comparison, not a hackathon delivery gate, not yet run:** choose one programme and one lawful de-identified
round with selected and unselected candidates, decision-time evidence, actual capacity and reasons.
First establish whether staff encounter an information problem. Agree with a qualified practitioner
which omissions and unsupported referrals matter before looking at proposed results. Compare current
practice with the added evidence on that same pool and information date; measure review-worthy
omissions, unsupported choices and preparation effort. Inspect whether plausible data uncertainty
changes the suggested action. Changed ordering alone is not success; unchanged choices with reduced
work may be useful if error does not increase. No numerical threshold is claimed before the operator
and task are identified.

**Rejection:** stop or narrow the candidate if current practice already answers the question,
additional evidence improves neither relevant errors nor effort, the join cannot support the decision,
or the binding constraint is authority/funding/capacity rather than information. Data access and
practitioner review are unresolved; a missing baseline means unresolved, not a successful simulation.

**Presentation:** explain method → original pain → existing practice → reproducible public-data
finding → declared action scenario → demonstration acceptance and deferred effectiveness validation.
The current real-data comparison below is an input-preparation subtask, not a replacement for
municipal selection or an unvalidated dashboard. Public-renewal review B and tracking remain separate.

### Real-data example — reconcile records before an investigation enquiry

**Owner decision — 2026-10-15:** deeply discover real sources and available connectors before
declaring inputs simulated. Complete the hackathon explanation using obtainable evidence;
interviews, agency replies and a historical decision cohort are post-event validation, not prerequisites.
Simulation needs a specific missing decision input and evidenced feasible acquisition/replacement.
The research request authorises calculations and report updates, not a production application.

**Hypothesis / bounded user outcome:** a municipal officer preparing an old-building enquiry can
see which public records need identity or management-scope confirmation before choosing whom to
approach. This supports one prerequisite of the official inspection-allocation question. It does
not solve allocation, consent, funding or physical safety, and does not establish an information
bottleneck. The existing baseline includes CMO's own lists, application service and internal records;
whether this comparison adds anything to that baseline remains unknown.

**Exploratory comparison completed, not a preregistered efficacy test:** use the same 5,489 permit
records in CMO's 2026-07-17 list throughout. Compare them with the original 2026-10-05 organisation
registration CSV, using exact use-permit ID intersection (D01/D02, §5). This is the named reference
rule, not the city's observed selection rule. Unit: permit records, never automatically buildings,
households or available assessment slots. The list is scoped to permits through ROC92, at least
six storeys and two households, titled **未成立管委會**; it is neither the complete old-stock pool
nor a verified age-30-plus or residential-only population.

**Evidence / finding:** the CSV has 1,017,840 parsed rows, but 1,008,127 are entirely blank. Its
9,713 nonempty rows contain 9,657 distinct permit IDs, including 53 repeated-ID groups. Exact
intersection finds **3** IDs. All three pairs have different representative addresses; one has
different district labels. Each registration name ends in **管理負責人**. This is a literal label
observation, not a legal determination of current management. The other 5,486 IDs have no matching
registration row in this snapshot; that does not prove they have no organisation.

**Inference / explainable action:** flag the three permit collisions for identity, management
scope, organisation-type and currentness verification. Do not transfer the registration state to
the listed building, automatically remove it from assistance, or call the sources contradictory.
A permit can cover multiple buildings/doorplates; a committee and a management representative
are different organisation forms. File refresh dates do not timestamp an organisation's formation.
The CSV's 核發日期 is not established as a registration-change date and is not used as one.

**Declared policy scenario, not observed agency action:** source list → permit collision →
verify shared building/management scope → if current organisation evidence is confirmed, retain it
for the officer's general-condition review; if scopes differ, keep the records separate; if still
unknown, request the missing scope evidence. Age, floors, recognition and consent still need their
own records. No scenario resolution is assigned to an identifiable real building, and no synthetic
F, resident count or risk score is needed. The age branch of P02 can be considered without F;
the pre-2003 list alone does not prove age ≥30.

**Prospective demonstration acceptance / rejection:** reproduce the two source hashes, 5,489-row
PDF sequence, nonempty CSV count and three intersections; retain all three as unresolved and all
5,486 nonmatches as unknown; show source dates, distinct units and the conditional next action.
Reject a claimed building-status finding if identity/scope cannot be linked. Reject a priority or
efficiency claim without the actual comparison. Source changes require a new audit, not silently
reusing these numbers. These are delivery checks; professional effectiveness, effort saved and
civic outcomes remain unverified. No owner/agency contact has occurred.

**Decision-to-data feasibility (audited 2026-10-15):**

| Essential or earlier-demo input | Decision it changes | Real source / availability and effort basis | Disposition and replacement path |
| --- | --- | --- | --- |
| Scoped candidate ID, source date, district, representative address, floors | Which records refer to the enquiry target? | D02 original 80-page PDF fully parsed, 5,489 numbered rows; simple local extraction; raw addresses private. Not a unique building key or current survey | **Use real** for aggregate reconciliation; verify identity before individual action. No invented all-city population |
| Organisation record/type/scope | Is organisation evidence available, or must it be checked? | D01 original CSV fully parsed; permit/name/address, no current-scope or change-history field. Free download; 53 repeated permit IDs | **Use real** as positive registration evidence only; missing or collided scope → **narrow scope**, not synthetic yes/no. Current proof would come from authorised committee/representative documents or agency lookup; not acquired |
| Age/completion and original structure/floors | Can age/floor branch support further review? | D03 historic raw XML is downloadable and parsed, including pre-2001 records. Dates/conflicts/current survival unresolved; D04 supplies historic government-license provenance, not byte equivalence. D02 permit year ≤92 is not age ≥30 | **Fetch/derive real** historical attributes for corroboration, not current eligibility. Missing/conflicted dates → unknown. Present-day identity/completion evidence must replace stale archive fields before case action |
| Professional F (S04), professional findings | Does the alternative F>60 branch apply? | No public candidate-level F source established. CMO FAQ D-19 restricts disclosure of assessment results; it is not evidence that F and initial-assessment R are identical. Acquisition needs the holder's lawful permission and a professional record; no case-access agreement exists | **Narrow scope:** unnecessary for this real reconciliation or an adequately evidenced age branch. S04 remains fictional rule teaching; not justified simulation of a real building or an established feasible data feed |
| Confirmed absence of an organisation (S01), current organisation (S02/S04), unknown (S03) | What evidence must be checked before a service route? | D01/D02 offer dated observations, not complete current yes/no truth. S01–S04 have no audited corresponding real records | Keep all four explicitly fictional. Do not grandfather their acquisition feasibility. The selected real example uses observation/unknown states instead of simulated organisation status |
| Agency recognition, willingness/consent, slot availability, officer decision reasons | Can a building proceed or receive a slot? | P02 provides the rule/sequence; public annual counts do not provide case evidence or live capacity. Holder is agency/community; no lawful case access or effort basis verified | **Narrow scope** to pre-enquiry evidence preparation; no synthetic recognition, consent, capacity or observed baseline. Historical cohort and practitioner study deferred |
| Building occupants, soil-site condition, rescue access | Who is exposed and what professional checks matter? | Existing starter audits are area geometry/statistics or textual lists, not joined case observations | Not essential to this example; **narrow scope**, retain source-grain restrictions. No synthetic attributes attached to real buildings |

**Result:** one complete pain → real-data finding → conditional action explanation is reproducible
without simulated inputs. It establishes a preparatory data-check result only. The stronger claim
that a new tool improves investigation selection remains an unresolved hypothesis. The next research
check is whether a bounded age-branch subset can link dated completion/floors and management scope
without treating a permit as a building; no UI expansion is needed to answer that check.

### Eligibility example — supporting teaching exercise

**Purpose and limit:** S01–S04 are four fictional records demonstrating that a published eligibility
rule needs case evidence. The age-only reveal is not a municipal baseline. Correct branches prove
rule consistency only; they do not compare priority between eligible candidates or discover a real
allocation insight. The example remains optional reference material, not the reason to choose this
research direction.

**Evidence — original-source recheck, 2026-10-15:** current
[CMO service page](https://cmo.gov.taipei/cp.aspx?n=53F406AE758E3270) (updated/reviewed 2026-09-17),
[operative points 5–6](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/0f3092a5-106a-4ce1-87b5-aefc03e9900f.pdf)
(revision order 2022-10-17), and
[flow attachment 5](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/d1c62bc5-5690-431c-93eb-51f85515dc16.pdf)
were read as HTML/PDF text. General eligibility is `(F > 60 OR age >= 30) AND management organisation
AND storeys >= 6`, with a separate executing-agency recognition route. F is the professional quick
screen, not initial-assessment R. The sequence is institutional contracting → solicitation → consent
→ institution assignment → report delivery. No consent percentage is inferred from other schemes.
The [2026-04-17 announcement, gazette pp. 36/39](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=fb8cb02f-8402-4261-88e0-f000f5c6e8fe)
also receives citizen applications; solicitation does not establish an agency-only intake route.
M01 digest remains `15d080547443febea9676183120723df0f7e093128ce2aeeaaaf0fcda6aef63c`;
P02 PDF digest is `51b99be0ff2c5e0c0dc3e7e9ff98af92cca580170faa6450111de41d57dc1414`.
These checks establish the documented process, not a city's actual choice difficulty or a particular
building's formal eligibility. The demo states general-condition evidence only and requires review.

**Evidence — full starter CSV recheck, 2026-10-15:** the
[DBAS original export](https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=6500&kind=21&type=0&funid=a05019201&cycle=4&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1)
still has 50 yearly rows, 13 columns, ROC65–114; SHA-256 matches §5's `8f471e3d2ab5ef6e17d5b7408a74b370458cc12870de57e0dced2fc086c2bde4`.
It supplies citywide totals and marginal age/floor bands, not building IDs, addresses, structure,
organisation or assessment evidence. The 5–6-storey band cannot isolate 6-storey buildings; there
is no age-by-floor cross-tab. Method: full download and CSV parse, original catalog checked.
**Inference:** even the number of generally eligible candidates cannot be derived from this source;
combining its margins would invent a relationship. Existing quality qualifications in §5 still apply.
No new dataset suitability or redistribution claim is made for unreviewed resources.

**Simulated comparison — one fixed set, not a baseline-effectiveness test:**

| Case | Fictional records dated 2026-10-15 | With age only | With case records | Action and boundary |
| --- | --- | --- | --- | --- |
| S01 | 62 years, 4 storeys, no organisation | Unresolved | General conditions not met | Ask agency about recognition/other service; retain support need, never infer safety |
| S02 | 46 years, 7 storeys, organisation confirmed | Unresolved | General-condition evidence present | Prepare solicitation, subject to review and consent; no priority or assignment claim |
| S03 | 35 years, 6 storeys, organisation unknown | Unresolved | Organisation evidence missing | Request/check that record, retain agency-recognition route |
| S04 | 28 years, 8 storeys, organisation confirmed, professional F=64 | Unresolved | Alternative F>60 branch supports general conditions | Prepare solicitation under review, despite age below 30; not a safety rank |

The interface can hide organisation evidence without changing the other inputs: S02/S04 become
unresolved; S01's known floor condition still requires agency consideration. A boundary test uses
F=60 to verify it does not pass the strict >60 branch. This tests logic consistency, not actual
prevalence, selection benefit or safety. The age-only view is a teaching reveal, **not** the city's
current process. A real comparison must include all evidence the officer already has, use the same
cases and capacity, and judge important omissions, unsupported claims and preparation effort.
An unchanged choice with lower effort can be useful; a different choice without justification cannot.

**Result:** supported as a bounded explanation of evidence-dependent next actions; insufficient for
priority between generally eligible buildings. No real allocation is made. Practitioner need,
case access, role authority, budget/capacity and adoption remain unknown. Hypothesis: the smallest
useful tool may be an evidence-comparison record, not a new board. Reject it if the current process
already achieves the same result without the alleged burden. Public-renewal project selection
remains a separate decision, and post-assessment funding/physical improvement remain separate outcomes.

**Bounded public baseline search — 2026-10-15:** three targeted searches of CMO, UDD and council
sources, followed by the original M01 announcement, M09 2025 accounts (printed p.31 / PDF p.35),
service page and flow attachment, did not locate a round-level candidate list with contemporaneous
evidence, actions, reasons and capacity. This is a bounded search result, not proof of no internal
records. Annual totals and published procedures cannot substitute for an observed decision round.
The actual-baseline experiment remains **unresolved**; no performance comparison was run.

**Prepared acquisition scope (not sent):** request one historical round's random case IDs for both
selected and unselected candidates; decision date/rule version; age or F evidence, storeys,
organisation and agency-recognition state as known at that date; solicitation/request-evidence/
defer action and reason; and that round's service capacity. No owner names, identity numbers,
addresses, contact details or free text containing personal information are needed. Ask whether
an existing de-identified table can be reused, rather than requiring new data collection. The
purpose is to compare decision completeness and preparation effort, not evaluate named staff or
publish building safety claims. Actual contact requires action-time owner confirmation.

**Next / disposition:** retain S01–S04 as fictional rule teaching. The current delivery path is
the real reconciliation above; a historical solicitation round is deferred effectiveness validation.
No request is sent and no real-acquisition feasibility is assumed for the fictional fields.

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

**Hypothesis — A, municipal inspection allocation:** a CMO programme reviewer prepares the
next selection/solicitation round for the 2026 proactive-assessment programme. Authority for the
programme is documented (M01); the particular officer, actual selection method, available remaining
slots and user difficulty are unobserved. The unit is a verified candidate building/幢 under that
programme, not an arbitrary address or the whole city. Baseline: eligibility → solicitation →
consent → institution assignment, with the existing agency evidence and professional judgement.

**Workflow and dependencies:** authorized candidate identity, eligibility evidence, dated
structural leads, prior assessment, consent/contact state and remaining slots → separate eligible,
excluded and unresolved cases → compare the eligible cases using the existing programme rules →
reviewer records solicit/assign/request evidence/defer and its reason. Unknown eligibility requires
a bounded evidence request; it is not a high danger score or an automatic place in the queue.
Keep difficult-to-coordinate cases visible without treating consent as proof of safety. Older
residents' actual access/assistance needs inform outreach and execution support, not frame strength.

**Success and rejection:** compare the same round with current agency practice. Success means
fewer independently adjudicated important omissions or less preparation effort without worse
eligibility/unsupported-claim errors. Reject a new tool if existing records already support those
actions, if there is no contested allocation decision, or if essential evidence cannot distinguish
candidates. If most cases remain equally unknown, suspend priority ordering and test evidence
acquisition instead. No public-only real ranking or effectiveness result is supported.

**Outcome boundary:** reported activity does not prove the quality or difficulty of selection.
Test allocation gain against actual practice; separately track professional findings, funded
improvement and physical safety. A useful upstream decision is not proof of downstream success,
and downstream financing difficulty does not prove the upstream decision is already adequate.

**Validation/adoption/presentation:** first reconstruct one published selection record and its
rule version; include an eligible case, an unresolved case and an excluded case as boundary tests,
not a prevalence sample. A later authorized paired reviewer task must compare omissions, effort
and reason traceability. A disclosed fictional round can explain the interaction but cannot
validate it. CMO, qualified institutions, lawful case handling and actual slots are required;
professional availability, costs and adoption are unknown. Demonstration remains specified,
decision insufficient. Before/action/after: a fictional mixed candidate batch → apply the actual
programme gates and record unresolved evidence → attributable assignment proposal, not safer homes.

**Hypothesis — B, public-renewal review priority:** the city renewal authority prepares which
project area/case should advance to suitability/feasibility review. It is a separate project-scale
decision. Baseline is the applicable public-led-renewal rule and existing suitability/financial
review, not A's seismic screen. Professional condition, project boundary, public land/interest,
owner willingness, reinforcement alternatives, displacement, cost and execution capacity must
remain separately visible. The output is advance review / request named missing evidence / defer
with reasons, never an automatic reconstruction order. Current source detail and a published
case are recorded in this section's municipal baseline refresh.

**Success/rejection and validation:** reproduce a public case's recorded decision and missing
conditions under its own rule version, then identify whether a new comparison changes a defensible
review action. Reject direct renewal selection from an inspection flag or an unexplained overall
score. Defer a prototype if project-level evidence is absent or existing review already supplies
the same result. Before/action/after: a disclosed project proposal → compare feasibility evidence
and alternatives under the official criteria → reasoned review disposition. A later authorized
reviewer comparison measures omissions and preparation effort; no adoption, cost, completed
renewal or civic gain is observed. Demonstration specified; decision insufficient.

**Validation proposal — not executed:** freeze a professional-adjudicated case set with building IDs, dated evidence and decision purpose. Compare current process against the proposed reasoned triage, including assessed/unassessed, contradictory, recently altered, high-consequence and hard-to-coordinate cases; selection is failure-mode coverage, not representative prevalence. Measure important omissions, unsupported assertions, reviewer effort, unknown-case handling and reason traceability. Test rank/list changes under plausible evidence and weight assumptions; flag unstable cases instead of claiming precise order. No arbitrary score, success percentage, equal weights, top-N budget, sensitivity range or complete candidate census is invented. Legal safety gates must remain professional gates. Observed task benefit, stable decisions and later allocation/civic outcomes are separate acceptance stages.

**Superseded next step — 2026-10-13:** verify whether one legally reusable building/permit source supplies stable identity, location, completion/permit date, structure and floor scope for one building. Completed below; the result changes what the allocation hypotheses can claim.

### Hypothesis A revised — tiered screen-to-verification sequencer

**Hypothesis — no implementation authorized:** test a programme-specific evidence review before adopting a **tiered screen-to-verification sequencer**:

1. An observable inclusion rule, such as a pre-1999-12-31 construction permit, with an explicit "status unknown" class.
2. Apply programme eligibility and consent gates before comparing candidates. Record missing evidence with a bounded follow-up; do not rank equally unknown buildings by missingness alone.
3. A separate road-segment layer counts how many candidate buildings could block each fire-rescue segment.
4. A separate support layer uses elderly occupancy and facility type to choose outreach intensity, not hazard.
5. Versioned rules and a change log.

Success still requires a frozen professional comparison. Candidate validation data are the city's confidential initial-assessment records and damage tags, accessible only through an authorized request. A disclosed fictional or district-aggregate demonstration remains possible from open data. Decision readiness stays **insufficient**.

**Hypothesis B consequence:** public renewal is driven by land, willingness and finance thresholds. A risk ranking can at most inform the city-designated policy-area clause and outreach, not select cases.

**Open questions / unfound:**
- Taipei multi-year proactive and owner-initiated assessment counts, grade distributions and completed retrofits; M02 now resolves selected 2025 programme totals only.
- The Taipei quick-screen F-value list and actual 2026 candidate/consent/assignment records.
- Full text of the 115–118 national seismic plan.
- 575/7599 intake counts.
- Private full-retrofit costs per m².
- Taipei bulk land-registry supply rules.
- Guest-visible coverage of img2.gov.taipei.
- The current status of NCDR's grid and NCREE inventories.

**Current next step:** §7 owns the one current action. The annual-count search above is now
partly resolved by M02; multi-year results and case-level selection remain open. Information
requests still need action-time owner confirmation.

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

**Evidence added 2026-10-15 (§3 funnel, M09–M10):** Taipei's own 2025 account attributes low weak-storey completion to the household share (about 20% of works), high works cost and residents' doubt about their actual burden. Retrofit design applications stayed in single digits a year in 2022–2025. This is an agency-stated downstream pain, attached to the official municipal user, and it moves T06-B from a supporting alternative to the follow-through that A needs. It does not show whether better information would change decisions when the burden itself is unaffordable.

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

**Deferred candidate — T06-D (hypothesis, not implemented):** a resident/promoter compares
applicable routes and asks the existing service a specific next-step question. This is supporting
research, not the primary municipal-allocation target. The CMO FAQ already contains the
prompt-designation route; discovering it does not establish an information-service gap.

**Baseline/success/rejection:** compare an identical case using the FAQ/promoter explanation and
a proposed route summary. Potential success is fewer unsupported eligibility/consent claims or
less preparation effort at equal correctness, not overcoming dissent or completing renewal.
Reject if existing services answer the task adequately, the route does not apply, or finance and
consent rather than comprehension determine the action.

**Smallest validation, not run:** freeze four distinct boundary cases: unanimous consent; more
than half by the applicable owner/area tests; exactly half; and unknown ownership/assessment/site
area. The Shilin account does not establish four equal owners or shares. In a hypothetical
four-equal-owner case, two approvals fail a strict majority; it must return unresolved/no demonstrated
route rather than a promise to bypass dissent. Separately verify whether assessment itself can
be obtained under that case's consent, whether prompt designation is discretionary, and applicable
unit-size limits. Failure in one case refutes that case's path, not every possible route tool.

**Dependencies/adoption/readiness:** verified professional results, ownership/area, programme
version, lawful source use and a professional recipient are necessary. No real case record,
user comparison, professional acceptance or cost is observed. Keep demonstration unassessed and
decision insufficient. Resume only if the municipal baseline work reveals a specific unresolved
case question that existing services do not already answer. Do not use undated promoter filings
as a substitute for this task comparison.

## 5. Evidence and data audits

### Broad discovery and real-input feasibility audit (2026-10-15)

**Method / question:** search from the official inspection-allocation pain for evidence that can
support one pre-enquiry action. Inspect original content before calling a field unavailable or
simulating it. Web routes covered organisation registration, unregistered-committee lists,
professional F/results, historic permits, research exposure inventories and public GIS. Download
and parse CSV/XML in full with standard-library Python, PDF with `pdftotext -layout`; inspect the
first/last PDF pages visually. Research calculations emit aggregates only. No public-feed
collection, model inference API, account enrolment, external contact or purchase occurred.

**Source ledger — retrieved 2026-10-15:**

| ID / original source | Observed content, coverage and access | Rights, limits and decision consequence |
| --- | --- | --- |
| **D01** CMO [organisation registration catalog 132391](https://data.gov.tw/dataset/132391), [city catalog](https://data.taipei/dataset/detail?id=d665fc9b-0f60-4d53-bd43-971ae8755680), [original CSV](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=b879cc87-7f42-4911-8093-d1f055ea9c45) | Original file updated 2026-10-05, 8,195,989 bytes. Fields: permit ID, issue date, district code/name, organisation name/address. 1,017,840 parsed rows, 1,008,127 entirely blank; 9,713 nonempty/distinct rows, 9,657 distinct permit IDs, 53 repeated-ID groups, no missing field in nonempty rows; 12 districts | Original national catalog explicitly OGDL v1, free. Publication snapshot, not proof of active scope, formation date or complete coverage. Permits can have several organisations. Positive evidence can support verification; absence cannot prove no organisation |
| **D02** CMO [service page](https://cmo.gov.taipei/cp.aspx?n=023341AF71C3812D), [可輔導成立公寓大廈管理組織清冊 PDF](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/eb00caaf-7533-4e47-9871-fc2b04028d22.pdf) | 80 pages, dated 115/07/17. Title: permit year ≤92, ≥6 above-ground storeys, ≥2 households, **未成立管委會**. 5,489 contiguous numbered rows / distinct permit IDs; fields ID, district, representative address, above/below-ground floors, households; floors 6–50 | Public read established; no file-specific redistribution license established. Cite source and derived aggregate observations only; do not publish the raw/per-building list. Not a full-city stock, age-30 eligibility list, residential-only cohort or current organisation truth |
| **D03** imdataman [pinned raw XML directory](https://github.com/imdataman/taipei-house-age-map/tree/ce08b2240fe68dc5cf78dc2f4dbd71b111112026/%E4%BD%BF%E7%94%A8%E5%9F%B7%E7%85%A7), [README provenance](https://github.com/imdataman/taipei-house-age-map/blob/ce08b2240fe68dc5cf78dc2f4dbd71b111112026/README.md) | Public unauthenticated full download: 66 XML files / 230,040,887 bytes; 71,690 permit records / 71,257 IDs, 433 repeated-ID groups, 18 with conflicting extracted identity/decision fields. `51.xml` and `52.xml` byte-identical. Fields: permit, issue/completion, original construction permit, type/structure, floors/households, addresses/lots. 55,268 records have nonempty completion; 69,894 have positive integer floors | Archive author attributes raw XML to CMO catalog 128203, whose current original file starts ROC90. Raw XML entered Git 2016-12-30; pinned repo commit 2017-01-09 is custody, not source retrieval date. D04 documents historic government terms. Exact equivalence to old publisher bytes unverified; current survival/demolition untested. Do not use author's geocoded derivatives or code under assumed permission. Historical corroboration only; no present-day full inventory or safety verdict |
| **D04** GFZ [source-specific README](https://git.gfz-potsdam.de/globaldynamicexposure/datasources/-/blob/15631b0e20096c9c6d0bdc619fe47992cabafa38/Taipei_construction_permits_1950_2020/README.md), [data license](https://git.gfz-potsdam.de/globaldynamicexposure/datasources/-/blob/15631b0e20096c9c6d0bdc619fe47992cabafa38/Taipei_construction_permits_1950_2020/LICENSE), [download script](https://git.gfz-potsdam.de/globaldynamicexposure/datasources/-/blob/15631b0e20096c9c6d0bdc619fe47992cabafa38/Taipei_construction_permits_1950_2020/download.sh) | Full source text read at pinned commit 2021-10-26; identifies catalog 128203, OGDL v1 copied 2021-10-07, and historic resource ID `07b57a4e-5ac8-471b-a5cd-4cb8bb4e5c59`. Historic publisher endpoint returned HTTP500; new download endpoint with historic rid returned HTTP200 / zero bytes | Research-institution provenance supports the historic government-data license, not byte authentication of D03. GFZ's exposure project publishes no downloadable model output; source directory contains no second data inventory. No historic original release was recovered |
| **D05** GEM [Taiwan v2026.0.0](https://github.com/gem/global_exposure_model/blob/v2026.0.0/East_Asia/Taiwan/README.md), [Adm1 CSV](https://raw.githubusercontent.com/gem/global_exposure_model/v2026.0.0/East_Asia/Taiwan/summaries/Exposure_Summary_Adm1.csv), [taxonomy CSV](https://raw.githubusercontent.com/gem/global_exposure_model/v2026.0.0/East_Asia/Taiwan/summaries/Exposure_Summary_Taxonomy.csv), [license](https://github.com/gem/global_exposure_model/blob/v2026.0.0/LICENSE.txt) | Full CSV parses: 66 Adm1 rows (22 divisions ×3 occupancies), 99 taxonomy rows. Model aligns counts to 2025 using census sources; no individual permits, addresses, F, organisation or completion records in public summaries. Finer data require a request | CC BY-NC-SA4.0; modeled exposure is not observed local building eligibility. Retain as model context only, exclude from this reconciliation. No request made |
| **D06** Zhuang et al. [2024 primary paper](https://link.springer.com/article/10.1007/s44195-024-00064-8), §2.1 / data availability | Full relevant source text: authors used 1949–2019 Taipei permits, retained 60,387 entries after obsolete-address exclusions, then 29,170 after geolocation filtering. No separately released case inventory observed; source link has a malformed UUID | Article CC BY4.0 does not license all imagery or prove D03 coverage/accuracy. Corroborates historic-source existence and identity uncertainty; not professional assessment or a current inventory |
| **D07** UDD [building-statistics function manual](https://webgis.udd.gov.taipei/upis_v2/pdf/%E5%BB%BA%E7%AF%89%E7%B5%B1%E8%A8%88.pdf) | Original 3-page PDF downloaded/text read. Public interface aggregates age/floors/structure in a selected area using building-map SHP periodically obtained from CMO; buildings without permits excluded | No bulk export/field-level coverage or reuse right established. Existing-service baseline, not an inspected new old-building dataset; excludes an unsupported claim that no such municipal lookup exists |
| **D08** CMO [current assessment service](https://cmo.gov.taipei/cp.aspx?n=53F406AE758E3270), [P02 original](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/0f3092a5-106a-4ce1-87b5-aefc03e9900f.pdf), [FAQ D-19, printed D94](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/35b648d6-30d1-4a2a-96ba-8e9ca300b37b.pdf) | Re-read original PDF text. P02 §5 permits age≥30 or professional F>60, with organisation/≥6 floors, plus agency recognition. §6 requires agreement before assignment. FAQ says subsidised assessment results are not proactively published and disclosure needs applicant consent | Rules and form availability do not provide actual F, recognition, consent or current capacity. FAQ concerns assessment results; do not conflate F with R. Narrow the example instead of synthesising these absent case records |

**Content audit / dependent-claim correction:** D03 disproves a blanket inference that pre-2001
permit attributes cannot be publicly retrieved. B01–B07's actual current-original-file coverage
findings remain valid, as do transaction-selection and address≠building limits. D03 is a dated
archive, not a verified surviving stock. Nonempty fields are not valid dates or independently
accurate attributes. Filenames are not year filters; duplicate IDs need field-level comparison.
All claims about a complete contemporary old-stock universe remain unresolved.

**Reproducible real comparison and uncertainty checks:**

1. Remove only entirely blank D01 rows; do not infer one row equals one building. Preserve the
   53 repeated-ID groups, then intersect distinct permit IDs with D02. This yields 3 IDs /3 pairs;
   deduplicating D01 exact rows does not change the result (all 9,713 nonempty rows are distinct).
2. Parse all D02 numbered rows and verify sequence 1–5,489; visually check first/last pages.
   All three intersections differ in representative address, one in district; their D01 names
   end in 管理負責人. NFKC width, whitespace and city-prefix normalization does not resolve addresses.
   A separate floor-suffix/district-prefix sensitivity check also finds no exact address agreement;
   no fuzzy match, geocoder or invented building ID is used.
3. Withhold automatic building-status transfer for all three. If future verification establishes
   a shared scope, the organisation evidence can enter the P02 review; if not, keep separate.
   The 5,486 nonmatches remain unmatched observations, not confirmed absence. No eligibility,
   invitation, assessment slot or safety label is assigned.

Run from the repository root with downloads at any private location:

```sh
python3 scripts/issue6_feasibility.py \
  --organisations /path/to/organisations.csv \
  --unregistered /path/to/unregistered.pdf \
  --archive-dir /path/to/community-permits
```

`--archive-dir` is optional; the two original official files alone reproduce the current finding.
The script checks original hashes, rejects malformed/missing PDF rows and emits no names, addresses
or permit IDs. D01 SHA-256 `a6e3883a772aa0caee72b754c495a28a98116e99e6c0404879f84818bb1ed245`;
D02 `0b75c68c602dafc21858e374ac6183ca212fab28c913b19250403b3f147d7225`.
Archive sorted filename/digest-list SHA-256 from the script is
`d5bf4cfc5b8d41d8310be784dd1c810d48343df6ad83f2fbf2c1e497c7e04233`.
No simulated input is required for these calculations.

**Search-route limits and stopping reason:** current-list reconciliation has two usable original
sources and a reproduced finding; historical permits have been fully inspected with explicit
provenance limits. GEM/GFZ model routes stop at aggregate summaries or unreleased output; NCREE's
[TERA report landing page](https://www.ncree.niar.org.tw/accomplishment/technicalreports/page/12183)
describes insurance exposure, not a released Taipei candidate table (full report not inspected).
The [EGU2020 original abstract](https://meetingorganizer.copernicus.org/EGU2020/EGU2020-19670.html)
describes permit/OSM/NCDR modelling, with no raw inventory linked in the inspected abstract.
Community geospatial searches led to D03; live OSM feature downloads were not run because footprints
cannot resolve management scope or professional F for this decision. This is an unexecuted route,
not evidence of no features. Targeted Taipei professional-F searches yielded no new case-level
public source; CMO sources give rules and restricted-result boundaries, not a public F feed.
The earlier exhausted historical-selection-cohort search was not restarted.

**Connector-assisted discovery:** an open-data search found 132391 and returned its columns and
download URL; the topic author verified publisher bytes and terms rather than adopting a quality
badge or catalog row count as usability. A
臺北+耐震 search returned no hits; a broad 快篩 search returned irrelevant water datasets, so web
and original service pages remained necessary. Code-repository search found pinned README/source
paths for D03, verified with raw XML. No additional public municipal/academic inventory route was
established through account-content connectors; this does not establish absence of other data.

### Building identity audit — public chains cover new buildings, not the old-building universe

**Scope correction — 2026-10-15:** this heading describes the B01–B07 current-publisher audit,
not all publicly retrievable history. D03 below supplies a community-preserved pre-2001 permit
archive; the earlier inference that historical building attributes are available only through
restricted sources is superseded. A complete current old-building universe remains unverified.

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

**Inference — consequence for allocation:** the verified building-level chain covers the newest part of the stock: issue6's target population, buildings roughly30 years or older (use permits before1996), is outside B01/B02 by construction. Within this 2026-10-14 current-publisher audit, older-building sources included (a) transaction-derived completion year, material and floors for about one in ten address keys, biased toward traded residential units, and (b) listed problem registers such as B05. Neither defines the eligible universe, and an untraded or unlisted building remains **unknown**, not newer or safe. D03 now adds historical permit attributes, superseding the exclusive-source inference. A complete current inventory still needs authoritative identity and survival checks; possible routes include building registration, house-tax registry or the scanned permit-image system (`img2.gov.taipei`, a script-rendered app whose coverage, query rules and terms were not observable without interactive use). Access to any of them is an owner/authority question, not a data-engineering step.

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

### Source ledger — municipal baseline refresh (retrieved 2026-10-14)

| ID | Original source / period | Inspected method and scope | Limits and use |
| --- | --- | --- | --- |
| M01 | [Taipei gazette 115 No. 71](https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=fb8cb02f-8402-4261-88e0-f000f5c6e8fe), announcement 2026-04-17 府都建字11561076341 | Normal-TLS curl; full PDF text extraction, visual check of printed p. 36 / PDF p. 37; attached rules pp. 38–44 points 5, 6, 14, 16 and annex headings | SHA-256 `15d080547443febea9676183120723df0f7e093128ce2aeeaaaf0fcda6aef63c`. Capacity/eligibility/process, not selection results or remaining slots. Official announcement/rule paraphrase; no raw register republished. |
| M02 | [UDD 114年度主管決算](https://www-ws.gov.taipei/Download.ashx?icon=.pdf&n=6YO955m85bGAMTE05bm05bqm5Li7566h5rG6566XLnBkZg%3D%3D&u=LzAwMS9VcGxvYWQvMzI4L3JlbGZpbGUvMzExMTQvOTU2ODQxMS8zMTNkZWYzMC01MDRkLTQzNGEtOGU4MS1mMzBmN2ZjODYzMWMucGRm), 2025 reporting period | Normal-TLS curl; full PDF extraction; total explanation pp. 2 and 31; p. 31 / PDF p. 35 visually checked | SHA-256 `c2b35aa99a93619dbb8c2a4d8d587ca2cf09f93d2bd6b72dea35a2e7bc4ee39e`. Programme aggregates; two 50-case budget lines cannot establish unique cases or conversion. Design fees are not completed works. Publication date not independently resolved. Aggregate paraphrase; no individual records. |
| M03 | [CMO professional reconnaissance announcement](https://cmo.gov.taipei/News_Content.aspx?n=2489C7DF2B5C1860&s=A10AD6427FA383AD&sms=72544237BBE4C5F6), page updated 2016-11-03 | Normal-TLS curl HTML main text: chosen Chongqing/Heping road axes, ≥30-year scope, 2016-11-07 start and 1,500 target | Historical agency account, no completion or current-force check. Reconnaissance is not formal initial assessment; 2016 consent statements cannot be used as a current exemption. Paraphrase and link only. |
| M04 | [Taipei public-renewal implementation rules](https://laws.gov.taipei/law/LawSearch/LawPrint/FL080447?type=0), revision 2020-04-09 / effective 2020-04-30 | Live city law-system HTML; articles 4–7 and 11–12 re-read in full | Defines project selection and written suitability review; ten required contents are not ten weighted factors. No case queue, quantitative weights or review-effort result. Statutory text is linked/paraphrased, not a licence for other site content. |
| M05 | [Citywide renewal-area designation plan](https://www-ws.gov.taipei/001/Upload/373/relfile/18970/9353208/d34b29fc-b649-4c03-9757-7bcd03a1d375.pdf), 2018 plan | Normal-TLS curl and PDF text extraction; printed pp. 7–9 weighted overlays and boundary/exclusion rules | SHA-256 `41b291b8fbc29ea616ad5a2cd981d64ec1e275b2b3f0db20433b744a37030cd3`. Area designation, not public-renewal project selection; later changes not audited. Official planning document paraphrase; no raw geodata redistributed. |
| M06 | [URO 虎林街60巷 advancement account](https://udd.gov.taipei/events/fhqekzq-19812), issued 2023-12-29 / page updated 2024-03-15; [follow-up](https://udd.gov.taipei/events/fhqekzq-20722), 2025-05-27 | Original HTML main text re-read; entry, technical estimates, willingness and advancement/implementer steps | Agency-reported success case, no rejected-case comparison, independent causal evaluation, source intent forms or completed rebuilding verified. Paraphrase and link only. |
| M07 | [URO public-renewal application FAQ](https://english.udd.gov.taipei/News_Content.aspx?n=6E18BA96F3CB0148&s=75051238204F5D67&sms=87415A8B9CE81B16), updated 2025-10-28 / reviewed 2026-09-11 | Original publisher HTML, all four 7599 stages | Programme intent/selection stages are distinct from statutory owner/area consent. FAQ is not every public-renewal route; exact site eligibility annex not independently refreshed here. Link/paraphrase only. |
| M08 | [CMO proactive initial-assessment flow, annex 5](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/d1c62bc5-5690-431c-93eb-51f85515dc16.pdf), PDF created 2023-02-08, linked from [CMO 建物耐震評估](https://cmo.gov.taipei/cp.aspx?n=53F406AE758E3270) | Normal-TLS curl, `pdftotext -layout`, one page in full | SHA-256 `e4b6706d0bd7737f341a8bd75cea2ea985ef70239a090ea2ee1c3916ef5d9354`. Process only; no selection criterion or volume. Paraphrase and link only. |
| M09 | UDD 主管決算 for [111](https://udd.gov.taipei/assets/c1psQ9R9EaX5htDXRd8UdL/attachs/111年度都發局主管決算.pdf), [112](https://udd.gov.taipei/assets/c1psQ9R9EaX5htDXRd8UdL/attachs/112年度都發局主管決算.pdf), [113](https://udd.gov.taipei/assets/c1psQ9R9EaX5htDXRd8UdL/attachs/都發局113年度主管決算.pdf) and 114 (M02), from [UDD 預決算書](https://udd.gov.taipei/collection/d37gqja) | Normal-TLS curl, `pdftotext -layout`; CMO revenue notes and 辦理情形 rows at the pages cited in §3; 114 PDF p. 9 explanation | SHA-256 111 `d84bfe36ac6d3522a0222310f244597792a9d2d69cc174b396e8fd3717f03918`, 112 `8991617cdbf14fb92cc07bb2f3e4a477005365adb14c8ccd9f2d00173b720d87`, 113 `e8df07b8914847ca13a7b17b01a5fde95ed09e24a1eaebc9843f4c8602e4d35c`; 114 matches M02. Agency-reported aggregates; overlapping year labels; no case identities. |
| M10 | UDD reports to the council, [第14屆第7次 (2026-04)](https://udd.gov.taipei/assets/nvKF2cDhA7pKtLuWKQLGHn/attachs/臺北市議會第14屆第7次大會都發局工作報告(115年4月).pdf) and [第8次 (2026-07)](https://udd.gov.taipei/assets/nvKF2cDhA7pKtLuWKQLGHn/attachs/臺北市議會第14屆第8次大會都發局工作報告(115年7月).pdf), from [機關工作報告](https://udd.gov.taipei/article/LnthK8f) | Normal-TLS curl, `pdftotext -layout`, keyword search then the 危老, 403 and 575 passages read in full | SHA-256 2026-04 `9458c2c9f7d1e428a4280649ed2bc67111f2d1ff39753be21468449534b66673`, 2026-07 `a8803169dc3448b5efe5ea70f991b2e864d65d31fc52991e2ef8ecd46de0ac57`. No passage on the proactive 50-case programme; agency-reported progress. |
| M11 | [CMO 危老問答集合併版](https://www-ws.gov.taipei/001/Upload/845/relfile/-1/845/35b648d6-30d1-4a2a-96ba-8e9ca300b37b.pdf), PDF created 2025-11-06, modified 2025-11-17, 273 pp., linked from [CMO 危老重建](https://cmo.gov.taipei/cp.aspx?n=CC5912F40B7F47CE) | Normal-TLS curl 2026-10-15, `pdftotext -layout`, keyword search; B-14, C-10, D-09–D-13, E-28–E-33, G-11 and H-02/H-06 read in full | SHA-256 `3a21746c1790b34f3a33071f66ee732c87fd4c74b816146acdd5effe21450bca` (same file as §2). Agency FAQ, not a legal instrument |
| M12 | [土地登記規則](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0060003) §24-1 (amended 2021-07-13); [URO class-3 transcript procedure](https://uract.nlma.gov.tw/uploads/rule/B3101110018700000.pdf), dated 2021-01-22, attaching MOI's 核發土地登記及地價資料謄本注意事項 (issued 2015-01-09) | National law database HTML; PDF curl and `pdftotext -layout`, points 1–7 of the attached rules read in full | PDF SHA-256 `42ee69d2d254a2ab4cfa13853301382d80b5d406c28a8ed10beae0c5de984988`. The attached MOI rules are the 2021 copy; later amendments unchecked, though FAQ B-14 (2025) is consistent |
| M13 | [公寓大廈管理條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070118) §6, §7, §25, §29, §29-1, §30–32, §47, §49-1 (amended 2022-05-11); [MOI criteria for at-risk buildings](https://www.moi.gov.tw/news_content.aspx?n=145&sms=9082&s=280390), issued 2023-06-06 | National law database HTML parsed in full; MOI page read with the web tool | Whether §6 covers a retrofit that takes floor area is untested; Taipei expansion under §29-1 ¶2 not found in a bounded search, absence unverified |
| M14 | [民法](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001&flno=1101) §1101 and §1113 | National law database single-article HTML | Application to 危老 consent is unsettled in the sources read; court decisions found concern sales only |

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

The [canonical readiness record](../research.md#problem-fit-and-separate-readiness-of-the-expanded-candidates)
owns status. Primary A now has a reproduced real aggregate input-reconciliation example (D01/D02),
while allocation itself and B remain demonstration specified / decision insufficient. T06-D is a
secondary deferred hypothesis, demonstration unassessed / decision insufficient. Earlier T06-A–C
remain bounded supporting alternatives with existing-service baselines; no new operational gain
is established. Local fictional-data prototypes exist (§4); no production application or real allocation has been implemented.

**Changed evidence and consequence:** M01 establishes the 2026 programme's planned 50-case scale,
not a backlog or remaining slots. M02 supplies selected 2025 activity totals, correcting the
blanket count gap but not supplying cohorts or grade distributions. M04/M06/M07 establish
public-renewal criteria and stage advancement; they do not validate comparative priority.
M05 refutes a blanket absence-of-weighting claim at the area-planning level. B01–B07 remain a
post-2001 identity-chain audit, not the old-stock universe. The two scoped CMO lists remain
readable sources, not licensed all-city inventory or progression evidence.
D03 additionally establishes retrievable historical pre-2001 permit attributes, superseding the
blanket restricted-only inference. It does not establish current survival or a complete inventory.
D01/D02 establish three permit-ID collisions with unmatched addresses, not three confirmed
building-status contradictions. No simulation is needed for that input-preparation example.
M08–M10 describe assessment activity and an agency explanation for retrofit funding difficulty.
Their different programmes and cohorts do not establish a conversion rate or the main bottleneck.
A remains demonstration specified / decision insufficient. T06-B is separate follow-up research;
S01–S04 and the board demonstrate different tasks, not measured allocation value.

**Supported / refuted / unresolved:** supported: existing programme gates and planned scale;
refuted for current public inputs: real all-city individual safety/renewal rankings and treating
missingness alone as a meaningful priority order; unresolved: actual selection difficulty,
incremental decision value, adoption and civic effect. A disclosed fictional example illustrates
logic only. Citizen samples inform execution questions, not a replacement for the explicit
municipal user. Propagate these qualifications to the master comparison, dependency index,
queue and reading mirrors; §7 owns the one current check.

## 7. Next actions and open decisions

**Next executable research check:** within D02's scoped permit list, measure whether a bounded
age-branch subset can link D03's dated completion/floors to D01 management evidence without
ambiguous permit-to-building transfer. Start with the three observed collisions and the archive's
duplicate/conflict groups; inspect permitted original identity records, keep raw identities private,
and report an explicit linked/unresolved result. Stop an individual action claim if contemporary
scope or survival cannot be confirmed. Do not add a citywide score, F simulation or UI before
this question is answered. The present all-real reconciliation is already reproducible (§4/§5).

**Hackathon delivery versus effectiveness:** show the original pain, existing rules, fixed source
population, real finding, uncertainty checks and conditional action using the reproducible aggregate
comparison. No interview, agency reply or historical cohort is a delivery prerequisite. The
historical solicitation comparison needs lawful selected/unselected records, decision-time
information, capacity and practitioner error/effort criteria; it is deferred post-event and remains
unresolved. The prepared request is retained as a later route, not sent.

**Deferred supporting check:** the public weak-storey cost reference (at least five comparable cases
with cost, layer area, storeys and households) remains useful to the estimator but does not establish
allocation value. Until supported, the estimator remains subsidy-side only.

**Completed 2026-10-15:** the 115年度 council-report and 2022–2025 account check (§3 funnel); the household burden check (§3), which is unresolved and adds an access gate. The owner-reachability check (§3): mechanisms supported, prevalence unresolved; the management organisation is a recurring gate.
The inspected public sources did not yield a complete candidate, invitation and refusal cohort; internal availability is unknown.

**Deferred owner-situation checks:** whether §6 entry duties cover a weak-storey retrofit that takes floor area, and whether Taipei has expanded the §29-1 at-risk criteria; both need an agency answer, which is external contact. Count owner situations only from de-identified agency statistics, never from personal records.

**Deferred checks:** T06-D's assessment-consent, discretionary designation and unit-size questions
remain open but do not lead this municipal-allocation cycle. Dated promoter-register comparisons
could test progression; a one-date filing snapshot cannot. Public-renewal case evidence informs B
separately and never transfers its project criteria to A.

**Acquisition boundary:** public council/agency/audit records remain the default. An alternative files information
requests for de-identified initial-assessment statistics or house-tax statistics under 稅捐稽徵法
§33 ¶2; this is external contact and needs action-time confirmation.

**Reading mirror rule:** refresh [the HTML report](issue-6-building-resilience.html) whenever this
document's conclusions change materially.

## Change log

| Date | Change |
| --- | --- |
| 2026-10-15 | Broad web/connector and academic/community discovery; D01–D08 original-source audit; real 5,489-permit/9,657-registration-ID reconciliation with three unresolved collisions; historic pre-2001 XML recovered and qualified; field feasibility including S01–S04; separated demonstration acceptance from post-event effectiveness |
| 2026-10-13 | Owner focus on issue 6; domain primer; allocation reorganization into decisions A and B |
| 2026-10-14 | Municipal decision scope clarified; 50-case programme and 2025 accounts verified; candidate baselines/rejections aligned; undated-filing and sample inferences qualified |
| 2026-10-15 | Owner adds "actually solves it" test; programme funnel (M08–M10): proactive slots fill, retrofit stalls on household burden; A gains downstream success condition; T06-B becomes follow-through; route map of exits and their gates; unreachable/restricted-owner rules and Taipei inheritance-listing counts; household burden check (regime-dependent magnitude, half-removable uncertainty, access gate); owner chooses demo direction (a); owner reachability and standing (M11–M14): transcript routes, management organisation as gate, guardianship and access levers; owner makes the stall board the core candidate, mapping each critical pain to its digital part; fictional-data HTML prototype of the board |
| 2026-10-14 | Identity audit; deep investigation (P/E/I/X); owner rule to start from the live prompt and citizen voices; pain re-anchor and pain tree; T06-D added; moved into this topic document (template v1) |
