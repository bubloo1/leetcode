from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        n = len(heights)
        m = len(heights[0])

        pq = [(0, 0, 0)]


        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        while pq:
            diff, row, col = heapq.heappop(pq)

            if row == n - 1 and col == m - 1:
                return diff

            for dr,dc in direction:
                newr = row + dr
                newc = col + dc

               
                if 0 <= newr < n and 0 <= newc < m:
    
                    newEffort = max(abs(heights[row][col] - heights[newr][newc]), diff)

                    if newEffort < dist[newr][newc]:
                        dist[newr][newc] = newEffort
                        heapq.heappush(pq, (newEffort, newr, newc))

        return 0 
