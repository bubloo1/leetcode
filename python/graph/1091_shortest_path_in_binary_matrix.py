from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size_of_grid = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        queue = [(0,0,1)]
        visited = set()

        while queue:
            r,c,length = queue.pop(0)
            if (min(r, c) < 0 or max(r, c) >= size_of_grid or
                grid[r][c]):
                continue
            if r == size_of_grid - 1 and c == size_of_grid - 1:
                return length

            for dr,dc in directions:
                if (r+dr,c+dc) not in visited:
                    queue.append((dr+r,dc+c,length+1))
                    visited.add((dr+r,dc+c))
        return -1

