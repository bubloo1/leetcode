from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def canFormWord(w,letterCount):
            wordCount = Counter(w)
            for c in wordCount:
                if wordCount[c] > letterCount[c]:
                    return False
            return True
        
        def getScore(w):
            res = 0
            for c in w:
                res += score[ord(c) - ord('a')]
            return res
        
        letterCount = Counter(letters)
        # O(2^n * W + L)
        def backtrack(i):
            if i == len(words):
                return 0
            
            res = backtrack(i+1)

            if canFormWord(words[i],letterCount):
                for c in words[i]:
                    letterCount[c] -= 1
                res = max(res,getScore(words[i]) + backtrack(i + 1))
                for c in words[i]:
                    letterCount[c] += 1
            return res
        return backtrack(0)


newObject = Solution()
print(newObject.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))