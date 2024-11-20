from typing import List
from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)

        for i, (src,dst) in enumerate(edges):
            adjList[src].append([dst,succProb[i]])
            adjList[dst].append([src,succProb[i]])

        pq = [(-1, start_node)]
        visited = set()
     
        while pq:
            prob, currNode = heapq.heappop(pq)
            visited.add(currNode)
            
            if currNode == end_node:
                return prob * -1
            
            for nei, edgeprob in adjList[currNode]:
                if nei not in visited:
                    heapq.heappush(pq, (prob * edgeprob,nei))
 
        return 0    



newObject = Solution()
print(newObject.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))