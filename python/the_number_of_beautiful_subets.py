from typing import List
from collections import defaultdict
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(i,count):
            if i==len(nums):
                return 1

            res = backtrack(i+1,count)
            if not count[nums[i]+k] and not count[nums[i]-k]:
                count[nums[i]]+=1
                res+=backtrack(i+1,count)
                count[nums[i]]-=1
            print(count)
            return res
        
        return backtrack(0,defaultdict(int))-1

newObject = Solution()
print(newObject.beautifulSubsets([2,4,6],2))
