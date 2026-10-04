# awesome-decision-models

A curated, **model-agnostic** guide to *decision models*: non-generative "System 1" models that read a state and return typed answers with probabilities instead of writing text.

Existing awesome lists are Jev-centric tool directories. This one adds what they don't: a side-by-side model comparison, benchmarks with their caveats, paper summaries, and tools grouped by what you're trying to get done.

> Last fact-checked: **04 Oct 2026**, against the cited source pages. The category is about three weeks old (Jev launched 15 Sep 2026), so expect churn. Corrections and additions welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
>
> **Dating convention:** prices, latencies, benchmark scores, star counts and "latest version" statements change quickly. They are marked "(as of 04 Oct 2026)" or carry the source's own date, so check the source before relying on a number.

## What is a decision model?

An ordinary LLM generates tokens. A decision model does a single forward pass and returns numbers. You supply a **state** (text, JSON, an email, a diff) and **typed questions**:

| Question type | You provide | You get back |
|---|---|---|
| **Choice** | a set of options (Jev: up to 255, per [2609.37647](https://arxiv.org/abs/2609.37647); Laya's docs advise staying under ~20) | probability for every option + confidence |
| **Score** | an ordered rubric of 2–10 described levels | probability of each level + probability-weighted level |
| **Noul** | a yes/no statement | probability it's true (Bernoulli-style, 0–1) |

Consequences that drive every design in this list:

- **Fast and cheap.** Jev's input price was $0.042 per million tokens with free output at launch ([Simon Willison, 21 Sep 2026](https://simonwillison.net/2026/Sep/21/jev/)); Vercel AI Gateway lists $0.04 / M input (as of 04 Oct 2026, [Vercel](https://vercel.com/ai-gateway/models/jev)). Open models such as Laya run locally; Laya's own docs report ~33 ms per question on a T4 GPU ([BENCHMARKS.md](https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md), as of 04 Oct 2026).
- **No explanation.** You get numbers, not reasons. Willison notes that Jev's own documentation says it is "not great with numbers, dates, or 'adversarial content'," and shares a one-off experiment in which Jev rated Cupertino the best and East Palo Alto the worst Bay Area city on a yes/no "Good city?" question ([same post](https://simonwillison.net/2026/Sep/21/jev/)). That is an anecdote, not a bias study.
- **Can't call tools or write arguments.** Something else proposes the options and your code executes ([Vercel](https://vercel.com/i/jev-agent-control)).
- **Calibration is the whole game.** The probabilities are only useful if they're trustworthy, and the papers below show they often need tuning.

## Contents

- **Website:** https://tech.anujsadani.in/awesome-decision-models/ (searchable tools table, same content)
- [Learn more](LEARN.md): the best introductions, tutorials and explainers, in reading order
- [Gaps](GAPS.md): what is and isn't built yet, with the evidence and its limits
- [References & credits](REFERENCES.md): sources, licenses and attribution
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

- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools): the largest Jev tool directory; one of several lists used to discover projects (see [REFERENCES.md](REFERENCES.md))
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev)
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev)
- [Open Jev collection on Hugging Face](https://huggingface.co/collections/Ferr0/open-jev-typed-decision-models)

## How to read the evidence in this repo

Almost every number here is **vendor-reported or single-author and not independently replicated**. Each entry says who measured it. Treat all comparisons as indicative. Where two sources disagree, both are shown.

Claims came from the linked source pages, which were downloaded and searched for the exact figures on 04 Oct 2026. Tool descriptions in the category files are written in my own words from each project's own GitHub description; I confirmed the links resolve but did not run the tools. Full credits and licenses: [REFERENCES.md](REFERENCES.md).

## Suggested reading order

1. [Simon Willison's overview](https://simonwillison.net/2026/Sep/21/jev/): the shape of the idea, plus sober caveats
2. [Evaluating and Benchmarking Jev (2609.37647)](https://arxiv.org/abs/2609.37647): the broadest independent evaluation
3. [Do System One Decisions Add Up? (2609.33971)](https://arxiv.org/abs/2609.33971): why decomposing a decision isn't free
4. [Laya reproduction (2609.33843)](https://arxiv.org/abs/2609.33843): calibration and escalation-gate failure
5. [JEV-as-a-Judge (2609.26550)](https://arxiv.org/abs/2609.26550): the strongest case for accept-or-escalate cascades
6. [Jev in the Wild (2609.30216)](https://arxiv.org/abs/2609.30216): what 2,170 projects actually build

## Website

The site at https://tech.anujsadani.in/awesome-decision-models/ is built from these Markdown files, which stay the single source of truth. To build it locally:

```text
pip install -r requirements-site.txt
python scripts/build_site.py     # writes _site/
python scripts/check_site.py     # structure, links and anchors
```

A GitHub Actions workflow builds, checks and deploys it on every push to `main`. Do not add a `CNAME` file: the site inherits the custom domain from the `asadani.github.io` repo.

## License

Original text in this repository is licensed under [CC BY 4.0](LICENSE). Credit Anuj Sadani and link to this repository when you reuse it. Third-party projects, quotations and data keep their own licenses; see [REFERENCES.md](REFERENCES.md).
