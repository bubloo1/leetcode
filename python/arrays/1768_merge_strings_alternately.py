class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left1 = left2 = 0
        res = ""
        while left1 < len(word1) and len(word2):
            res = res + word1[left1]
            res = res + word2[left2]
            left1 += 1
            left2 += 1
        
        res = res + word1[left1:]
        res = res + word2[left2:]

        return res




newObject = Solution()

print(newObject.mergeAlternately(word1 = "abc", word2 = "pqr"))