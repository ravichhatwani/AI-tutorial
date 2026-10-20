"""Day 1 lab: see an LLM fail on a private fact, fix it with context, count tokens.

Setup (once):
  1. Install Ollama from https://ollama.com/download and open a new terminal.
  2. ollama pull llama3.2
  3. pip install ollama tiktoken
Run:  python day1.py
"""
import ollama

MODEL = "llama3.2"

policy = "Our refund window is 17 days from delivery. Gift cards are not refundable."
question = "What is our refund window?"


def ask(prompt):
    reply = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return reply["message"]["content"].strip()


print("WITHOUT context:", ask(question))
print()
print("WITH context:   ", ask(f"Answer using only this context:\n{policy}\n\nQuestion: {question}"))
print()

# Count tokens. tiktoken is an estimate for non-OpenAI models; if it will not install, skip it.
try:
    import tiktoken

    enc = tiktoken.get_encoding("cl100k_base")
    print("Policy tokens (tiktoken estimate):", len(enc.encode(policy)))
except ImportError:
    print("tiktoken not installed; skipping the estimate.")

# Ollama also reports how many tokens it fed the model. This includes a few extra chat-template tokens (about 25), so it is higher than the plain-text count.
r = ollama.chat(model=MODEL, messages=[{"role": "user", "content": policy}])
print("Prompt tokens as Ollama counted them (text + chat template):", r["prompt_eval_count"])
