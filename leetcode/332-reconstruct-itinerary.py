"""332. Reconstruct Itinerary

https://leetcode.com/problems/reconstruct-itinerary

The problem is composed of directed cyclic graph. Gotcha can have 
multiple edges from same airport to dest airport.

The way we approach this problem is DFS. Since we need to use up
all the tickets we need a path of length tickets+1 or edges +1. 
Creates a linkedlist at the end. We first construct a map of 
from_location to edges (sorted by lexicographic order).  

We begin at JFK. And then we pick the next available edge, 
updating path. We keep going down dfs greedily, if we arrive at
a destination with no outward flights or no remaining edges but we 
haven't used up all the edges then we have found an invalid solution. 
If we ever reach the sitatuation where pos=len(path) we are done, we 
return true. And all the upper recursion stack returns true. 

Testing
-------
We want to search through this graph such that we reach
touch all the edges.

{JFK: [ATL, SFO], SFO: [ATL], ATL: [JFK,SFO]}
edges = {()}
path = [J,A,N,N,N,N]
                        pos=0, JFK
                        /           \
                    pos=1,ATL       pos=1,SFO
                    /       \                 \
                pos=2,JFK   pos=2,SFO
                /

"""
import dataclasses

ST_LOC = "JFK"


@dataclasses.dataclass(order=True)
class Edge:
    to_location: str
    used: bool = False


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        num_edges = len(tickets)
        node_to_edges = build_node_to_edges(tickets)
        path = [None]*(num_edges+1)
        print(node_to_edges)
        path[0] = ST_LOC
        _dfs(
            pos=1,
            node=ST_LOC,
            node_to_edges=node_to_edges,
            path=path
        )
        return path

def build_node_to_edges(tickets):
    node_to_edges = {}
    for from_place, to_place in tickets:
        edge = Edge(to_place)
        if from_place not in node_to_edges:
            node_to_edges[from_place] = [edge]
        else:
            node_to_edges[from_place].append(edge)
    return {
        from_place: sorted(edges)
        for from_place, edges in node_to_edges.items()
    }


def _dfs(pos, node, node_to_edges, path):
    if pos == len(path):
        return True
    for edge in node_to_edges.get(node, []):
        if edge.used:
            continue
        edge.used = True
        next_loc = edge.to_location
        path[pos] = next_loc
        if _dfs(
            pos=pos+1,
            node=next_loc,
            node_to_edges=node_to_edges,
            path=path,
        ):
            return True
        edge.used = False
    else:
        return False
