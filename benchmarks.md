# Benchmarks

What has been measured about decision models. **Read the "who measured" column first.** Very little here is independently replicated. Figures were checked against the cited pages on **04 Oct 2026**; scores, latencies and prices may have changed since.

## Head-to-head: Laya vs Jev (Laya's own docs)

Source: [Laya's BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md), written by Laya's author. Values as of 04 Oct 2026.

| Metric | Laya | Jev |
|---|---|---|
| typed-decisions accuracy (2,000 decisions) | 0.766 | 0.727 (Jev 1.13.0, published figure) |
| AG News (4 labels) | 0.953 | 0.910 |
| DAIR Emotion (6 labels) | 0.600 | 0.480 |
| ECE after temperature fitting | 0.081 | 0.246 |
| p50 latency, 1 question (T4 GPU) | 32.8 ms | 236–276 ms |

**Read these caveats before quoting the table:**

- The doc says the typed-decisions 0.766 is the **fine-tuned** checkpoint, with "no committed result file behind it yet." Base checkpoints score below a random baseline on that task and only rise with fine-tuning.
- The AG News and DAIR Emotion Laya cells are from the Applications run. The committed T4 English suites give lower numbers: 0.947 (AG News) and 0.573 (DAIR Emotion).
- The Jev numbers (accuracy, ECE, latency) are third-party, never measured by the Laya authors, who had no TypeSafe API access: "sample sizes and prompts differ; treat them as indicative."
- Weak spots the doc reports itself: held-out toxic-chat moderation is 0.530 accuracy with macro-F1 0.400 ("barely above chance"); the English checkpoint "collapses outside English" and stays confident while doing so; both checkpoints "ship over-confident"; keep Choice questions under about 20 options.

Other reruns:

- [pavanjava/jev_and_laya_benchmarking](https://github.com/pavanjava/jev_and_laya_benchmarking) reports, on a 400-case typed-decisions split: accuracy Jev 0.734 vs Laya 0.766; p50 latency 756 ms vs 484 ms; p95 2,957 ms vs 663 ms. It notes Jev's score is close to its published 0.727 and Laya's matches its model card. This is a single-author repo (as of 04 Oct 2026), and Laya's 0.766 matches the fine-tuned figure above.
- [Luni/laya-jev-benchmark](https://huggingface.co/datasets/Luni/laya-jev-benchmark) (dataset) and [harrymunro/jev-laya-benchmark](https://github.com/harrymunro/jev-laya-benchmark): related datasets and harnesses. I did not extract numbers from them.

Latency depends heavily on harness: Laya's docs cite 236–276 ms for Jev (third-party), Cloudflare measured 524.1 ms median, and pavanjava measured 756 ms. Compare only within one harness.

## New entrants, vendor-reported (30 Sep – 02 Oct 2026)

**Every number in this section comes from the vendors themselves, and I found no independent reproduction.** Panels, prompts and sample sizes differ, so don't compare across rows. Values as of 04 Oct 2026.

| Model | What was reported | Source |
|---|---|---|
| **Clef / Clef-flash** (Cloudflare, 01 Oct 2026) | Median latency 38.8 ms (Clef-flash), 209.3 ms (Clef) vs 524.1 ms for Jev; p95 122.4 / 238.6 / 536.0 ms. In the same table Laya's median is 5.8 ms, "very fast but trades off quality" (its BFCL score is 38.13). **By my reading of Cloudflare's 10-row table**, a Clef model has the top score on 7 of 10 benchmarks, Jev on 2 (When2Call 80.97 vs 72.37; BRIGHT 47.52 vs 45.91), and a "DiffusionGemma Jev" entry on PhishNChips (85.35). The post itself reports beating Jev "in 3 out of 4 areas" of TypeSafe's own eval suite and states results across 43 benchmarks. Examples: BANKING77 macro-F1 94.20 vs 79.74; BFCL 98.47 vs 95.75. | [Cloudflare blog](https://blog.cloudflare.com/clef-decision-models/) |
| **GLiDE** (Fastino, 30 Sep 2026) | "Decision Index" overall 64.81 vs Jev's *published* 57.91 (+6.90), using the Decision Index 0.2.1 scorer; leads across all five areas and 31 of 38 benchmarks. Knowledge & Reasoning 62.9 vs 51.4; Tools & Automation 83.5 vs 75.1; CLadder 88.7% vs 72.6%; CRUXEval 92.6% vs 73.0%. The post states "these results come from our own complete run." It doesn't say who built the Decision Index, and gives no latency or price. | [Fastino blog](https://fastino.ai/blog/introducing-glide-the-first-thinking-decision-model) |
| **pplx-decider-v1-27b** (Perplexity, 01 Oct 2026) | 85.71% vs Jev 84.51% on Perplexity's own 11-benchmark, 7,210-sample panel; widest gap RAGTruth 88.80% vs 77.27%; Jev ahead on 4 of the 11. Per the news summary, Perplexity's docs publish no benchmark table, so the figures trace to the company's own posts. | [AI Weekly summary](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel); the [model card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) also shows these scores |
| **Strands Decider** (AWS, 01 Oct 2026) | JevBench v1 public set (231 tasks): accuracy 0.723 (167/231); Brier 0.342, ECE 0.052. Answers at confidence ≥0.9 are right about 95% of the time on unseen short classification tasks. Latency on an RTX 3090 (WSL2): 115 ms median / 299 ms p95. The blog ranks it 3rd of 33 in the 2B class on accuracy and 1st of 30 on calibration excluding just-over-2B models. | [Repo README](https://github.com/strands-labs/strands-decider), [blog](https://strandsagents.com/blog/introducing-strands-decider/) |
| **llama.cpp runtime** (02 Oct 2026) | About 3 ms (Julia-1) to about 43 ms (OpenJev) per question | [ggml-org post](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) |

Patterns worth noting:

- **Every vendor reports beating Jev on its own panel**, by 1.2 points (Perplexity) to 6.9 points (Fastino). Each panel was chosen by the vendor.
- **Jev still wins some tasks** in two vendor tables (When2Call and BRIGHT in Cloudflare's; 4 of 11 in Perplexity's), so a single "best model" is unlikely.
- **Cost:** Jev was $0.042 / M input tokens at launch ([Willison](https://simonwillison.net/2026/Sep/21/jev/)); Perplexity charges $0.04 / M ([AI Weekly](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel)). Cloudflare's post gives no pricing, and I found no cited source for claims that Jev is 2–6× cheaper per token.

## Broad independent evaluation

**[Evaluating and Benchmarking the System One Model Jev (2609.37647)](https://arxiv.org/abs/2609.37647)**, 29 Sep 2026. Zero-shot evaluation of jev-1.13.0 on 37 datasets, compared with Qwen3.8-27B and Gemma-4-E4B on identical requests. Jev reaches 95–99% accuracy on IMDB, SST-2, HellaSwag and ARC and 86.7% on Belebele across 122 languages. It beats Qwen on 27 of 37 datasets (none of Qwen's nine leads fall outside the bootstrap intervals) and Gemma on all 37. All three models degrade on low-resource languages and fine-grained or noisy labeling.

## Calibration findings

| Finding | Source |
|---|---|
| Laya is **under-confident** in one preregistered study: signed confidence-accuracy gap −0.214; a single fitted temperature (T=0.469) took held-out ECE from 0.204 to 0.037 | [2609.33843](https://arxiv.org/abs/2609.33843), 27 Sep 2026 |
| Laya's own docs say both checkpoints **ship over-confident** and need temperature fitting | [BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md) |
| The frozen escalation gate beat random escalation but **missed its 10% accepted-error target** | [2609.33843](https://arxiv.org/abs/2609.33843) |
| layaAgent at its tuned gate decides 32% of steps alone at 9.8% error; `goal_met` AUROC 0.71. Thresholds were chosen on a 36-task dev split, a small sample | [layaAgent README](https://github.com/vishalmysore/layaAgent) |
| Independent OOD calibration test: 900 rule-generated tickets plus 3 public benchmarks | [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) (listed in awesome-jev-tools; not run by me) |

The first two rows disagree on the direction of miscalibration. That may come from different checkpoints or data, so measure on your own data.

## Consistency

**[Do System One Decisions Add Up? (2609.33971)](https://arxiv.org/abs/2609.33971)**, 27 Sep 2026. Jev and English Laya on 2,500 matched examples per system across TREC, CLINC150 and MASSIVE (72,000 classification questions). Mean category-level total variation distance ranged 0.219–0.349 for Jev and 0.424–0.689 for Laya. On CLINC150, reconstructing predictions through broad categories reduced Jev's accuracy by 22.9 points and improved Laya's by 21.3; the same directions held across all three datasets. Accuracy improvements sometimes came with worse calibration.

## Domain benchmarks

Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing (as of 04 Oct 2026); I confirmed the links resolve but did not run them.

| Benchmark | What it measures |
|---|---|
| [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) | SQL ORDER BY ranking defensibility (pairwise inversion, ordinality, calibration, wording invariance, ties) under pre-registered gates |
| [jev-research-eval](https://github.com/jgridifier/jev-research-eval) | Reproducible eval harness for Jev Ultrafast |
| [WindTunnel](https://github.com/nekuda-ai/WindTunnel) | Browser-agent benchmark comparing configurations |
| [jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) | Jev vs GPT-4o-mini and Sonnet |
| [Jev Playground](https://github.com/hegargarcia/jev-playground) | Jev vs Luna, Haiku, Gemini |
| [LegalForecastBench](https://github.com/johnhughes3/LegalForecastBench) | Federal motion-to-dismiss ruling prediction |
| [Hanno-Labs/decision-bench](https://huggingface.co/datasets/Hanno-Labs/decision-bench) | Decision benchmark dataset (listed in the Open Jev collection) |
| [LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | Typed-decisions set used by several comparisons |
| [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam classification |
| [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619) | Measured run over 33,047 catalog entries (X post; not verified, as X pages don't load for automated checks) |
| [Jev vs Mistral/Gemini for event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) | Local-events validation (blocks automated fetches; unverified) |

## Gaps

Things I could not find measured. Good candidates for contributions:

- Head-to-head on the **same harness and hardware** across hosted and open models, including the new entrants
- Calibration **drift** over time or after model updates (jevcal fails CI on this, but I found no published study)
- Robustness under **adversarial input**
- Cost per correct decision, including escalations to an LLM
- Independent replication of any vendor claim above
