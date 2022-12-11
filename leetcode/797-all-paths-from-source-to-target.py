"""797. All Paths From Source to Target

https://leetcode.com/problems/all-paths-from-source-to-target/

Solution DFS:
=============
We create a wrapper fn with output=[] and we create a running
path list which gets appended to ouptut once we find the final
node.

> WRONG assumption
> We know we are the final node as it contains no adjacent nodes.

We iterate over adjacent nodes, add it to the path dfs through it's
adjacent nodes and pop out this node.

Test
----
[[1,2],[3],[3],[]]

node  adj      path          outputs
-------------------------------------
0    [1,2]     [0]             []
--
1    [3]      [0,1]
3    []         [0,1,3]        [[0,1,3]]
2    [3]         [0,2]
3    []         [0,2,3]        [[0,1,3], [0,2,3]]
--

Edge cases
----------
[[]] - not possible according to test case
No circular
Disconnected graph
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return get_paths(graph=graph)

def get_paths(graph):
    output = []
    get_paths_rec(graph=graph, adj=graph[0], path=[0], output=output)
    return output


def get_paths_rec(graph, adj, path, output):
    if path[-1] == len(graph)-1:
        output.append(path[:])
        return
    for n in adj:
        path.append(n)
        get_paths_rec(graph=graph, adj=graph[n], path=path, output=output)
        path.pop()

