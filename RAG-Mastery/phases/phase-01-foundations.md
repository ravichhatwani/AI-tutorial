# Phase 1: Foundations (Days 1-4)

Outcome: you can explain RAG and build a working one in ~50 lines with no framework.

## Day 1 - Why RAG, LLM basics, tokens
- **Theory (30m):** LLM hallucination, knowledge cutoff, private data, context window, tokens, RAG vs fine-tuning vs prompting.
  - Paper: [Retrieval-Augmented Generation (Lewis et al.)](https://arxiv.org/abs/2005.11401) - read abstract + intro only.
  - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- **Watch (30m):** [Karpathy: [1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) and [3Blue1Brown: Large Language Models, Explained Briefly (7 min)](https://www.youtube.com/watch?v=WMcwoIyK4DA)
- **Practice (60m):** Set up Python venv + Git repo `rag-journey`. Call an LLM API with a question about a private fact; observe the wrong answer. Count tokens of a paragraph (`tiktoken`).
- **Done when:** you have a script showing the LLM failing on a fact you invented (e.g., "Our refund window is 17 days"), and a token count printed.
- Example (problem): LLM says refunds take 30 days. Example (fix): paste the policy paragraph into the prompt; it now says 17 days. That is RAG in miniature.

## Day 2 - Embeddings and similarity
- **Theory:** embeddings, vector space, cosine similarity vs dot product vs L2, dimensions.
  - [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/)
  - [Sentence-Transformers docs](https://www.sbert.net)
- **Watch:** [StatQuest: Word Embedding and Word2Vec, Clearly Explained](https://www.youtube.com/watch?v=viZrOnJclY0) and [Sentence Transformers (SBERT) with PyTorch: Similarity and Semantic Search](https://www.youtube.com/watch?v=nZ5j289WN8g) * | [Sentence Transformers: embedding, similarity, semantic search (code)](https://www.youtube.com/watch?v=OlhNZg4gOvA) *
- **Practice:** embed 20 sentences with `all-MiniLM-L6-v2`; write `cosine(a,b)` by hand with NumPy; rank sentences for the query "how do I get my money back".
- **Done when:** "refund policy" sentence ranks first without sharing keywords with the query.

## Day 3 - Basic RAG loop from scratch (HEAVY: allow 2 sessions)
- **Theory:** load -> chunk -> embed -> store -> retrieve (top-k) -> prompt -> generate.
  - [DeepLearning.AI: Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag) (watch lesson 1 for the baseline pipeline)
- **Watch:** [freeCodeCamp: Learn RAG From Scratch (Lance Martin, 2.5h)](https://www.youtube.com/watch?v=sVcwVQRHIc8) (2.5h; watch the first 45 min today, rest on later days).
- **Practice:** build `rag_v0.py`: split a text file into chunks, embed, keep vectors in a NumPy array, retrieve top-3, build a prompt, call the LLM.
- **Done when:** `python rag_v0.py "question"` prints an answer grounded in your file.

## Day 4 - Tiny eval set + Phase 1 quiz
- **Theory:** why measure from day 1; recall@k idea.
- **Watch:** finish the next 45 min of the freeCodeCamp video from Day 3.
- **Practice:** write 15 questions with the expected source chunk for your docs in `labs/eval/golden.json`. Compute "did top-3 contain the right chunk?" for `rag_v0`.
- **Done when:** you have a baseline hit-rate number (e.g., 9/15 = 60%) saved in the repo.
- **Then:** take `quizzes/phase-01-quiz.md`.
