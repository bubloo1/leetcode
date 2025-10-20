class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # rabin karp algo
        # convert char into number of a certain base (ex: 29)
        # multiply that number with base to move number formard : prefix
        # add char then multiply that base with power we will get same number in reverse : suffix
        prefix = suffix = 0
        base = 29
        lastIndex = 0
        power = 1
        mod = 10**9 + 7

        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1) 

            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                lastIndex = i
        suffix = s[lastIndex+1:]
        return suffix[::-1] + s

sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))

# brute force
# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         def isPalindrome(word, left, right):
#             while left <= right:
#                 if word[left] != word[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True
        
#         for i in range(len(s)-1, -1, -1):
#             if isPalindrome(s, 0, i):
#                 return s[i+1:][::-1] + s
#         return ""