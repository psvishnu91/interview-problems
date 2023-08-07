"""399. Evaluate Division

https://leetcode.com/problems/evaluate-division

Solution 1: Graphs 
------------------
N - Equations, M - Queries
T - O(N * M)
S - O(N)

Represent each symbol as a node.
The node has neighbours with an associated edgeweight.
The edgeweight <- node / neigb

For each equation
    1. a, b = 2, we create new nodes or update existing nodes.
        a.neib[b] = 2
        b.neib[a] = 1/2
    2.  b, c = 3
        b.neib[c] = 3
        c.neib[b] = 1/3

For each query
    1. a/c, dfs from `a` to get to c
        a -> b -> c
        a.neib[b] * b.neib[c]
        2 * 3

Edge cases,
1. variables in query don't exist in equations
2. var_i / var_i = 1


Idea 2: DSU 
-----------
d/m

a/b=2
b/c=3
b/e=4
f/e=5

        a                    d
     2 / 6\ 8\ (8/5)\        \
      b    c  e     f         m

- For every equation
    a/b = 2
    - Union a and b through it's parent.
    - Find_leader recursive function will push every new element
        under parent applying the apt mult.
    - Since both a and b are parents, we pick either as parent.
        here order of union has meaning.
    - let's take a scenario like below
                    a   (union(b, c)=3)    d
                   /2                       \ 4
                   b                         c
        to union these we will get parent (b) with edge wt
        parent[b] = a, edge_wt[b] = 2
        parent[c] = d, edge_wt[c] = 4
        parent[parent[c]] = parent[b] 
            (parent[d]= a)
        edge_wt[d] = edge_wt[b] * eqn(b, c) * (1 / edge_wt[c])

                    a   (union(c, b)=3)    d
                   /2                       \ 4
                   b                         c
        parent[d] = a
        edge_wt[d] = edge_wt[b] * (1 / eqn(c, b)) * (1 / edge_wt[c])


        a
        \ 3
        b
        \ 2
        c
        \ 4
        d
"""
import dataclasses as dc


@dc.dataclass
class Symbol:
    var: str
    neibs: dict['Symbol', float] = dc.field(default_factory=dict)

    def __hash__(self):
        return hash(self.var)


@dc.dataclass
class QuerySearchResult:
    ratio: float = 1.
    found: bool = False


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        return solve_w_graphs(equations, values, queries)

############################################################################
# SOLUTION 1: GRAPHS
############################################################################

def solve_w_graphs(equations, values, queries):
    # {symbol.char -> symbol}
    var2node = _build_symgraph(equations=equations, values=values)
    return [
        query_graph(var2node=var2node, query=query)
        for query in queries
    ]

def _build_symgraph(equations, values) -> dict[str, Symbol]:
    var2node = {}
    for (var1, var2), ratio in zip(equations, values):
        v1node = _get_node(var=var1, var2node=var2node)
        v2node = _get_node(var=var2, var2node=var2node)
        v1node.neibs[v2node] = ratio
        v2node.neibs[v1node] = 1 / ratio
    return var2node

def _get_node(var: str, var2node: dict) -> Symbol:
    try:
        return var2node[var]
    except KeyError:
        var2node[var] = Symbol(var=var)
        return var2node[var]

def query_graph(var2node, query):
    var1, var2 = query
    # Handle edge cases
    if var1 not in var2node or var2 not in var2node:
        return -1
    if var1 == var2:
        return 1
    # Let's assume a path always exists
    return _query_dfs(
        product=1.,
        cur=var2node[var1],
        end=var2node[var2],
        seen=set(),
    ).ratio

def _query_dfs(product, cur, end, seen) -> QuerySearchResult:
    if cur == end:
        return QuerySearchResult(ratio=product, found=True)
    seen.add(cur)
    for nb_sym, sub_prod in cur.neibs.items():
        if nb_sym in seen:
            continue
        res = _query_dfs(
            product=product * sub_prod,
            cur=nb_sym,
            end=end,
            seen=seen,
        )
        if res.found:
            return res
    else:
        return QuerySearchResult(ratio=-1., found=False)


############################################################################
# SOLUTION 2: DSU
############################################################################

class DivideDSU:

    def __init__(self, vars):
        self.parent = {var: var for var in vars}
        self.edge_wt = {var: 1. for var in vars}
        self.rank = {var: 1 for var in vars}

    def find_leader(self, var) -> str:
        if self.parent[var] == var:
            return var
        prev_parent = self.parent[var]
        self.parent[var] = self.find_leader(self.parent[var])
        self.edge_wt[var] *= self.edge_wt[prev_parent]
        return self.parent[var]

    def add_eqn(self, nr, dr, ratio):
        # union
        nr_lead = self.find_leader(var=nr)
        dr_lead = self.find_leader(var=dr)
        if nr_lead == dr_lead:
            return
        # When dr_lead goes under nr_lead
        maybe_dr_lead_edge_wt = (
            self.edge_wt[nr] * ratio * (1/self.edge_wt[dr])
        )
        # When nr_lead goes under dr_lead
        maybe_nr_lead_edge_wt = (
            self.edge_wt[dr] * (1/ratio) * (1/self.edge_wt[nr])
        )
        if self.rank[nr_lead] > self.rank[dr_lead]:
            self.parent[dr_lead] = nr_lead
            self.edge_wt[dr_lead] = maybe_dr_lead_edge_wt
        elif self.rank[dr_lead] > self.rank[nr_lead]:
            self.parent[nr_lead] = dr_lead
            self.edge_wt[nr_lead] = maybe_nr_lead_edge_wt
        else:
            # self.rank[dr_lead] == self.rank[nr_lead]:
            # Pick either one and increase height
            self.rank[nr_lead] += 1
            self.parent[dr_lead] = nr_lead
            self.edge_wt[dr_lead] = maybe_dr_lead_edge_wt
    
    def find_ratio(self, nr, dr):
        if nr not in self.parent or dr not in self.parent:
            return -1.
        if nr == dr:
            return 1.
        nr_lead = self.find_leader(nr)
        dr_lead = self.find_leader(dr)
        if nr_lead != dr_lead:
            return -1.
        # b / c ? 
        #
        #                 a
        #     / e[b]=a/b        \ e[c]=a/c
        #    b                      c
        # (1/e[b]) * (e[c]) = b/a * a/c 
        return (1 / self.edge_wt[nr]) * self.edge_wt[dr]


def solve_w_dsu(equations, values, queries):
    # vars
    div_dsu = DivideDSU(
        vars=set(var for eqn in equations for var in eqn)
    )
    for (nr, dr), ratio in zip(equations, values):
        div_dsu.add_eqn(nr=nr, dr=dr, ratio=ratio)
    return [div_dsu.find_ratio(nr=nr, dr=dr) for nr, dr in queries]
