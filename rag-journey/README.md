# rag-journey (my code for the RAG Mastery plan)

## Setup on Windows (do once)
1. Install Ollama: https://ollama.com/download , then open a NEW PowerShell window.
2. Download a small model (about 2 GB): `ollama pull llama3.2`
3. Test it: `ollama run llama3.2 "Say hi"` (type `/bye` to exit)
4. Create a Python environment in this folder:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install ollama tiktoken
   ```
5. Run Day 1: `python day1.py`

## If `pip install tiktoken` fails
Your PC is a Snapdragon (ARM) Windows laptop. Some libraries do not have ARM builds yet. If tiktoken fails, run `pip install ollama` only. `day1.py` skips tiktoken and prints Ollama's own token count instead, which is the count the model actually used (it includes about 25 chat-template tokens).

## Example (problem)
Without context, llama3.2 says it does not know your refund window (some models would guess "30 days" instead).

## Example (fix)
With the policy text in the prompt, it answers "17 days". That is RAG in miniature.
