from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False

        sumOfNums = sum(nums)
        targetSum = sumOfNums//k
        visited = set()

        nums.sort()

        def backtrack(index,currTotal,count):
            if count == k:
                return True
            
            if currTotal == targetSum:
                return backtrack(0,0,count + 1)


            for i in range(index,len(nums)):
                # skip duplicates if last same number was skipped
                if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                    continue
                
                if i in visited or currTotal + nums[i] > targetSum:
                    continue

                visited.add(i)

                if backtrack(i,currTotal + nums[i],count):
                    return True
                
                visited.remove(i)
            return False

        return backtrack(0,0,0)