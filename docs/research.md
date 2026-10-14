# Research Master — Method, Event Facts and Topic Index

## Scope

Research for [市政 debug松](https://puma.taipei/hackathon), started on 2026-10-13: investigate the
official issues and self-chosen civic problems from evidenced pain, verify public evidence and data,
and prepare an informed topic decision. The research does not imply a product build.

## Reading guide and evidence date

This master and the topic documents under `topics/` together form the research authority. The
master owns method, event facts and cross-topic records; each topic document owns its issue (see
the [topic document standard](#topic-document-standard)). Source observations were retrieved on **2026-10-13** unless a section states a later date (the T06 identity audit is 2026-10-14);
the ten-track deep run below re-read only its named sources and adds current source comparisons. Older audits retain their original scope; a retrieval does not establish current operating conditions. Git retains superseded recommendations. No separate
agent report or competing candidate document is needed.

| Reading goal | Current section |
| --- | --- |
| Understand the organizer's problems and scope | [Official pain points](#official-pain-points-and-decision-fit) |
| Understand how candidates are judged | [Research umbrella policy](#research-umbrella-policy) |
| Open one issue's research, or write a new topic document | [Topic index](#topic-index); [topic document standard](#topic-document-standard); [topic research playbook](#topic-research-playbook) |
| Compare all ten tracks and their separate decisions | [Current comparison](#cross-topic-decision-comparison); [historical eight-candidate comparison](#synthesis-and-recommended-order) |
| Check what is ready and what would reject a proposal | [Canonical readiness record](#problem-fit-and-separate-readiness-of-the-expanded-candidates) |
| Find additional dependencies and their verification state | [Dataset-to-candidate index](#dataset-to-candidate-index) |
| Reproduce the completed numerical comparison | [Meal-list analysis recipe](topics/issue-7-free-topic.md#reproducing-the-meal-list-comparison) |
| Inspect exact schemas, URLs, counts, licenses and failures | [Transport](topics/issue-7-free-topic.md#additional-transport-evidence-collision-review-and-youbike-transfers), [street environment](topics/issue-1-trees.md#environment-parks-and-street-service-track--outside-organizer-starters), [care services](topics/issue-7-free-topic.md#additional-theme-everyday-care-service-access), [flood preparedness](topics/issue-7-free-topic.md#flood-preparedness-twinkle-discovery-plus-original-publisher-audit), [organizer audit](#publisher-dataset-audit) |
| Read the completed problem-first investigations | [Topic index](#topic-index) (ten-track records live in the topic documents) |
| Resume work without redoing discovery | [Next-investigation queue](#next-investigation-queue) |
| Understand the Twinkle Hub discovery route | [Twinkle provenance](#twinkle-provenance-and-role-in-this-project) |

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

**Current limit:** ten tracks now have problem/baseline and bounded rejection findings; operational decision gain is still unvalidated. Follow the current comparison/queue before choosing a contest topic. No implementation or organizer contact occurred; no raw citizen
reports or personal information were retained in Git.

## Official baseline

**Evidence — retrieved and independently re-read during the deep run on 2026-10-13:** the [official event page](https://puma.taipei/hackathon)
announces 市政 debug松, organized by 沈伯洋競選辦公室. Registration closes October 18 at 23:59 (superseded 2026-10-14, see below);
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

**Evidence — live page re-read 2026-10-14 11:51 Taipei:** curl GET of the same page (51,055 bytes,
SHA-256 `d01038835138132b910f80115e2e9ecfa1a20a913bb4cfc471d528aa98eeb7b4`), HTMLParser text
extraction. Registration now closes early, **2026-10-14 (Wed) 14:00**, with 80 places. Admission is
selective: admitted participants are listed and emailed, others are not notified. Day 2 announces
the Demo list at 12:00; 10–15 teams demo. This supersedes the October 18 deadline above.
**Owner decision — 2026-10-14:** the owner reports having registered; admission is not yet known.

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
the organizer's de-identified copy to this event. **Limitations:** a rolling sample, not a census;
topic labels are self-selected; voices are reports, not prevalence. Raw voices, display names and
quotations stay outside Git; findings below are paraphrased.

**Open question:** which decision causes a repeated, consequential difficulty for a reachable user?
The official page does not establish a validated workflow, baseline or agreed success threshold.
Public-source research can investigate those gaps; external interviews/messages retain the existing
action-time confirmation boundary.

## Research umbrella policy

**Owner decision — 2026-10-13:** update the repository in depth and introduce an umbrella policy.
**Policy — analyst implementation:** this section governs research, data discovery, comparison and
demonstration proposals. It neither selects a topic nor authorizes implementation, and company
priorities remain with the origin repository. It applies to organizer and expanded free-topic candidates.

**Owner decision — 2026-10-13, current method:** adopt the method improvements following independent
GPT-6-Astra and Opus 5.5 consultation of `1e5619c`. Investigate each topic backward from an evidenced
pain point and observable success/rejection conditions. After this method update, delegate deep
research to GPT-6.1-Sol, with bounded Luna assistance for source discovery. Sources are not restricted
to Twinkle or government APIs. This direction supersedes data-readiness-first research priority;
it preserves research-only scope and the existing participation, payment and contact boundaries.

**Owner decision — 2026-10-14:** the original pain is the core of every topic. When a topic starts,
read its official prompt verbatim on the live page once and look for the citizen voices it was
organized from. Record the verbatim pain sentence, retrieval time and what the citizens themselves
describe in the topic document, separately from the policy team's suggested solution. Every later
step works from that recorded pain, not from a paraphrase. A suggested model, map or ranking is a
direction to test against that pain, not the problem definition.

**Owner decision — 2026-10-14 (later):** re-reading the live page before every piece of work is
excessive. Re-check it only before relying on event facts that change (deadlines, rules, data
terms) for an action, or when there is a reason to think the prompt changed.

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

GPT-6.1-Sol owns each deep investigation and interpretation. Luna may receive bounded discovery
tasks with a named question, search scope and completion condition: return candidate URLs,
original publishers, observed schemas/access, period, licensing evidence, limitations and
contradictory findings. Label uninspected hits as leads. The topic owner checks consequential
claims against source bytes before integrating; model output is not evidence. Stop a discovery
branch when its assigned uncertainty is resolved or the named route is exhausted, reporting the
remaining unknown and next feasible check. Do not silently substitute a different requested model.

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

## Topic document standard

**Owner decision — 2026-10-14:** keep one master document for method, event facts and cross-topic
comparison, and one maintained document per official issue. Structure and consistency come first.
Issue 6 is the first topic migrated to this standard.

### Document ownership

| Document | Owns | Does not own |
| --- | --- | --- |
| `docs/research.md` (this master) | Mandate, event facts, official prompts index, umbrella policy and this standard, cross-topic comparison, canonical readiness record, dataset-to-candidate index, next-investigation queue, shared audits, tooling and verification logs | Topic-specific evidence and workflows |
| `docs/topics/issue-N-<slug>.md` | Everything specific to one official issue: verbatim prompt, citizen pain, pain tree, practice, workflows, evidence, next actions | Status labels (it links the canonical readiness record); cross-topic ranking |
| `docs/topics/issue-N-<slug>.html` | Traditional Chinese reading mirror of one topic document | New findings; it never leads its Markdown |
| `docs/research-report.html` | Traditional Chinese overview: method, event facts, topic index and the historical cross-topic summary | Topic detail |

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
4. **`## 4. Candidate workflows`.** One `###` per workflow, using the required candidate record.
5. **`## 5. Evidence and data audits`.** Dataset audits and source ledgers, each with retrieval
   date, method and limitations.
6. **`## 6. Readiness and integration`.** The issue-specific consequence only; status stays in
   the canonical record.
7. **`## 7. Next actions and open decisions`.** One executable next check, plus owner decisions
   with their consequences.
8. **`## Change log`.** Dated one-line entries.

### Topic HTML skeleton

Build the page with `html-report-system` on its neutral foundation. Validate it with `--portable`
and look at it at 1200 px and 390 px.

The page title is 「<議題>研究報告」. The thesis states the current pain-based conclusion in one
line. The sections run in this order; the optional ones may be left out:

1. 本期重點 (six cards)
2. 01 市民原本在痛什麼
3. 02 官方方向與要做的決策
4. 03 現行做法與卡點
5. 04 專業判斷 (optional)
6. 05 資料能做到哪裡
7. 06 其他城市怎麼做 (optional)
8. 07 候選方向與方法
9. 08 怎麼驗證
10. 09 下一步與待決定
11. Appendix (optional)

Navigation labels use these section names exactly; an `h2` may phrase its section as a question.
The footer records the evidence cutoff and the SHA-256 of the topic Markdown.

Chinese line breaking: headings, the thesis, eyebrows, captions, summaries and table cells use
`word-break: keep-all; overflow-wrap: anywhere` so they break at punctuation rather than inside a
word (「沒｜人協調」); body prose keeps normal breaking, and `scripts/cjk_line_ends.py` keeps each
eligible block's final four characters together as a best-effort orphan-line reduction; endings
inside existing inline elements are left unchanged. Copy the rule from an existing report.

### Rules

- **Naming.** Files are named `issue-N-<english-slug>`. Workflow IDs keep their track prefix
  (T06-A), and candidates C01–C08 keep their identities.
- **Start from the source.** Every topic begins from its recorded official prompt and citizen
  voices (owner rule above). Quote organizer text verbatim only for the prompt; paraphrase
  citizen voices.
- **One place per fact.** Link instead of duplicating.
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
   as a direction to test. In issue 6 the suggested weighted ranking addressed neither observed
   voice (co-owner consent, missing coordination).
4. **Build the pain tree.** For each pain, write down who decides what, which fields that
   decision needs, and where each field could come from. Sources include public data, restricted
   routes needing a request, and data the team could collect.
5. **Read the baseline before proposing.** Find the existing rule, programme or service that
   already does the task, and its observed throughput. Issue 6's "city as project manager"
   already existed as the promoter programme; the gap was conversion, not existence.
6. **Read the governing rules in the original.** Statutes come from the national law database
   (`law.moj.gov.tw`, by pcode). Taipei rules come from `laws.gov.taipei` print views. Agency
   FAQs and attachments come from the agency topic page. A threshold can be the decisive lever:
   in issue 6 the assessment result changes which consent rule applies.
7. **Open the agency's attachments before calling data restricted.** In issue 6, CMO's topic
   page published two building-level lists that overturned an earlier "restricted only"
   conclusion. Parse PDFs with `pdftotext -layout`, and record only aggregates in Git.
8. **Locate the bottleneck.** Check where the process funnel stalls before designing a ranking or
   tool. For example, national initial assessments numbered thousands while detailed assessments
   numbered a handful.
9. **Write candidates with rejection conditions.** Use the
   [required candidate record](#required-candidate-record). Keep the policy-direction candidate
   and the pain-side candidate separate and both labelled hypotheses.
10. **Update in order.** Update the topic Markdown, then its HTML mirror, then the
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
  samples support "most stop at the first stage" but not rates or trends. Say which.

### Document management lessons

- **One owner per fact.** The master owns method and cross-topic records; the topic document
  owns its issue. Link instead of copying.
- **Restructure by script.** Track every original heading to its new anchor and rewrite every
  link from that map. The 2026-10-14 split moved 2,966 lines with zero lost lines and zero
  unresolved links. A hand-written header link still needed a fix, so always run the checker
  afterwards.
- **Use fixed names for consistency.** Topic HTML navigation uses the skeleton's section names
  exactly; headings may be questions.
- **Stamp each mirror with its source.** The footer carries the source Markdown's SHA-256.
  Recompute it after any Markdown edit made after the HTML build.
- **Migrate legacy topics with new research.** Reformat a legacy topic only when its pain is
  first recorded.

### Checks and tooling

| Check | Command | Catches |
| --- | --- | --- |
| Links and anchors | `python3 scripts/check_links.py` | Missing files, renamed headings, wrong relative depth |
| HTML gate | `python3 ~/.agents/skills/html-report-system/scripts/validate_html_report.py --portable <page>` | Report-system structure and portability |
| Chinese line endings | `python3 scripts/cjk_line_ends.py <pages>` (idempotent; run after any HTML text edit) | Paragraphs ending on a line of one or two characters; `text-wrap: pretty` does not prevent this for Chinese in Chrome |
| Rendering | `uv run --with playwright python scripts/render_check.py <scratch-dir> <pages>` | Horizontal scroll at 1200 px and 390 px; then look at the screenshots |
| Source hash | `shasum -a 256 <topic>.md` against the HTML footer | Stale mirror |

**Pitfalls observed:**
- zsh does not word-split unquoted variables. `set -- $pair` left `shasum` waiting on stdin and
  hung a background job; pass files explicitly.
- Playwright's bundled browsers are absent here; `render_check.py` uses the installed Chrome.
- The web fetch tool cannot open `puma.taipei`; curl and urllib with a browser User-Agent can.
- Downloads go to a temporary directory, never the repository.

## Ten-track deep research findings

**Evidence and inference — deep run, 2026-10-13:** the following records extend the existing
research authority. Track numbers preserve ownership, not priority; C01–C08 retain their identities.
Source-level experiments resolve specified data or baseline questions. They do not substitute for
observed practitioner task performance, adoption or civic outcomes. Each workflow distinguishes
supported, refuted and unresolved claims and names the condition for continuing, narrowing or deferring.
Older audits below remain dated observations; only explicitly re-read dependencies are refreshed.
The canonical readiness record and next-investigation queue own status and consequential next steps.

## Topic index

| Issue | Official prompt | Topic document | Template | Pain recorded | Reading mirror |
| --- | --- | --- | --- | --- | --- |
| 1 | 把三千棵樹種回來 | [Trees and shade equity](topics/issue-1-trees.md) (T01) | Legacy | Pending | — |
| 2 | 找回消失的垃圾桶 | [Public bins](topics/issue-2-bins.md) (T02, C07) | Legacy | Pending | — |
| 3 | 鼠患四處跑，衛生安全怎麼辦 | [Rats and source control](topics/issue-3-rats.md) (T03) | Legacy | Pending | — |
| 4 | 內湖尖峰車流好比停車場 | [Neihu peak traffic](topics/issue-4-neihu-traffic.md) (T04) | Legacy | Pending | — |
| 5 | 公車路網如何即時反應需求 | [Bus network and driver rest](topics/issue-5-buses.md) (T05) | Legacy | Pending | — |
| 6 | 危老耐震如何查，風險評級怎麼找 | [Old-building seismic resilience](topics/issue-6-building-resilience.md) (T06) | v1 | 2026-10-14 | [老屋韌性研究報告](topics/issue-6-building-resilience.html) |
| 7 | 自由題：你看見的市政 bug | [Free topic](topics/issue-7-free-topic.md) (T07–T10; C01, C02, C04–C06, C08) | Legacy | Pending | — |

The ten-track run below is summarized here only through the cross-topic comparison; each track's
full record now lives in its topic document.

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
| T06 Buildings | Municipal inspection allocation; public-renewal review; earlier preparation/feasibility/outreach | Professional process and historical affordability barriers; no building-specific safety or outreach-effect evidence | Existing CMO/URO/NCREE routes; consent, liquidity, professionals and work disruption | Rules found: eligibility+consent, no published ranking; uptake, not identification, is the bottleneck; building-level old stock is mostly restricted (two scoped CMO lists public). 2026-10-14 citizen voices point to co-owner consent and coordination; consent thresholds differ by route and a below-minimum assessment can open a discretionary majority route; promoter filings rarely reach plan stage. Taipei counts and assessment records needed before real prioritization |
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
| [**C01 Collision-site review**](topics/issue-7-free-topic.md#c01-collision-site-review) | `130110`: 22,762 published 2025 fatal/injury collision rows, 12 months; all first-party sequence 1, two missing coordinate rows | Traffic engineer filters a district/time band, compares observed collision concentrations and road/signal attributes, and prepares an auditable field-review list | Decode post-2023 codebook, confirm event/party/severity semantics and aggregate units; no exposure denominator, safest-route, all-pedestrian-victim or causal intervention claim |
| [**C02 Senior-meal inventory**](topics/issue-7-free-topic.md#c02-senior-meal-service-inventory) | `135495`: 440 meal-list rows + previously audited 2026-09 age-population data; root successfully joined all 12 districts | Social-welfare planner compares listed sites per 1,000 registered older residents and selects areas for site/activity/capacity investigation | Site list lacks row observation dates, meals/seats/hours/attendance; the ratio is an inventory proxy, not demonstrated service shortage or actual demand |
| [**C03 Accessible park entries**](topics/issue-1-trees.md#c03-accessible-park-entry-comparison) | `152266`: 745 park entrance rows with width/slope/TW97 XY; `128414`: 193 MRT accessible entrance rows | Park-access officer/caregiver compares published entrances and source conditions; flags entries or approaches requiring survey | Root found two coordinate-magnitude outliers; validate CRS and points, no common stable ID or complete walking topology. An inspection comparison, not wheelchair-safe navigation |
| [**C04 Shelter preparedness**](topics/issue-7-free-topic.md#c04-village-shelter-preparedness) | `tp-00002066`/`134683`: 419 SA-ID records in a 2026 ODS, plus service-village/hazard/accessibility/capacity fields and age population | District preparedness coordinator audits listed flood eligibility, backup/accessibility and service-village coverage, producing questions before exercises | Resolve differing agency inventories and flag/capacity semantics, district-qualified village joins, shared capacities and latest authority; no live opening/occupancy or evacuation instruction |
| [**C05 Rainfall-scenario review**](topics/issue-7-free-topic.md#c05-rainfall-scenario-facility-review) | `121550`/`tp-00000862`: official 2023 modeled 78.8/100/130 mm/h accumulation scenarios; one KML parsed with 1,945 polygons | Facility planner checks verified points against scenario depth bands for a preparedness review | Geocode/verify entrances, audit remaining scenarios; explicitly **government-modeled input**, not real flood observation or prediction. Intersection does not prove a building/shelter unsafe |
| [**C06 Childcare evidence**](topics/issue-7-free-topic.md#c06-childcare-evidence-shortlist) | `121337`:29 public-operated centers; `121278`:223 private; `156685`:292 assessment rows with uneven 2021–2025 coverage | Parent/planner forms a local evidence-linked shortlist and sees which assessment year applies | Verify name/address joins, active status, assessment cycles and meaning of 收托人數; no vacancies, capacity shortage or generic best-center score |
| [**C07 Market-bin audit**](topics/issue-1-trees.md#c07-market-bin-service-audit) | `121593`:47 geocoded markets + existing bin inventory | Sanitation supervisor prepares an inspection list of approaches, listed bins and unresolved public/private responsibility | Venue point is not a pedestrian entrance/catchment; no footfall, overflow or operational cost data. Audit candidate, not placement/collection optimization |
| [**C08 YouBike patterns**](topics/issue-7-free-topic.md#c08-youbike-transfer-patterns-and-current-availability) | `169174`:2023-only transfer-rental subset; December full response had 518,189 rows; `137993`:current publisher 1,819-station snapshot | Operations analyst explores historical station/time patterns; commuter uses a separate timestamped current station lookup | Full-month validation and historical/current station identity needed; no unmet demand, truck schedule or availability history. Old transfer subset cannot justify present redispatch/shortage predictions |

**Inference — earlier source-audit scope:** the first three had bounded real-data foundations in
that audit; this does not privilege them in the current problem-first queue. Flood preparedness
has administrative/scenario inputs distinct from real-time safety advice.
Original shade optimization, rodent prediction, individual-building safety ranking and bus-demand
network redesign remain unsupported by the missing outcomes/constraints; new catalog hits do
not cure those gaps. User value still requires validation with a named practitioner, and any
external contact needs owner authorization.

### Problem fit and separate readiness of the expanded candidates

**Canonical current judgment — 2026-10-13, after the deep run:** this stable section now owns
readiness for official themes and expanded candidates, separated into all 27 workflows below. The original deep run covered25; the later owner-requested allocation reframing adds2 explicit, unvalidated hypotheses, not2 completed practitioner studies.
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
| T06 municipal inspection allocation | specified | Reframed as tiered screen-to-verification sequencing; current rules are eligibility+consent, no published ranking; open stock data stop at district level; Taipei assessment counts, confidential initial-assessment records and slots missing; no real ranking |
| T06 public-renewal review priority | specified | Separate from inspection; exact program/rules, professional/project evidence and alternatives missing |
| T06 assessment preparation | specified | Fictional checklist; existing pack covers tested branches |
| T06 retrofit/renewal feasibility | specified | Professional case, financing/consent and quote evidence absent |
| T06 opt-in outreach | specified | Existing services; intake gain and available professional capacity unknown |
| T06-D route finder for a blocked walk-up | unassessed | Hypothesis from citizen voices; statutory thresholds and CMO Q30 verified; frequency of discretionary prompt designation and unit-size limits unknown; baseline is promoters and CMO FAQ |
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
| `130110` / `tp-00001025` collision records | C01 essential | T07 full 2025 aggregate audit; first-party extract, no event ID; current form does not resolve export 2–30-day-death semantics | [T07](topics/issue-7-free-topic.md#t07-c01-collision-site-review) |
| `137993` YouBike current inventory | C08 current lookup | T10 later 1,819-station snapshot; active/inactive and campus category separated; no arrival guarantee; capacity differs from bike+slot sums | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `169174` transfer rentals | C08 historical | Full December census completed; all 31 borrow dates, hour-rounded times, 858 identical-row excess and 543 unmatched current names; completeness/identity still unresolved | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| `135775` monthly YouBike total | C08 context only | MCP sample and publisher schema; no station dimension | [Transport audit](topics/issue-7-free-topic.md#exact-new-dependencies-and-observed-access) |
| `152266` park entrances | C03 officer/caregiver | T01 745-ID match with Wheelroute, identical width/slope and shared two gross location anomalies; source agreement is not independent validation | [T01](topics/issue-1-trees.md#t01-trees-shade-and-accessible-park-use) |
| `128414` / `tp-00001516` MRT accessible entrances | C03 essential | Full CSV parsed; network extends beyond Taipei, no downtime or shared entrance ID | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| `126553` garbage/compost collection totals | C07 context only | Full CSV parsed; no district/team dimension despite title | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| National catalog `121593` markets | C07 essential | Direct publisher discovery/full CSV; not independently discovered through MCP, no all-food-business coverage | [Street-environment audit](topics/issue-1-trees.md#additional-datasets-and-actual-reads) |
| Wheelroute `2b58f15a…` | C03 baseline/potential | 940 API records; 745 park measurements match, remaining 195 sentinel-like; separate 193-row MRT inventory not reconciled; units/topology/current conditions unresolved | [T01](topics/issue-1-trees.md#t01-trees-shade-and-accessible-park-use) |
| `135495` meal list; current 115.08 PDF/operator schedules | C02 planning/access | 440-row descriptive ratio preserved; ten source correspondences checked; age60 eligibility differs from age65 denominator; schedules exist, activity/capacity/acceptance unknown | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `121337` public childcare | C06 | Old count source differs from dated September roster; 29 public centers not the full supply system; no offered vacancy | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `121278` private childcare | C06 | Earlier 223 rows retained; dated full registry distinguishes service categories/periods; legal identity joins require review | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `156685` assessment CSV; 115/2026 PDF | C06 parent evidence | 292-row CSV ends2025; newer PDF and map disagree in inspected case; law/footer cycle conflict retained; missing assessment is not failure | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
| `135696` childcare enrollment | C06 context only | Full semiannual citywide series; no local/center vacancy inference | [Care-service audit](topics/issue-7-free-topic.md#evidence--retrieved-2026-10-13) |
| `121550` / `tp-00000862` rainfall scenarios | C05 | All three KMLs fully parsed; 1,945/7,330/29,738 polygons, 9/57/287 invalid under stated GEOS; modeled inputs, no validated facility join | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `135484` / `tp-00003479` welfare shelters | C04 | Older399-row source retained; T09 exact district+name joins differ from earlier recipe; scope/authority unresolved | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `134683` / `tp-00002066` education shelters | C04/C05 | 419 IDs/418 names; website ODS and April2026 plan compared; two school conflicts, shared capacities and authoritative semantics unresolved | [T09](topics/issue-7-free-topic.md#t09-c04-shelter-inventory-reconciliation-and-c05-rainfall-scenario-preparedness-review) |
| `tp-00003001` flood facilities; `tp-00003003` flood works | C04/C05 context leads | Catalogs inspected only; resource rows not read, annual aggregates cannot prove local protection | [Flood audit](topics/issue-7-free-topic.md#evidence-additional-dataset-inventory) |
| Existing village/district age population (`a6394e3f…`) | C02 essential; C04/C06 potential | Full source parsed earlier; C02 twelve-district join checked, village joins unvalidated | [Organizer population audit](topics/issue-6-building-resilience.md#organizer-starter-dataset-pages-2026-10-13) |
| Existing bin inventory `121355` | C07/T02 | T02 lookup equals681-row CSV; nonnumeric longitude, aggregate/duplicate sites; market point may be stale | [T02](topics/issue-2-bins.md#t02-public-bins-and-c07-market-bin-responsibility-audit) |
| Existing trees, pits and sidewalk geometry | C03 optional context | Full inventory/geometry checks earlier; stale surveys/duplicates, no measured shade or connected path | [Organizer tree audit](topics/issue-1-trees.md#trees-and-shade-four-dataset-pages) |
| T04 city v2 VD/static; annual survey128230; NFB archive | Official Neihu | Current public readings and historical local/upstream samples verified; exact city-v2/station-workbook rights and complete corridor history unresolved; NFB >40s request spacing | [T04](topics/issue-4-neihu-traffic.md#t04-official-neihu-traffic-timing-requires-an-executable-employer-decision) |
| T05 2025 route statistics / OMS-duty evidence | Official buses | Route-level context and one TTSB actual-duty case; stop/time demand, current private duty and rest facilities absent | [T05](topics/issue-5-buses.md#t05-official-buses-service-decisions-and-executable-driver-rest) |
| T06 building7889e8a0; soilec40e067; professional packs | Official buildings | Full city-aggregate parse; later primer fully parsed136 liquefaction polygons and refreshed population/fire file shapes. Later allocation audit found2 invalid polygons and building-count arithmetic differences; population totals passed bounded consistency checks. Current building-level coverage and independent accuracy remain unknown; no individual safety/priority inference. Professional routes already exist | [T06](topics/issue-6-building-resilience.md#issue-6--old-building-seismic-resilience) |
| T06 identity B01–B07: use permits128203, permit map151936, doorplates155472, MOI transactions, sea-sand register PDF | Official buildings (allocation A) | 2026-10-14 full parses; construction-permit join verified (99.5% floor agreement) for2001+ use permits; transactions give completion/material/floors for 9.8% of address keys; full sea-sand register only as PDF. Pre-1996 inventory and independent accuracy unresolved | [T06 identity audit](topics/issue-6-building-resilience.md#building-identity-audit--public-chains-cover-new-buildings-not-the-old-building-universe) |
| T06 deep investigation: Revenue Service 132020 district buildings; MOI pip T13/T15/T16 units; NLSC 3D model; restricted tax/land registers | Official buildings (allocation A/B) | 2026-10-14 full parses of district files (reconciled totals); building-level old stock only via restricted or request routes; no village/grid open data | [T06 deep investigation](topics/issue-6-building-resilience.md#selection-practice-bottleneck-and-professional-anchors) |
| T06 pain tree: statutes D0070249/D0070008/D0070118; CMO promoter register 115.10.1; CMO pre-2003 no-management list 115.07.17; CMO 危老問答集 B; elevator FAQ | Official buildings (T06-D, coordination, 人老 branch) | 2026-10-14 statute reads and full PDF parses: 3,698 promoter filings (3,182 initial, 22 detailed, 492 plan; median 4 households); 5,489 listed use permits. Addresses and names not retained in Git; no reuse licence stated | [T06 pain tree](topics/issue-6-building-resilience.md#2-pain-tree) |
| T03 food9431f450 / pipeaf1e6e42 / complaintcb423c17 / current ODT | Official rats | Full fields rechecked; no spatial outcome/repair chain. No-committee consent route verified; third-party reports require rights/privacy review | [T03](topics/issue-3-rats.md#t03-official-rats-intake-versus-inspectable-source-control) |
| T08 dated September2026 full registry;147154; baby-map layer6 | C06 | 314 serials, approved/actual/hours/fees/type; older215-row CSV has no row dates. Map/API rights unknown; actual enrollment is not offered vacancy | [T08](topics/issue-7-free-topic.md#t08-c02-senior-meals-and-c06-childcare) |
|166491 /174976 availability categories;166492 aggregated OD | C08 | Full June2026 catalog-labeled resources; category boundary/period conflicts, no numeric hourly rates or unmet demand; LineString not cycling route | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |
| MRT63f31c7e / 2025 survey/performance | Retained MRT | Index/schema, waiting recommendation and contrary compliance; no full OD-month or platform/service-constraint validation | [T10](topics/issue-7-free-topic.md#t10-mrt-service-review-and-c08-youbike-three-separate-decisions) |

Search-only leads, including bicycle lanes, bridge access and bicycle parking, remain in the
transport track. They must not silently become essential inputs. None of these observations
establishes all-city completeness or an operationally reliable live service.

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
| T06 | Re-anchored 2026-10-14 on citizen voices: consent and coordination after a building is known to be old; hypothesis A kept for the policy direction | Read urban renewal office designation notices and the Taipei renewal ordinance to test T06-D; then council/audit reports for Taipei counts (owner choice on information requests unchanged) |
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
| Problem/decision validation | Ten tracks:25 deep-run workflows plus2 later allocation hypotheses; bounded source checks completed, practitioner gain untested | Follow the current queue; separately authorize practitioner comparison if selecting a pilot |
| Selection and implementation | No topic selected; no contest app built | Owner selection/request and rechecked event rules required before implementation |

The [next-investigation queue](#next-investigation-queue) owns the executable research sequence.
Existing validation thresholds are proposed checks, not completed tests or measured user benefits.

## Open questions

- **Participation:** the owner registered on 2026-10-14 (see [official baseline](#official-baseline));
  admission is not yet known, and no topic or team has been chosen.
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
Authenticated Twinkle discovery is recorded separately. HTTP 200
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
being rewritten, with MCP unaffected. No Twinkle skill was installed; the README summarizes the
tested gateway/schema route. Source facts, transformations and solution conclusions
must remain separately attributable.
