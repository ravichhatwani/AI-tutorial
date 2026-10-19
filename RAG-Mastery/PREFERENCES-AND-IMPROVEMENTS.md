# My Learning Preferences + Improvement Log

This is a living file. Every time you ask Claude to improve the plan, it adds an entry here so nothing is forgotten.

## My preferences (Claude must follow these when adding resources or explaining)
1. **Practical first:** tutorials with many worked, runnable examples. I code along.
2. **Easy language:** plain words, no unexplained jargon; define each term once with a small example.
3. **Every topic has:** a short "Example (problem)" and "Example (fix)" with real values.
4. **Career goal:** AI engineer. Everything should end in code I can show (repo, eval numbers, demo).
5. **Time:** about 2 hours a day, so keep each day realistic; heavy days can use 2 sessions.
6. **Resources:** prefer official docs/courses and creators who build step by step. Replace theory-heavy resources.

## Improvement log
| Date | Request | What changed | Files |
|---|---|---|---|
| 2026-10-18 | Make plan realistic; list every video/tutorial; remember my preferences | Added `RESOURCES.md` (85 links, with watched + quality columns), flagged 7 heavy days, added weekly buffer days and a 58-day calendar, added this file and `CLAUDE.md` | RESOURCES.md, PROGRESS.md, README.md, phases/*.md |
| 2026-10-18 | Verify all 48 video links and add them upfront | Replaced all 48 YouTube search links with real video links (1-2 per topic, main + backup) in phases/*.md; rebuilt RESOURCES.md with Status column and TODO list of weak spots | phases/*.md, RESOURCES.md, README.md |
| 2026-10-18 | Fix weak spots (Days 17, 22, 24, 41) | Day 17: Pinecone + Weaviate articles and tested labs/eval/metrics.py; Day 22: Anthropic Reduce hallucinations guide + problem/fix example; Day 24: two Lost-in-the-Middle explainer videos; Day 41: Ragas docs as main source with version warning | phases/phase-03,05,08, labs/eval/metrics.py, RESOURCES.md |

## Pending ideas (Claude will do when you say so)
- Verify the best real video for each day, one day ahead ("Verify Day N resources").
- Add a worked example notebook per phase (`labs/phaseN/`).
- Add a glossary (`GLOSSARY.md`) that grows with each day's new terms.
- Add a spaced-repetition list: 5 flashcard questions per day, re-asked on Days +3 and +7.

## Example (problem)
Day 12 on HNSW: a video is 40 minutes of math and you understand nothing.

## Example (fix)
Rate it 1 in `RESOURCES.md`, tell Claude. It replaces it with a hands-on FAISS tutorial and adds a "HNSW in plain words" example to the glossary.
