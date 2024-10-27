class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
  
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            for j in range(i + 1,len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                start,end =  j + 1,len(nums) - 1
                while start < end:
                    currSum = n + nums[j] + nums[start] + nums[end]
                    if currSum > target:
                        end -= 1
                    elif currSum < target:
                        start += 1
                    else:
                        result.append([n,nums[j],nums[start],nums[end]])
                        start += 1
                        while nums[start] == nums[start - 1] and start < end:
                            start += 1
        return result
 

