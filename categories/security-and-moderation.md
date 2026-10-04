# Security, guardrails & moderation

Allow / block / escalate decisions are the most natural fit for decision models. They are also where the papers found the sharpest failure modes: confident wrong answers and failure clusters hidden by averages (see [2609.33401](https://arxiv.org/abs/2609.33401)). Treat these as a layer, never the only control.

## Agent permission and tool-call gates

| Tool | What it does |
|---|---|
| [jev-guard](https://github.com/leepokai/jev-guard) | Prompt-injection and dangerous-action guard for agents |
| [jev-axi](https://github.com/shiftynick/jev-axi) | PreToolUse gate scoring commands for destructiveness |
| [pi-jev](https://github.com/y0usaf/pi-jev) | Tool-call gate for the Pi coding agent |
| [pi-verdict](https://github.com/jesset/pi-verdict) | Pi permission gate using Choice decisions |
| [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) | Checks tool calls against user intent |
| [fx](https://github.com/vercel-labs/fx) | Coding agent with a built-in permission reviewer |

## Software supply chain

| Tool | What it does |
|---|---|
| [is-malicious](https://github.com/luantak/is-malicious) | Checks package source and build files |

## Content moderation

| Tool | What it does |
|---|---|
| [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | Discord bot scoring messages |
| [mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation) | Mastra input processor |
| [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam classification evaluation |

## Research

- [2609.33401](https://arxiv.org/abs/2609.33401): security-judge evaluation across Jev, Laya, Decider and Bespoke Nimble
- [2609.28940](https://arxiv.org/abs/2609.28940): decision layers for pentest agents
- Laya's own docs report weak held-out moderation accuracy (0.530 on toxic-chat), so calibrate on your own data before relying on it here.
