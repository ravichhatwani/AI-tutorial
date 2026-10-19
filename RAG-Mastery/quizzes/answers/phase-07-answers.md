# Phase 7 Answer Key

1. Keep the last N turns (or tokens) in the prompt. Limit: older info is dropped and tokens cost grows.
2. Saves tokens but loses detail and may add errors; summary quality matters.
3. Semantic: facts/preferences ("vegetarian"). Episodic: past events/interactions ("last Tuesday we debugged the ETL job").
4. On important, stable information (preferences, decisions, corrections), usually after the session or via an extraction step; not every message.
5. Store `user_id` in metadata and enforce it as a mandatory filter at query time; test with two users.
6. Mark the old fact inactive/superseded (keep timestamp); the newer fact wins; or ask for confirmation if unclear.
7. Passwords, API keys, payment/government IDs, health or sensitive data without consent, other people's private info. Support deletion by `user_id` removal and verify with a search.
8. Separate labelled sections: `<user_memory>` and `<documents>`; tell the model memory is for personalization and documents are the source of facts to cite.
