from typing import List
from collections import defaultdict,deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdjList = defaultdict(list)
        blueAdjList = defaultdict(list)

        for u,v in redEdges:
            redAdjList[u].append(v)
        for u,v in blueEdges:
            blueAdjList[u].append(v)

        dist = [-1 for i in range(n)]
        queue = deque()
        queue.append([0,0,None])
        visited = set()
        visited.add((0,None))

        while queue:
            node, length, edgeColor = queue.popleft()
            if dist[node] == -1:
                dist[node] = length

            if edgeColor != "RED":
                for nei in redAdjList[node]:
                    if (nei,"RED") not in visited:
                        visited.add((nei,"RED"))
                        queue.append([nei,length + 1, "RED"])

            if edgeColor != "BLUE":
                for nei in blueAdjList[node]:
                    if (nei,"BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        queue.append([nei,length + 1, "BLUE"])
        return dist
newObject = Solution()
print(newObject.shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))