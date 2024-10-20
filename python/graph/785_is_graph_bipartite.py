from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def chaeckColorBfs(start,color):
            queue = []
            queue.append(start)
            color[start] = 0
            while queue:
                node = queue.pop(0)

                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 if color[node] == 0 else 0
                        queue.append(neighbour)
                    else:
                        if color[neighbour] == color[node]:
                            return False

        color = [-1 for i in range(len(graph))]
       
        for i in range(len(graph)):
            if color[i] == -1:
                if chaeckColorBfs(i,color) == False:
                    return False

        return True
        