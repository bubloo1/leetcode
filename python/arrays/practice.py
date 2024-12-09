
from typing import List
from collections import defaultdict
class Solution:  
    def minOperations(self, nums: List[int], k: int) -> int:

        numsSet = set(nums)
        count = 0

        for i,val in enumerate(numsSet):
            if val > k:
                count+= 1
            elif val < k:
                return -1
        return count


newObject = Solution()
print(newObject.minOperations(nums = [9,7,5,3], k = 1))

# [5,2,5,4,5]

# [4,2,4,4,4]

# [2,2,2,2,2]