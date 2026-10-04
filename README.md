# awesome-decision-models

A curated, **model-agnostic** guide to *decision models*: non-generative "System 1" models that read a state and return typed answers with probabilities instead of writing text.

Existing awesome lists are Jev-centric tool directories. This one adds what they don't: a side-by-side model comparison, benchmarks with their caveats, paper summaries, and tools grouped by what you're trying to get done.

> Last updated: 2026-10-04. The category is about two weeks old (Jev launched 2026-09-15), so expect churn. Corrections and additions welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## What is a decision model?

An ordinary LLM generates tokens. A decision model does a single forward pass and returns numbers. You supply a **state** (text, JSON, an email, a diff) and **typed questions**:

| Question type | You provide | You get back |
|---|---|---|
| **Choice** | a set of options (Jev: up to 255; some models practical limit ~20) | probability for every option + confidence |
| **Score** | an ordered rubric of 2–10 described levels | probability of each level + probability-weighted level |
| **Noul** | a yes/no statement | probability it's true (Bernoulli-style, 0–1) |

Consequences that drive every design in this list:

- **Fast and cheap.** Jev is priced at $0.042 per million input tokens with free output ([Simon Willison](https://simonwillison.net/2026/Sep/21/jev/)). Open models such as Laya run locally in tens of milliseconds.
- **No explanation.** You get numbers, not reasons. Simon Willison also flags weakness with numbers, dates and adversarial content, and warns against uses like hiring.
- **Can't call tools or write arguments.** Something else proposes the options and your code executes ([Vercel](https://vercel.com/i/jev-agent-control)).
- **Calibration is the whole game.** The probabilities are only useful if they're trustworthy, and the papers below show they often need tuning.

## Contents

- [Models](models.md): hosted and open-weight decision models compared
- [Benchmarks](benchmarks.md): what's been measured, by whom, with caveats
- [Papers](papers.md): arXiv papers with summaries
- Tools by category:
  - [Productivity & personal](categories/productivity.md)
  - [Business & operations](categories/business.md)
  - [Developer tools & coding agents](categories/developer-tools.md)
  - [Security, guardrails & moderation](categories/security-and-moderation.md)
  - [Agents, browsers & routing](categories/agents-and-routing.md)
  - [Search, ranking & scoring](categories/search-and-ranking.md)
  - [Domain: finance, legal, health, science](categories/domains.md)
  - [Edge, robotics & games](categories/edge-and-games.md)
  - [Infra, SDKs & calibration/eval tooling](categories/infra-and-evaluation.md)

## Related lists

- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools): the largest Jev tool directory; most tool entries here were first found there
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev)
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev)
- [Open Jev collection on Hugging Face](https://huggingface.co/collections/Ferr0/open-jev-typed-decision-models)

## How to read the evidence in this repo

Almost every number here is **vendor-reported or single-author and not independently replicated**. Each entry says who measured it. Treat all comparisons as indicative. Where two sources disagree, both are shown.

## Suggested reading order

1. [Simon Willison's overview](https://simonwillison.net/2026/Sep/21/jev/): the shape of the idea, plus sober caveats
2. [Evaluating and Benchmarking Jev (2609.37647)](https://arxiv.org/abs/2609.37647): the broadest independent evaluation
3. [Do System One Decisions Add Up? (2609.33971)](https://arxiv.org/abs/2609.33971): why decomposing a decision isn't free
4. [Laya reproduction (2609.33843)](https://arxiv.org/abs/2609.33843): calibration and escalation-gate failure
5. [JEV-as-a-Judge (2609.26550)](https://arxiv.org/abs/2609.26550): the strongest case for accept-or-escalate cascades
6. [Jev in the Wild (2609.30216)](https://arxiv.org/abs/2609.30216): what 2,170 projects actually build
