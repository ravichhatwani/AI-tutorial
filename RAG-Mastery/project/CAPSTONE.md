# Capstone: "DocMind" - Production-style RAG Assistant (Days 49-50)

Portfolio goal: a GitHub repo and 3-minute demo video recruiters can run.

## Requirements
1. **Ingestion:** PDFs + HTML + one table-heavy file; metadata; contextual chunks; incremental re-index.
2. **Retrieval:** hybrid (BM25 + vector) + reranker + metadata/access filters.
3. **Query intelligence:** rewrite + router (docs vs SQL).
4. **Generation:** citations, abstention, structured JSON output, streaming.
5. **Orchestration:** LangGraph agentic loop with grader + max 2 retries.
6. **Memory:** short-term thread + long-term per-user store with `forget()`.
7. **Security:** per-group access control test; prompt-injection test.
8. **Evaluation:** 50-question golden set; Ragas scorecard; retrieval Recall@5 and MRR.
9. **Ops:** FastAPI + Docker; latency/cost log; feedback endpoint.

## Day 49 - Build and deploy
Assemble earlier labs into one repo. Run `docker compose up`. Fix integration bugs.

## Day 50 - Report, README, demo
- README: architecture diagram, quick start, results table.
- `REPORT.md`: baseline vs final scores (e.g., Recall@5 62% -> 88%), cost per query, 3 failures and what you learned.
- Record a 3-minute demo.

## Interview talking points
- Why hybrid beat vector-only on your data (use your numbers).
- How you prevented data leakage.
- What you would do at 10M documents.

Example (problem): "I built a RAG chatbot" - every candidate says this.
Example (fix): "Recall@5 went from 62% to 88% by adding BM25 fusion and reranking; p95 latency 2.1s; blocked an injected PDF." - evidence stands out.
