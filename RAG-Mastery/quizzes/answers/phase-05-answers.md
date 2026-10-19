# Phase 5 Answer Key

1. Role/task; "answer only from the context"; fallback rule ("say you don't know"); citation/format rules. Context clearly delimited and labelled with IDs.
2. Label chunks [doc1], [doc2]; require citation per claim; verify programmatically that cited IDs exist and the claim is supported (judge or string overlap).
3. Prompt rule plus a retrieval score threshold (no good chunk -> refuse); also a grader/groundedness check.
4. Models use information at the start and end of long context better than the middle. Put the best chunks first/last, limit k, rerank, compress.
5. Cost and latency, noise reduces accuracy, access control and freshness, scale beyond the window, easier citations.
6. Trimming retrieved text to relevant parts before the LLM. Risk: dropping a needed sentence.
7. Predictable parsing, UI display of sources, confidence flags, easier evaluation.
8. Groundedness check (claim-by-claim vs context; Ragas faithfulness), stricter prompt, lower temperature, require citations, abstain if unsupported.
