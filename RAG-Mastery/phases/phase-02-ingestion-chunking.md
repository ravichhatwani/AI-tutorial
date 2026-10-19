# Phase 2: Ingestion & Chunking (Days 5-9)

Outcome: you can turn messy real documents into clean, well-tagged chunks.

## Day 5 - Loading PDFs / HTML / text
- **Theory:** parsers, encoding issues, layout loss, boilerplate removal.
  - [Unstructured docs](https://docs.unstructured.io)
  - [LlamaIndex data loaders](https://docs.llamaindex.ai)
- **Watch:** [Reading complex PDFs for RAG with LangChain + Unstructured](https://www.youtube.com/watch?v=z95_D8nxtN4) * | [Docling PDF Parsing for RAG: clean tables and layout](https://www.youtube.com/watch?v=rSdh5y3Fn5Y) *
- **Practice:** load 3 PDFs + 1 HTML page with `pypdf` and `unstructured`; compare output quality.
- **Done when:** a script saves clean text for each file and you listed 3 parsing defects you saw.

## Day 6 - Chunking strategies
- **Theory:** fixed-size, recursive, sentence, semantic chunking; size/overlap trade-offs.
  - [LangChain text splitters](https://docs.langchain.com/oss/python/langchain/overview) (search "text splitters")
- **Watch:** [Greg Kamradt: The 5 Levels Of Text Splitting For Retrieval](https://www.youtube.com/watch?v=8OJC21T2SL4)
- **Practice:** implement fixed and recursive chunkers; test sizes 200/500/1000 on your golden set.
- **Done when:** a table of chunk size vs hit-rate from your Day 4 eval.

## Day 7 - Tables, OCR, messy docs
- **Theory:** table extraction, scanned PDFs, OCR, image captions.
- **Watch:** [RAG pipeline for complex PDFs (tables + images) with Docling & LangChain, fully local](https://www.youtube.com/watch?v=44MsptcNzp4) * | [UnstructuredIO tutorial: document OCR & extraction](https://www.youtube.com/watch?v=xPRzfYwYUmc) *
- **Practice:** OCR a scanned page with `pytesseract` or `unstructured` hi-res; keep a table as one chunk in Markdown.
- **Done when:** a question about a table cell is answered correctly.

## Day 8 - Metadata and parent-child chunks
- **Theory:** metadata (source, page, date, section, owner); small-to-big retrieval.
  - [LlamaIndex auto-merging / sentence-window retrieval](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag)
- **Watch:** [Advanced RAG 02 - Parent Document Retriever (Sam Witteveen, has Colab)](https://www.youtube.com/watch?v=wQEl0GGxPcM) * | [Advanced RAG 01: Small-to-Big Retrieval with LlamaIndex](https://www.youtube.com/watch?v=ihSiRrOUwmg) *
- **Practice:** store 150-token children with a pointer to 600-token parents; retrieve child, return parent.
- **Done when:** answer quality improves on 3 multi-sentence questions.

## Day 9 - Contextual chunking + Phase 2 quiz
- **Theory:** prepend situating context to each chunk before embedding.
  - [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- **Watch:** [The Best RAG Technique Yet? Anthropic's Contextual Retrieval Explained](https://www.youtube.com/watch?v=tmiBae2goJM) * | [Build Contextual Retrieval with Anthropic and Pinecone](https://www.youtube.com/watch?v=u-ocR-2P_YA) *
- **Practice:** for each chunk, ask the LLM for a 1-sentence context ("This chunk is from the 2024 refund policy, section 3"); embed context + chunk; re-run eval.
- **Done when:** you have before/after hit-rate numbers.
- **Then:** `quizzes/phase-02-quiz.md`.

Example (problem): chunk says "It expires after 30 days" with no subject. Example (fix): contextual prefix "Gift card terms, section 2:" makes it retrievable for "when do gift cards expire?".
