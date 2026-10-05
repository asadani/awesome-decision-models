# Developer tools & coding agents

Gates, reviewers and context tools for coding workflows. Descriptions are in original wording, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). The tools have not been run. The License column is what GitHub reports for each repo, not legal advice.

## Retrieval and context

| Tool | What it does | License |
|---|---|---|
| [jevgrep](https://github.com/dzhng/jevgrep) (`jg`) | Answers "where is X?" with relevant files and source excerpts. Walks folders, then files, then declarations, and uploads only what earlier steps didn't rule out. Its [README](https://github.com/dzhng/jevgrep) reports (as of 04 Oct 2026) 8 of 10 SWE-bench tasks solved with and without it, on ten tuned Python tasks. Coding-agent cost fell from $7.62 to $5.44 (28.6%, excluding Jev's own cost); a later run including Jev's cost measured 25.8% lower total cost; a still later 0.5.0 run cut Jev cost about 59% but combined cost was 2–3% higher. All self-reported, single runs, not a speed claim. | MIT |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | Claude Code plugin that replaces the compaction summary with decision-model choices over tool calls and results | MIT |
| [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) | Pi extension for verbatim context compaction guided by decisions | MIT |
| [fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) | Codex plugin that restores context around compaction, ported from fast-jev-compaction | MIT |
| [jev-pruner](https://github.com/tamaratran/jev-pruner) | Claude Code plugin that trims long Bash output before the model reads it | MIT |
| [yoshi](https://github.com/compozy/yoshi) | Proxy for Claude Code and Codex that prunes conversation history the model no longer needs | MIT |

## Review and pre-commit gates

| Tool | What it does | License |
|---|---|---|
| [jev-git](https://github.com/AkashPriyadarshii/jev-git) | Sub-second pre-commit and pre-push gate that screens diffs | MIT |
| [jev-commit](https://github.com/valentynkit/jev-commit) | Pre-commit hook that checks whether the commit message matches the diff and flags debug leftovers | MIT |
| [DiffJury](https://github.com/raihankhan-rk/diffjury) | Pull-request risk router and review coach | none stated |
| [jev-review](https://github.com/devagrawal09/jev-review) | Staged code-review workflow with a local dashboard | MIT |
| [Blink](https://blink.review) | CLI for checking diffs without an LLM reviewer (closed site; no repo) | n/a |
| [Hunch](https://github.com/Kelbie/hunch) | Semantic code review driven by plain-English rules and agent skills | MIT |
| [Abide](https://github.com/coldteadotai/abide) | Keeps coding agents within your project rules | MIT |
| [jev-pref](https://github.com/doeixd/jev-pref) | Turns AGENTS.md preferences into a fast AI linter | MIT |
| [Clean Code Judge](https://github.com/frostney/clean-code-review) | Judges each file in a pull request against Clean Code principles, then hands off to an LLM review | MIT |
| [Supercov](https://github.com/supercorp-ai/supercov) | Coverage, security and code-quality checks for coding agents | MIT |
| [jev.nvim](https://github.com/valentynkit/jev.nvim) | Neovim plugin: ask the buffer a question and get a quickfix list of scored functions | MIT |
| [Foreman](https://github.com/thruwire/foreman) | Agent supervisor for a software factory | MIT |

## Completion and stop hooks

| Tool | What it does | License |
|---|---|---|
| [limpet](https://github.com/noplan-inc/limpet) | Stop hook that prevents a coding agent from finishing too early, using plain-language rules | MIT |
| [jev-belay](https://github.com/valentynkit/jev-belay) | Claude Code Stop hook that blocks an unverified done by looking for evidence in the transcript | MIT |
