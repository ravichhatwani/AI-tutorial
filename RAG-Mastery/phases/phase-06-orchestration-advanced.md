# Phase 6: Orchestration & Advanced Patterns (Days 26-35)

Outcome: you can build agentic, graph-based and multimodal RAG with real frameworks.

## Day 26 - LlamaIndex pipeline
- **Theory:** Documents, Nodes, Index, Retriever, Query Engine, Settings.
  - [LlamaIndex docs](https://docs.llamaindex.ai)
- **Watch:** [LlamaIndex tutorial in less than 15 mins](https://www.youtube.com/watch?v=IWyUUrvmb2A) * | [Wikipedia RAG System in Python - Beginner Tutorial with LlamaIndex](https://www.youtube.com/watch?v=M9GtHb32F8w) *
- **Practice:** rebuild your pipeline in LlamaIndex; add sentence-window retrieval.
- **Done when:** same golden-set score as your hand-built version (or explain the gap).

## Day 27 - LangChain LCEL pipeline
- **Theory:** Runnables, retrievers, prompt templates, output parsers.
  - [LangChain docs](https://docs.langchain.com/oss/python/langchain/overview)
- **Watch:** [LangChain Expression Language (LCEL) Explained](https://www.youtube.com/watch?v=E9oFkaBSTuM) * | [Retrieval Augmented Generation (RAG) with LangChain: A Complete Tutorial](https://www.youtube.com/watch?v=YLPNA1j7kmQ) *
- **Practice:** same pipeline in LCEL; trace it in LangSmith (free tier).
- **Done when:** you can read a trace and name the slowest step.

## Day 28 - LangGraph basics
- **Theory:** state, nodes, edges, conditional edges, checkpoints.
  - [LangGraph agentic RAG tutorial](https://docs.langchain.com/oss/python/langgraph/agentic-rag)
- **Watch:** [LangGraph Complete Course for Beginners](https://www.youtube.com/watch?v=jGg_1h0qzaM) * | [LangGraph Tutorial for Beginners: Build Your First AI Agent](https://www.youtube.com/watch?v=UklCxmEvz2w) *
- **Practice:** a 3-node graph: retrieve -> grade -> generate.
- **Done when:** graph prints its path for 3 queries.

## Day 29 - Agentic RAG (HEAVY: allow 2 sessions)
- **Theory:** the model decides whether/what/when to retrieve; loops with a retry limit.
- **Practice:** follow the LangGraph agentic RAG tutorial above with your own corpus; add a rewrite-and-retry edge (max 2 retries).
- **Watch:** [Build an Agentic RAG System with LangGraph](https://www.youtube.com/watch?v=moaWbFTVOEo) * | [Stop Using Basic RAG - Build Agentic RAG with LangGraph (full tutorial)](https://www.youtube.com/watch?v=io5HFm93k40) *
- **Done when:** a vague query triggers a rewrite and succeeds on retry.

## Day 30 - Tool use / function calling
- **Theory:** tool schemas, tool-call loop, safe tools (read-only).
  - [Anthropic tool use docs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
- **Watch:** [How to Connect an LLM to Python Functions (Tool Calling Tutorial)](https://www.youtube.com/watch?v=liV0bfZ5Wu0) *
- **Practice:** tools: `search_docs`, `query_orders_sql`, `calculator`.
- **Done when:** one question uses 2 tools in sequence.

## Day 31 - Self-RAG and Corrective RAG
- **Theory:** grade retrieved docs; if poor, rewrite/search web; self-check the answer.
  - [Self-RAG](https://arxiv.org/abs/2310.11511), [CRAG](https://arxiv.org/abs/2401.15884)
- **Watch:** [Self-reflective RAG with LangGraph: Self-RAG and CRAG](https://www.youtube.com/watch?v=pbAd8O1Lvm4) * | [Corrective RAG (CRAG) Tutorial with LangGraph and LangChain](https://www.youtube.com/watch?v=cAdu8mO01Bo) *
- **Practice:** add a document grader and an answer-groundedness checker node.
- **Done when:** a bad retrieval is caught and repaired in a logged example.

## Day 32 - GraphRAG concepts
- **Theory:** entities + relations, community summaries, multi-hop questions.
  - [GraphRAG paper](https://arxiv.org/abs/2404.16130)
- **Watch:** [GraphRAG: LLM-Derived Knowledge Graphs for RAG](https://www.youtube.com/watch?v=r09tJfON6kE) * | [Graph RAG: Improving RAG with Knowledge Graphs](https://www.youtube.com/watch?v=vX3A96_F3FU) *
- **Done when:** you can explain when GraphRAG beats vector RAG (e.g., "Which suppliers connect project A and project B?").

## Day 33 - GraphRAG hands-on (HEAVY: allow 2 sessions)
- **Practice:** extract entities/relations from 10 docs with an LLM into `networkx` or Neo4j; answer a 2-hop question.
  - [Neo4j GraphRAG](https://neo4j.com/docs/neo4j-graphrag-python/current/)
- **Watch:** [Neo4j GraphRAG in Python: multi-hop retrieval for hard questions](https://www.youtube.com/watch?v=zV5ORht7Vkk) * | [RAG #14: GraphRAG Explained Clearly (Neo4j + LangChain)](https://www.youtube.com/watch?v=2XKSWe8DEFw) *
- **Done when:** a 2-hop question is answered correctly where vector RAG fails.

## Day 34 - Multimodal RAG (HEAVY: allow 2 sessions)
- **Theory:** image embeddings (CLIP), captioning, page-image retrieval.
- **Watch:** [Multimodal RAG: Chat with PDFs (Images & Tables)](https://www.youtube.com/watch?v=uLrReyH5cu0) * | [Multimodal RAG: Chat with Complex PDFs (Text, Tables & Images)](https://www.youtube.com/watch?v=X0oIeSJHFD8) *
- **Practice:** index chart images with captions; answer a question about a chart.
- **Done when:** "What was Q3 revenue?" is answered from a chart image.

## Day 35 - Multi-agent + Phase 6 quiz
- **Theory:** supervisor + specialist agents; cost of over-engineering.
- **Watch:** [Build a Supervisor Multi-agent Architecture with LangGraph](https://www.youtube.com/watch?v=KAwiykWkQ5Q) * | [LangGraph Multi-Agent Supervisor - build high level agents fast](https://www.youtube.com/watch?v=WWcDnUCT52Q) *
- **Practice:** supervisor routes to `docs_agent` and `sql_agent`.
- **Done when:** you wrote 5 lines: when a single agent is enough.
- **Then:** `quizzes/phase-06-quiz.md`.
