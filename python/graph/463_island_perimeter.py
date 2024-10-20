from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
      

        def dfs(r,c):
            
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] == 0):
                return  1

            if (r, c) in visited:
                return 0
            
            visited.add((r,c))
           
            perim = dfs(r+1, c)
            perim += dfs(r-1, c)
            perim += dfs(r, c+1)
            perim += dfs(r, c-1)


            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
                   