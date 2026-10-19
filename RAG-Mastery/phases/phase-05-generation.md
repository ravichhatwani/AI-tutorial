# Phase 5: Generation (Days 22-25)

Outcome: answers are grounded, cited, and honest when the data is missing.

## Day 22 - Prompt design for RAG
- **Theory:** system prompt, context delimiters, instructions to use only context, few-shot.
  - [Anthropic prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- **Read first (best match):** [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) - 3 easy techniques: allow "I don't know", quote the source first, cite every claim and retract unsupported ones.
- **Watch (optional, low confidence):** [Advanced Prompt Engineering for RAG Pipelines](https://www.youtube.com/watch?v=81gjLH3RWGM) * | [How I built a RAG system that answers only from your files](https://www.youtube.com/watch?v=i8XakkTRaJc) *
- **Example (problem):** question "Who approved the 2024 refund change?" and the chunk never says. Plain prompt -> the model invents "the CFO".
- **Example (fix):** add "If the context does not contain the answer, reply exactly: I don't have that information." -> it refuses correctly.
- **Practice:** write 3 prompt templates; compare faithfulness by hand on 10 questions.
- **Done when:** the best template is saved as `prompts/answer_v1.txt`.

## Day 23 - Citations and "I don't know"
- **Theory:** source IDs in context, inline citations, abstention when retrieval is weak (score threshold).
- **Watch:** [Master Explainable RAG: citations, sources & page-level answers](https://www.youtube.com/watch?v=PtsbjTuwcu4) * | [Advanced RAG Tutorial - Include Sources With LangChain LCEL](https://www.youtube.com/watch?v=69gUQ4XHg0o) *
- **Practice:** answers end with `[doc3, p12]`; unanswerable questions return "I don't have that information."
- **Done when:** 5 out-of-scope questions are correctly refused.

## Day 24 - Context ordering, compression, long context vs RAG
- **Theory:** "lost in the middle"; contextual compression; cost/latency of long context.
  - [Lost in the Middle](https://arxiv.org/abs/2307.03172)
- **Watch:** [Lost in the Middle: How Language Models use Long Context - Explained!](https://www.youtube.com/watch?v=Kf3LeaUGwlg) * | [What is Lost in the Middle?](https://www.youtube.com/watch?v=qDfTO9i4iSg) * | [Long-Context LLMs vs RAG: Who Will Win?](https://www.youtube.com/watch?v=-xcS9ByiJEo) *
- **Practice:** put the best chunk first/middle/last; measure answer accuracy; add a compressor that trims irrelevant sentences.
- **Done when:** a table of position vs accuracy.

## Day 25 - Structured output, streaming + Phase 5 quiz
- **Theory:** JSON schema outputs (Pydantic), streaming tokens to UI.
- **Watch:** [Get LLM output as Python object with LangChain and Pydantic](https://www.youtube.com/watch?v=R0RwdOc338w) * | [LlamaIndex: How to Get Structured Data from LLMs](https://www.youtube.com/watch?v=2Qr0yUGGpCE) *
- **Practice:** return `{answer, sources[], confidence}`; stream the answer in the terminal.
- **Done when:** output validates against a Pydantic model for all 15 golden questions.
- **Then:** `quizzes/phase-05-quiz.md`.
