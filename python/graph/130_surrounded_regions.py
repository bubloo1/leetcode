from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(r,c):

            if (r not in range(rows-1) or c not in range(cols-1) or (r,c) in visited or board[r][c] == "X"):
                return
            
            visited.add((r,c))
            board[r][c] = "X"
           
            dfs(r,c+1)
            dfs(r,c - 1)
            dfs(r + 1,c)
            dfs(r - 1,c)


        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if board[r][c] == "O":
                    dfs(r,c)
                    print(board)
