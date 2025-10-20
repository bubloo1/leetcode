from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        sizeOfArr = len(arr)
        prevSmaller = [0] * sizeOfArr

        for i in range(sizeOfArr):
            currEle = arr[i] 
            while stack and arr[stack[-1]] > currEle:
                stack.pop()
            prevSmaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        nextSmaller = [0] * sizeOfArr

        for i in range(sizeOfArr-1, -1, -1):
            currEle = arr[i]
            while stack and arr[stack[-1]] >= currEle:
                stack.pop()
            nextSmaller[i] = stack[-1] if stack else sizeOfArr
            stack.append(i)
        res = 0
        for i in range(sizeOfArr):
            left = i - prevSmaller[i]
            right = nextSmaller[i] - i
            res = (res + left * right * arr[i]) % mod
        return res

newObject = Solution()
print(newObject.sumSubarrayMins([3,1,2,4]))