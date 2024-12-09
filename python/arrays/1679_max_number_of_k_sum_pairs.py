from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()
        pairs = 0

        for num in nums:
            complement = k - num
            if count[complement] > 0:
                pairs += 1
                count[complement] -= 1
            else:
                count[num] += 1
                
        return pairs
    
        # two pointers technic without extra memory
        # nums.sort()
        # left, right = 0, len(nums) - 1
        # pairs = 0

        # while left < right:
        #     s = nums[left] + nums[right]
        #     if s == k:
        #         pairs += 1
        #         left += 1
        #         right -= 1
        #     elif s < k:
        #         left += 1
        #     else:
        #         right -= 1
                
        # return pairs





newObject = Solution()
print(newObject.maxOperations(nums = [1,2,3,4], k = 5))