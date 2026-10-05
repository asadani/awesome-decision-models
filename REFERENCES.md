# References and credits

This repository is a guide that points to other people's work. This page credits that work, records the license of every repository linked here, and explains what this repository does and does not take from each source. Facts below were checked on **04 Oct 2026**; licenses can change, so check the source before reusing anything.

Not legal advice. If you are the author of something listed here and want a correction or removal, open an issue and it will be handled promptly.

## What is taken, and what is not

| This repository does | This repository does not |
|---|---|
| Link to the original source for every claim | Copy source code, README prose, images or datasets |
| Report facts and figures (numbers, dates, sizes, license names), attributed to the source and dated | Present vendor claims as its own measurements |
| Describe each tool in original wording, based on that project's own GitHub description | Reproduce another list's wording |
| Use very short quotations (a phrase or a sentence) where wording matters, with a link | Quote at length |
| Summarize paper abstracts in original wording, with the arXiv link | Redistribute papers |

Linking to a repository does not give anyone a license to its code. Use each project under its own terms.

### Transparency note

An earlier version of this repository (commits `dc37a66` to `a1f46c2`) carried short tool descriptions taken from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing, which has no license. Those descriptions were rewritten from each project's own GitHub description in the version that added this file. The earlier text still exists in git history.

## Discovery sources

These were used to find projects and papers. No text was copied from them. Where a project appears in the tables, its description is original and its license is read from the project's own repo.

