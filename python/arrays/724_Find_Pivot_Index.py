from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            leftSum = leftSum + nums[i]
        return -1
