from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #using prefix and postfix
        res = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
    
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res

        # brute force O(n^2)
        # res = [0 for i in range(len(nums))] 
        
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         product *= nums[j]
        #     res[i] = product
        
        # return res
    
newObject = Solution()
print(newObject.productExceptSelf([1,2,3,4]))