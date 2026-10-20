# Day 1 Notes: Why RAG, LLM basics, tokens

Written in easy language. Every concept has a small example (problem and fix) with real values.

---

## 1. Why RAG exists

An LLM only knows what it saw during training. This causes three problems:
- **Stale:** it knows nothing after its training cutoff.
- **Private:** it has never seen your documents.
- **Guessing:** when it does not know, some models invent an answer.

**RAG = Retrieval-Augmented Generation.** First retrieve the right text, then give it to the model with the question.

**Example (problem):** you ask "What is our refund window?" with no context. llama3.2 replied that it has no information about your refund window. (Some models would guess "30 days".)
**Example (fix):** paste "Our refund window is 17 days from delivery." into the prompt and it answers "17 days". RAG automates that pasting for thousands of documents.

**RAG vs fine-tuning vs prompting**
- Prompting: facts are small and fixed, so put them in the prompt.
- RAG: facts are large or change often, and you need citations.
- Fine-tuning: you want to change style or behavior, not facts.

---

## 2. Ollama vs Llama

- **Llama** = the model (the "brain", made by Meta). `llama3.2` is one version.
- **Ollama** = the program that downloads and runs models on your PC and lets Python talk to them.
- Analogy: Llama is the music file, Ollama is the music player. The player can also play other models (Mistral, Gemma, Qwen).
- `ollama.chat(model="llama3.2", ...)` means "Ollama, run the llama3.2 model for me".
- Why this matters: you can swap the model by changing one word and the RAG code stays the same.
- Why Ollama for you: the Claude Pro plan does not include API keys (API is billed separately), and Ollama is free and local.

---

## 3. What is a token?

The model does not read letters or words. It reads **tokens**: pieces of text, roughly 3/4 of a word on average.
- Common words are often 1 token (` cards`). Rare words split into pieces (`Un` + `refund` + `able`).
- The context window is the maximum number of tokens per request (prompt + answer).
- Tokens are also the unit of cost and speed.

**Example (problem):** you paste a 30-page manual into the prompt and the model errors or forgets the start.
**Example (fix):** count tokens first, split into chunks of about 500 tokens, and send only the best chunks.

---

## 4. Why convert text to numbers?

A neural network can only do math on numbers, so text must become numbers. It happens in two steps, using **two different tables**.

**Table 1: the tokenizer's table (text piece -> ID).** A plain dictionary with no meaning.
```
" gift"  -> 8352
" cards" -> 7563
```
**Table 2: the model's embedding table (ID -> list of numbers).** Lives inside the model. One row per ID, each row is a long list of numbers (llama3.2 uses 3,072 numbers per row) that the model learned during training.
```
row 8352 (" gift")  -> [ 0.21, -0.80, 0.05, ... ]   (values illustrative)
row 7563 (" cards") -> [ 0.19, -0.15, 0.62, ... ]
```
Words used in similar situations end up with similar rows (" gift" is near " present", far from " engine"). That is where "meaning" lives.

**Flow:** `"gift cards"` -> (Table 1) `[8352, 7563]` -> (Table 2) two lists of numbers -> the rest of the model predicts the next word.

The ID itself means nothing. It is like a seat number: "Seat 14" only makes sense with the right theater's seating chart.

---

## 5. What is tiktoken? What is cl100k_base?

- **tiktoken** = a small Python library from OpenAI that splits text into tokens and counts them, exactly like OpenAI's models do.
- **cl100k_base** = the name of one tokenizer (one Table 1). It was made for GPT-3.5/GPT-4 and has about 100,000 pieces (the "100k"). Newer GPT-4o models use `o200k_base` (about 200,000 pieces).

**Real output from this PC** for "Unrefundable gift cards":

| Tokenizer | Pieces | IDs |
|---|---|---|
| cl100k_base | Un . refund . able . gift . cards | 1844, 69583, 481, 8352, 7563 |
| o200k_base | Un . ref . undable . gift . cards | 2265, 1874, 117266, 10317, 10541 |

