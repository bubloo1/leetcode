from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:


        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        
        # Mark the entrance as visited
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        while queue:
            row, col, steps = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within the maze bounds and is an empty space
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.':
                    # If it's at the border and not the entrance, we found the nearest exit
                    if (new_row in [0, rows - 1] or new_col in [0, cols - 1]) and [new_row, new_col] != entrance:
                        return steps + 1
                    
                    # Mark this cell as visited and add to the queue for further exploration
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, steps + 1))
        
        # If no exit was found
        return -1
        # getting time limit exceeded
        # rows = len(maze)
        # cols = len(maze[0])
        # visited = set()
        # def dfs(r,c, shortestPath):


        #     if(r not in range(rows) or c not in range(cols) or (r,c) 
        #         in visited or maze[r][c] == "+"):
        #         return float("inf")

        #     if (r in [0, rows-1] or c in [0,cols-1]) and [r,c] != entrance:
        #         return shortestPath

        #     visited.add((r,c))
        #     res = float("inf")
        #     res = min(res,dfs(r + 1,c,shortestPath + 1))
        #     res = min(res,dfs(r - 1,c,shortestPath + 1))
        #     res = min(res,dfs(r,c + 1,shortestPath + 1))
        #     res = min(res,dfs(r,c - 1,shortestPath + 1))   
        #     visited.remove((r,c))

        #     return res
        # ans = dfs(entrance[0],entrance[1],0) 
        # return ans if ans != float("inf") else -1
newObject = Solution()
print(newObject.nearestExit([[".","+","."]], entrance = [0,2]))