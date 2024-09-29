from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtracking(index,dot,iPaddress):
            
            if dot == 4 and index == len(s):
                res.append(iPaddress[:-1])
                print("gdfggfdgag")
                return 
            if dot >= 4:
                return 
            
            for i in range(index,min(index + 3,len(s))):
                currStr = int(s[index:i+1])

                if currStr < 256 and (i == index or s[index] != "0"):
                    backtracking(i+1,dot+1,iPaddress + s[index:i+1] + ".")
        backtracking(0,0,"")
        return res

newObject = Solution()
print(newObject.restoreIpAddresses("25525511135"))