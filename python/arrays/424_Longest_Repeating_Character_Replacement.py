class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = {}
        start = 0
        maxCharCount = res  = 0
        for i in range(len(s)):
            charCount[s[i]] = 1 + charCount.get(s[i],0)
            maxCharCount = max(maxCharCount,charCount[s[i]])

            if (i - start + 1) - maxCharCount > k:
                charCount[s[start]] -= 1
                start += 1
            
            res = max(res, i - start + 1)
        return res