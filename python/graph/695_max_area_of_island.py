from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans,res = 0,0

        def bfs(r,c):
            area = 1
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()

                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direction:
                    row,col = dr + r, dc + c

                    if (row in range(rows) and 
                        col in range(cols) and 
                        (row, col) not in visited and 
                        grid[row][col] == 1):
                        q.append((row,col))
                        visited.add((row, col))
                        area += 1
            return area
                

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans = bfs(i,j)
                    res = max(res, ans)
        return res