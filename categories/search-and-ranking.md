# Search, ranking & scoring

Using Score and Noul questions to rank or grade items. Descriptions are from the [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) listing unless noted; not run by me.

| Tool | What it does |
|---|---|
| [jev-reranker](https://github.com/hotchpotch/jev-reranker) | Assesses retrieved documents for relevance |
| [Jev Search](https://github.com/superagents-lab/jev-search) | Ranks Search1API results by relevance |
| [jevsearch](https://github.com/kylemclaren/jevsearch) | shadcn/ui search that reorders hits with Jev |
| [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) | LlamaIndex adapter for retrieval |
| [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) | Checks whether citations support the claims in academic papers |
| [jev-bfs](https://github.com/komikat/jev-bfs) | Finds Wikipedia link paths via ranked links |
| [jev-scout](https://github.com/AkashPriyadarshii/jev-scout) | Open-source repo scout |
| [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) | SEO and GEO search radar CLI suite |
| [SemanticSpace](https://semanticspace.dev/) | Places phrases in 2D via relationship scores |
| [jevql](https://github.com/kylemclaren/jevql) | psql-shaped CLI with SQL integration |
| [sqlite-jev](https://github.com/mgaitan/sqlite-jev) | SQLite loadable extension |

## Evidence on reranking

- [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619): measured run over 33,047 catalog entries. Read before assuming a decision model beats your current ranker.
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench): measures how defensible ORDER BY rankings are, including wording invariance and ties.
- [RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) reports hippo R@1 improving from 0.192 to 0.308 with a reranking reward in its v3.0 release, about +60% relative (self-reported, as of 04 Oct 2026).
