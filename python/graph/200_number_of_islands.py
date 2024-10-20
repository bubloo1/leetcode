from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,columns = len(grid), len(grid[0])
        visited = set()

        def bfs(r,c):
        
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    row,col = dr + r, dc + c

                    if row in range(rows) and col in range(columns) and grid[row][col] == "1" and (row,col) not in visited:
                        queue.append((row,col))
                        visited.add((row,col))


        islands = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    bfs(i,j)
        return islands 