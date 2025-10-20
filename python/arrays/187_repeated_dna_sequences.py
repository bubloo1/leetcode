from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dnaSeqSet = set()
        dnaSeqSet.add(s[0:10])
        left = 1
        res = set()

        for right in range(10,len(s)):
            curr = s[left:right + 1]
            if curr in dnaSeqSet:
                res.add(curr)
            dnaSeqSet.add(curr)
            left += 1

        return list(res)


newObject = Solution()
print(newObject.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))