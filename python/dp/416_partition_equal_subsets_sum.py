from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        targetSum = sum(nums)

        if targetSum % 2:
            return False
        
        targetSum = targetSum//2
        
        dp = set()
        dp.add(0)


        for i in range(len(nums) - 1, -1,-1):
            currDp = set()
            for currTotal in dp:
                if(currTotal + nums[i]) == targetSum:
                    return True
                currDp.add(currTotal + nums[i])
                currDp.add(currTotal)
            dp = currDp
        return False


        # if sum(nums) % 2:
        #     return False
        
        # targetSum = sum(nums)//2

        # def dfs(i,currSum):
 
        #     if currSum == targetSum:
        #         return True
            
        #     if i >= len(nums) or currSum > targetSum:
        #         return False
            
        #     if dfs(i + 1,currSum + nums[i]):
        #         return True
            
        #     if dfs(i + 1,currSum):
        #         return True
        #     return False
        # return dfs(0,0)

newObject = Solution()
print(newObject.canPartition([1,5,11,5]))