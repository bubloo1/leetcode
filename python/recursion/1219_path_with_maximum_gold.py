from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        def dfs(r,c, visited):
            if r not in range(rows) or c not in range(columns) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            gold = grid[r][c] + max(
                dfs(r + 1, c, visited),
                dfs(r - 1, c, visited),
                dfs(r, c + 1, visited),
                dfs(r, c - 1, visited)
            )
            visited.remove((r, c))  
            return gold
        ans = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] != 0:
                    ans = max(ans,dfs(r,c,set()))
        return ans