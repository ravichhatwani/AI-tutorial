# Phase 8: Evaluation, Security, Production (Days 41-48)

Outcome: you can prove quality, secure the system, and ship it.

## Day 41 - Golden dataset
- **Theory:** question, reference answer, source; coverage of easy/hard/unanswerable; synthetic generation + human review.
- **Read first (current code):** [Ragas docs: Generate a synthetic test set](https://docs.ragas.io/en/latest/getstarted/testset_generation.html) | pinned older version: [Ragas v0.2.9 RAG testset generation](https://docs.ragas.io/en/v0.2.9/getstarted/rag_testset_generation/). The Ragas API changed between versions, so put the exact version in `requirements.txt`.
- **Watch (older, idea only; code is outdated):** [How To Generate RAGAS Testset In 1 Minute](https://www.youtube.com/watch?v=VJMUH3LbyDM) *
- **Warning:** generated questions are not ground truth. Read each one and delete bad ones (the plan asks for 50 reviewed items).
- **Practice:** grow to 50 questions (10 unanswerable, 10 multi-hop).
- **Done when:** `golden.json` has 50 reviewed items.

## Day 42 - Ragas metrics
- **Theory:** faithfulness, answer relevancy, context precision, context recall.
  - [Ragas docs](https://docs.ragas.io)
- **Watch:** [RAG Evaluation Matrix Day 2: RAGAS Metrics (Faithfulness, Context Precision, Recall)](https://www.youtube.com/watch?v=jZqrprZWfsg) * | [RAG Evaluation (LangChain)](https://www.youtube.com/watch?v=bB56BaQIBm4) *
- **Practice:** run Ragas on your pipeline; save scores.
- **Done when:** a baseline scorecard in `labs/eval/ragas_baseline.md`.

## Day 43 - LLM-as-judge
- **Theory:** rubric prompts, pairwise comparison, judge bias, pinning judge model.
  - [RAG triad (DeepLearning.AI course)](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag)
- **Watch:** [DeepEval tutorial: RAG metrics with LLM-as-judge (Part 2)](https://www.youtube.com/watch?v=VOGgCMhu1zg) * | [Amazon Bedrock RAG Evaluation (LLM as a Judge)](https://www.youtube.com/watch?v=HI5b0g_mELA) *
- **Practice:** write a 1-5 groundedness rubric; check 10 judgments against your own.
- **Done when:** judge agrees with you on >= 8/10.

## Day 44 - Access control and PII
- **Theory:** filter by user/group at retrieval time (never after generation); PII redaction on ingestion and logs.
- **Watch:** [Permissions & Access Control for RAG - a Deep Dive Tutorial](https://www.youtube.com/watch?v=By_q6YCQlv4) * | [Access control & permissions in RAG for AI products](https://www.youtube.com/watch?v=dTPMpliHzpE) *
- **Practice:** tag chunks with `allowed_groups`; user "intern" must not retrieve "HR-salaries".
- **Done when:** a test proves the intern gets "no access" and zero leaked chunks.

## Day 45 - Prompt injection defenses
- **Theory:** instructions hidden in documents ("ignore previous instructions"); treat retrieved text as data.
  - [OWASP Top 10 for LLM Apps](https://genai.owasp.org/llm-top-10/)
- **Watch:** [Indirect Prompt Injection Explained For Beginners](https://www.youtube.com/watch?v=Iih7Ln8wvPY) *
- **Practice:** plant a malicious doc; add delimiters, instruction hierarchy, output checks.
- **Done when:** the attack fails and the test is saved.

## Day 46 - Caching, latency, cost
- **Theory:** embedding cache, semantic cache, prompt caching, model tiering, batching.
- **Watch:** [Optimizing RAG with Semantic Caching & LLM Memory (Redis)](https://www.youtube.com/watch?v=QA3h4H5jqJw) * | [Semantic Caching Explained: reduce AI API costs with Redis](https://www.youtube.com/watch?v=NrqvtsnjIHU) *
- **Practice:** log latency/tokens per step; add a cache; report p50/p95.
- **Done when:** a before/after latency and cost-per-query table.

## Day 47 - API (FastAPI), Docker, monitoring (HEAVY: allow 2 sessions)
- **Theory:** endpoints, health checks, tracing, feedback thumbs.
  - [FastAPI docs](https://fastapi.tiangolo.com)
- **Watch:** [RAG Tutorial 2026: Containerizing LLM Apps with LangChain & Docker](https://www.youtube.com/watch?v=k4o8Zc8cSNU) * | [RAG API using FastAPI in 10 Minutes](https://www.youtube.com/watch?v=h2NvBeAFGa0) *
- **Practice:** `POST /ask`, `POST /feedback`; Dockerfile; run locally.
- **Done when:** `curl` returns answer + sources from the container.

## Day 48 - Re-indexing + Phase 8 quiz
- **Theory:** content hashes, incremental updates, deletes, versioned indexes, embedding model migration.
- **Practice:** change one doc; only its chunks re-embed; deleted doc disappears from search.
- **Done when:** a log shows "1 doc changed, 6 chunks re-embedded, 0 others touched".
- **Then:** `quizzes/phase-08-quiz.md`.
