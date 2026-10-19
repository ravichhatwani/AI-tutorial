# Phase 3: Retrieval & Semantic Search (Days 10-17)

Outcome: you can choose and tune an embedding model, vector DB and hybrid retrieval, and prove it with numbers.

## Day 10 - Embedding models and MTEB
- **Theory:** model choice (size, language, domain), dimensions, normalization, query vs document prefixes.
  - [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
  - [Sentence-Transformers docs](https://www.sbert.net)
- **Watch:** [Embedding Models Explained: How to Choose the Right One](https://www.youtube.com/watch?v=YXjX3u4LZdQ) * | [Benchmark embedding models #1 - Introduction & MTEB leaderboard](https://www.youtube.com/watch?v=6YrkXr-2cCc) *
- **Practice:** compare 2-3 models on your golden set.
- **Done when:** a results table (model, dims, hit@3, speed).

## Day 11 - Vector DBs: Chroma
- **Theory:** collections, persistence, metadata filters.
  - [Chroma docs](https://docs.trychroma.com)
- **Watch:** [RAG Tutorial with Ollama and ChromaDB](https://www.youtube.com/watch?v=g8fMRuGR5z0) * | [RAG Made Simple: ChromaDB + Python (all local)](https://www.youtube.com/watch?v=InlB5-3-nR4) *
- **Practice:** move `rag_v0` from NumPy to Chroma with persistent storage and a `source` filter.
- **Done when:** a filtered query returns only chunks from one file.

## Day 12 - Index internals: HNSW, IVF, FAISS (HEAVY: allow 2 sessions)
- **Theory:** exact vs approximate NN, recall/latency/memory, quantization.
  - [Pinecone: HNSW explained](https://www.pinecone.io/learn/series/faiss/hnsw/)
  - [HNSW paper](https://arxiv.org/abs/1603.09320) (skim)
  - [FAISS wiki](https://github.com/facebookresearch/faiss/wiki)
- **Watch:** [HNSW for Vector Search Explained and Implemented with Faiss (Python)](https://www.youtube.com/watch?v=QvKMwLjdK-s) * | [Vector Database Search - HNSW Explained](https://www.youtube.com/watch?v=77QH0Y2PYKg) *
- **Practice:** with 100k random vectors, compare `IndexFlatL2` vs `IndexHNSWFlat` (time and recall).
- **Done when:** a chart/table of speed vs recall.

## Day 13 - Qdrant and pgvector (HEAVY: allow 2 sessions)
- **Theory:** managed vs self-hosted, SQL + vectors, payload filters.
  - [Qdrant docs](https://qdrant.tech/documentation/)
  - [pgvector](https://github.com/pgvector/pgvector)
- **Watch:** [Vector Databases Explained in 10 Minutes & Get Started with Qdrant (Python)](https://www.youtube.com/watch?v=GDJN4QJezYY) * | [Semantic Search for Beginners with Qdrant](https://www.youtube.com/watch?v=SgCd2o6hJIA) * and [RAG with PostgreSQL and pgvector: Postgres as your vector database](https://www.youtube.com/watch?v=_9WPh490T-A) * | [Set Up pgvector and Store Embeddings in PostgreSQL (Windows install)](https://www.youtube.com/watch?v=ZwASqFrUXVw) *
- **Practice:** run Qdrant in Docker; run Postgres+pgvector in Docker; index the same corpus in both.
- **Done when:** same query works against both and you wrote a 5-line pros/cons.

## Day 14 - BM25 keyword search
- **Theory:** TF-IDF, BM25, why exact terms (IDs, names, codes) need keywords.
  - [rank_bm25](https://github.com/dorianbrown/rank_bm25)
- **Watch:** [BM25 in Python: better text search than TF-IDF with rank_bm25](https://www.youtube.com/watch?v=aT-ubeEy6p4) * | [A no nonsense intro to BM25](https://www.youtube.com/watch?v=TW9vHU1GpU4) *
- **Practice:** BM25 over your chunks; find 3 queries where BM25 beats vectors (e.g., "ERR-4021").
- **Done when:** 3 documented examples.

## Day 15 - Hybrid search and rank fusion
- **Theory:** combining lexical + semantic; Reciprocal Rank Fusion `score = sum(1/(60+rank))`.
- **Watch:** [Reciprocal Rank Fusion in Python: combine BM25 and embedding search](https://www.youtube.com/watch?v=tHTQw-zHxks) * | [Hybrid RAG Explained: Dense + BM25 + RRF](https://www.youtube.com/watch?v=UgYrGLKyYmI) *
- **Practice:** implement RRF over BM25 + vector; compare to each alone.
- **Done when:** hybrid hit@3 >= max(BM25, vector) on your golden set.

## Day 16 - Reranking, MMR, metadata filters
- **Theory:** bi-encoder vs cross-encoder, retrieve 50 then rerank to 5; MMR for diversity.
  - [Sentence-Transformers cross-encoders](https://www.sbert.net)
- **Watch:** [RAG Reranking Explained: Bi-Encoder vs Cross-Encoder (with benchmarking code)](https://www.youtube.com/watch?v=tA85v3aGBIU) * | [Advanced RAG 04 - Reranking with Cross Encoders and Cohere API](https://www.youtube.com/watch?v=ZFbaA9eM0uo) *
- **Practice:** add `cross-encoder/ms-marco-MiniLM-L-6-v2` rerank; add MMR.
- **Done when:** before/after table with latency cost.

## Day 17 - Retrieval metrics + Phase 3 quiz
- **Theory:** Recall@k, Precision@k, MRR, nDCG.
- **Read (better than any video found):** [Pinecone: Offline evaluation (Recall@K, MRR, MAP, NDCG)](https://www.pinecone.io/learn/offline-evaluation) | [Weaviate: Retrieval evaluation metrics](https://weaviate.io/blog/retrieval-evaluation-metrics)
- **Quick recap (1-minute Short):** [RAG Retrieval Metrics Explained](https://www.youtube.com/watch?v=1M24UHWL41A) *
- **Worked example (run it, then rewrite it from memory):** `labs/eval/metrics.py` has `recall_at_k`, `hit_at_k`, `reciprocal_rank`, `ndcg_at_k` with a 3-query example (MRR = 0.444, same as Phase 3 quiz Q11). Run: `python labs/eval/metrics.py`
- **Practice:** `evaluate_retrieval.py` printing Recall@5, MRR for every retriever you built.
- **Done when:** a leaderboard in `labs/eval/results.md`.
- **Then:** `quizzes/phase-03-quiz.md`.
