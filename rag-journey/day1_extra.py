"""Day 1 extra tasks.

Task 1: ask something the context does NOT answer. Does the model admit it or invent?
Task 2: count tokens of a long text and work out how many 500-token chunks it makes.

Before Task 2: paste about 3 pages of any text (an article, a Wikipedia page) into sample.txt in this folder.
Run:  python day1_extra.py
"""
import math
import os

import ollama
import tiktoken

MODEL = "llama3.2"
policy = "Our refund window is 17 days from delivery. Gift cards are not refundable."


def ask(prompt):
    reply = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return reply["message"]["content"].strip()


# ---- Task 1 ----
question = "What is our shipping time?"          # NOT in the policy
print("TASK 1 - plain prompt:")
print(ask(f"Answer using only this context:\n{policy}\n\nQuestion: {question}"))
print()
print("TASK 1 - with an 'I don't know' rule:")
print(ask(
    f"Answer using only this context:\n{policy}\n\nQuestion: {question}\n\n"
    "If the context does not contain the answer, reply exactly: I don't have that information."
))
print()

# ---- Task 2 ----
if not os.path.exists("sample.txt"):
    print("TASK 2 skipped: create sample.txt (paste about 3 pages of text) and run again.")
else:
    text = open("sample.txt", encoding="utf-8").read()
    enc = tiktoken.get_encoding("cl100k_base")
    n = len(enc.encode(text))
    print(f"TASK 2 - words: {len(text.split())}, tokens (estimate): {n}")
    print(f"TASK 2 - 500-token chunks needed: {math.ceil(n / 500)}")
