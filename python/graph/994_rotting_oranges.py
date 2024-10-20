from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # => we need pos of rotten orange
        # => no of fresh orange
        queue = deque([])
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for dr, dc in directions:
                    dr = dr + r
                    dc = dc + c
                    if dr in range(rows) and dc in range(cols) and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        queue.append((dr,dc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1