#!/usr/bin/env python3
"""Tiny exact examples. Bit i represents vertex/coordinate i; no SAT dependency."""
from itertools import combinations
import json
from math import inf

def subsets(mask):
    s = mask
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & mask

def cost(family, target, n, model="mixed"):
    if target not in family:
        return inf
    full = (1 << n) - 1
    pool = target if model == "include" else full ^ target if model == "exclude" else full
    return min(d.bit_count() for d in subsets(pool)
               if sum(((z ^ target) & d) == 0 for z in family) == 1)

def best(family, n, model="mixed"):
    return min((cost(family, t, n, model) for t in family), default=inf)

def covers(n, edges, active=None):
    active = (1 << n) - 1 if active is None else active
    return [s for s in subsets(active)
            if all((s >> u) & 1 or (s >> v) & 1
                   for u, v in edges if active >> u & 1 and active >> v & 1)]

def optima(family):
    k = min(s.bit_count() for s in family)
    return k, [s for s in family if s.bit_count() == k]

def graph_row(name, n, edges):
    tau, opts = optima(covers(n, edges))
    return {"name": name, "n": n, "tau": tau, "number_of_minimum_covers": len(opts),
            "include": best(opts, n, "include"), "exclude": best(opts, n, "exclude"),
            "mixed": best(opts, n, "mixed")}

def verify():
    rows = [
        graph_row("K3", 3, list(combinations(range(3), 2))),
        graph_row("K5", 5, list(combinations(range(5), 2))),
        graph_row("C4", 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        graph_row("P3", 3, [(0, 1), (1, 2)]),
    ]
    assert [(r["include"], r["exclude"], r["mixed"]) for r in rows] == [
        (2, 1, 1), (4, 1, 1), (1, 1, 1), (0, 0, 0)]
    family = [0, 1, 2, 4]
    fixed = [cost(family, t, 3) for t in family]
    assert fixed == [3, 1, 1, 1]
    global_cost = min(d.bit_count() for d in range(8)
                      if len({s & d for s in family}) == len(family))
    assert global_cost == 3
    assert best([], 3) == inf and best([0], 3) == 0
    # Minimal need not mean minimum.
    family2 = [0, 3, 5]
    assert cost(family2, 0, 3) == 1
    assert all(any(d & z for z in family2[1:]) for d in (1, 6))
    assert all(not all(d & z for z in family2[1:]) for d in (0, 2, 4))
    tau, original = optima(covers(3, [(0, 1), (1, 2)]))
    constrained = [s for s in covers(3, [(0, 1), (1, 2)]) if s & 5 == 5]
    value, constrained_opts = optima(constrained)
    assert tau == 1 and original == [2] and value == 2 and constrained_opts == [5]
    tested = 0
    for n in range(5):
        universe = list(combinations(range(n), 2))
        for e in range(1 << len(universe)):
            edges = [uv for j, uv in enumerate(universe) if e >> j & 1]
            tau, opts = optima(covers(n, edges))
            costs = [best(opts, n, m) for m in ("include", "exclude", "mixed")]
            assert costs[1] == costs[2] <= costs[0]
            for a in range(1 << n):
                k, residual = optima(covers(n, edges, ((1 << n) - 1) ^ a))
                succeeds = sum(s & a == a for s in opts) == 1
                assert succeeds == (len(residual) == 1 and k == tau - a.bit_count())
            for t in opts:
                for d in range(1 << n):
                    direct = sum((s ^ t) & d == 0 for s in opts) == 1
                    hitting = all((s ^ t) & d for s in opts if s != t)
                    assert direct == hitting
            tested += 1
    return {"graph_examples": rows,
            "fixed_target_costs": {"000": fixed[0], "100": fixed[1],
                                   "010": fixed[2], "001": fixed[3]},
            "global_distinguishing_cost": global_cost,
            "all_labelled_graphs_n_at_most_4_checked": tested,
            "checks": ["model cost relation for selectable targets",
                       "INCLUDE deletion and optimum-preservation equivalence",
                       "difference-set hitting equivalence",
                       "restricted-reoptimization counterexample",
                       "empty and singleton families",
                       "minimal versus minimum"]}

if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))

