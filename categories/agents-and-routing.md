# Agents, browsers & routing

The pattern: a decision model handles frequent, closed, recoverable choices inside an agent loop, and an LLM handles reasoning and generation. Decision models can't call tools or produce free-form arguments, so something else proposes the options and your code executes ([Vercel](https://vercel.com/i/jev-agent-control), [layaAgent](https://github.com/vishalmysore/layaAgent)).

Descriptions are in original wording, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). The tools have not been run. The License column is what GitHub reports for each repo, not legal advice.

## Model routers (pick the cheapest capable LLM)

| Tool | What it does | License |
|---|---|---|
| [jev-router (gargpratyush)](https://github.com/gargpratyush/jev-router) | Picks the cheapest suitable model for each Claude Code task | MIT |
| [Codex Jev Router](https://github.com/suenot/codex-jev-router) | Cost-aware choice of Codex subagent models, with a portable setup guide | MIT |
| [jev-router (prismhq)](https://github.com/prismhq/jev-router) | Open-source router that chooses an LLM per request on top of LiteLLM | MIT |
| [pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) | Automatic model selection for the Pi agent, via Vercel AI Gateway | MIT |
| [jcm-router](https://github.com/adarshmishra07/jcm-router) | Local proxy that selects a Claude model and effort level per message while leaving the cached main chat untouched | MIT |
| [Switchboard](https://github.com/ruban-24/switchboard) | Router for model and reasoning effort in Claude Code and Codex; works with Jev or an experimental self-hosted model | Apache-2.0 |
| [Jevonian](https://github.com/xinyao27/jevonian) | Single local endpoint that picks the model for each turn, enforced in code | AGPL-3.0 |
| [rotom](https://github.com/RyanKung/rotom) | Local gateway compatible with the OpenAI and Anthropic APIs, authenticated through Codex OAuth | LGPL-3.0 |
| [hono-jev-router](https://github.com/yusukebe/hono-jev-router) | Semantic router for Hono: sends HTTP requests to handlers by meaning | MIT |

## Skill and tool selection

| Tool | What it does | License |
|---|---|---|
| [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) | Chooses an agent skill with confidence-aware typed decisions | MIT |
| [omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router) | One-pass skill router for OmO that trims the skill list in the system prompt | MIT |
| [pi-jev (TheoOliveira)](https://github.com/TheoOliveira/pi-jev) | Semantic tool routing and typed decisions for the Pi coding agent | MIT |
| [pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) | Routes Pi agent work through typed decisions (repo has no description) | MIT |
| [duet-agent](https://github.com/dzhng/duet-agent) | Full-stack agent harness with memory, long-running tasks and multi-agent relay; listed as keeping a Jev-backed routing table | Apache-2.0 |
| [layaAgent](https://github.com/vishalmysore/layaAgent) | Picks a tool, then picks arguments from extracted candidates ("extraction by choice"), with a confidence gate. Its own numbers (as of 04 Oct 2026): decides 32% of steps alone at 9.8% error, with thresholds tuned on a 36-task dev split | Apache-2.0 |

## Browser and computer-use agents

| Tool | What it does | License |
|---|---|---|
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Fast, low-cost web agent from the browser-use project | MIT |
| [Jev Browser](https://github.com/jkudish/jev-browser) | Browser automation where a decision model picks each step | MIT |
| [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) | Browser agent: a decision model picks actions from the page while an LLM reads and plans | MIT |
| [public-browser](https://github.com/Silbercue/public-browser) | Lets Claude Code and Cursor drive Chrome; its README cites a blind benchmark against another browser agent | MIT |
| [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) | Controls your everyday Chrome from AI agents without losing logins or focus | AGPL-3.0 |
| [jev-agent-browser](https://github.com/forvela/jev-agent-browser) | Fast, bounded browser agents with typed actions, built on agent-browser | MIT |
| [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) | Community Chrome extension that drives the current tab with a decision model | MIT |
| [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) | Action selection for Codex Computer Use | MIT |
| [jev-social](https://github.com/socai-io/jev-social) | Local-first research agent for Instagram, TikTok and LinkedIn; the decision model routes read-only operations | MIT |

## Agent memory

| Tool | What it does | License |
|---|---|---|
| [Jev-Mem](https://github.com/craftsland/Jev-Mem) | Reference code for [2609.23986](https://arxiv.org/abs/2609.23986): a decision-model controller handles memory typing, routing, scoring and stopping; the LLM only synthesizes the answer. Reported on LoCoMo in the paper's abstract: 6.6× faster memory build, 36.7% lower query latency. A second repo, [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem), also appears; Which one is canonical has not been determined. | MIT |

See also the pre-registered test in [papers.md](../papers.md#agent-memory): selecting raw turns with one decision-model call matched LLM extraction at a tight budget, but extraction won at generous budgets.

## Large option sets and memory

Found through GitHub searches on 04 Oct 2026 (see [GAPS.md](../GAPS.md)). Star counts as of that date.

| Tool | What it does | License |
|---|---|---|
| [NylonME](https://github.com/nylon-memory/NylonME) | Memory engine for agents that models each memory as strands (facts, emotions, timing, relationships, beliefs); its description says pairing with a decision model improves accuracy (46 stars) | Apache-2.0 |
| [jev-tree](https://github.com/lee-lou2/jev-tree) | Hierarchical knowledge service: a model carries context down a taxonomy tree to search and ingest Q&A; Rust, Axum and SQLite (0 stars) | MIT |
| [jev-native-agent-with-extended-options](https://github.com/6Mikao9/jev-native-agent-with-extended-options) | Research design for handling more options than a model's limit using virtualization and paging, with fallbacks (22 stars) | none stated |
| [jev-chat](https://github.com/adhyaay-karnwal/jev-chat) | Chatbot built from typed decisions using hierarchical speculative decoding over probabilities (4 stars) | MIT |
| [jev-graph-search](https://github.com/Emlembow/jev-graph-search) | Retrieval and evidence inspection over local Markdown, Obsidian and Logseq notes (11 stars) | MIT |
| [jev-second-brain](https://github.com/fellowship-dev/jev-second-brain) | Local-first Markdown memory alignment and source-linked search (3 stars) | MIT |

## Multi-model connectors and local Laya agents

| Tool | What it does | License |
|---|---|---|
| [system-one-connector](https://github.com/itsmostafa/system-one-connector) | MCP connector that gives an agent access to several decision models, including Jev and Laya (340 stars) | MIT |
| [laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent) | Local browser agent that makes its decisions with Laya, with no cloud or API key (17 stars) | Apache-2.0 |
| [omp-laya-judge](https://github.com/F0Rextasy/omp-laya-judge) | Local Laya judge as an MCP server and skill for oh-my-pi (7 stars) | unclear |

## Loop control

| Tool | What it does | License |
|---|---|---|
| [wakegate](https://github.com/shitianfang/wakegate) | Fail-open gate that asks whether waking a sleeping agent is worth a full LLM turn | MIT |
| [super-jev](https://github.com/Kevthetech143/super-jev) | Small harness that turns a decision-model answer into a bounded action | MIT |
| [augustus](https://github.com/24601/Augustus) | Agent skills for designing, training and evaluating application-specific decision systems | MIT |
| [Smithers](https://github.com/smithersai/smithers) | Agent workflow framework configured in TypeScript | MIT |
| [stanley-code](https://github.com/devagrawal09/stanley-code) | Bounded decision-model workflows for coding agents | MIT |
