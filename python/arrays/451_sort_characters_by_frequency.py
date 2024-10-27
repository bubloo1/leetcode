
class Solution:
    def frequencySort(self, s: str) -> str:

        char_count = {}
        res = ""
        for i in range(len(s)):

            char_count[s[i]] = 1 + char_count.get(s[i],0)
        
        
        for c in sorted(char_count.items(), key=lambda x:x[1]):
            res += c[0] * c[1]

        return res[::-1]