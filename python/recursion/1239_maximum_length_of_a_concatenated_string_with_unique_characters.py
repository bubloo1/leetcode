from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(string):
            currSet = set()

            for char in string:
                if char in charSet or char in currSet:
                    return True
                currSet.add(char)
            return False

        def backtrack(i):

            if len(arr) == i:
                return len(charSet)
            res = 0
            if not overlap(arr[i]):
                for char in arr[i]:
                    charSet.add(char)
                
                res = backtrack(i + 1)
                for char in arr[i]:
                    charSet.remove(char)
            return max(res,backtrack(i+1))
        return backtrack(0)

newObject = Solution()
print(newObject.maxLength(["un","iq","ue"]))