# Business & operations

Triage, routing and screening for teams. Descriptions are my own words, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). I have not run the tools. The License column is what GitHub reports for each repo, not legal advice.

| Tool | What it does | License |
|---|---|---|
| [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow) | Routes incoming emails to the matching handler (repo has no description) | none stated |
| [typeful-triage](https://github.com/cephalization/jev-triage) | Issue-triage dashboard that avoids a full repository sync | MIT |
| [Notra](https://github.com/usenotra/notra) | GEO tool that asks AI assistants the questions buyers ask (listed as using Jev for brand-visibility checks) | AGPL-3.0 |
| [secondlayer](https://github.com/ryanwaits/secondlayer) | Self-hosted database of decoded Stacks blockchain data (how it uses Jev is not shown in the repo description) | MIT |
| [typesafe-jev CV screener](https://github.com/gtaras7/typesafe-jev) | Screens a folder of CVs against an editable policy using typed judgments (see the caution below) | MIT |
| [opencompany](https://github.com/useopencompany/opencompany) | AI workspace with chat, durable tasks, workflows and a knowledge base; listed as using Jev for approval review | MIT |
| [Refix](https://refix.ai) | Product experimentation and growth automation service (closed; no repo) | n/a |
| [GeekLink Subtitle Translator](https://github.com/GeekLinkDev/jev-subtitle-translator) | Translates SRT subtitles with an LLM and checks each translation with Jev | GPL-3.0 |
| [json-render](https://github.com/vercel-labs/json-render) | Generative-UI framework from Vercel Labs; listed as using Jev to pick components | Apache-2.0 |
| [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | High-throughput sifter for synthetic and pretraining datasets, with a Rust streaming core | MIT |

## Caution: people decisions

Decision models return probabilities with no explanation, and none of the sources I read audits them for bias in people-related decisions. Simon Willison [describes](https://simonwillison.net/2026/Sep/21/jev/) a one-off experiment where Jev rated Cupertino the best and East Palo Alto the worst Bay Area city on a yes/no "Good city?" question. That is an anecdote, not evidence of bias in hiring. My own suggestion, not a claim from the sources: keep a human in the loop and audit outcomes if you build screening tools.
