# Models

Decision models that answer typed Choice / Score / Noul questions. Sizes, licenses and figures are as stated by the linked source on **04 Oct 2026**; blank means it was not confirmed. The linked pages were read; none of the models were run.

## Hosted

| Model | By | Access | Notes |
|---|---|---|---|
| **Jev** | TypeSafe AI | API; listed on Vercel AI Gateway as `typesafe-ai/jev` (release date 15 Sep 2026, 32K context, as of 04 Oct 2026) | Input price was $0.042 / M tokens with free output at launch ([Willison, 21 Sep 2026](https://simonwillison.net/2026/Sep/21/jev/)); Vercel lists $0.04 / M (as of 04 Oct 2026). Median latency varies by who measures: 524.1 ms in [Cloudflare's test](https://blog.cloudflare.com/clef-decision-models/), 236–276 ms per [Laya's docs](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md). Text-only per Cloudflare (as of 01 Oct 2026). [Vercel model page](https://vercel.com/ai-gateway/models/jev) |
| **Jev Ultrafast** | TypeSafe AI | API | Faster variant referenced in agent-control docs and browser-agent tools such as [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast). |
| **Decisions API (GPT-6 Luna)** | OpenAI | Limited preview, announced at DevDay 2026 | Uses Luna to classify inputs, route requests or choose an action from predefined answers. Pricing not disclosed; official docs sparse. [OpenAI community post](https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006) |
| **Clef / Clef-flash** | Cloudflare | Workers AI; weights also open (see below) | Announced 2026-10-01. Takes images. 64k context vs Jev's 32k. [Cloudflare blog](https://blog.cloudflare.com/clef-decision-models/) |
| **pplx-decider-v1-27b** | Perplexity | Decisions API, $0.04 / M input tokens, free output; weights also open | Announced 2026-10-01. [Summary](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel) |
| **GLiDE** | Fastino | API only (not open weights) | Announced 2026-09-30. "Thinking" decision model: computes a fast probability distribution, and if the leading answer is uncertain it runs reasoning and folds that into the final probabilities. 40k-token context; oversized requests are rejected, not truncated. [Fastino blog](https://fastino.ai/blog/introducing-glide-the-first-thinking-decision-model) |

## Open weights

| Model | Size | Base | License | Notes |
|---|---|---|---|---|
| **[Laya](https://github.com/NandhaKishorM/laya)** ([HF](https://huggingface.co/convaiinnovations/laya)) | ~421M | ModernBERT-large + head | Apache-2.0 | Convai Innovations. Non-autoregressive; 32.8 ms/question p50 on a T4 per its own docs (as of 04 Oct 2026). Accuracy figures are self-reported and the headline typed-decisions score is from a fine-tuned checkpoint; see [benchmarks.md](benchmarks.md). Multilingual checkpoint: [laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) (~0.3B). Runs via ONNX; [Node/TS runner](https://github.com/receptron/laya). Reported limit: ~20 Choice options. English checkpoint "collapses outside English" per its own docs. |
| **[Strands Decider](https://github.com/strands-labs/strands-decider)** ([weights](https://huggingface.co/StrandsAgents)) | 1.9B | Qwen3.5-2B-Base, LoRA, pointer head instead of LM head | Apache-2.0 | AWS (Strands Agents), announced 2026-10-01. JevBench v1 public set: 0.723 (167/231), ECE 0.052 (as of 04 Oct 2026; self-reported). Latency on an RTX 3090 (WSL2): 115 ms median / 299 ms p95. The repo says it retrains in about 11 hours on one RTX 3090 (or 1 h 10 min on eight H100s), so the recipe is reproducible on consumer hardware. The repo had 324 GitHub stars on 04 Oct 2026. Binary and multiple-choice only; the authors say it is unsuited to coding, chat or summarization. `pip install strands-decider`. [Blog](https://strandsagents.com/blog/introducing-strands-decider/) |
| **[Clef-flash](https://huggingface.co/Cloudflare/clef-flash)** / **[Clef](https://huggingface.co/Cloudflare/clef)** | 9B / 27B | frozen Qwen 3.5-9B / Qwen 3.8-27B + low-rank adapters (Clef rank 256) | Apache-2.0 | Cloudflare. Non-autoregressive, with a vision encoder for images. Median latency in Cloudflare's own test (as of 01 Oct 2026): 38.8 ms (flash), 209.3 ms (Clef), 524.1 ms (Jev). Trained with synthetic data, Brier loss and RLCD. See [benchmarks.md](benchmarks.md) for the vendor-reported scores and what is unreplicated. |
| **[pplx-decider-v1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)** | 27B | Qwen3.8-27B | Apache-2.0 | Perplexity, released 01 Oct 2026. 262,144-token context. Per the [AI Weekly summary](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel) of its docs: responses under two seconds for a few hundred input tokens, up to 23 s near the context limit. |
| **Julia-1** | 144M | | Apache-2.0 | Multilingual (50+ languages), no images; the fastest model in the llama.cpp post (~3 ms/question there). Listed in [llama.cpp's decision-model post](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp). |
| **lev** | 4B | | Apache-2.0 | English only. Listed in the llama.cpp post. Its source repo was not found. |
| **OpenJev (27B)** | 27B | | **CC BY-NC 4.0** | Multilingual (en, de, fr, hi, zh, ja) and image input; ~43 ms/question in llama.cpp. **Non-commercial license**, unlike most others here. Listed in the llama.cpp post. |
| **[RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev)** | 0.8B, 2B; later a 3B vision-language release | Qwen 3.5 | Code MIT; weights Apache-2.0 (following the base model) | Produced by a self-improving research loop. As of 04 Oct 2026 the README lists v3.0 (15-benchmark suite 0.756, ECE 0.066), v4.0-VL (01 Oct 2026; image top-1 0.803 on held-out image benchmarks, ECE 0.043) and a v5.0-VL 3B weights release. It reports about 10 ms for a second question about a document already read, not for every decision. All figures self-reported. [HF v1.0 2B](https://huggingface.co/shgao/rsi-jev-v1.0-qwen3.5-2b) |
| **[autotrust/JEV-27B](https://huggingface.co/blog/autotrust/autotrustjev-27b-fast-calibrated-decisions-and-ful)** | 27B | | Apache-2.0 | "Fast calibrated decisions and full reasoning"; larger model that can also reason. |
| **[Mapika/decider-2b](https://github.com/Mapika/decider)** | 2B | Qwen 3.5 | | Fine-tune that emits typed decisions; listed in the Open Jev collection on Hugging Face. |
| **[Kev](https://github.com/jaredpalmer/kev)** | 0.5B–27B family | Qwen 2.5 / 3.5 | | Trainable replica; sources disagree on exact sizes. |
| **SemIf (formerly OpenJev)** | wraps e.g. 4B | frozen Qwen3.5-4B | MIT | Per a secondary roundup (search result; not verified): reads logprobs of candidate tokens in one pass, so no training required. Its repo was not located. |
| **[openjev (zhihz)](https://github.com/zhihz/openjev)** | | | | Described as an independent local bilingual decision model. May be unrelated to SemIf despite the name; unverified. |
| **[NanoJev](https://github.com/TianyuCodings/NanoJev)** | 0.6B | | | Parallel decision model with training pipeline. |
| **[von](https://github.com/wfzyx/von)** | 395M | | | Non-autoregressive System One model. |
| **[juspay/xor](https://huggingface.co/juspay/xor)** | 35B | Qwen 3.6-35B-A3B | | Listed in the Open Jev collection. |
| **[Open-Jev-9B](https://huggingface.co/ZefanCai/Open-Jev-9B)** | 9B | Qwen 3.5-9B | | |
| **[bosun-v3.1-1.7b](https://huggingface.co/Hanno-Labs/bosun-v3.1-1.7b)** | 1.7B | | | Hanno Labs. |
| **[OneJev](https://github.com/OmniJev/OneJev)** | four sizes | | | Multimodal System One. |
| **[CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms)** | | | | Specialist form-field scorer. |
| **[Open Medical Jev](https://github.com/FeiLiuEM/open-medical-jev)** | | | | Medical exam evaluation. |

More in the [Open Jev collection](https://huggingface.co/collections/Ferr0/open-jev-typed-decision-models) (also lists Eikos-27B, mojev 0.9B, Lumma-fev-0.6b, agent-jev 0.6B, Tev1-4B-experimental).

## Runtimes

**llama.cpp** added decision-model support on 2026-10-02 ([ggml-org post](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp)). It serves a `/v1/systemone` endpoint with `choice`, `score` and `noul` question types, and supports five models: Julia-1 (144M), Laya (421M), Kev-4B, lev (4B) and OpenJev (27B). Start one with `llama serve -hf ggml-org/Kev-4B-GGUF`; router mode serves several models and picks per request. Reported speed: ~3 ms (Julia-1) to ~43 ms (OpenJev) per question. This makes open decision models usable without writing your own ONNX plumbing. The post's example values are rounded.

Other runtimes: [Laya via ONNX/Node](https://github.com/receptron/laya), [jev-local](https://github.com/us/jev-local), [ruling](https://github.com/bradAGI/ruling).

## Keep the model swappable

Five new decision models or APIs appeared within a few days of each other (GLiDE 09-30; Strands, Clef and Perplexity 10-01; OpenAI's preview at DevDay). Cloudflare says Clef uses the same System One API as Jev, and llama.cpp serves a `/v1/systemone` endpoint. The others were not checked. Pin the model version, keep a calibration set, and put the model behind a thin interface so you can switch.

## Training and conversion kits

Turn your own data, or any LLM, into a decision model.

- [DecisionSmith](https://github.com/izam-mohammed/decisionsmith): fine-tune Jev/Laya on your data with an LLM as the teacher. Under ~1,000 rows trains only the head.
- [LitJev](https://github.com/zhengxuyu/litjev): turn any Qwen into a fast decision model.
- [jevlike](https://github.com/vinnylarouge/jevlike) / [jevbetter](https://github.com/olanotolu/jevbetter): training library and improved one-pass option scorer.
- [ruling](https://github.com/bradAGI/ruling): Jev-compatible server built from logits.
- [jev-local](https://github.com/us/jev-local): local `/v1/systemone` server.

## Which one when

Suggested from the evidence in [benchmarks.md](benchmarks.md), not proven:

- **Need zero setup, moderate volume:** hosted Jev.
- **Private data, high volume, latency-sensitive:** an open model, calibrated on your own labels.
- **Need a decision model that can also fall back to reasoning:** the larger open models (e.g. JEV-27B), or GLiDE, which reasons only when its first-pass answer is uncertain (API-only).
- **Want to train your own on a single consumer GPU:** Strands Decider (about 11 hours on an RTX 3090).
- **Need image input:** Clef or OpenJev (OpenJev is non-commercial only).
- **Lowest latency, small footprint:** Julia-1 (144M) or Laya (421M) through llama.cpp.
- **Non-English:** check the checkpoint; Laya's English one is reported to degrade badly, so use the multilingual one.
