from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = {i: [] for i in range(N)}  
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        print(adjList)
        # Prrim's algo
        res = 0
        visit = set()
        minH = [[0, 0]] 
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adjList[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


newObject = Solution()

print(newObject.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))