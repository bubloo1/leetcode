from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        nums.sort()
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            start,end = i + 1, len(nums) - 1
            while start < end:
                currentSum = n + nums[start] + nums[end]
                if currentSum > 0:
                    end -= 1
                
                elif currentSum < 0:
                    start += 1
                else:
                    answer.append([n,nums[start],nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return answer
