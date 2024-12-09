class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
    
        lenOfString = len(t)
        if lenOfString < 2:
            return True
        if lenOfString % k != 0:
            return False
        noOfParts = lenOfString//k
       
        tStrHashMap = {}
        for i in range(0,lenOfString,noOfParts):
            tStrHashMap[t[i:i + noOfParts]] = 1 + tStrHashMap.get(t[i:i + noOfParts],0)
      
        for j in range(0,lenOfString,noOfParts):
            if s[j:j+noOfParts] not in tStrHashMap or  tStrHashMap[s[j:j+noOfParts]] < 1:
                return False
            tStrHashMap[s[j:j + noOfParts]] -= 1
        
        return True

newObject = Solution()
print(newObject.isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3))