| Source | License | How it was used |
|---|---|---|
| [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) | None stated | Found most of the tool projects; see the transparency note above |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | None stated | Related list, cross-reference only |
| [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) | Unclear (GitHub could not classify it) | Related list, cross-reference only |
| [Open Jev collection (Hugging Face)](https://huggingface.co/collections/Ferr0/open-jev-typed-decision-models) | Per model | Found open-weight models; each model's license is read from its own page |
| GitHub repository search, run on 04 Oct 2026 | n/a | Counted and found projects for [GAPS.md](GAPS.md) |
| [Jev in the Wild (arXiv 2609.30216)](https://arxiv.org/abs/2609.30216) | arXiv | Aggregate ecosystem statistics (category counts, stars); only the numbers are reused |

## Projects, models and vendors used as fact sources

| Source | License (as of 04 Oct 2026) | What was used |
|---|---|---|
| TypeSafe AI, [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) | Proprietary API | Release date, price, context size |
| [Simon Willison's post on Jev](https://simonwillison.net/2026/Sep/21/jev/) | © author | Price at launch; quoted phrase on weaknesses; the "good city" anecdote |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) and [Laya on Hugging Face](https://huggingface.co/convaiinnovations/laya) (Convai Innovations) | Apache-2.0 | Model size, architecture, benchmark figures and stated limitations from its BENCHMARKS.md |
| [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider) and [AWS Strands blog](https://strandsagents.com/blog/introducing-strands-decider/) | Apache-2.0 (code); blog © AWS | Size, base model, benchmark figures, training time, limitations |
| [Cloudflare Clef blog](https://blog.cloudflare.com/clef-decision-models/) and [Clef](https://huggingface.co/Cloudflare/clef) / [Clef-flash](https://huggingface.co/Cloudflare/clef-flash) | Apache-2.0 (weights); blog © Cloudflare | Latency and benchmark tables, architecture, licensing |
| [Fastino GLiDE blog](https://fastino.ai/blog/introducing-glide-the-first-thinking-decision-model) | © Fastino; API only | Benchmark figures, availability, context limit |
| [Perplexity pplx-decider-v1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) and [AI Weekly's summary](https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel) | Apache-2.0 (weights); article © AI Weekly | Size, license, pricing, benchmark figures |
| [OpenAI DevDay community post](https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006) | © OpenAI | Decisions API status and model name |
| [llama.cpp decision-models post](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) (ggml-org) | © author; the post reports OpenJev as CC BY-NC 4.0 and the others as Apache-2.0 | Supported models, sizes, licenses, speeds, commands |
| [Shanghua-Gao/RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) | MIT (code); Apache-2.0 (weights, per its README) | Versions, benchmark figures |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | MIT | Evaluation figures and architecture notes from its README and docs |
| [vishalmysore/layaAgent](https://github.com/vishalmysore/layaAgent) | Apache-2.0 | Gate results and design statements |
| [abhixhek/jevcal](https://github.com/abhixhek/jevcal) | MIT | What the tool does |
| [izam-mohammed/decisionsmith](https://github.com/izam-mohammed/decisionsmith) | Apache-2.0 | What the tool does, data-size guidance |
| [craftsland/Jev-Mem](https://github.com/craftsland/Jev-Mem) | MIT | Link to reference code |
| [pavanjava/jev_and_laya_benchmarking](https://github.com/pavanjava/jev_and_laya_benchmarking) | MIT | Rerun figures |
| [autotrust JEV-27B post](https://huggingface.co/blog/autotrust/autotrustjev-27b-fast-calibrated-decisions-and-ful) | © author; model stated as Apache-2.0 | Model existence and license |

## Papers

Abstract-level summaries in original wording. Each paper is the property of its authors; follow the arXiv link for terms.

| arXiv | Title | First author | Date |
|---|---|---|---|
| [2609.37647](https://arxiv.org/abs/2609.37647) | Evaluating and Benchmarking the System One Model Jev | Deußer | 2026-09-29 |
| [2609.34227](https://arxiv.org/abs/2609.34227) | When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model | Sharma | 2026-09-28 |
| [2609.33971](https://arxiv.org/abs/2609.33971) | Do System One Decisions Add Up? A Study of Probabilistic Coherence | Joy | 2026-09-27 |
| [2609.33843](https://arxiv.org/abs/2609.33843) | Laya as a Typed Probabilistic Assessor: An Independent Reproduction and a Preregistered Study of Calibration and Selective Escalation | Nandakishore | 2026-09-27 |
| [2609.33401](https://arxiv.org/abs/2609.33401) | Evaluating System One Models for Agent Security Decisions | Liu | 2026-09-27 |
| [2609.30216](https://arxiv.org/abs/2609.30216) | Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem | Ling | 2026-09-24 |
| [2609.29769](https://arxiv.org/abs/2609.29769) | JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places | Rao | 2026-09-24 |
| [2609.28940](https://arxiv.org/abs/2609.28940) | Calibrated Decision Models for Autonomous Penetration-Testing Harnesses | Barbosa | 2026-09-24 |
| [2609.28587](https://arxiv.org/abs/2609.28587) | NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees | Ye | 2026-09-23 |
| [2609.26550](https://arxiv.org/abs/2609.26550) | JEV-as-a-Judge: Accept When Confident, Escalate When Unsure | Li | 2026-09-22 |
| [2609.24052](https://arxiv.org/abs/2609.24052) | Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev) | Rafe | 2026-09-21 |
| [2609.23986](https://arxiv.org/abs/2609.23986) | Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents | Jiang | 2026-09-21 |
| [2609.22753](https://arxiv.org/abs/2609.22753) | Replacing Large Language Models with Jev Decision Models for Low-Latency Edge Service Orchestration | Li | 2026-09-19 |

Background papers listed in [papers.md](papers.md) but not summarized: [2605.06350](https://arxiv.org/abs/2605.06350), [2606.27457](https://arxiv.org/abs/2606.27457), [2609.12582](https://arxiv.org/abs/2609.12582).

## Articles and documentation

Linked in [LEARN.md](LEARN.md). All © their respective authors; only links, original-wording summaries and short quoted phrases are used.

[Hugging Face community guide (paidaxccc)](https://huggingface.co/blog/paidaxccc/what-is-jev-model-a-practical-guide-to-typed-ai-de) · [LangChain](https://www.langchain.com/blog/building-a-harness-with-jev) · [Michał Chromiak](https://mchromiak.github.io/articles/2026/Sep/17/Typed-Decision-Models-Jev-and-Laya-in-Agentic-AI/) · [Vercel: Jev in the agent loop](https://vercel.com/i/jev-agent-control) · [Vercel Knowledge Base](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk) · [Firecrawl](https://www.firecrawl.dev/blog/what-is-jev) · [DSPy docs](https://dspy.ai/current/tutorials/jev_decisions/) · [dev.to: What is Laya?](https://dev.to/vishalmysore/what-is-laya-laya-vs-jev-with-live-demo-4j6e)

## Hugging Face models and datasets linked

License as reported by the Hugging Face API on 04 Oct 2026.

| Model or dataset | License |
|---|---|
| [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) | apache-2.0 |
| [Cloudflare/clef](https://huggingface.co/Cloudflare/clef) | apache-2.0 |
| [convaiinnovations/laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) | apache-2.0 |
| [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya) | apache-2.0 |
| [cua-ai/cua-s1-forms](https://huggingface.co/cua-ai/cua-s1-forms) | mit |
| [datasets/Hanno-Labs/decision-bench](https://huggingface.co/datasets/Hanno-Labs/decision-bench) | other |
| [datasets/LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | apache-2.0 |
| [datasets/Luni/laya-jev-benchmark](https://huggingface.co/datasets/Luni/laya-jev-benchmark) | apache-2.0 |
| [Hanno-Labs/bosun-v3.1-1.7b](https://huggingface.co/Hanno-Labs/bosun-v3.1-1.7b) | apache-2.0 |
| [juspay/xor](https://huggingface.co/juspay/xor) | apache-2.0 |
| [perplexity-ai/pplx-decider-v1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) | apache-2.0 |
| [shgao/rsi-jev-v1.0-qwen3.5-2b](https://huggingface.co/shgao/rsi-jev-v1.0-qwen3.5-2b) | apache-2.0 |
| [ZefanCai/Open-Jev-9B](https://huggingface.co/ZefanCai/Open-Jev-9B) | apache-2.0 |

OpenJev 27B is **CC BY-NC 4.0 (non-commercial)** according to the llama.cpp post; most other open models above are Apache-2.0.

## Index of all 195 GitHub repositories linked

Licenses as reported by GitHub's API on 04 Oct 2026: 134 MIT, 25 Apache-2.0, 20 NONE, 10 NOASSERTION, 3 AGPL-3.0, 1 GPL-3.0, 1 CC-BY-4.0, 1 LGPL-3.0. Repos are linked, not copied. The license groups below are what matter if you plan to reuse code.

**MIT** (134): [24601/Augustus](https://github.com/24601/Augustus), [abhixhek/jevcal](https://github.com/abhixhek/jevcal), [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev), [adarshmishra07/jcm-router](https://github.com/adarshmishra07/jcm-router), [adhyaay-karnwal/jev-chat](https://github.com/adhyaay-karnwal/jev-chat), [agent-labs-dev/fastbrowse](https://github.com/agent-labs-dev/fastbrowse), [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate), [AkashPriyadarshii/jev-git](https://github.com/AkashPriyadarshii/jev-git), [AkashPriyadarshii/jev-scout](https://github.com/AkashPriyadarshii/jev-scout), [AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo), [alterhq/typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift), [andududu/jeview](https://github.com/andududu/jeview), [ariel-frischer/jevkit](https://github.com/ariel-frischer/jevkit), [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval), [blakestone-x/jev-mcp](https://github.com/blakestone-x/jev-mcp), [bradAGI/ruling](https://github.com/bradAGI/ruling), [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot), [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast), [Butochnikov/laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev), [cephalization/jev-triage](https://github.com/cephalization/jev-triage), [choyiny/decidebench](https://github.com/choyiny/decidebench), [chy4pro/jev-for-chrome](https://github.com/chy4pro/jev-for-chrome), [CodeAlive-AI/mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation), [coldteadotai/abide](https://github.com/coldteadotai/abide), [compozy/yoshi](https://github.com/compozy/yoshi), [craftsland/Jev-Mem](https://github.com/craftsland/Jev-Mem), [dakdevs/decide-mcp](https://github.com/dakdevs/decide-mcp), [dannote/jev](https://github.com/dannote/jev), [DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest), [davertor/jev-slop-guard](https://github.com/davertor/jev-slop-guard), [david-cermak/jevlike-esp32](https://github.com/david-cermak/jevlike-esp32), [Dearest/plotveil](https://github.com/Dearest/plotveil), [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review), [devagrawal09/stanley-code](https://github.com/devagrawal09/stanley-code), [dharun-cohere/jev-sortwell](https://github.com/dharun-cohere/jev-sortwell), [doeixd/jev-pref](https://github.com/doeixd/jev-pref), [dzhng/jevgrep](https://github.com/dzhng/jevgrep), [edgardcham/huncho](https://github.com/edgardcham/huncho), [Emlembow/jev-graph-search](https://github.com/Emlembow/jev-graph-search), [FeiLiuEM/open-medical-jev](https://github.com/FeiLiuEM/open-medical-jev), [fellowship-dev/jev-second-brain](https://github.com/fellowship-dev/jev-second-brain), [forvela/jev-agent-browser](https://github.com/forvela/jev-agent-browser), [frostney/clean-code-review](https://github.com/frostney/clean-code-review), [gaborishka/jev-canvas](https://github.com/gaborishka/jev-canvas), [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router), [gbesse/jev-workflow](https://github.com/gbesse/jev-workflow), [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router), [gtaras7/typesafe-jev](https://github.com/gtaras7/typesafe-jev), [harrymunro/jev-laya-benchmark](https://github.com/harrymunro/jev-laya-benchmark), [hotchpotch/jev-reranker](https://github.com/hotchpotch/jev-reranker), [innocentdiaz/s1_ruby](https://github.com/innocentdiaz/s1_ruby), [islee23520/omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router), [ItisNoMatter/kojev](https://github.com/ItisNoMatter/kojev), [itsmostafa/system-one-connector](https://github.com/itsmostafa/system-one-connector), [jekozyra/pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router), [jesset/pi-verdict](https://github.com/jesset/pi-verdict), [jkudish/jev-browser](https://github.com/jkudish/jev-browser), [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp), [jmanhype/jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab), [joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction), [jolehuit/jev-downloads-sorter](https://github.com/jolehuit/jev-downloads-sorter), [Kelbie/hunch](https://github.com/Kelbie/hunch), [Kevthetech143/super-jev](https://github.com/Kevthetech143/super-jev), [kitze/pagegrade](https://github.com/kitze/pagegrade), [kitze/unclutter](https://github.com/kitze/unclutter), [komikat/jev-bfs](https://github.com/komikat/jev-bfs), [kylemclaren/jevpdf](https://github.com/kylemclaren/jevpdf), [kylemclaren/jevql](https://github.com/kylemclaren/jevql), [kylemclaren/jevsearch](https://github.com/kylemclaren/jevsearch), [lee-lou2/jev-tree](https://github.com/lee-lou2/jev-tree), [leepokai/jev-guard](https://github.com/leepokai/jev-guard), [leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction), [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem), [luantak/is-malicious](https://github.com/luantak/is-malicious), [lukstei/slop-grader](https://github.com/lukstei/slop-grader), [mandu5/jevcompat](https://github.com/mandu5/jevcompat), [MANISH007700/tidy](https://github.com/MANISH007700/tidy), [MarissaFamularo/citation-verifier](https://github.com/MarissaFamularo/citation-verifier), [maxxo-1/jev-file-library-organizer](https://github.com/maxxo-1/jev-file-library-organizer), [mejiasd3v/pi-jev-router](https://github.com/mejiasd3v/pi-jev-router), [nexibeo/jev-cookbook](https://github.com/nexibeo/jev-cookbook), [nexibeo/jev-organize](https://github.com/nexibeo/jev-organize), [nikkoxgonzales/jev-certify](https://github.com/nikkoxgonzales/jev-certify), [noplan-inc/limpet](https://github.com/noplan-inc/limpet), [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed), [obie/ruby_decision_model](https://github.com/obie/ruby_decision_model), [olanotolu/jevbetter](https://github.com/olanotolu/jevbetter), [pavanjava/jev_and_laya_benchmarking](https://github.com/pavanjava/jev_and_laya_benchmarking), [phyous/tsai-sc](https://github.com/phyous/tsai-sc), [prismhq/jev-router](https://github.com/prismhq/jev-router), [r-ms/mini-jev](https://github.com/r-ms/mini-jev), [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock), [receptron/laya](https://github.com/receptron/laya), [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone), [ryanwaits/secondlayer](https://github.com/ryanwaits/secondlayer), [sameerkhan24/decidekit](https://github.com/sameerkhan24/decidekit), [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration), [Shanghua-Gao/RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev), [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi), [shitianfang/jev-use](https://github.com/shitianfang/jev-use), [shitianfang/wakegate](https://github.com/shitianfang/wakegate), [Silbercue/public-browser](https://github.com/Silbercue/public-browser), [silverstein/minutes](https://github.com/silverstein/minutes), [smithersai/smithers](https://github.com/smithersai/smithers), [socai-io/jev-social](https://github.com/socai-io/jev-social), [steven-shoemaker/hunch](https://github.com/steven-shoemaker/hunch), [Stumble/jev-go](https://github.com/Stumble/jev-go), [suenot/codex-jev-router](https://github.com/suenot/codex-jev-router), [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search), [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov), [tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge), [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction), [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner), [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev), [thruwire/foreman](https://github.com/thruwire/foreman), [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev), [TKY-27/JevSlop](https://github.com/TKY-27/JevSlop), [tumf/jev-cli](https://github.com/tumf/jev-cli), [typesafe-ai/skills](https://github.com/typesafe-ai/skills), [useopencompany/opencompany](https://github.com/useopencompany/opencompany), [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay), [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit), [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red), [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip), [valentynkit/jev.nvim](https://github.com/valentynkit/jev.nvim), [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike), [WiktorB2004/llama-index-jev](https://github.com/WiktorB2004/llama-index-jev), [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev), [yikangy873-gif/jev-desktop](https://github.com/yikangy873-gif/jev-desktop), [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench), [yohanargentina-oss/Foq](https://github.com/yohanargentina-oss/Foq), [yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router), [yzbcs/Should-I-Jev](https://github.com/yzbcs/Should-I-Jev), [zljr/file-guide](https://github.com/zljr/file-guide)

**Apache-2.0** (25): [ably-labs/jev-pong](https://github.com/ably-labs/jev-pong), [bladedevoff/stuntd](https://github.com/bladedevoff/stuntd), [ChenneyZhuang/laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent), [cline/plugins](https://github.com/cline/plugins), [dzhng/duet-agent](https://github.com/dzhng/duet-agent), [FFatTiger/new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe), [izam-mohammed/decisionsmith](https://github.com/izam-mohammed/decisionsmith), [jamesward/zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai), [jaredpalmer/kev](https://github.com/jaredpalmer/kev), [johnhughes3/LegalForecastBench](https://github.com/johnhughes3/LegalForecastBench), [Mapika/decider](https://github.com/Mapika/decider), [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya), [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel), [nitinnat/jev-file-organizer](https://github.com/nitinnat/jev-file-organizer), [nylon-memory/NylonME](https://github.com/nylon-memory/NylonME), [OmniJev/OneJev](https://github.com/OmniJev/OneJev), [OmniJev/PlayJev](https://github.com/OmniJev/PlayJev), [ruban-24/switchboard](https://github.com/ruban-24/switchboard), [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider), [vercel-labs/fx](https://github.com/vercel-labs/fx), [vercel-labs/json-render](https://github.com/vercel-labs/json-render), [vercel/eve](https://github.com/vercel/eve), [vishalmysore/layaAgent](https://github.com/vishalmysore/layaAgent), [wfzyx/von](https://github.com/wfzyx/von), [zhengxuyu/litjev](https://github.com/zhengxuyu/litjev)

**CC-BY-4.0** (1): [Jevals/jevals-data](https://github.com/Jevals/jevals-data)

**AGPL-3.0** (3). Strong copyleft. These are linked only; do not copy their code into closed-source work.

[GoldenLoaf24h/browserclaw](https://github.com/GoldenLoaf24h/browserclaw), [usenotra/notra](https://github.com/usenotra/notra), [xinyao27/jevonian](https://github.com/xinyao27/jevonian)

**GPL-3.0** (1). Copyleft. Link only.

[GeekLinkDev/jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator)

**LGPL-3.0** (1). Weak copyleft. Link only.

[RyanKung/rotom](https://github.com/RyanKung/rotom)

**License unclear** (10). GitHub could not identify a standard license. Check the repo before reuse. Link only.

[aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade), [bastani-inc/atomic](https://github.com/bastani-inc/atomic), [F0Rextasy/omp-laya-judge](https://github.com/F0Rextasy/omp-laya-judge), [jgridifier/jev-research-eval](https://github.com/jgridifier/jev-research-eval), [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev), [legacybridge-tech/pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev), [milanboers/jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon), [vercel-labs/ai-python](https://github.com/vercel-labs/ai-python), [whysooraj/laya-file-organizer](https://github.com/whysooraj/laya-file-organizer), [zhihz/openjev](https://github.com/zhihz/openjev)

**No license stated** (20). No license stated, so default copyright applies (all rights reserved). These are linked and described in original wording; no code or prose is copied. Ask the owner before reusing anything.

[6Mikao9/jev-native-agent-with-extended-options](https://github.com/6Mikao9/jev-native-agent-with-extended-options), [andrelandgraf/safer-with-jev](https://github.com/andrelandgraf/safer-with-jev), [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments), [diegocp01/living-folders](https://github.com/diegocp01/living-folders), [direwolfiy/JevPi](https://github.com/direwolfiy/JevPi), [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario), [GiesN/typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow), [grmkris/robo-harness](https://github.com/grmkris/robo-harness), [hegargarcia/jev-playground](https://github.com/hegargarcia/jev-playground), [kavehmz/typesafe-playground](https://github.com/kavehmz/typesafe-playground), [kxzk/typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo), [mgaitan/sqlite-jev](https://github.com/mgaitan/sqlite-jev), [raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury), [Shogo-nfrealmusic/jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval), [sosopop/jev_stock](https://github.com/sosopop/jev_stock), [unicodeveloper/jevocks](https://github.com/unicodeveloper/jevocks), [us/jev-local](https://github.com/us/jev-local), [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools), [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli), [yibie/awesome-jev](https://github.com/yibie/awesome-jev)


## Website tooling

| Component | License | Use |
|---|---|---|
| [Python-Markdown](https://github.com/Python-Markdown/markdown) | BSD-3-Clause | Converts the Markdown to HTML at build time |
| [Newsreader](https://fonts.google.com/specimen/Newsreader), [Inter](https://fonts.google.com/specimen/Inter), [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) | SIL Open Font License 1.1 | Page fonts, loaded from Google Fonts (the same fonts as the parent blog) |
| GitHub Pages and GitHub Actions | GitHub terms | Hosting and deployment |

The site's design follows the parent blog's design system at [tech.anujsadani.in](https://tech.anujsadani.in/).

## Trademarks and affiliation

Jev and TypeSafe AI, Laya, Strands, Clef, GLiDE, Perplexity, OpenAI and other names are the property of their owners. This repository is independent and is not affiliated with, endorsed by, or sponsored by any of them. Third-party projects named here, including tools that call themselves "unofficial," belong to their authors.

## This repository's own license

The original text in this repository (curation, summaries and analysis) is licensed under [CC BY 4.0](LICENSE): you may share and adapt it, including commercially, if you credit Anuj Sadani and link to this repository. This covers only the original text. Third-party material keeps its own licenses as listed above, and CC BY 4.0 does not apply to it.
