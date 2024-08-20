from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


        # wordsDictSet = set(wordDict)
       
        # def backtrack(start):

        #     if start == len(s):
        #         return True

        #     for end in range(start,len(s)):
        #         if s[start:end+1] in wordsDictSet:
                    
        #             if backtrack(end+1):
        #                 return True

        #     return False
        # return backtrack(0)

newObject = Solution()
print(newObject.wordBreak(s = "aaaaaaa", wordDict = ["aaaa","aaa"]))