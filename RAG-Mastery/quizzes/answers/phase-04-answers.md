# Phase 4 Answer Key

1. "What is the refund window for the Premium plan?"
2. Different phrasings hit different relevant chunks, covering vocabulary gaps. Merge by dedupe + Reciprocal Rank Fusion.
3. LLM writes a hypothetical answer; embed that to search, since answers resemble documents more than questions do. Hurts when the LLM lacks domain knowledge and invents misleading content.
4. (a) 2023 refund rules (b) 2024 refund rules (c) who approved the change. Retrieve each, then combine.
5. Vector docs (policy/how-to questions), SQL (counts/aggregates/dates), web or API (fresh info), none (chit-chat/math). Signal from an LLM classifier or semantic similarity to route examples.
6. Read-only DB user; allow-list tables/columns and give schema only; validate/limit queries (LIMIT, timeouts, block DDL/DML); log queries.
7. Measure each step on the golden set: keep only steps that improve metrics enough to justify added latency/cost; skip rewrite for already-clear single-turn queries.
8. 15 follow-up questions with history; compare hit@5 with and without rewrite; check some rewrites by eye.
