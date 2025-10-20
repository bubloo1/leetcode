from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixIndex = {0: -1}  # sum -> first index
        maxLen = 0
        prefixSum = 0

        for i, num in enumerate(nums):
            prefixSum += 1 if num == 1 else -1

            if prefixSum in prefixIndex:
                maxLen = max(maxLen, i - prefixIndex[prefixSum])
            else:
                prefixIndex[prefixSum] = i

        return maxLen


newObject = Solution()
print(newObject.findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))