from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        # max_side = 0
        # for i in range(len(matrix)-1,-1,-1):
        #     for j in range(len(matrix[0])-1,-1,-1):
        #         if matrix[i][j] == "1":
        #             dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        #             max_side = max(max_side,dp[i][j])
        # return max_side**2
    

        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}  # map each (r, c) -> maxLength of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

        #brute force time comlexity is Olen(m * n) ^ 2
        # if not matrix:
        #     return 0
        
        # rows = len(matrix)
        # columns = len(matrix[0])
        # max_square_length = 0

        # def findMaxSquare(i: int, j: int) -> int:
            # if i >= rows or j >= columns:
                # return 0
            
            # Recursively find the maximum square size from right, bottom, and bottom-right neighbors
            # right = findMaxSquare(i, j + 1)
            # bottom = findMaxSquare(i + 1, j)
            # bottom_right = findMaxSquare(i + 1, j + 1)
            
            # if matrix[i][j] == '1':
                # If the current cell is '1', the size of the square is determined by the minimum of the three neighbors + 1
            #     square_size = 1 + min(right, bottom, bottom_right)
            #     nonlocal max_square_length
            #     max_square_length = max(max_square_length, square_size)
            #     return square_size
            # else:
            #     return 0
        
        # Check every cell as a starting point
        # for i in range(rows):
            # for j in range(columns):
                # findMaxSquare(i, j)
        
        # Return the area of the largest square
        # return max_square_length ** 2

      

newObject = Solution()
print(newObject.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))