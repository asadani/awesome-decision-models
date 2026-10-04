# Business & operations

Triage, routing and screening for teams. Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing; not run by me.

| Tool | What decision it makes |
|---|---|
| [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow) | Routes inbound emails to the right handler |
| [typeful-triage](https://github.com/cephalization/jev-triage) | Multiplayer issue-triage dashboard |
| [Notra](https://github.com/usenotra/notra) | Routes brand-visibility classifiers to Jev Boolean decisions at a 0.5 threshold |
| [secondlayer](https://github.com/ryanwaits/secondlayer) | Slack gate and fault triage for a Stacks service |
| [typesafe-jev CV screener](https://github.com/gtaras7/typesafe-jev) | Screens CVs against an editable policy. See the caution below |
| [opencompany](https://github.com/useopencompany/opencompany) | Runs approval review through a decision model |
| [Refix](https://refix.ai) | Product experiments and growth automation |
| [GeekLink Subtitle Translator](https://github.com/GeekLinkDev/jev-subtitle-translator) | Reviews translated subtitle pairs for omissions or meaning changes |
| [json-render](https://github.com/vercel-labs/json-render) | Vercel Labs UI framework using Jev to select components |
| [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | Sifts synthetic data rows with Jev checks |

## Caution: people decisions

Simon Willison [reports](https://simonwillison.net/2026/Sep/21/jev/) an experiment where Jev ranked one city highest and a neighboring one lowest for being a "good city," and warns against hiring uses. Biased, unexplainable scores are a poor fit for decisions about people. Keep a human in the loop and audit outcomes if you build in this area.
