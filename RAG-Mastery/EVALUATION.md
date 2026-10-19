# Weak-Topic Log

After each quiz, Claude fills this in with you.

| Date | Phase | Topic | Why weak | Revision task | Re-tested? |
|---|---|---|---|---|---|

## Example (problem)
Phase 3 quiz: you missed 3 of 4 questions on hybrid search and rank fusion.

## Example (fix)
Revision task: implement Reciprocal Rank Fusion (`score = sum(1/(60+rank))`) over BM25 + vector results for 10 queries, then re-take only the hybrid-search questions.
