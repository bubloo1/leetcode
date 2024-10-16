from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        currMin = nums[0]
        

        for n in nums[1:]:

            while stack and stack[-1][0] <= n:
                stack.pop()

            if stack and n > stack[-1][1] :
                return True
            
            stack.append([n,currMin])
            currMin = min(n,currMin)
        return False

newObject = Solution()
print(newObject.find132pattern([3,1,4,2]))




        