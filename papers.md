# Papers

arXiv papers on typed decision / System One models, 13 so far, all published Sept 2026. Summaries are paraphrased from the abstracts (I read the arXiv abstract pages, not the full papers). Grouped by theme.

## Evaluation and calibration

**[Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647)**: Deußer, Sparrenberg, Sifa · 2026-09-29
Evaluates Jev on 37 datasets. Reaches 95–99% accuracy on IMDB, SST-2, HellaSwag and ARC and beats competitors on most. Probabilities are well-calibrated enough for selective prediction; performance falls on low-resource languages and nuanced labels.

**[Laya as a Typed Probabilistic Assessor: An Independent Reproduction and a Preregistered Study of Calibration and Selective Escalation](https://arxiv.org/abs/2609.33843)**: Nandakishore · 2026-09-27
Laya (ModernBERT-large) is systematically under-confident (signed gap −0.214). Temperature scaling (T=0.469) cuts ECE from 0.214 to 0.037. 20 of 22 preregistered tests were significant, but the confidence-based escalation gate missed its 10% error target on both tracks.

**[Do System One Decisions Add Up? A Study of Probabilistic Coherence](https://arxiv.org/abs/2609.33971)**: Joy · 2026-09-27
Tests whether a decision stays consistent when broken into hierarchical steps, on Jev and English Laya over 72,000 questions. Substantial disagreement (total variation distance 0.219–0.689). Going through broad categories dropped Jev by 22.9 points and raised Laya by 21.3.

## Decision models as judges

**[JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)**: Li et al. · 2026-09-22
Uses Jev's confidence to decide whether to accept its verdict or escalate to a reasoning judge. Against sixteen generative and reward-model judges with blinded human adjudication, Jev lands within three points of GPT-6 where a verdict can be read off the text, at 0.36% of the fee and 0.15 s median latency. It falls behind where the verdict must be derived (math, code, logic), and its confidence marks that boundary. With a threshold frozen in advance, the cascade is 0.9 points more accurate than GPT-6 on 1,610 held-out pairs at 41% of the fee. (Abstract-level claims; this is the strongest published evidence for the accept-or-escalate pattern, in contrast to the escalation-gate misses in the Laya studies below.)

**[JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places](https://arxiv.org/abs/2609.29769)**: Rao · 2026-09-24
Compares Jev with three flash-tier LLM judges on nine panels from seven human-judged benchmarks, with identical criteria. The LLM judges cost 16–325× as much and take 28–350× as long. Jev's accuracy differs significantly from theirs in at most 8 of 27 paired comparisons, ahead mostly on binary checklist criteria and behind only on ordinal ones.

## Ecosystem and method

**[Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216)**: Ling et al. · 2026-09-24
Analyzes 2,170 public Jev projects from GitHub as of 2026-09-22. Finds rapid early growth in new projects and in integrations into existing repos. Attribute judgment and scoring are widely used; action selection, content filtering and model/tool selection vary by domain. The authors read Jev as a reusable decision component. This is the best map of what people actually build, and a source for finding gaps.

**[NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees](https://arxiv.org/abs/2609.28587)**: Ye et al. · 2026-09-23
A training-free method that gets numeric output from any LLM with a Jev-like structured-choice interface by recursively refining a range through a multiway decision tree. On the authors' arithmetic benchmark it beats direct selection from a candidate list containing the right answer by 2.93 points. Relevant beyond numbers: it is evidence that hierarchical descent over choices can beat flat selection.

## Agent memory

**[Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986)**: Jiang et al. · 2026-09-21 · [code](https://github.com/craftsland/Jev-Mem)
Splits agent memory along System 1 / System 2 lines. A decision-model control plane handles memory typing, relational organization, query routing, retrieval-budget allocation, graph traversal, candidate scoring and adaptive stopping. The LLM is invoked only for complex reasoning and answer synthesis. On LoCoMo: LLM-as-a-Judge score 0.777 (11.0% relative gain over the strongest baseline), memory construction in 158 s (6.6× faster than the fastest competitor), and average query latency 0.93 s (36.7% lower).

**[When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model](https://arxiv.org/abs/2609.34227)**: Sharma · 2026-09-28
Pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns selected by one Jev call are non-inferior to an LLM-extraction memory (bound −3.0 vs a −5-point margin), and raw turns cost 3,061× less to write. Reranking adds 17.4 points on LoCoMo and 9.1 on LongMemEval at a tight budget (3 of 30 candidates kept), but only 1.5 and 1.1 at generous budgets, where extraction systems are more accurate. That may explain why published results disagree. Jev selects as accurately as an LLM reranker at a third of the latency. Reranking lowers correct abstention.

Read together: Jev-Mem is the architecture claim, and the pre-registered study is a more cautious test showing the advantage depends on the budget.

## Security

**[Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation](https://arxiv.org/abs/2609.33401)**: Liu · 2026-09-27
Tests Jev, Laya, Decider and Bespoke Nimble as judges for prompt injection and harmful-request screening. Failures concentrate in particular attack groups and can hide behind good averages. Models can be confidently wrong. Separate allow/block thresholds raise automation mainly by blocking more aggressively, not by approving more.

**[Calibrated Decision Models for Autonomous Penetration-Testing Harnesses](https://arxiv.org/abs/2609.28940)**: Barbosa · 2026-09-24
Defines four decision points for pentest agents (finding adjudication, severity recalibration, agent pruning, confirmation loops). A 13-vulnerability NeuroSploit case study compares runs with and without Jev, and it proposes a domain-adapted model, Rave. This is a single small case study.

## Applications

**[Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables](https://arxiv.org/abs/2609.24052)**: Rafe, Das · 2026-09-21
Used on nearly 500,000 Texas crash narratives. F1 0.908 against human judgments and better than two frontier LLMs. Combined with existing coded data, it flagged an extra 10,747 injury and fatal crashes per year.

**[Replacing Large Language Models with Jev Decision Models for Low-Latency Edge Service Orchestration](https://arxiv.org/abs/2609.22753)**: Li, Wang, Gong, Lang, Yu · 2026-09-19 (rev. 09-26)
Across 8,280 verified requests and a live system, Jev cut median decision latency by 22.7–64.5% versus the fastest LLM, held accuracy on unseen services, and stayed resilient under heavy load where LLMs failed significantly.

## Related, not decision-model-specific

Useful background on cascades, the "when to escalate" problem these systems face:

- [Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades](https://arxiv.org/abs/2605.06350)
- [Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving](https://arxiv.org/abs/2606.27457)
- [NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs](https://arxiv.org/abs/2609.12582)

(Titles confirmed against arXiv; I haven't read these abstracts closely, so how closely they relate is unconfirmed.)

## Patterns visible across the papers

1. **Calibrate before you trust.** Every calibration paper found a gap between stated and actual confidence.
2. **Averages hide failure clusters.** Slice by category or attack type.
3. **Confidence gates are mixed.** Two studies found escalation thresholds missing their targets, while JEV-as-a-Judge reports a pre-frozen threshold beating GPT-6 on accuracy at 41% of the cost. The difference may be the task: reading a verdict off text vs. deriving one.
4. **Decomposition isn't free.** Splitting a decision changes the answer, in opposite directions for different models.
5. **Language and nuance are the weak spots** across models.

## Not yet covered

Only abstracts have been read, not full texts. Still to add: the RSI-Jev research write-up, and any paper on tool use with decision models (none found). The review at [ArXivIQ](https://arxiviq.substack.com/p/jev-and-the-emergence-of-system-one) surveys several of the papers above and mentions KV-cache sharing for parallel question evaluation and RLCD training for calibration. I haven't checked those claims against the papers.
