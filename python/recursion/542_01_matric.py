from typing import List
from collections import deque

class Solution:
    def updateMatrix(mat):
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Initialize the queue with all 0's and set their distance to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # Directions for moving in the matrix (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # BFS to update distances
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # If this cell has not been visited (distance is infinity)
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))

        return dist


newObject = Solution()
print(newObject.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))