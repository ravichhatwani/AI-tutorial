# Phase 1 Answer Key (don't open before attempting)

1. Stale knowledge (cutoff), private/internal data, hallucination without sources; also citations/traceability and cheap updates.
2. Fine-tuning for style, format, tone or a narrow skill that doesn't depend on changing facts. RAG for facts that change or must be cited. They can be combined.
3. 8000 - 500 - 50 - 1000 = 6,450 tokens.
4. A dense vector produced by a model trained so that texts with similar meaning have similar vectors (learned from context/contrastive training).
5. When vectors are normalized to length 1, dot product == cosine, so ranking is identical. L2 ranking also matches for normalized vectors.
6. Load -> chunk -> embed -> store -> retrieve top-k -> build prompt -> generate (answer).
7. Different models create different vector spaces; similarity between them is meaningless.
8. 9 of 15. It's a baseline so every later change (chunking, hybrid, rerank) can be measured, not guessed.
9. `q = embed(query); scores = doc_vecs @ q (normalized); idx = np.argsort(-scores)[:k]; return [chunks[i] for i in idx]`
10. (a) Was the right chunk actually retrieved? (b) Does the prompt tell the model to use only the context? (c) Context too long/noisy or contradictory; also model temperature, chunk cut off mid-sentence.
