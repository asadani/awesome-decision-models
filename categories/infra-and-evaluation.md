# Infra, SDKs & calibration/eval tooling

Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing unless noted; not run by me.

## Calibration, thresholds and evaluation

| Tool | What it does |
|---|---|
| [jevcal](https://github.com/abhixhek/jevcal) | Fits a per-question confidence threshold to a target accuracy on your labeled data, verifies on a held-out split, reports how much traffic still escalates to an LLM, and fails CI when a model update breaks locked thresholds. Can calibrate against an LLM teacher |
| [huncho](https://github.com/edgardcham/huncho) | TypeScript/Python/Go SDK: named decisions with enter/exit (hysteresis) thresholds, nested decision trees, JSONL journal, replay of a threshold change over recorded answers without new inference, Brier/reliability calibration |
| [jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) | Calibration, confidence-gating, latency and modeled-cost benchmarks for decisions inside DSPy workflows; threshold sweep 0.0–1.0 |
| [DSPy: Decision-Making with Jev Types](https://dspy.ai/current/tutorials/jev_decisions/) | Official DSPy tutorial; calibrates decision programs with the ReAnchor optimizer |
| [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | Out-of-distribution calibration test |
| [DecisionSmith](https://github.com/izam-mohammed/decisionsmith) | Fine-tune a decision model on your data with an LLM as teacher |

## Gateways and platforms

| Tool | What it does |
|---|---|
| [eve](https://github.com/vercel/eve) | Vercel's agent engine; Jev is its default evaluation model |
| [AI CLI](https://github.com/vercel-labs/ai-cli) | Vercel Labs CLI with an evaluation command |
| [ai-python](https://github.com/vercel-labs/ai-python) | Official Vercel AI SDK for Python |
| [new-api-typesafe-plugin](https://github.com/FFatTiger/new-api-plugin-typesafe) | Adds a `/v1/systemone` endpoint to the new-api gateway |
| [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) | Neon Function proxy |
| [Cline plugins](https://github.com/cline/plugins) | Official Cline plugin collection |
| [Atomic](https://github.com/bastani-inc/atomic) | Jev as a first-class structured-output provider |

## MCP servers and agent bridges

These expose a decision model **to** an LLM agent as tools. They don't give the decision model tools.

| Tool | What it does |
|---|---|
| [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) | Claim verification, content screening, ranking |
| [jev-mcp (blakestone-x)](https://github.com/blakestone-x/jev-mcp) | classify, score, check, match, screen tools |
| [decide-mcp](https://github.com/dakdevs/decide-mcp) | Configurable decision server with bias routing |
| [jev-use](https://github.com/shitianfang/jev-use) | Plugin for Claude Code / Codex / Pi exposing typed judgments as MCP tools |
| [Jevbridge](https://github.com/tacticocc/Jevbridge) | ACP and MCP adapter |
| [pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev) | System One judgments as Pi tools |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | Official installable agent skills |

## SDKs and clients

Python: [jevclient](https://pypi.org/project/jevclient/), [hunch (DataFrames)](https://github.com/steven-shoemaker/hunch) · TypeScript: [huncho](https://github.com/edgardcham/huncho) · Go: [jev-go](https://github.com/Stumble/jev-go) · Rust: [jevkit](https://github.com/ariel-frischer/jevkit) · Ruby: [ruby_decision_model](https://github.com/obie/ruby_decision_model), [s1_ruby](https://github.com/innocentdiaz/s1_ruby) · Kotlin: [kojev](https://github.com/ItisNoMatter/kojev) · Swift: [typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift) · Elixir: [jev](https://github.com/dannote/jev) · Scala: [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) · PHP: [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) · CLI: [jev-cli](https://github.com/tumf/jev-cli) · Node cookbook: [jev-cookbook](https://github.com/nexibeo/jev-cookbook)

## Local servers and proxies

[jev-local](https://github.com/us/jev-local), [ruling](https://github.com/bradAGI/ruling), [stuntd](https://github.com/bladedevoff/stuntd), [should-i-jev](https://github.com/yzbcs/Should-I-Jev) (migration CLI), [mini-jev](https://github.com/r-ms/mini-jev) (Jev interface on a local LLM)

## Gaps

- Observability and tracing for decision pipelines (the awesome-jev-tools list itself names this as missing)
- Open **Laya** tool registries; nearly all tooling above targets Jev
- Cross-step threshold optimization: every calibration tool I found tunes one question at a time
