class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        orderedSeq = 0
        if len(s) > len(t):
            return False
        elif(len(s) == 0):
            return True
        else:
            for i in range(len(t)):
                if orderedSeq < len(s) and s[orderedSeq] == t[i]:
                    orderedSeq += 1
                
        return orderedSeq == len(s)