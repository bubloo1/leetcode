from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid
        grid = [["." for _ in range(n)] for _ in range(m)]

        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"

        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Mark guarded cells
        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] not in ("G", "W"):
                    if grid[r][c] == ".":
                        grid[r][c] = "V"
                    r += dr
                    c += dc

        # Count unguarded cells
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == ".":
                    count += 1
        print(grid,"sfgfg")
        return count



newObject = Solution()
print(newObject.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))