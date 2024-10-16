class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelsSet = set(['a','e','i','o','u'])
        vowelsCount = 0
        maxVowelsCount = 0
        l = 0

        for r,char in enumerate(s):
            if char in vowelsSet:
                vowelsCount += 1
            if (r - l + 1) > k:
                if s[l] in vowelsSet:
                    vowelsCount -= 1
                l += 1
            maxVowelsCount = max(maxVowelsCount,vowelsCount)

        return maxVowelsCount

newObject = Solution()
print(newObject.maxVowels(s = "abciiidef", k = 3))