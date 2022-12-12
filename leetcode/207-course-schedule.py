"""207. Course Schedule

Requirements
------------
- no cycles

Solution
--------
- DFS to find cycles. Keep track of 3 sets
    explore = has all nodes to be visited
    visiting = has all nodes in the current recursion stack
    done = has all the nodes, such that it and all of it's descendents are visited

Invariant not to be broken, the node being visited should never be in the
`visiting` set. If that's the case we have a cycle.

Exploration
-----------
0 <- 1
0 <- 1
  ->

[1,0], [2,0], [3,2], [1,3] - possible
num_courses = 3, impossible fewer than unique courses
    but this is given as a constraint.
num_courses = 4

[1,0], [2,0], [3,2], [1,3] - possible
[1] ->      [0]
 |           ^
 v           |
[3] ->      [2]

[1,0], [2,0], [3,2], [3,1] - possible
[1] ->      [0]
 ^           ^
 |           |
[3] ->      [2]

[1,0], [0,2], [2,3], [3,1] - impossible
[1] ->      [0]
 ^           |
 |           v
[3] <-      [2]

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return can_finish(numCourses, prerequisites)


def can_finish(num_classes, prereqs) -> bool:
    return not _has_cycle_dag(
        graph=_build_graph(edges=prereqs, num_nodes=num_classes),
    )
    

def _build_graph(edges: list[list[int]], num_nodes: int) -> list[set]:
    adj_set = [set() for _ in range(num_nodes)]
    for e in edges:
        adj_set[e[0]].add(e[1])
    print(f"{adj_set=}")
    return adj_set


def _has_cycle_dag(graph: list[set]) -> bool:
    """Checks if a DAG has a cycle.
    
    :param graph: Each item in a list is a node
        and each element in the set are the nodes at the
        head of the outward arc from this node.
    
    Sample cyclic input::

        [{2}, {0}, {3}, {1}]

        [1] -> [0]
        ^       |
        |       v
        [3] <-  [2]
    
    Sample non-cyclic input::

        [{}, {0,3}, {0}, {2}, {}]
          0    1     2    3    4
  
        [1] -> [0]     [4]
        |       ^
        v       |
        [3] -> [2]
    """
    explore = set(range(len(graph)))
    visiting, done = set(), set()
    while explore:
        if _cycle_dfs(
            node=next(iter(explore)),
            graph=graph,
            explore=explore,
            visiting=visiting,
            done=done,
        ):
            return True
    else:
        return False

def _cycle_dfs(node, graph, explore, visiting, done):
    _move_node(node, explore, visiting)
    for adj in graph[node]:
        if adj in done:
            continue
        if adj in visiting:
            return True
        if _cycle_dfs(node=adj, graph=graph, explore=explore, visiting=visiting, done=done):
            return True
    else:
        _move_node(node, visiting, done)
        return False

def _move_node(node, from_set, to_set) -> None:
    """Side effect, mutates the input sets"""
    from_set.discard(node)
    to_set.add(node)
