# Agents, browsers & routing

The pattern: a decision model handles frequent, closed, recoverable choices inside an agent loop, and an LLM handles reasoning and generation. Decision models can't call tools or produce free-form arguments, so something else proposes the options and your code executes ([Vercel](https://vercel.com/i/jev-agent-control), [layaAgent](https://github.com/vishalmysore/layaAgent)).

Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing unless noted; not run by me.

## Model routers (pick the cheapest capable LLM)

| Tool | What it does |
|---|---|
| [jev-router (gargpratyush)](https://github.com/gargpratyush/jev-router) | Routes Claude Code tasks to the cheapest capable model |
| [Codex Jev Router](https://github.com/suenot/codex-jev-router) | Selects Codex subagent model and reasoning tier |
| [jev-router (prismhq)](https://github.com/prismhq/jev-router) | LiteLLM-based per-request model routing |
| [pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) | Per-request routing for the Pi agent |
| [jcm-router](https://github.com/adarshmishra07/jcm-router) | Picks Claude model and reasoning effort per message |
| [Switchboard](https://github.com/ruban-24/switchboard) | Selects model and effort while avoiding cache disruption |
| [Jevonian](https://github.com/xinyao27/jevonian) | Proxy choosing model route and thinking level |
| [rotom](https://github.com/RyanKung/rotom) | OpenAI-compatible API gateway |
| [hono-jev-router](https://github.com/yusukebe/hono-jev-router) | Hono middleware for semantic routing |

## Skill and tool selection

| Tool | What it does |
|---|---|
| [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) | Confidence-aware agent skill selection |
| [omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router) | Shrinks the skill catalog with routing |
| [pi-jev (TheoOliveira)](https://github.com/TheoOliveira/pi-jev) | Semantic tool routing for Pi |
| [pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) | Routes Pi work through typed decisions |
| [duet-agent](https://github.com/dzhng/duet-agent) | Agent harness maintaining a Jev-backed routing table |
| [layaAgent](https://github.com/vishalmysore/layaAgent) | Picks a tool, then picks arguments from extracted candidates ("extraction by choice"), with a confidence gate. Its own numbers (as of 04 Oct 2026): decides 32% of steps alone at 9.8% error, with thresholds tuned on a 36-task dev split |

## Browser and computer-use agents

| Tool | What it does |
|---|---|
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Decides browser actions and target elements |
| [Jev Browser](https://github.com/jkudish/jev-browser) | Drives a browser with Jev deciding each step |
| [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) | Decision model picks actions while an LLM plans |
| [public-browser](https://github.com/Silbercue/public-browser) | Jev loop deciding Chrome actions |
| [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) | Chrome MCP with a Jev semantic micro-loop |
| [jev-agent-browser](https://github.com/forvela/jev-agent-browser) | Delegates bounded tasks with a Jev loop |
| [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) | Chrome extension port of Jev Ultrafast |
| [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) | Action selection for Codex Computer Use |
| [jev-social](https://github.com/socai-io/jev-social) | Selects socai CLI operations on social media |

## Agent memory

| Tool | What it does |
|---|---|
| [Jev-Mem](https://github.com/craftsland/Jev-Mem) | Reference code for [2609.23986](https://arxiv.org/abs/2609.23986): a decision-model controller handles memory typing, routing, scoring and stopping; the LLM only synthesizes the answer. Reported on LoCoMo in the paper's abstract: 6.6× faster memory build, 36.7% lower query latency. A second repo, [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem), also appears; I haven't determined which is canonical. |

See also the pre-registered test in [papers.md](../papers.md#agent-memory): selecting raw turns with one decision-model call matched LLM extraction at a tight budget, but extraction won at generous budgets.

## Loop control

| Tool | What it does |
|---|---|
| [wakegate](https://github.com/shitianfang/wakegate) | Decides whether to wake a sleeping agent |
| [super-jev](https://github.com/Kevthetech143/super-jev) | Turns a Jev answer into a bounded action |
| [augustus](https://github.com/24601/Augustus) | Maps Choice, Score and Noul onto classical methods |
| [Smithers](https://github.com/smithersai/smithers) | TypeScript workflow framework |
| [stanley-code](https://github.com/devagrawal09/stanley-code) | Bounded workflows keeping agent judgments typed |
