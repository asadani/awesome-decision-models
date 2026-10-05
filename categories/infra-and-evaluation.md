# Infra, SDKs & calibration/eval tooling

Descriptions are in original wording, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). The tools have not been run. The License column is what GitHub reports for each repo, not legal advice.

## Calibration, thresholds and evaluation

| Tool | What it does | License |
|---|---|---|
| [jevcal](https://github.com/abhixhek/jevcal) | Fits a per-question confidence threshold to a target accuracy on your labeled data, verifies on a held-out split, reports how much traffic still escalates to an LLM, and fails CI when a model update breaks locked thresholds. Can calibrate against an LLM teacher | MIT |
| [huncho](https://github.com/edgardcham/huncho) | TypeScript/Python/Go SDK: named decisions with enter/exit (hysteresis) thresholds, nested decision trees, JSONL journal, replay of a threshold change over recorded answers without new inference, Brier/reliability calibration | MIT |
| [jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) | Calibration, confidence-gating, latency and modeled-cost benchmarks for decisions inside DSPy workflows; threshold sweep 0.0–1.0 | MIT |
| [DSPy: Decision-Making with Jev Types](https://dspy.ai/current/tutorials/jev_decisions/) | Official DSPy tutorial; calibrates decision programs with the ReAnchor optimizer | n/a |
| [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | Out-of-distribution calibration test | MIT |
| [DecisionSmith](https://github.com/izam-mohammed/decisionsmith) | Fine-tune a decision model on your data with an LLM as teacher | Apache-2.0 |

## Gateways and platforms

| Tool | What it does | License |
|---|---|---|
| [eve](https://github.com/vercel/eve) | Open framework for building agents (Vercel); listed as using Jev as a default evaluation model | Apache-2.0 |
| [AI CLI](https://github.com/vercel-labs/ai-cli) | Vercel Labs terminal CLI; listed as including a Jev evaluation command | none stated |
| [ai-python](https://github.com/vercel-labs/ai-python) | Vercel AI SDK for Python | unclear |
| [new-api-typesafe-plugin](https://github.com/FFatTiger/new-api-plugin-typesafe) | Adds a native /v1/systemone endpoint to the new-api gateway | Apache-2.0 |
| [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) | Neon Function proxy for the Neon AI Gateway with Jev-based routing | none stated |
| [Cline plugins](https://github.com/cline/plugins) | Official curated plugins for the Cline CLI and extensions | Apache-2.0 |
| [Atomic](https://github.com/bastani-inc/atomic) | Coding-agent runtime where you define the process in natural language; listed as supporting Jev structured output | unclear |

## MCP servers and agent bridges

These expose a decision model **to** an LLM agent as tools. They don't give the decision model tools.

| Tool | What it does | License |
|---|---|---|
| [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) | Exposes typed judgments as MCP tools | MIT |
| [jev-mcp (blakestone-x)](https://github.com/blakestone-x/jev-mcp) | MCP server with typed classify, score, check, match and screen tools | MIT |
| [decide-mcp](https://github.com/dakdevs/decide-mcp) | Configurable decision MCP server with percentage scores and bias-profile routing | MIT |
| [jev-use](https://github.com/shitianfang/jev-use) | Plugin for Claude Code, Codex and Pi that hands text-free agent steps to the decision model | MIT |
| [Jevbridge](https://github.com/tacticocc/Jevbridge) | ACP and MCP adapter bridging a decision model with any LLM | MIT |
| [pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev) | Pi extension exposing judgments as five tools the model can call | unclear |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | Agent skills for building with the System One API (official) | MIT |

## SDKs and clients

Python: [jevclient](https://pypi.org/project/jevclient/), [hunch (DataFrames)](https://github.com/steven-shoemaker/hunch) · TypeScript: [huncho](https://github.com/edgardcham/huncho) · Go: [jev-go](https://github.com/Stumble/jev-go) · Rust: [jevkit](https://github.com/ariel-frischer/jevkit) · Ruby: [ruby_decision_model](https://github.com/obie/ruby_decision_model), [s1_ruby](https://github.com/innocentdiaz/s1_ruby) · Kotlin: [kojev](https://github.com/ItisNoMatter/kojev) · Swift: [typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift) · Elixir: [jev](https://github.com/dannote/jev) · Scala: [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) · PHP: [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) · CLI: [jev-cli](https://github.com/tumf/jev-cli) · Node cookbook: [jev-cookbook](https://github.com/nexibeo/jev-cookbook)

## Local servers and proxies

[jev-local](https://github.com/us/jev-local), [ruling](https://github.com/bradAGI/ruling), [stuntd](https://github.com/bladedevoff/stuntd), [should-i-jev](https://github.com/yzbcs/Should-I-Jev) (migration CLI), [mini-jev](https://github.com/r-ms/mini-jev) (Jev interface on a local LLM)

## More calibration, evaluation and observability projects

Found through GitHub searches on 04 Oct 2026 (see [GAPS.md](../GAPS.md)). All are young and small; star counts as of that date.

| Tool | What it does | License |
|---|---|---|
| [jev-certify](https://github.com/nikkoxgonzales/jev-certify) | Uses conformal risk control to turn calibrated probabilities into certified routing thresholds, and audits them with prediction-powered inference (1 star) | MIT |
| [jevcompat](https://github.com/mandu5/jevcompat) | Spec and conformance test suite for Jev-compatible API servers, with a mock server and a GitHub Action (0 stars) | MIT |
| [jeview](https://github.com/andududu/jeview) | Unofficial local visualizer that shows every decision-model call your code makes; not affiliated with TypeSafe (61 stars) | MIT |
| [jevals-data](https://github.com/Jevals/jevals-data) | Independent benchmark data comparing Jev and LLMs on accuracy, calibration and cost, with per-decision logs (1 star) | CC-BY-4.0 |
| [decidebench](https://github.com/choyiny/decidebench) | Benchmark of decision models and LLMs on 400 contrastive decisions: accuracy, cost per task and latency (1 star) | MIT |
| [Foq](https://github.com/yohanargentina-oss/Foq) | Free, local, open-source alternative to Jev that claims about 25 ms per decision (self-reported; 10 stars) | MIT |
| [decidekit](https://github.com/sameerkhan24/decidekit) | TypeScript and Python client with confidence-aware decisions, fallbacks and per-call cost tracking (2 stars) | MIT |
| [jev-workflow](https://github.com/gbesse/jev-workflow) | Decision contracts, adversarial testing, tracing, stability and privacy controls (0 stars) | MIT |
| [JevPi](https://github.com/direwolfiy/JevPi) | Decision-first agent loop on Pi with an LLM fallback, full tracing and paired evaluations (1 star) | none stated |

## Gaps

- Observability and tracing for decision pipelines: only a few small projects (for example jeview, 61 stars), see [GAPS.md](../GAPS.md)
- Open **Laya** tool registries; nearly all tooling above targets Jev
- Cross-step threshold optimization: every calibration tool found tunes one question at a time
