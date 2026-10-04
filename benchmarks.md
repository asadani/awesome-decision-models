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
