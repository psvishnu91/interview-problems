"""261. Graph Valid Tree

https://leetcode.com/problems/graph-valid-tree/

Main idea, find if there are cycles in an undirected graph
and all the nodes are connected

Solution 1: DFS + set
---------------
T-O(n), S-O(n)

We start at a node and dfs through neighbours and
during recursion if one of the adj is an already seen node
and not the parent that led us here, then we have a cycle.


Solution 2: Disjoint Set Union
------------------------------
We create a disconnected dsu for all the nodes.  For every edge
we check if the two nodes are already connected, if so we we
return false, otherwise if we iterated through everything and never
found a cycle we return true.

Edge cases
==========
[]

"""
class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.max_size = 1

    def leader(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.leader(node=self.parent[node])
        return self.parent[node]
    
    def union(self, node_1, node_2):
        n1_lead = self.leader(node_1)
        n2_lead = self.leader(node_2)
        if self.rank[n1_lead] > self.rank[n2_lead]:
            self._update_lead(child=n2_lead, new_lead=n1_lead)
        elif self.rank[n1_lead] < self.rank[n2_lead]:
            self._update_lead(child=n1_lead, new_lead=n2_lead)
        else:
            # equal rank
            self._update_lead(child=n2_lead, new_lead=n1_lead)
            self.rank[n1_lead] += 1
    
    def _update_lead(self, child, new_lead):
        self.parent[child] = new_lead
        self.size[new_lead] += self.size[child]
        self.max_size = max(self.max_size, self.size[new_lead])
    
    def is_connected(self, node_1, node_2):
        return self.leader(node_1) == self.leader(node_2)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return _valid_dsu(n=n, edges=edges)
        # return _valid_dfs(n=n, edges=edges)


def _valid_dsu(n, edges):
    if n==0:
        return True
    dsu = DSU(n=n)
    for n1, n2 in edges:
        if dsu.is_connected(n1, n2):
            return False
        dsu.union(n1, n2)
    else:
        return dsu.max_size == n

#---------------------------------------

def _valid_dfs(n, edges):
    graph = _to_adj_list(edges=edges, n=n)
    seen = set()
    if not _dfs(node=0, parent=None, graph=graph, seen=seen):
        return False
    else:
        print(seen, graph)
        return len(seen) == n

def _to_adj_list(edges, n):
    adj_list = [[] for _ in range(n)]
    for n1, n2 in edges:
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
    return adj_list


def _dfs(node, parent, graph, seen):
    seen.add(node)
    for adj in graph[node]:
        if adj == parent:
            continue
        if adj in seen:
            return False
        if not _dfs(node=adj, parent=node, graph=graph, seen=seen):
            return False
    else:
        return True

