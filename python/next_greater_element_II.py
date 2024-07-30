from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = [-1] * len(nums)
        stack = []

        for i,n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                index = stack.pop()
                res[index] = n 
 
            stack.append(i)
        
        for n in nums:
            while stack and nums[stack[-1]] < n:
                index = stack.pop()
                res[index] = n 

        return res

newObject = Solution()

print(newObject.nextGreaterElements([5,4,3,2,1]))