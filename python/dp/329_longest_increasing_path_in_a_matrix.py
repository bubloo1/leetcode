from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        maxLen = 0
        dp = [[-1] * columns for i in range(rows)]
       
        def dfs(r,c,prevNum):

            if (r not in range(rows) or c not in range(columns) 
                or matrix[r][c] <= prevNum):
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]      
           
            up = dfs(r + 1, c,matrix[r][c]) 
            down = dfs(r - 1, c,matrix[r][c]) 
            left = dfs(r, c - 1,matrix[r][c]) 
            right = dfs(r, c + 1,matrix[r][c])
            dp[r][c] = 1 + max(up,right,left,down)
            return dp[r][c]

        for r in range(rows):
            for c in range(columns):
                maxLen = max(maxLen,dfs(r,c,float('-inf')))
        return maxLen

newObject = Solution()
print(newObject.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  