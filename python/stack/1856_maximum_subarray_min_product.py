from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Prefix Sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # Step 2: Monotonic Stack for Left
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Step 3: Monotonic Stack for Right
        right = [0] * n
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Step 4: Compute max min-product
        max_product = 0
        for i in range(n):
            total = prefix[right[i]] - prefix[left[i] + 1]
            max_product = max(max_product, nums[i] * total)
        
        return max_product % MOD

newObject = Solution()
print(newObject.maxSumMinProduct([1,2,3,2]))
