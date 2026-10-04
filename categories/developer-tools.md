# Developer tools & coding agents

Gates, reviewers and context tools for coding workflows. Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing unless noted; not run by me.

## Retrieval and context

| Tool | What it does |
|---|---|
| [jevgrep](https://github.com/dzhng/jevgrep) (`jg`) | Answers "where is X?" with relevant files and source excerpts. Walks folders, then files, then declarations, and uploads only what earlier steps didn't rule out. Its [README](https://github.com/dzhng/jevgrep) reports (as of 04 Oct 2026) 8 of 10 SWE-bench tasks solved with and without it, on ten tuned Python tasks. Coding-agent cost fell from $7.62 to $5.44 (28.6%, excluding Jev's own cost); a later run including Jev's cost measured 25.8% lower total cost; a still later 0.5.0 run cut Jev cost about 59% but combined cost was 2–3% higher. All self-reported, single runs, not a speed claim. |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | Claude Code: replaces the compaction summary |
| [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) | Prunes stale tool history |
| [fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) | Codex context-compaction port |
| [jev-pruner](https://github.com/tamaratran/jev-pruner) | Trims Bash output in Claude Code |
| [yoshi](https://github.com/compozy/yoshi) | Proxy judging which conversation history is needed |

## Review and pre-commit gates

| Tool | What it does |
|---|---|
| [jev-git](https://github.com/AkashPriyadarshii/jev-git) | Sub-second pre-commit and pre-push gate screening diffs |
| [jev-commit](https://github.com/valentynkit/jev-commit) | Judges whether the commit message matches the diff |
| [DiffJury](https://github.com/raihankhan-rk/diffjury) | Routes pull requests by risk before human review |
| [jev-review](https://github.com/devagrawal09/jev-review) | Staged code-review workflow gating each stage |
| [Blink](https://blink.review) | CLI that checks diffs in place of an LLM reviewer |
| [Hunch](https://github.com/Kelbie/hunch) | Plain-English rule checking against code |
| [Abide](https://github.com/coldteadotai/abide) | Flags rule violations in coding-agent edits |
| [jev-pref](https://github.com/doeixd/jev-pref) | Checks project preferences against diffs |
| [Clean Code Judge](https://github.com/frostney/clean-code-review) | Scores files on 31 Clean Code smells |
| [Supercov](https://github.com/supercorp-ai/supercov) | Answers twelve properties per source file |
| [jev.nvim](https://github.com/valentynkit/jev.nvim) | Neovim plugin scoring functions against questions |
| [Foreman](https://github.com/thruwire/foreman) | Independently judges whether an implementation is complete |

## Completion and stop hooks

| Tool | What it does |
|---|---|
| [limpet](https://github.com/noplan-inc/limpet) | Stop hook that keeps an agent from finishing early |
| [jev-belay](https://github.com/valentynkit/jev-belay) | Claude Code Stop hook with an evidence check |
