"""433. Minimum Genetic Mutation

https://leetcode.com/problems/minimum-genetic-mutation/

Exploration
-----------
Solution 1: BFS (faster)
------------------------
BFS, from current genome, we look at every
valid one mutation change and then continue until we
find the distance to the mutation we desire. We don't visit
the same node again because we reaching it earlier in the search
needs fewer mutations.

T - O(V + E)
if n is the length of the string, O(4^n) solution.

Solution 2: A*
--------------
T - O(ElogV)

We start at the startnode, the priority queue contains source
then for each child node, we push to the heap with
dist = dist(start_gene, cur_gene) + manhattan_dist(end_gene).

Because the heuristic manhattan_dist is an underestimate we are
guaranteed optimality.
"""
import heapq as hq

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        return min_mutation_bfs(
            start_gene=startGene,
            end_gene=endGene,
            bank=set(bank),
        )

#######################################################
# Solution 1: BFS
#######################################################

def min_mutation_bfs(start_gene, end_gene, bank):
    q = collections.deque([start_gene])
    visited = {start_gene}
    mutations = 0
    while q:
        qlen = len(q)
        for _ in range(qlen):
            gene = q.popleft()
            if gene == end_gene:
                return mutations
            for adj in _iter_mutations(gene=gene, bank=bank):
                if adj in visited:
                    continue
                q.append(adj)
                visited.add(adj)
        mutations += 1
    else:
        return -1



def _iter_mutations(gene, bank):
    mutant = list(gene)
    for i, orig_c in enumerate(gene):
        for c in ['A', 'C', 'G', 'T']:
            if c == orig_c:
                continue
            mutant[i] = c
            mutant_str = ''.join(mutant)
            if mutant_str in bank:
                yield mutant_str
            mutant[i] = orig_c


#######################################################
# Solution 2: A star
#######################################################

def min_mutation_a_star(start_gene, end_gene, bank):
    dist = {start_gene: 0}
    heap = [(0, start_gene)]
    visited = set()
    while heap:
        cur_dist, cur_gene = hq.heappop(heap)
        if cur_gene == end_gene:
            return cur_dist
        if cur_gene in visited:
            continue
        visited.add(cur_gene)
        for adj_gene in _iter_mutations(gene=cur_gene, bank=bank):
            if adj_gene in visited:
                continue
            this_dist = dist[cur_gene] + 1
            if dist.get(adj_gene, float('inf')) > this_dist:
                dist[adj_gene] = this_dist
                heuristic = this_dist # + manhattan_dist(adj_gene, end_gene)
                hq.heappush(heap, (heuristic, adj_gene))
    else:
        return -1


def manhattan_dist(s1, s2) -> int:
    # assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
