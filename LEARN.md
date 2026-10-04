# Learn more

The best starting points, in a suggested reading order. I opened and read each one on 04 Oct 2026. The one-line notes say what you get from it. Dates are each page's own publication date.

## 1. What is a decision model? (start here)

1. **[What Is Jev Model? A Practical Guide to Typed AI Decisions](https://huggingface.co/blog/paidaxccc/what-is-jev-model-a-practical-guide-to-typed-ai-de)** · community article by paidaxccc on Hugging Face · 25 Sep 2026
   The gentlest introduction. Covers state plus typed questions, the three question types (Choice, Score, Noul), where a decision model sits next to an LLM, a routing example, how to read probability and confidence, a limits-and-evaluation checklist, and an FAQ. It is a community article, not an official source, so check pricing and limits against the vendor.
2. **[Jev introduces a new shape of LLM: System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/)** · Simon Willison · 21 Sep 2026
   A short, skeptical overview. Includes the pricing, the API shape and Jev's own documented weaknesses.
3. **[What Is Jev? A Guide to TypeSafe AI's System One Model](https://www.langchain.com/blog/building-a-harness-with-jev)** · LangChain (Runkle, Lovell) · 17 Sep 2026
   Short, practical: the agent loop, model routing, and an "auto mode" gate for agent actions.

## 2. How decision models fit into agents

4. **[Typed Decision Models: Jev and Laya in Agentic AI](https://mchromiak.github.io/articles/2026/Sep/17/Typed-Decision-Models-Jev-and-Laya-in-Agentic-AI/)** · Michał Chromiak · 17 Sep 2026
   The most careful explainer I found. It separates the decision pattern from any one model, explains what the probabilities do and don't mean, compares Jev and Laya claims critically, and lists production failure modes and how to evaluate on your own workflow.
5. **[Where does Jev fit in an AI agent loop?](https://vercel.com/i/jev-agent-control)** · Vercel
   Short and official. The key point: your application invokes tools and enforces permissions; the decision model supplies judgments.
6. **[What Is Jev? Inside TypeSafe's Decision-Only AI Model and Its Developer Use Cases](https://www.firecrawl.dev/blog/what-is-jev)** · Firecrawl (Hiba Fathima) · 23 Sep 2026 (updated)
   Broad tour with six developer use cases and a useful section on why "can't hallucinate" is a narrower claim than it sounds. It also reports TypeSafe's own speed claims, which I did not verify.

## 3. Hands-on tutorials

7. **[How to classify, route, and score with Jev and AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** · Vercel Knowledge Base · 19 Sep 2026
   Step by step: one boolean question, several questions against structured state, branching on probabilities, and unit-testing the branching with a mock model.
8. **[Decision-Making with Jev Types (DSPy)](https://dspy.ai/current/tutorials/jev_decisions/)** · DSPy docs
   Defining decision types, tuning decision boundaries and automatic calibration with `ReAnchor`.
9. **[Decision models in llama.cpp](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp)** · Xuan-Son Nguyen, ggml-org · 2 Oct 2026
   Run an open decision model locally with `llama serve`, including tips on describing options, per-model confidence cutoffs, and batching.

## 4. Open models and local use

10. **[What Is Laya? Laya vs Jev, with Live Demo](https://dev.to/vishalmysore/what-is-laya-laya-vs-jev-with-live-demo-4j6e)** · Vishal Mysore · 26 Sep 2026
    A friendly comparison with a browser demo and an honest "where Laya needs help" section.
11. **[Introducing Strands Decider](https://strandsagents.com/blog/introducing-strands-decider/)** · AWS Strands Agents · 1 Oct 2026
    Explains the architecture (a pointer head replacing the LM head, with a LoRA-tuned torso) and the repo shows a retraining recipe that fits on one consumer GPU.

## 5. Evidence and caveats

12. **[Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647)** · Deußer, Sparrenberg, Sifa · 29 Sep 2026
    The broadest independent evaluation (37 datasets, zero-shot).
13. **[JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)** · 22 Sep 2026
    The strongest published case for confidence-gated cascades.
14. **[Laya as a Typed Probabilistic Assessor](https://arxiv.org/abs/2609.33843)** · 27 Sep 2026
    A preregistered study showing why you must calibrate on your own data.

More papers: [papers.md](papers.md). Benchmarks and their caveats: [benchmarks.md](benchmarks.md).

## Suggested paths

- **"What is this, in 15 minutes":** 1, 2, then 5.
- **"I'm building an agent":** 3, 4, 5, then 7.
- **"I want to run one locally":** 9, 10, 11.
- **"Is it actually reliable?":** 12, 13, 14, then [benchmarks.md](benchmarks.md).
