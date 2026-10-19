# Phase 1 Quiz (Foundations) - 10 questions
Write answers in `quizzes/my-answers/phase-01.md`. No notes first, then check docs. Tag in [brackets] = topic for gap analysis.

1. [why-rag] Name 3 problems RAG solves that prompting alone doesn't.
2. [why-rag] When would you pick fine-tuning over RAG?
3. [tokens] A model has a 8k-token context. Your prompt template uses 500 tokens, the question 50, and you want 1,000 tokens left for the answer. How many tokens of retrieved context fit?
4. [embeddings] What does an embedding represent, and why do similar meanings land close together?
5. [similarity] Cosine similarity vs dot product vs L2: when do cosine and dot product give the same ranking?
6. [pipeline] List the 6 steps of the basic RAG loop in order.
7. [pipeline] Why must you embed the query with the same model as the documents?
8. [eval] Your top-3 hit-rate is 60% on 15 questions. How many questions did you get right? Why is this number useful on Day 4?
9. [practical] Write pseudocode for `retrieve(query, k)` using NumPy.
10. [practical] The bot answers confidently but wrongly even with context supplied. Name 3 things to check.
