# Phase 3 Answer Key

1. Domain/language fit, dimensions & cost/latency, max input length, license/hosting (local vs API), benchmark score on similar tasks.
2. Benchmarks use generic datasets; your jargon, language or document style may differ. Always test on your golden set.
3. Chroma: quick prototypes. FAISS: in-process library for speed/research. Qdrant: dedicated server with rich filtering. pgvector: when data already lives in Postgres and you want SQL joins.
4. Flat is 100% accurate but slow at scale; approximate (ANN) is far faster with slightly lower recall and extra memory.
5. M: connections per node (recall, memory). efConstruction: build-time search width (index quality, build time). efSearch: query-time width (recall vs latency).
6. IVF clusters vectors and searches only nearby clusters (nprobe). PQ compresses vectors, trading precision for memory.
7. Exact tokens like "ERR-4021" or a product SKU/name: BM25 matches the literal term; embeddings may blur it.
8. 1/(60+1) + 1/(60+3) = 0.01639 + 0.01587 = 0.03226.
9. BM25 and cosine scores are on different scales; ranks are comparable and robust.
10. Bi-encoder embeds query and doc separately (fast, precomputable). Cross-encoder reads both together (more accurate, but a model call per pair), so use it only to rerank the top 20-100.
11. Recall@k: fraction of relevant items found in the top k. MRR: mean of 1/rank of first relevant. (1 + 1/3 + 0)/3 = 0.444.
12. Bad fusion weights/normalization; BM25 tokenization issues (no lowercase/stop words); chunks differ between indexes; too small candidate pool; golden set too small/noisy.
