# Security, guardrails & moderation

Allow / block / escalate decisions are the most natural fit for decision models. They are also where the papers found the sharpest failure modes: confident wrong answers and failure clusters hidden by averages (see [2609.33401](https://arxiv.org/abs/2609.33401)). Treat these as a layer, never the only control.

## Agent permission and tool-call gates

| Tool | What it does | License |
|---|---|---|
| [jev-guard](https://github.com/leepokai/jev-guard) | Auto mode for coding agents: risk-scores each tool call using session context | MIT |
| [jev-axi](https://github.com/shiftynick/jev-axi) | Agent-friendly CLI for fast calibrated judgments (pick, rate, check, rank, triage) | MIT |
| [pi-jev](https://github.com/y0usaf/pi-jev) | Decision layer for the Pi agent: a measured tool-call gate plus an ask tool | MIT |
| [pi-verdict](https://github.com/jesset/pi-verdict) | Minimal permission gate for Pi in the style of Claude Code auto mode | MIT |
| [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) | Checks side-effecting tool calls in Pi against what you asked for | MIT |
| [fx](https://github.com/vercel-labs/fx) | Unix-style coding agent from Vercel Labs; listed as having a built-in permission reviewer | Apache-2.0 |

## Software supply chain

| Tool | What it does | License |
|---|---|---|
| [is-malicious](https://github.com/luantak/is-malicious) | Codebase scanner that helps avoid running malicious code | MIT |

## Content moderation

| Tool | What it does | License |
|---|---|---|
| [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | Discord moderation bot that scores messages (repo has no description) | MIT |
| [mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation) | Input-moderation processor for Mastra agents, in a single file | MIT |
| [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam filtering with yes/no questions, compared against TF-IDF baselines | MIT |

## Research

- [2609.33401](https://arxiv.org/abs/2609.33401): security-judge evaluation across Jev, Laya, Decider and Bespoke Nimble
- [2609.28940](https://arxiv.org/abs/2609.28940): decision layers for pentest agents
- Laya's own docs report weak held-out moderation: 0.530 accuracy and macro-F1 0.400 on toxic-chat, which they call "barely above chance on a balanced split" ([BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md), as of 04 Oct 2026). Calibrate on your own data before relying on any model here.
