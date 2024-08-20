from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def findNextQueenPos(row,col,board):
            rowDup = row
            colDup = col
            
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1


            col = colDup
            row = rowDup
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1


            row = rowDup
            col = colDup
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1

            return True

        board = ["." * n for i in range(n)]
        ans = []
        def solve(col,board):
            if col == n:
                ans.append(list(board))
                return

            for row in range(n):
                if board[row][col] == ".":
                    if findNextQueenPos(row,col,board):
                        board[row] = board[row][:col] + "Q" + board[row][col+1:]
                        solve(col+1,board)
                        board[row] = board[row][:col] + "." + board[row][col+1:]
            return ans
        return solve(0,board)


newObject = Solution()
print(newObject.solveNQueens(5))
