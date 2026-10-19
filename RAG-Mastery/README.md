# RAG Mastery: 50-Day Career Plan (2 hours/day)

Goal: go from zero to building and shipping a production-style RAG app that you can show in interviews.

## How to use this folder
1. Open `PROGRESS.md` every day. Tick the day when finished.
2. Open the phase file for today (`phases/phase-0X-*.md`) and follow the day's block.
3. Each day = **30 min theory + 30 min video + 60 min hands-on**.
4. At the end of each phase, take the quiz in `quizzes/`. Write your answers in a new file `quizzes/my-answers/phase-0X.md`.
5. Tell Claude: "Evaluate my phase X quiz". Claude grades it against `quizzes/answers/`, finds weak topics, and gives revision tasks. Do **not** open `quizzes/answers/` before you attempt the quiz.
6. Log weak topics in `EVALUATION.md`.

## Files at a glance
- `PROGRESS.md` daily tracker + calendar
- `RESOURCES.md` every video, doc, paper and course in one table (rate each one)
- `PREFERENCES-AND-IMPROVEMENTS.md` your learning preferences + log of every plan improvement
- `phases/` daily lessons, `quizzes/` tests, `EVALUATION.md` weak topics, `project/CAPSTONE.md`

## Tech stack (free or near-free)
- Python 3.11+, VS Code, Git, a virtual environment
- Vector stores: Chroma, FAISS, Qdrant, pgvector
- Embeddings: `sentence-transformers` (local, free)
- LLM: an API key (Claude or OpenAI) or local Ollama (free)
- Frameworks: plain Python first, then LlamaIndex / LangChain / LangGraph
- Eval: Ragas

## Rules that make this career-useful
- Every day ends with committed code in `project/` or `labs/`. No code, no tick.
- Keep one Git repo. Commit messages = what you learned.
- The capstone (Days 49-50) becomes your portfolio piece. See `project/CAPSTONE.md`.

## Video note
Video links are real YouTube links found by a web search (not guesses). Items marked with * in the phase files were top search hits whose title fits but which I have not watched; see RESOURCES.md for what 'verified' means. Rate each video and tell Claude the weak ones.

## Example (problem)
You read about chunking for 2 hours and feel like you learned it, but cannot code it a week later.

## Example (fix)
Day 5 rule: read for 30 min, then code `chunk_text(text, size=500, overlap=50)` on a real PDF and print chunk 3. If you can't run it, the day is not done.
