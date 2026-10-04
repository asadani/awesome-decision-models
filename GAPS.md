# Gaps: what is built, what isn't

**Short answer:** almost every idea I could think of already has a prototype, built within three weeks of Jev's launch. The gap is **maturity and evidence**, not existence: the projects are tiny, mostly one-person, and almost none has an independent evaluation. This page shows the evidence and its limits. Data collected **04 Oct 2026**; the numbers will date quickly.

## Corrections to what I said earlier

- I told you I found no decision-model tool for organizing files, and an earlier version of [productivity.md](categories/productivity.md) repeated that. **Wrong.** I had only checked one list. Nine projects exist ([list](categories/productivity.md#file-and-folder-organization)).
- I proposed three possible gaps in chat: hierarchical choice over large option sets, cross-step error budgets, and a neutral cross-model benchmark. **Each has at least one existing prototype** (table below), though all are small and unproven.
- I said calibration tooling was missing, and then found jevcal, DSPy's `ReAnchor`, huncho and others. See [infra-and-evaluation.md](categories/infra-and-evaluation.md).

## Method

1. **Ecosystem census from a paper.** [Jev in the Wild (arXiv 2609.30216)](https://arxiv.org/abs/2609.30216) analyzed 2,170 verified public Jev projects on GitHub as of 22 Sep 2026, each assigned to one of 18 subcategories, with project counts and total stars. I reuse its Table 1 numbers and compute stars per project myself.
2. **My own GitHub searches on 04 Oct 2026** (repository search, keyword queries such as "jev organize files"). I read the top results for each niche to check they are actually relevant.
3. **Cross-check against this repo's catalog.**

## 1. Where the ecosystem is, per the census

Source: Table 1 of [2609.30216](https://arxiv.org/abs/2609.30216) (22 Sep 2026; Jev only; Laya, Clef and later models are not in it). The last column is my own division, and the paper cautions that stars show visibility and not unmet demand.

| Category | Subcategory | Projects | % of projects | Stars | % of stars | Stars per project |
|---|---|---|---|---|---|---|
| Interface Agents | Web Interaction | 125 | 5.8% | 46,067 | 21.0% | 369 |
| Interface Agents | Desktop & Mobile | 50 | 2.3% | 1,418 | 0.6% | 28 |
| Software Engineering | Code Quality | 90 | 4.1% | 1,500 | 0.7% | 17 |
| Software Engineering | Dev Workflows | 218 | 10.0% | 3,014 | 1.4% | 14 |
| Search & Memory | Context & Memory | 77 | 3.5% | 10,533 | 4.8% | 137 |
| Search & Memory | Search & Data | 120 | 5.5% | 2,334 | 1.1% | 19 |
| Search & Memory | Classification | 184 | 8.5% | 1,169 | 0.5% | 6 |
| Safety & Governance | Review & Approval | 82 | 3.8% | 5,750 | 2.6% | 70 |
| Safety & Governance | Security & Compliance | 93 | 4.3% | 1,904 | 0.9% | 20 |
| Routing & Automation | Model & Tool Routing | 132 | 6.1% | 71,671 | 32.6% | 543 |
| Routing & Automation | Workflow Automation | 118 | 5.4% | 19,332 | 8.8% | 164 |
| Simulation & Control | Games & Simulation | 227 | 10.5% | 1,825 | 0.8% | 8 |
| Simulation & Control | Robotics & Control | 25 | 1.2% | 264 | 0.1% | 11 |
| Content & Expert Tasks | Professional Tasks | 176 | 8.1% | 6,597 | 3.0% | 37 |
| Content & Expert Tasks | Content & Dialogue | 211 | 9.7% | 5,363 | 2.4% | 25 |
| Infrastructure & Other | SDKs & Tools | 175 | 8.1% | 34,800 | 15.8% | 199 |
| Infrastructure & Other | Research & Resources | 56 | 2.6% | 6,010 | 2.7% | 107 |
| Infrastructure & Other | Other Applications | 11 | 0.5% | 107 | 0.0% | 10 |

Reading it, with the paper's caveat that a few prominent repos dominate star totals:

- **Attention is very concentrated.** The paper reports Routing & Automation and Interface Agents hold 19.6% of projects but 63.0% of stars. Model & Tool Routing alone has about 543 stars per project, and Classification about 6.
- **Thin supply, decent attention:** Context & Memory (77 projects, about 137 stars each), Review & Approval (82 projects, about 70 each) and Research & Resources (56 projects, about 107 each) have fewer projects than most categories but more stars per project than the median. This is a weak signal, not demand.
- **Crowded and quiet:** Games & Simulation (227 projects, about 8 stars each) and Classification (184, about 6) are large, low-attention categories.
- **How Jev is used:** attribute judgment appears in 77% of projects, scoring or ranking in 52% and action selection in 31%; 69.7% of projects with an identified purpose use more than one purpose.

## 2. My niche check

Raw counts are **noisy**: the bare keyword "jev" matches 15,683 repositories (the paper verified 2,170 real projects), so I only trust small, specific queries where I could read the results. Counts are GitHub repository-search totals on 04 Oct 2026.

| Idea | Query | Raw hits | What I found on reading the results | Most stars |
|---|---|---|---|---|
| File and folder organization | "jev file organizer", "jev organize files", "jev downloads folder", "laya organize files", "jev duplicate files" | 6, 5, 2, 1, 1 | 9 distinct projects, created between 18 Sep and 4 Oct 2026 ([list](categories/productivity.md#file-and-folder-organization)). One uses Laya locally; one files notes through an MCP server | 2 |
| Hierarchical choice and large option sets | "jev hierarchical" | 8 | At least 4 relevant: a taxonomy-tree knowledge service, an agent design that handles more options than the model's limit through paging, a hierarchical chat decoder, and a memory engine | 46 (NylonME) |
| Error guarantees across decisions | "jev conformal" | 4 | 1 relevant: jev-certify (conformal risk control for routing thresholds). None found for multi-step chains | 1 |
| Independent benchmarks | "jev cost per decision", "decision model leaderboard" | 5, 21 | 2 relevant: jevals-data, decidebench. Both tiny; decidebench uses 400 decisions | 1 |
| API conformance | "jev conformal" | 4 | 1: jevcompat, a conformance suite for Jev-compatible servers | 0 |
| Observability | "jev observability", "jev tracing" | 55, 8 | A local call visualizer (jeview) and a couple of tracing-focused agent loops; most hits are unrelated | 61 (jeview) |
| Calibration and thresholds | "jev calibration", "jev threshold", "laya calibration" | 263, 37, 58 | Well covered by jevcal, huncho, DSPy and others, though most raw hits are noise | n/a |
| Memory for agents | "jev memory", "jev obsidian", "jev notes" | 104, 28, 56 | Several note and memory projects ([list](categories/agents-and-routing.md#large-option-sets-and-memory)) | 46 |
| Laya-specific tooling | "laya mcp", "laya tool", "laya agent" | 94, 82, 175 | A multi-model MCP connector (340 stars) and a few local Laya agents. Laya-only tooling is thin but not absent | 340 |
| Multi-model connectors | "decision model system one" | 443 | One strong multi-model MCP connector (system-one-connector), plus a client with fallbacks and cost tracking (decidekit) | 340 |
| Cross-model evaluation after the new entrants | "clef decision model", "strands decider" | 24, 40 | Too new to judge; mostly unrelated hits | n/a |

"Raw hits" for queries that returned 0 (for example "jev cascade escalation LLM fallback" and "system one decision model benchmark harness Jev Laya Clef") means the exact phrasing found nothing, which says little about whether such projects exist under other words.

## 3. What this suggests (my interpretation, not a finding)

1. **Don't build another prototype in these niches without a reason.** Someone has already made a small one. What is missing is a *good* one: tested, documented and evaluated.
2. **The evidence gap is the biggest one.** Every performance claim about the new models is vendor-reported ([benchmarks.md](benchmarks.md)). The independent benchmarks I found are small (hundreds of items). A reproducible, multi-model comparison with calibration and cost per correct decision would be new and useful, and it fits a curation repo.
3. **Compare, don't just list.** For any tool category, a short head-to-head on the same inputs would beat another list entry. File organization is a good test case because the projects are small enough to run.
4. **Attention follows routing and browser agents**, per the census. If you want visibility, those are where stars go, but the census warns that this is concentration and not unmet demand.

## Limits

- Everything here is GitHub only. Closed products and projects hosted elsewhere are invisible.
- The census covers Jev projects up to 22 Sep 2026 only. Projects built for Laya, Clef, Strands Decider, pplx-decider or GLiDE are undercounted, as are Jev projects created after that date.
- My searches mostly use the word "jev", so projects that don't name it are missed. Search ranking is by stars, so I read the most visible results and may have missed lower ones.
- I did not run any project. "Exists" means a repository with that stated purpose, not that it works.
- Star counts are a snapshot and a crude proxy.
- Search hit counts are noisy and unvetted except where I read the results.