Same text, different cuts, different numbers. Decoding ID 8352 with the other table gave `'лы'`. A number only has meaning together with its own table.

---

## 6. How does tiktoken work with Ollama? (the confusing part)

**Short answer: tiktoken does NOT feed anything to Ollama.**

- Your code sends plain text (a string) to Ollama.
- Ollama runs llama3.2's **own** tokenizer, with its own Table 1, then the model's Table 2. tiktoken's IDs are never sent.
- tiktoken in your script is only a **ruler to estimate length**. You use it to answer "will this text fit?" before sending.

```
your text --(tiktoken)--> estimate only: "about 17 tokens"      (not sent)
your text --(plain string)--> Ollama --(llama3.2 tokenizer)--> real IDs --> model
```

**Why the estimate is good for English:** Meta built the Llama 3 tokenizer on top of the same family of tokenizer that tiktoken uses (it starts from the same ~100k pieces and adds ~28k more, for about 128k in total). This is from my own knowledge of the Llama 3 release, so confirm it on Meta's model card if you need to cite it. My measurement on your PC agrees with it:

| Text | tiktoken (cl100k_base) | llama3.2 real count |
|---|---|---|
| Our refund window is 17 days from delivery. Gift cards are not refundable. | 17 | 17 |
| Unrefundable gift cards | 5 | 5 |
| refund | 1 | 1 |
| "The quick brown fox..." x10 | 101 | 101 |
| आपकी रिफंड विंडो 17 दिन है (Hindi) | 28 | 16 |

(llama3.2's number = Ollama's `prompt_eval_count` minus about 25 tokens of chat-template overhead.)

**Reading the table:** for English, tiktoken is a perfect ruler for llama3.2 here. For Hindi it overcounts by almost 2x, because llama3.2's larger vocabulary has more Hindi pieces. I did not compare the IDs themselves, only the counts.

**Rules**
- Plan budgets with tiktoken only as an estimate, and add a safety margin (about 10-20%), especially for non-English text.
- For the exact number, ask Ollama: `r["prompt_eval_count"]` (includes about 25 template tokens).
- Never pass token IDs from one model to another. Pass text.
- For Claude later, use Anthropic's token-counting API instead of tiktoken.

**Example (problem):** you size chunks at 500 tiktoken tokens for Hindi documents and assume you have room, but the real llama3.2 count is lower (16 vs 28 above), so the budget is wasted by almost half.
**Example (fix):** measure with `prompt_eval_count` on a sample of your real documents and set the chunk size from that.

---

## 7. Windows and Python gotchas

- **Error:** `ModuleNotFoundError: No module named 'ollama'` when running `python3 day1.py`.
- **Cause:** `python3` is a Microsoft Store shortcut to the system Python, which has no `ollama`. The libraries were installed inside the project's `.venv`.
- **Fix:** activate the venv, then use `python` (not `python3`):
```
cd "C:\AI Tutorials\rag-journey"
.venv\Scripts\activate
python day1.py
```
- **Why `python` works but `python3` does not:** a Windows venv only creates `python.exe` (no `python3.exe`), so after activation `python` finds the venv's one, while `python3` falls through to the Store shortcut.
- Inside an activated venv always type `python` and `pip`.

---

## 8. Day 1 summary (what you should be able to say)

1. RAG = retrieve the right text, then generate an answer from it.
2. A token is a piece of text, and the model reads token IDs, not words.
3. Tokenizer table: text piece to ID. Embedding table: ID to a list of learned numbers (the meaning).
4. tiktoken is a ruler for estimating length. It does not feed Ollama.
5. Ollama runs the model; llama3.2 is the model.

## 9. Self-check (answer in your own words)
1. Why can't we paste all company documents into every prompt?
2. Name one case where fine-tuning is better than RAG.
3. In one sentence: why does the same token ID mean different things in different models?
4. Does the output of `tiktoken.encode()` get sent to Ollama? What is it used for?

## 10. My own notes
(Write the things that confused you and how you solved them here.)
