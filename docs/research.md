# Research Master — Method, Event Facts and Topic Index

## Scope

Research for [市政 debug松](https://puma.taipei/hackathon), started on 2026-10-13: investigate the
official issues and self-chosen civic problems from evidenced pain, verify public evidence and data,
and prepare informed civic research.

**Current focus (owner decision):** issue 6, old-building seismic resilience: a municipal priority
model for earlier inspection **A** and public-renewal suitability assessment **B**. Its position is
summarized under [Current focus — issue 6](#current-focus--issue-6) and owned by the
[topic document](topics/issue-6-building-resilience.md). Issues 1–5 and 7 keep their dated
2026-10-13 records as legacy topics, deferred while the owner focuses on issue 6. Research claims
freeze on 2026-10-23 12:00 Taipei (topic §7). Final entry selection and new application
implementation remain separate owner decisions; the existing app and prototypes are historical
exploration.

## Reading guide and evidence date

This master and the topic documents under `topics/` together form the research authority. The
master owns method, event facts and cross-topic records; each topic document owns its issue (see
the [topic document standard](#topic-document-standard)). Source observations were retrieved on
**2026-10-13** unless a section states a later date (event page re-read 2026-10-14; issue-6 work
2026-10-14–22). No blanket external-source refresh followed the 2026-10-13 run, and a retrieval
date does not establish current operating conditions.

**Document revision — 2026-10-22:** building-first narrative and F01–F08 source audit integrated; F01 score refresh and report rebuild completed; five-track method deepening now reports actual source/linkage tests, with numerical inputs unchanged; liquefaction category meaning/full-population coverage verified or qualified; paired missing-input stress completed without adopting new scores. **2026-10-21:** condensed; superseded material (the data-readiness-first
direction, the 2026-10-13 cross-topic recommendations and candidate ordering, stage tables and
tool-run history) removed. The previous consolidation (2026-10-20)
made no external refresh.

| Reading goal | Section |
| --- | --- |
| Understand the event and the organizer's problems | [Official baseline](#official-baseline); [official pain points](#official-pain-points-and-decision-fit) |
| Understand how research is judged | [Research umbrella policy](#research-umbrella-policy) |
| Follow the analysis and connect findings to decisions | [Analysis protocol](#analysis-protocol-and-finding-to-decision-synthesis); [issue-6 worked synthesis](topics/issue-6-building-resilience.md#synthesis--what-the-analysis-changes-about-the-proposal) |
| Continue issue 6 | [Current focus — issue 6](#current-focus--issue-6); [topic §7](topics/issue-6-building-resilience.md#7-next-actions-and-open-decisions) |
| Open one issue, or write a new topic document | [Topic index](#topic-index); [topic document standard](#topic-document-standard); [topic research playbook](#topic-research-playbook) |
| Check legacy-topic status, readiness and resume checks | [Next-investigation queue](#next-investigation-queue); [canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates) |
| Find dataset dependencies and their verification state | [Dataset-to-candidate index](#dataset-to-candidate-index) |
| Inspect the organizer-listed sources and supplementary platforms | [Publisher dataset audit](#publisher-dataset-audit) |
| Understand the Twinkle Hub discovery route | [Twinkle provenance](#twinkle-provenance-and-role-in-this-project) |

**Interpretation:** catalog read, row sample, full-file parse and validated join are different
observations. A full parse verifies only the stated checks; it does not prove completeness,
unique real-world objects or operational accuracy. Counts refer to records unless explicitly
qualified. In particular, a meal-list row is not a verified operating site/capacity unit; an entrance
row is not a park/station; and collision rows are not asserted unique accidents or all victims.

## Official baseline

**Evidence — event page, retrieved 2026-10-13 and re-read 2026-10-14 11:51 Taipei:** the
[official event page](https://puma.taipei/hackathon) announces 市政 debug松, organized by
沈伯洋競選辦公室. Registration closed early on **2026-10-14 (Wed) 14:00** with 80 places (the
2026-10-13 read showed October 18, 23:59); admission is selective: admitted participants are listed
and emailed, others are not notified. Attendance is free. October 23, 19:00–22:00 is online;
October 24, 09:30–18:00 is onsite, and at least one team member must attend onsite. Day 2 announces
the Demo list at 12:00 and 10–15 teams demo. Submission closes October 24 at 16:00. Dates are
interpreted as 2026, local Taipei time; the displayed schedule omits the year and timezone.

The seven directions concern trees, public bins, rats, Neihu traffic, bus networks, building
resilience and a self-chosen civic problem. Working demonstrations are required. Simulated inputs
are allowed with disclosure; README must identify AI tools and open-source dependencies. Coding
is permitted from Day 1. Complaint data is activity-only and must not identify people. Dataset
licenses apply individually. Teams retain copyright; organizer open-source inclusion needs consent.
Voting determines three featured works; there is no prize money.

Method: curl GET and standard-library HTMLParser text extraction (2026-10-14 snapshot: 51,055 bytes,
SHA-256 `d01038835138132b910f80115e2e9ecfa1a20a913bb4cfc471d528aa98eeb7b4`), with web-search
corroboration; the browser and web-fetch tools could not open the page. Scope: one organizer page.
It is not confirmation of team acceptance or of the organizer's underlying civic claims, which stay
attributed unless separately sourced. Recheck event rules before acting on them.

**Owner decision — 2026-10-14:** the owner reports having registered; admission is not yet known.

**Open questions:** eligibility of pre-existing code is unclear although coding is permitted from
Day 1; check official clarification before reusing a prebuilt artifact. Team, final entry and
application stack remain owner decisions.

## Official pain points and decision fit

**Evidence — retrieved again 2026-10-13:** the [official issues section](https://puma.taipei/hackathon#issues)
frames the topics as citizen pain points organized by the policy team. Six prompts include desired
directions; the seventh invites an independently defined problem. The page permits disclosed
simulated inputs and prioritizes an operable solution. Its [rules](https://puma.taipei/hackathon#rules)
require a working demonstration and recommend explaining the department, data and cost needed
for implementation within 100 days.

Method: curl GET, standard-library HTMLParser text extraction and inspection of `issue-1` through
`issue-7` and `rules`. Limitations: this verifies the organizer's framing, not the prevalence,
causes or numerical claims behind it.

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

**Inference:** data readiness is not topic merit. A tree inventory is a prerequisite to site
review, not proof of planting feasibility or shade equity; a bin-access comparison addresses
placement, not overflow or collection dispatch. A narrowed workflow must identify its contribution
to the official pain point and the parts it leaves unresolved.

**Evidence — verbatim re-read 2026-10-14:** the issues section states 「以下是市政痛點，不是市政解答。題目來自「市長，你給我聽好了」蒐集的市民意見，由政策組整理。」
The page says the campaign's citizen stage received over a thousand complaints and suggestions,
organized into seven pain points. Each prompt's proposed model or map is therefore the policy
team's suggested direction; the pain is the citizen situation that precedes it. Method: same
curl/HTMLParser snapshot as the live-page re-read above.

**Evidence — citizen-voice origin, 2026-10-14:** the stage is [taipeispeaksup.org](https://taipeispeaksup.org/)
(operator 碳矽互動設計). Its public pages load `feed/v1/voices.json` from the operator's public
storage. The 2026-10-14T03:50Z feed held 18 topic categories with counts (no housing or building
category), and only a rolling sample of four recent voices per topic and per district; no history
is exposed. Voice labels reached about No.63,900. The privacy and use notice (updated 2026-08-19)
reserves copyright in reports and statistics; quoting, reproduction or adaptation by candidates,
media or researchers requires the operator's prior written consent. The hackathon rules restrict
the organizer's de-identified copy to this event; on 2026-10-13 it was announced as forthcoming and
no download was observed. **Limitations:** a rolling sample, not a census; topic labels are
self-selected; voices are reports, not prevalence. Raw voices, display names and quotations stay
outside Git; topic findings are paraphrased.

**Open question:** which decision causes a repeated, consequential difficulty for a reachable user?
The official page does not establish a validated workflow, baseline or agreed success threshold.
Public-source research can investigate those gaps; external interviews/messages retain the existing
action-time confirmation boundary.

## Research umbrella policy

**Owner decisions — 2026-10-13/14:** this policy governs research, data discovery, comparison and
demonstration proposals for organizer and free-topic candidates. It neither selects a topic nor
authorizes implementation; company priorities remain with the origin repository.

- Investigate each topic backward from an evidenced pain point and observable success/rejection
  conditions. Sources are not restricted to one discovery service or government APIs. This
  replaced the earlier data-readiness-first priority (2026-10-13).
- The original pain is the core of every topic. When a topic starts, read its official prompt
  verbatim on the live page once and look for the citizen voices it was organized from. Record the
  verbatim pain sentence, retrieval time and what the citizens themselves describe in the topic
  document, separately from the policy team's suggested solution; a suggested model, map or ranking
  is a direction to test, not the problem definition (2026-10-14).
- Re-check the live page only before relying on event facts that change (deadlines, rules, data
  terms) for an action, or when there is a reason to think the prompt changed (2026-10-14, later).

Internal review and research-route custody is retained in `docs/provenance.md`, not in the
published method.

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
6. **Analyse the fixed population.** Apply the [analysis protocol](#analysis-protocol-and-finding-to-decision-synthesis)
   before interpreting a join or distribution. Reconcile all records, inspect missingness and
   ambiguity, and test consequential definitions. Completion: reproducible results retain the
   original denominator, uncertainty groups and sensitivity checks; exploratory refinements are disclosed.
7. **Interpret findings, then choose presentation.** Trace each supported finding to what a named
   user could check or decide differently, and distinguish that implication from measured benefit.
   Present the same bounded case from pain and baseline through evidence, conditional action and
   result, including rejection evidence. Completion: the required record is complete, unknowns have
   resolution actions, and the queue names one consequential next check. Compare topics on the same
   dimensions; presentation follows supported claims, while topic/product selection remains an owner decision.

**Domain-practice check — owner direction 2026-10-16:** before interpreting data or choosing a
workflow, reconstruct how the relevant professionals and agencies actually perform the task.
Use operative rules, applicable methods/manuals, original forms and operator evidence; record the
purpose, version, unit, qualifications, necessary observations, outputs and downstream authority.
Resolve overloaded scores and terms by instrument rather than name alone. Separate engineering
findings, administrative eligibility, funding/consent and measured outcomes. A field absent from
public data must not be replaced by a convenient proxy without a justified decision-specific method.
Professional disagreement, unavailable governing text and unobserved practice remain explicit gaps.
Issue 6's [professional audit](topics/issue-6-building-resilience.md#professional-practice-and-assessment-to-action-audit-2026-10-16)
records instrument boundaries; the [core dictionary](topics/issue-6-building-resilience.md#indicator-dictionary-and-weight-provenance) applies them to the current model. No licensed assessment is claimed.

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
| Analysis contract | Fixed population/unit/as-of date, reference rule, transformations, exclusive result groups, missingness and sensitivity checks; prospective versus exploratory parts |
| Claims | Observations, proxies, modeled scenarios and simulated inputs distinguished; permitted conclusion |
| Finding to decision | Source-backed result → interpretation → named next check/action → scope of the claim → what would refute it; baseline gain separately established or unresolved |
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

One topic author owns each investigation and the complete interpretation. Bounded discovery
assistance receives a named question, search scope and completion condition: return candidate URLs,
original publishers, observed schemas/access, period, licensing evidence, limitations and
contradictory findings. Label uninspected hits as leads. The topic owner checks consequential
claims against source bytes before integrating; an assistant's output is not evidence. Stop a discovery
branch when its assigned uncertainty is resolved or the named route is exhausted, reporting the
remaining unknown and next feasible check. Separate assistance/verification receipts from the
public argument; preserve explicit research-route requirements in internal provenance.

### Analysis protocol and finding-to-decision synthesis

The [issue-6 scoped analysis](topics/issue-6-building-resilience.md#age-branch-linkage-analysis-2026-10-16)
is a worked application of this protocol (2026-10-16). It adds reusable analytical discipline, not a
universal numerical threshold, building-risk model or requirement that every topic use the same
datasets. The topic owns the calculations; this master owns the procedure and interpretation rules.

| Stage | Required analytical record | Completion / rejection |
| --- | --- | --- |
| Frame | Recorded pain, decision owner/trigger, current practice, supported and unresolved parts | An information question connects to an executable action; otherwise retain a hypothesis rather than invent a software need |
| Freeze | Source versions/hashes and rights; observation versus retrieval dates; analysis date; population, inclusion rule, unit and denominator | Same population throughout a comparison; a scoped list is not a census and a permit/address is not automatically a building |
| Audit | Raw-to-used row counts; blanks/duplicates/conflicts; calendar, units, chronology and category meaning; source lineage | Parseability, internal consistency, independent accuracy and currentness remain separate; never silently repair consequential values |
| Link | Exact key namespace and one-to-one/one-to-many/many-to-many relationships; distinct fields/scopes; unmatched and ambiguous partitions | A successful key match establishes only the stated relationship; contemporary identity/scope requires its own evidence |
| Explore | Exclusive result groups that reconcile; missingness by relevant source/time/geography strata; relationships justified by the question | Complete-list descriptions are bounded to that list; subgroup counts do not establish prevalence, causes or treatment effects |
| Challenge | Alternative plausible definitions, boundary dates, address rules and record types; provenance independence; contrary evidence | Report result/action changes and unchanged results; identical copies do not independently validate each other |
| Synthesize | Finding → reasoning → named action/check → remaining gap → rejection and presentation implication | Descriptive pattern, hypothesized usefulness and observed baseline gain are explicitly separate; the interface cannot promote one into another |

State the contract before the new experiment. When inspection reveals a new quality predicate,
label it exploratory, explain its reason and report the consequence beside the original or relaxed
definition. A discovered criterion must not be described as preregistered. Independent extraction
can verify arithmetic/parsing; it does not make the underlying administrative data independently true.
For a nonrandom administrative list, do not attach population estimates or generic statistical
significance to frequencies without a justified sampling/inference design. An unmatched record is
not absence; an empty date is not zero age; a field passing syntax is not confirmed meaning.

The issue-6 example shows why the stages matter: broad historical linkage did not establish current
management scope; a year-specific gap made matched-only summaries misleading; chronology flags
persisted in a current publisher export. Those findings change which originals to check, not which
building is safest or most urgent. Source copies sharing administrative lineage corroborate
reproduction, while the error explanation stays unknown.

**Spatial, temporal and aggregation controls:**

1. **Match the unit of analysis.** City totals, district counts, village populations, stops, trees
   and building sites are not equivalent observations. Never distribute a district total across
   points and label the result observed demand or risk.
2. **Establish spatial keys.** Prefer stable publisher IDs. For coordinate joins, check CRS, axis
   order, Taipei bounds and geometry validity, and compute distance in a projected CRS; for name
   joins, normalize spelling and aliases but report unmatched records. A straight-line buffer is a
   scenario, not a measured walking catchment.
3. **Align time.** State each dataset's observation period and refresh behavior. Join traffic by
   detector, direction, lane, vehicle class and timestamp; sum only disjoint count intervals, never
   rates or speeds, and do not count the same vehicles repeatedly across downstream detectors.
4. **Separate observation from counterfactual.** An assumed shift, candidate placement, future
   canopy, synthetic boardings or a manually weighted risk score is a scenario; label inputs and
   results accordingly.
5. **Measure dependency quality.** Report records used, missing values, duplicates, successful
   joins, stale timestamps, invalid units and coverage gaps. Missing live readings are unknown, not
   zero; a fresh metadata date cannot rescue an old resource.
6. **Keep licenses separate.** A government open-data license does not cover third-party reports,
   photographs, tiles or the organizer's activity-only feedback. Unknown permission blocks
   redistribution, not read-only investigation.

**Presentation rule:** choose the smallest form that preserves the supported claim. Use a grouped
evidence explanation when the result distinguishes missing/conflicting/usable historical evidence;
use a map only for verified spatial relationships at the stated scale; use a scenario comparison
for declared assumptions; use a priority recommendation only with a defensible candidate universe,
purpose-specific criterion, uncertainty and baseline comparison. An analysis that finds no consequential difference is also a result:
narrow or defer a workflow when the data cannot distinguish a consequential action. A recommendation
about how to explain research is not product selection or permission to build a new interface.

**Separate delivery from effectiveness:** a reproducible pain → data → finding/scenario → conditional
action explanation can complete a hackathon demonstration. Interview access, agency replies and
historical cohorts are later effectiveness routes, not automatic delivery prerequisites. In their
absence, effort saved, selection gain, adoption and civic outcomes remain unverified. Where an
essential real input has no evidenced feasible acquisition path, narrow the workflow rather than
simulate a solved dependency; disclosed simulation supports only its stated demonstration.

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
  [analysis protocol](#analysis-protocol-and-finding-to-decision-synthesis) controls own spatial,
  temporal and aggregation checks.
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

## Topic document standard

**Owner decision — 2026-10-14:** keep one master document for method, event facts and cross-topic
records, and one maintained document per official issue. Structure and consistency come first.
Issue 6 is the first topic migrated to this standard.

### Document ownership

| Document | Owns | Does not own |
| --- | --- | --- |
| `docs/research.md` (this master) | Mandate, event facts, umbrella policy, analysis protocol and this standard, topic index and current-focus summary, cross-topic comparison, next-investigation queue, canonical readiness, dataset-to-candidate index and shared organizer-source audits | Topic-specific evidence/workflows and internal tool/run custody, which belongs to `docs/provenance.md` |
| `docs/topics/issue-N-<slug>.md` | Everything specific to one official issue: verbatim prompt, citizen pain, pain tree, practice, workflows, evidence, next actions | Status labels (it links the canonical readiness record); cross-topic ranking |
| `docs/topics/issue-N-<slug>.html` | Traditional Chinese reading mirror of one topic document | New findings; it never leads its Markdown |
| `docs/research-report.html` | Traditional Chinese overview: method, event facts, topic index, the current focus and a short legacy-topic summary | Topic detail |

### Topic Markdown skeleton (template v1)

Start a new topic by copying [the template](topics/TEMPLATE.md); [issue 6](topics/issue-6-building-resilience.md) and [its mirror](topics/issue-6-building-resilience.html) are the reference implementation.

The order and numbered headings are fixed. A section without work yet says `Not yet investigated`
and names its next action.

0. **Title and status table.** `# Issue N — <English name>`, then a table with these fields: the
   official prompt link and verbatim title, the template version, the pain recorded time, the
   evidence cutoff, the workflows with a link to the canonical readiness record, the reading
   mirror and the open owner decisions.
1. **`## 1. Official prompt and citizen pain`.** The verbatim pain sentence and its retrieval
   time, and citizen voices paraphrased with their sample limits. The organizer's suggested
   solution is kept separate from the pain.
2. **`## 2. Pain tree`.** A table running pain (source) → decision and owner → fields the
   decision needs → where they could come from, including data the team could collect. The
   evidence behind the table follows.
3. **`## 3. Current practice and baseline`.** Rules, existing services and their observed
   performance.
4. **`## 4. Candidate workflows`.** Lead with the current bounded workflow and its finding-to-decision
   synthesis, linking detailed calculations in §5. Then show supporting/deferred alternatives with
   their current disposition. Use the required candidate record; do not let an older prototype lead
   by file order or imply that a presentation recommendation is product selection.
5. **`## 5. Evidence and data audits`.** Dataset audits, source ledgers and analysis contracts/results,
   each with retrieval date, method and limitations. Keep raw evidence, transformations, exploratory
   refinements, exclusive partitions and sensitivity results traceable in one owning subsection.
6. **`## 6. Readiness and integration`.** The issue-specific consequence only; status stays in
   the canonical record.
7. **`## 7. Next actions and open decisions`.** One executable next check, plus owner decisions
   with their consequences.
8. **`## Change log`.** Dated one-line entries.

### Topic HTML skeleton

Build the page with `html-report-system` on its neutral foundation. Validate it with `--portable`
and look at it at 1200 px and 390 px.

The page title is 「<議題>研究報告」. The thesis states the current pain-based conclusion; the summary
states what is supported and still unknown. Preserve the incumbent neutral report tokens. Use this
reasoning order, with short natural-language navigation rather than mandatory cards or section numbers:

1. Research method and evidence labels.
2. Original official pain, citizen experience and decision owner.
3. Existing practice and unresolved bottlenecks.
4. Data scope, audited findings and uncertainty checks.
5. Finding-to-decision synthesis: implication, action, remaining gap and permitted claim.
6. Current workflow and separate supporting alternatives.
7. Demonstration acceptance, later effectiveness validation and stopping conditions.
8. One next research check, owner decisions and directly accessible source/professional appendices.

Headings and navigation reflect the actual content; preserve established anchors or update every
dependent link. Short explanations and sources are visible directly, and longer material uses
ordinary headings/navigation rather than triangle disclosure controls. The footer records the
evidence cutoff and the SHA-256 of the topic Markdown.

Link behavior: links to other pages, research documents and sources open in a new tab with
`target="_blank" rel="noopener"`; fragment-only links (`#section`) stay in the current page.
Do not add link-opening instructions or notices to reports or README files (owner, 2026-10-14).
GitHub-rendered Markdown keeps its native link behavior.

Chinese prose wraps naturally across the allocated reading width, including headings, summaries
and tables. Do not force paragraph tails, balance body copy or impose separate narrow prose caps.
Scope aggressive word breaking to unbounded hashes/URLs/code. Do not run `cjk_line_ends.py` or add
tail spans on reports (owner's natural-reading rule).

### Rules

- **Naming.** Files are named `issue-N-<english-slug>`. Workflow IDs keep their track prefix
  (T06-A), and candidates C01–C08 keep their identities.
- **Start from the source.** Every topic begins from its recorded official prompt and citizen
  voices (owner rule above). Quote organizer text verbatim only for the prompt; paraphrase
  citizen voices.
- **One place per fact.** The master owns method and cross-topic records; the topic document owns
  its issue. Link instead of duplicating.
- **Keep sensitive material out of Git.** This covers raw downloads, names, addresses and
  restricted data.
- **Migrate legacy documents with new research.** A legacy topic document keeps its earlier
  layout and says so in its status table. Migrate it when its pain is first recorded; do not reformat it
  without new research.
- **Update in order.** When a topic's conclusions change materially, update its Markdown first,
  then its HTML mirror, then its row in the master topic index.

## Topic research playbook

**Owner decision — 2026-10-14:** consolidate what the issue-6 work taught about method and
document management so that any researcher can continue a topic, or start the next one, the same
way. Each lesson cites the issue-6 observation that produced it.

### Procedure for one topic

Run these steps in order. Each step ends with something written in the topic document.

1. **Record the source once.** Run `python3 scripts/official_prompt.py N --rules`. Quote the
   issue's pain sentence verbatim with the printed retrieval time in §1; later work starts from
   that record. Re-run it only before relying on deadlines or data terms for an action. Compare
   extracted text, not page hashes: the markup changed between two reads on 2026-10-14 while the
   text did not.
2. **Find the citizen voices.** The prompts were organized from the campaign's citizen stage (see
   [Official pain points](#official-pain-points-and-decision-fit)). Read what the public pages
   show, paraphrase, and state the sample limits. Do not collect the feed systematically, and
   quote only with the operator's written consent. The organizer's de-identified event copy is
   the route to a larger set.
3. **Separate the pain from the suggested solution.** Record the prompt's model, map or ranking
   as a direction to test without discarding the named decision owner. In issue 6 residents are
   affected, while the city decides inspection/public-renewal priorities; two sampled voices
   raise execution constraints, not proof that the municipal objective should be replaced.
4. **Build the pain tree.** For each pain, write down who decides what, which fields that
   decision needs, and where each field could come from. Sources include public data, restricted
   routes needing a request, and data the team could collect.
5. **Read the baseline before proposing.** Find the existing rule, programme or service that
   already does the task, and its observed throughput. Issue 6's "city as project manager"
   already existed as the promoter programme; an undated filing register does not establish
   conversion or delay. Test the remaining gap against that existing service.
6. **Read the governing rules in the original.** Statutes come from the national law database
   (`law.moj.gov.tw`, by pcode). Taipei rules come from `laws.gov.taipei` print views. Agency
   FAQs and attachments come from the agency topic page. A threshold can be the decisive lever:
   in issue 6 the assessment result changes which consent rule applies.
7. **Open the agency's attachments before calling data restricted.** In issue 6, CMO's topic
   page published two building-level lists that overturned an earlier "restricted only"
   conclusion. Parse PDFs with `pdftotext -layout`, and record only aggregates in Git.
8. **Locate the bottleneck without inventing a funnel.** Separate programme rules, administrative
   totals and linked case progression. Different assessment/retrofit counts do not establish a
   conversion rate, selection quality or the main constraint. Keep competing explanations unresolved
   until evidence distinguishes information from authority, finance, capacity or coordination.
9. **Execute the bounded analysis.** Follow the [analysis protocol](#analysis-protocol-and-finding-to-decision-synthesis):
   freeze units/population/versions and the reference rule; audit, link, retain every result group,
   inspect structured missingness and challenge definitions. Keep exploratory refinements visible.
10. **Translate findings into conditional actions.** In topic §4, connect each supported result to
    the original decision, its next check, remaining gap and rejection condition. Choose how to
    explain those results; do not declare a new product or measured benefit from a descriptive pattern.
11. **Write candidates with rejection conditions.** Use the
    [required candidate record](#required-candidate-record). Keep the policy-direction candidate
    and the pain-side candidate separate and both labelled hypotheses.
12. **Update in order.** Update the topic Markdown, then its HTML mirror, then the
    [topic index](#topic-index) row. Then run the checks below and commit one coherent change.

### Method lessons

- **Anchor on the recorded pain; re-check facts that move.** A paraphrase in this repository
  drifted from the source and framed issue 6 around the wrong problem, so work from the verbatim
  record. Event facts do move (registration was brought forward from 18 October to 14 October
  14:00), so re-check the live page before acting on a deadline or rule.
- **No public data is a starting point, not a stop.** Look for the original agency document, a
  request route or a collectable observation. If a route needs external contact, name it and wait
  for owner confirmation.
- **Label every claim.** Use Evidence (source, retrieval time, method, limitations), Inference,
  Hypothesis, Owner decision or lead. Press figures stay leads until read in the original; the
  lift-subsidy count is an example.
- **Respect use terms as data facts.** Readable is not reusable. Record each source's terms next
  to its findings.
- **Keep rough analysis honest.** Approximate address matching, undated registers and rolling
  samples establish recorded composition or reported concerns, not progression, duration, causes
  or prevalence. Use dated cohorts or repeated observations before claiming a bottleneck.
- **Audit meaning after syntax.** Issue 6's calendar-valid completion/issue pairs still had chronology
  flags; identical current and archived publisher values did not resolve their meaning. See the
  [date corroboration and sensitivity checks](topics/issue-6-building-resilience.md#age-branch-linkage-analysis-2026-10-16).
- **Clear source-defined label compatibility before a held-out run.** In issue 6's signed 2026-10-20
  run, exact headers and synthetic execution succeeded while abbreviations/annotated labels still
  excluded entire cohorts. An independent custodian must verify semantic vocabulary against publisher
  definitions before signing; unresolved categories block candidate execution. After exposure,
  repairs remain development, not a renewed independent test. Preserve the failed mapping and full
  denominator ([observed result](topics/issue-6-building-resilience.md#one-signed-external-run--results-and-disposition-2026-10-20)).
- **Separate arithmetic, model validity and policy usefulness.** Agreement between independent
  numerical solvers checks shared equations/assumptions, not equivalence to the publisher's software
  or accuracy on real buildings. A tested probability gate can fail while the calculation still runs;
  a simpler comparator does not become safety truth by default
  ([issue-6 disposition](topics/issue-6-building-resilience.md#one-signed-external-run--results-and-disposition-2026-10-20)).
- **Use a population denominator before judging a probability's level.** Issue 6's case series showed
  35% Moderate+ against a mean prior below 1%, which looked like a factor-50 error. In the Yujing census,
  with every building counted, one shared shaking level reproduced seven of eight official class
  cells within −20% to +21%. A separate level solved for each target would match by construction, so
  a reproduction needs one shared parameter. The failure lay in applying an absolute gate to a population-level
  probability, and the gap is consistent with case selection. Calibration still needs an observed
  population share of the same damage label
  ([Taiwan census check](topics/issue-6-building-resilience.md#taiwan-census-and-taipei-s1-development-check-2026-10-20)).
- **Report what survives the uncertainty, not a rank.** In issue 6, structure and older-resident
  share are nearly independent across 里, so declared weights between them would decide most of the
  list; the method combines them as one quantity with a stated meaning instead. Its structural term, a
  full capacity-spectrum chain, reduces mostly to one composition share (R² 0.82), so regress a
  composite on its simplest driver before presenting it as a multi-attribute signal. Propagate sampling
  and assumption uncertainty into the output itself, report the untested assumption switched off as a
  stress test beside the result, and resample before naming any stable set
  ([inspection priority A](topics/issue-6-building-resilience.md#inspection-priority-a-by-里-2026-10-21)).
- **Keep missingness in the denominator.** Issue 6's year-specific linkage gap would be hidden in
  a matched-only view. Show missing/conflicting groups and bounded subgroup coverage, not only successes.
- **A key is a relationship, not a real-world identity.** The same analysis found extensive
  multiple-doorplate scope. Permit links and address membership do not settle a current building or
  management boundary; they change the next source check, not eligibility or safety.
- **Let findings constrain the presentation.** Evidence groups and conditional checks can explain
  the completed analysis; a risk map, queue or new board needs its own supporting decision evidence.

### Document management lessons

- **Restructure by script.** Track every original heading to its new anchor and rewrite every
  link from that map. The 2026-10-14 split moved 2,966 lines with zero lost lines and zero
  unresolved links. A hand-written header link still needed a fix, so always run the checker
  afterwards.
- **Keep a stable reading path.** Topic HTML follows the reasoning order above, with meaningful
  headings and working anchors; source authority, synthesis and mirror have distinct roles.
- **Stamp each mirror with its source.** The footer carries the source Markdown's SHA-256.
  Recompute it after any Markdown edit made after the HTML build.
- **Replace superseded current-state text in place.** Git keeps history; a document states the
  current position once instead of appending corrections beneath stale text.

### Checks and tooling

| Check | Command | Catches |
| --- | --- | --- |
| Links and anchors | `python3 scripts/check_links.py` | Missing files, renamed headings, wrong relative depth |
| HTML gate | `python3 ~/.agents/skills/html-report-system/scripts/validate_html_report.py --portable <page>` | Report-system structure and portability |
| Analysis reconciliation | Topic's documented reproduction command and uncertainty checks | Changed source bytes, dropped groups, ambiguous keys, invalid dates and unstable definitions |
| Rendering | `uv run --no-project --with playwright python scripts/render_check.py <scratch-dir> <pages>` | Horizontal scroll at 1200 px and 390 px; then look at the screenshots |
| Source hash | `shasum -a 256 <topic>.md` against the HTML footer | Stale mirror |

**Pitfalls observed:**
- zsh does not word-split unquoted variables. `set -- $pair` left `shasum` waiting on stdin and
  hung a background job; pass files explicitly.
- Playwright's bundled browsers are absent here; `render_check.py` uses the installed Chrome.
- The web fetch tool cannot open `puma.taipei`; curl and urllib with a browser User-Agent can.
- Raw identities and downloaded source records stay outside Git; ignored `private/` is the established
  custody location for inputs required by an active analysis. Disposable scratch is removed after verification.

## Topic index

| Issue | Official prompt | Topic document | Template | Pain recorded | Reading mirror |
| --- | --- | --- | --- | --- | --- |
| 1 | 把三千棵樹種回來 | [Trees and shade equity](topics/issue-1-trees.md) (T01) | Legacy | Pending | — |
| 2 | 找回消失的垃圾桶 | [Public bins](topics/issue-2-bins.md) (T02, C07) | Legacy | Pending | — |
| 3 | 鼠患四處跑，衛生安全怎麼辦 | [Rats and source control](topics/issue-3-rats.md) (T03) | Legacy | Pending | — |
| 4 | 內湖尖峰車流好比停車場 | [Neihu peak traffic](topics/issue-4-neihu-traffic.md) (T04) | Legacy | Pending | — |
| 5 | 公車路網如何即時反應需求 | [Bus network and driver rest](topics/issue-5-buses.md) (T05) | Legacy | Pending | — |
| 6 | 危老耐震如何查，風險評級怎麼找 | [Old-building seismic resilience](topics/issue-6-building-resilience.md) (T06); [primary building method](topics/issue-6-building-rating.md); [municipal comparison and blind spots](topics/issue-6-building-resilience.md#municipal-research-comparison-and-selection-blind-spots-2026-10-22) | v1 | 2026-10-14 | [Report](topics/issue-6-building-resilience.html) |
| 7 | 自由題：你看見的市政 bug | [Free topic](topics/issue-7-free-topic.md) (T07–T10; C01, C02, C04–C06, C08) | Legacy | Pending | — |

Legacy topics hold their 2026-10-13 ten-track records; the [cross-topic records](#cross-topic-records)
below summarize them.

### Current focus — issue 6

**Owner direction (2026-10-21–22):** building-level inspection priority A is primary. Villages summarize candidate distribution; the independent village report is retired. Public-renewal B remains a limited area-assessment extension. Explore broader, finer and newer original data before fixing the case-audit scope, including the sources behind the city's own disaster grade.

**Owner clarification (2026-10-22):** retain an independent research method. Use other studies to identify missing mechanisms, coverage and measurement; admit improvements through source/decision-specific checks. Agreement with Taipei's results, geographic convergence and retaining our current candidates are not optimisation targets. Topic §5 owns the admission plan and completed five-track deepening. Source coverage/uncertainty selected the fixed-area F05 diagnostic; the completed national-2026 liquefaction source audit follows actual service currentness, not city rank.

**Current numerical result (2026-10-22):** the [building method](topics/issue-6-building-rating.md) scores 38,345 old buildings represented by historical permits, with 3,709 taller buildings unscored. The top 1% contains 385 buildings in 62 villages; the next wave contains 3,467. These lines are policy choices. Removing the national model's unvalidated mid-rise uplift retains 332 of the 385. The 65+ share is at smallest-statistical-area level and fire access at listed street stretches. One permit can represent several buildings, and surrounding population is not occupancy. The municipal liquefaction export codes are verified by the original renderer and full136-feature equivalence. Missing coverage and multi-point averaging remain calculation conventions, not low-susceptibility observations.

**Municipal comparison (2026-10-22):** original city planning/assessment sources and national Taipei research establish different decisions, hazard scenarios and populations, not a competing observed building queue. The current structural term leaves 5,929 C1M/P buildings tied at the highest structural-only median at published precision; the composite's finer choice depends partly on older-neighbourhood share and declared multipliers. The [comparison audit](topics/issue-6-building-resilience.md#municipal-research-comparison-and-selection-blind-spots-2026-10-22) prioritises objective clarity, current-stock/omission checks and admissible local shaking. It preserves the current result as a conditional investigation demonstration, without a citywide safety, casualties-prevented or superiority claim.

Taiwan evidence supports parts of the class/era ordering, not calibrated absolute probabilities or a validated Taipei candidate list. The absolute referral gate was rejected. Known findings route separately; most first-priority buildings are walk-ups, so the proactive assessment programme is one route rather than the target population. B calculates only 30 of 366 site-sized pieces under its case admission rule; coverage and suitability are unresolved.

**Current research (2026-10-22):** F01 confirmed-link refresh and disagreement tracing are complete. The [independent deepening](topics/issue-6-building-resilience.md#independent-method-deepening--source-and-linkage-results-2026-10-22) now completes a fixed-area F05 diagnostic (158 old permit records / 387 intersecting footprints, with one/many/unmatched partitions) and 110-institution care diagnostic (36 single-permit candidate rows, 13 in the tall lane). A newer nursing register reconciles to 1,101 opened beds; a separate 12-row Taipei LTC category and actual vacancy export expose source/definition gaps. These are not current building identities or occupants. Published tall-class parameters, numeric historical shaking and the new national liquefaction service are actual sources with taxonomy, code-domain, component/scenario and reuse gates. Planned width cannot measure vehicle passage. No new model input, weight or candidate universe was adopted. The [liquefaction audit](topics/issue-6-building-resilience.md#liquefaction-source-semantics-and-full-population-coverage-audit-2026-10-22) now closes municipal semantics, reproduces all25,225 L inputs and audits both raw sources over the frozen population. National NOT/year/geometry qualifications remain; no source swap is adopted. The reader-facing reports now distinguish the event organiser, independent research approximation, permit/building units, omitted stock and conditional operational routes; B stays an admitted-record case requiring coverage/site checks before suitability action. Topic §7's next action is owner-confirmed publication of these corrected existing reports. F04 standard geometry recovery and care/LTC identity remain separate. Government map agreement and retaining our list are not success; inspection benefit and civic outcomes remain unverified. Agency replies are later validation routes. The [paired missing-input stress](topics/issue-6-building-resilience.md#missing-liquefaction-input-stress-test-2026-10-22) is also complete: assigning only uncovered points the highest increment retains384/385 current first-priority棟 (388 selected after full ties), while top10% retains3,793/3,852 (3,840 selected). Current uplift-off remains332/385; joint upper-input uplift-off retains328/388. This is one common hypothetical assignment, not all missing-value patterns or record-bootstrap robustness; current scores/list remain unchanged.

## Cross-topic records

### Cross-topic decision comparison

**Inference — after all ten investigations (2026-10-13):** the same minimum problem record is
complete for 25 distinct workflows, with explicit hypotheses where public evidence cannot validate
a user need. Evidence depth is unequal: full-file technical checks are stronger for entrances,
scenarios, transfer rentals and the childcare roster; lived/practitioner evidence is mostly
historical, self-selected, operator-reported or geographically limited. No interviews or observed
practitioner comparisons occurred, and no workflow has a demonstrated decision gain. Unknown value
is not low merit; the free topic is a container, not an extra candidate competing with its children.

The comparison did not select a topic. The owner later directed the research to issue 6, and the
2026-10-13 cross-topic recommendations are not reopened. For any track, operational adoption still
requires a named custodian, existing-process comparison, lawful evidence access, expertise and
available capacity; 100-day staff/procurement/maintenance costs are unknown.

### Next-investigation queue

This ten-track queue is neither a launch queue nor a priority ranking; it records each track's
disposition and the one bounded public-source check that would resume it. Legacy tracks are deferred
by owner focus. No implementation, participation or contact is authorized by this table.

| Track | Possible actionable contribution | Decisive limits and existing baseline | Disposition | Resume check |
| --- | --- | --- | --- | --- |
| T01 Trees / C03 | Planting field review; officer entrance exceptions; caregiver confirmation | Shared entrance errors; no continuous trip or plantability evidence; existing tree/Wheelroute/park tools; utilities, survey and repair capacity may bind | Narrow inspection/checklist; defer shade/routing recommendations | Compare named-street history and the two anomalous entrance plans; preserve missing connections |
| T02 Bins / C07 | Verify/repair/siting review; overflow response; market boundary referral | Same lookup data, stale venue, no public synchronized load/crew series; existing lookup and sensor trial | Narrow placement/C07 verification; defer real collection optimization | Inspect the current replacement SOP and published sensor-trial results before more mapping |
| T03 Rats | Correct referral; observed-condition owner and reinspection | No local linked public inspection/action/outcome chain; 1999, Rat Radar and professional diagnosis exist; access/repair responsibility can dominate | Defer duplicate intake; investigate inspection/ownership/recheck | Find a current public joint-inspection/recheck form and test condition→owner→completion linkage |
| T04 Neihu | Employer feasible trial; city expansion evaluation | Feeds/history geographically incomplete; treatment attribution unavailable; existing TUIC/DOT/employer coordination; care obligations and through traffic rival timing | Retain trial/evaluation hypotheses; no optimal clock or causal savings | Inspect the named-city-detector historical catalog, retention and exact reuse terms; stop at auth/payment |
| T05 Buses | Service evidence request; changed actual-duty review | No stop/time demand or authorized present duty/facility record; approval/OMS/reservation systems exist; staffing and facilities may dominate | Narrow service/duty evidence reviews; defer operational redesign | Trace the Blue27 reduction rationale and the current TTSB actual-duty monitoring response |
| T06 Buildings | Building-level inspection priority A; limited public-renewal B extension | Historical permits are not current buildings; structural uplift and selection gain unvalidated | Current focus ([above](#current-focus--issue-6)) | F01 disagreements resolved; municipal comparison identifies objective, missing-stock and local-shaking limits. Five-track source/linkage tests completed. Liquefaction semantics/coverage audit completed; missing-input stress also completed (384/385 retained, 388 after ties); lay-page source, scoring-unit, unknown/mixed/regional and follow-up explanations reconciled, preserving current scores; public push awaits owner confirmation. No independent village rerun; agency requests remain separate |
| T07 / C01 | One review question for an already shortlisted site | Event/victim/exposure semantics incomplete; national hotspot tool and official packets exist; engineering agreement/capacity may dominate | Narrow next site-review question; generic hotspot gap refuted | Inspect the Gongguan micro-adjustment review record for boundary, rationale and rejection reasons |
| T08 / C02, C06 | Meal audit and resident confirmation; parent reconciliation and planning investigation | No acceptance/vacancy/deduplicated demand; existing maps/admissions/professionals; premises, staff, cost and hours compete with information | Narrow meal/access and parent reconciliation; defer shortage/vacancy claims | Find the completed district childcare demand analysis requested in 2025 and inspect sample/deduplication/acceptable service |
| T09 / C04, C05 | Publication discrepancy confirmation; facility preparedness follow-up | Authoritative meaning unresolved; invalid geometry and missing entrance/floor evidence; existing inventories/EOC GIS/coordination | Manual discrepancy review; real facility-scenario demo blocked | Compare the two 螢橋 school references with the latest Zhongzheng flood maps and revision dates |
| T10 MRT / C08 | Metro observation request; historical transfer question; current provisional station choice | Coarse old subset, ambiguous identities, contrary compliance; capable current tools; fleet/staffing/space may dominate | Retain metro review; historical subset and current lookup separate | Extract line-specific waiting results for one review case; keep the historical station and lookup checks in their workflow records |

Every workflow retains its own resolution/resume condition in its topic record. Practitioner
effort/acceptance tests require separately authorized participation; absent public records do not
prove agencies lack them or people do not experience difficulty. Do not substitute invented labels,
arbitrary buffers or weighted scores for unresolved evidence.

### Problem fit and separate readiness of the expanded candidates

**Canonical judgment:** this section owns readiness for the official themes and the expanded
candidates, separated into 27 workflows: the 2026-10-13 deep run covered 25, and the later
owner-requested issue-6 allocation reframing added 2 explicit, unvalidated hypotheses (A and B).
`specified` is a written bounded demo proposal, including disclosed hypothetical inputs where noted;
it does not establish a production application or participant test. Every row has
**decision=insufficient** for its operational action and **target civic outcome=unknown**. Completed
source/schema comparisons and descriptive calculations are supported only within their stated scope
and do not satisfy the baseline decision-gain requirement.

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
| T06 municipal inspection allocation (A) | unassessed | Building-level development result: 385 first-priority buildings in 62 villages; uplift-off stress test retains 332/385. Municipal comparison finds a coarse structural class term, older-share objective dependence, omitted/unverified stock and unmatched local shaking; no actual inspection queue or gain established. F01 disagreements resolved. Five-track source/linkage tests completed; liquefaction semantics/coverage audit completed; old export meaning verified, no-data/mixed inputs and national geometry/NOT retained. Paired missing-input stress retains384/385 current first-priority棟 (388 after ties), with current uplift-off332/385. Reader explanations now distinguish source attribution, scoring unit, missingness, research-model scope and conditional routes. B is a sparse admitted-record comparison, not an operational priority; owner-confirmed publication is next. See [comparison](topics/issue-6-building-resilience.md#municipal-research-comparison-and-selection-blind-spots-2026-10-22) and [companion](topics/issue-6-building-rating.md). The historical app is not a validated deployment |
| T06 public-renewal review priority (B) | unassessed | One research case (topic §5, 2026-10-21): 469 designated renewal-area pieces (the 更新地區 a 7599 site must lie in); public records order 30 of the 366 pieces of at least 2,000 m², so the first action for 336 is a request for building-level records (city tax registry). One band-1 piece in the 2026 民生社區 designation, also in the uplift-off stress test; its M04 suitability record mostly lacks willingness, finance and ownership. Listed (575) and existing-project lanes kept. No inherited A order, comparable project pool or observed project-selection gain |
| T06 assessment preparation | specified | Paused T06-A: existing pack covers tested branches; fictional teaching, no measured service gain |
| T06 retrofit/renewal feasibility | specified | Paused T06-B: professional/programme boundaries and household burden known; no paired same-case cost/performance or validated new-tool benefit. Execution limits remain separate from structural-risk weights |
| T06 opt-in outreach | specified | Paused T06-C: existing services, unknown incremental intake gain and capacity |
| T06-D route finder for a blocked walk-up | unassessed | Paused: FAQ already contains routes; ownership, applicable consent and benefit unresolved. No safety penalty for coordination difficulty |
| T06 stall board (follow-up demonstration) | specified | Paused. R04 historical four-community/five-row account and R08 scope include strengthening; R09 is not an adopted full formula. No linked live cohort, causal bottleneck or reader/operator gain. Not the municipal model target |
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
Each topic record owns its completed comparison, difficult cases, supported/refuted/unresolved exit,
operator/authority/cost unknowns and next check; the queue owns the topic-level next action. Neither
table selects a topic.

### Dataset-to-candidate index

This is a navigation index, not a second source audit. The linked record owns exact publisher and
resource URLs, retrieval method, period, fields, license and limitations. National and `tp-` aliases
are the same dependency when they resolve to the same publisher resource.

Candidate IDs C01–C08 are the eight expanded free-topic hypotheses from the 2026-10-13
Twinkle-assisted discovery, not organizer issue numbers:
[C01 collision-site review](topics/issue-7-free-topic.md#c01-collision-site-review),
[C02 senior-meal inventory](topics/issue-7-free-topic.md#c02-senior-meal-service-inventory),
[C03 accessible park entries](topics/issue-1-trees.md#c03-accessible-park-entry-comparison),
[C04 shelter preparedness](topics/issue-7-free-topic.md#c04-village-shelter-preparedness),
[C05 rainfall-scenario review](topics/issue-7-free-topic.md#c05-rainfall-scenario-facility-review),
[C06 childcare evidence](topics/issue-7-free-topic.md#c06-childcare-evidence-shortlist),
[C07 market-bin audit](topics/issue-1-trees.md#c07-market-bin-service-audit) and
[C08 YouBike patterns](topics/issue-7-free-topic.md#c08-youbike-transfer-patterns-and-current-availability).
Search-only leads (bicycle lanes, bridge access, bicycle parking) stay in the transport track and
must not silently become essential inputs. No observation below establishes all-city completeness
or an operationally reliable live service.

| Dataset identity | Candidate use | Observed evidence state / unresolved dependency | Detailed owner |
| --- | --- | --- | --- |
| K01–K06 professional/repair rules; S08 operator cases | T06 professional evidence review and supporting follow-through | Current methods, representation/qualification and five-condition-count funding rule verified; current repair list does not explicitly include structural strengthening. K06 main text and Annex 7 checked against a government-hosted PDF; no actual applicant cohort, current building grade or paired engineering option inputs. R04 is a different programme | [Professional audit](topics/issue-6-building-resilience.md#professional-practice-and-assessment-to-action-audit-2026-10-16) |
| `130110` / `tp-00001025` collision records | C01 essential | T07 full 2025 aggregate audit; first-party extract, no event ID; current form does not resolve export 2–30-day-death semantics | [T07](topics/issue-7-free-topic.md#t07-c01-collision-site-review) |
| `137993` YouBike current inventory | C08 current lookup | T10 later 1,819-station snapshot; active/inactive and campus category separated; no arrival guarantee; capacity differs from bike+slot sums | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `169174` transfer rentals | C08 historical | Full December census completed; all 31 borrow dates, hour-rounded times, 858 identical-row excess and 543 unmatched current names; completeness/identity still unresolved | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `135775` monthly YouBike total | C08 context only | MCP sample and publisher schema; no station dimension | [Transport audit](topics/issue-7-free-topic.md#exact-new-dependencies-and-observed-access) |
| `152266` park entrances | C03 officer/caregiver | T01 745-ID match with Wheelroute, identical width/slope and shared two gross location anomalies; source agreement is not independent validation | [T01](topics/issue-1-trees.md#t01-trees-shade-and-accessible-park-use) |
| `128414` / `tp-00001516` MRT accessible entrances | C03 essential | Full CSV parsed; network extends beyond Taipei, no downtime or shared entrance ID | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| `126553` garbage/compost collection totals | C07 context only | Full CSV parsed; no district/team dimension despite title | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| National catalog `121593` markets | C07 essential | Direct publisher discovery/full CSV; not independently discovered through MCP, no all-food-business coverage | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| Wheelroute `2b58f15a…` | C03 baseline/potential | 940 API records; 745 park measurements match, remaining 195 sentinel-like; separate 193-row MRT inventory not reconciled; units/topology/current conditions unresolved | [T01](topics/issue-1-trees.md#t01-trees-shade-and-accessible-park-use) |
| `135495` meal list; current 115.08 PDF/operator schedules | C02 planning/access | 440-row descriptive ratio preserved; ten source correspondences checked; age-60 eligibility differs from age-65 denominator; schedules exist, activity/capacity/acceptance unknown | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `121337` public childcare | C06 | Old count source differs from dated September roster; 29 public centers not the full supply system; no offered vacancy | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `121278` private childcare | C06 | Earlier 223 rows retained; dated full registry distinguishes service categories/periods; legal identity joins require review | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `156685` assessment CSV; 115/2026 PDF | C06 parent evidence | 292-row CSV ends 2025; newer PDF and map disagree in inspected case; law/footer cycle conflict retained; missing assessment is not failure | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `135696` childcare enrollment | C06 context only | Full semiannual citywide series; no local/center vacancy inference | [Care-service audit](topics/issue-7-free-topic.md#evidence--retrieved-2026-10-13) |
| `121550` / `tp-00000862` rainfall scenarios | C05 | All three KMLs fully parsed; 1,945/7,330/29,738 polygons, 9/57/287 invalid under stated GEOS; modeled inputs, no validated facility join | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `135484` / `tp-00003479` welfare shelters | C04 | Older 399-row source retained; T09 exact district+name joins differ from earlier recipe; scope/authority unresolved | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `134683` / `tp-00002066` education shelters | C04/C05 | 419 IDs/418 names; website ODS and April 2026 plan compared; two school conflicts, shared capacities and authoritative semantics unresolved | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `tp-00003001` flood facilities; `tp-00003003` flood works | C04/C05 context leads | Catalogs inspected only; resource rows not read, annual aggregates cannot prove local protection | [Flood audit](topics/issue-7-free-topic.md#evidence-additional-dataset-inventory) |
| Existing village/district age population (`a6394e3f…`) | C02 essential; C04/C06 potential | Full source parsed earlier; C02 twelve-district join checked, village joins unvalidated | [Organizer population audit](topics/issue-6-building-resilience.md#organizer-starter-dataset-pages-2026-10-13) |
| Existing bin inventory `121355` | C07/T02 | T02 lookup equals 681-row CSV; nonnumeric longitude, aggregate/duplicate sites; market point may be stale | [T02](topics/issue-2-bins.md#t02-public-bins-and-c07-market-bin-responsibility-audit) |
| Existing trees, pits and sidewalk geometry | C03 optional context | Full inventory/geometry checks earlier; stale surveys/duplicates, no measured shade or connected path | [Organizer tree audit](topics/issue-1-trees.md#trees-and-shade-four-dataset-pages) |
| T04 city v2 VD/static; annual survey 128230; NFB archive | Official Neihu | Current public readings and historical local/upstream samples verified; exact city-v2/station-workbook rights and complete corridor history unresolved; NFB >40 s request spacing | [T04](topics/issue-4-neihu-traffic.md#t04-official-neihu-traffic-timing-requires-an-executable-employer-decision) |
| T05 2025 route statistics / OMS-duty evidence | Official buses | Route-level context and one TTSB actual-duty case; stop/time demand, current private duty and rest facilities absent | [T05](topics/issue-5-buses.md#t05-official-buses-service-decisions-and-executable-driver-rest) |
| T06 building `7889e8a0`; soil `ec40e067`; professional packs | Official buildings | Full city-aggregate parse; a later primer parsed 136 liquefaction polygons and refreshed population/fire file shapes; the allocation audit found 2 invalid polygons and building-count arithmetic differences, while population totals passed bounded consistency checks. Current building-level coverage and independent accuracy unknown; no individual safety inference from these aggregates | [T06](topics/issue-6-building-resilience.md#issue-6--old-building-seismic-resilience) |
| T06 D01–D12: organisation 132391, scoped no-committee PDF, archived raw permits, GFZ/GEM/academic/GIS sources | Official buildings (core model input audit) | 2026-10-15/16 full CSV/PDF/XML checks: 9,713 organisation rows / 9,657 IDs, 5,489 scoped permit IDs, 3 unresolved intersections; 5,441 archive links / 4,130 conservative historical attribute records. Missingness is structured, date anomalies persist in the current publisher subset, current scope/survival unresolved | [T06 feasibility audit](topics/issue-6-building-resilience.md#broad-discovery-and-real-input-feasibility-audit-2026-10-15) |
| T06 V01–V05: address positions, cadastral I3S, NLSC supply, community geometry and TGOS | Official buildings (model spatial-unit evidence) | Full V01 CSV: 1,157,763 rows; unique/ambiguous/unmatched = 3,898/3/1,588. Adopted EPSG:3826 qualified; V02 node sample gives 16 diagnostic links. Geometry/identity/coverage constrain overlays; app and 3D expansion are paused | [Spatial audit](topics/issue-6-building-resilience.md#spatial-evidence--location-geometry-and-model-units) |
| T06 W01–W03: FEMA P-154/P-155; OECD/JRC composite indicators | Official buildings (core method/weights) | Originals checked 2026-10-16: instrument-specific score applicability, normative weighting, overlap, compensation and sensitivity. No Taipei coefficients or transferable US cutoff established | [Weighting-method audit](topics/issue-6-building-resilience.md#weighted-model-method-audit-2026-10-16) |
| T06 identity B01–B07: use permits 128203, permit map 151936, doorplates 155472, MOI transactions, sea-sand register PDF | Official buildings (allocation A) | 2026-10-14 full parses; construction-permit join verified (99.5% floor agreement) for 2001+ use permits; transactions give completion/material/floors for 9.8% of address keys; full sea-sand register only as PDF. Pre-1996 inventory and independent accuracy unresolved | [T06 identity audit](topics/issue-6-building-resilience.md#building-identity-audit--public-chains-cover-new-buildings-not-the-old-building-universe) |
| T06 deep investigation: Revenue Service 132020 district buildings; MOI pip T13/T15/T16 units; NLSC 3D model; restricted tax/land registers | Official buildings (allocation A/B) | 2026-10-14 full parses of district files (reconciled totals); aggregate old-stock tables verified; D03 later supplies public historical permit attributes. No complete current old-stock universe or public village/grid inventory verified | [T06 deep investigation](topics/issue-6-building-resilience.md#source-ledger--deep-investigation-retrieved-2026-10-14) |
| T06 G01–G30 / D13: scientific models, shaking sources, local and foreign damage cohorts and source-field audit | Official buildings (structural component and method comparison) | Actual NCREE shared 216-row export; reproduced label/coverage/algebra audit; Tgbs manual, GEM 139 Taiwan loss functions and global originals inspected. 2026-10-20: private approximation, independent numerical checks and one frozen five-cohort run (Nepal primary gate 81/81 misses, no ranking gain; Ecuador/Pohang/Bolu mapping-limited, Mexico prior-uncomputable). G06 Yujing census reproduces the official class output at one shaking level (development). G29/G30 village/ground-failure inputs audited; G30 municipal codes and complete export equivalence verified2026-10-22, with full source/unknown/geometry coverage checks. D03 location bias explicit. No fitting, official-equivalence or Taipei validity established | [Scientific audit](topics/issue-6-building-resilience.md#global-scientific-method-and-case-data-audit-2026-10-16); [2026-10-20 audit](topics/issue-6-building-resilience.md#method-shaking-and-cohort-admission-audit-2026-10-20); [liquefaction audit](topics/issue-6-building-resilience.md#liquefaction-source-semantics-and-full-population-coverage-audit-2026-10-22) |
| T06 A inputs (2026-10-21): Fire Department 搶救不易狹小巷道清冊 42289 (NCHC mirror, 2020 snapshot); B01 128203 reused for supersession; DBAS 132952 use permits by structure | Official buildings (allocation A) | 267 lanes, 248 placed on 143 里 by doorplate range, 19 unresolved; 12% of located D03 records superseded by a later new build; D03 holds 300/512 permits for ROC 81 and 2,447/5,529 for ROC 57, otherwise complete for ROC 63–94; `51.xml` duplicates `52.xml`. Narrow-lane currentness after 2020 unverified | [Inspection priority A](topics/issue-6-building-resilience.md#inspection-priority-a-by-里-2026-10-21) |
| T06 municipal M01–M07: inspection programme, renewal rules, weighted designation and case | Official buildings (core A/B baseline) | Planned 50-case programme; M04 project suitability; M05 actual weighted area overlays followed by boundary/staging adjustments, not individual seismic weights. Current queue and comparative gain unknown | [Municipal baseline](topics/issue-6-building-resilience.md#municipal-allocation-baseline--bounded-refresh-2026-10-14) |
| T06 action evidence R01–R09: current Taipei extension notices/forms, 2023 pilot report, contemporary 2022 plan/551st minutes, 2024 commissioned strategy, results and progress portals | Official buildings follow-through / supporting stall explanation | Four-community phase / five scope rows visually verified; distinct barriers and existing accompaniment. R04/R08 expressly include strengthening; R09 records suggestions and a report accepted for record, not a full adopted ranking formula. No live extension cohort; cumulative totals cannot establish stalls | [Scope audit](topics/issue-6-building-resilience.md#r04-contemporary-programme-scope-check-2026-10-16) |
| T06 funnel M08–M10: CMO proactive flow annex; UDD 2022–2024 accounts; UDD council reports 2026-04/07 | Official buildings (A, T06-B) | 2026-10-15 full-text reads: solicit→consent→assign; annual reports describe 50 completions; oversubscription unobserved; owner-initiated approvals 82–200 a year; retrofit design applications single digits; 403/575 progress. No case identities, refusals or pools | [T06 funnel](topics/issue-6-building-resilience.md#municipal-allocation-baseline--bounded-refresh-2026-10-14) |
| T06 owner situations M11–M14: CMO 危老 FAQ; 土地登記規則 §24-1 and MOI transcript rules; 公寓大廈管理條例 and MOI at-risk criteria; 民法 §1101 | Official buildings (A follow-through, T06-B, T06-D) | 2026-10-15 full reads: class-3 transcript routes differ by route; the management organisation gates proactive assessment, retrofit application and owner contact; guardianship and access levers. No count beyond the inheritance listing | [T06 owner reachability](topics/issue-6-building-resilience.md#owner-reachability-and-standing--the-second-stall-2026-10-15) |
| T06 pain tree: statutes D0070249/D0070008/D0070118; CMO promoter register 115.10.1; CMO through-2003 no-committee list 115.07.17 (organisation status not established); CMO 危老問答集 B; elevator FAQ | Official buildings (T06-D, coordination, 人老 branch) | 2026-10-14 statute reads and full PDF parses: 3,698 promoter filings (3,182 initial, 22 detailed, 492 plan, 2 unparsed; median 4 households); undated snapshot, not conversion; 5,489 listed use permits. Addresses and names not retained in Git; no reuse licence stated | [T06 pain tree](topics/issue-6-building-resilience.md#2-pain-tree) |
| T03 food `9431f450` / pipe `af1e6e42` / complaint `cb423c17` / current ODT | Official rats | Full fields rechecked; no spatial outcome/repair chain. No-committee consent route verified; third-party reports require rights/privacy review | [T03](topics/issue-3-rats.md#t03-official-rats-intake-versus-inspectable-source-control) |
| T08 dated September 2026 full registry; 147154; baby-map layer 6 | C06 | 314 serials, approved/actual/hours/fees/type; older 215-row CSV has no row dates. Map/API rights unknown; actual enrollment is not offered vacancy | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| 166491 / 174976 availability categories; 166492 aggregated OD | C08 | Full June 2026 catalog-labeled resources; category boundary/period conflicts, no numeric hourly rates or unmet demand; LineString not cycling route | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| MRT `63f31c7e` / 2025 survey/performance | Retained MRT | Index/schema, waiting recommendation and contrary compliance; no full OD-month or platform/service-constraint validation | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| F01–F08 (2026-10-22 original-source discovery) | T06 inspection A; F06 separate known-condition route | F01 scoring complete (1,193 confirmed / 580 possible-only scored buildings after rounding recovery), F05 fixed-area and 110-institution care diagnostics completed, without numerical adoption; F04 finest geometry/currentness unresolved; F07 adopted input unchanged, F08 snapshot rejected. Liquefaction source/coverage audit completed; municipal codes verified and national NOT/year/geometry qualifications retained, no scoring adoption. Paired missing-input stress retains384/385 current first-priority棟 under one joint assumption; no global-bound/robustness claim. F01 is a text/key link used in a conditional score, not observed access | [Building-first audit](topics/issue-6-building-resilience.md#building-first-source-discovery-2026-10-22); [deepening](topics/issue-6-building-resilience.md#independent-method-deepening--source-and-linkage-results-2026-10-22) |

## Publisher dataset audit

**Evidence — retrieved 2026-10-13:** the organizer supplies 26 government dataset link
occurrences, representing **22 distinct dataset pages** (4 on data.gov.tw and 18 on data.taipei).
Every distinct page was read with curl, but one traffic catalog is withdrawn. Food-business data is
one citywide total, public complaint categories contain no coordinates, the listed bus-stop file is
from 2021, and the water-level dataset is only station locations. Tree exports contain older surveys
and duplicate holes. The legacy recovered VD feed contains a 2024 timestamp; a later full read of
the separate v2 feed establishes current public access, with historical retention unresolved. MRT
offers 116 monthly index entries through August 2026; the latest monthly CSV was sampled. An
independent readback reproduced the food CSV's single citywide row, the tree-hole counts (2,259 rows
/ 1,308 IDs / 1,758 unique objects), the MRT index and latest-month header, and the stale VD XML; a
second rain read returned 42 stations and an anomalous station-025 timestamp (`206104101530`).
Per-dataset records live in the owning topic documents.

Method: extract organizer anchors; read publisher HTML and metadata; follow actual download links
and pointer CSVs to their sources; request the first 262,144 bytes with HTTP Range where supported
and parse full responses when servers ignored Range. Tree inventories and the bus shape GZIP were
read in full. Public endpoints only, without account login or purchase; no raw records,
credentials, restricted complaints or personal information were retained in Git. A browser-index
read of the bus-stop page returned 503 once while the direct page and ZIP returned 200; Python's
default TLS library rejected the Taipei portal certificate chain while curl succeeded. These are
client-specific observations. Counts describe this retrieval, not guaranteed future totals; metadata
dates are **catalog dates** unless labeled file, survey, record or coverage. HTTP 200 is an access
check, not a usable-data verdict: inspect content type, actual columns, records and observation
dates.

Reproduction: decode CSV using the response charset (Big5 where labeled) and count nonempty data
rows with a quoted-field-aware reader, without the header. JSON counts use array length or
FeatureCollection `features` length; tree uniqueness uses TreeID, hole uniqueness uses TreeHoleID
and serialized whole-object equality. The bus shape response is a root JSON array (T05 re-read),
while ETA retains `BusInfo`; continuity with the earlier read is unverified. The bus SHP ZIP record
count uses the DBF header, not validated geometry. Date bounds are lexical bounds of fixed-width
strings, with blanks reported separately; invalid-looking survey dates are suspected placeholders
not confirmed with the publisher.

### Supplementary platforms and organizer-only inputs

Retrieved **2026-10-13**, separately from the dataset-ID audit.

| Source | Observed access | Restrictions and consequence |
| --- | --- | --- |
| [Organizer citizen feedback](https://puma.taipei/hackathon#issues) | Release announced as forthcoming; no resource inspected | Activity-only; schema, volume, dates and spatial precision unknown. A feedback-driven tool stays a hypothesis until released and inspected |
| [Tree/streetlight information website](https://geopkl.gov.taipei/) | curl 200; public tree-movement-history search interface | Query website, not a demonstrated bulk export or license; supports manual validation of a few tree records, not complete annual removal causes |
| [TDX API guide](https://tdx.transportdata.tw/api-service/swagger) and [homepage](https://tdx.transportdata.tw/) | Guide describes basic, advanced and historical service families; guest access is browser-only basic service, at most 20 requests per source IP/day; member access needs Client ID/Secret; homepage describes a basic-member monthly allowance of 3 points | No account or authenticated query used. Static topology, live snapshots and historical series are three dependencies; historical availability, retention, charges and license unverified |
| [Rat Radar reports](https://ratdar.taipei/reports), [CSV export](https://ratdar.taipei/reports/export), [transparency page](https://ratdar.taipei/transparency) | CSV parsed **1,429 rows** (report time, type, location, status, description, photo URL, coordinates), 2026-05-01 13:20 to 2026-10-13 08:11; 1,410 rat and 19 bait reports; 1,373 reviewed, 3 reported to 1999, 53 pending | Mixed cities and types; reviewed is not confirmed infestation; no explicit reuse license seen; text/photos may identify people, so no raw reports retained. Reported sightings only, not prevalence, subject to permission and privacy review |
| [Old night-market entry](https://foodtracer.taipei.gov.tw/Front/Nightmarket), [move notice](https://foodtracer.taipei.gov.tw/), [new entry](https://foodtracer.health.gov.taipei/Front/Nightmarket) | Old URL fails certificate validation; new host returned a maintenance page; [catalog 62075](https://data.nat.gov.tw/dataset/62075) describes 14 night markets (indexed description only) | No live vendor table or API read; not a geocoded inventory of all restaurants or a rat-risk label |
| [Taipei liquefaction portal](https://soil.taipei/) and [official Q&A](https://soil.taipei/Taipei2019/Main/pages/QA_handle.html) | Root refreshes to the [current landing page](https://soil.taipei/Taipei2019/Main/pages/index.html); curl reads the public query information | The Q&A states the medium-resolution city map cannot determine liquefaction at an individual building site. Area-level context and referral only; no bulk download rights inferred |
| [Education Department check portal](https://www.doe.gov.taipei/News_Link.aspx?n=9E714C7EB1702778&sms=10FAB7D5E5149055) | curl 200; an index linking personnel announcements, kindergarten public/building inspections and other checks | Not a normalized dataset or complete registry; no personnel records ingested. Unsuitable as a default personal-data aggregation project |
| [Taipei data catalog](https://data.taipei) | General discovery entry point | Audit an exact dataset/resource rather than citing the catalog as evidence of access |

**Inference:** the organizer's data list is a starting bibliography, not a ready-made analytical
dataset. Website availability, machine-readable availability, permission to reuse, and fitness for a
particular decision are four independent checks.

### License and interpretation

**Evidence:** all four national catalog pages explicitly name Government Open Data License v1.
The 18 Taipei pages say `公開` (public), free, and link the platform's
[Government Open Data License v1](https://data.taipei/rule). That policy permits reuse and derived
services without individual written permission, subject to attribution. Preserve publisher,
release title/version and year; link the license. Platform openness does not erase third-party
rights or establish that a separate event-only complaint feed is open data. No separate resource
license override was observed in the sampled pages. Recheck terms when freezing a project source.

Resource labels in the topic inventories use “Download CSV/asset” for exact public URLs of the form
`https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=<rid>`.
Older national-catalog links sometimes use `/api/dataset/<dataset>/resource/<rid>/download`;
those exact links were also tested successfully. `200/full` means the response ignored the
requested Range or the file was deliberately read in full; `206/sample` means a byte-range sample.

### Cross-dataset validation still required

**Open question — organizer-starter scope:** the most consequential unresolved joins are current
bus StopID vs 2021 SHP IDs, sewage pipes vs sewage manhole geometry, village population vs village
boundaries, and tree positions vs sidewalk polygons after EPSG:3826 reprojection. Before committing
to a workflow, audit the full selected time slice for missing/duplicate records, coordinate extent,
ID join rate and date semantics, and obtain publisher field documentation for units, risk-class
legend and current bus-stop mappings. Complete-month MRT validation, operational ground truth and
any authenticated TDX access remain outside the verified results. Keep measured quantities separate
from proxies: MRT riders are not street pedestrians; complaints are not prevalence; tree positions
are not shade; equipment locations are not readings; citywide building age is not individual
structural risk. No inaccessible source is silently replaced with simulated observations.

## Taiwan open-data discovery provenance

### Twinkle provenance and role in this project

**Owner decisions — 2026-10-13:** use Twinkle to discover data beyond the organizer list; four
tracks (transport, flood preparedness, street environment, everyday care services) produced the
C01–C08 hypotheses, with selected original resources verified before integration. The owner also
requested a Taiwan open-data MCP configured at repository scope; this authorized research-tool
configuration, not a contest application or paid subscription.

**Evidence — official service pages re-read 2026-10-13:** the
[provider's Taiwan source inventory](https://hub.twinkleai.tw/zh-TW/data/country/tw) distinguishes
central-government catalog material, government websites not necessarily indexed centrally,
community sources, and provider-derived content. Its source/coverage counts are provider claims,
not independently enumerated facts in this project.

| Source class | What is established / example | Project handling |
| --- | --- | --- |
| Government original | Tree data 128274 has direct publisher CSV/JSON/XML; government datasets also exist outside data.gov.tw | Use MCP for discovery, then pin the exact original resource/version for analysis |
| Government material collected/normalized by Twinkle | Local catalogs, procurement and tourism sources are listed by the provider; the MCP may supply a cached/normalized copy | Verify what was transformed, the observation period, update delay and coverage; provider processing dates are not source observation dates |
| Community content | Provider lists Taiwan.md and community-maintained event information | Label the actual publisher; do not describe it as government data or assume government terms |
| Provider-derived content | Provider identifies its IVOD speech-to-text output as AI transcription, not an official record | Distinguish source video from derived transcript and inspect the specific license; no derivative transcript was used in the eight candidate analyses |

**Evidence — contribution and caveats (2026-10-13):** Twinkle discovered datasets outside the
organizer list and returned metadata and samples; structured row reads work through `execute_tool`
with `select`, `filters`, `aggregate`, `group_by`, `order_by` and `limit`, after older column-based
`tw_query_rows` calls were rejected as `QUERY_NOT_ALLOWED`. No top-up or purchase occurred.
Normalization date is not observation date; metadata join hints may name absent columns; a
live-named YouBike mirror was hours behind its publisher; the two shelter inventories have different
agencies/versions/rows and 37 flood-flag differences among 386 name-matched current rows, which does
not prove 37 real-world eligibility changes. No extra catalog creates missing canopy, pedestrian
exposure, rodent outcomes, bus passenger demand or real-time shelter occupancy.

The [license page](https://hub.twinkleai.tw/zh-TW/licenses) describes passing through source terms;
this is a provider statement, not a blanket license for every payload. The exact dataset/resource
and rights-holder terms control the dependency. The
[Skills page](https://hub.twinkleai.tw/zh-TW/skills) said its old packs were withdrawn while being
rewritten, with MCP unaffected; no Twinkle skill was installed. Source facts, transformations and
solution conclusions must remain separately attributable.
