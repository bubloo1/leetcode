class Solution:
    def maxPower(self,s: str):
        # if len(s) <= 1:
        #     return len(s)
        currentCharCount = 0
        maxCharCount = 0
        previousChar = None
        for char in s:
            if previousChar == char:
                currentCharCount += 1
            else:
                currentCharCount = 1
                previousChar = char   
        maxCharCount = max(maxCharCount, currentCharCount) 
        return maxCharCount

sol = Solution()
print(sol.maxPower("cc"))