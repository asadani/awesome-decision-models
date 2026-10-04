# Business & operations

Triage, routing and screening for teams. Descriptions are my own words, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). I have not run the tools. The License column is what GitHub reports for each repo, not legal advice.

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

Decision models return probabilities with no explanation, and none of the sources I read audits them for bias in people-related decisions. Simon Willison [describes](https://simonwillison.net/2026/Sep/21/jev/) a one-off experiment where Jev rated Cupertino the best and East Palo Alto the worst Bay Area city on a yes/no "Good city?" question. That is an anecdote, not evidence of bias in hiring. My own suggestion, not a claim from the sources: keep a human in the loop and audit outcomes if you build screening tools.
