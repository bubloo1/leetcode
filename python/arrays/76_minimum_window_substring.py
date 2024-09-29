class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveHashmap,needHashmap = {},{}
        needCharCount = 0
        start = 0
        res = float('inf')
        ans = []

        for i in range(len(t)):
            haveHashmap[t[i]] = 1 + haveHashmap.get(t[i],0)
        
        for j in range(len(s)):
            if s[j] in haveHashmap:
                needHashmap[s[j]] = 1 + needHashmap.get(s[j],0)
                if haveHashmap[s[j]] == needHashmap[s[j]]:
                    needCharCount += 1
                
            while needCharCount == len(haveHashmap):
            
                if res > (j - start):
                    ans = (start,j)
                    res = j - start

                if s[start] in needHashmap:
                    needHashmap[s[start]] -= 1
                    if needHashmap[s[start]] < haveHashmap[s[start]]:
                        needCharCount -= 1
                
                start += 1
            
        return s[ans[0]:ans[1]+1] if res != float('inf') else "" 