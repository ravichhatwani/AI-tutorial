# Phase 7: Memory (Days 36-40)

Outcome: your assistant remembers within a chat and across chats, safely.

## Day 36 - Short-term memory
- **Theory:** chat history in the prompt, windowing, token budgets, checkpointers.
  - [LangGraph persistence / memory](https://docs.langchain.com/oss/python/langgraph/overview) (search "persistence")
- **Watch:** [Short-Term Memory with LangGraph](https://www.youtube.com/watch?v=k3FUWWEwgfc) * | [LangGraph Tutorial: Conversation State with Checkpoints & Memory](https://www.youtube.com/watch?v=crS0PNjElWo) *
- **Practice:** keep the last N turns; use thread IDs.
- **Done when:** "and its price?" works after "Tell me about Plan X".

## Day 37 - Summarization memory
- **Theory:** rolling summary vs window; information loss.
- **Watch:** [Conversation Summary Memory (4.4)](https://www.youtube.com/watch?v=asZQ8Ktqmt8) *
- **Practice:** when history > 2000 tokens, summarize the oldest part.
- **Done when:** a 40-turn chat stays under budget and still recalls turn 3.

## Day 38 - Long-term memory store
- **Theory:** facts/preferences stored as embeddings + metadata (`user_id`); semantic vs episodic memory; write on important events only.
- **Watch:** [Long-Term Memory with LangGraph](https://www.youtube.com/watch?v=fsENEq4F55Q) * | [LangGraph + Mem0 Integration: long-term memory for agents](https://www.youtube.com/watch?v=e-wBojpJrrQ) *
- **Practice:** extract "user prefers Python" after a chat; store; recall in a new session.
- **Done when:** a new thread recalls the preference with the right `user_id` only.

## Day 39 - Mem0 / memory frameworks
- **Theory:** managed memory layers, add/search/update/delete.
  - [Mem0 docs](https://docs.mem0.ai)
- **Watch:** [Mem0: a framework for long-term, personalized memory](https://www.youtube.com/watch?v=bqKfT4waYEk) * | [Build AI Agents with REAL MEMORY (OpenAI + Mem0)](https://www.youtube.com/watch?v=dFfLyCbPzRM) *
- **Practice:** replace your hand-made store with Mem0; compare effort and quality.
- **Done when:** 5-line comparison written.

## Day 40 - Memory policies + Phase 7 quiz
- **Theory:** what NOT to remember (secrets, PII), forgetting, user deletion, conflicts ("moved from Pune to Delhi").
- **Practice:** add `forget(user_id)` and contradiction handling (newer fact wins, old marked inactive).
- **Done when:** deleting a user removes all their memories (verify by search).
- **Then:** `quizzes/phase-07-quiz.md`.

Example (problem): user said "I'm vegetarian" last month; today the bot suggests chicken. Example (fix): long-term memory retrieved by `user_id` is injected into the system prompt.
