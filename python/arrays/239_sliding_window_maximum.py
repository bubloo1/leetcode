from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - 3):
            currMaxValue = float('-inf')
            for j in range(i,min(i + 3,len(nums))):
                currMaxValue = max(currMaxValue,nums[j])
            res.append(currMaxValue)
        return res
    

newObject = Solution()
print(newObject.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
