# Phase 6 Answer Key

1. LlamaIndex: data/indexing and retrieval abstractions. LangChain: general LLM app components and chains. LangGraph: stateful, controllable agent/graph workflows with loops and persistence.
2. State: shared data passed through the graph. Node: a function that updates state. Edge: fixed transition. Conditional edge: next node chosen by a function of state.
3. Prevent infinite loops, cost blow-ups and timeouts.
4. Pipeline: predictable, cheaper, easier to test. Agentic: handles vague/multi-step questions and multiple sources but is slower, costlier and harder to debug.
5. Read-only (or least privilege), validated inputs, bounded output/time, logged/auditable, human approval for write actions.
6. Return the error message as a tool result so the model can fix it, with a max attempt count; never crash the loop.
7. Scores each retrieved doc as relevant or not. If all irrelevant: rewrite query and retry, fall back to web search, or abstain.
8. CRAG grades retrieval quality and corrects it (rewrite, web search, filtering). Self-RAG trains/prompts the model to decide when to retrieve and to critique its own output.
9. Multi-hop relation questions ("Which suppliers connect project A and B?") because the graph links entities across documents; vector RAG retrieves isolated chunks.
10. Expensive entity extraction, schema/maintenance work, slower indexing, extraction errors, complexity.
11. Caption/summarize images into text and embed that; or use multimodal embeddings (CLIP/page-image retrieval) and a vision model to read the retrieved image.
12. When one agent with a few tools solves it: extra agents add latency, cost and failure modes.
