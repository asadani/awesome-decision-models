# Search, ranking & scoring

Using Score and Noul questions to rank or grade items. Descriptions are in original wording, based on each project's own GitHub description (as of 04 Oct 2026). Projects were discovered through several lists and searches (see [REFERENCES.md](../REFERENCES.md)). The tools have not been run. The License column is what GitHub reports for each repo, not legal advice.

| Tool | What it does | License |
|---|---|---|
| [jev-reranker](https://github.com/hotchpotch/jev-reranker) | Relevance filtering and reranking for RAG in Python | MIT |
| [Jev Search](https://github.com/superagents-lab/jev-search) | Web search with source selection, query understanding and relevance ranking | MIT |
| [jevsearch](https://github.com/kylemclaren/jevsearch) | Site-search component that ranks results by answering the question | MIT |
| [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) | LlamaIndex reranker and router returning typed scores and choices | MIT |
| [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) | Checks whether each cited paper supports the sentence that cites it | MIT |
| [jev-bfs](https://github.com/komikat/jev-bfs) | Wikipedia link races using direct ranking, with a live terminal display | MIT |
| [jev-scout](https://github.com/AkashPriyadarshii/jev-scout) | Scouts open-source repos and crates using System One scoring | MIT |
| [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) | Free Rust SEO and GEO toolkit with site audits, crawls and citation checks | MIT |
| [SemanticSpace](https://semanticspace.dev/) | Web tool placing phrases on a 2D map by relationship scores (closed; no repo) | n/a |
| [jevql](https://github.com/kylemclaren/jevql) | Semantic SQL for Postgres | MIT |
| [sqlite-jev](https://github.com/mgaitan/sqlite-jev) | Batched natural-language judgments inside SQLite | none stated |

## Evidence on reranking

- [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619): measured run over 33,047 catalog entries. Read before assuming a decision model beats your current ranker.
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench): measures how defensible ORDER BY rankings are, including wording invariance and ties.
- [RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) reports hippo R@1 improving from 0.192 to 0.308 with a reranking reward in its v3.0 release, about +60% relative (self-reported, as of 04 Oct 2026).
