"""785. Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

Brute force:
Create all combinations of two-sets. And check if bipartite, by
iterating over edges and checking if the edge connects both sides.


Solution 2: Not accepted
- We iterate over each node N
- We try adding to set a if we cannot add it to set b. If we cannot we return false.
- the check for can add, is based on the outward edges from N, if it has any in set being
added, cannot add.


def _dfs(node, seta, setb, graph):
    if node == len(graph):
        return True
    for gset in (seta, setb):
        if not can_add(node, gset, graph):
            continue
        gset.add(node)
        if _dfs(node=node+1, seta=seta, setb, graph):
            return True
        gset.discard(node)
    else:
        return False

[[1,3], [0,2], [1,3], [0,2]]

                node=0, A {} B {}
                   /        \
            n=1 A{0}B{}        A{} B{0}
                /
              A{0}B{1}
              /
              A{0,2} B{1,3}

Solution 3: Graph colouring
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # graph coloring
        color = {}
        for node in range(len(graph)):
            if node in color:
                continue
            if not _dfs(node=node, graph=graph, color=color):
                return False
        else:
            return True

def _dfs(node, graph, color):
    color[node] = 0
    stk = [node]
    while stk:
        nd = stk.pop()
        for adj in graph[nd]:
            if adj not in color:
                color[adj] = ~color[nd]
                stk.append(adj)
            elif color[adj] == color[nd]:
                return False
    else:
        return True
