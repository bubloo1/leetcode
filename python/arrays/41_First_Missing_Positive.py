from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # smallestNumber = 1
        # lenOfNums = len(nums)
        # for i in range(lenOfNums):
        #     if nums[i] < 1:
        #         continue
        #     elif i < lenOfNums - 1 and nums[i] == nums[i+1]:
        #         continue
        #     elif nums[i] > smallestNumber:
        #         return smallestNumber
        #     smallestNumber += 1

        # return nums[lenOfNums-1] + 1 if nums[lenOfNums - 1] > 0  else 1

        n = len(nums)

        # Step 1: Convert all negative numbers and zeros to n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
    
        # Step 2: Mark the numbers that are present by negating the corresponding index
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
    
        # Step 3: Find the first positive number's index
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Step 4: If all numbers are present, return n+1
        return n + 1