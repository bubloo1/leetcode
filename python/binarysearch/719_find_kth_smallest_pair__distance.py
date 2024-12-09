from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        def helper(dist):
            # count total number of pairs with diff <= dist
            left = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[left] > dist:
                    left += 1
                res += r - left
            
            return res
        
        left,right = 0, max(nums)
        while left < right:
            m = left + ((right - left)//2)
            pairs = helper(m)
            if pairs >= k:
                right = m
            else:
                left = m + 1
        return right
        