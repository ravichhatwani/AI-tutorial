"""Day 17 lab: retrieval metrics from scratch (no libraries).

Run:  python metrics.py
Each function takes, per query, the ranked list of retrieved chunk IDs and the set of relevant chunk IDs.
"""
import math


def recall_at_k(retrieved, relevant, k):
    """Share of relevant items found in the top k. Example: 1 of 2 relevant found -> 0.5"""
    if not relevant:
        return 0.0
    return len(set(retrieved[:k]) & set(relevant)) / len(relevant)


def hit_at_k(retrieved, relevant, k):
    """1 if ANY relevant item is in the top k, else 0 (this is the 'hit-rate' from Day 4)."""
    return 1.0 if set(retrieved[:k]) & set(relevant) else 0.0


def reciprocal_rank(retrieved, relevant):
    """1/rank of the first relevant item; 0 if none found."""
    for i, doc in enumerate(retrieved, start=1):
        if doc in relevant:
            return 1.0 / i
    return 0.0


def ndcg_at_k(retrieved, relevant, k):
    """Rewards relevant items near the top. Binary relevance version."""
    dcg = sum(1.0 / math.log2(i + 1) for i, d in enumerate(retrieved[:k], start=1) if d in relevant)
    ideal_hits = min(len(relevant), k)
    idcg = sum(1.0 / math.log2(i + 1) for i in range(1, ideal_hits + 1))
    return dcg / idcg if idcg else 0.0


def evaluate(results, k=5):
    """results = list of (retrieved_ids, relevant_ids). Returns averages over queries."""
    n = len(results)
    return {
        f"hit@{k}": sum(hit_at_k(r, rel, k) for r, rel in results) / n,
        f"recall@{k}": sum(recall_at_k(r, rel, k) for r, rel in results) / n,
        "MRR": sum(reciprocal_rank(r, rel) for r, rel in results) / n,
        f"nDCG@{k}": sum(ndcg_at_k(r, rel, k) for r, rel in results) / n,
    }


if __name__ == "__main__":
    # Worked example with real values (3 queries).
    results = [
        (["c7", "c2", "c9"], {"c7"}),        # right chunk ranked 1st  -> RR = 1.0
        (["c4", "c1", "c3"], {"c3"}),        # right chunk ranked 3rd  -> RR = 0.333
        (["c5", "c6", "c8"], {"c2"}),        # right chunk missing     -> RR = 0.0
    ]
    scores = evaluate(results, k=3)
    print(scores)
    assert abs(scores["MRR"] - (1 + 1 / 3 + 0) / 3) < 1e-9          # 0.444, matches quiz Phase 3 Q11
    assert scores["hit@3"] == 2 / 3
    assert abs(ndcg_at_k(["c1", "c2"], {"c2"}, 2) - 1 / math.log2(3)) < 1e-9
    print("All checks passed.")
