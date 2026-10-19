# Phase 4: Query Intelligence (Days 18-21)

Outcome: your system fixes bad questions before searching.

## Day 18 - Query rewriting and multi-query
- **Theory:** users write vague/conversational queries; rewrite with an LLM; generate 3-5 variants and merge results.
- **Watch:** [RAG from scratch: Part 5 (Multi Query)](https://www.youtube.com/watch?v=JChPi0CRnDY) | [RAG from scratch: Part 6 (RAG Fusion)](https://www.youtube.com/watch?v=77qELPbNgxA)
- **Practice:** `rewrite_query()` and `multi_query_retrieve()` with dedupe + RRF.
- **Done when:** "what about the second one?" (with chat history) becomes a standalone query.
- Example (problem): "and for premium?" retrieves nothing. Example (fix): rewrite to "What is the refund window for premium plan?".

## Day 19 - HyDE and decomposition
- **Theory:** HyDE = embed a hypothetical answer; decompose multi-part questions.
  - [HyDE paper](https://arxiv.org/abs/2212.10496)
- **Watch:** [RAG from scratch: Part 9 (HyDE)](https://www.youtube.com/watch?v=SaDzIVkYqyY)
- **Practice:** implement HyDE and step-back prompting; compare on your golden set.
- **Done when:** a per-technique results table.

## Day 20 - Routing and text-to-SQL
- **Theory:** route to vector store / SQL / web / no-retrieval; schema-aware SQL generation; read-only DB users.
- **Watch:** [RAG from scratch: Part 10 (Routing)](https://www.youtube.com/watch?v=pfpIndq7Fi8) and [Text to SQL with GPT-4o and SQLite (Colab, Python)](https://www.youtube.com/watch?v=M9_ErR59_XY) * | [Build a local SQL AI agent (LangChain + Ollama)](https://www.youtube.com/watch?v=ay_sYadoxgk) *
- **Practice:** SQLite with a `orders` table; an LLM router picks docs-search vs SQL.
- **Done when:** "How many orders in March?" -> SQL; "What is the refund policy?" -> vector search.

## Day 21 - Integration + Phase 4 quiz
- **Practice:** wire rewrite -> route -> hybrid retrieve -> rerank into one `pipeline.py`. Re-run eval.
- **Done when:** end-to-end hit-rate improved vs Day 17 or you wrote why not.
- **Then:** `quizzes/phase-04-quiz.md`.
