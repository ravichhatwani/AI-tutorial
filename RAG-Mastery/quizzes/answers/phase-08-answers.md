# Phase 8 Answer Key

1. Context relevance (retrieved chunks relate to the question), groundedness (answer supported by context), answer relevance (answer addresses the question).
2. Faithfulness: share of answer claims supported by context. Context precision: relevant chunks ranked high among retrieved. Context recall: how much of the reference answer's info is present in the retrieved context.
3. It only checks consistency with retrieved context; if retrieval returned outdated or wrong text, the answer is faithful but wrong.
4. Easy, hard, multi-hop, unanswerable, ambiguous, and different document types; reviewed by a human; reference answers and source IDs.
5. Position bias, verbosity bias, self-preference. Randomize order, use rubrics, pin the judge model, calibrate against human labels.
6. Retrieved content may already reach the LLM and appear in the output or logs; filter in the retriever (metadata/ACL) so unauthorized chunks are never fetched.
7. Treat retrieved text as data not instructions; delimiters and instruction hierarchy; no powerful tools/sending ability without approval; output filtering; ingestion scanning.
8. Source documents, vector payloads/metadata, prompts and logs, memory store, cache, traces sent to third parties.
9. Caching (embedding/semantic/prompt), smaller model for easy steps, reduce k and compress, batch embeddings, skip unnecessary LLM steps.
10. Hash content; re-chunk and re-embed only that doc's chunks; delete removed IDs. New embedding model means re-embed everything into a new versioned index, then switch over.
11. Latency per step (p50/p95), token cost, retrieval scores, empty-result and refusal rate, user feedback, errors, eval score drift.
12. Structured/aggregate data (use SQL), tiny stable knowledge (put in prompt), style or behavior change (fine-tune), real-time computation.
