from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
        
            stack.append(n)
        
        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip('0')
        return res if res else "0"


newObject = Solution()

print(newObject.removeKdigits(num = "1432219", k = 3))

