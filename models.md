# Models

Decision models that answer typed Choice / Score / Noul questions. Sizes and licenses are as reported by the linked source; blank means I didn't confirm it. "Verified" means I read the linked page, not that I ran the model.

## Hosted

| Model | By | Access | Notes |
|---|---|---|---|
| **Jev** | TypeSafe AI | API; available on Vercel AI Gateway as `typesafe-ai/jev` (from 2026-09-16) | Launched 2026-09-15. $0.042 / M input tokens, output free. Typical latency reported 236–276 ms per call. [Vercel model page](https://vercel.com/ai-gateway/models/jev) · [Simon Willison](https://simonwillison.net/2026/Sep/21/jev/) |
| **Jev Ultrafast** | TypeSafe AI | API | Faster variant referenced in agent-control docs and browser-agent tools such as [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast). |

## Open weights

| Model | Size | Base | License | Notes |
|---|---|---|---|---|
| **[Laya](https://github.com/NandhaKishorM/laya)** ([HF](https://huggingface.co/convaiinnovations/laya)) | ~421M | ModernBERT-large + head | Apache-2.0 | Convai Innovations. Non-autoregressive; ~33 ms/question on a T4 (self-reported). Multilingual checkpoint: [laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) (~0.3B). Runs via ONNX; [Node/TS runner](https://github.com/receptron/laya). Reported limit: ~20 Choice options. English checkpoint "collapses outside English" per its own docs. |
| **[RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev)** | 0.8B, 2B | Qwen 3.5 | Code MIT; checkpoints Apache-2.0 | Produced by a self-improving research loop. v3.0 reports 15-benchmark mean 0.756, ECE 0.066, ~10 ms/decision (self-reported). [HF v1.0 2B](https://huggingface.co/shgao/rsi-jev-v1.0-qwen3.5-2b) |
| **[autotrust/JEV-27B](https://huggingface.co/blog/autotrust/autotrustjev-27b-fast-calibrated-decisions-and-ful)** | 27B | | Apache-2.0 | "Fast calibrated decisions and full reasoning"; larger model that can also reason. |
| **[Mapika/decider-2b](https://github.com/Mapika/decider)** | 2B | Qwen 3.5 | | Fine-tune that emits typed decisions. Described in one roundup as the most-used open model; unverified. |
| **[Kev](https://github.com/jaredpalmer/kev)** | 0.5B–27B family | Qwen 2.5 / 3.5 | | Trainable replica; sources disagree on exact sizes. |
| **SemIf (formerly OpenJev)** | wraps e.g. 4B | frozen Qwen 3.5 | MIT | By Theodore Lee per one roundup. Reads logprobs of candidate tokens in one pass, so no training required. I haven't located its repo. |
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
- **Need a decision model that can also fall back to reasoning:** the larger open models (e.g. JEV-27B).
- **Non-English:** check the checkpoint; Laya's English one is reported to degrade badly, so use the multilingual one.
