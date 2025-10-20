from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0
        
        res = len(nums)
        currSum = 0

        remainToIdx = {0:-1}
        
        for i, n in enumerate(nums):
            # x = currSum - remain
            currSum = (currSum + n) % p
            prefix = (currSum - remain + p) % p
            if prefix in remainToIdx:
                length = i - remainToIdx[prefix]
                res = min(res, length)
            remainToIdx[currSum] = i
        return -1 if res == len(nums) else res
ss = Solution()
print(ss.minSubarray([3,1,4,2],6))

 