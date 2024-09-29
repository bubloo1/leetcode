from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close,currStr):
            
            if open == n and close == n:
                res.append(currStr)
                return 
            
            if open < n:
                dfs(open + 1, close, currStr + '(' ) 
            
            if close < open:
                dfs(open, close + 1, currStr + ')' )

            return res
        return dfs(0,0,"")
newObject = Solution()
print(newObject.generateParenthesis(3)) 