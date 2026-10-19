# Phase 2 Answer Key

1. Multi-column text read in wrong order; headers/footers repeated in every chunk; tables flattened into nonsense; hyphenation/encoding errors; missing scanned pages.
2. Fixed: simple/fast, may cut mid-sentence; fine for uniform text. Recursive: splits on paragraph, then sentence, then word - preserves structure; the sensible default.
3. Chunk embeds many topics, so the vector is blurry and the prompt is noisy. Use ~200-500 tokens, or parent-child.
4. Facts straddling a boundary. Cost: more chunks, storage, duplicates in results.
5. Convert to Markdown/CSV text as one chunk with caption + headers repeated; or summarize table and store raw table as payload.
6. Scanned/image PDFs. Verify by sampling output vs the page image; check numbers and names.
7. source (filter by file), page (cite), date (latest only), section (scoped search), allowed_groups/owner (access control).
8. Embed small child chunks for precise matching, then return the larger parent chunk to the LLM for full context.
9. Chunks lose their subject. Before: "It expires after 30 days." After: "[Gift card terms, section 2] It expires after 30 days."
10. `i=0; while i < len(text): out.append(text[i:i+size]); i += size - overlap` (size-overlap = step of 450).
