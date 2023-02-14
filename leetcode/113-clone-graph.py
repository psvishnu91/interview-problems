"""133. Clone Graph

https://leetcode.com/problems/clone-graph/

Solution: DFS T-O(N), S-O(N)
----------------------------
- have a dict called cloned_nodes[val] -> cloned_node
- start at the root node, create copy and add it to clone_nodes 
- for adj in neighbours: check if cloned_nodes in which case we just
    add it to new neighbours list, otherwise, we dfs to adj  create
    adj and it to neighb list.

# Todo need to handle empty list to None

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Edge cases
- null node
- single node with no adj
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        cloned_nodes = {}
        return _dfs(node=node, cloned_nodes=cloned_nodes)

def _dfs(node, cloned_nodes):
    """

    Test
    1-2-3-4
    |-----|

    node=1, [2,4], cn={1: n(1,[]), 2: n(2, [n(1, [])])}
    clone={1, []}  
            /           \
            2               4 

    """
    clone = Node(val=node.val, neighbors=[])
    cloned_nodes[clone.val] = clone
    if node.neighbors is None:
        clone.neighbors = None
        return clone
    for orig_adj in node.neighbors:
        if orig_adj.val in cloned_nodes:
            clone_adj = cloned_nodes[orig_adj.val]
        else:
            clone_adj = _dfs(node=orig_adj, cloned_nodes=cloned_nodes)
        clone.neighbors.append(clone_adj)
    return clone
