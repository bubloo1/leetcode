from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        lastSmallest = float('-inf')
        maxLength , length = 0,1 
        for i,n in enumerate(nums):
            if n - 1 == lastSmallest: 
                lastSmallest = n
                length += 1
            else:
                maxLength = max(length,maxLength)
                length = 1
                lastSmallest = n
        return maxLength


newObject = Solution()
print(newObject.longestConsecutive([100,4,200,1,3,2]))