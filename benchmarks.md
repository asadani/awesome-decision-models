# Benchmarks

What has been measured about decision models. **Read the "who measured" column first.** Very little here is independently replicated.

## Head-to-head: Laya vs Jev

Source: [Laya's own BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md), the model author's benchmark.

| Metric | Laya | Jev |
|---|---|---|
| typed-decisions accuracy (2,000 decisions) | 0.766 | 0.727 |
| AG News (4 labels) | 0.953 | 0.910 |
| DAIR Emotion (6 labels) | 0.600 | 0.480 |
| ECE after temperature fitting | 0.081 | 0.246 |
| p50 latency, 1 question (T4 GPU) | 32.8 ms | 236–276 ms |

**Caveat (from the source itself):** Jev figures are third-party published, never measured by the Laya authors, so sample sizes and prompts differ; treat them as indicative. Base Laya checkpoints score below a random baseline on typed-decisions and only rise after fine-tuning; moderation on held-out toxic-chat data is weak (0.530).

Independent-looking reruns, not yet cross-checked by me:

- [Luni/laya-jev-benchmark](https://huggingface.co/datasets/Luni/laya-jev-benchmark) (dataset): 400-case test split reports Jev 0.734 vs Laya 0.766, with p50 latency of 756 ms vs 484 ms (a different setup than the T4 numbers above).
- [pavanjava/jev_and_laya_benchmarking](https://github.com/pavanjava/jev_and_laya_benchmarking)
- [harrymunro/jev-laya-benchmark](https://github.com/harrymunro/jev-laya-benchmark)

Note how much latency depends on setup: 33 ms (T4, one question) vs 484 ms p50 in a different harness. Compare only within one harness.

## New entrants, vendor-reported (2026-09-30 to 10-02)

**All numbers in this section come from the vendors themselves, and I found no independent reproduction of any of them.** The benchmark panels, prompts and sample sizes differ, so don't compare across rows.

| Model | Claim | Source |
|---|---|---|
| **Clef / Clef-flash** (Cloudflare) | Median latency 38.8 ms (flash) / 209.3 ms (Clef) vs 524.1 ms for Jev. Per the post, best score on 7 of 10 benchmarks. Jev wins When2Call (80.97 vs 72.37 for Clef) and BRIGHT (47.52 vs 45.91). Examples: BANKING77 macro-F1 94.20 vs 79.74; BFCL 98.47 vs 95.75. | [Cloudflare](https://blog.cloudflare.com/clef-decision-models/) |
| **GLiDE** (Fastino) | "Decision Index" overall 64.81 vs Jev 57.91 (+6.90). Knowledge & Reasoning 62.9 vs 51.4; Tools & Automation 83.5 vs 75.1; CLadder 88.7% vs 72.6%; CRUXEval 92.6% vs 73.0%. The Decision Index spans 38 benchmarks in five areas; the post doesn't say who built it. No latency or price given. | [Fastino](https://fastino.ai/blog/introducing-glide-the-first-thinking-decision-model) |
| **pplx-decider-v1-27b** (Perplexity) | 85.71% vs Jev 84.51% across 11 benchmarks, 7,210 samples; biggest gap on RAGTruth (88.80% vs 77.27%). Jev wins 4 of the 11. The docs publish no benchmark table, per the summary. | [AI Weekly](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel) |
| **Strands Decider** (AWS) | JevBench v1 public set: 0.723 (167/231), ECE 0.052; answers at confidence ≥0.9 are right about 95% of the time on unseen short classification tasks. 115 ms median on an RTX 3090. Ranked 3rd of 33 in the 2B class on JevBench per the blog. | [Repo](https://github.com/strands-labs/strands-decider), [blog](https://strandsagents.com/blog/introducing-strands-decider/) |
| **llama.cpp runtime** | ~3 ms (Julia-1) to ~43 ms (OpenJev) per question | [ggml-org](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) |

Patterns worth noting:

- **Every vendor reports winning against Jev on its own panel.** The margins range from 1.2 points (Perplexity) to 6.9 (Fastino), and each panel was chosen by the vendor.
- **Jev keeps winning on a few tasks** in two independent vendor tables (When2Call and BRIGHT for Cloudflare; 4 of 11 for Perplexity). So a single "best model" is unlikely.
- **Jev's latency figures vary by who measures.** 524 ms median (Cloudflare), 236–276 ms (Laya's docs), 756 ms (Luni dataset). Latency depends on network and region, so measure from your own deployment.
- **Cost:** Jev's price is $0.042 / M input tokens, Perplexity's $0.04. A tweet-length summary of Cloudflare's results says Jev is 2–6× cheaper per token; the Cloudflare post itself gave no pricing in what I read, so that is unconfirmed.

## Broad independent evaluation

**[Evaluating and Benchmarking the System One Model Jev (2609.37647)](https://arxiv.org/abs/2609.37647)**, 2026-09-29. 37 datasets across domains. Jev reaches 95–99% accuracy on IMDB, SST-2, HellaSwag and ARC and beats competing models on most. Its probabilities are well-calibrated enough for selective prediction. Performance drops significantly on low-resource languages and nuanced labeling, and all tested models share those limits.

## Calibration findings

| Finding | Source |
|---|---|
| Laya is **under-confident** in one study: signed gap −0.214; temperature T=0.469 cut ECE from 0.214 to 0.037 | [2609.33843](https://arxiv.org/abs/2609.33843) |
| Laya's own docs say both checkpoints ship **over-confident** and need temperature fitting | [BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md) |
| An escalation gate targeting 10% error **missed its target** on both tracks | [2609.33843](https://arxiv.org/abs/2609.33843) |
| layaAgent at a tuned gate: decides 32% of steps alone at 9.8% error; `goal_met` AUROC 0.71 | [layaAgent](https://github.com/vishalmysore/layaAgent) |
| Independent OOD calibration test: 900 rule-generated tickets + 3 public benchmarks | [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) |

The first two rows disagree on the direction of miscalibration. That may come from different checkpoints or data, so measure on your own data.

## Consistency

**[Do System One Decisions Add Up? (2609.33971)](https://arxiv.org/abs/2609.33971)** tests whether a decision stays consistent when split into hierarchical steps. Across 72,000 questions, total variation distance ranged 0.219–0.689. Rebuilding a prediction through broad categories cut Jev's accuracy by 22.9 points and raised Laya's by 21.3. Accuracy gains sometimes came with worse calibration.

## Domain benchmarks

| Benchmark | What it measures |
|---|---|
| [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) | SQL ORDER BY ranking defensibility (pairwise inversion, ordinality, calibration, wording invariance, ties) under pre-registered gates |
| [jev-research-eval](https://github.com/jgridifier/jev-research-eval) | Reproducible eval harness for Jev Ultrafast |
| [WindTunnel](https://github.com/nekuda-ai/WindTunnel) | Browser-agent benchmark comparing configurations |
| [jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) | Jev vs GPT-4o-mini and Sonnet |
| [Jev Playground](https://github.com/hegargarcia/jev-playground) | Jev vs Luna, Haiku, Gemini |
| [LegalForecastBench](https://github.com/johnhughes3/LegalForecastBench) | Federal motion-to-dismiss ruling prediction |
| [Hanno-Labs/decision-bench](https://huggingface.co/datasets/Hanno-Labs/decision-bench) | Decision benchmark dataset |
| [LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | Common typed-decisions set used by several comparisons |
| [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam classification |
| [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619) | Measured run over 33,047 catalog entries |
| [Jev vs Mistral/Gemini for event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) | Local-events validation |

## Gaps

Things I could not find measured. Good candidates for contributions:

- Head-to-head on the **same harness, same hardware**, across hosted and open models
- Calibration **drift** over time or after model updates (jevcal fails CI on this, but I found no published study)
- Robustness under **adversarial input**
- Cost per correct decision, including escalations to an LLM
