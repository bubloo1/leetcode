from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length_graph = len(graph)
        adjRev = [[] for _ in range(length_graph)]
        indegree = [0] * length_graph
        # Reverse the edges and compute in-degrees
        for i in range(length_graph):
            for it in graph[i]:
                adjRev[it].append(i)
                indegree[i] += 1

        # Initialize queue with nodes having in-degree 0
        q = deque()
        safeNodes = []
        for i in range(length_graph):
            if indegree[i] == 0:
                q.append(i)

        # Topological Sort
        while q:
            node = q.popleft()
            safeNodes.append(node)
            for it in adjRev[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return sorted(safeNodes)

    
        